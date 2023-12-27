#!/usr/bin/env python3

# standard libraries
import datetime as dt
import glob
import logging
import math
import os
import shutil
import subprocess
import sys
from collections import deque
from pathlib import Path
from threading import Thread
from typing import List, Tuple

# third party libraries
from pyhashxx import hashxx

# rubiks cube libraries
from rubikscubennnsolver.misc import (
    parse_ascii_222,
    parse_ascii_333,
    parse_ascii_444,
    parse_ascii_555,
    parse_ascii_666,
    parse_ascii_777,
)
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, moves_222, rotate_222, solved_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, moves_333, rotate_333, solved_333
from rubikscubennnsolver.RubiksCube444 import (
    RubiksCube444,
    centers_444,
    edges_444,
    edges_recolor_pattern_444,
    moves_444,
    rotate_444,
    solved_444,
    wings_for_edges_recolor_pattern_444,
)
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    centers_555,
    edges_555,
    edges_recolor_pattern_555,
    moves_555,
    rotate_555,
    solved_555,
    wings_for_edges_pattern_555,
)
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, moves_666, rotate_666, solved_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, moves_777, rotate_777, solved_777

log = logging.getLogger(__name__)
supported_sizes = ("2x2x2", "3x3x3", "4x4x4", "5x5x5", "6x6x6", "7x7x7")

WRITE_BATCH_SIZE = 1000000
LOG_BATCH_SIZE = 1000000

# SLOW_TMP = Path("/storage/dwalton76/tmp/")
# FAST_TMP = Path("/bigssd/lz4/tmp/")
SLOW_TMP = Path("lookup-tables")
FAST_TMP = Path("./tmp/")


def get_line_number_splits(lines: int, cores: int) -> Tuple:
    """
    >>> get_line_number_splits(100, 1)
    ((0, 99),)

    >>> get_line_number_splits(100, 2)
    ((0, 49), (50, 99))

    >>> get_line_number_splits(100, 5)
    ((0, 19), (20, 39), (40, 59), (60, 79), (80, 99))

    >>> get_line_number_splits(100, 3)
    ((0, 32), (33, 65), (66, 99))

    >>> get_line_number_splits(10, 3)
    ((0, 2), (3, 5), (6, 9))
    """
    assert isinstance(lines, int)
    assert isinstance(cores, int)
    assert lines > 0
    assert cores > 0

    lines_per_core = math.trunc(lines / cores)
    start = 0
    results = []
    log.debug("lines %d, cores %d, lines_per_core %d" % (lines, cores, lines_per_core))

    if lines_per_core == 0:
        for core in range(cores):
            if core == 0:
                start = 0
                end = lines - 1
            else:
                start = None
                end = None
            results.append((start, end))

    else:
        for core in range(cores):
            # The last core ends at linecount
            if core == cores - 1:
                end = lines - 1
            else:
                end = start + lines_per_core - 1

            log.debug("core %d, start %d, end %d" % (core, start, end))
            results.append((start, end))
            start = end + 1

    log.debug("\n")
    return tuple(results)


def reverse_steps(steps: List[str]) -> List[str]:
    """
    >>> reverse_steps([])
    []

    >>> reverse_steps(["U"])
    ["U'"]

    >>> reverse_steps(["U", "R'", "D2"])
    ['D2', 'R', "U'"]
    """
    return [step if step[-1] == "2" else step[0:-1] if step[-1] == "'" else step + "'" for step in reversed(steps)]


def convert_state_to_hex(state: str) -> str:
    """
    This assumes that state only has "x"s and Us or Ls or Fs or Rs or Bs or Ds

    >>> convert_state_to_hex("xxxU")
    '1'

    >>> convert_state_to_hex("UxUx")
    'a'

    >>> convert_state_to_hex("UUxUx")
    '1a'
    """
    state = (
        state.replace("x", "0")
        .replace("-", "0")
        .replace("U", "1")
        .replace("L", "1")
        .replace("F", "1")
        .replace("R", "1")
        .replace("B", "1")
        .replace("D", "1")
    )
    hex_width = int(math.ceil(len(state) / 4.0))
    hex_state = hex(int(state, 2))[2:]

    if hex_state.endswith("L"):
        hex_state = hex_state[:-1]

    return hex_state.zfill(hex_width)


def convert_to_cost_only(filename: str) -> None:
    filename_new = filename.replace(".txt", ".cost-only.txt")
    prev_state_int = None

    with open(filename, "r") as fh:
        with open(filename_new, "w") as fh_new:
            for line_number, line in enumerate(fh):
                (state, steps) = line.strip().split(":")
                steps = steps.split()
                state_int = int(state, 16)
                # log.info("%s: state_int %d" % (state, state_int))

                # Add 0s for every state from prev_state_int to state_int
                if prev_state_int is None:
                    zeroes_between_prev_and_now = state_int
                else:
                    zeroes_between_prev_and_now = state_int - prev_state_int - 1

                if zeroes_between_prev_and_now > 0:
                    # log.info("zeroes_between_prev_and_now %s" % zeroes_between_prev_and_now)
                    zeroes_between_prev_and_now = zeroes_between_prev_and_now * "0"
                    fh_new.write(zeroes_between_prev_and_now)

                # Write the steps_len
                if steps and steps[0].isdigit():
                    steps_len = int(steps[0])
                else:
                    steps_len = len(steps)

                # We save the steps_len as a single hex character so cap it at 15
                if steps_len > 15:
                    log.warning("steps_len %d is > 15...saving as 15" % steps_len)
                    steps_len = 15

                # Convert steps_len to hex and ignore the 0x part of the string
                steps_len = hex(steps_len)[2]
                fh_new.write(steps_len)
                prev_state_int = state_int


def convert_to_hash_cost_only(filename: str, bucketcount: int) -> None:
    filename_new = filename.replace(".txt", ".hash-cost-only.txt")

    bucket = bytearray(bucketcount)
    collisions = 0

    with open(filename, "r") as fh:
        for line_number, line in enumerate(fh):
            (state, steps) = line.strip().split(":")
            steps = steps.split()

            hash_raw = hashxx(state.encode("utf-8"))
            hash_index = int(hash_raw % bucketcount)

            # Write the steps_len
            if steps[0].isdigit():
                steps_len = int(steps[0])
            else:
                steps_len = len(steps)

            # log.info("state: %s, hash_index %s, steps_len %s" % (state, hash_index, steps_len))

            if not bucket[hash_index]:
                bucket[hash_index] = steps_len
            else:
                collisions += 1

                if bucket[hash_index] > steps_len:
                    bucket[hash_index] = steps_len

            if line_number % 1000000 == 0:
                log.info(line_number)
            # if line_number >= 1000:
            #    break

    log.info("%d collisions" % collisions)
    log.info(f"begin writing {filename_new}")
    with open(filename_new, "w") as fh_new:
        to_write = []

        for index, x in enumerate(bucket):
            if x > 15:
                to_write.append("f")
            else:
                # Convert steps_len to hex and ignore the 0x part of the string
                to_write.append(hex(x)[2])

            if index % 100000 == 0:
                fh_new.write("".join(to_write))
                to_write = []

        if to_write:
            fh_new.write("".join(to_write))

        fh_new.write("\n")
    log.info(f"end writing {filename_new}")


def parse_histogram(filename: str) -> str:
    if not os.path.exists("histogram.txt"):
        print("\n\nERROR: histogram.txt does not exist")
        sys.exit(1)

    with open("histogram.txt", "r") as fh:
        found_filename = False
        histogram = []
        linecount = 0
        max_depth = 0

        for line in fh:
            line = line.strip()

            if not found_filename and line == filename:
                found_filename = True
                line = line.replace("lookup-tables/", "")
                histogram.append("    " + line)
                log.info(line)

            elif found_filename:
                if line.startswith("===="):
                    line = line[len("lookup-tables/") :]

                histogram.append("    " + line)
                log.info(line)

                if "steps has" in line:
                    max_depth = int(line.split()[0])
                elif line.startswith("Total:"):
                    linecount = int(line.split()[1].replace(",", ""))
                elif line.startswith("Average"):
                    break

    if not found_filename:
        print(f"\n\nERROR: {filename} is not in histogram.txt")
        sys.exit(0)

    return ("\n".join(histogram), linecount, max_depth)


def get_starting_states(filename, class_name, hex_digits):
    """
    TODO hex_digits needs to be the number of hex characters in the state
    """
    ss_filename = "starting-states-" + filename

    if not os.path.exists(ss_filename):
        print(f"\n\nERROR: {ss_filename} does not exist. run:")
        print(f"\n./builderui.py {class_name.replace('LookupTable', 'StartingStates')}\n")
        sys.exit(1)

    with open(ss_filename, "r") as fh:
        result = []
        for line in fh:
            line = line.strip()
            line = line.replace(" 'ULFRBD'),", "")
            line = line.replace("(", "")
            line = line.replace(".", "")
            line = line.replace(",", "")

            if hex_digits:
                line = (
                    line.replace("x", "0")
                    .replace("U", "1")
                    .replace("L", "1")
                    .replace("F", "1")
                    .replace("R", "1")
                    .replace("B", "1")
                    .replace("D", "1")
                )
                line = line.replace("'", "")
                line = line.replace(",", "")
                hex_format = "TBD_HEX_FORMAT"
                result.append("             '" + hex_format % int(line, 2) + "'")
            else:
                result.append(f"{line}")

        result.sort()

        if len(result) < 100:
            result = "(" + ",\n             ".join(result) + ")"
        else:
            pass
        return result


class BackgroundProcess(Thread):
    def __init__(self, cmd, desc):
        Thread.__init__(self)
        self.cmd = cmd
        self.desc = desc
        self.result = None
        self.ok = False

    def __str__(self):
        return self.desc

    def run(self):
        log.debug(f"Running {' '.join(self.cmd)}")
        try:
            self.result = subprocess.check_output(self.cmd)

            if self.result is not None and self.result.isdigit():
                self.result = int(self.result)
            self.ok = True
        except subprocess.CalledProcessError as e:
            self.ok = False
            self.result = e.output.decode("utf-8")


class BFS(object):
    """
    Base class for all classes that build lookup tables
    """

    def __init__(
        self,
        name,
        illegal_moves,
        size,
        filename,
        store_as_hex,
        starting_cube_states,
        use_cost_only=False,
        use_hash_cost_only=False,
        use_edges_pattern=False,
        legal_moves=None,
        rotations=[],
        use_centers_then_edges=False,
        use_c=False,
    ):
        self.name = name
        self.illegal_moves = illegal_moves
        self.size = size

        if SLOW_TMP:
            self.filename = str(SLOW_TMP / filename)
        else:
            self.filename = filename

        self.store_as_hex = store_as_hex
        self.starting_cubes = []
        self.use_cost_only = use_cost_only
        self.use_hash_cost_only = use_hash_cost_only
        self.use_edges_pattern = use_edges_pattern
        self.starting_cube_states = starting_cube_states
        self.rotations = rotations
        self.use_centers_then_edges = use_centers_then_edges
        self.lt_centers = {}
        self.lt_centers_max_depth = None
        self.use_c = use_c

        assert isinstance(self.name, str)
        assert isinstance(self.illegal_moves, tuple)
        assert self.size in supported_sizes, f"{self.size} not supported"
        assert isinstance(self.filename, str)
        assert isinstance(self.store_as_hex, bool)
        assert isinstance(starting_cube_states, tuple)
        assert isinstance(self.use_cost_only, bool)
        assert isinstance(self.use_hash_cost_only, bool)
        assert not (self.use_cost_only and self.use_hash_cost_only), "Both cannot be true"

        if size == "2x2x2":
            self.all_moves = moves_222
            self.rotate_xxx = rotate_222
            self.cube = RubiksCube222(solved_222, order="URFDLB")

            for state, order in starting_cube_states:
                if order == "ascii":
                    state = parse_ascii_222(state)
                    order = "ULFRBD"
                self.starting_cubes.append(RubiksCube222(state, order))

        elif size == "3x3x3":
            self.all_moves = moves_333
            self.rotate_xxx = rotate_333
            self.cube = RubiksCube333(solved_333, order="URFDLB")

            for state, order in starting_cube_states:
                if order == "ascii":
                    state = parse_ascii_333(state)
                    order = "ULFRBD"
                self.starting_cubes.append(RubiksCube333(state, order))

        elif size == "4x4x4":
            self.all_moves = moves_444
            self.rotate_xxx = rotate_444
            self.cube = RubiksCube444(solved_444, order="URFDLB")

            for state, order in starting_cube_states:
                if order == "ascii":
                    state = parse_ascii_444(state)
                    order = "ULFRBD"
                self.starting_cubes.append(RubiksCube444(state, order))

        elif size == "5x5x5":
            self.all_moves = moves_555
            self.rotate_xxx = rotate_555
            self.cube = RubiksCube555(solved_555, order="URFDLB")

            for state, order in starting_cube_states:
                if order == "ascii":
                    state = parse_ascii_555(state)
                    order = "ULFRBD"
                self.starting_cubes.append(RubiksCube555(state, order))

        elif size == "6x6x6":
            self.all_moves = moves_666
            self.rotate_xxx = rotate_666
            self.cube = RubiksCube666(solved_666, order="URFDLB")

            for state, order in starting_cube_states:
                if order == "ascii":
                    state = parse_ascii_666(state)
                    order = "ULFRBD"
                self.starting_cubes.append(RubiksCube666(state, order))

        elif size == "7x7x7":
            self.all_moves = moves_777
            self.rotate_xxx = rotate_777
            self.cube = RubiksCube777(solved_777, order="URFDLB")

            for state, order in starting_cube_states:
                if order == "ascii":
                    state = parse_ascii_777(state)
                    order = "ULFRBD"
                self.starting_cubes.append(RubiksCube777(state, order))

        # Print all starting cubes
        if len(self.starting_cubes) < 200:
            for cube in self.starting_cubes:
                cube.print_cube("starting cube")

        # Build list of legal moves from allmoves minus illegal moves
        if legal_moves:
            self.legal_moves = legal_moves
        else:
            self.legal_moves = []

            for move in self.all_moves:
                if move not in self.illegal_moves:
                    self.legal_moves.append(move)

        # self.legal_moves = sorted(self.legal_moves)
        log.info(f"all moves     : {' '.join(self.all_moves)}")
        log.info(f"illegal moves : {' '.join(self.illegal_moves)}")
        log.info(f"legal moves   : {' '.join(self.legal_moves)}")
        self.bucketcount = 0
        self.size_number = int(self.size[0])
        self.workq_line_length = self.get_workq_line_length()

        self.time_in_sort = 0
        self.time_in_file_delete = 0
        self.time_in_building_workq = 0
        self.time_in_crunching_workq = 0
        self.time_in_save = 0
        self.time_in_find_new_states = 0
        self.time_in_keep_best_solution = 0

    def __str__(self):
        return self.name

    def get_workq_line_length(self):
        """
        When building the workq file make each line the same length (pad with spaces)
        this way the cruncher can jump right to its start line instead of wasting cycles
        looping over each line until it reaches start.

        How much to pad?
        - 1 for the leading x
        - number of squares on cube
        - 1 for the : seperator
        - 5 chars for each step...figure max of 20 steps on a line would be plenty
        """
        LEADING_X = 1
        SIDES_PER_CUBE = 6
        SEPERATORS = 2
        CHARS_PER_STEP = 5
        MAX_STEPS = 20
        EDGES_STATE = 36
        WIGGLE_ROOM = 50

        if self.name.startswith("5x5x5-edges"):
            return 512
        else:
            return (
                LEADING_X
                + (SIDES_PER_CUBE * self.size_number * self.size_number)
                + SEPERATORS
                + (CHARS_PER_STEP * MAX_STEPS)
                + EDGES_STATE
                + WIGGLE_ROOM
            )

    def get_workq_filename_for_core(self, core):
        return "%s.core-%d" % (self.workq_filename, core)

    def rm_per_core_workq_results_files(self):
        # These are the per-core files in tmp where the results of builder-crunch-workq are written
        for core in range(self.cores):
            filename = self.get_workq_filename_for_core(core)

            if os.path.isfile(filename):
                os.remove(filename)

    def log_table_stats(self):
        states_per_depth = ""
        total = 0

        for i in sorted(self.stats)[1:]:
            total += self.stats[i]

        for i in sorted(self.stats)[1:]:
            if self.stats[i - 1]:
                delta = float(self.stats[i] / self.stats[i - 1])
            else:
                delta = float(0)

            if self.stats[i]:
                states_per_depth += "    {} steps has {:,} entries ({} percent, {:.2f}x previous step)\n".format(
                    i, self.stats[i], int(float(self.stats[i] / total) * 100), delta
                )

        states_per_depth += f"    Total: {total:,} entries"
        log.info("\n\n" + states_per_depth + "\n\n")

    def _search_setup(self):
        """
        Prep work needed before we start our BFS
        """
        # We will write the workq to a file in a local tmp directory
        self.workq_filename = os.path.join(FAST_TMP, f"{self}.workq.txt")
        self.workq_filename_next = self.workq_filename + ".next"
        self.workq_size = 0
        self.depth = 1

        # We are starting from scratch so for each starting_cube loop over all legal moves
        # and add that tuple to the workq
        log.info("setup: starting from scratch")

        # If we crashed delete all of the files we had created
        for filename in (self.workq_filename_next, self.workq_filename, self.filename):
            if os.path.isfile(filename):
                os.remove(filename)

        self.rm_per_core_workq_results_files()

        if self.use_edges_pattern:
            pattern = None

            if self.size == "4x4x4":
                # pattern = "10425376a8b9ecfdhgkiljnm"
                if self.filename.endswith("lookup-table-4x4x4-step32-first-four-edges.txt"):
                    pattern = "--------a8b9ecfd--------"
                elif self.filename.endswith("lookup-table-4x4x4-step42-last-eight-edges.txt"):
                    pattern = "10425376--------hgkiljnm"

            elif self.size == "5x5x5":
                if self.filename.endswith("lookup-table-5x5x5-step53-phase5-high-edge-and-midge.txt"):
                    pattern = "-------------SSTT--UUVV-------------"

                elif self.filename.endswith("lookup-table-5x5x5-step54-phase5-low-edge-and-midge.txt"):
                    pattern = "------------sS--TtuU--Vv------------"

                elif self.filename.endswith("lookup-table-5x5x5-step501-pair-last-eight-edges-edges-only.txt"):
                    pattern = "OOopPPQQqrRR------------WWwxXXYYyzZZ"

                elif self.filename.endswith("lookup-table-5x5x5-step62-phase6-high-edge-midge.txt"):
                    pattern = "OO--PPQQ--RR------------WW--XXYY--ZZ"

                elif self.filename.endswith("lookup-table-5x5x5-step63-phase6-low-edge-midge.txt"):
                    pattern = "-OopP--QqrR--------------WwxX--YyzZ-"

            if pattern is None:
                raise Exception(f"implement edges-pattern for {self.size} {self.filename}")
        else:
            pattern = ""

        with open(self.workq_filename, "w") as fh_workq, open(self.filename, "w") as fh:
            for cube in self.starting_cubes:
                log.info(f"starting cube {''.join(cube.state).replace('.', '')[1:]}")
                if self.use_edges_pattern:
                    workq_line = f"{pattern}:{''.join(cube.state)}:"
                else:
                    workq_line = f"{''.join(cube.state)}:"

                fh.write(workq_line + "\n")
                fh_workq.write(workq_line + " " * (self.workq_line_length - len(workq_line)) + "\n")
                self.workq_size += 1

        self.starting_cubes = []

    def _sort_merge_state_files(self, files_to_sort, sorted_results_filename):
        log.info(f"sort {len(files_to_sort)} files created by builder-crunch-workq processes begin")
        start_time = dt.datetime.now()

        # create a file with the list of the filenames to sort
        files_to_sort_filename = f"{FAST_TMP}/files_to_sort.txt"
        with open(files_to_sort_filename, "w") as fh:
            fh.write("\0".join(files_to_sort))

        # find state_width by reading the first line of the first file
        first_file = files_to_sort[0]

        with open(first_file, "r") as fh:
            line = next(fh)

            if line.count(":") == 1:
                state = line.split(":")[0]
            elif line.count(":") == 2:
                (state1, state2, steps) = line.split(":")
                state = ":".join([state1, state2])
            else:
                raise Exception(f"Found {line.count(':')} :s in line:\n{line}")

            state_width = len(state)

        cmd = (
            "LC_ALL=C nice sort --batch-size=1000 --parallel=%d --uniq --key=1.1,1.%d  --merge --temporary-directory=%s --output %s --files0-from=%s"
            % (self.cores, state_width, FAST_TMP, sorted_results_filename, files_to_sort_filename)
        )
        # log.info(cmd)

        subprocess.check_output(cmd, shell=True)
        self.time_in_sort += (dt.datetime.now() - start_time).total_seconds()
        os.unlink(files_to_sort_filename)
        # linecount = int(subprocess.check_output("wc -l %s" % sorted_results_filename, shell=True).decode("ascii").strip().split()[0])
        # log.info("sort all of the files created by builder-crunch-workq processes end ({:,} lines)".format(linecount))
        log.info(f"sort {len(files_to_sort)} files created by builder-crunch-workq processes end")

    def rm_files(self, filenames: List[str]):
        log.info("rm builder-crunch-workq output files begin")
        start_time = dt.datetime.now()
        for filename in filenames:
            os.unlink(filename)
        self.time_in_file_delete += (dt.datetime.now() - start_time).total_seconds()
        log.info("rm builder-crunch-workq output files end")

    def _search_launch_builder_crunch_workq_per_core(self):
        """
        Launch one builder-crunch-workq process per core. Wait for all of them
        to complete before returning.
        """
        start_time = dt.datetime.now()

        MILLION = 1000000
        BILLION = 1000 * MILLION
        BATCH_SIZE = BILLION
        batch_count = int(self.workq_size / BATCH_SIZE) + 1
        workq_size = self.workq_size

        for batch_index in range(batch_count):
            log.info(f"builder-crunch-workq begin batch {batch_index+1}/{batch_count}")
            threads = []
            line_numbers_for_cores = get_line_number_splits(min(workq_size, BATCH_SIZE), self.cores)
            line_number_offset = batch_index * BATCH_SIZE

            # Launch one builder-crunch-workq process per core
            # - each one will process a subsection of workq_filename_next
            # - wait for all of them to finish before we move on
            for core in range(self.cores):
                (start, end) = line_numbers_for_cores[core]

                if start is None:
                    continue

                start += line_number_offset
                end += line_number_offset

                if self.use_c:
                    # fmt: off
                    cmd = [
                        "nice",
                        "./rubikscubelookuptables/builder-crunch-workq",
                        "--size", self.size[0],
                        "--inputfile", self.workq_filename,
                        "--linewidth", str(self.workq_line_length + 1),
                        "--start", str(start),
                        "--end", str(end),
                        "--outputfile", self.get_workq_filename_for_core(core),
                        "--moves", f"{' '.join(self.legal_moves)}",
                    ]
                    # fmt: on

                else:
                    cmd = [
                        "nice",
                        "./rubikscubelookuptables/builder-crunch-workq.py",
                        self.size,
                        self.workq_filename,
                        str(self.workq_line_length),
                        str(start),
                        str(end),
                        self.get_workq_filename_for_core(core),
                        f"{' '.join(self.legal_moves)}",
                    ]

                if self.use_edges_pattern:
                    cmd.append("--use-edges-pattern")

                log.info(" ".join(cmd))

                thread = BackgroundProcess(cmd, "builder-crunch-workq core %d" % core)
                thread.start()
                threads.append(thread)

            hit_error = False
            for thread in threads:
                thread.join()

                if thread.ok:
                    log.info("depth %d %s: finished" % (self.depth, thread))
                else:
                    hit_error = True
                    log.info("depth %d %s: finished but with an error\n%s\n" % (self.depth, thread, thread.result))

            if hit_error:
                log.error("builder-crunch-workq hit an error")
                sys.exit(1)

            if workq_size > BATCH_SIZE:
                workq_size -= BATCH_SIZE
            else:
                workq_size = 0

            log.info(f"builder-crunch-workq end batch {batch_index+1}/{batch_count}")

            sorted_results_filename = f"{self.filename}-batch-{batch_index}"
            core_files = sorted(glob.glob(f"{FAST_TMP}/*core*"))
            self._sort_merge_state_files(core_files, sorted_results_filename)
            self.rm_files(core_files)

        self.time_in_crunching_workq += (dt.datetime.now() - start_time).total_seconds()

    def _search_process_builder_crunch_workq_results(self, max_depth):
        """
        Process the results from all of the builder-crunch-workq processes
        and build a new workq_filename_next
        """
        to_write = []
        to_write_count = 0
        workq_line_length = self.workq_line_length
        self.workq_size = 0
        sorted_results_filename = f"{self.workq_filename}.10-results"

        # Remove the workq file to save some disk space
        if os.path.exists(self.workq_filename):
            os.remove(self.workq_filename)

        batch_files = sorted(glob.glob(f"{self.filename}-batch*"))

        if len(batch_files) == 1:
            shutil.move(batch_files[0], sorted_results_filename)
        else:
            self._sort_merge_state_files(batch_files, sorted_results_filename)
            self.rm_files(batch_files)

        # Use "builder-find-new-states.py" to find the entries in the .results file that are not
        # in our current lookup-table.txt file. Save these in a .new_states file.
        if self.use_edges_pattern:
            log.info("keep-best-solution.py begin")
            start_time = dt.datetime.now()
            subprocess.check_output(f"nice ./utils/keep-best-solution.py {sorted_results_filename}", shell=True)
            self.time_in_keep_best_solution += (dt.datetime.now() - start_time).total_seconds()
            log.info("keep-best-solution.py end")

            log.info("builder-find-new-edges-pattern-states.py begin")
            start_time = dt.datetime.now()
            cmd = "nice ./rubikscubelookuptables/builder-find-new-edges-pattern-states.py %s %s %s.20-new-states" % (
                self.filename,
                sorted_results_filename,
                self.workq_filename,
            )
            log.info(cmd)
            subprocess.check_output(cmd, shell=True)
            self.time_in_find_new_states += (dt.datetime.now() - start_time).total_seconds()
            log.info("builder-find-new-edges-pattern-states.py end")
        else:
            log.info("builder-find-new-states.py begin")
            start_time = dt.datetime.now()
            cmd = "nice ./rubikscubelookuptables/builder-find-new-states.py %s %s %s.20-new-states" % (
                self.filename,
                sorted_results_filename,
                self.workq_filename,
            )
            log.info(cmd)
            subprocess.check_output(cmd, shell=True)
            self.time_in_find_new_states += (dt.datetime.now() - start_time).total_seconds()
            log.info("builder-find-new-states.py end")

        log.info("building next workq file begin")
        start_time = dt.datetime.now()
        new_states_count = int(
            subprocess.check_output(f"wc -l {self.workq_filename}.20-new-states", shell=True).strip().split()[0]
        )
        log.info(f"there are {new_states_count:,} new states")
        pruned = 0
        kept = 0

        if max_depth is None or self.depth < max_depth:
            to_write = []
            to_write_count = 0

            with open(self.workq_filename + ".20-new-states", "r") as fh_new_states, open(
                self.workq_filename_next, "w"
            ) as fh_workq_next:
                for line in fh_new_states:
                    # Find the state and steps_to_solve
                    if self.use_edges_pattern:
                        (pattern, state, steps_to_solve) = line.rstrip().split(":")
                        self.cube.state = list(state)

                    else:
                        (state, steps_to_solve) = line.rstrip().split(":")
                        self.cube.state = list(state)

                    if self.lt_centers_max_depth:
                        if max_depth is None:
                            move_budget = 999
                        else:
                            move_budget = max_depth - self.depth + 1

                        centers = "".join([self.cube.state[x] for x in centers_555])
                        centers_cost = self.lt_centers.get(centers, self.lt_centers_max_depth + 1)

                        # Are the centers so scrambled that we cannot solve them in the steps
                        # budget we have left? If so prune this branch.
                        if centers_cost > move_budget:
                            pruned += 1
                            continue

                        # Or if the centers are back to solved we can prune this branch
                        elif centers == "UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD":
                            pruned += 1
                            continue

                        else:
                            kept += 1

                    # Add entries to the next workq file
                    steps_to_scramble = " ".join(reverse_steps(steps_to_solve.split()))

                    if self.use_edges_pattern:
                        workq_line = f"{pattern}:{state}:{steps_to_scramble}"
                    else:
                        workq_line = f"{state}:{steps_to_scramble}"

                    to_write.append(workq_line + " " * (workq_line_length - len(workq_line)) + "\n")
                    to_write_count += 1
                    self.workq_size += 1

                    if to_write_count >= 10000:
                        fh_workq_next.write("".join(to_write))
                        to_write = []
                        to_write_count = 0

                if to_write_count:
                    fh_workq_next.write("".join(to_write))
                    to_write = []
                    to_write_count = 0

        else:
            with open(self.workq_filename_next, "w") as fh_workq_next:
                pass

        if pruned:
            log.warning(f"kept {kept:,}, pruned {pruned:,}")

        self.time_in_building_workq += (dt.datetime.now() - start_time).total_seconds()
        log.info("building next workq file end")

        # Now merge the lookup-table.txt we built in the previous levels with the .new file
        # Both are sorted so we can use the --merge option
        if os.path.exists(self.filename):
            log.info("sort --merge our current lookup-table.txt file with the .20-new-states file begin")
            start_time = dt.datetime.now()
            subprocess.check_output(
                "LC_ALL=C nice sort --parallel=%d --merge --temporary-directory=%s --output %s.30-final %s %s.20-new-states"
                % (self.cores, FAST_TMP, self.workq_filename, self.filename, self.workq_filename),
                shell=True,
            )
            self.time_in_sort += (dt.datetime.now() - start_time).total_seconds()
            log.info("sort --merge our current lookup-table.txt file with the .20-new-states file end")
        else:
            subprocess.check_output(
                f"cp {self.workq_filename}.20-new-states {self.workq_filename}.30-final", shell=True
            )

        log.info("move files begin")
        start_time = dt.datetime.now()
        os.remove(f"{self.workq_filename}.10-results")
        os.remove(f"{self.workq_filename}.20-new-states")
        shutil.move(f"{self.workq_filename}.30-final", self.filename)

        # mv the next workq to be the current workq
        shutil.move(self.workq_filename_next, self.workq_filename)
        self.time_in_file_delete += (dt.datetime.now() - start_time).total_seconds()
        log.info("move files end")

        # We have finished this depth of the search, update our stats and print them
        self.stats[self.depth] = new_states_count
        log.warning(f"{self.index}: finished depth {self.depth}, workq size {self.workq_size:,}")

    def search(self, max_depth, cores):
        """
        This is where the magic happens
        """
        self.index = 0
        self.stats = {0: 0}
        self.cores = cores

        self._search_setup()

        while True:
            self._search_launch_builder_crunch_workq_per_core()
            self._search_process_builder_crunch_workq_results(max_depth)

            self.depth += 1
            self.log_table_stats()

            # If the workq file is empty our search is complete
            if not os.path.getsize(self.workq_filename):
                os.remove(self.workq_filename)
                break

    def save_starting_states(self):
        patterns = []
        to_write = []
        with open(self.filename, "r") as fh_read:
            for line in fh_read:
                if self.use_edges_pattern:
                    (pattern, cube_state_string, steps) = line.rstrip().split(":")
                    self.cube.state = list(cube_state_string)
                else:
                    (cube_state_string, steps) = line.rstrip().split(":")
                    self.cube.state = list(cube_state_string)

                if self.use_edges_pattern:
                    patterns.append(pattern)

                if self.name == "5x5x5-edges-solve-second-four":
                    if (
                        self.cube.state[53] != "F"
                        or self.cube.state[73] != "F"
                        or self.cube.state[103] != "B"
                        or self.cube.state[123] != "B"
                    ):
                        continue

                to_write.append(f"             ('{cube_state_string[1:]}', 'ULFRBD'),")

                for step in self.rotations:
                    self.cube.state = list(cube_state_string)
                    self.cube.rotate(step)
                    # self.cube.print_cube()
                    to_write.append(f"             ('{''.join(self.cube.state[1:])}', 'ULFRBD'),")

        with open(f"{self.filename}.starting-states", "w") as fh_final:
            to_write.sort()
            fh_final.write("\n".join(to_write) + "\n")
        log.info("wrote %d starting states" % len(to_write))

        to_write = []
        with open(f"{self.filename}.starting-states", "r") as fh_read:
            for line in fh_read:
                (state, order) = line.strip().split("', '")

                # remove the leading ('
                state = state[2:]
                state = state.replace(".", "")

                if self.store_as_hex:
                    state = convert_state_to_hex(state)

                to_write.append(f"'{state}',")

        with open(f"{self.filename}.starting-states.compact", "w") as fh:
            to_write.sort()
            fh.write("\n".join(to_write) + "\n")

        if self.use_edges_pattern:
            print("state_target patterns:\n%s\n\n" % "\n".join(patterns))

        shutil.move(f"{self.filename}.starting-states", self.filename)

    def save(self):
        start_time = dt.datetime.now()

        to_write = []
        to_write_count = 0

        # Convert the states in our lookup-table to their smaller format...basically
        # remove all of the '.'s and if convert to hex (if requested).
        log.info(f"{self}: save() begin")
        log.info(f"{self}: convert state to smaller format, file {self.filename}")
        with open(f"{self.filename}.small", "w") as fh_final:
            with open(self.filename, "r") as fh_read:
                if self.use_edges_pattern:
                    for line in fh_read:
                        (pattern, cube_state_string, steps) = line.rstrip().split(":")
                        pattern = pattern.replace(".", "")
                        self.cube.state = list(cube_state_string)

                        if self.lt_centers_max_depth:
                            centers = "".join([self.cube.state[x] for x in centers_555])

                            # Only keep the entries where centers are solved
                            if centers != "UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD":
                                continue

                            pattern = pattern.replace("UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD", "")

                        to_write.append(f"{pattern}:{steps}")
                        to_write_count += 1

                        if to_write_count >= WRITE_BATCH_SIZE:
                            fh_final.write("\n".join(to_write) + "\n")
                            to_write = []
                            to_write_count = 0

                elif self.use_centers_then_edges:
                    for line in fh_read:
                        (cube_state_string, steps) = line.rstrip().split(":")
                        self.cube.state = list(cube_state_string)

                        if self.size == "4x4x4":
                            centers = "".join([self.cube.state[x] for x in centers_444])
                            edges = "".join([self.cube.state[x] for x in edges_444])
                            centers = centers.replace(".", "")
                            edges = edges.replace(".", "")

                            if self.store_as_hex:
                                centers = convert_state_to_hex(centers)
                                edges = convert_state_to_hex(edges)

                        elif self.size == "5x5x5":
                            centers = "".join([self.cube.state[x] for x in centers_555])
                            edges = "".join([self.cube.state[x] for x in edges_555])
                            centers = centers.replace(".", "")
                            edges = edges.replace(".", "")

                            if self.store_as_hex:
                                centers = convert_state_to_hex(centers)
                                edges = convert_state_to_hex(edges)

                        else:
                            raise Exception(f"Add support for {self.size}")

                        to_write.append(f"{centers}{edges}:{steps}")
                        to_write_count += 1

                        if to_write_count >= WRITE_BATCH_SIZE:
                            fh_final.write("\n".join(to_write) + "\n")
                            to_write = []
                            to_write_count = 0

                else:
                    lt_centers_max_depth = self.lt_centers_max_depth
                    store_as_hex = self.store_as_hex

                    for line in fh_read:
                        (cube_state_string, steps) = line.rstrip().split(":")

                        if lt_centers_max_depth:
                            self.cube.state = list(cube_state_string)
                            edges = "".join([self.cube.state[x] for x in edges_555])
                            edges = edges.replace("-", "x")
                            centers = "".join([self.cube.state[x] for x in centers_555])

                            if centers != "UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD":
                                continue

                            cube_state_string_small = edges
                        else:
                            cube_state_string_small = cube_state_string[1:].replace(".", "")

                        if store_as_hex:
                            cube_state_string_small = convert_state_to_hex(cube_state_string_small)

                        to_write.append(f"{cube_state_string_small}:{steps}")
                        to_write_count += 1

                        if to_write_count >= WRITE_BATCH_SIZE:
                            fh_final.write("\n".join(to_write))
                            fh_final.write("\n")
                            to_write = []
                            to_write_count = 0

            if to_write_count:
                fh_final.write("\n".join(to_write))
                fh_final.write("\n")
                to_write = []
                to_write_count = 0

        shutil.move(f"{self.filename}.small", self.filename)
        files_to_pad = (self.filename,)

        for filename in files_to_pad:
            log.info(f"{self}: pad the file")
            subprocess.check_output(f"nice ./utils/pad-lines.py {filename}", shell=True)

            # Check to see if the file is already sorted before we spend the cycles to sort it
            try:
                log.info(f"{self}: sort --check")
                subprocess.check_output(f"LC_ALL=C nice sort --check {filename}", shell=True)
            except subprocess.CalledProcessError:
                log.info(f"{self}: sort the file")
                subprocess.check_output(
                    "LC_ALL=C nice sort --parallel=%d --temporary-directory=%s --output=%s %s"
                    % (self.cores, FAST_TMP, filename, filename),
                    shell=True,
                )

            log.info(f"{self}: build histogram")
            subprocess.check_output(f"nice ./utils/print-histogram.py {filename} >> histogram.txt", shell=True)

            if self.use_cost_only:
                log.info(f"{self}: build cost-only copy of file")
                convert_to_cost_only(filename)

            elif self.use_hash_cost_only:
                log.info(f"{self}: build hash-cost-only copy of file")
                convert_to_hash_cost_only(filename, self.bucketcount)

            log.info(f"{self}: save() end")

        self.time_in_save = (dt.datetime.now() - start_time).total_seconds()

    def get_starting_states(self, use_hex, use_edges_pattern):
        if self.starting_cube_states:
            foo = []

            for state, state_type in self.starting_cube_states:
                if state_type == "ULFRBD":
                    if use_edges_pattern:
                        self.cube.state = ["x"] + list(state)

                        if self.size == "5x5x5":
                            state = edges_recolor_pattern_555(self.cube.state[:])
                            state = "".join([state[index] for index in wings_for_edges_pattern_555])
                        elif self.size == "4x4x4":
                            state = edges_recolor_pattern_444(self.cube.state[:])
                            state = "".join([state[index] for (_, index, _) in wings_for_edges_recolor_pattern_444])
                        else:
                            raise Exception(f"use_edges_pattern not supported for {self.size}")

                    else:
                        state = "".join(state.split()).strip().replace(".", "")

                        if use_hex:
                            state = convert_state_to_hex(state)

                    foo.append('        "' + state + '"')

                elif state_type == "ascii":
                    # do this later
                    pass
                else:
                    raise Exception(f"{state_type} is an invalid state_type")

            foo.sort()
            starting_states = ",\n".join(foo)
        else:
            class_name = type(self).__name__.replace("Build", "LookupTable")
            starting_states = get_starting_states(self.filename, class_name, None)

        return starting_states

    def _code_gen_lookup_table(self):
        class_name = type(self).__name__.replace("Build", "LookupTable")
        (histogram, linecount, max_depth) = parse_histogram(self.filename)
        starting_states = self.get_starting_states(self.store_as_hex, self.use_edges_pattern)
        filename_minus_directory = self.filename.split("/")[1]

        print(
            '''
class %s(LookupTable):
    """
%s
    """

    # fmt: off
    state_targets = (
%s
    )
    # fmt: on

    def __init__(self, parent, build_state_index: bool = False):
        LookupTable.__init__(
            self,
            parent,
            \"%s\",
            self.state_targets,
            linecount=%d,
            max_depth=%d,
            all_moves=moves_%s,
            # fmt: off
            illegal_moves=(
                "%s"
            ),
            # fmt: on
            use_state_index=True,
            build_state_index=build_state_index,
        )

    def state(self):
        return "".join([self.parent.state[x] for x in CUBE_POSITION_LIST])
        return "".join(["U" if self.parent.state[x] in ("U", "D") else "x" for x in CUBE_POSITION_LIST])

    def populate_cube_from_state(self, state, cube, steps_to_solve):
        state = list(state)

        for (pos, pos_state) in zip(CUBE_POSITION_LIST, state):
            cube[pos] = pos_state
'''
            % (
                class_name,
                histogram,
                starting_states,
                filename_minus_directory,
                linecount,
                max_depth,
                self.size.replace("x", ""),
                '",\n                "'.join(self.illegal_moves),
            )
        )

    def _code_gen_lookup_table_ida(self):
        class_name = type(self).__name__.replace("Build", "LookupTableIDA")
        (histogram, linecount, max_depth) = parse_histogram(self.filename)
        starting_states = self.get_starting_states(self.store_as_hex, self.use_edges_pattern)

        print(
            '''
class %s(LookupTableIDA):
    """
%s
    """

    state_targets = (
%s
    )

    def __init__(self, parent):
        LookupTableIDA.__init__(
            self,
            parent,
            '%s',
            self.state_targets,
            moves_%s,
            # illegal moves
            (TBD),

            linecount=%d,
            max_depth=%d,
            filesize=%d)

    def ida_heuristic(self):
        parent_state = self.parent.state'''
            % (
                class_name,
                histogram,
                starting_states,
                self.filename,
                self.size.replace("x", ""),
                linecount,
                max_depth,
                os.path.getsize(self.filename),
            )
        )

        if self.store_as_hex:
            print(
                "        lt_state = ''.join(['1' if parent_state[x] in (foo, bar) else '0' for x in TBD_%s])"
                % self.size.replace("x", "")
            )
            print("        lt_state = self.hex_format % int(lt_state, 2)\n\n")

        elif self.use_edges_pattern:
            print(f"        state = edges_recolor_pattern_{self.size.replace('x', '')}(parent_state[:])")
            print(
                "        edges_state = ''.join([state[index] for index in wings_for_edges_pattern_%s])"
                % self.size.replace("x", "")
            )
            print("        lt_state = edges_state")

        else:
            print(f"        lt_state = ''.join([parent_state[x] for x in TBD_{self.size.replace('x', '')}])")

        print("        cost_to_goal = max(foo_cost, bar_cost)")
        print("        return (lt_state, cost_to_goal)\n\n")

    def code_gen(self):
        if "0.txt" in self.filename:
            first_prune_table_filename = self.filename.replace("0.txt", "1.txt").replace(
                "lookup-table", "starting-states-lookup-table"
            )

            # if os.path.exists(first_prune_table_filename):
            if True or os.path.exists(first_prune_table_filename):
                log.info(f"prune table {first_prune_table_filename} does exist")
                self._code_gen_lookup_table_ida()
            else:
                log.info(f"prune table {first_prune_table_filename} does NOT exist")
                self._code_gen_lookup_table()
        else:
            self._code_gen_lookup_table()

    def search_new(self, max_depth=99, cores=4):
        workq = deque()
        table = {}

        # seed the workq
        for cube in self.starting_cubes:
            cube_state_minus_x = "".join(cube.state[1:])
            table[cube_state_minus_x] = []

            for step in self.legal_moves:
                workq.append((cube_state_minus_x, [step]))

        index = 0
        max_depth = 5
        log.info(f"max_depth {max_depth}")

        while workq:
            (state, steps_to_scramble) = workq.popleft()
            # log.info(f"{index}: {state}, {steps_to_scramble}")

            debug = False
            """
            if len(steps_to_scramble) >= 3 and steps_to_scramble[0] == "Lw" and steps_to_scramble[1] == "U'" and steps_to_scramble[2] == "3Bw2":
                log.info(f"{index}: {steps_to_scramble}")
                debug = True

            if debug:
                log.info(state)
            """

            cube.state = ["x"]
            cube.state.extend(list(state))

            if debug:
                cube.print_cube()

            cube.rotate(steps_to_scramble[-1])
            cube_state_minus_x = "".join(cube.state[1:])

            add_to_table = False

            if cube_state_minus_x not in table:
                add_to_table = True
            else:
                # if len(steps_to_scramble) <= len(table[cube_state_minus_x]):
                if len(steps_to_scramble) < len(table[cube_state_minus_x]):
                    add_to_table = True

            if add_to_table:
                table[cube_state_minus_x] = steps_to_scramble[:]

                if len(steps_to_scramble) < max_depth:
                    for step in self.legal_moves:
                        workq.append((cube_state_minus_x, steps_to_scramble + [step]))

            if debug:
                cube.print_cube()
                log.info(
                    f"cube_state_minus_x {cube_state_minus_x}, cube state pretty {cube_state_minus_x.replace('.', '')}, add_to_table {add_to_table}"
                )

            index += 1

            if index % 10000 == 0:
                log.info(
                    f"{index:,}: depth {len(steps_to_scramble)}, {len(workq):,} items on workq, {len(table):,} items in table"
                )

        with open(self.filename, "w") as fh:
            for cube_state_minus_x in sorted(table.keys()):
                steps_to_scramble = table[cube_state_minus_x]
                steps_to_solve = reverse_steps(steps_to_scramble)
                fh.write(f"{cube_state_minus_x}:{' '.join(steps_to_solve)}\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)24s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, f"[91m   {logging.getLevelName(logging.ERROR)}[0m")
    logging.addLevelName(logging.WARNING, f"[91m {logging.getLevelName(logging.WARNING)}[0m")

    # standard libraries
    import doctest

    doctest.testmod()

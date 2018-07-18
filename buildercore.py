#!/usr/bin/env python3

from collections import Counter
from rubikscubennnsolver.misc import parse_ascii_222, parse_ascii_333, parse_ascii_444, parse_ascii_555, parse_ascii_666, parse_ascii_777
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_222, moves_222, rotate_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333, moves_333, rotate_333
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444, centers_444, edges_444
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666, moves_666, rotate_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777, moves_777, rotate_777
from threading import Thread, Event
import argparse
import datetime as dt
import gc
import logging
import math
import os
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)
supported_sizes = ('2x2x2', '3x3x3', '4x4x4', '5x5x5', '6x6x6', '7x7x7')

WRITE_BATCH_SIZE = 1000000
LOG_BATCH_SIZE = 1000000

def create_dir(dirname):

    if os.path.isdir(dirname):
        return

    if os.path.isfile(dirname):
        raise Exception("%s already exist but is a file" % dirname)

    os.makedirs(dirname)


def get_line_number_splits(lines, cores):
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


def reverse_steps(steps):
    """
    >>> reverse_steps([])
    []

    >>> reverse_steps(["U"])
    ["U'"]

    >>> reverse_steps(["U", "R'", "D2"])
    ['D2', 'R', "U'"]
    """
    assert isinstance(steps, list)

    results = []
    for step in reversed(steps):
        if step.endswith("2"):
            pass
        elif step.endswith("'"):
            step = step[0:-1]
        else:
            step += "'"
        results.append(step)
    return results


def convert_state_to_hex(state):
    """
    This assumes that state only has "x"s and Us or Ls or Fs or Rs or Bs or Ds

    >>> convert_state_to_hex("xxxU")
    '1'

    >>> convert_state_to_hex("UxUx")
    'a'

    >>> convert_state_to_hex("UUxUx")
    '1a'
    """
    state = state.replace('x', '0').replace('U', '1').replace('L', '1').replace('F', '1').replace('R', '1').replace('B', '1').replace('D', '1')
    hex_width = int(math.ceil(len(state)/4.0))
    hex_state = hex(int(state, 2))[2:]

    if hex_state.endswith('L'):
        hex_state = hex_state[:-1]

    return hex_state.zfill(hex_width)


def convert_to_cost_only(filename):
    filename_new = filename.replace('.txt', '.cost-only.txt')
    prev_state_int = None

    with open(filename, 'r') as fh:
        with open(filename_new, 'w') as fh_new:
            for (line_number, line) in enumerate(fh):
                (state, steps) = line.strip().split(':')
                steps = steps.split()
                state_int = int(state, 16)
                #log.info("%s: state_int %d" % (state, state_int))

                # Add 0s for every state from prev_state_int to state_int
                if prev_state_int is None:
                    zeroes_between_prev_and_now = state_int
                else:
                    zeroes_between_prev_and_now = (state_int - prev_state_int - 1)

                if zeroes_between_prev_and_now > 0:
                    #log.info("zeroes_between_prev_and_now %s" % zeroes_between_prev_and_now)
                    zeroes_between_prev_and_now = zeroes_between_prev_and_now * '0'
                    fh_new.write(zeroes_between_prev_and_now)

                # Write the steps_len
                if steps[0].isdigit():
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


def convert_to_hash_cost_only(filename, bucketcount):
    filename_new = filename.replace('.txt', '.hash-cost-only.txt')
    prev_state_int = None
    first_permutation_rank = None

    bucket = bytearray(bucketcount)
    collisions = 0
    from pyhashxx import hashxx

    with open(filename, 'r') as fh:
        for (line_number, line) in enumerate(fh):
            (state, steps) = line.strip().split(':')
            steps = steps.split()

            hash_raw = hashxx(state.encode('utf-8'))
            hash_index = int(hash_raw % bucketcount)

            # Write the steps_len
            if steps[0].isdigit():
                steps_len = int(steps[0])
            else:
                steps_len = len(steps)

            #log.info("state: %s, hash_index %s, steps_len %s" % (state, hash_index, steps_len))

            if not bucket[hash_index]:
                bucket[hash_index] = steps_len
            else:
                collisions += 1

                if bucket[hash_index] > steps_len:
                    bucket[hash_index] = steps_len

            if line_number % 1000000 == 0:
                log.info(line_number)
            #if line_number >= 1000:
            #    break

    log.info("%d collisions" % collisions)
    log.info("begin writing %s" % filename_new)
    with open(filename_new, 'w') as fh_new:
        to_write = []

        for (index, x) in enumerate(bucket):
            if x > 15:
                to_write.append('f')
            else:
                # Convert steps_len to hex and ignore the 0x part of the string
                to_write.append(hex(x)[2])

            if index % 100000 == 0:
                fh_new.write(''.join(to_write))
                to_write = []

        if to_write:
            fh_new.write(''.join(to_write))

        fh_new.write('\n')
    log.info("end writing %s" % filename_new)


def parse_histogram(filename):

    if not os.path.exists('histogram.txt'):
        print("\n\nERROR: histogram.txt does not exist")
        sys.exit(1)

    with open('histogram.txt', 'r') as fh:
        found_filename = False
        histogram = []
        linecount = 0
        max_depth = 0

        for line in fh:
            line = line.strip()

            if not found_filename and line == filename:
                found_filename = True
                histogram.append('    ' + line)
                log.info(line)

            elif found_filename:
                histogram.append('    ' + line)
                log.info(line)

                if 'steps has' in line:
                    max_depth = int(line.split()[0])
                elif line.startswith('Total:'):
                    linecount = int(line.split()[1].replace(',', ''))
                elif line.startswith('Average'):
                    break

    if not found_filename:
        print("\n\nERROR: %s is not in histogram.txt" % filename)
        sys.exit(0)

    return ('\n'.join(histogram), linecount, max_depth)


def get_starting_states(filename, class_name, hex_digits):
    """
    TODO hex_digits needs to be the number of hex characters in the state
    """
    ss_filename = 'starting-states-' + filename

    if not os.path.exists(ss_filename):
        print("\n\nERROR: %s does not exist. run:" % ss_filename)
        print("\n./builderui.py %s\n" % class_name.replace('LookupTable', 'StartingStates'))
        sys.exit(1)

    with open(ss_filename, 'r') as fh:
        result = []
        for line in fh:
            line = line.strip()
            line = line.replace(" 'ULFRBD'),", "")
            line = line.replace("(", "")
            line = line.replace(".", "")
            line = line.replace(",", "")

            if hex_digits:
                line = line.replace('x', '0').replace('U', '1').replace('L', '1').replace('F', '1').replace('R', '1').replace('B', '1').replace('D', '1')
                line = line.replace("'", "")
                line = line.replace(",", "")
                #print("             %0dx," % hex(int(line, 2))[2:])
                result.append("             '" + hex_format % int(line, 2) + "'")
            else:
                result.append("%s" % line)

        result.sort()

        if len(result) < 100:
            result = '(' + ',\n             '.join(result) + ')'
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
        log.debug("Running %s" % ' '.join(self.cmd))
        try:
            self.result = subprocess.check_output(self.cmd)

            if self.result is not None and self.result.isdigit():
                self.result = int(self.result)
            self.ok = True
        except subprocess.CalledProcessError:
            self.ok = False



class BFS(object):
    """
    Base class for all classes that build lookup tables
    """

    def __init__(self, name, illegal_moves, size, filename, store_as_hex, starting_cube_states,
                 use_cost_only=False, use_hash_cost_only=False, use_edges_pattern=False, legal_moves=None,
                 rotations=[], use_centers_then_edges=False, symmetries=[]):
        self.name = name
        self.illegal_moves = illegal_moves
        self.size = size
        self.filename = filename
        self.store_as_hex = store_as_hex
        self.starting_cubes = []
        self.use_cost_only = use_cost_only
        self.use_hash_cost_only = use_hash_cost_only
        self.use_edges_pattern = use_edges_pattern
        self.size = size
        self.starting_cube_states = starting_cube_states
        self.rotations = rotations
        self.use_centers_then_edges = use_centers_then_edges
        self.symmetries = symmetries

        assert isinstance(self.name, str)
        assert isinstance(self.illegal_moves, tuple)
        assert self.size in supported_sizes
        assert isinstance(self.filename, str)
        assert isinstance(self.store_as_hex, bool)
        assert isinstance(starting_cube_states, tuple)
        assert isinstance(self.use_cost_only, bool)
        assert isinstance(self.use_hash_cost_only, bool)
        assert not (self.use_cost_only and self.use_hash_cost_only), "Both cannot be true"

        if size == '2x2x2':
            self.all_moves = moves_222
            self.rotate_xxx = rotate_222
            self.cube = RubiksCube222(solved_222, order='URFDLB')

            for (state, order) in starting_cube_states:
                if order == 'ascii':
                    state = parse_ascii_222(state)
                    order = 'ULFRBD'
                self.starting_cubes.append(RubiksCube222(state, order))

        elif size == '3x3x3':
            self.all_moves = moves_333
            self.rotate_xxx = rotate_333
            self.cube = RubiksCube333(solved_333, order='URFDLB')

            for (state, order) in starting_cube_states:
                if order == 'ascii':
                    state = parse_ascii_333(state)
                    order = 'ULFRBD'
                self.starting_cubes.append(RubiksCube333(state, order))

        elif size == '4x4x4':
            self.all_moves = moves_444
            self.rotate_xxx = rotate_444
            self.cube = RubiksCube444(solved_444, order='URFDLB')

            for (state, order) in starting_cube_states:
                if order == 'ascii':
                    state = parse_ascii_444(state)
                    order = 'ULFRBD'
                self.starting_cubes.append(RubiksCube444(state, order))

        elif size == '5x5x5':
            self.all_moves = moves_555
            self.rotate_xxx = rotate_555
            self.cube = RubiksCube555(solved_555, order='URFDLB')

            for (state, order) in starting_cube_states:
                if order == 'ascii':
                    state = parse_ascii_555(state)
                    order = 'ULFRBD'
                self.starting_cubes.append(RubiksCube555(state, order))

        elif size == '6x6x6':
            self.all_moves = moves_666
            self.rotate_xxx = rotate_666
            self.cube = RubiksCube666(solved_666, order='URFDLB')

            for (state, order) in starting_cube_states:
                if order == 'ascii':
                    state = parse_ascii_666(state)
                    order = 'ULFRBD'
                self.starting_cubes.append(RubiksCube666(state, order))

        elif size == '7x7x7':
            self.all_moves = moves_777
            self.rotate_xxx = rotate_777
            self.cube = RubiksCube777(solved_777, order='URFDLB')

            for (state, order) in starting_cube_states:
                if order == 'ascii':
                    state = parse_ascii_777(state)
                    order = 'ULFRBD'
                self.starting_cubes.append(RubiksCube777(state, order))

        # Print all starting cubes
        if len(self.starting_cubes) < 20000:
            for cube in self.starting_cubes:
                cube.print_cube()

        # Build list of legal moves from allmoves minus illegal moves
        if legal_moves:
            self.legal_moves = legal_moves
        else:
            self.legal_moves = []

            for move in self.all_moves:
                if move not in self.illegal_moves:
                    self.legal_moves.append(move)

        #self.legal_moves = sorted(self.legal_moves)
        log.info("all moves     : %s" % ' '.join(self.all_moves))
        log.info("illegal moves : %s" % ' '.join(self.illegal_moves))
        log.info("legal moves   : %s" % ' '.join(self.legal_moves))
        self.bucketcount = 0
        self.size_number = int(self.size[0])
        self.workq_line_length = self.get_workq_line_length()

        self.time_in_sort = 0
        self.time_in_crunching_workq = 0
        self.time_in_building_workq = 0
        self.time_in_save = 0
        self.time_in_find_new_states = 0

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
        SEPERATORS = 1
        CHARS_PER_STEP = 5
        MAX_STEPS = 20

        #return 512
        return LEADING_X + (SIDES_PER_CUBE * self.size_number * self.size_number) + SEPERATORS + (CHARS_PER_STEP * MAX_STEPS)

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
        prev = None
        total = 0

        for i in sorted(self.stats)[1:]:
            total += self.stats[i]

        for i in sorted(self.stats)[1:]:
            if self.stats[i-1]:
                delta = float(self.stats[i]/self.stats[i-1])
            else:
                delta = float(0)

            if self.stats[i]:
                states_per_depth += "    {} steps has {:,} entries ({} percent, {:.2f}x previous step)\n".format(i, self.stats[i], int(float(self.stats[i]/total) * 100), delta)

        states_per_depth += "    Total: {:,} entries".format(total)
        log.info("\n\n" + states_per_depth + "\n\n")

    def _search_setup(self):
        """
        Prep work needed before we start our BFS
        """
        # We will write the workq to a file in a local tmp directory
        tmp_dirname = 'tmp'
        create_dir(tmp_dirname)
        self.workq_filename = os.path.join(tmp_dirname, "%s.workq.txt" % self)
        self.workq_filename_next = self.workq_filename + ".next"
        self.workq_size = 0

        # If we crashed while building the next workq file we need to delete that file
        if os.path.isfile(self.workq_filename_next):
            os.remove(self.workq_filename_next)

        # We are picking up where we left off, we must populate stats
        if os.path.isfile(self.workq_filename) and os.path.isfile(self.filename):

            log.info("setup: picking up where we left off")
            filename_linecount = int(subprocess.check_output("wc -l %s" % self.filename, shell=True).strip().split()[0])
            self.depth = 0

            with open(self.filename, 'r') as fh:
                for (line_number, line) in enumerate(fh):
                    (state, steps) = line.rstrip().split(':')

                    steps_len = len(steps.split())

                    if steps_len > self.depth:
                        self.depth = steps_len

                    if steps_len not in self.stats:
                        self.stats[steps_len] = 0

                    self.stats[steps_len] += 1

                    if line_number % LOG_BATCH_SIZE == 0:
                        log.info("setup: loaded %d/%d" % (line_number, filename_linecount))
            self.depth += 1
            self.log_table_stats()

            log.info("setup: get workq_size")
            self.workq_size = int(subprocess.check_output("wc -l %s" % self.workq_filename, shell=True).strip().split()[0])
            log.info("setup: workq_size %d" % self.workq_size)
            self.rm_per_core_workq_results_files()

        # We are starting from scratch so for each starting_cube loop over all legal moves
        # and add that tuple to the workq
        else:
            log.info("setup: starting from scratch")
            self.depth = 1
            self.rm_per_core_workq_results_files()

            if os.path.isfile(self.workq_filename):
                os.remove(self.workq_filename)

            if os.path.isfile(self.filename):
                os.remove(self.filename)

            if self.use_edges_pattern:
                if self.size == '4x4x4':
                    pattern = '10425376a8b9ecfdhgkiljnm'
                elif self.size == '5x5x5':
                    pattern = 'TBD'
                else:
                    raise Exception("implement edges-pattern for %s" % self.size)
            else:
                pattern = ''

            with open(self.workq_filename, 'w') as fh:
                for cube in self.starting_cubes:
                    for move in self.legal_moves:
                        if self.use_edges_pattern:
                            workq_line = "%s:%s:%s" % (pattern, ''.join(cube.state), move)
                        else:
                            workq_line = "%s:%s" % (''.join(cube.state), move)
                        fh.write(workq_line + " " * (self.workq_line_length - len(workq_line)) + "\n")
                        self.workq_size += 1

        self.starting_cubes = []
        gc.collect()

    def _search_launch_builder_crunch_workq_per_core(self):
        """
        Launch one builder-crunch-workq process per core. Wait for all of them
        to complete before returning.
        """
        threads = []
        line_numbers_for_cores = get_line_number_splits(self.workq_size, self.cores)
        start_time = dt.datetime.now()

        # Launch one builder-crunch-workq process per core
        # - each one will process a subsection of workq_filename_next
        # - wait for all of them to finish before we move on
        for core in range(self.cores):
            per_core_filename = self.get_workq_filename_for_core(core)

            # If _setup() left this file, it means all of the work needed
            # by this core was already done
            if os.path.exists(per_core_filename):
                continue

            # If we are out of memory and swapping this will fail due to "OSError: Cannot allocate memory"
            (start, end) = line_numbers_for_cores[core]

            cmd = [
                'nice',
                './builder-crunch-workq.py',
                self.size,
                self.workq_filename,
                str(self.workq_line_length),
                str(start),
                str(end),
                self.get_workq_filename_for_core(core)
            ]

            if self.use_edges_pattern:
                cmd.append('--use-edges-pattern')

            if self.symmetries:
                cmd.append('--symmetries')
                cmd.append(','.join(self.symmetries))
            

            '''
            if self.use_edges_pattern:
                cmd = [
                    'nice',
                    './builder-crunch-workq.py',
                    self.size,
                    self.workq_filename,
                    str(self.workq_line_length),
                    str(start),
                    str(end),
                    self.get_workq_filename_for_core(core)
                ]

                # dwalton
                assert not self.symmetries, "Add symmetry support to builder-crunch-workq.py"
            else:
                cmd = [
                    'nice',
                    './builder-crunch-workq',
                    '--size', str(self.size_number),
                    '--start', str(start),
                    '--end', str(end),
                    '--linewidth', str(self.workq_line_length),
                    '--input', self.workq_filename,
                    '--output', self.get_workq_filename_for_core(core)
                ]
            '''

            log.info(' '.join(cmd))

            thread = BackgroundProcess(cmd, 'builder-crunch-workq core %d' % core)
            thread.start()
            threads.append(thread)

        hit_error = False
        for thread in threads:
            thread.join()

            if thread.ok:
                log.info("depth %d %s: finished" % (self.depth, thread))
            else:
                hit_error = True
                log.info("depth %d %s: finished but with an error" % (self.depth, thread))

        if hit_error:
            log.error("builder-crunch-workq hit an error")
            sys.exit(1)

        self.time_in_crunching_workq += (dt.datetime.now() - start_time).total_seconds()

    def _search_process_builder_crunch_workq_results(self, max_depth):
        """
        Process the results from all of the builder-crunch-workq processes
        and build a new workq_filename_next
        """
        to_write = []
        to_write_count = 0
        to_write_lookup_table = []
        to_write_lookup_table_count = 0
        cube = self.cube
        rotate_xxx = self.rotate_xxx
        workq_line_length = self.workq_line_length
        self.workq_size = 0

        # Remove the workq file to save some disk space
        if os.path.exists(self.workq_filename):
            os.remove(self.workq_filename)

        start_time = dt.datetime.now()
        log.info("sort --merge all of the files created by builder-crunch-workq processes")

        # Use --merge again once the C cruncher sorts its writes
        subprocess.check_output("LC_ALL=C sort --merge --temporary-directory=./tmp/ --output %s.10-results %s.core* " % (self.workq_filename, self.workq_filename), shell=True)
        self.time_in_sort += (dt.datetime.now() - start_time).total_seconds()

        log.info("rm %s.core*" % self.workq_filename)
        subprocess.check_output("rm %s.core* " % self.workq_filename, shell=True)

        # Use "builder-find-new-states.py" to find the entries in the .results file that are not
        # in our current lookup-table.txt file. Save these in a .new_states file.
        log.info("builder-find-new-states.py begin")
        start_time = dt.datetime.now()
        if self.use_edges_pattern:
            subprocess.check_output("./builder-find-new-edges-pattern-states.py %s %s.10-results %s.20-new-states" % (self.filename, self.workq_filename, self.workq_filename) , shell=True)
        else:
            subprocess.check_output("./builder-find-new-states.py %s %s.10-results %s.20-new-states" % (self.filename, self.workq_filename, self.workq_filename) , shell=True)
        self.time_in_find_new_states += (dt.datetime.now() - start_time).total_seconds()
        log.info("builder-find-new-states.py end")

        log.info("begin building next workq file")
        start_time = dt.datetime.now()
        new_states_count = int(subprocess.check_output("wc -l %s.20-new-states" % self.workq_filename, shell=True).strip().split()[0])

        if max_depth is None or self.depth < max_depth:
            with open(self.workq_filename + '.20-new-states', 'r') as fh_new_states,\
                open(self.workq_filename_next, 'w') as fh_workq_next:

                for line in fh_new_states:
                    if self.use_edges_pattern:
                        (pattern, state, steps_to_solve) = line.rstrip().split(':')
                    else:
                        (state, steps_to_solve) = line.rstrip().split(':')

                    # Add entries to the next workq file
                    steps_to_scramble = ' '.join(reverse_steps(steps_to_solve.split()))

                    for next_move in self.legal_moves:
                        if self.use_edges_pattern:
                            workq_line = "%s:%s:%s %s" % (pattern, state, steps_to_scramble, next_move)
                        else:
                            workq_line = "%s:%s %s" % (state, steps_to_scramble, next_move)

                        fh_workq_next.write(workq_line + " " * (workq_line_length - len(workq_line)) + "\n")
                        self.workq_size += 1
        else:
            with open(self.workq_filename_next, 'w') as fh_workq_next:
                pass
        self.time_in_building_workq += (dt.datetime.now() - start_time).total_seconds()
        log.info("end building next workq file")

        log.info("sort --merge our current lookup-table.txt file with the .20-new-states file")
        # Now merge the lookup-table.txt we build in the previous levels with the .new file
        # Both are sorted so we can use the --merge option
        if os.path.exists(self.filename):
            start_time = dt.datetime.now()
            subprocess.check_output("LC_ALL=C sort --merge --temporary-directory=./tmp/ --output %s.30-final %s %s.20-new-states" % (self.workq_filename, self.filename, self.workq_filename), shell=True)
            self.time_in_sort += (dt.datetime.now() - start_time).total_seconds()
        else:
            subprocess.check_output("cp %s.20-new-states %s.30-final" % (self.workq_filename, self.workq_filename) , shell=True)

        shutil.move("%s.30-final" % self.workq_filename, self.filename)
        os.remove("%s.10-results" % self.workq_filename)
        os.remove("%s.20-new-states" % self.workq_filename)

        # mv the next workq to be the current workq
        shutil.move(self.workq_filename_next, self.workq_filename)

        # We have finished this depth of the search, update our stats and print them
        self.stats[self.depth] = new_states_count
        log.warning("{}: finished depth {}, workq size {:,}".format(self.index, self.depth, self.workq_size))

    def search(self, max_depth,cores):
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

            #log.info("PAUSED")
            #input("PAUSED")

            # If the workq file is empty our search is complete
            if not os.path.getsize(self.workq_filename):
                os.remove(self.workq_filename)
                break

    def save_starting_states(self):
        patterns = []
        to_write = []
        with open(self.filename, 'r') as fh_read:
            for line in fh_read:
                if self.use_edges_pattern:
                    (pattern, cube_state_string, steps) = line.rstrip().split(':')
                    patterns.append(pattern)
                else:
                    (cube_state_string, steps) = line.rstrip().split(':')
                    self.cube.state = list(cube_state_string)
                    self.cube.print_cube()
                to_write.append("             ('%s', 'ULFRBD')," % cube_state_string[1:])

                for step in self.rotations:
                    self.cube.state = list(cube_state_string)
                    self.cube.rotate(step)
                    self.cube.print_cube()
                    to_write.append("             ('%s', 'ULFRBD')," % ''.join(self.cube.state[1:]))

        with open("%s.starting-states" % self.filename, 'w') as fh_final:
            to_write.sort()
            fh_final.write("\n".join(to_write) + "\n")

        log.info("wrote %d starting states" % len(to_write))

        if self.use_edges_pattern:
            print("state_target patterns:\n%s\n\n" % '\n'.join(patterns))

        shutil.move("%s.starting-states" % self.filename, self.filename)


    def save(self):
        start_time = dt.datetime.now()

        # Convert the states in our lookup-table to their smaller format...basically
        # remove all of the '.'s and if convert to hex (if requested).
        log.info("%s: convert state to smaller format" % self)
        with open(self.filename, 'r') as fh_read, open("%s.small" % self.filename, 'w') as fh_final:
            if self.use_edges_pattern:
                for line in fh_read:
                    (pattern, cube_state_string, steps) = line.rstrip().split(':')
                    fh_final.write("%s:%s\n" % (pattern, steps))

            elif self.use_centers_then_edges:
                for line in fh_read:
                    (cube_state_string, steps) = line.rstrip().split(':')
                    self.cube.state = list(cube_state_string)

                    if self.size == '4x4x4':
                        centers = ''.join(self.cube.state[x] for x in centers_444)
                        edges = ''.join(self.cube.state[x] for x in edges_444)

                        centers = centers.replace('.', '')
                        edges = edges.replace('.', '')
                    else:
                        raise Exception("Add support for %s" % self.size)

                    fh_final.write("%s%s:%s\n" % (centers, edges, steps))

            else:
                for line in fh_read:
                    (cube_state_string, steps) = line.rstrip().split(':')

                    cube_state_string_small = cube_state_string[1:].replace('.', '')

                    if self.store_as_hex:
                        cube_state_string_small = convert_state_to_hex(cube_state_string_small)

                    fh_final.write("%s:%s\n" % (cube_state_string_small, steps))

        shutil.move("%s.small" % self.filename, self.filename)

        log.info("%s: pad the file" % self)
        subprocess.check_output("./utils/pad-lines.py %s" % self.filename, shell=True)

        log.info("%s: sort the file" % self)
        subprocess.check_output("LC_ALL=C nice sort --temporary-directory=./tmp/ --output=%s %s" %
            (self.filename, self.filename), shell=True)

        log.info("%s: build histogram" % self)
        subprocess.check_output("./utils/print-histogram.py %s >> histogram.txt" % self.filename, shell=True)

        if self.use_cost_only:
            log.info("%s: build cost-only copy of file" % self)
            convert_to_cost_only(self.filename)

        elif self.use_hash_cost_only:
            log.info("%s: build hash-cost-only copy of file" % self)
            convert_to_hash_cost_only(self.filename, self.bucketcount)

        self.time_in_save = (dt.datetime.now() - start_time).total_seconds()

    def get_starting_states(self):
        if self.starting_cube_states:
            foo = []
            for (state, state_type) in self.starting_cube_states:
                if state_type == 'ULFRBD':
                    foo.append("        '" + ''.join(state.split()).strip().replace('.', '') + "'")
                elif state_type == 'ascii':
                    # do this later
                    pass
                else:
                    raise Exception("%s is an invalid state_type" % state_type)

            starting_states = ",\n".join(foo)
        else:
            starting_states = get_starting_states(self.filename, class_name, None)

        return starting_states

    def _code_gen_lookup_table(self):
        class_name = type(self).__name__.replace('Build', 'LookupTable')

        # I do 2x the key then take the next prime number
        next_prime = {
            24010000 : 48020003,
            165636900 : 331273823,
            239500800 : 479001629,
        }

        (histogram, linecount, max_depth) = parse_histogram(self.filename)
        starting_states = self.get_starting_states()

        print('''
#class %s(LookupTableHashCostOnly):
class %s(LookupTable):
    """
%s
    """

    state_targets = (
%s
    )

    def __init__(self, parent):
        LookupTable.__init__(
            self,
            parent,
            '%s',
            self.state_targets,
            linecount=%d,
            max_depth=%d,
            filesize=TBD)
        ''\'
        LookupTableHashCostOnly.__init__(
            self,
            parent,
            '%s',
            self.state_targets,
            linecount=%d,
            max_depth=%d,
            bucketcount=%d,
            filesize=%d)
        ''\'

    def state(self):
        parent_state = self.parent.state''' % (
    class_name,
    class_name,
    histogram,
    starting_states,
    self.filename,
    linecount,
    max_depth,
    self.filename.replace('.txt', '.hash-cost-only.txt'),
    linecount,
    max_depth,
    next_prime[linecount],
    next_prime[linecount]+1, # +1 for the newline
    ))

        if self.store_as_hex:
            print("        result = ''.join(['1' if parent_state[x] in (foo, bar) else '0' for x in TBD_%s])" % self.size.replace('x', ''))
            print("        return self.hex_format % int(result, 2)\n\n")
        else:
            print("        result = ''.join([parent_state[x] for x in TBD_%s])" % self.size.replace('x', ''))
            print("        return result\n\n")

        #print("\n\n\n\n")
        #print("        self.lt_foo = %s(self)" % class_name)
        #print("\n\n\n\n")

    def _code_gen_lookup_table_ida(self):
        class_name = type(self).__name__.replace('Build', 'LookupTableIDA')
        (histogram, linecount, max_depth) = parse_histogram(self.filename)
        starting_states = self.get_starting_states()

        print('''
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

            # prune tables
            (parent.lt_foo,
             parent.lt_bar),
            linecount=%d,
            max_depth=%d,
            filesize=%d)

    def state(self):
        parent_state = self.parent.state''' % (
    class_name,
    histogram,
    starting_states,
    self.filename,
    self.size.replace('x', ''),
    linecount,
    max_depth,
    os.path.getsize(self.filename)
    ))

        if self.store_as_hex:
            print("        result = ''.join(['1' if parent_state[x] in (foo, bar) else '0' for x in TBD_%s])" % self.size.replace('x', ''))
            print("        return self.hex_format % int(result, 2)\n\n")
        else:
            print("        result = ''.join([parent_state[x] for x in TBD_%s])" % self.size.replace('x', ''))
            print("        return result\n\n")

    def code_gen(self):
        assert self.filename.startswith('lookup-table-'), "--code-gen only applies to BuildXYZ classes"

        if '0.txt' in self.filename:
            first_prune_table_filename = self.filename.replace('0.txt', '1.txt').replace('lookup-table', 'starting-states-lookup-table')

            if os.path.exists(first_prune_table_filename):
                log.info("prune table %s does exist" % first_prune_table_filename)
                self._code_gen_lookup_table_ida()
            else:
                log.info("prune table %s does NOT exist" % first_prune_table_filename)
                self._code_gen_lookup_table()
        else:
            self._code_gen_lookup_table()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    import doctest
    doctest.testmod()

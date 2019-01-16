#!/usr/bin/env python3

import argparse
import subprocess
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555, centers_555, edges_555, edges_recolor_pattern_555, wings_for_edges_pattern_555
from rubikscubennnsolver import reverse_steps
import os
import logging
import sys



def binary_search(fh, width, state_width, linecount, state_to_find):
    first = 0
    last = linecount - 1
    b_state_to_find = bytearray(state_to_find, encoding='utf-8')
    result = []

    while first <= last:
        midpoint = int((first + last)/2)
        fh.seek(midpoint * width)

        # Only read the 'state' part of the line (for speed)
        b_state = fh.read(state_width)

        if b_state_to_find < b_state:
            last = midpoint - 1

        # If this is the line we are looking for, then read the entire line
        elif b_state_to_find == b_state:
            #fh.seek(midpoint * width)
            #line = fh.read(width)
            #(_, value) = line.decode('utf-8').rstrip().split(':')
            break

        else:
            first = midpoint + 1

    line_number_midpoint_state_to_find = midpoint

    # Go back one line at a time until we are at the first line with state_to_find
    while True:
        fh.seek(midpoint * width)

        line = fh.read(width)
        line = line.decode('utf-8').rstrip()
        (state, steps) = line.split(':')

        if state != state_to_find:
            break

        result.append(steps.rstrip())
        midpoint -= 1

        if midpoint < 0:
            break

    # Go forward one line at a time until we have read all the lines
    # with state
    midpoint = line_number_midpoint_state_to_find + 1

    while midpoint <= linecount - 1:
        fh.seek(midpoint * width)
        line = fh.read(width)
        line = line.decode('utf-8').rstrip()
        (state, steps) = line.split(':')

        if state == state_to_find:
            result.append(steps.rstrip())
        else:
            break

        midpoint += 1

    return result


def get_file_vitals(filename):
    """
    Return the width of each line, the width of the state, and the number of lines in the file
    """
    size = os.path.getsize(filename)

    # Find the state_width for the entries in our .txt file
    with open(filename, 'r') as fh:
        first_line = next(fh)
        width = len(first_line)
        (state, steps) = first_line.split(':')
        state_width = len(state)
        linecount = int(size/width)
        return (width, state_width, linecount)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=0, help='starting line number')
    parser.add_argument('--end', type=int, default=0, help='starting line number')
    parser.add_argument('--centers-filename', type=str)
    parser.add_argument('--lookup-table-filename', type=str)
    parser.add_argument('--specific-depth', type=int, default=0)
    args = parser.parse_args()
    start = args.start
    end = args.end

    if end:
        assert end > start, "--end must be greater than --start"

    #lookup_table_filename = "lookup-table-5x5x5-step100-stage-first-six-edges.txt"
    centers_filename = args.centers_filename
    lookup_table_filename = args.lookup_table_filename

    if end:
        lookup_table_filename_new = "{}-{}-{}.new".format(lookup_table_filename, start, end)
    else:
        lookup_table_filename_new = "{}.new".format(lookup_table_filename)

    (centers_width, centers_state_width, centers_linecount) = get_file_vitals(centers_filename)

    cube = RubiksCube555(solved_555, order='URFDLB')
    to_write = []
    to_write_count = 0
    BATCH_SIZE = 20000

    if end:
        lines_to_process = end - start + 1
    else:
        lines_to_process = int(subprocess.check_output("wc -l %s" % lookup_table_filename, shell=True).strip().split()[0])

    line_number_processed = 0
    state_cache = {}
    SPECIFIC_DEPTH = args.specific_depth

    with open(lookup_table_filename_new, "w") as fh_new:
        with open(lookup_table_filename, "r") as fh, open(centers_filename, "rb") as fh_centers:
            for (line_number, line) in enumerate(fh):

                if start and line_number < start:
                    continue

                if end and line_number > end:
                    break

                (state, steps_to_solve) = line.rstrip().split(":")
                steps_to_solve = steps_to_solve.split()
                steps_to_scramble = reverse_steps(steps_to_solve)

                cube.re_init()

                if lookup_table_filename == "lookup-table-5x5x5-step100-stage-first-six-edges.txt":
                    cube.state[1:] = state
                else:
                    for step in steps_to_scramble:
                        cube.state = rotate_555(cube.state[:], step)

                tmp_state = cube.state[:]
                tmp_solution = cube.solution[:]
                centers_state = ''.join([cube.state[index] for index in centers_555])

                # dwalton
                centers_solutions = binary_search(fh_centers, centers_width, centers_state_width, centers_linecount, centers_state)
                #log.info("{} centers_state".format(centers_state))
                #log.info("{} centers solutions".format(len(centers_solutions)))
                #log.info("{} centers solutions".format(centers_solutions))
                #sys.exit(0)

                for centers_solution in centers_solutions:
                    cube.state = tmp_state[:]
                    cube.solution = tmp_solution[:]
                    centers_solution = centers_solution.split()

                    if SPECIFIC_DEPTH and (len(steps_to_scramble) + len(centers_solution)) != SPECIFIC_DEPTH:
                        continue

                    for step in centers_solution:
                        cube.state = rotate_555(cube.state[:], step)

                    if lookup_table_filename == "lookup-table-5x5x5-step100-stage-first-six-edges.txt":
                        state_to_write = "".join(cube.state[index] for index in edges_555)
                    elif lookup_table_filename == "lookup-table-5x5x5-step100-solve-first-six-edges.txt":
                        state = edges_recolor_pattern_555(cube.state[:])
                        state_to_write = ''.join([state[index] for index in wings_for_edges_pattern_555])
                    else:
                        raise Exception("Implement this")

                    steps_to_write = steps_to_scramble + centers_solution

                    if state_to_write not in state_cache or len(steps_to_write) < state_cache[state_to_write]:
                        to_write.append("{}:{}".format(state_to_write, " ".join(reverse_steps(steps_to_write))))
                        to_write_count += 1
                        state_cache[state_to_write] = len(steps_to_write)

                line_number_processed += 1

                if line_number_processed % 1000 == 0:
                    if end:
                        log.info("{:,} -> {:,}: {:,}/{:,}".format(start, end, line_number_processed, lines_to_process))
                    else:
                        log.info("{:,}/{:,}".format(line_number_processed, lines_to_process))

                if to_write_count >= BATCH_SIZE:
                    to_write.sort()
                    fh_new.write("\n".join(to_write) + "\n")
                    fh_new.flush()
                    to_write = []
                    to_write_count = 0
                    state_cache = {}

        if to_write_count:
            to_write.sort()
            fh_new.write("\n".join(to_write) + "\n")
            fh_new.flush()
            to_write = []
            to_write_count = 0
            state_cache = {}

    if end:
        log.info("{:,} -> {:,}: FINISHED".format(start, end))

    # If we processed the entire file ourselves then we can sort the results, keep the best
    # solution per state, etc.  If we only did a subset though we need to wait until all of
    # those are done, combine all of the results files, then sort, keep best, etc.
    else:

        # sort the file
        log.info("sorting...")
        subprocess.check_output(
            "LC_ALL=C sort --temporary-directory=./tmp/ --output %s %s " %
            (lookup_table_filename_new, lookup_table_filename_new),
            shell=True)

        # keep the best entry per state
        log.info("keep-best-solution...")
        subprocess.check_output("./utils/keep-best-solution.py %s" % (lookup_table_filename_new), shell=True)

        # pad the lines
        log.info("pad-lines...")
        subprocess.check_output("./utils/pad-lines.py %s" % (lookup_table_filename_new), shell=True)

        # print the histogram
        subprocess.call("./utils/print-histogram.py %s" % (lookup_table_filename_new), shell=True)

#!/usr/bin/env python3

import argparse
import subprocess
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555, centers_555, edges_555, edges_recolor_pattern_555, wings_for_edges_pattern_555
from rubikscubennnsolver import reverse_steps
import os
import pickle
import logging
import sys

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

#centers_filename = "centers_solutions_555.txt"
#lookup_table_filename = "lookup-table-5x5x5-step100-stage-first-six-edges.txt"
centers_filename = args.centers_filename
centers_filename_pkl = centers_filename + ".pkl"
lookup_table_filename = args.lookup_table_filename

assert centers_filename
assert lookup_table_filename

if end:
    lookup_table_filename_new = "{}-{}-{}.new".format(lookup_table_filename, start, end)
else:
    lookup_table_filename_new = "{}.new".format(lookup_table_filename)


if os.path.exists(centers_filename_pkl):
    log.info("%s: begin pickle load" % centers_filename)
    centers_solutions = pickle.load(open(centers_filename_pkl, "rb"))
    log.info("%s: end pickle load" % centers_filename)
else:
    log.info("%s: begin load" % centers_filename)
    centers_solutions = {}
    with open(centers_filename, "r") as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(":")
            if state not in centers_solutions:
                centers_solutions[state] = []
            centers_solutions[state].append(steps)
    log.info("%s: end load" % centers_filename)

    log.info("%s: begin pickle dump" % centers_filename)
    pickle.dump(centers_solutions, open(centers_filename_pkl, "wb"))
    log.info("%s: end pickle dump" % centers_filename)

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
    with open(lookup_table_filename, "r") as fh:
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
            #log.info("{} centers solutions".format(len(centers_solutions[centers_state])))

            for centers_solution in centers_solutions[centers_state]:
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
                fh_new.write("\n".join(to_write) + "\n")
                fh_new.flush()
                to_write = []
                to_write_count = 0
                state_cache = {}

    if to_write_count:
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

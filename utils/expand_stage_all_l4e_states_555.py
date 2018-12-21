#!/usr/bin/env python3

import argparse
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555, centers_555, edges_555, edges_recolor_pattern_555, wings_for_edges_pattern_555
from rubikscubennnsolver import reverse_steps
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=0, help='starting line number')
parser.add_argument('--end', type=int, default=0, help='starting line number')
args = parser.parse_args()
start = args.start
end = args.end

if end:
    assert end > start, "--end must be greater than --start"

centers_filename = "centers_solutions_555.txt"
edges_filename = "lookup-table-5x5x5-step102-stage-first-and-second-four-edges.txt"

if end:
    edges_filename_new = "{}-{}-{}.new".format(edges_filename, start, end)
else:
    edges_filename_new = "{}.new".format(edges_filename)

log.info("%s: begin load" % centers_filename)
centers_solutions = {}
with open(centers_filename, "r") as fh:
    for line in fh:
        (state, steps) = line.rstrip().split(":")
        if state not in centers_solutions:
            centers_solutions[state] = []
        centers_solutions[state].append(steps)

        #if state == "BBBBUBBDBLLLULLRRRUFUUFUDRDRRRRRDLLLDDDLBBUUUFDFFDFFFF":
        #    break

log.info("%s: end load" % centers_filename)


cube = RubiksCube555(solved_555, order='URFDLB')
to_write = []
to_write_count = 0
BATCH_SIZE = 10000

with open(edges_filename_new, "w") as fh_new:
    with open(edges_filename, "r") as fh:
        for (line_number, line) in enumerate(fh):

            if start and line_number < start:
                continue

            if end and line_number > end:
                break

            (state, steps_to_solve) = line.rstrip().split(":")
            steps_to_solve = steps_to_solve.split()
            steps_to_scramble = reverse_steps(steps_to_solve)

            cube.re_init()
            for step in steps_to_scramble:
                cube.state = rotate_555(cube.state[:], step)
            cube.state[1:] = state
            #log.info("setup {}".format(steps_to_scramble))
            #cube.print_cube()

            tmp_state = cube.state[:]
            tmp_solution = cube.solution[:]
            centers_state = ''.join([cube.state[index] for index in centers_555])
            #log.info("centers solutions: {}".format(centers_solutions[centers_state]))

            for centers_solution in centers_solutions[centers_state]:
                cube.state = tmp_state[:]
                cube.solution = tmp_solution[:]
                centers_solution = centers_solution.split()

                for step in centers_solution:
                    cube.state = rotate_555(cube.state[:], step)

                #log.info("post centers solution {}".format(centers_solution))
                cube.print_cube()
                if not cube.centers_solved():
                    raise Exception("centers should be solved")

                edges_state = ''.join([cube.state[index] for index in edges_555])
                log.info("edges_state: {}\n".format(edges_state))
                to_write.append("{}:{}".format(edges_state, " ".join(reverse_steps(steps_to_scramble + centers_solution))))
                to_write_count += 1

            if line_number % 10000 == 0:
                log.info("{:,}".format(line_number))

            if to_write_count >= BATCH_SIZE:
                fh_new.write("\n".join(to_write) + "\n")
                fh_new.flush()
                to_write = []
                to_write_count = 0

    if to_write_count:
        fh_new.write("\n".join(to_write) + "\n")
        fh_new.flush()
        to_write = []
        to_write_count = 0

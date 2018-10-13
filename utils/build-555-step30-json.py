#!/usr/bin/env python3

from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, centers_555
import json
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)20s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

cube = RubiksCube555(solved_555, order='URFDLB')
data = {}
lt_centers = {}
lt_centers_max_depth = 4

# lookup-table-5x5x5-step30-ULFRBD-centers-solve-unstaged.txt.5-deep for example
filename = sys.argv[1]

with open(filename, "r") as fh:
    for line in fh:
        (state, steps) = line.strip().split(':')
        lt_centers[state] = len(steps.split())

with open(filename, "r") as fh:
    for (line_number, line) in enumerate(fh):
        (state, steps_to_solve) = line.strip().split(":")
        steps_to_solve = steps_to_solve.split()
        i = 0
        offset_555 = 0

        for x in range(6):
            cube.state[7 + offset_555] = state[i]
            i += 1

            cube.state[8 + offset_555] = state[i]
            i += 1

            cube.state[9 + offset_555] = state[i]
            i += 1

            cube.state[12 + offset_555] = state[i]
            i += 1

            cube.state[13 + offset_555] = state[i]
            i += 1

            cube.state[14 + offset_555] = state[i]
            i += 1

            cube.state[17 + offset_555] = state[i]
            i += 1

            cube.state[18 + offset_555] = state[i]
            i += 1

            cube.state[19 + offset_555] = state[i]
            i += 1

            offset_555 += 25

        #cube.print_cube()
        original_state = cube.state[:]
        data[state] = {}

        for step in moves_555:
            cube.state = original_state[:]
            cube.rotate(step)
            centers = ''.join([cube.state[x] for x in centers_555])
            centers_cost = lt_centers.get(centers, lt_centers_max_depth+1)
            #log.info("{} takes us to {} with cost of {}".format(step, centers, centers_cost))
            data[state][step] = centers_cost

        if line_number % 100000 == 0:
            log.info("{:,}".format(line_number))

with open(filename + ".json", "w") as fh:
    json.dump(data, fh)

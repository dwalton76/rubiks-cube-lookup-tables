#!/usr/bin/env python3

# This also needs to
# - resort
# - keep-best
# - pad-lines

# standard libraries
import logging
import sys

# rubiks cube libraries
from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    edges_recolor_pattern_555,
    solved_555,
    wings_for_edges_pattern_555,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

cube = RubiksCube555(solved_555, "URFDLB")
cube.cpu_mode = "fast"

filename = sys.argv[1]
filename_new = filename + ".new"
to_write = []
to_write_count = 0
line_number = 0
BATCH_SIZE = 100000

with open(filename_new, "w") as fh_new:
    with open(filename, "r") as fh:

        for line in fh:
            (state, steps_to_solve) = line.rstrip().split(":")
            steps_to_solve = steps_to_solve.split()
            steps_to_scramble = reverse_steps(steps_to_solve)
            cube.re_init()

            for step in steps_to_scramble:
                cube.rotate(step)

            cube.edges_flip_to_original_orientation()

            state = edges_recolor_pattern_555(cube.state[:])
            edges_state = "".join([state[index] for index in wings_for_edges_pattern_555])
            to_write.append("%s:%s" % (edges_state, " ".join(steps_to_solve)))
            to_write_count += 1

            if to_write_count == BATCH_SIZE:
                fh_new.write("\n".join(to_write) + "\n")
                to_write = []
                to_write_count = 0

            line_number += 1

            if line_number % 1000000 == 0:
                log.info(line_number)

        if to_write_count:
            fh_new.write("\n".join(to_write) + "\n")
            to_write = []

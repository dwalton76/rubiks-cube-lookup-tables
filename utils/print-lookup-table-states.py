#!/usr/bin/env python3

from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777
from pprint import pprint
import sys
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)20s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

filename = sys.argv[1]

with open(filename, "r") as fh:

    if '4x4x4' in filename:
        cube = RubiksCube444(solved_444, 'URFDLB')
    elif '5x5x5' in filename:
        cube = RubiksCube555(solved_555, 'URFDLB')
    elif '6x6x6' in filename:
        cube = RubiksCube666(solved_666, 'URFDLB')
    elif '7x7x7' in filename:
        cube = RubiksCube777(solved_777, 'URFDLB')
    else:
        raise Exception("What size cube?")

    for line in fh:
        (state, steps_to_solve) = line.strip().split(":")
        cube.re_init()
        cube.nuke_corners()
        cube.nuke_edges()
        #cube.nuke_centers()
        steps_to_solve = steps_to_solve.split()
        steps_to_scramble = reverse_steps(steps_to_solve)

        for step in steps_to_scramble:
            cube.rotate(step)

        cube.print_cube()
        log.info("steps_to_scramble %s" % " ".join(steps_to_scramble))
        log.info("steps_to_solve    %s\n\n" % " ".join(steps_to_solve))

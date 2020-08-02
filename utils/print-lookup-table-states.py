"""
Print the cubes for the states in the lookup table
"""

# standard libraries
import logging
import sys

# rubiks cube libraries
from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

filename = sys.argv[1]

with open(filename, "r") as fh:

    if "2x2x2" in filename:
        cube = RubiksCube222(solved_222, "URFDLB")
    elif "3x3x3" in filename:
        cube = RubiksCube333(solved_333, "URFDLB")
    elif "4x4x4" in filename:
        cube = RubiksCube444(solved_444, "URFDLB")
    elif "5x5x5" in filename:
        cube = RubiksCube555(solved_555, "URFDLB")
    elif "6x6x6" in filename:
        cube = RubiksCube666(solved_666, "URFDLB")
    elif "7x7x7" in filename:
        cube = RubiksCube777(solved_777, "URFDLB")
    else:
        raise Exception("What size cube?")

    for line in fh:
        (state, steps_to_solve) = line.strip().split(":")
        cube.re_init()
        cube.nuke_corners()
        # cube.nuke_edges()
        # cube.nuke_centers()
        steps_to_solve = steps_to_solve.split()
        steps_to_scramble = reverse_steps(steps_to_solve)

        for step in steps_to_scramble:
            cube.rotate(step)

        cube.print_cube()
        log.info("steps_to_scramble %s" % " ".join(steps_to_scramble))
        log.info("steps_to_solve    %s\n\n" % " ".join(steps_to_solve))

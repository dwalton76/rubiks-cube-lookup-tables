#!/usr/bin/env python3

# standard libraries
import logging
import sys

# rubiks cube libraries
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, f"[91m   {logging.getLevelName(logging.ERROR)}[0m")
logging.addLevelName(logging.WARNING, f"[91m {logging.getLevelName(logging.WARNING)}[0m")


filename = sys.argv[1]
with open(filename, "r") as fh:

    if "4x4x4" in filename:
        cube = RubiksCube444(solved_444, "URFDLB")
    elif "5x5x5" in filename:
        cube = RubiksCube555(solved_555, "URFDLB")
    elif "6x6x6" in filename:
        cube = RubiksCube666(solved_666, "URFDLB")
    elif "7x7x7" in filename:
        cube = RubiksCube777(solved_777, "URFDLB")
    else:
        raise Exception("What size cube?")

    # cube.print_cube()

    for line in fh:
        (state, order, _) = line.strip().split(",")
        state = state.replace("('", "").replace("'", "")
        cube.state = ["x"] + list(state)
        # pprint(cube.state)
        cube.print_cube()

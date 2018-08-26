#!/usr/bin/env python3

from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555
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
    cube = RubiksCube555(solved_555, 'URFDLB')
    #cube.print_cube()

    for line in fh:
        (state, order, _) = line.strip().split(",")
        state = state.replace("('", "").replace("'", "")
        cube.state = ["x"] + list(state)
        #pprint(cube.state)
        cube.print_cube()
        #break



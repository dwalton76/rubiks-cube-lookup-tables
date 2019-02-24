#!/usr/bin/env python3

import sys
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555

cube = RubiksCube555(solved_555, "URFDLB")

filename = sys.argv[1]
filename_new = filename + ".new"
print(filename_new)

with open(filename_new, "w") as fh_new:
    line_number = 0
    with open(filename, "r") as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(":")
            cube.solution = steps.split()
            cube.compress_solution()
            fh_new.write("%s:%s\n" % (state, " ".join(cube.solution)))
            line_number += 1

            if line_number % 1000000 == 0:
                print(line_number)

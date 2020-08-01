#!/usr/bin/env python3

# standard libraries
import shutil
import sys

filename = sys.argv[1]
filename_new = filename + ".new"
print(filename_new)

with open(filename_new, "w") as fh_new:
    line_number = 0
    with open(filename, "r") as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(":")

            if state.startswith("x."):
                state = state[2:]

            state = state.replace(".", "")

            fh_new.write("%s:%s\n" % (state, steps))
            line_number += 1

            if line_number % 1000000 == 0:
                print(line_number)

shutil.move(filename_new, filename)

"""
Create a .final copy of the lookup table that contains the solution length
instead of the solution steps
"""

# standard libraries
import sys

filename = sys.argv[1]

with open(filename + ".final", "w") as fh_final:
    with open(filename, "r") as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(":")
            fh_final.write("%s:%d\n" % (state, len(steps.split())))

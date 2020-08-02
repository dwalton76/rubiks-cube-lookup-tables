#!/usr/bin/env python3

"""
Merge the tables for 777 UD oblique edges
"""
# standard libraries
import itertools
import os
from subprocess import check_output

permutation = []
for x in itertools.permutations("UUUUDDDD"):
    permutation.append(x)
permutation = reversed(sorted(list(set(permutation))))


data = {}

for extension in permutation:
    extension = "".join(extension)
    filename = "lookup-table-7x7x7-step52-UD-solve-inner-center-and-oblique-edges-edges-only.txt." + extension

    if not os.path.isfile(filename):
        print("%s does not exist" % filename)
        continue

    with open(filename, "r") as fh:
        """
        xxxxLLLLxxxxRRRRxxxxxxxx:B2
        xxxxLLLRxxxxLRRRxxxxxxxx:Dw2 L' Fw2
        """
        print(filename)

        for line in fh:
            (state, steps) = line.strip().split(":")
            steps_length = len(steps.split())

            if state not in data:
                data[state] = steps
            else:
                min_steps_length = len(data[state].split())

                if steps_length < min_steps_length:
                    data[state] = steps

filename = "lookup-table-7x7x7-step52-UD-solve-inner-center-and-oblique-edges-edges-only.txt"
with open(filename, "w") as fh:
    print("%d entries to write" % len(data.keys()))

    for state in sorted(data.keys()):
        steps = data[state]
        fh.write("%s:%s\n" % (state, steps))

check_output("./utils/pad-lines.py %s" % filename, shell=True)

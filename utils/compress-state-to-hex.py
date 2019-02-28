#!/usr/bin/env python3

import sys
from buildercore import convert_state_to_hex

filename = sys.argv[1]
filename_new = filename + ".new"
print(filename_new)

with open(filename_new, "w") as fh_new:
    line_number = 0
    with open(filename, "r") as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(":")
            state = convert_state_to_hex(state)
            fh_new.write("%s:%s\n" % (state, steps))
            line_number += 1

            if line_number % 1000000 == 0:
                print(line_number)

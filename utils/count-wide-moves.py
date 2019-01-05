#!/usr/bin/env python3

import sys
odd = 0
even = 0

with open(sys.argv[1], "r") as fh:
    for line in fh:
        count = line.count("w")

        if count % 2 == 0:
            even += 1
        else:
            odd += 1
            line = line.strip()
            print("odd(%d): %s" % (count, line))

print("even : %d" % even)
print("odd: %d" % odd)


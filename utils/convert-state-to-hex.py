#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as fh_read:
    with open('hex.txt', 'w') as fh:
        for line in fh_read:
            (state, steps) = line.strip().split(':')
            state = state.replace('x', '0').replace('-', '0').replace('U', '1').replace('L', '1').replace('F', '1').replace('R', '1').replace('B', '1').replace('D', '1')

            if steps:
                fh.write("%s:%s\n" % (hex(int(state, 2))[2:], steps))
            else:
                fh.write("%s:\n" % hex(int(state, 2))[2:])

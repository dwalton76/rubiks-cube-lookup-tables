#!/usr/bin/env python3

import math
import sys

def convert_state_to_hex(state):
    """
    This assumes that state only has "x"s and Us or Ls or Fs or Rs or Bs or Ds

    >>> convert_state_to_hex("xxxU")
    '1'

    >>> convert_state_to_hex("UxUx")
    'a'

    >>> convert_state_to_hex("UUxUx")
    '1a'
    """
    state = state.replace('x', '0').replace('-', '0').replace('U', '1').replace('L', '1').replace('F', '1').replace('R', '1').replace('B', '1').replace('D', '1')
    hex_width = int(math.ceil(len(state)/4.0))
    hex_state = hex(int(state, 2))[2:]

    if hex_state.endswith('L'):
        hex_state = hex_state[:-1]

    return hex_state.zfill(hex_width)


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

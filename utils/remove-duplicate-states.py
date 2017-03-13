#!/usr/bin/env python2

"""
Assumes that filename is sorted
"""

import shutil
import sys

filename = sys.argv[1]
filename_new = filename + '.new'
prev_state = ''

with open(filename_new, 'w') as fh:
    with open(filename, 'r') as fh_read:
        for line in fh_read:
            (state, steps) = line.split(':')

            if state != prev_state:
                fh.write(line)

            prev_state = state

shutil.move(filename_new, filename)

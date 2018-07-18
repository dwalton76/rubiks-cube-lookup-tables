#!/usr/bin/env python3

import sys
import subprocess

filename = sys.argv[1]
filename_final = filename + '.final'

with open(filename_final, 'w') as fh_final:
    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(':')
            fh_final.write("%s:%d\n" % (state, len(steps.split())))

subprocess.check_output("./utils/pad-lines.py %s" % filename_final, shell=True)

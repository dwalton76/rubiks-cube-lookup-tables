#!/usr/bin/env python3

from rubikscubennnsolver.RubiksCube555 import get_edges_paired_binary_signature_555
import sys
import subprocess

filename = sys.argv[1]
filename_new = filename + '.new'
keepers = {}

with open(filename_new, 'w') as fh_new:
    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            signature = get_edges_paired_binary_signature_555(state)
            fh_new.write("%s_%s:%s\n" % (signature, state, steps))

subprocess.check_output("LC_ALL=C sort --temporary-directory=./tmp/ --output=%s %s" %
    (filename_new, filename_new), shell=True)

subprocess.check_output("./utils/pad-lines.py %s" % filename_new, shell=True)

#!/usr/bin/env python3

from rubikscubennnsolver.RubiksCube444 import get_edges_paired_binary_signature
import sys
import subprocess

filename = sys.argv[1]
filename_new = filename + '.new'
keepers = {}

with open(filename_new, 'w') as fh_new:
    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')

            # If we are running this against a file where we have already added some signatures
            # remove that signature so we can recalc (maybe we fixed a bug)
            if '_' in state:
                state = state.split('_')[1]

            signature = get_edges_paired_binary_signature(state)
            fh_new.write("%s_%s:%s\n" % (signature, state, steps))

subprocess.check_output("LC_ALL=C nice sort --temporary-directory=./tmp/ --output=%s %s" %
    (filename_new, filename_new), shell=True)

subprocess.check_output("./utils/pad-lines.py %s" % filename_new, shell=True)

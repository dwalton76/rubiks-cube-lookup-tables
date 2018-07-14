#!/usr/bin/env python3

import logging
import os
import subprocess
import sys


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

filename = sys.argv[1]
filename_best = filename + '.best'

if not os.path.exists(filename):
    print("ERROR: %s does not exist")
    sys.exit(1)

keeper_count = 0
line_count = 0
prev_state = None
prev_state_steps = None
prev_state_steps_len = None

with open(filename_best, 'w') as fh_best:
    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(':')
            steps_len = len(steps.split())

            if prev_state is None:
                prev_state = state
                prev_state_steps = steps
                prev_state_steps_len = steps_len
            else:
                if state == prev_state:
                    if steps_len < prev_state_steps_len:
                        prev_state_steps = steps
                        prev_state_steps_len = steps_len

                # changed states
                else:
                    fh_best.write("%s:%s\n" % (prev_state, prev_state_steps)) 
                    keeper_count += 1
                    prev_state = state
                    prev_state_steps = steps
                    prev_state_steps_len = steps_len

            line_count += 1

            # log an update every 1 million lines
            if line_count % 1000000 == 0:
                log.info("line %d, keepers %d" % (line_count, keeper_count))

    fh_best.write("%s:%s\n" % (prev_state, prev_state_steps)) 
    keeper_count += 1

subprocess.check_output("LC_ALL=C nice sort --parallel=4 --temporary-directory=./tmp/ --output=%s %s" % (filename_best, filename_best), shell=True)

# Make all lines the same length by adding whitespaces to the end. This is needed
# to simplify binary searching of the file.
subprocess.check_output(['nice', './utils/pad-lines.py', filename_best])

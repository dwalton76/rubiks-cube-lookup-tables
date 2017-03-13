#!/usr/bin/env python3

# Typical entry in lookup-table.txt is
# DDDDUDDDDLLLLLLLLLBBBBFFBFFRRRRRRRRRBBFFBFFBFUUUUDUUUUOOoPppQQsrRRVsqttTzUUSVvZWwXxxYYyuZW:L U Bw2 Lw2 F Rw2 Fw2

import logging
import subprocess

def centers_solved_555(state):
    if state[0:54] == 'UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD':
        return True
    return False


def steps_have_slice(steps):
    for step in steps.split():
        if 'w' in step:
            return True

    return False


def remove_trailing_outside_moves(steps):
    steps = steps.split()
    while 'w' not in steps[-1]:
        steps = steps[0:-1]
    return ' '.join(steps)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))


    keeper_count = 0
    line_count = 0

    with open('keepers.new', 'w') as fh_keepers:
        with open('lookup-table.txt', 'r') as fh:
            for line in fh:
                (state, steps) = line.rstrip().split(':')

                if centers_solved_555(state) and steps_have_slice(steps):

                    # The first 54 characters are the centers state
                    edges = ''.join(state[54:])

                    steps = remove_trailing_outside_moves(steps).split()

                    # We know the centers are solved so no need to write the centers state to the file
                    fh_keepers.write("%s:%s\n" % (edges, ' '.join(steps)))
                    keeper_count += 1

                line_count += 1

                # log an update every 1 million lines
                if line_count % 1000000 == 0:
                    log.info("line %d, keepers %d" % (line_count, keeper_count))

    subprocess.check_output("LC_ALL=C nice sort --parallel=4 --temporary-directory=./tmp/ --output=keepers.new keepers.new", shell=True)

    # Make all lines the same length by adding whitespaces to the end. This is needed
    # to simplify binary searching of the file.
    subprocess.check_output(['nice', './utils/pad_lines.py', 'keepers.new'])

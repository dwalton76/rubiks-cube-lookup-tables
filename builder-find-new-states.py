#!/usr/bin/env python3

"""
Given two lookup-table files (A & B), find all of the new cube states in B that
are not in A and write them to an output file.
"""

from buildercore import reverse_steps
import argparse
import logging
import os
import sys

def advance_filehandle(fh):
    try:
        line = next(fh)
        line = line.strip()
    except StopIteration:
        line = None

    return line


def advance_filehandle_to_state_change(state, fh):
    prev_state = state

    while True:
        line = advance_filehandle(fh)

        if line is None:
            break
        else:
            (state, _) = line.strip().split(':')

            if state != prev_state:
                break

            prev_state = state

    return line


def diff_states(filenameA, filenameB, outputfile):

    if not os.path.isfile(filenameA):
        # touch the file so the while loop below can do its magic
        with open(filenameA, 'w') as fhA:
            pass

    if not os.path.isfile(filenameB):
        raise Exception("%s does not exists" % filenameB)

    with open(filenameA, 'r') as fhA,\
         open(filenameB, 'r') as fhB,\
         open(outputfile, 'w') as fh:
        lineA = advance_filehandle(fhA)
        lineB = advance_filehandle(fhB)

        # filenameB is emtpy
        if lineB:
            (stateB, steps_to_scrambleB) = lineB.split(':')
        else:
            return

        # filenameA is emtpy
        if lineA:
            (stateA, steps_to_scrambleA) = lineA.split(':')
        else:
            stateA = None

        while lineB:

            # We have hit the end of filenameA so everything left in filenameB is missing from filenameA
            if lineA is None:
                fh.write("%s:%s\n" % (stateB, ' '.join(reverse_steps(steps_to_scrambleB.split()))))
                lineB = advance_filehandle_to_state_change(stateB, fhB)

                if lineB:
                    (stateB, steps_to_scrambleB) = lineB.split(':')
                else:
                    break

            elif stateA < stateB:
                lineA = advance_filehandle(fhA)

                if lineA:
                    (stateA, steps_to_scrambleA) = lineA.split(':')
                else:
                    stateA = None

            elif stateA == stateB:
                #log.info("stateA == stateB, advance both filehandles")
                lineA = advance_filehandle(fhA)
                lineB = advance_filehandle_to_state_change(stateB, fhB)

                if lineA:
                    (stateA, steps_to_scrambleA) = lineA.split(':')
                else:
                    stateA = None

                if lineB:
                    (stateB, steps_to_scrambleB) = lineB.split(':')
                else:
                    stateB = None

            else:
                while stateB < stateA:
                    fh.write("%s:%s\n" % (stateB, ' '.join(reverse_steps(steps_to_scrambleB.split()))))
                    #log.info("stateB < stateA writing %s" % lineB)
                    lineB = advance_filehandle_to_state_change(stateB, fhB)

                    if lineB:
                        (stateB, steps_to_scrambleB) = lineB.split(':')
                    else:
                        stateB = None
                        break


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    parser = argparse.ArgumentParser()
    parser.add_argument('filenameA', type=str, help='filenameA')
    parser.add_argument('filenameB', type=str, help='filenameB')
    parser.add_argument('outputfile', type=str, help='output file')
    args = parser.parse_args()

    diff_states(args.filenameA, args.filenameB, args.outputfile)

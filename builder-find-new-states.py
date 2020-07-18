#!/usr/bin/env python3.6

"""
Given two lookup-table files (A & B), find all of the new cube states in B that
are not in A and write them to an output file.
"""

from buildercore import reverse_steps, WRITE_BATCH_SIZE
import argparse
import logging
import os
import sys

def advance_filehandle(fh):
    try:
        line = next(fh)
        # line = line.rstrip()
    except StopIteration:
        line = None

    return line


def advance_filehandle_to_state_change(current_state, fh):

    while True:
        line = advance_filehandle(fh)

        if line is None:
            break
        else:
            state = line.split(':')[0]

            if state != current_state:
                break

    return line


def diff_states(filenameA, filenameB, outputfile):

    if not os.path.isfile(filenameA):
        # touch the file so the while loop below can do its magic
        with open(filenameA, 'w') as fhA:
            pass

    if not os.path.isfile(filenameB):
        raise Exception("%s does not exists" % filenameB)

    to_write = []
    to_write_count = 0

    with open(filenameA, 'r') as fhA,\
         open(filenameB, 'r') as fhB,\
         open(outputfile, 'w') as fh:
        lineA = advance_filehandle(fhA)
        lineB = advance_filehandle(fhB)

        if lineB:
            (stateB, steps_to_scrambleB) = lineB.split(':')
        # filenameB is empty
        else:
            return

        if lineA:
            (stateA, steps_to_scrambleA) = lineA.split(':')
        # filenameA is empty
        else:
            stateA = None

        while lineB:

            # We have hit the end of filenameA so everything left in filenameB is missing from filenameA
            if lineA is None:
                to_write.append("%s:%s" % (stateB, ' '.join(reverse_steps(steps_to_scrambleB.split()))))
                to_write_count += 1

                if to_write_count >= WRITE_BATCH_SIZE:
                    fh.write("\n".join(to_write))
                    fh.write("\n")
                    to_write = []
                    to_write_count = 0

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

            # stateA > stateB
            else:
                while stateA > stateB:
                    to_write.append("%s:%s" % (stateB, ' '.join(reverse_steps(steps_to_scrambleB.split()))))
                    to_write_count += 1

                    if to_write_count >= WRITE_BATCH_SIZE:
                        fh.write("\n".join(to_write))
                        fh.write("\n")
                        to_write = []
                        to_write_count = 0

                    #log.info("stateB < stateA writing %s" % lineB)
                    lineB = advance_filehandle_to_state_change(stateB, fhB)

                    if lineB:
                        (stateB, steps_to_scrambleB) = lineB.split(':')
                    else:
                        stateB = None
                        break

        if to_write_count:
            fh.write("\n".join(to_write))
            fh.write("\n")
            to_write = []
            to_write_count = 0


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

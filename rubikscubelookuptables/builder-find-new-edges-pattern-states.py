#!/usr/bin/env python3

"""
Given two lookup-table files (A & B), find all of the new cube states in B that
are not in A and write them to an output file.
"""

# standard libraries
import argparse
import logging
import os

# rubiks cube libraries
from rubikscubelookuptables.buildercore import reverse_steps


def advance_filehandle(fh):
    try:
        line = next(fh)
        line = line.strip()
    except StopIteration:
        line = None

    return line


def advance_filehandle_to_edges_pattern_change(pattern, fh):
    prev_pattern = pattern

    while True:
        line = advance_filehandle(fh)

        if line is None:
            break
        else:
            (pattern, state, moves) = line.strip().split(":")

            if pattern != prev_pattern:
                break

            prev_pattern = pattern

    return line


def diff_states(filenameA, filenameB, outputfile):

    if not os.path.isfile(filenameA):
        # touch the file so the while loop below can do its magic
        with open(filenameA, "w") as fhA:
            pass

    if not os.path.isfile(filenameB):
        raise Exception(f"{filenameB} does not exists")

    with open(filenameA, "r") as fhA, open(filenameB, "r") as fhB, open(outputfile, "w") as fh:
        lineA = advance_filehandle(fhA)
        lineB = advance_filehandle(fhB)

        # filenameB is emtpy
        if lineB:
            (patternB, stateB, steps_to_scrambleB) = lineB.split(":")
        else:
            return

        # filenameA is emtpy
        if lineA:
            (patternA, stateA, steps_to_scrambleA) = lineA.split(":")
        else:
            stateA = None

        while lineB:

            # We have hit the end of filenameA so everything left in filenameB is missing from filenameA
            if lineA is None:
                fh.write(f"{patternB}:{stateB}:{' '.join(reverse_steps(steps_to_scrambleB.split()))}\n")
                lineB = advance_filehandle_to_edges_pattern_change(patternB, fhB)

                if lineB:
                    (patternB, stateB, steps_to_scrambleB) = lineB.split(":")
                else:
                    break

            elif patternA < patternB:
                lineA = advance_filehandle(fhA)

                if lineA:
                    (patternA, stateA, steps_to_scrambleA) = lineA.split(":")
                else:
                    patternA = None
                    stateA = None

            elif patternA == patternB:
                lineA = advance_filehandle(fhA)
                lineB = advance_filehandle_to_edges_pattern_change(patternB, fhB)

                if lineA:
                    (patternA, stateA, steps_to_scrambleA) = lineA.split(":")
                else:
                    patternA = None
                    stateA = None  # noqa: F841

                if lineB:
                    (patternB, stateB, steps_to_scrambleB) = lineB.split(":")
                else:
                    patternB = None
                    stateB = None

            else:
                while patternB < patternA:
                    fh.write(f"{patternB}:{stateB}:{' '.join(reverse_steps(steps_to_scrambleB.split()))}\n")
                    # log.info("stateB < stateA writing %s" % lineB)
                    lineB = advance_filehandle_to_edges_pattern_change(patternB, fhB)

                    if lineB:
                        (patternB, stateB, steps_to_scrambleB) = lineB.split(":")
                    else:
                        patternB = None
                        stateB = None
                        break


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)24s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, f"[91m   {logging.getLevelName(logging.ERROR)}[0m")
    logging.addLevelName(logging.WARNING, f"[91m {logging.getLevelName(logging.WARNING)}[0m")

    parser = argparse.ArgumentParser()
    parser.add_argument("filenameA", type=str, help="filenameA")
    parser.add_argument("filenameB", type=str, help="filenameB")
    parser.add_argument("outputfile", type=str, help="output file")
    args = parser.parse_args()

    diff_states(args.filenameA, args.filenameB, args.outputfile)

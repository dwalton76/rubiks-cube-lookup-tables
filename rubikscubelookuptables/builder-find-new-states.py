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
from rubikscubelookuptables.buildercore import WRITE_BATCH_SIZE, reverse_steps


def advance_filehandle(fh):
    try:
        line = next(fh)
    except StopIteration:
        line = None

    return line


def advance_filehandle_to_state_change(state_length, current_state, fh):
    while True:
        try:
            line = next(fh)

            if line[0:state_length] != current_state:
                break
        except StopIteration:
            line = None
            break

    return line


def diff_states(filenameA, filenameB, outputfile):
    if not os.path.isfile(filenameA):
        # touch the file so the while loop below can do its magic
        with open(filenameA, "w") as fhA:
            pass

    if not os.path.isfile(filenameB):
        raise Exception(f"{filenameB} does not exists")

    to_write = []
    to_write_count = 0

    with open(filenameA, "r") as fhA, open(filenameB, "r") as fhB, open(outputfile, "w") as fh:
        lineA = advance_filehandle(fhA)
        lineB = advance_filehandle(fhB)

        if lineB:
            (stateB, steps_to_scrambleB) = lineB.split(":")
        # filenameB is empty
        else:
            return

        if lineA:
            (stateA, steps_to_scrambleA) = lineA.split(":")
        # filenameA is empty
        else:
            stateA = None

        if stateA:
            state_length = len(stateA)
        elif stateB:
            state_length = len(stateB)
        else:
            raise Exception("should not be here")

        while lineB:
            # We have hit the end of filenameA so everything left in filenameB is missing from filenameA
            if lineA is None:
                steps_to_solve = " ".join(reverse_steps(steps_to_scrambleB.split()))
                to_write.append(f"{stateB}:{steps_to_solve}")
                to_write_count += 1

                if to_write_count >= WRITE_BATCH_SIZE:
                    fh.write("\n".join(to_write))
                    fh.write("\n")
                    to_write = []
                    to_write_count = 0

                lineB = advance_filehandle_to_state_change(state_length, stateB, fhB)

                if lineB:
                    (stateB, steps_to_scrambleB) = lineB.split(":")
                else:
                    break

            elif stateA < stateB:
                # Avoid this function call
                # lineA = advance_filehandle(fhA)
                try:
                    lineA = next(fhA)
                except StopIteration:
                    lineA = None

                if lineA:
                    (stateA, steps_to_scrambleA) = lineA.split(":")
                else:
                    stateA = None

            elif stateA == stateB:
                # log.info("stateA == stateB, advance both filehandles")

                # Avoid this function call
                # lineA = advance_filehandle(fhA)
                try:
                    lineA = next(fhA)
                except StopIteration:
                    lineA = None

                lineB = advance_filehandle_to_state_change(state_length, stateB, fhB)

                if lineA:
                    (stateA, steps_to_scrambleA) = lineA.split(":")
                else:
                    stateA = None

                if lineB:
                    (stateB, steps_to_scrambleB) = lineB.split(":")
                else:
                    stateB = None

            # stateA > stateB
            else:
                while stateA > stateB:
                    steps_to_solve = " ".join(reverse_steps(steps_to_scrambleB.split()))
                    to_write.append(f"{stateB}:{steps_to_solve}")
                    to_write_count += 1

                    if to_write_count >= WRITE_BATCH_SIZE:
                        fh.write("\n".join(to_write))
                        fh.write("\n")
                        to_write = []
                        to_write_count = 0

                    # log.info("stateB < stateA writing %s" % lineB)
                    lineB = advance_filehandle_to_state_change(state_length, stateB, fhB)

                    if lineB:
                        (stateB, steps_to_scrambleB) = lineB.split(":")
                    else:
                        stateB = None
                        break

        if to_write_count:
            fh.write("\n".join(to_write))
            fh.write("\n")
            to_write = []
            to_write_count = 0


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

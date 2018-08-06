#!/usr/bin/env python3

import argparse
import logging
import os
import re
import subprocess
import sys
from pprint import pformat
from builder import (
    lookup_tables,
    moves_2x2x2,
    moves_3x3x3,
    moves_4x4x4,
    moves_5x5x5,
    moves_6x6x6,
    moves_7x7x7,
)


def reverse_steps(steps):
    results = []
    for step in reversed(steps):
        if step.endswith("2"):
            pass
        elif step.endswith("'"):
            step = step[0:-1]
        else:
            step += "'"
        results.append(step)
    return results


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='The diff file to process')
    parser.add_argument('--output', type=str, help='The workq file to write to')
    parser.add_argument('--start', type=int, help='Line to start with')
    parser.add_argument('--end', type=int, help='Line to end with')
    parser.add_argument('--type', type=str, help='The type of lookup table to build')
    parser.add_argument('--max-depth', type=int, help='How deep we are willing to go')
    args = parser.parse_args()

    lookup_table_type = args.type
    lookup_table_filename_diff = args.input
    workq_filename = args.output

    if args.end:
        line_start = args.start
        line_end = args.end
        lines_to_crunch = line_end - line_start
    else:
        line_start = None
        line_end = None
        lines_to_crunch = 99999999

    lt = lookup_tables[args.type]
    lookup_table_add_count = 0
    line_number = 0
    workq_count = 0
    workq_add = []
    workq_add.append('INIT')
    prev_steps = None
    max_depth = args.max_depth
    centers_lookup_table = None
    args_type = args.type

    if not os.path.exists(lookup_table_filename_diff):
        print("ERROR: %s does not exist" % lookup_table_filename_diff)
        sys.exit(1)

    if lt['size'] == '2x2x2':
        moves = [x for x in moves_2x2x2 if x not in lt['illegal']]

    elif lt['size'] == '3x3x3':
        moves = [x for x in moves_3x3x3 if x not in lt['illegal']]

    elif lt['size'] == '4x4x4':
        moves = [x for x in moves_4x4x4 if x not in lt['illegal']]

    elif lt['size'] == '5x5x5':
        moves = [x for x in moves_5x5x5 if x not in lt['illegal']]

    elif lt['size'] == '6x6x6':
        moves = [x for x in moves_6x6x6 if x not in lt['illegal']]

    elif lt['size'] == '7x7x7':
        moves = [x for x in moves_7x7x7 if x not in lt['illegal']]

    else:
        raise Exception("Add support for size %s" % lt['size'])

    special_case_777 = False

    if args_type in ('7x7x7-UD-oblique-edge-pairing',
                     '7x7x7-UD-oblique-edge-pairing-middle-only',
                     '7x7x7-UD-oblique-edge-pairing-left-only',
                     '7x7x7-UD-oblique-edge-pairing-right-only',
                     '7x7x7-LR-oblique-edge-pairing',
                     '7x7x7-LR-oblique-edge-pairing-middle-only',
                     '7x7x7-LR-oblique-edge-pairing-left-only',
                     '7x7x7-LR-oblique-edge-pairing-right-only'):
        special_case_777 = True

    centers_lookup_table = None
    line_number = 0

    with open(lookup_table_filename_diff, 'r') as fh_diff:
        pruned = 0
        kept = 0
        log.info("0/%d '+' lines from lookup-table.txt processed" % lines_to_crunch)

        for line in fh_diff:

            if line_end:
                if line_number < line_start:
                    line_number += 1
                    #log.info("SKIP %d" % line_number)
                    continue

                elif line_number > line_end:
                    #log.info("DONE %d" % line_number)
                    break

            #log.info("LINE %d" % line_number)
            line = line.strip()
            line_number += 1
            lookup_table_add_count += 1
            (state, steps) = line.split(':')

            steps = steps.split()
            steps = reverse_steps(steps)
            steps_str = ' '.join(steps)

            if lookup_table_add_count % 1000000 == 0:
                log.info("%d/%d '+' lines from lookup-table.txt processed (kept %d, pruned %d)" % (lookup_table_add_count, lines_to_crunch, kept, pruned))

            last_step = steps[-1]

            for next_step in moves:

                # Special case, we must preserve the outer UD oblique edges that have already been paired
                if special_case_777:
                    if next_step == "3Rw2":
                        next_step = ["3Rw2", "3Lw2"]

                    elif next_step == "3Lw2":
                        next_step = ["3Lw2", "3Rw2"]

                    elif next_step == "3Fw2":
                        next_step = ["3Fw2", "3Bw2"]

                    elif next_step == "3Bw2":
                        next_step = ["3Bw2", "3Fw2"]

                    elif next_step == "3Uw2":
                        next_step = ["3Uw2", "3Dw2"]

                    elif next_step == "3Dw2":
                        next_step = ["3Dw2", "3Uw2"]

                    elif next_step == "3Uw":
                        next_step = ["3Uw", "3Dw'"]

                    elif next_step == "3Uw'":
                        next_step = ["3Uw'", "3Dw"]

                    elif next_step == "3Dw":
                        next_step = ["3Dw", "3Uw'"]

                    elif next_step == "3Dw'":
                        next_step = ["3Dw'", "3Uw"]

                    if isinstance(next_step, list):
                        combined_steps = steps + next_step
                    else:
                        combined_steps = steps + [next_step]

                else:
                    combined_steps = steps + [next_step]

                if prev_steps is not None and combined_steps[0:-1] != prev_steps[0:-1]:
                    workq_add.append('INIT')

                # batch the writes
                workq_add.append(' '.join(combined_steps))
                workq_count += 1
                prev_steps = combined_steps

                if workq_count % 10000 == 0:
                    with open(workq_filename, 'a') as fh_workq:
                        fh_workq.write('\n'.join(workq_add) + '\n')
                    workq_add = []

        if pruned:
            log.info("%s: kept %d, pruned %d" % (workq_filename, kept, pruned))

        if workq_add:
            with open(workq_filename, 'a') as fh_workq:
                fh_workq.write('\n'.join(workq_add) + '\n')

    print("%s: added %d\n" % (workq_filename, lookup_table_add_count))

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


centers_solved_states_444 = set()
centers_solved_states_444.add('UUUULLLLFFFFRRRRBBBBDDDD')
centers_solved_states_444.add('UUUUFFFFRRRRBBBBLLLLDDDD')
centers_solved_states_444.add('UUUURRRRBBBBLLLLFFFFDDDD')
centers_solved_states_444.add('UUUUBBBBLLLLFFFFRRRRDDDD')
centers_solved_states_444.add('DDDDLLLLBBBBRRRRFFFFUUUU')
centers_solved_states_444.add('DDDDBBBBRRRRFFFFLLLLUUUU')
centers_solved_states_444.add('DDDDRRRRFFFFLLLLBBBBUUUU')
centers_solved_states_444.add('DDDDFFFFLLLLBBBBRRRRUUUU')
centers_solved_states_444.add('LLLLUUUUBBBBDDDDFFFFRRRR')
centers_solved_states_444.add('LLLLBBBBDDDDFFFFUUUURRRR')
centers_solved_states_444.add('LLLLDDDDFFFFUUUUBBBBRRRR')
centers_solved_states_444.add('LLLLFFFFUUUUBBBBDDDDRRRR')
centers_solved_states_444.add('FFFFLLLLDDDDRRRRUUUUBBBB')
centers_solved_states_444.add('FFFFDDDDRRRRUUUULLLLBBBB')
centers_solved_states_444.add('FFFFRRRRUUUULLLLDDDDBBBB')
centers_solved_states_444.add('FFFFUUUULLLLDDDDRRRRBBBB')
centers_solved_states_444.add('RRRRDDDDBBBBUUUUFFFFLLLL')
centers_solved_states_444.add('RRRRBBBBUUUUFFFFDDDDLLLL')
centers_solved_states_444.add('RRRRUUUUFFFFDDDDBBBBLLLL')
centers_solved_states_444.add('RRRRFFFFDDDDBBBBUUUULLLL')
centers_solved_states_444.add('BBBBUUUURRRRDDDDLLLLFFFF')
centers_solved_states_444.add('BBBBRRRRDDDDLLLLUUUUFFFF')
centers_solved_states_444.add('BBBBDDDDLLLLUUUURRRRFFFF')
centers_solved_states_444.add('BBBBLLLLUUUURRRRDDDDFFFF')


def centers_solved_444(state):
    if state[0:24] in centers_solved_states_444:
        return True
    return False

def centers_solved_555(state):
    if state[0:54] == 'UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD':
        return True
    return False


def load_centers_lookup_table_444():
    """
    lookup-table-4x4x4-step30-ULFRBD-centers-solve-with-edges-oriented.txt
    ======================================================================
    1 steps has 4 entries (0 percent, 0.00x previous step)
    2 steps has 34 entries (0 percent, 8.50x previous step)
    3 steps has 247 entries (0 percent, 7.26x previous step)
    4 steps has 1282 entries (2 percent, 5.19x previous step)
    5 steps has 4844 entries (8 percent, 3.78x previous step)
    6 steps has 11821 entries (20 percent, 2.44x previous step)
    7 steps has 17486 entries (29 percent, 1.48x previous step)
    8 steps has 15121 entries (25 percent, 0.86x previous step)
    9 steps has 6889 entries (11 percent, 0.46x previous step)
    10 steps has 1063 entries (1 percent, 0.15x previous step)
    11 steps has 9 entries (0 percent, 0.01x previous step)

    Total: 58800 entries
    Average: 7.095017 moves
    """
    log.info("load_centers_lookup_table_444() start")
    result = {}
    with open('lookup-table-4x4x4-step30-ULFRBD-centers-solve-with-edges-oriented.txt', 'r') as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            result[state] = len(steps.split())
    log.info("load_centers_lookup_table_444() end")
    return result


def load_centers_lookup_table_555():
    """
    lookup-table-5x5x5-step30-ULFRBD-centers-solve.txt
    ==================================================
    """
    log.info("load_centers_lookup_table_555() start")
    result = {}
    with open('lookup-table-5x5x5-step30-ULFRBD-centers-solve.txt', 'r') as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            result[state] = len(steps.split())
    log.info("load_centers_lookup_table_555() end")
    return result


def load_centers_unstaged_lookup_table_555():
    """
    lookup-table-5x5x5-step30-ULFRBD-centers-solve.txt
    ==================================================
    """
    log.info("load_centers_unstaged_lookup_table_555() start")
    result = {}
    with open('lookup-table-5x5x5-step30-ULFRBD-centers-solve-unstaged.txt', 'r') as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            result[state] = len(steps.split())
    log.info("load_centers_unstaged_lookup_table_555() end")
    return result


type_edges_444 = (
    '4x4x4-edges',
)

type_edges_all_turns_555 = (
    '5x5x5-stage-first-four-edges',
    '5x5x5-stage-second-four-edges',
    '5x5x5-pair-last-four-edges',
    '5x5x5-stage-all-edges',
)

type_edges_555 = (
)


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

            if (args_type in type_edges_444 or
                args_type in type_edges_555 or
                args_type in type_edges_all_turns_555):

                cost_to_here = len(steps)

                # We are at max-depth...nothing to add
                if cost_to_here == max_depth:
                    with open(workq_filename, 'w') as fh_workq:
                        fh_workq.write('INIT\n')
                    sys.exit(0)

                # Say our max-depth is 8 but we are only 3 steps in, since we are only 3 steps
                # in, the max steps it could take to solve any center is 3. Don't bother doing
                # any pruning work until cost_to_here is more than half of our max_depth.
                if (cost_to_here * 2) > max_depth:

                    if args_type in type_edges_444:
                        centers = ''.join(state[0:24])
                    elif args_type in type_edges_555 or args_type in type_edges_all_turns_555:
                        centers = ''.join(state[0:54])
                    else:
                        raise Exception("we should not be here")

                    if ((args_type in type_edges_444 and centers_solved_444(state)) or
                        (args_type in type_edges_555 and centers_solved_555(state)) or
                        (args_type in type_edges_all_turns_555 and centers_solved_555(state))):
                        costs_to_solve_these_centers = 0
                    else:
                        if centers_lookup_table is None:
                            if args_type in type_edges_444:
                                centers_lookup_table = load_centers_lookup_table_444()

                            elif args_type in type_edges_all_turns_555:
                                centers_lookup_table = load_centers_unstaged_lookup_table_555()

                            elif args_type in type_edges_555:
                                centers_lookup_table = load_centers_lookup_table_555()

                            else:
                                raise Exception("we should not be here")

                        costs_to_solve_these_centers = centers_lookup_table.get(centers)

                        if costs_to_solve_these_centers is None:
                            if args_type in type_edges_444:
                                raise Exception("we should never get a miss for 4x4x4 staged centers solve table (%s)" % centers)

                            elif args_type in type_edges_all_turns_555:
                                costs_to_solve_these_centers = 6

                            # These centers tables are only built 6-deep so if we get a miss
                            # we know the cost is at least 7.
                            elif args_type in type_edges_555:
                                costs_to_solve_these_centers = 7

                            else:
                                raise Exception("we should not be here")

                    # If the centers are so scrambled that we cannot solve them by the time we
                    # reach max_depth steps then prune this branch
                    if (cost_to_here + costs_to_solve_these_centers) > max_depth:
                        #log.info("prune %s, cost %d" % (centers, costs_to_solve_these_centers))
                        pruned += 1
                        continue

                    else:
                        kept += 1

                else:
                    kept += 1

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

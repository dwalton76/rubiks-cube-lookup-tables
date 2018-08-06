#!/usr/bin/env python3

from collections import deque
from pprint import pformat
from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555, centers_555, edges_555
import argparse
import logging
import os
import shutil
import subprocess
import sys


def chop_trailing_outer_layer_steps(steps):
    last_w_index = 0

    for (index, step) in enumerate(steps):
        if "w" in step:
            last_w_index = index

    #log.info("chop_trailing_outer_layer_steps stesp %s, last_w_index %d" % (pformat(steps), last_w_index))
    return steps[0:last_w_index+1]


def file_line_count(filename):
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename) as fh:
            for (i, l) in enumerate(fh):
                pass
        return i + 1
    else:
        return 0


def step_sequence_is_interesting(steps):
    """
    Saving "Uw2 U' Uw2" isn't all that interesting.

    Neither is "Uw D' U2 Uw'" so change D->U, etc when calculating
    the number of layers involved.
    """
    result = set()

    for step in steps:
        step = step.replace("w", "").replace("'", "").replace("2", "")
        step = step.replace("D", "U").replace("R", "L").replace("B", "F")
        result.update(step)

    #if len(steps) >= 4:
    #    log.info("steps %s, result %s" % (pformat(steps), pformat(result)))
    return len(result) > 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    parser = argparse.ArgumentParser()
    parser.add_argument('depth', type=int, default=None, help='The number of moves deep to explore')
    parser.add_argument('--min-wide-turns', type=int, default=0, help='Min number of wide turns to make')
    args = parser.parse_args()

    # Load the lt_centers dictionary
    lt_centers = {}
    lt_centers_max_depth = 5
    lt_centers_filename = "lookup-table-5x5x5-step30-ULFRBD-centers-solve-unstaged.txt"
    log.info("begin loading %s" % lt_centers_filename)

    if not os.path.exists(lt_centers_filename):
        log.info("Unzipping %s.gz" % lt_centers_filename)
        subprocess.check_output(["gunzip", "--keep", lt_centers_filename + ".gz"])

    with open(lt_centers_filename, "r") as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            lt_centers[state] = len(steps.split())

    log.info("end loading %s" % lt_centers_filename)


    # Init the workq
    workq = deque()
    for step in moves_555:
        if "w" in step:
            workq.append((1, step))


    # Init misc variables
    cube = RubiksCube555(solved_555, order='URFDLB')
    depth = 1
    kept = 0
    total_processed = 0
    processed = 0
    pruned = 0
    max_depth = args.depth
    min_wide_turns = args.min_wide_turns
    keepers = []
    keepers_count = 0
    keepers_filename = "keepers_555.txt"
    workq_filename = "workq.txt"

    next_workq = []
    next_workq_count = 0

    if os.path.exists(keepers_filename):
        os.unlink(keepers_filename)

    if os.path.exists(workq_filename):
        os.unlink(workq_filename)

    WORKQ_BATCH_SIZE = 50000000
    KEEPERS_BATCH_SIZE = 10000
    NEXT_WORKQ_BATCH_SIZE = 10000
    prev_step_sequence = []
    prev_step_sequence_len = 0
    prev_step_sequence_state_before_last_move = None

    while workq:
        (_, step_sequence_str) = workq.popleft()
        step_sequence = step_sequence_str.split()
        len_step_sequence = len(step_sequence)
        cube.re_init()

        # The rotate_555() calls are the most expensive part so use some caching to try eliminate a good chunk of them
        # This took 5-deep from 4s to 2s
        # This took 6-deep from 51s to 28s (14x longer than 5-deep)
        # This took 7-deep from 10m to 4m 31s (9.6x longer than 6-deep)
        # 8-deep took 1hr 40m (22x longer than 8-deep)
        # 9-deep took 14hr 5m (8.4x longer than 9-deep)
        # 10-deep would take about 5 days
        if prev_step_sequence and len_step_sequence > 2 and step_sequence[0:-1] == prev_step_sequence[0:-1]:
            state_before_last_move = prev_step_sequence_state_before_last_move[:]
            cube.state = prev_step_sequence_state_before_last_move[:]
            cube.state = rotate_555(cube.state[:], step_sequence[-1])

        else:
            state_before_last_move = []

            for (index, step) in enumerate(step_sequence):
                cube.state = rotate_555(cube.state[:], step)

                if index == len_step_sequence - 2:
                    state_before_last_move = cube.state[:]

        if not workq:

            # Write whatever next_workq entries we have to the disk
            if next_workq_count:
                with open(workq_filename, "a") as fh:
                    fh.write("\n".join(next_workq) + "\n")
                next_workq = []
                next_workq_count = 0

            # Now load the first WORKQ_BATCH_SIZE entries from workq_filename onto our workq.
            # We do this because the workq gets so large we would run out of memory if
            # we loaded it all at once.
            if os.path.exists(workq_filename):
                with open(workq_filename, "r") as fh:
                    for (linenumber, line) in enumerate(fh):
                        workq.append((line.count(" ") + 1, line.strip()))

                        if linenumber == WORKQ_BATCH_SIZE:
                            break
                subprocess.check_output("tail -n +%d %s > %s.tmp" % (WORKQ_BATCH_SIZE, workq_filename, workq_filename), shell=True)
                shutil.move("%s.tmp" % workq_filename, workq_filename,)
                workq = deque(sorted(list(workq)))

        centers = ''.join([cube.state[x] for x in centers_555])

        # If the centers are solved, save this sequence
        if centers == "UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD":
            steps_to_write = chop_trailing_outer_layer_steps(step_sequence)

            # Only save the ones where more than one face was involved.
            if step_sequence_is_interesting(steps_to_write):
                keepers.append(" ".join(steps_to_write))
                keepers_count += 1

                if keepers_count >= KEEPERS_BATCH_SIZE:
                    with open(keepers_filename, "a") as fh:
                        fh.write("\n".join(keepers) + "\n")
                    keepers = []
                    keepers_count = 0

        # Print a message to the let user know we are at a new level
        if len_step_sequence != depth:
            workq_file_linecount = file_line_count(workq_filename)
            log.info("processed {:,} at depth {}, kept {:,}, pruned {:,}, workq has {:,} entries ({:,} in memory, {:,} on next_workq, {:,} on disk)".format(
                processed, depth, kept, pruned,
                len(workq) + next_workq_count + workq_file_linecount,
                len(workq), next_workq_count, workq_file_linecount
            ))
            depth = len_step_sequence
            total_processed += processed
            kept = 0
            processed = 0
            pruned = 0
        processed += 1
        prev_step_sequence_len = len_step_sequence
        prev_step_sequence = step_sequence[:]
        prev_step_sequence_state_before_last_move = state_before_last_move[:]

        # Add items to the workq
        if len_step_sequence < max_depth:
            centers_cost = lt_centers.get(centers, lt_centers_max_depth+1)

            if (len_step_sequence + centers_cost) > max_depth:
                pruned += 1
                continue
            else:
                kept += 1

            # Do not add a step if it is on the same face/layer as the last step in step_sequence
            prev_step = step_sequence[-1]

            wide_count = step_sequence_str.count("w")

            if wide_count % 2 == 0:
                wide_count_even = True
                wide_count_odd = False
            else:
                wide_count_even = False
                wide_count_odd = True

            if min_wide_turns:
                wide_turns_needed = min_wide_turns - wide_count

                if wide_turns_needed < 0:
                    wide_turns_needed = 0

                steps_remaining = max_depth - len_step_sequence

                if wide_turns_needed > steps_remaining:
                    continue

            # If we are building the workq for the last step, only add "w" moves. We will chop
            # all of the trailing outer later moves anyway so there is no need to do them.
            if len_step_sequence == max_depth - 1:
                for step in moves_555:

                    if steps_on_same_face_and_layer(prev_step, step):
                        continue

                    if "w" in step:

                        # This is the last step and we are only interested in sequences
                        # with an even number of wide turns so if the wide_count is already even
                        # do not bother with this step
                        if wide_count_even:
                            continue

                        if len_step_sequence >= 2 and "w" in step_sequence[-1] and "w" in step_sequence[-2]:
                            last_three_steps = [step_sequence[-2], step_sequence[-1], step]

                            # Prune off the branch if it is something like "Uw2 Dw Uw"
                            if not step_sequence_is_interesting(last_three_steps):
                                continue
                    else:
                        continue

                    next_workq.append(" ".join(step_sequence + [step,]))
                    next_workq_count += 1

            else:

                for step in moves_555:
                    if steps_on_same_face_and_layer(prev_step, step):
                        continue

                    # before
                    # 5-deep processed 72,378 total, took 4s
                    # 6-deep processed 1,203,732 total, took 1m 4s
                    #
                    # after
                    # 5-deep processed 63,792 total, took 3s
                    # 6-deep processed 1,081,152 total, took 57s
                    if "w" in step:

                        if len_step_sequence >= 2 and "w" in step_sequence[-1] and "w" in step_sequence[-2]:
                            last_three_steps = [step_sequence[-2], step_sequence[-1], step]

                            # Prune off the branch if it is something like "Uw2 Dw Uw"
                            if not step_sequence_is_interesting(last_three_steps):
                                continue

                    # If
                    # - this is an outer layer move
                    # - the centers on this side are solved and the edges are paired
                    #
                    # Then there is no need to do this move
                    #
                    # before
                    # 5-deep processed 363,654 total, took 18s
                    # 6-deep processed 5,109,768 total, took 4m 46s
                    #
                    # after
                    # 5-deep processed 72,378 total, took 4s
                    # 6-deep processed 1,203,732 total, took 1m 4s
                    #
                    else:
                        side = cube.sides[step[0]]

                        if side.centers_solved() and side.edges_paired():
                            continue

                    next_workq.append(" ".join(step_sequence + [step,]))
                    next_workq_count += 1

            # write our next_workq entries to disk so we don't run out of memory
            if next_workq_count >= NEXT_WORKQ_BATCH_SIZE:
                with open(workq_filename, "a") as fh:
                    fh.write("\n".join(next_workq) + "\n")
                next_workq = []
                next_workq_count = 0

    total_processed += processed
    log.info("processed {:,} at depth {}".format(processed, depth))
    log.info("processed {:,} total".format(total_processed))

    if keepers_count:
        with open(keepers_filename, "a") as fh:
            fh.write("\n".join(keepers) + "\n")

    if os.path.exists(keepers_filename):
        log.info("sort %s" % keepers_filename)
        subprocess.check_output("LC_ALL=C sort --temporary-directory=./tmp/ --output %s %s" % (keepers_filename, keepers_filename), shell=True)

        subprocess.check_output("uniq %s %s.uniq" % (keepers_filename, keepers_filename), shell=True)
        shutil.move("%s.uniq" % keepers_filename, keepers_filename,)
    else:
        log.info("did not find any keepers")

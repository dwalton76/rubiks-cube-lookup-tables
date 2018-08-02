#!/usr/bin/env python3

from collections import deque
from pprint import pformat
from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555, centers_555, edges_555
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


    if len(sys.argv) != 2:
        print("syntax is \n\n    bfs_555.py MAX_DEPTH\n\n")
        sys.exit(1)


    # Load the lt_centers dictionary
    lt_centers = {}
    lt_centers_max_depth = 5
    lt_centers_filename = "lookup-table-5x5x5-step30-ULFRBD-centers-solve-unstaged.txt"
    log.info("begin loading %s" % lt_centers_filename)

    with open(lt_centers_filename, "r") as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            lt_centers[state] = len(steps.split())

    log.info("end loading %s" % lt_centers_filename)


    # Init the workq
    workq = deque()
    for step in moves_555:
        if "w" in step:
            workq.append(step)


    # Init misc variables
    cube = RubiksCube555(solved_555, order='URFDLB')
    depth = 1
    kept = 0
    processed = 0
    pruned = 0
    max_depth = int(sys.argv[1])
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

    while workq:
        step_sequence_str = workq.popleft()
        step_sequence = step_sequence_str.split()
        cube.re_init()
        #log.info("step_sequence %s" % pformat(step_sequence))

        for step in step_sequence:
            cube.state = rotate_555(cube.state[:], step)
            #cube.rotate(step)

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
                        workq.append(line.strip())

                        if linenumber == WORKQ_BATCH_SIZE:
                            break
                subprocess.check_output("tail -n +%d %s > %s.tmp" % (WORKQ_BATCH_SIZE, workq_filename, workq_filename), shell=True)
                shutil.move("%s.tmp" % workq_filename, workq_filename,)

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
        len_step_sequence = len(step_sequence)

        if len_step_sequence != depth:
            workq_file_linecount = file_line_count(workq_filename)
            log.info("processed {:,} at depth {}, kept {:,}, pruned {:,}, workq has {:,} entries ({:,} in memory, {:,} on next_workq, {:,} on disk)".format(
                processed, depth, kept, pruned,
                len(workq) + next_workq_count + workq_file_linecount,
                len(workq), next_workq_count, workq_file_linecount
            ))
            depth = len_step_sequence
            kept = 0
            processed = 0
            pruned = 0
        processed += 1

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

            # If we are building the workq for the last step, only add "w" moves. We will chop
            # all of the trailing outer later moves so there is no need to do them.
            if len_step_sequence == max_depth - 1:
                for step in moves_555:

                    if "w" not in step:
                        continue

                    if not steps_on_same_face_and_layer(prev_step, step):
                        next_workq.append(" ".join(step_sequence + [step,]))
                        next_workq_count += 1
            else:
                for step in moves_555:
                    if not steps_on_same_face_and_layer(prev_step, step):
                        next_workq.append(" ".join(step_sequence + [step,]))
                        next_workq_count += 1

            # write our next_workq entries to disk so we don't run out of memory
            if next_workq_count >= NEXT_WORKQ_BATCH_SIZE:
                with open(workq_filename, "a") as fh:
                    fh.write("\n".join(next_workq) + "\n")
                next_workq = []
                next_workq_count = 0

    log.info("processed {:,} at depth {}".format(processed, depth))

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

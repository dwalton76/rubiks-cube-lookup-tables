#!/usr/bin/env python3

from buildercore import supported_sizes, WRITE_BATCH_SIZE, reverse_steps
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_222, moves_222, rotate_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333, moves_333, rotate_333
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444, edges_recolor_pattern_444, wings_444, centers_444
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    solved_555,
    moves_555,
    rotate_555,
    centers_555,
    edges_recolor_pattern_555,
    wings_555,
    midges_recolor_tuples_555,
)

from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666, moves_666, rotate_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777, moves_777, rotate_777
from pprint import pformat
import argparse
import json
import logging
import sys

log = logging.getLogger(__name__)

def get_odd_even(steps, layer):
    assert isinstance(steps, list)
    quarter_wide_turns = 0

    for step in steps:
        if "w" in step and not step.endswith("2"):

            if layer is None:
                if (step.startswith("U") or
                    step.startswith("L") or
                    step.startswith("F") or
                    step.startswith("R") or
                    step.startswith("B") or
                    step.startswith("D")):
                    quarter_wide_turns += 1

            else:
                if layer == "2":
                    if not step[0].isdigit():
                        quarter_wide_turns += 1
                else:
                    if step.startswith(layer):
                        quarter_wide_turns += 1

    if quarter_wide_turns % 2 == 0:
        return "even"
    else:
        return "odd"


def crunch_workq(size, inputfile, linewidth, start, end, outputfilebase, use_edges_pattern):
    assert isinstance(size, str)
    assert size in supported_sizes
    assert isinstance(inputfile, str)
    assert isinstance(outputfilebase, str)
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert start >= 0
    assert end >= start

    if size == '2x2x2':
        rotate_xxx = rotate_222
    elif size == '3x3x3':
        rotate_xxx = rotate_333
    elif size == '4x4x4':
        rotate_xxx = rotate_444
    elif size == '5x5x5':
        rotate_xxx = rotate_555
    elif size == '6x6x6':
        rotate_xxx = rotate_666
    elif size == '7x7x7':
        rotate_xxx = rotate_777
    else:
        raise Exception("we should not be here")

    to_write = []
    to_write_count = 0
    outputfile_index = 0

    #if "5x5x5-edges-last-twelve" in inputfile:
    #    exec_all_steps = True
    #else:
    #    exec_all_steps = False
    exec_all_steps = False

    with open(inputfile, 'r') as fh_input:

        # We add 1 here to account for the newline character
        fh_input.seek(start * (linewidth+1))

        for linenumber in range(start, end+1):
            line = next(fh_input)

            if use_edges_pattern:
                try:
                    (_, cube_state, moves_to_scramble) = line.rstrip().split(':')
                except Exception:
                    log.warning("ERROR on %d: %s" % (linenumber, line))
                    raise
            else:
                try:
                    (cube_state, moves_to_scramble) = line.rstrip().split(':')
                except Exception:
                    log.warning("ERROR on %d: %s" % (linenumber, line))
                    raise

            moves_to_scramble = moves_to_scramble.split()

            if exec_all_steps:
                cube_state = list(cube_state)

                for step in moves_to_scramble:
                    cube_state = rotate_xxx(cube_state[:], step)

            else:
                if moves_to_scramble:
                    if moves_to_scramble[-1] == "x2":
                        cube_state = rotate_xxx(list(cube_state), "x")
                        cube_state = rotate_xxx(list(cube_state), "x")
                    elif moves_to_scramble[-1] == "y2":
                        cube_state = rotate_xxx(list(cube_state), "y")
                        cube_state = rotate_xxx(list(cube_state), "y")
                    elif moves_to_scramble[-1] == "z2":
                        cube_state = rotate_xxx(list(cube_state), "z")
                        cube_state = rotate_xxx(list(cube_state), "z")
                    else:
                        cube_state = rotate_xxx(list(cube_state), moves_to_scramble[-1])
                else:
                    cube_state = list(cube_state)

            if use_edges_pattern:

                cube_state_string = ''.join(cube_state)

                if size == '4x4x4':
                    state_for_edges = edges_recolor_pattern_444(cube_state[:])
                    edges_pattern = ''.join([state_for_edges[square_index] for square_index in wings_444])
                    centers = ''.join([cube_state[x] for x in centers_444])
                elif size == '5x5x5':
                    state_for_edges = edges_recolor_pattern_555(cube_state[:])
                    edges_pattern = ''.join([state_for_edges[square_index] for square_index in wings_555])
                    centers = ''.join([cube_state[x] for x in centers_555])
                else:
                    raise Exception("Implement this")

                to_write.append("%s%s:%s:%s" % (centers, edges_pattern, cube_state_string, ' '.join(moves_to_scramble)))
                to_write_count += 1

            else:
                cube_state_string = ''.join(cube_state)

                if "6x6x6-LR-inner-x-center-stage" in inputfile or "6x6x6-UD-inner-x-centers-stage" in inputfile:
                    odd_even = get_odd_even(moves_to_scramble, "3")
                    to_write.append("%s_%s:%s" % (cube_state_string, odd_even, ' '.join(moves_to_scramble)))

                elif "5x5x5-lr-t-center-stage" in inputfile:
                    odd_even = get_odd_even(moves_to_scramble, "2")
                    to_write.append("%s_%s:%s" % (cube_state_string, odd_even, ' '.join(moves_to_scramble)))

                elif "4x4x4-LRFB-centers-stage" in inputfile:
                    odd_even = get_odd_even(moves_to_scramble, "2")
                    to_write.append("%s_%s:%s" % (cube_state_string, odd_even, ' '.join(moves_to_scramble)))

                else:
                    to_write.append("%s:%s" % (cube_state_string, ' '.join(moves_to_scramble)))

                to_write_count += 1

            #if to_write_count >= WRITE_BATCH_SIZE or linenumber == end:
            if to_write_count >= WRITE_BATCH_SIZE:
                to_write.sort()
                outputfile = outputfilebase + ".%04d" % outputfile_index
                outputfile_index += 1

                with open(outputfile, 'w') as fh_output:
                    fh_output.write("\n".join(to_write) + "\n")

                to_write = []
                to_write_count = 0

        if to_write:
            to_write.sort()
            outputfile = outputfilebase + ".%04d" % outputfile_index
            outputfile_index += 1

            with open(outputfile, 'w') as fh_output:
                fh_output.write("\n".join(to_write) + "\n")

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
    parser.add_argument('size', type=str, help='Cube size')
    parser.add_argument('inputfile', type=str, help='The workq file to crunch')
    parser.add_argument('linewidth', type=int, help='The width of a line in the file')
    parser.add_argument('start', type=int, help='The starting linenumber to crunch in inputfile')
    parser.add_argument('end', type=int, help='The final linenumber to crunch in inputfile')
    parser.add_argument('outputfile', type=str, help='The file to write results')
    parser.add_argument('--use-edges-pattern', default=False, action='store_true', help='use edges patterns')
    args = parser.parse_args()

    crunch_workq(args.size, args.inputfile, args.linewidth,
        args.start, args.end,
        args.outputfile,
        args.use_edges_pattern,
    )

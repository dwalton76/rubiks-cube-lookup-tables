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
    #tsai_phase3_orient_edges_555,
    centers_555,
    edges_recolor_without_midges_555,
    edges_recolor_with_midges_555,
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
                if step.startswith(layer):
                    quarter_wide_turns += 1

    if quarter_wide_turns % 2 == 0:
        return "even"
    else:
        return "odd"


midges_recolor_tuples_555 = (
    ('o', 3, 103), # upper
    ('p', 11, 28),
    ('q', 15, 78),
    ('r', 23, 53),

    ('s', 36, 115), # left
    ('t', 40, 61),

    ('u', 86, 65),  # right
    ('v', 90, 111),

    ('w', 128, 73), # down
    ('x', 136, 48),
    ('y', 140, 98),
    ('z', 148, 123)
)


wings_555= (
    2, 3, 4, # Upper
    6, 11, 16,
    10, 15, 20,
    22, 23, 24,

    31, 36, 41, # Left
    35, 40, 45,

    81, 86, 91, # Right
    85, 90, 95,

    127, 128, 129, # Down
    131, 136, 141,
    135, 140, 145,
    147, 148, 149
)

'''
wings_555= (
    ('0', 2, 104),  # upper
    ('1', 4, 102),
    ('2', 6, 27),
    ('3', 10, 79),
    ('4', 16, 29),
    ('5', 20, 77),
    ('6', 22, 52),
    ('7', 24, 54),

    ('8', 31, 110), # left
    ('9', 35, 56),
    ('a', 41, 120),
    ('b', 45, 66),

    ('c', 81, 60), # right
    ('d', 85, 106),
    ('e', 91, 70),
    ('f', 95, 116),

    ('g', 127, 72), # down
    ('h', 129, 74),
    ('i', 131, 49),
    ('j', 135, 97),
    ('k', 141, 47),
    ('l', 145, 99),
    ('m', 147, 124),
    ('n', 149, 122)
)
'''

def edges_recolor_pattern_555(state):
    (edge_index, square_index, partner_index) = midges_recolor_tuples_555[0]
    square_value = state[square_index]

    # If the middle edges pieces are all "." then we ignore them and recolor the
    # edges in terms of one edge piece as it relates to its partner piece.
    if square_value == '.':
        return edges_recolor_without_midges_555(state)

    # If the middle edges are not "." though then we return recolor each edge
    # as it relates to its midge.
    else:
        return edges_recolor_with_midges_555(state)


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

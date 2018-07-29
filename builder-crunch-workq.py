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


def crunch_workq(size, inputfile, linewidth, start, end, outputfilebase, use_edges_pattern, symmetries, color_symmetries):
    assert isinstance(size, str)
    assert size in supported_sizes
    assert isinstance(inputfile, str)
    assert isinstance(outputfilebase, str)
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert start >= 0
    assert end > start
    assert isinstance(symmetries, str)

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

    # Convert the sequences from strings to lists
    if symmetries:
        symmetries_final = []
        for seq in symmetries.strip().split(','):
            symmetries_final.append(seq.split())
        symmetries = symmetries_final
        #log.warning("symmetries: %s" % pformat(symmetries))

    to_write = []
    to_write_count = 0
    outputfile_index = 0

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
            cube_state = rotate_xxx(list(cube_state), moves_to_scramble[-1])

            if use_edges_pattern:

                if symmetries or color_symmetries:
                    results = []
                    cube_state_original = cube_state[:]

                    for seq in symmetries:
                        state = cube_state_original[:]

                        for step in seq:
                            state = rotate_xxx(state[:], step)

                        if size == '4x4x4':
                            state_for_edges = edges_recolor_pattern_444(state[:])
                            edges_pattern = ''.join([state_for_edges[square_index] for square_index in wings_444])
                            centers = ''.join([state[x] for x in centers_444])
                        elif size == '5x5x5':
                            state_for_edges = edges_recolor_pattern_555(state[:])
                            edges_pattern = ''.join([state_for_edges[square_index] for square_index in wings_555])
                            centers = ''.join([state[x] for x in centers_555])
                        else:
                            raise Exception("Implement this")

                        #log.info("move %s, symmetry %s, edges_pattern %s\n\n\n\n" % (moves_to_scramble[-1], ' '.join(seq), edges_pattern))
                        centers = centers.replace('.', '')
                        results.append((centers, edges_pattern, ''.join(state)))

                    if color_symmetries:
                        assert False, "Add support for --color-symmetries here"

                    results = sorted(results)[0]
                    (centers, edges_pattern, cube_state_string) = results
                    to_write.append("%s%s:%s:%s" % (centers, edges_pattern, cube_state_string, ' '.join(moves_to_scramble)))
                    to_write_count += 1
                else:
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
                if symmetries or color_symmetries:
                    results = []
                    cube_state_original = cube_state[:]

                    if not symmetries:
                        symmetries = [[]]

                    for seq in symmetries:
                        cube_state = cube_state_original[:]

                        for step in seq:
                            cube_state = rotate_xxx(cube_state[:], step)

                        if color_symmetries:
                            base_color_cube_state = cube_state[:]

                            # dwalton
                            for (colorA, colorB) in color_symmetries:
                                cube_state = base_color_cube_state[:]
                                cube_state = ''.join(cube_state[1:])
                                cube_state = cube_state.replace(colorA, 'Z')
                                cube_state = cube_state.replace(colorB, colorA)
                                cube_state = cube_state.replace('Z', colorB)
                                cube_state = ['x'] + list(cube_state)
                                #log.info("converted\n%s\nto\n%s\n\n" % (cube_state_original, tmp))
                                results.append(cube_state)
                        else:
                            results.append(cube_state)

                    results = sorted(results)
                    cube_state_string = ''.join(results[0])
                else:
                    cube_state_string = ''.join(cube_state)

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
    parser.add_argument('--symmetries', default='', type=str, help='cube symmetries to apply')
    parser.add_argument('--color-symmetries', default='', type=str, help='cube symmetries to apply')
    args = parser.parse_args()

    if args.color_symmetries:
        args.color_symmetries = json.loads(args.color_symmetries)
        #log.info(args.color_symmetries)

    crunch_workq(args.size, args.inputfile, args.linewidth,
        args.start, args.end,
        args.outputfile,
        args.use_edges_pattern,
        args.symmetries,
        args.color_symmetries,
    )

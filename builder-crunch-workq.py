#!/usr/bin/env python3

from buildercore import supported_sizes, WRITE_BATCH_SIZE, reverse_steps
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_222, moves_222, rotate_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333, moves_333, rotate_333
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444, edges_recolor_pattern_444, wings_444, centers_444
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555, tsai_phase2_orient_edges_555, centers_555
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666, moves_666, rotate_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777, moves_777, rotate_777
from pprint import pformat
import argparse
import logging

log = logging.getLogger(__name__)


edges_recolor_tuples_555 = (
    ('0', 2, 104), # upper
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


def edges_recolor_without_midges_555(state):
    edge_map = {
        'BD': [],
        'BL': [],
        'BR': [],
        'BU': [],
        'DF': [],
        'DL': [],
        'DR': [],
        'FL': [],
        'FR': [],
        'FU': [],
        'LU': [],
        'RU': []
    }

    for (edge_index, square_index, partner_index) in wings_555:
        square_value = state[square_index]
        partner_value = state[partner_index]
        wing_str = ''.join(sorted([square_value, partner_value]))

        if 'x' not in wing_str:
            edge_map[wing_str].append(edge_index)

    # Where is the other wing_str like us?
    for (edge_index, square_index, partner_index) in wings_555:
        square_value = state[square_index]
        partner_value = state[partner_index]
        wing_str = ''.join(sorted([square_value, partner_value]))

        if 'x' in wing_str:
            state[square_index] = 'x'
            state[partner_index] = 'x'
        else:
            for tmp_index in edge_map[wing_str]:
                if tmp_index != edge_index:
                    state[square_index] = tmp_index
                    state[partner_index] = tmp_index
                    break
            else:
                raise Exception("could not find tmp_index")

    return ''.join(state)


def edges_recolor_with_midges_555(state):
    midges_map = {
        'BD': None,
        'BL': None,
        'BR': None,
        'BU': None,
        'DF': None,
        'DL': None,
        'DR': None,
        'FL': None,
        'FR': None,
        'FU': None,
        'LU': None,
        'RU': None
    }

    for (edge_index, square_index, partner_index) in midges_recolor_tuples_555:
        square_value = state[square_index]
        partner_value = state[partner_index]
        wing_str = ''.join(sorted([square_value, partner_value]))
        midges_map[wing_str] = edge_index

        # We need to indicate which way the midge is rotated.  If the square_index contains
        # U, D, L, or R use the uppercase of the edge_index, if not use the lowercase of the
        # edge_index.
        if square_value == 'U':
            state[square_index] = edge_index.upper()
            state[partner_index] = edge_index.upper()
        elif partner_value == 'U':
            state[square_index] = edge_index
            state[partner_index] = edge_index
        elif square_value == 'D':
            state[square_index] = edge_index.upper()
            state[partner_index] = edge_index.upper()
        elif partner_value == 'D':
            state[square_index] = edge_index
            state[partner_index] = edge_index
        elif square_value == 'L':
            state[square_index] = edge_index.upper()
            state[partner_index] = edge_index.upper()
        elif partner_value == 'L':
            state[square_index] = edge_index
            state[partner_index] = edge_index
        elif square_value == 'R':
            state[square_index] = edge_index.upper()
            state[partner_index] = edge_index.upper()
        elif partner_value == 'R':
            state[square_index] = edge_index
            state[partner_index] = edge_index
        elif square_value == 'x' or partner_value == 'x':
            state[square_index] = 'x'
            state[partner_index] = 'x'
        else:
            raise Exception("We should not be here, state[%d] %s, partner state [%d] %s" % (square_index, state[square_index], partner_index, state[partner_index]))

    # Where is the midge for each high/low wing?
    for (edge_index, square_index, partner_index) in edges_recolor_tuples_555:
        square_value = state[square_index]
        partner_value = state[partner_index]

        if square_value == 'x' or partner_value == 'x':
            pass
        else:
            high_low = tsai_phase2_orient_edges_555[(square_index, partner_index, square_value, partner_value)]
            wing_str = ''.join(sorted([square_value, partner_value]))

            # If this is a high wing use the uppercase of the midge edge_index
            if high_low == 'U':
                state[square_index] = midges_map[wing_str].upper()
                state[partner_index] = midges_map[wing_str].upper()

            # If this is a low wing use the lowercase of the midge edge_index
            elif high_low == 'D':
                state[square_index] = midges_map[wing_str]
                state[partner_index] = midges_map[wing_str]

            else:
                raise Exception("(%s, %s, %s, %) high_low is %s" % (square_index, partner_index, square_value, partner_value, high_low))

    return ''.join(state)


def edges_recolor_555(state):
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


def edges_pattern_555(state):
    state = list(state)
    edges_recolor_555(state)
    state = ''.join(state)

    edges = ''.join((
        state[2], state[3], state[4],
        state[6], state[11], state[16],
        state[10], state[15], state[20],
        state[22], state[23], state[24],
        state[31], state[36], state[41],
        state[35], state[40], state[45],
        state[81], state[86], state[91],
        state[85], state[90], state[95],
        state[127], state[128], state[129],
        state[131], state[136], state[141],
        state[135], state[140], state[145],
        state[147], state[148], state[149]
    ))

    return edges


def crunch_workq(size, inputfile, linewidth, start, end, outputfilebase, use_edges_pattern, symmetries):
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

        cube_444 = RubiksCube444(solved_444, 'URFDLB')

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

                if symmetries:
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
                            state_for_edges = edges_recolor_555(state[:])
                            edges_pattern = ''.join([state_for_edges[square_index] for square_index in wings_555])
                            centers = ''.join([state[x] for x in centers_555])
                        else:
                            raise Exception("Implement this")

                        #log.info("move %s, symmetry %s, edges_pattern %s\n\n\n\n" % (moves_to_scramble[-1], ' '.join(seq), edges_pattern))
                        centers = centers.replace('.', '')
                        results.append((centers, edges_pattern, ''.join(state)))

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
                        state_for_edges = edges_recolor_555(cube_state[:])
                        edges_pattern = ''.join([state_for_edges[square_index] for square_index in wings_555])
                        centers = ''.join([cube_state[x] for x in centers_555])
                    else:
                        raise Exception("Implement this")

                    to_write.append("%s%s:%s:%s" % (centers, edges_pattern, cube_state_string, ' '.join(moves_to_scramble)))
                    to_write_count += 1

            else:
                if symmetries:
                    results = []
                    cube_state_original = cube_state[:]

                    for seq in symmetries:
                        cube_state = cube_state_original[:]

                        for step in seq:
                            cube_state = rotate_xxx(cube_state[:], step)

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
    args = parser.parse_args()

    crunch_workq(args.size, args.inputfile, args.linewidth, args.start, args.end, args.outputfile, args.use_edges_pattern, args.symmetries)

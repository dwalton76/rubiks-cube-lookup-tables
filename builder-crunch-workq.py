#!/usr/bin/env python3

from buildercore import supported_sizes, WRITE_BATCH_SIZE, reverse_steps
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_222, moves_222, rotate_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333, moves_333, rotate_333
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666, moves_666, rotate_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777, moves_777, rotate_777
import argparse
import logging

log = logging.getLogger(__name__)


wings_444 = (
    ('0', 2, 67),  # upper
    ('1', 3, 66),
    ('2', 5, 18),
    ('3', 8, 51),
    ('4', 9, 19),
    ('5', 12, 50),
    ('6', 14, 34),
    ('7', 15, 35),

    ('8', 21, 72), # left
    ('9', 24, 37),
    ('a', 25, 76),
    ('b', 28, 41),

    ('c', 53, 40), # right
    ('d', 56, 69),
    ('e', 57, 44),
    ('f', 60, 73),

    ('g', 82, 46), # down
    ('h', 83, 47),
    ('i', 85, 31),
    ('j', 88, 62),
    ('k', 89, 30),
    ('l', 92, 63),
    ('m', 94, 79),
    ('n', 95, 78))


def edges_recolor_444(state):
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

    for (edge_index, square_index, partner_index) in wings_444:
        square_value = state[square_index]
        partner_value = state[partner_index]
        wing_str = ''.join(sorted([square_value, partner_value]))

        if 'x' not in wing_str:
            edge_map[wing_str].append(edge_index)

    # Where is the other wing_str like us?
    for (edge_index, square_index, partner_index) in wings_444:
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


def edges_pattern_444(state):
    state = list(state)
    edges_recolor_444(state)
    state = ''.join(state)

    edges = ''.join((
        state[2], state[3],
        state[5], state[9],
        state[8], state[12],
        state[14], state[15],
        state[21], state[25],
        state[24], state[28],
        state[53], state[57],
        state[56], state[60],
        state[82], state[83],
        state[85], state[89],
        state[88], state[92],
        state[94], state[95]
    ))

    return edges


def crunch_workq(size, inputfile, linewidth, start, end, outputfilebase):
    assert isinstance(size, str)
    assert size in supported_sizes
    assert isinstance(inputfile, str)
    assert isinstance(outputfilebase, str)
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert start >= 0
    assert end > start

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

    with open(inputfile, 'r') as fh_input:

        # We add 1 here to account for the newline character
        fh_input.seek(start * (linewidth+1))

        for linenumber in range(start, end+1):
            line = next(fh_input)
            (_, cube_state, moves_to_scramble) = line.rstrip().split(':')
            moves_to_scramble = moves_to_scramble.split()

            cube_state_string = ''.join(rotate_xxx(list(cube_state), moves_to_scramble[-1]))
            edges_pattern = edges_pattern_444(cube_state_string)
            to_write.append("%s:%s:%s" % (edges_pattern, cube_state_string, ' '.join(moves_to_scramble)))
            to_write_count += 1

            if to_write_count >= WRITE_BATCH_SIZE or linenumber == end:
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
    args = parser.parse_args()

    crunch_workq(args.size, args.inputfile, args.linewidth, args.start, args.end, args.outputfile)

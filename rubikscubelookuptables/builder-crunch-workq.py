#!/usr/bin/env python3.6

# standard libraries
import argparse
import json
import logging
import subprocess
import sys
from pprint import pformat

# rubiks cube libraries
from rubikscubelookuptables.buildercore import WRITE_BATCH_SIZE, reverse_steps, supported_sizes
#from rubikscubelookuptables.buildercore import supported_sizes, reverse_steps
from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, moves_222, rotate_222, solved_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, moves_333, rotate_333, solved_333
from rubikscubennnsolver.RubiksCube444 import (
    RubiksCube444,
    centers_444,
    edges_recolor_pattern_444,
    moves_444,
    rotate_444,
    solved_444,
    wings_444,
)
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    centers_555,
    edges_recolor_pattern_555,
    midges_recolor_tuples_555,
    moves_555,
    rotate_555,
    solved_555,
    wings_555,
)
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, moves_666, rotate_666, solved_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, moves_777, rotate_777, solved_777

log = logging.getLogger(__name__)

l_edges = [4, 11, 42, 13, 15, 22, 17, 49]
r_edges = [6, 29, 24, 31, 33, 40, 35, 51]
l_corners = [1, 10, 39, 7, 12, 19, 16, 45, 52, 18, 25, 46]
r_corners = [9, 21, 28, 30, 3, 37, 27, 34, 48, 36, 43, 54]
l_edges_and_corners = l_edges + l_corners
r_edges_and_corners = r_edges + r_corners

f_edges = [8, 20, 15, 22, 24, 31, 26, 47]
b_edges = [2, 38, 33, 40, 42, 13, 44, 53]
f_corners = [7, 12, 19, 9, 21, 28, 18, 25, 46, 27, 34, 48]
b_corners = [37, 30, 3, 39, 1, 10, 36, 43, 54, 45, 16, 52]
f_edges_and_corners = f_edges + f_corners
b_edges_and_corners = b_edges + b_corners

u_edges = [2, 38, 4, 11, 6, 29, 8, 20]
d_edges = [26, 47, 17, 49, 35, 51, 53, 44]
u_corners = [1, 10, 39, 3, 30, 37, 7, 12, 19, 9, 21, 28]
d_corners = [18, 25, 46, 27, 34, 48, 52, 16, 45, 54, 36, 43]
u_edges_and_corners = u_edges + u_corners
d_edges_and_corners = d_edges + d_corners

l_midges_555 = [11, 28, 36, 115, 40, 61, 48, 136]
r_midges_555 = [15, 78, 65, 86, 90, 111, 98, 140]


def apply_333_phase_binary(cube_state, positions):

    for x in positions:
        if cube_state[x] == '1':
            cube_state[x] = '0';
        elif cube_state[x] == '0':
            cube_state[x] = '1';

    return cube_state


def apply_555_phase_binary(cube_state, positions):

    for x in positions:
        if cube_state[x] == 'U':
            cube_state[x] = 'D';
        elif cube_state[x] == 'D':
            cube_state[x] = 'U';

    return cube_state


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


def crunch_workq(size, inputfile, linewidth, start, end, outputfilebase, use_edges_pattern, legal_moves):
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
    states_written = set()
    outputfile_index = 0
    lines_since_last_merge = 0

    legal_moves_per_move = {}
    for move1 in legal_moves:
        legal_moves_per_move[move1] = []
        for move2 in legal_moves:
            if not steps_on_same_face_and_layer(move1, move2):
                legal_moves_per_move[move1].append(move2)

    legal_moves_per_move[None] = legal_moves
    legal_moves.insert(0, None)

    if "6x6x6-LR-inner-x-center-stage" in inputfile or "6x6x6-UD-inner-x-centers-stage" in inputfile:
        odd_even_layer = "3"
    elif "4x4x4-LRFB-centers-stage" in inputfile:
        odd_even_layer = "2"
    else:
        odd_even_layer = None

    with open(inputfile, 'r') as fh_input:

        # We add 1 here to account for the newline character
        fh_input.seek(start * (linewidth+1))
        is_333_phase1 = "3x3x3-phase1" in inputfile
        is_333_phase2 = "3x3x3-phase2" in inputfile
        is_333_phase3 = "3x3x3-phase3" in inputfile

        is_555_EO = (
            "5x5x5-LR-center-stage-EO-inner-orbit" in inputfile or
            "5x5x5-LR-center-stage-EO-both-orbits" in inputfile or
            "5x5x5-EO-inner-orbit" in inputfile or
            "5x5x5-EO-both-orbits" in inputfile
        )

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

            if moves_to_scramble:
                moves_to_scramble_original = moves_to_scramble.split()
            else:
                moves_to_scramble_original = []

            cube_state_original = cube_state

            if moves_to_scramble_original:
                prev_step = moves_to_scramble_original[-1]
            else:
                prev_step = None

            for next_move in legal_moves_per_move[prev_step]:
                moves_to_scramble = moves_to_scramble_original[:]

                if next_move is not None:
                    moves_to_scramble.append(next_move)

                cube_state = cube_state_original[:]

                if next_move:
                    if next_move == "x2":
                        cube_state = rotate_xxx(list(cube_state), "x")
                        cube_state = rotate_xxx(list(cube_state), "x")
                    elif next_move == "y2":
                        cube_state = rotate_xxx(list(cube_state), "y")
                        cube_state = rotate_xxx(list(cube_state), "y")
                    elif next_move == "z2":
                        cube_state = rotate_xxx(list(cube_state), "z")
                        cube_state = rotate_xxx(list(cube_state), "z")
                    else:
                        cube_state = rotate_xxx(list(cube_state), next_move)

                    if is_333_phase1:
                        if next_move == "L" or next_move == "L'":
                            cube_state = apply_333_phase_binary(cube_state, l_edges_and_corners)
                        elif next_move == "R" or next_move == "R'":
                            cube_state = apply_333_phase_binary(cube_state, r_edges_and_corners)

                    elif is_333_phase2:
                        if next_move == "F" or next_move == "F'":
                            cube_state = apply_333_phase_binary(cube_state, f_edges)
                        elif next_move == "B" or next_move == "B'":
                            cube_state = apply_333_phase_binary(cube_state, b_edges)

                    elif is_555_EO:
                        if next_move == "L" or next_move == "L'":
                            cube_state = apply_555_phase_binary(cube_state, l_midges_555)
                        elif next_move == "R" or next_move == "R'":
                            cube_state = apply_555_phase_binary(cube_state, r_midges_555)

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

                    if odd_even_layer is not None:
                        odd_even = get_odd_even(moves_to_scramble, odd_even_layer)
                        to_write.append("%s_%s:%s" % (cube_state_string, odd_even, ' '.join(moves_to_scramble)))
                        to_write_count += 1

                    else:
                        if cube_state_string not in states_written:
                            if next_move is None:
                                to_write.append("%s:%s" % (cube_state_string, ' '.join(moves_to_scramble[0:-1])))
                            else:
                                to_write.append("%s:%s" % (cube_state_string, ' '.join(moves_to_scramble)))
                            states_written.add(cube_state_string)
                            to_write_count += 1

            if to_write_count >= WRITE_BATCH_SIZE:
                to_write.sort()
                outputfile = outputfilebase + ".%05d" % outputfile_index
                outputfile_index += 1
                lines_since_last_merge += to_write_count

                with open(outputfile, 'w') as fh_output:
                    fh_output.write("\n".join(to_write) + "\n")

                to_write = []
                to_write_count = 0
                states_written = set()

                # Every 100 million lines sort what we've writen and run keep-best-solution against
                # it.  We do this to keep the amount of disk spaced used reasonable when building
                # huge tables.
                if lines_since_last_merge >= 100000000:
                    #log.info("sort --merge all of the files created so far")
                    subprocess.check_output("LC_ALL=C nice sort --merge --temporary-directory=./tmp/ --output %s.all %s.*" %
                        (outputfilebase, outputfilebase), shell=True)
                    #log.info("rm %s.0*" % outputfilebase)
                    subprocess.check_output("rm %s.0*" % outputfilebase, shell=True)
                    subprocess.check_output("nice ./utils/keep-best-solution.py %s.all" % outputfilebase, shell=True)
                    lines_since_last_merge = 0

        if to_write:
            to_write.sort()
            outputfile = outputfilebase + ".%05d" % outputfile_index
            outputfile_index += 1

            with open(outputfile, 'w') as fh_output:
                fh_output.write("\n".join(to_write) + "\n")

            to_write = []
            to_write_count = 0
            states_written = set()


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
    parser.add_argument('legalmoves', type=str, help='List of legal moves')
    parser.add_argument('--use-edges-pattern', default=False, action='store_true', help='use edges patterns')
    args = parser.parse_args()

    crunch_workq(args.size, args.inputfile, args.linewidth,
        args.start, args.end,
        args.outputfile,
        args.use_edges_pattern,
        args.legalmoves.split(),
    )

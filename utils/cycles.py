#!/usr/bin/env python3

from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube333 import moves_333
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555
from pprint import pprint, pformat
import json
import itertools
import sys
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)20s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))


'''
and the sequences are always going to be something like:
phase2 - 1 "w" move, could be quarter or half turn
phase3 - 2 or more outer layer moves...I say 2 because seems like you need at
    least 2 to get the midges you just paired out of the way.  This
    would also be doing some setup to pair 3 more midges on the final "w" move
phase4 - 1 "w" move to bring the centers back to solved
'''

wide_moves = []
for x in moves_555:
    if "w" in x:
        wide_moves.append(x)

closing_wide_moves = {
    "Bw": ["Bw'", "Fw"],
    "Bw'": ["Bw", "Fw'"],
    "Bw2": ["Bw2", "Fw2"],
    "Dw": ["Dw'", "Uw"],
    "Dw'": ["Dw", "Uw'"],
    "Dw2": ["Dw2", "Uw2"],
    "Fw": ["Fw'", "Bw"],
    "Fw'": ["Fw", "Bw'"],
    "Fw2": ["Fw2", "Bw2"],
    "Lw": ["Lw'", "Rw"],
    "Lw'": ["Lw", "Rw'"],
    "Lw2": ["Lw2", "Rw2"],
    "Rw": ["Rw'", "Lw"],
    "Rw'": ["Rw", "Lw'"],
    "Rw2": ["Rw2", "Lw2"],
    "Uw": ["Uw'", "Dw"],
    "Uw'": ["Uw", "Dw'"],
    "Uw2": ["Uw2", "Dw2"]
}


def combo_steps_cancel(combo):

    if len(combo) <= 1:
        return False

    prev_step = combo[0]

    for step in combo[1:]:
        if steps_cancel_out(prev_step, step):
            return True

        if steps_on_same_face_and_layer(prev_step, step):
            return True

        prev_step = step
    return False


def get_outer_layer_sequences(depth):
    results = []
    for combo in itertools.product(moves_333, repeat=depth):
        if not combo_steps_cancel(combo):
            results.append(combo)
    return results


def save_outer_layer_sequences(depth):
    log.info("depth {}: find cycles".format(depth))
    cycles = get_outer_layer_sequences(depth)
    BATCH_SIZE = 10000000

    with open("cycles-outer-layer-%d-deep.json" % depth, "w") as fh:
        log.info("depth {}: found {:,} cycles".format(depth, len(cycles)))
        json.dump(cycles, fh)
        log.info("depth {}: wrote cycles\n\n".format(depth))


UD_other_axis = ("L", "R", "F", "B")
LR_other_axis = ("U", "D", "F", "B")
FB_other_axis = ("U", "D", "L", "R")

def combo_move_on_other_axis(wide_move, combo):

    if wide_move == "U" or wide_move == "D":
        for step in combo:
            first_letter = step[0]

            if first_letter in UD_other_axis:
                return True

    elif wide_move == "L" or wide_move == "R":
        for step in combo:
            first_letter = step[0]

            if first_letter in LR_other_axis:
                return True

    elif wide_move == "F" or wide_move == "B":
        for step in combo:
            first_letter = step[0]

            if first_letter in FB_other_axis:
                return True

    return False


def combo_even_turns_on_plane(wide_move, combo):
    U_count = 0
    L_count = 0
    F_count = 0
    R_count = 0
    B_count = 0
    D_count = 0

    for step in combo:
        if step == "U" or step == "U'":
            U_count += 1
        elif step == "L" or step == "L'":
            L_count += 1
        elif step == "F" or step == "F'":
            F_count += 1
        elif step == "R" or step == "R'":
            R_count += 1
        elif step == "B" or step == "B'":
            B_count += 1
        elif step == "D" or step == "D'":
            D_count += 1

    if wide_move == "U" or wide_move == "D":
        if L_count % 2 or F_count % 2 or R_count % 2 or B_count % 2:
            return False

    elif wide_move == "L" or wide_move == "R":
        if U_count % 2 or F_count % 2 or D_count % 2 or B_count % 2:
            return False

    elif wide_move == "F" or wide_move == "B":
        if L_count % 2 or U_count % 2 or R_count % 2 or D_count % 2:
            return False

    return True


def combo_centers_will_solve(opening_wide_move, combo, closing_wide_move):
    U_count = 0
    L_count = 0
    F_count = 0
    R_count = 0
    B_count = 0
    D_count = 0

    for step in combo:
        if step == "U":
            U_count += 1
        elif step == "U'":
            U_count -= 1
        elif step == "U2":
            U_count += 2

        elif step == "L":
            L_count += 1
        elif step == "L'":
            L_count -= 1
        elif step == "L2":
            L_count += 2

        elif step == "F":
            F_count += 1
        elif step == "F'":
            F_count -= 1
        elif step == "F2":
            F_count += 2

        elif step == "R":
            R_count += 1
        elif step == "R'":
            R_count -= 1
        elif step == "R2":
            R_count += 2

        elif step == "B":
            B_count += 1
        elif step == "B'":
            B_count -= 1
        elif step == "B2":
            B_count += 2

        elif step == "D":
            D_count += 1
        elif step == "D'":
            D_count -= 1
        elif step == "D2":
            D_count += 2

    U_count = U_count % 4
    L_count = L_count % 4
    F_count = F_count % 4
    R_count = R_count % 4
    B_count = B_count % 4
    D_count = D_count % 4

    if opening_wide_move == "U":

        if closing_wide_move == "U":
            if L_count == 0 and L_count == F_count and F_count == R_count and R_count == B_count:
                return True

        elif closing_wide_move == "D":
            if L_count == 2 and L_count == F_count and F_count == R_count and R_count == B_count:
                return True

        else:
            raise Exception("open %s, close %s" % (opening_wide_move, closing_wide_move))

    elif opening_wide_move == "D":

        if closing_wide_move == "D":
            if L_count == 0 and L_count == F_count and F_count == R_count and R_count == B_count:
                return True

        elif closing_wide_move == "U":

            if L_count == 2  and L_count == F_count and F_count == R_count and R_count == B_count:
                return True
        else:
            raise Exception("open %s, close %s" % (opening_wide_move, closing_wide_move))

    elif opening_wide_move == "L":

        if closing_wide_move == "L":
            if U_count == 0 and U_count == F_count and F_count == D_count and D_count == B_count:
                return True

        elif closing_wide_move == "R":

            if U_count == 2 and U_count == F_count and F_count == D_count and D_count == B_count:
                return True
        else:
            raise Exception("open %s, close %s" % (opening_wide_move, closing_wide_move))

    elif opening_wide_move == "R":

        if closing_wide_move == "R":
            if U_count == 0 and U_count == F_count and F_count == D_count and D_count == B_count:
                return True

        elif closing_wide_move == "L":

            if U_count == 2 and U_count == F_count and F_count == D_count and D_count == B_count:
                return True
        else:
            raise Exception("open %s, close %s" % (opening_wide_move, closing_wide_move))

    elif opening_wide_move == "F":

        if closing_wide_move == "F":
            if L_count == 0 and L_count == U_count and U_count == R_count and R_count == D_count:
                return True

        elif closing_wide_move == "B":

            if L_count == 2 and L_count == U_count and U_count == R_count and R_count == D_count:
                return True

        else:
            raise Exception("open %s, close %s" % (opening_wide_move, closing_wide_move))

    elif opening_wide_move == "B":

        if closing_wide_move == "B":
            if L_count == 0 and L_count == U_count and U_count == R_count and R_count == D_count:
                return True

        elif closing_wide_move == "F":
            if L_count == 2 and L_count == U_count and U_count == R_count and R_count == D_count:
                return True

        else:
            raise Exception("open %s, close %s" % (opening_wide_move, closing_wide_move))


    return False

def get_cycles(phase3_count):
    results = []

    phase3_combos = []
    log.info("(1, {}, 1): building phase3_combos: begin".format(phase3_count))
    for phase3_combo in itertools.product(moves_333, repeat=phase3_count):
        if combo_steps_cancel(phase3_combo):
            continue
        phase3_combos.append(phase3_combo)
    log.info("(1, {}, 1): building phase3_combos: end, found {:,}".format(phase3_count, len(phase3_combos)))

    for opening_wide_move in wide_moves:
        log.info("(1, {}, 1): opening_wide_move {}, found {:,} so far".format(phase3_count, opening_wide_move, len(results)))

        for phase3_combo in phase3_combos:

            if not combo_move_on_other_axis(opening_wide_move[0], phase3_combo):
                continue

            if not combo_even_turns_on_plane(opening_wide_move[0], phase3_combo):
                continue

            for closing_wide_move in closing_wide_moves[opening_wide_move]:

                if not combo_centers_will_solve(opening_wide_move[0], phase3_combo, closing_wide_move[0]):
                    continue

                moves_for_cycle = []
                moves_for_cycle.append(opening_wide_move)
                moves_for_cycle.extend(phase3_combo)
                moves_for_cycle.append(closing_wide_move)
                results.append(" ".join(moves_for_cycle))

    return results


def write_cycles_for_depth(depth):
    log.info("DEPTH %d" % depth)
    log.info("wide moves: %s" % " ".join(wide_moves))
    BATCH_SIZE = 10000000
    phase3_count = depth - 2 # 1 for opening wide move, 1 for closing wide move

    with open("cycles-%d-deep.txt" % depth, "w") as fh:
        cube = RubiksCube555(solved_555, 'URFDLB')

        log.info("(1, {}, 1): find cycles".format(phase3_count))
        cycles = get_cycles(phase3_count)
        log.info("(1, {}, 1): found {:,} cycles".format(phase3_count, len(cycles)))

        '''
        keepers = []

        for cycle in cycles:
            cube.re_init()

            for step in cycle.split():
                cube.state = rotate_555(cube.state[:], step)

            if cube.centers_solved():
                keepers.append(cycle)
            #    log.info("(1, {}, 1): centers solved {}".format(phase3_count, cycle))
            else:
                log.info("(1, {}, 1): centers broken {}".format(phase3_count, cycle))

        log.info("(1, {}, 1): found {:,} keepers".format(phase3_count, len(keepers)))

        while keepers:
            if len(keepers) > BATCH_SIZE:
                fh.write("\n".join(keepers[0:BATCH_SIZE]) + "\n")
                keepers = keepers[BATCH_SIZE:]
            else:
                fh.write("\n".join(keepers) + "\n")
                keepers = []
        log.info("(1, {}, 1): wrote keepers\n\n".format(phase3_count))
        '''
        fh.write("\n".join(cycles) + "\n")


def write_foobar():

    BATCH_SIZE = 10000000
    cube = RubiksCube555(solved_555, 'URFDLB')
    depth = 5
    keepers = []

    with open("foobar.txt", "w") as fh_write:

        for depth in (5, 6, 7, 8):
            with open("cycles-%d-deep.txt" % depth, "r") as fh:

                for (line_number, steps) in enumerate(fh):
                    steps = steps.rstrip().split()

                    for opening_wide_move in wide_moves:

                        if steps_on_same_face_and_layer(opening_wide_move, steps[0]):
                            continue

                        for closing_wide_move in closing_wide_moves[opening_wide_move]:
                            cube.re_init()
                            cube.state = rotate_555(cube.state[:], opening_wide_move)

                            for step in steps:
                                cube.state = rotate_555(cube.state[:], step)

                            cube.state = rotate_555(cube.state[:], closing_wide_move)

                            if cube.centers_solved():
                                cycle = []
                                cycle.append(opening_wide_move)
                                cycle.extend(steps)
                                cycle.append(closing_wide_move)

                                keepers.append(" ".join(cycle))

                    if line_number and line_number % 10000 == 0:
                        log.info("line {}, keepers {}".format(line_number, len(keepers)))

            log.info("depth {} found {:,} keepers".format(depth, len(keepers)))

            while keepers:
                if len(keepers) > BATCH_SIZE:
                    fh_write.write("\n".join(keepers[0:BATCH_SIZE]) + "\n")
                    keepers = keepers[BATCH_SIZE:]
                else:
                    fh_write.write("\n".join(keepers) + "\n")
                    keepers = []
            fh_write.flush()
        log.info("wrote keepers\n\n")


if __name__ == "__main__":

    # Ran these once to build the cycles*.json files
    #save_outer_layer_sequences(1)
    #save_outer_layer_sequences(2)
    #save_outer_layer_sequences(3)
    #save_outer_layer_sequences(4)
    #save_outer_layer_sequences(5)
    #save_outer_layer_sequences(6)

    # Took 0.9s
    # INFO: (0, 1, 3, 1, False): found 1,296 cycles
    #write_cycles_for_depth(5) # (1, 3, 1)

    # Took 4s
    # INFO: (0, 1, 4, 1, False): found 21,816 cycles
    #write_cycles_for_depth(6) # (1, 4, 1)

    # Took 38s
    # INFO: (0, 1, 5, 1, False): found 259,200 cycles
    #write_cycles_for_depth(7) # (1, 5, 1)

    # Took 8hr 45m but this was before I added combo_even_turns_on_plane and combo_centers_will_solve which make a HUGE difference (about 20x)
    # INFO: (0, 1, 6, 1, False): found 492,022,512 cycles
    # INFO: (0, 1, 6, 1, False): found 3,163,968 keepers
    #write_cycles_for_depth(8) # (1, 6, 1)

    write_foobar()

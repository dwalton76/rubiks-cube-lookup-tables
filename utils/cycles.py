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


#log.info("wide moves: %s" % pformat(wide_moves))
def count_permutations(MAX_MOVES):
    PHASE2_MOVES = 1
    PHASE3_MIN_MOVES = 3
    PHASE3_MAX_MOVES = 6
    PHASE4_MOVES = 1
    PHASE234_MIN_MOVES = PHASE2_MOVES + PHASE3_MIN_MOVES + PHASE4_MOVES
    count_permutations = []

    # phase 3 is 2 or more outer layer moves
    phase3_max_moves = min(PHASE3_MAX_MOVES, MAX_MOVES - PHASE4_MOVES - PHASE2_MOVES)

    '''
    if (PHASE2_MOVES, phase3_max_moves, PHASE4_MOVES) in count_permutations:
        continue

    if (phase3_max_moves, PHASE2_MOVES, PHASE4_MOVES, True) in count_permutations:
        log.info("SKIP: (%d, %d, %d, %d, %s)" % (PHASE2_MOVES, phase3_max_moves, PHASE4_MOVES))
        continue
    '''

    count_permutations.append((PHASE2_MOVES, phase3_max_moves, PHASE4_MOVES))
    log.info("(%d, %d, %d)" % (PHASE2_MOVES, phase3_max_moves, PHASE4_MOVES))

    return count_permutations


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


def combo_move_on_other_axis(wide_move, combo):

    if wide_move == "U" or wide_move == "D":
        for step in combo:
            first_letter = step[0]

            if first_letter in ("L", "R", "F", "B"):
                return True

    elif wide_move == "L" or wide_move == "R":
        for step in combo:
            first_letter = step[0]

            if first_letter in ("U", "D", "F", "B"):
                return True

    elif wide_move == "F" or wide_move == "B":
        for step in combo:
            first_letter = step[0]

            if first_letter in ("U", "D", "L", "R"):
                return True

    return False


def get_cycles(count_permutation):
    results = []
    (phase2_count, phase3_count, phase4_count) = count_permutation

    phase3_combos = []
    log.info("{}: building phase3_combos: begin".format(count_permutation))
    for phase3_combo in itertools.product(moves_333, repeat=phase3_count):
        if combo_steps_cancel(phase3_combo):
            continue
        phase3_combos.append(phase3_combo)
    log.info("{}: building phase3_combos: end, found {:,}".format(count_permutation, len(phase3_combos)))

    for opening_wide_move in wide_moves:
        log.info("{}: opening_wide_move {}, found {:,} so far".format(count_permutation, opening_wide_move, len(results)))

        for phase3_combo in phase3_combos:

            if not combo_move_on_other_axis(opening_wide_move[0], phase3_combo):
                continue

            for closing_wide_move in closing_wide_moves[opening_wide_move]:
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
    
    with open("cycles-%d-deep.txt" % depth, "w") as fh:
        cube = RubiksCube555(solved_555, 'URFDLB')

        for permutation in count_permutations(depth):
            log.info("{}: find cycles".format(permutation))
            cycles = get_cycles(permutation)
            log.info("{}: found {:,} cycles".format(permutation, len(cycles)))
            keepers = []

            for cycle in cycles:
                cube.re_init()

                for step in cycle.split():
                    cube.state = rotate_555(cube.state[:], step)

                if cube.centers_solved():
                    keepers.append(cycle)
                #    log.info("{}: centers solved {}".format(permutation, cycle))
                #else:
                #    log.info("{}: centers broken {}".format(permutation, cycle))

            log.info("{}: found {:,} keepers".format(permutation, len(keepers)))

            while keepers:
                if len(keepers) > BATCH_SIZE:
                    fh.write("\n".join(keepers[0:BATCH_SIZE]) + "\n")
                    keepers = keepers[BATCH_SIZE:]
                else:
                    fh.write("\n".join(keepers) + "\n")
                    keepers = []
            log.info("{}: wrote keepers\n\n".format(permutation))


# Ran these once to build the cycles*.json files
#save_outer_layer_sequences(1)
#save_outer_layer_sequences(2)
#save_outer_layer_sequences(3)
#save_outer_layer_sequences(4)
#save_outer_layer_sequences(5)
#save_outer_layer_sequences(6)

# Took 6s
# INFO: (0, 1, 3, 1, False): found 143,856 cycles
# INFO: (0, 1, 3, 1, False): found 1,296 keepers
write_cycles_for_depth(5) # (1, 3, 1)

# Took 1m 43s
# INFO: (0, 1, 4, 1, False): found found 2,181,168 cycles
# INFO: (0, 1, 4, 1, False): found 21,816 keepers
#write_cycles_for_depth(6) # (1, 4, 1)

# Took 29m 38s
# INFO: (0, 1, 5, 1, False): found 32,787,504 cycles
# INFO: (0, 1, 5, 1, False): found 259,200 keepers
#write_cycles_for_depth(7) # (1, 5, 1)

# Took 8hr 45m
# INFO: (0, 1, 6, 1, False): found 492,022,512 cycles
# INFO: (0, 1, 6, 1, False): found 3,163,968 keepers
#write_cycles_for_depth(8) # (1, 6, 1)

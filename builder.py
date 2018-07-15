#!/usr/bin/env python3

from copy import copy
from pprint import pprint, pformat
from threading import Thread, Event
import argparse
import logging
import json
import re
import os
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)

moves_2x2x2 = ("U", "U'", "U2",
               "L", "L'", "L2",
               "F" , "F'", "F2",
               "R" , "R'", "R2",
               "B" , "B'", "B2",
               "D" , "D'", "D2")
moves_3x3x3 = moves_2x2x2


moves_4x4x4 = ("U", "U'", "U2", "Uw", "Uw'", "Uw2",
               "L", "L'", "L2", "Lw", "Lw'", "Lw2",
               "F" , "F'", "F2", "Fw", "Fw'", "Fw2",
               "R" , "R'", "R2", "Rw", "Rw'", "Rw2",
               "B" , "B'", "B2", "Bw", "Bw'", "Bw2",
               "D" , "D'", "D2", "Dw", "Dw'", "Dw2")
moves_5x5x5 = moves_4x4x4


moves_6x6x6 = ("U", "U'", "U2", "Uw", "Uw'", "Uw2", "3Uw", "3Uw'", "3Uw2",
               "L", "L'", "L2", "Lw", "Lw'", "Lw2", "3Lw", "3Lw'", "3Lw2",
               "F", "F'", "F2", "Fw", "Fw'", "Fw2", "3Fw", "3Fw'", "3Fw2",
               "R", "R'", "R2", "Rw", "Rw'", "Rw2", "3Rw", "3Rw'", "3Rw2",
               "B", "B'", "B2", "Bw", "Bw'", "Bw2", "3Bw", "3Bw'", "3Bw2",
               "D", "D'", "D2", "Dw", "Dw'", "Dw2", "3Dw", "3Dw'", "3Dw2")
moves_7x7x7 = moves_6x6x6


def touch(filename):
    with open(filename, 'w') as fh:
        pass


def advance_filehandle(fh):
    try:
        line = next(fh)
        line = line.strip()
    except StopIteration:
        line = None

    return line


def advance_filehandle_to_state_change(state, fh):
    prev_state = state

    while True:
        line = advance_filehandle(fh)

        if line is None:
            break
        else:
            (state, _) = line.strip().split(':')

            if state != prev_state:
                break

            prev_state = state

    return line


class BackgroundProcess(Thread):

    def __init__(self, cmd, desc):
        Thread.__init__(self)
        self.cmd = cmd
        self.desc = desc
        self.result = None
        self.ok = False

    def __str__(self):
        return self.desc

    def run(self):
        log.debug("Running %s" % ' '.join(self.cmd))
        try:
            self.result = subprocess.check_output(self.cmd)

            if self.result is not None and self.result.isdigit():
                self.result = int(self.result)
            self.ok = True
        except subprocess.CalledProcessError:
            self.ok = False


def get_start_end_lines(CORES, core, file_linecount):
    if file_linecount < CORES:
        if core == 1:
            return (0, file_linecount)
        else:
            return (None, None)

    lines_per_core = int(file_linecount/CORES)
    start_line = (core-1) * lines_per_core

    if core == CORES:
        end_line = file_linecount
    else:
        end_line = start_line + lines_per_core

    return (start_line, end_line)


lookup_tables = {

    # ===========================
    # 4x4x4 centers
    # ===========================

    # Centers are staged, now solve them
    '4x4x4-ULFRBD-centers-solve' : {
        'illegal'  : ("Rw", "Rw'",
                      "Lw", "Lw'",
                      "Fw", "Fw'",
                      "Bw", "Bw'",
                      "Uw", "Uw'",
                      "Dw", "Dw'"),
        'size'     : '4x4x4',
        'filename' : 'lookup-table-4x4x4-step30-ULFRBD-centers-solve.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers'
    },

    # Only used when building 444-edges table
    '4x4x4-ULFRBD-centers-solve-with-edges-oriented' : {
        'illegal' : ("Fw", "Fw'",
                     "Uw", "Uw'",
                     "Rw", "Rw'",
                     "Lw", "Lw'", "Lw2",
                     "Bw", "Bw'", "Bw2",
                     "Dw", "Dw'", "Dw2",
                     "R", "R'",
                     "L", "L'"),
        'size'     : '4x4x4',
        'filename' : 'lookup-table-4x4x4-step30-ULFRBD-centers-solve-with-edges-oriented.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers'
    },

    # ===========
    # 4x4x4 edges
    # ===========
    '4x4x4-edges' : {
        'illegal' : ("Fw", "Fw'",
                     "Uw", "Uw'",
                     "Rw", "Rw'",
                     "Lw", "Lw'", "Lw2",
                     "Bw", "Bw'", "Bw2",
                     "Dw", "Dw'", "Dw2",
                     "R", "R'",
                     "L", "L'"),
        'size'     : '4x4x4',
        'filename' : 'lookup-table-4x4x4-step110-edges.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers-and-edges-pattern'
    },

    # ===================
    # 5x5x5 centers stage
    # ===================
    '5x5x5-UD-centers-stage' : {
        'illegal'  : (),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step10-UD-centers-stage.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'centers'
    },

    '5x5x5-UD-centers-stage-T-centers' : {
        'illegal'  : (),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step11-UD-centers-stage-t-center-only.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 't-centers'
    },

    '5x5x5-UD-centers-stage-X-centers' : {
        'illegal'  : (),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step12-UD-centers-stage-x-center-only.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'x-centers'
    },

    '5x5x5-LR-centers-stage' : {
        'illegal'  : ("Rw", "Rw'",
                      "Lw", "Lw'",
                      "Fw", "Fw'",
                      "Bw", "Bw'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step20-LR-centers-stage.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'LFRB-centers'
    },

    # ===================
    # 5x5x5 centers solve
    # ===================
    '5x5x5-ULFRBD-centers-solve' : {
        'illegal'  : ("Rw", "Rw'", "Lw", "Lw'",
                      "Fw", "Fw'", "Bw", "Bw'",
                      "Uw", "Uw'", "Dw", "Dw'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step30-ULFRBD-centers-solve.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers'
    },

    '5x5x5-UL-centers-solve' : {
        'illegal'  : ("Rw", "Rw'", "Lw", "Lw'",
                      "Fw", "Fw'", "Bw", "Bw'",
                      "Uw", "Uw'", "Dw", "Dw'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step31-UL-centers-solve.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'centers'
    },

    '5x5x5-ULFRBD-t-centers-solve' : {
        'illegal'  : ("Rw", "Rw'", "Lw", "Lw'",
                      "Fw", "Fw'", "Bw", "Bw'",
                      "Uw", "Uw'", "Dw", "Dw'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step32-ULFRBD-t-centers-solve.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers'
    },

    '5x5x5-UF-centers-solve' : {
        'illegal'  : ("Rw", "Rw'", "Lw", "Lw'",
                      "Fw", "Fw'", "Bw", "Bw'",
                      "Uw", "Uw'", "Dw", "Dw'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step33-UF-centers-solve.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'centers'
    },

    # stage the first L4E while solving centers
    '5x5x5-ULFRBD-centers-solve-stage-first-four-edges-edges-only' : {
        'illegal'  : ("Rw", "Rw'", "Lw", "Lw'",
                      "Fw", "Fw'", "Bw", "Bw'",
                      "Uw", "Uw'", "Dw", "Dw'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step34-first-four-edges-stage.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'edges'
    },

    # This is used to build the 5x5x5-pair-last-four-edges table
    '5x5x5-ULFRBD-centers-solve-unstaged' : {
        'illegal'  : (),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step30-ULFRBD-centers-solve-unstaged.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers'
    },

    '5x5x5-LR-t-centers-solve' : {
        'illegal'  : ("Rw", "Rw'", "Lw", "Lw'",
                      "Fw", "Fw'", "Bw", "Bw'",
                      "Uw", "Uw'", "Dw", "Dw'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step40-LR-t-centers-solve.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'LR-t-centers'
    },

    # ===========
    # 5x5x5 edges
    # ===========
    '5x5x5-stage-first-four-edges' : {
        'illegal'  : (),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step100-stage-first-four-edges.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers-and-edges-separate'
    },

    '5x5x5-stage-second-four-edges' : {
        'illegal'  : ("Lw", "Lw'", "Rw", "Rw'",
                      "Fw", "Fw'", "Bw", "Bw'",
                      "Uw", "Uw'", "Dw", "Dw'",
                      "Uw2", "Dw2",
                      "L", "L'",
                      "R", "R'",
                      "F", "F'",
                      "B", "B'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step101-stage-second-four-edges.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers-and-edges-separate'
    },

    # Assumes the first 8 edges are paired and on sides U and D
    '5x5x5-pair-last-four-edges' : {
        'illegal'  : ("Rw", "Rw'", "Rw2",
                      "Lw", "Lw'", "Lw2",
                      "Fw", "Fw'", "Fw2",
                      "Bw", "Bw'", "Bw2",
                      "L", "L'",
                      "F", "F'",
                      "R", "R'",
                      "B", "B'"),
        'size'     : '5x5x5',
        'filename' : 'lookup-table-5x5x5-step102-pair-last-four-edges.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'centers-and-last-four-edges-pattern'
    },

    # ======================
    # 6x6x6 LR oblique edges
    # ======================
    # There is no IDA for this one so we can keep 3Lw, 3Lw', 3Lw2, 3Dw, 3Dw', 3Dw2, 3Bw, 3Bw', 3Bw2
    '6x6x6-UD-solve-inner-x-center-and-oblique-edges' : {
        'illegal'  : ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'", "3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged centers
                      "Rw", "Rw'", "Lw", "Lw'", "Fw", "Fw'", "Bw", "Bw'", "Uw", "Uw'", "Dw", "Dw'"),            # do not mess up staged centers
        'size'     : '6x6x6',
        'filename' : 'lookup-table-6x6x6-step50-UD-solve-inner-x-center-and-oblique-edges.txt',
        'allsteps' : True,
        'hex'      : False,
        'keep'     : 'UD-centers'
    },

    # =====
    # 7x7x7
    # =====
    '7x7x7-UD-oblique-edge-pairing' : {
        'illegal'  : ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'"), # do not mess up UD 5x5x5 centers
        'size'     : '7x7x7',
        'filename' : 'lookup-table-7x7x7-step10-UD-oblique-edge-pairing.txt',
        'allsteps' : True, # Do NOT set this to False!!
        'hex'      : True,
        'keep'     : 'oblique-edges'
    },

    '7x7x7-UD-oblique-edge-pairing-middle-only' : {
        'illegal'  : ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'"), # do not mess up UD 5x5x5 centers
        'size'     : '7x7x7',
        'filename' : 'lookup-table-7x7x7-step11-UD-oblique-edge-pairing-middle-only.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'oblique-edges'
    },

    '7x7x7-UD-oblique-edge-pairing-left-only' : {
        'illegal'  : ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'"), # do not mess up UD 5x5x5 centers
        'size'     : '7x7x7',
        'filename' : 'lookup-table-7x7x7-step12-UD-oblique-edge-pairing-left-only.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'oblique-edges'
    },

    '7x7x7-UD-oblique-edge-pairing-right-only' : {
        'illegal'  : ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'"), # do not mess up UD 5x5x5 centers
        'size'     : '7x7x7',
        'filename' : 'lookup-table-7x7x7-step13-UD-oblique-edge-pairing-right-only.txt',
        'allsteps' : True,
        'hex'      : True,
        'keep'     : 'oblique-edges'
    },
}


def do_backup(workq_count, depth, max_depth, lookup_table_type):

    if not workq_count:
        return False

    if lookup_table_type == '5x5x5-ULFRBD-centers-solve' and depth == max_depth-1:
        return False

    if lookup_table_type == '5x5x5-UD-centers-stage' and depth == max_depth-1:
        return False

    if lookup_table_type == '6x6x6-UD-oblique-edge-pairing' and depth == max_depth-1:
        return False

    return True


def do_repopulate_workq(lookup_table_filename_diff_count, depth, max_depth, lookup_table_type):

    if lookup_table_filename_diff_count:

        if depth == max_depth-1:
            return False
        else:
            return True

    return False


def steps_have_slice(steps):
    for step in steps.split():
        if 'w' in step:
            return True

    return False


def remove_trailing_outside_moves(steps):
    steps = steps.split()
    while 'w' not in steps[-1]:
        steps = steps[0:-1]
    return ' '.join(steps)


centers_solved_states_444 = set()
centers_solved_states_444.add('UUUULLLLFFFFRRRRBBBBDDDD')
centers_solved_states_444.add('UUUUFFFFRRRRBBBBLLLLDDDD')
centers_solved_states_444.add('UUUURRRRBBBBLLLLFFFFDDDD')
centers_solved_states_444.add('UUUUBBBBLLLLFFFFRRRRDDDD')
centers_solved_states_444.add('DDDDLLLLBBBBRRRRFFFFUUUU')
centers_solved_states_444.add('DDDDBBBBRRRRFFFFLLLLUUUU')
centers_solved_states_444.add('DDDDRRRRFFFFLLLLBBBBUUUU')
centers_solved_states_444.add('DDDDFFFFLLLLBBBBRRRRUUUU')
centers_solved_states_444.add('LLLLUUUUBBBBDDDDFFFFRRRR')
centers_solved_states_444.add('LLLLBBBBDDDDFFFFUUUURRRR')
centers_solved_states_444.add('LLLLDDDDFFFFUUUUBBBBRRRR')
centers_solved_states_444.add('LLLLFFFFUUUUBBBBDDDDRRRR')
centers_solved_states_444.add('FFFFLLLLDDDDRRRRUUUUBBBB')
centers_solved_states_444.add('FFFFDDDDRRRRUUUULLLLBBBB')
centers_solved_states_444.add('FFFFRRRRUUUULLLLDDDDBBBB')
centers_solved_states_444.add('FFFFUUUULLLLDDDDRRRRBBBB')
centers_solved_states_444.add('RRRRDDDDBBBBUUUUFFFFLLLL')
centers_solved_states_444.add('RRRRBBBBUUUUFFFFDDDDLLLL')
centers_solved_states_444.add('RRRRUUUUFFFFDDDDBBBBLLLL')
centers_solved_states_444.add('RRRRFFFFDDDDBBBBUUUULLLL')
centers_solved_states_444.add('BBBBUUUURRRRDDDDLLLLFFFF')
centers_solved_states_444.add('BBBBRRRRDDDDLLLLUUUUFFFF')
centers_solved_states_444.add('BBBBDDDDLLLLUUUURRRRFFFF')
centers_solved_states_444.add('BBBBLLLLUUUURRRRDDDDFFFF')

# These are tables that we build where the centers must be preserved
type_edges_444 = (
    '4x4x4-edges',
)

type_edges_555 = (
    '5x5x5-stage-first-four-edges',
    '5x5x5-stage-second-four-edges',
    '5x5x5-pair-last-four-edges',
    '5x5x5-stage-all-edges',
)


def centers_solved_444(state):
    if state[0:24] in centers_solved_states_444:
        return True
    return False


def centers_solved_555(state):
    if state[0:54] == 'UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD':
        return True
    return False


def write_keepers_444(lookup_table_type, level_desc, lookup_table_filename, lookup_table_filename_final, do_move, mac):
    log.info("%s writing keepers to %s" % (level_desc, lookup_table_filename_final))
    keepers = {}

    # TODO this needs to not hold everything in memory
    with open(lookup_table_filename, 'r') as fh_curr:
        for line in fh_curr:
            (state, steps) = line.rstrip().split(':')

            if centers_solved_444(state) and steps_have_slice(steps):

                # The first 24 characters are the centers state
                edges = ''.join(state[24:])

                # We only need the edges to be paired, we do not need to move them to
                # their home location so remove any trailing outside moves.
                steps = remove_trailing_outside_moves(steps).split()

                if edges not in keepers:
                    keepers[edges] = steps
                elif len(steps) < len(keepers[edges]):
                    keepers[edges] = steps

    with open(lookup_table_filename_final, 'w') as fh_keepers:
        for (state, steps) in keepers.items():
            fh_keepers.write("%s:%s\n" % (state, ' '.join(steps)))

    log.warning("%s keeper_count %d" % (level_desc, len(keepers)))

    if mac:
        subprocess.check_output("LC_ALL=C nice sort --temporary-directory=./tmp/ --output=%s %s" %
            (lookup_table_filename_final, lookup_table_filename_final), shell=True)

    else:
        subprocess.check_output("LC_ALL=C nice sort --parallel=%d --temporary-directory=./tmp/ --output=%s %s" %
            (CORES, lookup_table_filename_final, lookup_table_filename_final), shell=True)

    if do_move:
        shutil.move(lookup_table_filename_final, lookup_table_filename)


def write_keepers_555(lookup_table_type, level_desc, lookup_table_filename, lookup_table_filename_final, do_move, mac):
    log.info("%s writing keepers to %s" % (level_desc, lookup_table_filename_final))
    keepers = {}

    # TODO this needs to not hold everything in memory
    with open(lookup_table_filename, 'r') as fh_curr:
        for line in fh_curr:
            (state, steps) = line.rstrip().split(':')

            if centers_solved_555(state) and steps_have_slice(steps):

                if lookup_table_type in ('5x5x5-stage-first-four-edges',
                                         '5x5x5-stage-second-four-edges',
                                         '5x5x5-stage-all-edges'):
                    steps = steps.split()
                else:

                    # We only need the edges to be paired, we do not need to move them to
                    # their home location so remove any trailing outside moves.
                    steps = remove_trailing_outside_moves(steps).split()

                # The first 54 characters are the centers state
                edges = ''.join(state[54:])

                if edges not in keepers:
                    keepers[edges] = steps
                elif len(steps) < len(keepers[edges]):
                    keepers[edges] = steps

    with open(lookup_table_filename_final, 'w') as fh_keepers:
        for (state, steps) in keepers.items():
            fh_keepers.write("%s:%s\n" % (state, ' '.join(steps)))

    log.warning("%s keeper_count %d" % (level_desc, len(keepers)))

    if mac:
        subprocess.check_output("LC_ALL=C nice sort --temporary-directory=./tmp/ --output=%s %s" %
            (lookup_table_filename_final, lookup_table_filename_final), shell=True)
    else:
        subprocess.check_output("LC_ALL=C nice sort --parallel=%d --temporary-directory=./tmp/ --output=%s %s" %
            (CORES, lookup_table_filename_final, lookup_table_filename_final), shell=True)

    if do_move:
        shutil.move(lookup_table_filename_final, lookup_table_filename)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    parser = argparse.ArgumentParser()
    parser.add_argument('--depth', type=int, default=5, help='The number of moves deep to explore')
    parser.add_argument('--cores', type=int, default=1, help='The number of CPU cores to use')
    parser.add_argument('--type', type=str, help='The type of lookup table to build')
    parser.add_argument('--option', type=str, default=None, help='option to pass to rotate.c')
    parser.add_argument('--noturn', action='store_true', default=False)
    parser.add_argument('--backup', action='store_true', default=False)
    parser.add_argument('--mac', action='store_true', default=False)
    args = parser.parse_args()
    MAX_DEPTH = args.depth
    CORES = args.cores
    lookup_table_type = args.type

    if lookup_table_type not in lookup_tables:
        print("%s is an invalid --type, choices are\n    %s\n" %
            (lookup_table_type, '\n    '.join(sorted(lookup_tables.keys()))))
        sys.exit(1)

    # file maintenance
    workq_filename = 'tmp/workq.txt'
    workq_filename1 = workq_filename + '1'
    workq_results_filename = 'tmp/workq-results.txt'

    lookup_table_filename = 'lookup-table.txt'
    lookup_table_filename_original = lookup_table_filename + ".original"
    lookup_table_filename_final = lookup_table_filename + ".final"
    lookup_table_filename_diff = lookup_table_filename + ".diff"
    lookup_table_filename_gz = lookup_table_filename + ".gz"

    dest_filename = lookup_tables[lookup_table_type]['filename']

    if args.option:
        dest_filename += '.' + args.option

    # If there is a lookup_table_filename that means we have run this
    # program before, gone to some depth MAX_DEPTH of x and now we've
    # increased MAX_DEPTH to be > x and are running again.  We do not
    # want to repeat all of the work we did to get to x though so pick
    # up where we left off.
    if os.path.exists(lookup_table_filename):

        if not os.path.exists(workq_filename1) and os.path.exists(workq_filename1 + '.gz'):
            log.info("gunzip %s.gz" % workq_filename1)
            subprocess.check_output(['nice', 'gunzip', workq_filename1 + '.gz'])

        if not os.path.exists(workq_filename1):
            print("ERROR: lookup-table.txt exists but not %s" % workq_filename)
            sys.exit(1)

        # Read workq.txt1 to figure out our starting depth
        depth = None
        with open(workq_filename1, 'r') as fh:
            for line in fh:
                line = line.strip()

                if depth is None and line != 'INIT':
                    depth = len(line.split()) - 1
                    break

    # We are starting from scratch
    else:

        # remove all workq files
        if os.path.exists(workq_filename1):
            subprocess.call('rm tmp/workq*', shell=True)

        # Initialize the lookup-table.txt
        with open(lookup_table_filename, 'w') as fh:
            pass

        # Build a list of the starting steps to place in the workq.txt files
        lines = []

        lt = lookup_tables[lookup_table_type]

        if lt['size'] == '2x2x2':
            for step in moves_2x2x2:
                if step not in lt['illegal']:
                    lines.append(step)

        elif lt['size'] == '3x3x3':
            for step in moves_3x3x3:
                if step not in lt['illegal']:
                    lines.append(step)

        elif lt['size'] == '4x4x4':

            if lookup_table_type in ('4x4x4-pair-edges-stage-centers',
                                     '4x4x4-pair-edges-stage-centers-edges-only',
                                     '4x4x4-pair-edges-stage-centers-UD-only',
                                     '4x4x4-pair-edges-stage-centers-LR-only',
                                     '4x4x4-pair-edges-stage-centers-FB-only'):

                for step in moves_4x4x4:
                    if step not in lt['illegal']:

                        if step in ("L", "L'", "Lw", "Lw'", "R", "R'", "Rw", "Rw'"):
                            lines.append("%s L" % step)
                            lines.append('INIT')
                            lines.append("%s L'" % step)
                            lines.append('INIT')
                            lines.append("%s Lw" % step)
                            lines.append('INIT')
                            lines.append("%s Lw'" % step)
                            lines.append('INIT')
                            lines.append("%s R" % step)
                            lines.append('INIT')
                            lines.append("%s R'" % step)
                            lines.append('INIT')
                            lines.append("%s Rw" % step)
                            lines.append('INIT')
                            lines.append("%s Rw'" % step)
                            lines.append('INIT')

                        elif step in ("U", "U'", "Uw", "Uw'", "D", "D'", "Dw", "Dw'"):
                            lines.append("%s D" % step)
                            lines.append('INIT')
                            lines.append("%s D'" % step)
                            lines.append('INIT')
                            lines.append("%s Dw" % step)
                            lines.append('INIT')
                            lines.append("%s Dw'" % step)
                            lines.append('INIT')
                            lines.append("%s U" % step)
                            lines.append('INIT')
                            lines.append("%s U'" % step)
                            lines.append('INIT')
                            lines.append("%s Uw" % step)
                            lines.append('INIT')
                            lines.append("%s Uw'" % step)
                            lines.append('INIT')

                        elif step in ("F", "F'", "Fw", "Fw'", "B", "B'", "Bw", "Bw'"):
                            lines.append("%s B" % step)
                            lines.append('INIT')
                            lines.append("%s B'" % step)
                            lines.append('INIT')
                            lines.append("%s Bw" % step)
                            lines.append('INIT')
                            lines.append("%s Bw'" % step)
                            lines.append('INIT')
                            lines.append("%s F" % step)
                            lines.append('INIT')
                            lines.append("%s F'" % step)
                            lines.append('INIT')
                            lines.append("%s Fw" % step)
                            lines.append('INIT')
                            lines.append("%s Fw'" % step)
                            lines.append('INIT')

                        else:
                            lines.append(step)
                            lines.append('INIT')
            else:
                for step in moves_4x4x4:
                    if step not in lt['illegal']:
                        lines.append(step)

        elif lt['size'] == '5x5x5':

            for step in moves_5x5x5:
                if step not in lt['illegal']:
                    lines.append(step)

        elif lt['size'] == '6x6x6':
            for step in moves_6x6x6:
                if step not in lt['illegal']:
                    lines.append(step)

        elif lt['size'] == '7x7x7':

            # Do not unpair the outer UD oblique edges that have already been paired
            if lookup_table_type in ('7x7x7-UD-oblique-edge-pairing',
                                     '7x7x7-UD-oblique-edge-pairing-middle-only',
                                     '7x7x7-UD-oblique-edge-pairing-left-only',
                                     '7x7x7-UD-oblique-edge-pairing-right-only',
                                     '7x7x7-LR-oblique-edge-pairing',
                                     '7x7x7-LR-oblique-edge-pairing-middle-only',
                                     '7x7x7-LR-oblique-edge-pairing-left-only',
                                     '7x7x7-LR-oblique-edge-pairing-right-only'):

                for step in moves_7x7x7:
                    if step not in lt['illegal']:
                        if step == "3Rw2":
                            lines.append("3Rw2 3Lw2")
                        elif step == "3Lw2":
                            lines.append("3Lw2 3Rw2")
                        elif step == "3Fw2":
                            lines.append("3Fw2 3Bw2")
                        elif step == "3Bw2":
                            lines.append("3Bw2 3Fw2")
                        elif step == "3Uw2":
                            lines.append("3Uw2 3Dw2")
                        elif step == "3Dw2":
                            lines.append("3Dw2 3Uw2")
                        elif step == "3Uw":
                            lines.append("3Uw 3Dw'")
                        elif step == "3Uw'":
                            lines.append("3Uw' 3Dw")
                        elif step == "3Dw":
                            lines.append("3Dw 3Uw'")
                        elif step == "3Dw'":
                            lines.append("3Dw' 3Uw")
                        elif step.startswith("3"):
                            raise Exception("step is %s" % step)
                        else:
                            lines.append(step)
                        lines.append('INIT')
            else:
                for step in moves_7x7x7:
                    if step not in lt['illegal']:
                        lines.append(step)

        else:
            raise Exception("Add support for size %s" % lt['size'])

        # rarely used
        if args.noturn:
            lines = ['noturn',]

        workq_count = len(lines)
        depth = 0

        if not os.path.exists('tmp'):
            os.mkdir('tmp')

        # Initialize the workq.txt files (one per core)
        for core in range(1, CORES+1):
            (start_line, end_line) = get_start_end_lines(CORES, core, workq_count)
            filename = workq_filename + str(core)

            with open(filename, 'w') as fh:
                for line in lines[start_line:end_line]:
                    fh.write(line + '\n')

    while depth < MAX_DEPTH:
        level_desc = "Level %d/%d:" % (depth, MAX_DEPTH-1)

        log.info("%s cp %s %s" % (level_desc, lookup_table_filename, lookup_table_filename_original))
        # cp lookup-table.txt lookup-table.txt.original
        shutil.copyfile(lookup_table_filename, lookup_table_filename_original)

        log.info("%s begin gunzip workq.txt files" % level_desc)
        try:
            subprocess.check_output('nice gunzip tmp/workq.txt*.gz', shell=True)
        except subprocess.CalledProcessError:
            pass
        log.info("%s end   gunzip workq.txt files" % level_desc)
        log.info('')

        # Crunch the the workq file, figure out what the
        # cube will look like for each set of steps (multi core done)
        # ===========================================================
        log.info("%s begin rotate" % level_desc)
        threads = []

        for core in range(1, CORES+1):
            if os.path.exists(workq_filename + str(core)):
                cmd = ['nice',
                       './rotate',
                       '--input', workq_filename + str(core),
                       '--output', workq_results_filename + str(core),
                       '--type', lookup_table_type]

                if args.option is not None:
                    cmd.append('--option')
                    cmd.append(args.option)

                log.info("%s %s" % (level_desc, ' '.join(cmd)))
                thread = BackgroundProcess(cmd, 'rotate core %d' % core)
                thread.start()
                threads.append(thread)

        hit_error = False
        for thread in threads:
            thread.join()
            log.info("%s %s: finished" % (level_desc, thread))

            if not thread.ok:
                hit_error = True

        if hit_error:
            log.error("rotate BackgroundProcess hit an error")
            sys.exit(1)

        log.info("%s end   rotate" % level_desc)
        log.info('')

        # Process the workq-results.txt files (multi core done)
        # process-workq-results.py will write the results from the workq-results.txt file
        # (the one it is analyzing) to lookup-table.txt
        # ================================================
        log.info("%s begin process workq-results.txt files" % level_desc)
        hit_error = False
        threads = []

        for core in range(1, CORES+1):
            if os.path.exists(workq_results_filename + str(core)):
                cmd = ['nice',
                       './process-workq-results.py',
                       workq_results_filename + str(core),
                       '--type', lookup_table_type]
                log.info("%s %s" % (level_desc, ' '.join(cmd)))
                thread = BackgroundProcess(cmd, 'process-workq-results.py core %d' % core)
                thread.start()
                threads.append(thread)

        for thread in threads:
            thread.join()
            log.info("%s %s: finished" % (level_desc, thread))

            if not thread.ok:
                hit_error = True

        if hit_error:
            log.error("process-workq-results.py BackgroundProcess hit an error")
            sys.exit(1)

        log.info("%s end   process workq-results.txt files" % level_desc)

        # re-sort lookup-table.txt (multi core done)
        # =======================================================================
        if not os.path.isdir('./tmp/'):
            os.makedirs('./tmp/')
        log.info("%s begin sort" % level_desc)

        if args.mac:
            subprocess.check_output("LC_ALL=C nice sort --temporary-directory=./tmp/ --output=%s %s" %
                                    (lookup_table_filename, lookup_table_filename),
                                    shell=True)
        else:
            subprocess.check_output("LC_ALL=C nice sort --parallel=%d --temporary-directory=./tmp/ --output=%s %s" %
                                    (CORES, lookup_table_filename, lookup_table_filename),
                                    shell=True)
        log.info("%s end   sort" % level_desc)
        log.info('')

        # - go line by line through lookup-table.txt and lookup-table.txt.original (in parallel)
        # - parse the state:steps from each
        # - write the results to lookup-table.txt.final
        # ================================================
        log.info("%s begin write %s" % (level_desc, lookup_table_filename_final))
        tmp_line_number = 0

        # log.info("./utils/sanity.py %s" % lookup_table_filename_original)
        # subprocess.check_output("nice ./utils/sanity.py %s" % lookup_table_filename_original, shell=True)

        with open(lookup_table_filename, 'r') as fh_curr:
            with open(lookup_table_filename_original, 'r') as fh_orig:
                with open(lookup_table_filename_final, 'w') as fh_final:

                    prev_state_orig = None
                    prev_state_curr = None
                    to_write = []
                    to_write_count = 0
                    line_orig = advance_filehandle(fh_orig)
                    line_curr = advance_filehandle(fh_curr)

                    while line_orig or line_curr:
                        tmp_line_number += 1

                        if line_orig is None:
                            state_orig = None
                            steps_orig = None
                        else:
                            (state_orig, steps_orig) = line_orig.split(':')

                        if line_curr is None:
                            state_curr = None
                            steps_curr = None
                        else:
                            try:
                                (state_curr, steps_curr) = line_curr.split(':')
                            except ValueError:
                                log.info("LINE %d: '%s'" % (tmp_line_number, line))
                                raise

                        # handle the scenario where one file ends before the other
                        # - write the line_curr entry
                        # - advance the line_curr filehandle until it is on a different state
                        if state_orig is None:
                            to_write.append(line_curr)
                            to_write_count += 1
                            line_curr = advance_filehandle_to_state_change(state_curr, fh_curr)

                        # No brainer
                        # - keep the line from the original lookup-table.txt
                        # - advance the fh_orig filehandle
                        elif state_curr is None:
                            to_write.append(line_orig)
                            to_write_count += 1
                            line_orig = advance_filehandle(fh_orig)

                        # No brainer
                        # - keep the line from the original lookup-table.txt
                        # - advance the fh_orig filehandle
                        elif state_orig < state_curr:
                            to_write.append(line_orig)
                            to_write_count += 1
                            line_orig = advance_filehandle(fh_orig)

                        # Also a no brainer
                        # - keep the line from the original lookup-table.txt
                        # - advance the fh_orig filehandle
                        # - advance the line_curr filehandle until it is on a different state
                        elif state_orig == state_curr:
                            to_write.append(line_orig)
                            to_write_count += 1
                            line_orig = advance_filehandle(fh_orig)
                            line_curr = advance_filehandle_to_state_change(state_curr, fh_curr)

                        # This is a new state for lookup-table.txt
                        # - write the line_curr entry
                        # - advance the line_curr filehandle until it is on a different state
                        elif state_orig > state_curr:
                            to_write.append(line_curr)
                            to_write_count += 1
                            line_curr = advance_filehandle_to_state_change(state_curr, fh_curr)

                        # Batch the writes
                        if to_write_count % 10000 == 0:
                            fh_final.write('\n'.join(to_write) + '\n')
                            to_write = []

                            if to_write_count % 1000000 == 0:
                                log.info("%s %d" % (level_desc, tmp_line_number))

                        prev_state_orig = state_orig
                        prev_state_curr = state_curr

                    if to_write:
                        fh_final.write('\n'.join(to_write) + '\n')
                        log.info("%s %d" % (level_desc, to_write_count))
                        to_write = []

        # log.info("./utils/sanity.py %s" % lookup_table_filename_final)
        # subprocess.check_output("nice ./utils/sanity.py %s" % lookup_table_filename_final, shell=True)

        # mv lookup-table.txt.final lookup-table.txt
        shutil.move(lookup_table_filename_final, lookup_table_filename)
        log.info("%s end   write %s" % (level_desc, lookup_table_filename_final))
        log.info('')

        # Print how many "keepers" we have found so far...this is only to give you some sense
        # of progress while the builder is running.
        if depth < MAX_DEPTH-1:
            if lookup_table_type in type_edges_444:
                write_keepers_444(lookup_table_type, level_desc, lookup_table_filename, 'keepers.txt', False, args.mac)

            elif lookup_table_type in type_edges_555:
                write_keepers_555(lookup_table_type, level_desc, lookup_table_filename, 'keepers.txt', False, args.mac)

        # TODO we should only do this if do_repopulate_workq() returns True

        # diff lookup-table.txt vs lookup-table.txt.original
        # (this step cannot be spread over multiple cores)
        # ================================================
        log.info("%s begin diff %s vs %s" % (level_desc, lookup_table_filename_original, lookup_table_filename))
        if depth == 0:
            shutil.copyfile(lookup_table_filename, lookup_table_filename_diff)
        else:

            if args.mac:
                cmd = "comm -3 %s %s > %s" % (lookup_table_filename_original, lookup_table_filename, lookup_table_filename_diff)
            else:
                cmd = "comm -3 --nocheck-order %s %s > %s" % (lookup_table_filename_original, lookup_table_filename, lookup_table_filename_diff)

            log.info("comm: %s" % cmd)
            subprocess.call(cmd, shell=True)

        log.info("%s end   diff %s vs %s" % (level_desc, lookup_table_filename_original, lookup_table_filename))
        log.info('')
        lookup_table_filename_diff_count = int(subprocess.check_output(['nice', 'wc', '-l', lookup_table_filename_diff]).decode('ascii').split()[0])
        os.remove(lookup_table_filename_original)

        if lookup_table_filename_diff_count == 0:
            print("comm -3 did not find a delta...we are done")
            break

        # re-populate the workq
        # =====================
        log.info("%s begin re-populate %s files" % (level_desc, workq_filename))
        threads = []

        if do_repopulate_workq(lookup_table_filename_diff_count, depth, MAX_DEPTH, lookup_table_type):
            hit_error = False

            for core in range(1, CORES+1):
                filename = workq_filename + str(core)

                if os.path.exists(filename):
                    os.remove(filename)

                (start_line, end_line) = get_start_end_lines(CORES, core, lookup_table_filename_diff_count)

                if end_line == 0:
                    raise Exception("lookup_table_filename_diff_count %d, core %d, start_line %d, end_line %d" %
                        (lookup_table_filename_diff_count, core, start_line, end_line))

                if end_line is not None:
                    cmd = ['nice',
                           './repopulate-workq.py',
                            '--input', lookup_table_filename_diff,
                            '--output', filename,
                            '--start', str(start_line),
                            '--end', str(end_line),
                            '--type', lookup_table_type,
                            '--max-depth', str(MAX_DEPTH)]

                    log.info("%s %s" % (level_desc, ' '.join(cmd)))
                    thread = BackgroundProcess(cmd, 'repopulate-workq.py core %d' % core)
                    thread.start()
                    threads.append(thread)

            for thread in threads:
                thread.join()
                log.info("%s %s: finished" % (level_desc, thread))

                if not thread.ok:
                    hit_error = True

            if hit_error:
                log.error("repopulate-workq.py BackgroundProcess hit an error")
                sys.exit(1)

            # TODO this needs to cat together all of the workq files and split them apart into even chunks
            workq_count = True
        else:
            workq_count = False

        # rm lookup-table.txt.diff
        if os.path.exists(lookup_table_filename_diff):
            os.remove(lookup_table_filename_diff)
        log.info("%s end   re-populate %s files" % (level_desc, workq_filename))
        log.info('')

        # Remove the older backups
        for x in range(depth):
            backup_dir = "./backup-%d/" % x
            if os.path.isdir(backup_dir):
                shutil.rmtree(backup_dir)

        # backup everything
        # =================
        if args.backup and do_backup(workq_count, depth, MAX_DEPTH, lookup_table_type):
            log.info("%s begin backup" % level_desc)

            backup_dir = "./backup-%d/" % depth
            if os.path.isdir(backup_dir):
                shutil.rmtree(backup_dir)
            os.makedirs(backup_dir)

            # We used to gzip everything here prior to copying it to the backup directory, we did
            # this to save disk space but it waste a lot of time and you don't keep the files for
            # all that long anyway so just leave them unzipped.

            #lookup_table_filename_gz = lookup_table_filename + '.gz'
            #if not os.path.exists(lookup_table_filename_gz):
            #    subprocess.check_output(['nice', 'gzip', '--keep', '--fast', lookup_table_filename])
            #subprocess.check_output("nice mv %s.gz %s" % (lookup_table_filename, backup_dir), shell=True)
            subprocess.check_output("nice cp %s %s" % (lookup_table_filename, backup_dir), shell=True)

            #subprocess.check_output("nice gzip --keep --fast tmp/workq.txt*", shell=True)
            #subprocess.check_output("nice mv tmp/*.gz %s" % backup_dir, shell=True)
            subprocess.check_output("nice cp tmp/* %s" % backup_dir, shell=True)

            log.info("%s end   backup" % level_desc)

        log.info('')
        log.info('')
        log.info('')
        log.info('')
        depth += 1

        if not workq_count:
            break

    # Only keep the entries where the centers are intact (keepers)
    if lookup_table_type in type_edges_444:
        write_keepers_444(lookup_table_type, level_desc, lookup_table_filename, lookup_table_filename_final, True, args.mac)

    elif lookup_table_type in type_edges_555:
        write_keepers_555(lookup_table_type, level_desc, lookup_table_filename, lookup_table_filename_final, True, args.mac)

    # Run print-histogram.py
    output = subprocess.check_output(['nice', './utils/print-histogram.py', lookup_table_filename]).decode('ascii')
    log.info('\n' + output)

    with open('histogram.txt', 'a') as fh:
        fh.write(dest_filename + '\n')
        fh.write('=' * len(dest_filename) + '\n')
        fh.write(output + '\n')

    if not lookup_tables[lookup_table_type]['allsteps']:
        subprocess.check_output(['nice', './utils/chop-all-but-last-step.py', lookup_table_filename])

    # Make all lines the same length by adding whitespaces to the end. This is needed
    # to simplify binary searching of the file.
    subprocess.check_output(['nice', './utils/pad-lines.py', lookup_table_filename])

    shutil.move(lookup_table_filename, dest_filename)
    log.info('Finished!!')

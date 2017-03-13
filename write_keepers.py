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


def centers_solved_555(state):
    if state[0:54] == 'UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD':
        return True
    return False


def write_keepers_444(lookup_table_type, level_desc, lookup_table_filename, lookup_table_filename_final, do_move, mac):
    lookup_table_filename_grep = lookup_table_filename + '.grep'
    log.info("%s grep for lines with solved centers" % level_desc)

    if not os.path.exists(lookup_table_filename_grep):
        subprocess.check_output("grep ^UUUULLLLFFFFRRRRBBBBDDDD %s > %s" %
            (lookup_table_filename, lookup_table_filename_grep), shell=True)

    log.info("%s find keepers" % level_desc)
    with open(lookup_table_filename_final, 'w') as fh_keepers:
        with open(lookup_table_filename_grep, 'r') as fh_curr:
            prev_edges = None
            min_steps = []

            for (line_number, line) in enumerate(fh_curr):
                (state, steps) = line.rstrip().split(':')

                if steps_have_slice(steps):

                    # The first 24 characters are the centers state
                    edges = ''.join(state[24:])

                    # We only need the edges to be paired, we do not need to move them to
                    # their home location so remove any trailing outside moves.
                    steps = remove_trailing_outside_moves(steps).split()

                    if prev_edges is None:
                        min_steps = steps
                    else:
                        if edges == prev_edges:
                            if len(steps) < len(min_steps):
                                min_steps = steps
                        else:
                            fh_keepers.write("%s:%s\n" % (prev_edges, ' '.join(min_steps)))
                            min_steps = steps

                    prev_edges = edges

                if line_number % 1000000 == 0:
                    log.info(line_number)

            if min_steps:
                fh_keepers.write("%s:%s\n" % (prev_edges, ' '.join(min_steps)))

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
    parser.add_argument('--type', type=str, help='The type of lookup table to build')
    parser.add_argument('--mac', action='store_true', default=False)
    args = parser.parse_args()
    lookup_table_type = args.type

    # file maintenance
    lookup_table_filename = 'lookup-table.txt'
    lookup_table_filename_original = lookup_table_filename + ".original"
    lookup_table_filename_final = lookup_table_filename + ".final"
    lookup_table_filename_diff = lookup_table_filename + ".diff"
    lookup_table_filename_gz = lookup_table_filename + ".gz"
    level_desc = 'N/A'

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
    subprocess.check_output(['nice', './utils/pad_lines.py', lookup_table_filename])

    shutil.move(lookup_table_filename, dest_filename)
    log.info('Finished!!')

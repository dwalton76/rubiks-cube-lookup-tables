#!/usr/bin/env python3

from copy import copy
import argparse
import gc
import logging
import math
import os
import subprocess
import sys
from rotate_xxx import rotate_777
from builder import lookup_tables
from pprint import pformat


def reverse_steps(steps):
    results = []
    for step in reversed(steps):
        if step.endswith("2"):
            pass
        elif step.endswith("'"):
            step = step[0:-1]
        else:
            step += "'"
        results.append(step)
    return results


def convert_state_to_hex(state):
    """
    This assumes that state only has "x"s and Us or Ls or Fs or Rs or Bs or Ds
    """
    state = state.replace('x', '0').replace('U', '1').replace('L', '1').replace('F', '1').replace('R', '1').replace('B', '1').replace('D', '1')
    hex_width = int(math.ceil(len(state)/4.0))
    hex_state = hex(int(state, 2))[2:]

    if hex_state.endswith('L'):
        hex_state = hex_state[:-1]

    return hex_state.zfill(hex_width)


def do_nothing(state):
    return state


def reflect_y_777(cube):
    """
    Used the following to print the guts of this function

    for x in (7, 154, 105, 56, 203, 252):
        for y in range(7):
            print("        cube[%d], cube[%d], cube[%d], cube[%d], cube[%d], cube[%d], cube[%d]," % (x+y, x+y-1, x+y-2, x+y-3, x+y-4, x+y-5, x+y-6))
            x += 6

    """
    return [cube[0],
        # upper
        cube[7], cube[6], cube[5], cube[4], cube[3], cube[2], cube[1],
        cube[14], cube[13], cube[12], cube[11], cube[10], cube[9], cube[8],
        cube[21], cube[20], cube[19], cube[18], cube[17], cube[16], cube[15],
        cube[28], cube[27], cube[26], cube[25], cube[24], cube[23], cube[22],
        cube[35], cube[34], cube[33], cube[32], cube[31], cube[30], cube[29],
        cube[42], cube[41], cube[40], cube[39], cube[38], cube[37], cube[36],
        cube[49], cube[48], cube[47], cube[46], cube[45], cube[44], cube[43],

        # left...left and right trade places
        cube[154], cube[153], cube[152], cube[151], cube[150], cube[149], cube[148],
        cube[161], cube[160], cube[159], cube[158], cube[157], cube[156], cube[155],
        cube[168], cube[167], cube[166], cube[165], cube[164], cube[163], cube[162],
        cube[175], cube[174], cube[173], cube[172], cube[171], cube[170], cube[169],
        cube[182], cube[181], cube[180], cube[179], cube[178], cube[177], cube[176],
        cube[189], cube[188], cube[187], cube[186], cube[185], cube[184], cube[183],
        cube[196], cube[195], cube[194], cube[193], cube[192], cube[191], cube[190],

        # front
        cube[105], cube[104], cube[103], cube[102], cube[101], cube[100], cube[99],
        cube[112], cube[111], cube[110], cube[109], cube[108], cube[107], cube[106],
        cube[119], cube[118], cube[117], cube[116], cube[115], cube[114], cube[113],
        cube[126], cube[125], cube[124], cube[123], cube[122], cube[121], cube[120],
        cube[133], cube[132], cube[131], cube[130], cube[129], cube[128], cube[127],
        cube[140], cube[139], cube[138], cube[137], cube[136], cube[135], cube[134],
        cube[147], cube[146], cube[145], cube[144], cube[143], cube[142], cube[141],

        # right...left and right trade places
        cube[56], cube[55], cube[54], cube[53], cube[52], cube[51], cube[50],
        cube[63], cube[62], cube[61], cube[60], cube[59], cube[58], cube[57],
        cube[70], cube[69], cube[68], cube[67], cube[66], cube[65], cube[64],
        cube[77], cube[76], cube[75], cube[74], cube[73], cube[72], cube[71],
        cube[84], cube[83], cube[82], cube[81], cube[80], cube[79], cube[78],
        cube[91], cube[90], cube[89], cube[88], cube[87], cube[86], cube[85],
        cube[98], cube[97], cube[96], cube[95], cube[94], cube[93], cube[92],

        # back
        cube[203], cube[202], cube[201], cube[200], cube[199], cube[198], cube[197],
        cube[210], cube[209], cube[208], cube[207], cube[206], cube[205], cube[204],
        cube[217], cube[216], cube[215], cube[214], cube[213], cube[212], cube[211],
        cube[224], cube[223], cube[222], cube[221], cube[220], cube[219], cube[218],
        cube[231], cube[230], cube[229], cube[228], cube[227], cube[226], cube[225],
        cube[238], cube[237], cube[236], cube[235], cube[234], cube[233], cube[232],
        cube[245], cube[244], cube[243], cube[242], cube[241], cube[240], cube[239],

        # down
        cube[252], cube[251], cube[250], cube[249], cube[248], cube[247], cube[246],
        cube[259], cube[258], cube[257], cube[256], cube[255], cube[254], cube[253],
        cube[266], cube[265], cube[264], cube[263], cube[262], cube[261], cube[260],
        cube[273], cube[272], cube[271], cube[270], cube[269], cube[268], cube[267],
        cube[280], cube[279], cube[278], cube[277], cube[276], cube[275], cube[274],
        cube[287], cube[286], cube[285], cube[284], cube[283], cube[282], cube[281],
        cube[294], cube[293], cube[292], cube[291], cube[290], cube[289], cube[288]
    ]


def oblique_edges_777(state):
    state = 'x' + state
    state = ''.join((state[10], state[11], state[12],
                     state[16], state[20],
                     state[23], state[27],
                     state[30], state[34],
                     state[38], state[39], state[40],

                     state[59], state[60], state[61],
                     state[65], state[69],
                     state[72], state[76],
                     state[79], state[83],
                     state[87], state[88], state[89],

                     state[108], state[109], state[110],
                     state[114], state[118],
                     state[121], state[125],
                     state[128], state[132],
                     state[136], state[137], state[138],

                     state[157], state[158], state[159],
                     state[163], state[167],
                     state[170], state[174],
                     state[177], state[181],
                     state[185], state[186], state[187],

                     state[206], state[207], state[208],
                     state[212], state[216],
                     state[219], state[223],
                     state[226], state[230],
                     state[234], state[235], state[236],

                     state[255], state[256], state[257],
                     state[261], state[265],
                     state[268], state[272],
                     state[275], state[279],
                     state[283], state[284], state[285]))
    return state


state_functions = {
    ('7x7x7', 'oblique-edges')      : oblique_edges_777,
}


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='The workq file to process')
    parser.add_argument('--type', type=str, help='The type of lookup table to build')
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        print("ERROR: %s does not exist" % args.filename)
        sys.exit(1)

    lookup_table_add_count = 0
    lookup_table_filename = 'lookup-table.txt'
    lt = lookup_tables[args.type]

    known = set()
    known_count = 0

    lt_hex = lt['hex']
    lt_size = lt['size']
    lt_keep = lt['keep']
    lookup_table_add = []
    line_number = 0

    state_function = state_functions.get((lt_size, lt_keep))
    assert state_function is not None, "state_function is None for (%s, %s)" % (lt_size, lt_keep)

    with open(args.filename, 'r') as fh_workq_results:
        for line in fh_workq_results:
            try:
                (state, steps) = line.rstrip().split(':')
            except ValueError:
                continue

            if lt_size == '4x4x4' and lt_keep == 'centers-and-edge-parity':
                state = state_function(state, steps)
            else:
                state = state_function(state)

            if lt_hex:
                state = convert_state_to_hex(state)

            if state not in known:

                # Ideally we would never add an entry to the lookup table that is
                # already there, if we could do that the 'sort' phase would be much
                # faster as lookup-table.txt would be much smaller since it wouldn't
                # contain tons of duplicate entries. We do not have enough RAM to
                # create a set() to store all of the entries though so store up to
                # 2 million of them as a means of avoiding adding some duplicates.
                #
                # time ./builder.py --cores 4 --depth 6 --type 4x4x4-UD-centers-stage
                # With the 'known' set this it took 56s
                # Without the 'known' set this it took 1m 13s
                if known_count >= 2000000:
                    known = set()
                    known_count = 0
                    gc.collect()
                    # log.info("%s: reset known set()" % args.filename)
                known.add(state)
                known_count += 1

                # Add entries to the lookup table file but batch the writes
                steps_reversed = reverse_steps(steps.split())
                steps_reversed_str = ' '.join(steps_reversed)

                lookup_table_add.append("%s:%s" % (state, steps_reversed_str))
                lookup_table_add_count += 1

                if lookup_table_add_count % 10000 == 0:

                    # We are going to have to sort lookup-table.txt later so sort the little
                    # chunk we are about to write to that file...it can't hurt
                    lookup_table_add = sorted(lookup_table_add)

                    with open(lookup_table_filename, 'a') as fh_lookup_table:
                        fh_lookup_table.write('\n'.join(lookup_table_add) + '\n')

                    lookup_table_add = []

                    if lookup_table_add_count % 1000000 == 0:
                        log.info("%s: added %d, line %d" % (args.filename, lookup_table_add_count, line_number))

            line_number += 1

        if lookup_table_add:
            lookup_table_add = sorted(lookup_table_add)
            with open(lookup_table_filename, 'a') as fh_lookup_table:
                fh_lookup_table.write('\n'.join(lookup_table_add) + '\n')
            lookup_table_add = []

    log.info("%s: DONE added %d" % (args.filename, lookup_table_add_count))

    # rm the workq-results file (we are finished with it)
    if os.path.exists(args.filename):
        os.unlink(args.filename)
    sys.exit(0)

#!/usr/bin/env python3

from copy import copy
import argparse
import gc
import logging
import math
import os
import subprocess
import sys
from rotate_xxx import rotate_444, rotate_555, rotate_777
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


def edges_333(state):
    state = 'x' + state
    state = ''.join((state[2], state[4], state[6], state[8],
                     state[11], state[13], state[15], state[17],
                     state[20], state[22], state[24], state[26],
                     state[29], state[31], state[33], state[35],
                     state[38], state[40], state[42], state[44],
                     state[47], state[49], state[51], state[53]))
    return state


def corners_333(state):
    state = 'x' + state
    state = ''.join((state[1], state[3], state[7], state[9],
                     state[10], state[12], state[16], state[18],
                     state[19], state[21], state[25], state[27],
                     state[28], state[30], state[34], state[36],
                     state[37], state[39], state[43], state[45],
                     state[46], state[48], state[52], state[54]))
    return state



def edges_444(state):
    state = 'x' + state
    state = ''.join((state[2:4],   state[5],  state[8:10],  state[12], state[14:16],
                     state[18:20], state[21], state[24:26], state[28], state[30:32],
                     state[34:36], state[37], state[40:42], state[44], state[46:48],
                     state[50:52], state[53], state[56:58], state[60], state[62:64],
                     state[66:68], state[69], state[72:74], state[76], state[78:80],
                     state[82:84], state[85], state[88:90], state[92], state[94:96]))
    return state


symmetry_rotations_tsai_phase3_444 =\
    ("",
     "y y",
     "x",
     "x y y",
     "x'",
     "x' y y",
     "x x",
     "x x y y",
     "reflect-x",
     "reflect-x y y",
     "reflect-x x",
     "reflect-x x y y",
     "reflect-x x'",
     "reflect-x x' y y",
     "reflect-x x x",
     "reflect-x x x y y")


def reflect_x_444(cube):
    return [cube[0],
           cube[93], cube[94], cube[95], cube[96],
           cube[89], cube[90], cube[91], cube[92],
           cube[85], cube[86], cube[87], cube[88],
           cube[81], cube[82], cube[83], cube[84],

           cube[29], cube[30], cube[31], cube[32],
           cube[25], cube[26], cube[27], cube[28],
           cube[21], cube[22], cube[23], cube[24],
           cube[17], cube[18], cube[19], cube[20],

           cube[45], cube[46], cube[47], cube[48],
           cube[41], cube[42], cube[43], cube[44],
           cube[37], cube[38], cube[39], cube[40],
           cube[33], cube[34], cube[35], cube[36],

           cube[61], cube[62], cube[63], cube[64],
           cube[57], cube[58], cube[59], cube[60],
           cube[53], cube[54], cube[55], cube[56],
           cube[49], cube[50], cube[51], cube[52],

           cube[77], cube[78], cube[79], cube[80],
           cube[73], cube[74], cube[75], cube[76],
           cube[69], cube[70], cube[71], cube[72],
           cube[65], cube[66], cube[67], cube[68],

           cube[13], cube[14], cube[15], cube[16],
           cube[9], cube[10], cube[11], cube[12],
           cube[5], cube[6], cube[7], cube[8],
           cube[1], cube[2], cube[3], cube[4]]


def reflect_y_555(cube):
    """
SIZE = 5
for x in (5, 80, 55, 30, 105, 130):
    for y in range(SIZE):
        print("        cube[%d], cube[%d], cube[%d], cube[%d], cube[%d]," % (x+y, x+y-1, x+y-2, x+y-3, x+y-4))
        x += (SIZE - 1)
    print("")
    """
    return [cube[0],
        cube[5], cube[4], cube[3], cube[2], cube[1],
        cube[10], cube[9], cube[8], cube[7], cube[6],
        cube[15], cube[14], cube[13], cube[12], cube[11],
        cube[20], cube[19], cube[18], cube[17], cube[16],
        cube[25], cube[24], cube[23], cube[22], cube[21],

        cube[80], cube[79], cube[78], cube[77], cube[76],
        cube[85], cube[84], cube[83], cube[82], cube[81],
        cube[90], cube[89], cube[88], cube[87], cube[86],
        cube[95], cube[94], cube[93], cube[92], cube[91],
        cube[100], cube[99], cube[98], cube[97], cube[96],

        cube[55], cube[54], cube[53], cube[52], cube[51],
        cube[60], cube[59], cube[58], cube[57], cube[56],
        cube[65], cube[64], cube[63], cube[62], cube[61],
        cube[70], cube[69], cube[68], cube[67], cube[66],
        cube[75], cube[74], cube[73], cube[72], cube[71],

        cube[30], cube[29], cube[28], cube[27], cube[26],
        cube[35], cube[34], cube[33], cube[32], cube[31],
        cube[40], cube[39], cube[38], cube[37], cube[36],
        cube[45], cube[44], cube[43], cube[42], cube[41],
        cube[50], cube[49], cube[48], cube[47], cube[46],

        cube[105], cube[104], cube[103], cube[102], cube[101],
        cube[110], cube[109], cube[108], cube[107], cube[106],
        cube[115], cube[114], cube[113], cube[112], cube[111],
        cube[120], cube[119], cube[118], cube[117], cube[116],
        cube[125], cube[124], cube[123], cube[122], cube[121],

        cube[130], cube[129], cube[128], cube[127], cube[126],
        cube[135], cube[134], cube[133], cube[132], cube[131],
        cube[140], cube[139], cube[138], cube[137], cube[136],
        cube[145], cube[144], cube[143], cube[142], cube[141],
        cube[150], cube[149], cube[148], cube[147], cube[146]
    ]


def reflect_y_666(cube):
    """
SIZE = 6
for x in (6, 114, 78, 42, 150, 186):

    for y in range(SIZE):
        print("        cube[%d], cube[%d], cube[%d], cube[%d], cube[%d], cube[%d]," % (x+y, x+y-1, x+y-2, x+y-3, x+y-4, x+y-5))
        x += (SIZE - 1)
    print("")
    """
    return [cube[0],
        cube[6], cube[5], cube[4], cube[3], cube[2], cube[1],
        cube[12], cube[11], cube[10], cube[9], cube[8], cube[7],
        cube[18], cube[17], cube[16], cube[15], cube[14], cube[13],
        cube[24], cube[23], cube[22], cube[21], cube[20], cube[19],
        cube[30], cube[29], cube[28], cube[27], cube[26], cube[25],
        cube[36], cube[35], cube[34], cube[33], cube[32], cube[31],

        cube[114], cube[113], cube[112], cube[111], cube[110], cube[109],
        cube[120], cube[119], cube[118], cube[117], cube[116], cube[115],
        cube[126], cube[125], cube[124], cube[123], cube[122], cube[121],
        cube[132], cube[131], cube[130], cube[129], cube[128], cube[127],
        cube[138], cube[137], cube[136], cube[135], cube[134], cube[133],
        cube[144], cube[143], cube[142], cube[141], cube[140], cube[139],

        cube[78], cube[77], cube[76], cube[75], cube[74], cube[73],
        cube[84], cube[83], cube[82], cube[81], cube[80], cube[79],
        cube[90], cube[89], cube[88], cube[87], cube[86], cube[85],
        cube[96], cube[95], cube[94], cube[93], cube[92], cube[91],
        cube[102], cube[101], cube[100], cube[99], cube[98], cube[97],
        cube[108], cube[107], cube[106], cube[105], cube[104], cube[103],

        cube[42], cube[41], cube[40], cube[39], cube[38], cube[37],
        cube[48], cube[47], cube[46], cube[45], cube[44], cube[43],
        cube[54], cube[53], cube[52], cube[51], cube[50], cube[49],
        cube[60], cube[59], cube[58], cube[57], cube[56], cube[55],
        cube[66], cube[65], cube[64], cube[63], cube[62], cube[61],
        cube[72], cube[71], cube[70], cube[69], cube[68], cube[67],

        cube[150], cube[149], cube[148], cube[147], cube[146], cube[145],
        cube[156], cube[155], cube[154], cube[153], cube[152], cube[151],
        cube[162], cube[161], cube[160], cube[159], cube[158], cube[157],
        cube[168], cube[167], cube[166], cube[165], cube[164], cube[163],
        cube[174], cube[173], cube[172], cube[171], cube[170], cube[169],
        cube[180], cube[179], cube[178], cube[177], cube[176], cube[175],

        cube[186], cube[185], cube[184], cube[183], cube[182], cube[181],
        cube[192], cube[191], cube[190], cube[189], cube[188], cube[187],
        cube[198], cube[197], cube[196], cube[195], cube[194], cube[193],
        cube[204], cube[203], cube[202], cube[201], cube[200], cube[199],
        cube[210], cube[209], cube[208], cube[207], cube[206], cube[205],
        cube[216], cube[215], cube[214], cube[213], cube[212], cube[211]
    ]


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


# 12-23 are high edges, make these U (1)
# 0-11 are low edges, make these D (6)
# https://github.com/cs0x7f/TPR-4x4x4-Solver/blob/master/src/FullCube.java
high_edges_444 = ((14, 2, 67),  # upper
                  (13, 9, 19),
                  (15, 8, 51),
                  (12, 15, 35),
                  (21, 25, 76), # left
                  (20, 24, 37),
                  (23, 57, 44), # right
                  (22, 56, 69),
                  (18, 82, 46), # down
                  (17, 89, 30),
                  (19, 88, 62),
                  (16, 95, 78))

low_edges_444 = ((2, 3, 66),  # upper
                 (1, 5, 18),
                 (3, 12, 50),
                 (0, 14, 34),
                 (9, 21, 72), # left
                 (8, 28, 41),
                 (11, 53, 40), # right
                 (10, 60, 73),
                 (6, 83, 47), # down
                 (5, 85, 31),
                 (7, 92, 63),
                 (4, 94, 79))

def edges_high_low_recolor_444(state):
    """
    Look at all of the high edges and find the low edge for each.
    Return a cube state that represents where all the low edge siblings
    live in relation to their high edge counterpart.
    """

    #assert len(state) == 97, "Invalid state %s, len is %d" % (state, len(state))
    low_edge_map = {}

    for (low_edge_index, square_index, partner_index) in low_edges_444:
        square_value = state[square_index]
        partner_value = state[partner_index]
        #assert square_value != partner_value, "both squares are %s" % square_value
        wing_str = ''.join(sorted([square_value, partner_value]))
        low_edge_index = str(hex(low_edge_index))[2:]
        state[square_index] = low_edge_index
        state[partner_index] = low_edge_index

        #assert wing_str not in low_edge_map, "We have two %s wings, one at high_index %s %s and one at high_index %s (%d, %d), state %s" %\
        #    (wing_str,
        #     low_edge_map[wing_str],
        #     pformat(low_edges_444[int(low_edge_map[wing_str])]),
        #     low_edge_index,
        #     square_index, partner_index,
        #     ''.join(state[1:]))

        # save low_edge_index in hex and chop the leading 0x via [2:]
        low_edge_map[wing_str] = low_edge_index

    #assert len(low_edge_map.keys()) == 12, "Invalid low_edge_map\n%s\n" % pformat(low_edge_map)

    for (high_edge_index, square_index, partner_index) in high_edges_444:
        square_value = state[square_index]
        partner_value = state[partner_index]
        wing_str = ''.join(sorted([square_value, partner_value]))
        state[square_index] = low_edge_map[wing_str]
        state[partner_index] = low_edge_map[wing_str]
    return state


def edges_high_low_pattern_444(state):
    original_state = list('x' + state)
    state = edges_high_low_recolor_444(original_state[:])

    # record the state of all edges
    state = ''.join(state)
    state = ''.join((state[2],   state[9],  state[8],  state[15],
                     state[25], state[24],
                     state[57], state[56],
                     state[82], state[89], state[88], state[95]))
    return state


def edges_high_low_pattern_symmetry_444(state):
    original_state = list('x' + state)
    results = []

    for seq in symmetry_rotations_tsai_phase3_444:
        state = original_state[:]

        for step in seq.split():
            if step == 'reflect-x':
                state = reflect_x_444(state[:])
            else:
                state = rotate_444(state[:], step)

        state = edges_high_low_recolor_444(state[:])

        # record the state of all edges
        state = ''.join(state)
        state = ''.join((state[2],   state[9],  state[8],  state[15],
                         state[25], state[24],
                         state[57], state[56],
                         state[82], state[89], state[88], state[95]))
        results.append(state[:])

    results = sorted(results)
    return results[0]


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


def centers_and_edges_pattern_444(state):
    state = list('x' + state)
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

    centers = ''.join((
        state[6:8],   state[10:12],
        state[22:24], state[26:28],
        state[38:40], state[42:44],
        state[54:56], state[58:60],
        state[70:72], state[74:76],
        state[86:88], state[90:92]
    ))

    return centers + edges


def edges_pattern_444(state):
    state = list('x' + state)
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

def centers_and_edges_separate_444(state):
    state = 'x' + state

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

    centers = ''.join((
        state[6:8],   state[10:12],
        state[22:24], state[26:28],
        state[38:40], state[42:44],
        state[54:56], state[58:60],
        state[70:72], state[74:76],
        state[86:88], state[90:92]
    ))

    return centers + edges


def centers_and_last_four_edges_pattern_444(state):
    state = list('x' + state)
    edges_recolor_444(state)
    state = ''.join(state)

    edges = ''.join((
        state[21],
        state[25],
        state[24],
        state[28],
        state[53],
        state[57],
        state[56],
        state[60]
    ))

    centers = ''.join((
        state[6:8],   state[10:12],
        state[22:24], state[26:28],
        state[38:40], state[42:44],
        state[54:56], state[58:60],
        state[70:72], state[74:76],
        state[86:88], state[90:92]
    ))

    return centers + edges


def last_four_edges_pattern_444(state):
    state = list('x' + state)
    edges_recolor_444(state)
    state = ''.join(state)

    edges = ''.join((
        state[21],
        state[25],
        state[24],
        state[28],
        state[53],
        state[57],
        state[56],
        state[60]
    ))

    return edges


def centers_and_edge_parity_444(state, steps):
    """
    4x4x4 centers-and-edge-parity
    """
    centers_state = centers_444(state)
    parity_even = True

    # Parity starts off as even on a solved cube, and when you do a quarter
    # turn of an inner slice, it switches from even to odd and odd to even.
    # That's literally all you need to keep track of.
    # --xyzzy
    for step in steps.split():
        if 'w' in step and step.endswith('2'):
            if parity_even:
                parity_even = False
            else:
                parity_even = True

    if parity_even:
        edge_parity = '0'
    else:
        edge_parity = '1'

    return centers_state + edge_parity


def all_xxx(state):
    return state


def centers_444(state):
    state = 'x' + state
    state = ''.join((state[6:8],   state[10:12],
                     state[22:24], state[26:28],
                     state[38:40], state[42:44],
                     state[54:56], state[58:60],
                     state[70:72], state[74:76],
                     state[86:88], state[90:92]))
    return state


def LFRB_centers_444(state):
    state = 'x' + state
    state = ''.join((state[22:24], state[26:28],
                     state[38:40], state[42:44],
                     state[54:56], state[58:60],
                     state[70:72], state[74:76]))
    return state


def UFBD_centers_444(state):
    state = 'x' + state
    state = ''.join((state[6:8],   state[10:12],
                     # state[22:24], state[26:28],
                     state[38:40], state[42:44],
                     #state[54:56], state[58:60],
                     state[70:72], state[74:76],
                     state[86:88], state[90:92]))
    return state


def centers_then_edges_444(state):
    return centers_444(state) + edges_444(state)


def centers_and_edges_444(state):
    state = 'x' + state
    state = ''.join((state[2:4],
                     state[5:13],
                     state[14:16],
                     state[18:20],
                     state[21:29],
                     state[30:32],
                     state[34:36],
                     state[37:45],
                     state[46:48],
                     state[50:52],
                     state[53:61],
                     state[62:64],
                     state[66:68],
                     state[69:77],
                     state[78:80],
                     state[82:84],
                     state[85:93],
                     state[94:96]))

    return state


def centers_555(state):
    state = 'x' + state
    state = ''.join((state[7:10],    state[12:15],   state[17:20],
                     state[32:35],   state[37:40],   state[42:45],
                     state[57:60],   state[62:65],   state[67:70],
                     state[82:85],   state[87:90],   state[92:95],
                     state[107:110], state[112:115], state[117:120],
                     state[132:135], state[137:140], state[142:145]))
    return state

def t_centers_555(state):
    state = 'x' + state
    state = ''.join((state[8], state[12], state[14], state[18],
                     state[33], state[37], state[39], state[43],
                     state[58], state[62], state[64], state[68],
                     state[83], state[87], state[89], state[93],
                     state[108], state[112], state[114], state[118],
                     state[133], state[137], state[139], state[143]))
    return state


def LR_t_centers_555(state):
    state = 'x' + state
    state = ''.join((state[33], state[37], state[39], state[43],
                     state[83], state[87], state[89], state[93]))
    return state


def x_centers_555(state):
    state = 'x' + state
    state = ''.join((state[7], state[9], state[17], state[19],
                     state[32], state[34], state[42], state[44],
                     state[57], state[59], state[67], state[69],
                     state[82], state[84], state[92], state[94],
                     state[107], state[109], state[117], state[119],
                     state[132], state[134], state[142], state[144]))
    return state



def UD_centers_555(state):
    state = 'x' + state
    state = ''.join((state[7:10],    state[12:15],   state[17:20],
                     state[132:135], state[137:140], state[142:145]))
    return state


def LFRB_centers_555(state):
    state = 'x' + state
    state = ''.join((state[32:35],   state[37:40],   state[42:45],
                     state[57:60],   state[62:65],   state[67:70],
                     state[82:85],   state[87:90],   state[92:95],
                     state[107:110], state[112:115], state[117:120]))
    return state


def LR_centers_555(state):
    state = 'x' + state
    state = ''.join((state[32:35],   state[37:40],   state[42:45],
                     state[82:85],   state[87:90],   state[92:95]))
    return state


def edges_555(state):
    state = 'x' + state
    state = ''.join((state[2:5]    , state[6]  , state[10:12]  , state[15:17]  , state[20] , state[22:25],
                     state[27:30]  , state[31] , state[35:37]  , state[40:42]  , state[45] , state[47:50],
                     state[52:55]  , state[56] , state[60:62]  , state[65:67]  , state[70] , state[72:75],
                     state[77:80]  , state[81] , state[85:87]  , state[90:92]  , state[95] , state[97:100],
                     state[102:105], state[106], state[110:112], state[115:117], state[120], state[122:125],
                     state[127:130], state[131], state[135:137], state[140:142], state[145], state[147:150]))
    return state


def edges_outside_555(state):
    state = 'x' + state
    state = ''.join((state[2], state[4], state[6], state[10], state[16], state[20], state[22], state[24],
                     state[27], state[29], state[31], state[35], state[41], state[45], state[47], state[49],
                     state[52], state[54], state[56], state[60], state[66], state[70], state[72], state[74],
                     state[77], state[79], state[81], state[85], state[91], state[95], state[97], state[99],
                     state[102], state[104], state[106], state[110], state[116], state[120], state[122], state[124],
                     state[127], state[129], state[131], state[135], state[141], state[145], state[147], state[149]))
    return state


def LR_centers_and_edges_outside_555(state):
    state = 'x' + state
    state = ''.join((
                     # Upper
                     state[2], state[4], state[6], state[10], state[16], state[20], state[22], state[24],

                     # Left
                     state[27], state[29],
                     state[31:36],
                     state[37:40],
                     state[41:46],
                     state[47], state[49],

                     # Front
                     state[52], state[54], state[56], state[60], state[66], state[70], state[72], state[74],

                     # Right
                     state[77], state[79],
                     state[81:86],
                     state[87:90],
                     state[91:96],
                     state[97], state[99],

                     # Back
                     state[102], state[104], state[106], state[110], state[116], state[120], state[122], state[124],

                     # Down
                     state[127], state[129], state[131], state[135], state[141], state[145], state[147], state[149]))
    return state


def centers_and_edges_555(state):
    state = 'x' + state
    state = ''.join((state[2:5],
                     state[6:21],
                     state[22:25],
                     state[27:30],
                     state[31:46],
                     state[47:50],
                     state[52:55],
                     state[56:71],
                     state[72:75],
                     state[77:80],
                     state[81:96],
                     state[97:100],
                     state[102:105],
                     state[106:121],
                     state[122:125],
                     state[127:130],
                     state[131:146],
                     state[147:150]))
    return state


# 12-23 are high edges, make these U (1)
# 0-11 are low edges, make these D (6)
# https://github.com/cs0x7f/TPR-4x4x4-Solver/blob/master/src/FullCube.java
high_edges_555 = ((14, 2, 104),  # upper
                  (13, 16, 29),
                  (15, 10, 79),
                  (12, 24, 54),
                  (21, 41, 120), # left
                  (20, 35, 56),
                  (23, 91, 70), # right
                  (22, 85, 106),
                  (18, 127, 72), # down
                  (17, 141, 47),
                  (19, 135, 97),
                  (16, 149, 122))

low_edges_555 = ((2, 4, 102),  # upper
                 (1, 6, 27),
                 (3, 20, 77),
                 (0, 22, 52),
                 (9, 31, 110), # left
                 (8, 45, 66),
                 (11, 60, 81), # right
                 (10, 95, 116),
                 (6, 74, 129), # down
                 (5, 49, 131),
                 (7, 145, 99),
                 (4, 147, 124))

def edges_high_low_recolor_555(state):
    """
    Look at all of the high edges and find the low edge for each.
    Return a cube state that represents where all the low edge siblings
    live in relation to their high edge counterpart.
    """

    #assert len(state) == 97, "Invalid state %s, len is %d" % (state, len(state))
    low_edge_map = {}

    for (low_edge_index, square_index, partner_index) in low_edges_555:
        square_value = state[square_index]
        partner_value = state[partner_index]
        #assert square_value != partner_value, "both squares are %s" % square_value
        wing_str = ''.join(sorted([square_value, partner_value]))

        if wing_str == 'xx':
            low_edge_index = 'x'
        else:
            low_edge_index = str(hex(low_edge_index))[2:]

        state[square_index] = low_edge_index
        state[partner_index] = low_edge_index

        #assert wing_str not in low_edge_map, "We have two %s wings, one at high_index %s %s and one at high_index %s (%d, %d), state %s" %\
        #    (wing_str,
        #     low_edge_map[wing_str],
        #     pformat(low_edges_555[int(low_edge_map[wing_str])]),
        #     low_edge_index,
        #     square_index, partner_index,
        #     ''.join(state[1:]))

        # save low_edge_index in hex and chop the leading 0x via [2:]
        low_edge_map[wing_str] = low_edge_index

    #assert len(low_edge_map.keys()) == 12, "Invalid low_edge_map\n%s\n" % pformat(low_edge_map)

    for (high_edge_index, square_index, partner_index) in high_edges_555:
        square_value = state[square_index]
        partner_value = state[partner_index]
        wing_str = ''.join(sorted([square_value, partner_value]))
        state[square_index] = low_edge_map[wing_str]
        state[partner_index] = low_edge_map[wing_str]
    return state


def edges_outside_high_low_pattern_555(state):
    state = list('x' + state)
    state = edges_high_low_recolor_555(state[:])
    state = ''.join(state)

    state = ''.join((state[2], state[16], state[10], state[24],
                     state[41], state[35],
                     state[91], state[85],
                     state[127], state[141], state[135], state[149]))

    return state


def centers_and_last_four_edges_pattern_555(state):
    state = list('x' + state)
    edges_recolor_555(state)
    state = ''.join(state)

    edges = ''.join((
        state[31],
        state[36],
        state[41],
        state[35],
        state[40],
        state[45],
        state[81],
        state[86],
        state[91],
        state[85],
        state[90],
        state[95]
    ))

    centers = ''.join((
        state[7:10],    state[12:15],   state[17:20],
        state[32:35],   state[37:40],   state[42:45],
        state[57:60],   state[62:65],   state[67:70],
        state[82:85],   state[87:90],   state[92:95],
        state[107:110], state[112:115], state[117:120],
        state[132:135], state[137:140], state[142:145]
    ))

    return centers + edges


tsai_phase2_orient_edges_555 = {
    (2, 104, 'B', 'D'): 'D',
    (2, 104, 'B', 'L'): 'D',
    (2, 104, 'B', 'R'): 'D',
    (2, 104, 'B', 'U'): 'D',
    (2, 104, 'D', 'B'): 'U',
    (2, 104, 'D', 'F'): 'U',
    (2, 104, 'D', 'L'): 'U',
    (2, 104, 'D', 'R'): 'U',
    (2, 104, 'F', 'D'): 'D',
    (2, 104, 'F', 'L'): 'D',
    (2, 104, 'F', 'R'): 'D',
    (2, 104, 'F', 'U'): 'D',
    (2, 104, 'L', 'B'): 'U',
    (2, 104, 'L', 'D'): 'D',
    (2, 104, 'L', 'F'): 'U',
    (2, 104, 'L', 'U'): 'D',
    (2, 104, 'R', 'B'): 'U',
    (2, 104, 'R', 'D'): 'D',
    (2, 104, 'R', 'F'): 'U',
    (2, 104, 'R', 'U'): 'D',
    (2, 104, 'U', 'B'): 'U',
    (2, 104, 'U', 'F'): 'U',
    (2, 104, 'U', 'L'): 'U',
    (2, 104, 'U', 'R'): 'U',
    (4, 102, 'B', 'D'): 'U',
    (4, 102, 'B', 'L'): 'U',
    (4, 102, 'B', 'R'): 'U',
    (4, 102, 'B', 'U'): 'U',
    (4, 102, 'D', 'B'): 'D',
    (4, 102, 'D', 'F'): 'D',
    (4, 102, 'D', 'L'): 'D',
    (4, 102, 'D', 'R'): 'D',
    (4, 102, 'F', 'D'): 'U',
    (4, 102, 'F', 'L'): 'U',
    (4, 102, 'F', 'R'): 'U',
    (4, 102, 'F', 'U'): 'U',
    (4, 102, 'L', 'B'): 'D',
    (4, 102, 'L', 'D'): 'U',
    (4, 102, 'L', 'F'): 'D',
    (4, 102, 'L', 'U'): 'U',
    (4, 102, 'R', 'B'): 'D',
    (4, 102, 'R', 'D'): 'U',
    (4, 102, 'R', 'F'): 'D',
    (4, 102, 'R', 'U'): 'U',
    (4, 102, 'U', 'B'): 'D',
    (4, 102, 'U', 'F'): 'D',
    (4, 102, 'U', 'L'): 'D',
    (4, 102, 'U', 'R'): 'D',
    (6, 27, 'B', 'D'): 'U',
    (6, 27, 'B', 'L'): 'U',
    (6, 27, 'B', 'R'): 'U',
    (6, 27, 'B', 'U'): 'U',
    (6, 27, 'D', 'B'): 'D',
    (6, 27, 'D', 'F'): 'D',
    (6, 27, 'D', 'L'): 'D',
    (6, 27, 'D', 'R'): 'D',
    (6, 27, 'F', 'D'): 'U',
    (6, 27, 'F', 'L'): 'U',
    (6, 27, 'F', 'R'): 'U',
    (6, 27, 'F', 'U'): 'U',
    (6, 27, 'L', 'B'): 'D',
    (6, 27, 'L', 'D'): 'U',
    (6, 27, 'L', 'F'): 'D',
    (6, 27, 'L', 'U'): 'U',
    (6, 27, 'R', 'B'): 'D',
    (6, 27, 'R', 'D'): 'U',
    (6, 27, 'R', 'F'): 'D',
    (6, 27, 'R', 'U'): 'U',
    (6, 27, 'U', 'B'): 'D',
    (6, 27, 'U', 'F'): 'D',
    (6, 27, 'U', 'L'): 'D',
    (6, 27, 'U', 'R'): 'D',
    (10, 79, 'B', 'D'): 'D',
    (10, 79, 'B', 'L'): 'D',
    (10, 79, 'B', 'R'): 'D',
    (10, 79, 'B', 'U'): 'D',
    (10, 79, 'D', 'B'): 'U',
    (10, 79, 'D', 'F'): 'U',
    (10, 79, 'D', 'L'): 'U',
    (10, 79, 'D', 'R'): 'U',
    (10, 79, 'F', 'D'): 'D',
    (10, 79, 'F', 'L'): 'D',
    (10, 79, 'F', 'R'): 'D',
    (10, 79, 'F', 'U'): 'D',
    (10, 79, 'L', 'B'): 'U',
    (10, 79, 'L', 'D'): 'D',
    (10, 79, 'L', 'F'): 'U',
    (10, 79, 'L', 'U'): 'D',
    (10, 79, 'R', 'B'): 'U',
    (10, 79, 'R', 'D'): 'D',
    (10, 79, 'R', 'F'): 'U',
    (10, 79, 'R', 'U'): 'D',
    (10, 79, 'U', 'B'): 'U',
    (10, 79, 'U', 'F'): 'U',
    (10, 79, 'U', 'L'): 'U',
    (10, 79, 'U', 'R'): 'U',
    (16, 29, 'B', 'D'): 'D',
    (16, 29, 'B', 'L'): 'D',
    (16, 29, 'B', 'R'): 'D',
    (16, 29, 'B', 'U'): 'D',
    (16, 29, 'D', 'B'): 'U',
    (16, 29, 'D', 'F'): 'U',
    (16, 29, 'D', 'L'): 'U',
    (16, 29, 'D', 'R'): 'U',
    (16, 29, 'F', 'D'): 'D',
    (16, 29, 'F', 'L'): 'D',
    (16, 29, 'F', 'R'): 'D',
    (16, 29, 'F', 'U'): 'D',
    (16, 29, 'L', 'B'): 'U',
    (16, 29, 'L', 'D'): 'D',
    (16, 29, 'L', 'F'): 'U',
    (16, 29, 'L', 'U'): 'D',
    (16, 29, 'R', 'B'): 'U',
    (16, 29, 'R', 'D'): 'D',
    (16, 29, 'R', 'F'): 'U',
    (16, 29, 'R', 'U'): 'D',
    (16, 29, 'U', 'B'): 'U',
    (16, 29, 'U', 'F'): 'U',
    (16, 29, 'U', 'L'): 'U',
    (16, 29, 'U', 'R'): 'U',
    (20, 77, 'B', 'D'): 'U',
    (20, 77, 'B', 'L'): 'U',
    (20, 77, 'B', 'R'): 'U',
    (20, 77, 'B', 'U'): 'U',
    (20, 77, 'D', 'B'): 'D',
    (20, 77, 'D', 'F'): 'D',
    (20, 77, 'D', 'L'): 'D',
    (20, 77, 'D', 'R'): 'D',
    (20, 77, 'F', 'D'): 'U',
    (20, 77, 'F', 'L'): 'U',
    (20, 77, 'F', 'R'): 'U',
    (20, 77, 'F', 'U'): 'U',
    (20, 77, 'L', 'B'): 'D',
    (20, 77, 'L', 'D'): 'U',
    (20, 77, 'L', 'F'): 'D',
    (20, 77, 'L', 'U'): 'U',
    (20, 77, 'R', 'B'): 'D',
    (20, 77, 'R', 'D'): 'U',
    (20, 77, 'R', 'F'): 'D',
    (20, 77, 'R', 'U'): 'U',
    (20, 77, 'U', 'B'): 'D',
    (20, 77, 'U', 'F'): 'D',
    (20, 77, 'U', 'L'): 'D',
    (20, 77, 'U', 'R'): 'D',
    (22, 52, 'B', 'D'): 'U',
    (22, 52, 'B', 'L'): 'U',
    (22, 52, 'B', 'R'): 'U',
    (22, 52, 'B', 'U'): 'U',
    (22, 52, 'D', 'B'): 'D',
    (22, 52, 'D', 'F'): 'D',
    (22, 52, 'D', 'L'): 'D',
    (22, 52, 'D', 'R'): 'D',
    (22, 52, 'F', 'D'): 'U',
    (22, 52, 'F', 'L'): 'U',
    (22, 52, 'F', 'R'): 'U',
    (22, 52, 'F', 'U'): 'U',
    (22, 52, 'L', 'B'): 'D',
    (22, 52, 'L', 'D'): 'U',
    (22, 52, 'L', 'F'): 'D',
    (22, 52, 'L', 'U'): 'U',
    (22, 52, 'R', 'B'): 'D',
    (22, 52, 'R', 'D'): 'U',
    (22, 52, 'R', 'F'): 'D',
    (22, 52, 'R', 'U'): 'U',
    (22, 52, 'U', 'B'): 'D',
    (22, 52, 'U', 'F'): 'D',
    (22, 52, 'U', 'L'): 'D',
    (22, 52, 'U', 'R'): 'D',
    (24, 54, 'B', 'D'): 'D',
    (24, 54, 'B', 'L'): 'D',
    (24, 54, 'B', 'R'): 'D',
    (24, 54, 'B', 'U'): 'D',
    (24, 54, 'D', 'B'): 'U',
    (24, 54, 'D', 'F'): 'U',
    (24, 54, 'D', 'L'): 'U',
    (24, 54, 'D', 'R'): 'U',
    (24, 54, 'F', 'D'): 'D',
    (24, 54, 'F', 'L'): 'D',
    (24, 54, 'F', 'R'): 'D',
    (24, 54, 'F', 'U'): 'D',
    (24, 54, 'L', 'B'): 'U',
    (24, 54, 'L', 'D'): 'D',
    (24, 54, 'L', 'F'): 'U',
    (24, 54, 'L', 'U'): 'D',
    (24, 54, 'R', 'B'): 'U',
    (24, 54, 'R', 'D'): 'D',
    (24, 54, 'R', 'F'): 'U',
    (24, 54, 'R', 'U'): 'D',
    (24, 54, 'U', 'B'): 'U',
    (24, 54, 'U', 'F'): 'U',
    (24, 54, 'U', 'L'): 'U',
    (24, 54, 'U', 'R'): 'U',
    (27, 6, 'B', 'D'): 'D',
    (27, 6, 'B', 'L'): 'D',
    (27, 6, 'B', 'R'): 'D',
    (27, 6, 'B', 'U'): 'D',
    (27, 6, 'D', 'B'): 'U',
    (27, 6, 'D', 'F'): 'U',
    (27, 6, 'D', 'L'): 'U',
    (27, 6, 'D', 'R'): 'U',
    (27, 6, 'F', 'D'): 'D',
    (27, 6, 'F', 'L'): 'D',
    (27, 6, 'F', 'R'): 'D',
    (27, 6, 'F', 'U'): 'D',
    (27, 6, 'L', 'B'): 'U',
    (27, 6, 'L', 'D'): 'D',
    (27, 6, 'L', 'F'): 'U',
    (27, 6, 'L', 'U'): 'D',
    (27, 6, 'R', 'B'): 'U',
    (27, 6, 'R', 'D'): 'D',
    (27, 6, 'R', 'F'): 'U',
    (27, 6, 'R', 'U'): 'D',
    (27, 6, 'U', 'B'): 'U',
    (27, 6, 'U', 'F'): 'U',
    (27, 6, 'U', 'L'): 'U',
    (27, 6, 'U', 'R'): 'U',
    (29, 16, 'B', 'D'): 'U',
    (29, 16, 'B', 'L'): 'U',
    (29, 16, 'B', 'R'): 'U',
    (29, 16, 'B', 'U'): 'U',
    (29, 16, 'D', 'B'): 'D',
    (29, 16, 'D', 'F'): 'D',
    (29, 16, 'D', 'L'): 'D',
    (29, 16, 'D', 'R'): 'D',
    (29, 16, 'F', 'D'): 'U',
    (29, 16, 'F', 'L'): 'U',
    (29, 16, 'F', 'R'): 'U',
    (29, 16, 'F', 'U'): 'U',
    (29, 16, 'L', 'B'): 'D',
    (29, 16, 'L', 'D'): 'U',
    (29, 16, 'L', 'F'): 'D',
    (29, 16, 'L', 'U'): 'U',
    (29, 16, 'R', 'B'): 'D',
    (29, 16, 'R', 'D'): 'U',
    (29, 16, 'R', 'F'): 'D',
    (29, 16, 'R', 'U'): 'U',
    (29, 16, 'U', 'B'): 'D',
    (29, 16, 'U', 'F'): 'D',
    (29, 16, 'U', 'L'): 'D',
    (29, 16, 'U', 'R'): 'D',
    (31, 110, 'B', 'D'): 'U',
    (31, 110, 'B', 'L'): 'U',
    (31, 110, 'B', 'R'): 'U',
    (31, 110, 'B', 'U'): 'U',
    (31, 110, 'D', 'B'): 'D',
    (31, 110, 'D', 'F'): 'D',
    (31, 110, 'D', 'L'): 'D',
    (31, 110, 'D', 'R'): 'D',
    (31, 110, 'F', 'D'): 'U',
    (31, 110, 'F', 'L'): 'U',
    (31, 110, 'F', 'R'): 'U',
    (31, 110, 'F', 'U'): 'U',
    (31, 110, 'L', 'B'): 'D',
    (31, 110, 'L', 'D'): 'U',
    (31, 110, 'L', 'F'): 'D',
    (31, 110, 'L', 'U'): 'U',
    (31, 110, 'R', 'B'): 'D',
    (31, 110, 'R', 'D'): 'U',
    (31, 110, 'R', 'F'): 'D',
    (31, 110, 'R', 'U'): 'U',
    (31, 110, 'U', 'B'): 'D',
    (31, 110, 'U', 'F'): 'D',
    (31, 110, 'U', 'L'): 'D',
    (31, 110, 'U', 'R'): 'D',
    (35, 56, 'B', 'D'): 'D',
    (35, 56, 'B', 'L'): 'D',
    (35, 56, 'B', 'R'): 'D',
    (35, 56, 'B', 'U'): 'D',
    (35, 56, 'D', 'B'): 'U',
    (35, 56, 'D', 'F'): 'U',
    (35, 56, 'D', 'L'): 'U',
    (35, 56, 'D', 'R'): 'U',
    (35, 56, 'F', 'D'): 'D',
    (35, 56, 'F', 'L'): 'D',
    (35, 56, 'F', 'R'): 'D',
    (35, 56, 'F', 'U'): 'D',
    (35, 56, 'L', 'B'): 'U',
    (35, 56, 'L', 'D'): 'D',
    (35, 56, 'L', 'F'): 'U',
    (35, 56, 'L', 'U'): 'D',
    (35, 56, 'R', 'B'): 'U',
    (35, 56, 'R', 'D'): 'D',
    (35, 56, 'R', 'F'): 'U',
    (35, 56, 'R', 'U'): 'D',
    (35, 56, 'U', 'B'): 'U',
    (35, 56, 'U', 'F'): 'U',
    (35, 56, 'U', 'L'): 'U',
    (35, 56, 'U', 'R'): 'U',
    (41, 120, 'B', 'D'): 'D',
    (41, 120, 'B', 'L'): 'D',
    (41, 120, 'B', 'R'): 'D',
    (41, 120, 'B', 'U'): 'D',
    (41, 120, 'D', 'B'): 'U',
    (41, 120, 'D', 'F'): 'U',
    (41, 120, 'D', 'L'): 'U',
    (41, 120, 'D', 'R'): 'U',
    (41, 120, 'F', 'D'): 'D',
    (41, 120, 'F', 'L'): 'D',
    (41, 120, 'F', 'R'): 'D',
    (41, 120, 'F', 'U'): 'D',
    (41, 120, 'L', 'B'): 'U',
    (41, 120, 'L', 'D'): 'D',
    (41, 120, 'L', 'F'): 'U',
    (41, 120, 'L', 'U'): 'D',
    (41, 120, 'R', 'B'): 'U',
    (41, 120, 'R', 'D'): 'D',
    (41, 120, 'R', 'F'): 'U',
    (41, 120, 'R', 'U'): 'D',
    (41, 120, 'U', 'B'): 'U',
    (41, 120, 'U', 'F'): 'U',
    (41, 120, 'U', 'L'): 'U',
    (41, 120, 'U', 'R'): 'U',
    (45, 66, 'B', 'D'): 'U',
    (45, 66, 'B', 'L'): 'U',
    (45, 66, 'B', 'R'): 'U',
    (45, 66, 'B', 'U'): 'U',
    (45, 66, 'D', 'B'): 'D',
    (45, 66, 'D', 'F'): 'D',
    (45, 66, 'D', 'L'): 'D',
    (45, 66, 'D', 'R'): 'D',
    (45, 66, 'F', 'D'): 'U',
    (45, 66, 'F', 'L'): 'U',
    (45, 66, 'F', 'R'): 'U',
    (45, 66, 'F', 'U'): 'U',
    (45, 66, 'L', 'B'): 'D',
    (45, 66, 'L', 'D'): 'U',
    (45, 66, 'L', 'F'): 'D',
    (45, 66, 'L', 'U'): 'U',
    (45, 66, 'R', 'B'): 'D',
    (45, 66, 'R', 'D'): 'U',
    (45, 66, 'R', 'F'): 'D',
    (45, 66, 'R', 'U'): 'U',
    (45, 66, 'U', 'B'): 'D',
    (45, 66, 'U', 'F'): 'D',
    (45, 66, 'U', 'L'): 'D',
    (45, 66, 'U', 'R'): 'D',
    (47, 141, 'B', 'D'): 'U',
    (47, 141, 'B', 'L'): 'U',
    (47, 141, 'B', 'R'): 'U',
    (47, 141, 'B', 'U'): 'U',
    (47, 141, 'D', 'B'): 'D',
    (47, 141, 'D', 'F'): 'D',
    (47, 141, 'D', 'L'): 'D',
    (47, 141, 'D', 'R'): 'D',
    (47, 141, 'F', 'D'): 'U',
    (47, 141, 'F', 'L'): 'U',
    (47, 141, 'F', 'R'): 'U',
    (47, 141, 'F', 'U'): 'U',
    (47, 141, 'L', 'B'): 'D',
    (47, 141, 'L', 'D'): 'U',
    (47, 141, 'L', 'F'): 'D',
    (47, 141, 'L', 'U'): 'U',
    (47, 141, 'R', 'B'): 'D',
    (47, 141, 'R', 'D'): 'U',
    (47, 141, 'R', 'F'): 'D',
    (47, 141, 'R', 'U'): 'U',
    (47, 141, 'U', 'B'): 'D',
    (47, 141, 'U', 'F'): 'D',
    (47, 141, 'U', 'L'): 'D',
    (47, 141, 'U', 'R'): 'D',
    (49, 131, 'B', 'D'): 'D',
    (49, 131, 'B', 'L'): 'D',
    (49, 131, 'B', 'R'): 'D',
    (49, 131, 'B', 'U'): 'D',
    (49, 131, 'D', 'B'): 'U',
    (49, 131, 'D', 'F'): 'U',
    (49, 131, 'D', 'L'): 'U',
    (49, 131, 'D', 'R'): 'U',
    (49, 131, 'F', 'D'): 'D',
    (49, 131, 'F', 'L'): 'D',
    (49, 131, 'F', 'R'): 'D',
    (49, 131, 'F', 'U'): 'D',
    (49, 131, 'L', 'B'): 'U',
    (49, 131, 'L', 'D'): 'D',
    (49, 131, 'L', 'F'): 'U',
    (49, 131, 'L', 'U'): 'D',
    (49, 131, 'R', 'B'): 'U',
    (49, 131, 'R', 'D'): 'D',
    (49, 131, 'R', 'F'): 'U',
    (49, 131, 'R', 'U'): 'D',
    (49, 131, 'U', 'B'): 'U',
    (49, 131, 'U', 'F'): 'U',
    (49, 131, 'U', 'L'): 'U',
    (49, 131, 'U', 'R'): 'U',
    (52, 22, 'B', 'D'): 'D',
    (52, 22, 'B', 'L'): 'D',
    (52, 22, 'B', 'R'): 'D',
    (52, 22, 'B', 'U'): 'D',
    (52, 22, 'D', 'B'): 'U',
    (52, 22, 'D', 'F'): 'U',
    (52, 22, 'D', 'L'): 'U',
    (52, 22, 'D', 'R'): 'U',
    (52, 22, 'F', 'D'): 'D',
    (52, 22, 'F', 'L'): 'D',
    (52, 22, 'F', 'R'): 'D',
    (52, 22, 'F', 'U'): 'D',
    (52, 22, 'L', 'B'): 'U',
    (52, 22, 'L', 'D'): 'D',
    (52, 22, 'L', 'F'): 'U',
    (52, 22, 'L', 'U'): 'D',
    (52, 22, 'R', 'B'): 'U',
    (52, 22, 'R', 'D'): 'D',
    (52, 22, 'R', 'F'): 'U',
    (52, 22, 'R', 'U'): 'D',
    (52, 22, 'U', 'B'): 'U',
    (52, 22, 'U', 'F'): 'U',
    (52, 22, 'U', 'L'): 'U',
    (52, 22, 'U', 'R'): 'U',
    (54, 24, 'B', 'D'): 'U',
    (54, 24, 'B', 'L'): 'U',
    (54, 24, 'B', 'R'): 'U',
    (54, 24, 'B', 'U'): 'U',
    (54, 24, 'D', 'B'): 'D',
    (54, 24, 'D', 'F'): 'D',
    (54, 24, 'D', 'L'): 'D',
    (54, 24, 'D', 'R'): 'D',
    (54, 24, 'F', 'D'): 'U',
    (54, 24, 'F', 'L'): 'U',
    (54, 24, 'F', 'R'): 'U',
    (54, 24, 'F', 'U'): 'U',
    (54, 24, 'L', 'B'): 'D',
    (54, 24, 'L', 'D'): 'U',
    (54, 24, 'L', 'F'): 'D',
    (54, 24, 'L', 'U'): 'U',
    (54, 24, 'R', 'B'): 'D',
    (54, 24, 'R', 'D'): 'U',
    (54, 24, 'R', 'F'): 'D',
    (54, 24, 'R', 'U'): 'U',
    (54, 24, 'U', 'B'): 'D',
    (54, 24, 'U', 'F'): 'D',
    (54, 24, 'U', 'L'): 'D',
    (54, 24, 'U', 'R'): 'D',
    (56, 35, 'B', 'D'): 'U',
    (56, 35, 'B', 'L'): 'U',
    (56, 35, 'B', 'R'): 'U',
    (56, 35, 'B', 'U'): 'U',
    (56, 35, 'D', 'B'): 'D',
    (56, 35, 'D', 'F'): 'D',
    (56, 35, 'D', 'L'): 'D',
    (56, 35, 'D', 'R'): 'D',
    (56, 35, 'F', 'D'): 'U',
    (56, 35, 'F', 'L'): 'U',
    (56, 35, 'F', 'R'): 'U',
    (56, 35, 'F', 'U'): 'U',
    (56, 35, 'L', 'B'): 'D',
    (56, 35, 'L', 'D'): 'U',
    (56, 35, 'L', 'F'): 'D',
    (56, 35, 'L', 'U'): 'U',
    (56, 35, 'R', 'B'): 'D',
    (56, 35, 'R', 'D'): 'U',
    (56, 35, 'R', 'F'): 'D',
    (56, 35, 'R', 'U'): 'U',
    (56, 35, 'U', 'B'): 'D',
    (56, 35, 'U', 'F'): 'D',
    (56, 35, 'U', 'L'): 'D',
    (56, 35, 'U', 'R'): 'D',
    (60, 81, 'B', 'D'): 'D',
    (60, 81, 'B', 'L'): 'D',
    (60, 81, 'B', 'R'): 'D',
    (60, 81, 'B', 'U'): 'D',
    (60, 81, 'D', 'B'): 'U',
    (60, 81, 'D', 'F'): 'U',
    (60, 81, 'D', 'L'): 'U',
    (60, 81, 'D', 'R'): 'U',
    (60, 81, 'F', 'D'): 'D',
    (60, 81, 'F', 'L'): 'D',
    (60, 81, 'F', 'R'): 'D',
    (60, 81, 'F', 'U'): 'D',
    (60, 81, 'L', 'B'): 'U',
    (60, 81, 'L', 'D'): 'D',
    (60, 81, 'L', 'F'): 'U',
    (60, 81, 'L', 'U'): 'D',
    (60, 81, 'R', 'B'): 'U',
    (60, 81, 'R', 'D'): 'D',
    (60, 81, 'R', 'F'): 'U',
    (60, 81, 'R', 'U'): 'D',
    (60, 81, 'U', 'B'): 'U',
    (60, 81, 'U', 'F'): 'U',
    (60, 81, 'U', 'L'): 'U',
    (60, 81, 'U', 'R'): 'U',
    (66, 45, 'B', 'D'): 'D',
    (66, 45, 'B', 'L'): 'D',
    (66, 45, 'B', 'R'): 'D',
    (66, 45, 'B', 'U'): 'D',
    (66, 45, 'D', 'B'): 'U',
    (66, 45, 'D', 'F'): 'U',
    (66, 45, 'D', 'L'): 'U',
    (66, 45, 'D', 'R'): 'U',
    (66, 45, 'F', 'D'): 'D',
    (66, 45, 'F', 'L'): 'D',
    (66, 45, 'F', 'R'): 'D',
    (66, 45, 'F', 'U'): 'D',
    (66, 45, 'L', 'B'): 'U',
    (66, 45, 'L', 'D'): 'D',
    (66, 45, 'L', 'F'): 'U',
    (66, 45, 'L', 'U'): 'D',
    (66, 45, 'R', 'B'): 'U',
    (66, 45, 'R', 'D'): 'D',
    (66, 45, 'R', 'F'): 'U',
    (66, 45, 'R', 'U'): 'D',
    (66, 45, 'U', 'B'): 'U',
    (66, 45, 'U', 'F'): 'U',
    (66, 45, 'U', 'L'): 'U',
    (66, 45, 'U', 'R'): 'U',
    (70, 91, 'B', 'D'): 'U',
    (70, 91, 'B', 'L'): 'U',
    (70, 91, 'B', 'R'): 'U',
    (70, 91, 'B', 'U'): 'U',
    (70, 91, 'D', 'B'): 'D',
    (70, 91, 'D', 'F'): 'D',
    (70, 91, 'D', 'L'): 'D',
    (70, 91, 'D', 'R'): 'D',
    (70, 91, 'F', 'D'): 'U',
    (70, 91, 'F', 'L'): 'U',
    (70, 91, 'F', 'R'): 'U',
    (70, 91, 'F', 'U'): 'U',
    (70, 91, 'L', 'B'): 'D',
    (70, 91, 'L', 'D'): 'U',
    (70, 91, 'L', 'F'): 'D',
    (70, 91, 'L', 'U'): 'U',
    (70, 91, 'R', 'B'): 'D',
    (70, 91, 'R', 'D'): 'U',
    (70, 91, 'R', 'F'): 'D',
    (70, 91, 'R', 'U'): 'U',
    (70, 91, 'U', 'B'): 'D',
    (70, 91, 'U', 'F'): 'D',
    (70, 91, 'U', 'L'): 'D',
    (70, 91, 'U', 'R'): 'D',
    (72, 127, 'B', 'D'): 'U',
    (72, 127, 'B', 'L'): 'U',
    (72, 127, 'B', 'R'): 'U',
    (72, 127, 'B', 'U'): 'U',
    (72, 127, 'D', 'B'): 'D',
    (72, 127, 'D', 'F'): 'D',
    (72, 127, 'D', 'L'): 'D',
    (72, 127, 'D', 'R'): 'D',
    (72, 127, 'F', 'D'): 'U',
    (72, 127, 'F', 'L'): 'U',
    (72, 127, 'F', 'R'): 'U',
    (72, 127, 'F', 'U'): 'U',
    (72, 127, 'L', 'B'): 'D',
    (72, 127, 'L', 'D'): 'U',
    (72, 127, 'L', 'F'): 'D',
    (72, 127, 'L', 'U'): 'U',
    (72, 127, 'R', 'B'): 'D',
    (72, 127, 'R', 'D'): 'U',
    (72, 127, 'R', 'F'): 'D',
    (72, 127, 'R', 'U'): 'U',
    (72, 127, 'U', 'B'): 'D',
    (72, 127, 'U', 'F'): 'D',
    (72, 127, 'U', 'L'): 'D',
    (72, 127, 'U', 'R'): 'D',
    (74, 129, 'B', 'D'): 'D',
    (74, 129, 'B', 'L'): 'D',
    (74, 129, 'B', 'R'): 'D',
    (74, 129, 'B', 'U'): 'D',
    (74, 129, 'D', 'B'): 'U',
    (74, 129, 'D', 'F'): 'U',
    (74, 129, 'D', 'L'): 'U',
    (74, 129, 'D', 'R'): 'U',
    (74, 129, 'F', 'D'): 'D',
    (74, 129, 'F', 'L'): 'D',
    (74, 129, 'F', 'R'): 'D',
    (74, 129, 'F', 'U'): 'D',
    (74, 129, 'L', 'B'): 'U',
    (74, 129, 'L', 'D'): 'D',
    (74, 129, 'L', 'F'): 'U',
    (74, 129, 'L', 'U'): 'D',
    (74, 129, 'R', 'B'): 'U',
    (74, 129, 'R', 'D'): 'D',
    (74, 129, 'R', 'F'): 'U',
    (74, 129, 'R', 'U'): 'D',
    (74, 129, 'U', 'B'): 'U',
    (74, 129, 'U', 'F'): 'U',
    (74, 129, 'U', 'L'): 'U',
    (74, 129, 'U', 'R'): 'U',
    (77, 20, 'B', 'D'): 'D',
    (77, 20, 'B', 'L'): 'D',
    (77, 20, 'B', 'R'): 'D',
    (77, 20, 'B', 'U'): 'D',
    (77, 20, 'D', 'B'): 'U',
    (77, 20, 'D', 'F'): 'U',
    (77, 20, 'D', 'L'): 'U',
    (77, 20, 'D', 'R'): 'U',
    (77, 20, 'F', 'D'): 'D',
    (77, 20, 'F', 'L'): 'D',
    (77, 20, 'F', 'R'): 'D',
    (77, 20, 'F', 'U'): 'D',
    (77, 20, 'L', 'B'): 'U',
    (77, 20, 'L', 'D'): 'D',
    (77, 20, 'L', 'F'): 'U',
    (77, 20, 'L', 'U'): 'D',
    (77, 20, 'R', 'B'): 'U',
    (77, 20, 'R', 'D'): 'D',
    (77, 20, 'R', 'F'): 'U',
    (77, 20, 'R', 'U'): 'D',
    (77, 20, 'U', 'B'): 'U',
    (77, 20, 'U', 'F'): 'U',
    (77, 20, 'U', 'L'): 'U',
    (77, 20, 'U', 'R'): 'U',
    (79, 10, 'B', 'D'): 'U',
    (79, 10, 'B', 'L'): 'U',
    (79, 10, 'B', 'R'): 'U',
    (79, 10, 'B', 'U'): 'U',
    (79, 10, 'D', 'B'): 'D',
    (79, 10, 'D', 'F'): 'D',
    (79, 10, 'D', 'L'): 'D',
    (79, 10, 'D', 'R'): 'D',
    (79, 10, 'F', 'D'): 'U',
    (79, 10, 'F', 'L'): 'U',
    (79, 10, 'F', 'R'): 'U',
    (79, 10, 'F', 'U'): 'U',
    (79, 10, 'L', 'B'): 'D',
    (79, 10, 'L', 'D'): 'U',
    (79, 10, 'L', 'F'): 'D',
    (79, 10, 'L', 'U'): 'U',
    (79, 10, 'R', 'B'): 'D',
    (79, 10, 'R', 'D'): 'U',
    (79, 10, 'R', 'F'): 'D',
    (79, 10, 'R', 'U'): 'U',
    (79, 10, 'U', 'B'): 'D',
    (79, 10, 'U', 'F'): 'D',
    (79, 10, 'U', 'L'): 'D',
    (79, 10, 'U', 'R'): 'D',
    (81, 60, 'B', 'D'): 'U',
    (81, 60, 'B', 'L'): 'U',
    (81, 60, 'B', 'R'): 'U',
    (81, 60, 'B', 'U'): 'U',
    (81, 60, 'D', 'B'): 'D',
    (81, 60, 'D', 'F'): 'D',
    (81, 60, 'D', 'L'): 'D',
    (81, 60, 'D', 'R'): 'D',
    (81, 60, 'F', 'D'): 'U',
    (81, 60, 'F', 'L'): 'U',
    (81, 60, 'F', 'R'): 'U',
    (81, 60, 'F', 'U'): 'U',
    (81, 60, 'L', 'B'): 'D',
    (81, 60, 'L', 'D'): 'U',
    (81, 60, 'L', 'F'): 'D',
    (81, 60, 'L', 'U'): 'U',
    (81, 60, 'R', 'B'): 'D',
    (81, 60, 'R', 'D'): 'U',
    (81, 60, 'R', 'F'): 'D',
    (81, 60, 'R', 'U'): 'U',
    (81, 60, 'U', 'B'): 'D',
    (81, 60, 'U', 'F'): 'D',
    (81, 60, 'U', 'L'): 'D',
    (81, 60, 'U', 'R'): 'D',
    (85, 106, 'B', 'D'): 'D',
    (85, 106, 'B', 'L'): 'D',
    (85, 106, 'B', 'R'): 'D',
    (85, 106, 'B', 'U'): 'D',
    (85, 106, 'D', 'B'): 'U',
    (85, 106, 'D', 'F'): 'U',
    (85, 106, 'D', 'L'): 'U',
    (85, 106, 'D', 'R'): 'U',
    (85, 106, 'F', 'D'): 'D',
    (85, 106, 'F', 'L'): 'D',
    (85, 106, 'F', 'R'): 'D',
    (85, 106, 'F', 'U'): 'D',
    (85, 106, 'L', 'B'): 'U',
    (85, 106, 'L', 'D'): 'D',
    (85, 106, 'L', 'F'): 'U',
    (85, 106, 'L', 'U'): 'D',
    (85, 106, 'R', 'B'): 'U',
    (85, 106, 'R', 'D'): 'D',
    (85, 106, 'R', 'F'): 'U',
    (85, 106, 'R', 'U'): 'D',
    (85, 106, 'U', 'B'): 'U',
    (85, 106, 'U', 'F'): 'U',
    (85, 106, 'U', 'L'): 'U',
    (85, 106, 'U', 'R'): 'U',
    (91, 70, 'B', 'D'): 'D',
    (91, 70, 'B', 'L'): 'D',
    (91, 70, 'B', 'R'): 'D',
    (91, 70, 'B', 'U'): 'D',
    (91, 70, 'D', 'B'): 'U',
    (91, 70, 'D', 'F'): 'U',
    (91, 70, 'D', 'L'): 'U',
    (91, 70, 'D', 'R'): 'U',
    (91, 70, 'F', 'D'): 'D',
    (91, 70, 'F', 'L'): 'D',
    (91, 70, 'F', 'R'): 'D',
    (91, 70, 'F', 'U'): 'D',
    (91, 70, 'L', 'B'): 'U',
    (91, 70, 'L', 'D'): 'D',
    (91, 70, 'L', 'F'): 'U',
    (91, 70, 'L', 'U'): 'D',
    (91, 70, 'R', 'B'): 'U',
    (91, 70, 'R', 'D'): 'D',
    (91, 70, 'R', 'F'): 'U',
    (91, 70, 'R', 'U'): 'D',
    (91, 70, 'U', 'B'): 'U',
    (91, 70, 'U', 'F'): 'U',
    (91, 70, 'U', 'L'): 'U',
    (91, 70, 'U', 'R'): 'U',
    (95, 116, 'B', 'D'): 'U',
    (95, 116, 'B', 'L'): 'U',
    (95, 116, 'B', 'R'): 'U',
    (95, 116, 'B', 'U'): 'U',
    (95, 116, 'D', 'B'): 'D',
    (95, 116, 'D', 'F'): 'D',
    (95, 116, 'D', 'L'): 'D',
    (95, 116, 'D', 'R'): 'D',
    (95, 116, 'F', 'D'): 'U',
    (95, 116, 'F', 'L'): 'U',
    (95, 116, 'F', 'R'): 'U',
    (95, 116, 'F', 'U'): 'U',
    (95, 116, 'L', 'B'): 'D',
    (95, 116, 'L', 'D'): 'U',
    (95, 116, 'L', 'F'): 'D',
    (95, 116, 'L', 'U'): 'U',
    (95, 116, 'R', 'B'): 'D',
    (95, 116, 'R', 'D'): 'U',
    (95, 116, 'R', 'F'): 'D',
    (95, 116, 'R', 'U'): 'U',
    (95, 116, 'U', 'B'): 'D',
    (95, 116, 'U', 'F'): 'D',
    (95, 116, 'U', 'L'): 'D',
    (95, 116, 'U', 'R'): 'D',
    (97, 135, 'B', 'D'): 'U',
    (97, 135, 'B', 'L'): 'U',
    (97, 135, 'B', 'R'): 'U',
    (97, 135, 'B', 'U'): 'U',
    (97, 135, 'D', 'B'): 'D',
    (97, 135, 'D', 'F'): 'D',
    (97, 135, 'D', 'L'): 'D',
    (97, 135, 'D', 'R'): 'D',
    (97, 135, 'F', 'D'): 'U',
    (97, 135, 'F', 'L'): 'U',
    (97, 135, 'F', 'R'): 'U',
    (97, 135, 'F', 'U'): 'U',
    (97, 135, 'L', 'B'): 'D',
    (97, 135, 'L', 'D'): 'U',
    (97, 135, 'L', 'F'): 'D',
    (97, 135, 'L', 'U'): 'U',
    (97, 135, 'R', 'B'): 'D',
    (97, 135, 'R', 'D'): 'U',
    (97, 135, 'R', 'F'): 'D',
    (97, 135, 'R', 'U'): 'U',
    (97, 135, 'U', 'B'): 'D',
    (97, 135, 'U', 'F'): 'D',
    (97, 135, 'U', 'L'): 'D',
    (97, 135, 'U', 'R'): 'D',
    (99, 145, 'B', 'D'): 'D',
    (99, 145, 'B', 'L'): 'D',
    (99, 145, 'B', 'R'): 'D',
    (99, 145, 'B', 'U'): 'D',
    (99, 145, 'D', 'B'): 'U',
    (99, 145, 'D', 'F'): 'U',
    (99, 145, 'D', 'L'): 'U',
    (99, 145, 'D', 'R'): 'U',
    (99, 145, 'F', 'D'): 'D',
    (99, 145, 'F', 'L'): 'D',
    (99, 145, 'F', 'R'): 'D',
    (99, 145, 'F', 'U'): 'D',
    (99, 145, 'L', 'B'): 'U',
    (99, 145, 'L', 'D'): 'D',
    (99, 145, 'L', 'F'): 'U',
    (99, 145, 'L', 'U'): 'D',
    (99, 145, 'R', 'B'): 'U',
    (99, 145, 'R', 'D'): 'D',
    (99, 145, 'R', 'F'): 'U',
    (99, 145, 'R', 'U'): 'D',
    (99, 145, 'U', 'B'): 'U',
    (99, 145, 'U', 'F'): 'U',
    (99, 145, 'U', 'L'): 'U',
    (99, 145, 'U', 'R'): 'U',
    (102, 4, 'B', 'D'): 'D',
    (102, 4, 'B', 'L'): 'D',
    (102, 4, 'B', 'R'): 'D',
    (102, 4, 'B', 'U'): 'D',
    (102, 4, 'D', 'B'): 'U',
    (102, 4, 'D', 'F'): 'U',
    (102, 4, 'D', 'L'): 'U',
    (102, 4, 'D', 'R'): 'U',
    (102, 4, 'F', 'D'): 'D',
    (102, 4, 'F', 'L'): 'D',
    (102, 4, 'F', 'R'): 'D',
    (102, 4, 'F', 'U'): 'D',
    (102, 4, 'L', 'B'): 'U',
    (102, 4, 'L', 'D'): 'D',
    (102, 4, 'L', 'F'): 'U',
    (102, 4, 'L', 'U'): 'D',
    (102, 4, 'R', 'B'): 'U',
    (102, 4, 'R', 'D'): 'D',
    (102, 4, 'R', 'F'): 'U',
    (102, 4, 'R', 'U'): 'D',
    (102, 4, 'U', 'B'): 'U',
    (102, 4, 'U', 'F'): 'U',
    (102, 4, 'U', 'L'): 'U',
    (102, 4, 'U', 'R'): 'U',
    (104, 2, 'B', 'D'): 'U',
    (104, 2, 'B', 'L'): 'U',
    (104, 2, 'B', 'R'): 'U',
    (104, 2, 'B', 'U'): 'U',
    (104, 2, 'D', 'B'): 'D',
    (104, 2, 'D', 'F'): 'D',
    (104, 2, 'D', 'L'): 'D',
    (104, 2, 'D', 'R'): 'D',
    (104, 2, 'F', 'D'): 'U',
    (104, 2, 'F', 'L'): 'U',
    (104, 2, 'F', 'R'): 'U',
    (104, 2, 'F', 'U'): 'U',
    (104, 2, 'L', 'B'): 'D',
    (104, 2, 'L', 'D'): 'U',
    (104, 2, 'L', 'F'): 'D',
    (104, 2, 'L', 'U'): 'U',
    (104, 2, 'R', 'B'): 'D',
    (104, 2, 'R', 'D'): 'U',
    (104, 2, 'R', 'F'): 'D',
    (104, 2, 'R', 'U'): 'U',
    (104, 2, 'U', 'B'): 'D',
    (104, 2, 'U', 'F'): 'D',
    (104, 2, 'U', 'L'): 'D',
    (104, 2, 'U', 'R'): 'D',
    (106, 85, 'B', 'D'): 'U',
    (106, 85, 'B', 'L'): 'U',
    (106, 85, 'B', 'R'): 'U',
    (106, 85, 'B', 'U'): 'U',
    (106, 85, 'D', 'B'): 'D',
    (106, 85, 'D', 'F'): 'D',
    (106, 85, 'D', 'L'): 'D',
    (106, 85, 'D', 'R'): 'D',
    (106, 85, 'F', 'D'): 'U',
    (106, 85, 'F', 'L'): 'U',
    (106, 85, 'F', 'R'): 'U',
    (106, 85, 'F', 'U'): 'U',
    (106, 85, 'L', 'B'): 'D',
    (106, 85, 'L', 'D'): 'U',
    (106, 85, 'L', 'F'): 'D',
    (106, 85, 'L', 'U'): 'U',
    (106, 85, 'R', 'B'): 'D',
    (106, 85, 'R', 'D'): 'U',
    (106, 85, 'R', 'F'): 'D',
    (106, 85, 'R', 'U'): 'U',
    (106, 85, 'U', 'B'): 'D',
    (106, 85, 'U', 'F'): 'D',
    (106, 85, 'U', 'L'): 'D',
    (106, 85, 'U', 'R'): 'D',
    (110, 31, 'B', 'D'): 'D',
    (110, 31, 'B', 'L'): 'D',
    (110, 31, 'B', 'R'): 'D',
    (110, 31, 'B', 'U'): 'D',
    (110, 31, 'D', 'B'): 'U',
    (110, 31, 'D', 'F'): 'U',
    (110, 31, 'D', 'L'): 'U',
    (110, 31, 'D', 'R'): 'U',
    (110, 31, 'F', 'D'): 'D',
    (110, 31, 'F', 'L'): 'D',
    (110, 31, 'F', 'R'): 'D',
    (110, 31, 'F', 'U'): 'D',
    (110, 31, 'L', 'B'): 'U',
    (110, 31, 'L', 'D'): 'D',
    (110, 31, 'L', 'F'): 'U',
    (110, 31, 'L', 'U'): 'D',
    (110, 31, 'R', 'B'): 'U',
    (110, 31, 'R', 'D'): 'D',
    (110, 31, 'R', 'F'): 'U',
    (110, 31, 'R', 'U'): 'D',
    (110, 31, 'U', 'B'): 'U',
    (110, 31, 'U', 'F'): 'U',
    (110, 31, 'U', 'L'): 'U',
    (110, 31, 'U', 'R'): 'U',
    (116, 95, 'B', 'D'): 'D',
    (116, 95, 'B', 'L'): 'D',
    (116, 95, 'B', 'R'): 'D',
    (116, 95, 'B', 'U'): 'D',
    (116, 95, 'D', 'B'): 'U',
    (116, 95, 'D', 'F'): 'U',
    (116, 95, 'D', 'L'): 'U',
    (116, 95, 'D', 'R'): 'U',
    (116, 95, 'F', 'D'): 'D',
    (116, 95, 'F', 'L'): 'D',
    (116, 95, 'F', 'R'): 'D',
    (116, 95, 'F', 'U'): 'D',
    (116, 95, 'L', 'B'): 'U',
    (116, 95, 'L', 'D'): 'D',
    (116, 95, 'L', 'F'): 'U',
    (116, 95, 'L', 'U'): 'D',
    (116, 95, 'R', 'B'): 'U',
    (116, 95, 'R', 'D'): 'D',
    (116, 95, 'R', 'F'): 'U',
    (116, 95, 'R', 'U'): 'D',
    (116, 95, 'U', 'B'): 'U',
    (116, 95, 'U', 'F'): 'U',
    (116, 95, 'U', 'L'): 'U',
    (116, 95, 'U', 'R'): 'U',
    (120, 41, 'B', 'D'): 'U',
    (120, 41, 'B', 'L'): 'U',
    (120, 41, 'B', 'R'): 'U',
    (120, 41, 'B', 'U'): 'U',
    (120, 41, 'D', 'B'): 'D',
    (120, 41, 'D', 'F'): 'D',
    (120, 41, 'D', 'L'): 'D',
    (120, 41, 'D', 'R'): 'D',
    (120, 41, 'F', 'D'): 'U',
    (120, 41, 'F', 'L'): 'U',
    (120, 41, 'F', 'R'): 'U',
    (120, 41, 'F', 'U'): 'U',
    (120, 41, 'L', 'B'): 'D',
    (120, 41, 'L', 'D'): 'U',
    (120, 41, 'L', 'F'): 'D',
    (120, 41, 'L', 'U'): 'U',
    (120, 41, 'R', 'B'): 'D',
    (120, 41, 'R', 'D'): 'U',
    (120, 41, 'R', 'F'): 'D',
    (120, 41, 'R', 'U'): 'U',
    (120, 41, 'U', 'B'): 'D',
    (120, 41, 'U', 'F'): 'D',
    (120, 41, 'U', 'L'): 'D',
    (120, 41, 'U', 'R'): 'D',
    (122, 149, 'B', 'D'): 'U',
    (122, 149, 'B', 'L'): 'U',
    (122, 149, 'B', 'R'): 'U',
    (122, 149, 'B', 'U'): 'U',
    (122, 149, 'D', 'B'): 'D',
    (122, 149, 'D', 'F'): 'D',
    (122, 149, 'D', 'L'): 'D',
    (122, 149, 'D', 'R'): 'D',
    (122, 149, 'F', 'D'): 'U',
    (122, 149, 'F', 'L'): 'U',
    (122, 149, 'F', 'R'): 'U',
    (122, 149, 'F', 'U'): 'U',
    (122, 149, 'L', 'B'): 'D',
    (122, 149, 'L', 'D'): 'U',
    (122, 149, 'L', 'F'): 'D',
    (122, 149, 'L', 'U'): 'U',
    (122, 149, 'R', 'B'): 'D',
    (122, 149, 'R', 'D'): 'U',
    (122, 149, 'R', 'F'): 'D',
    (122, 149, 'R', 'U'): 'U',
    (122, 149, 'U', 'B'): 'D',
    (122, 149, 'U', 'F'): 'D',
    (122, 149, 'U', 'L'): 'D',
    (122, 149, 'U', 'R'): 'D',
    (124, 147, 'B', 'D'): 'D',
    (124, 147, 'B', 'L'): 'D',
    (124, 147, 'B', 'R'): 'D',
    (124, 147, 'B', 'U'): 'D',
    (124, 147, 'D', 'B'): 'U',
    (124, 147, 'D', 'F'): 'U',
    (124, 147, 'D', 'L'): 'U',
    (124, 147, 'D', 'R'): 'U',
    (124, 147, 'F', 'D'): 'D',
    (124, 147, 'F', 'L'): 'D',
    (124, 147, 'F', 'R'): 'D',
    (124, 147, 'F', 'U'): 'D',
    (124, 147, 'L', 'B'): 'U',
    (124, 147, 'L', 'D'): 'D',
    (124, 147, 'L', 'F'): 'U',
    (124, 147, 'L', 'U'): 'D',
    (124, 147, 'R', 'B'): 'U',
    (124, 147, 'R', 'D'): 'D',
    (124, 147, 'R', 'F'): 'U',
    (124, 147, 'R', 'U'): 'D',
    (124, 147, 'U', 'B'): 'U',
    (124, 147, 'U', 'F'): 'U',
    (124, 147, 'U', 'L'): 'U',
    (124, 147, 'U', 'R'): 'U',
    (127, 72, 'B', 'D'): 'D',
    (127, 72, 'B', 'L'): 'D',
    (127, 72, 'B', 'R'): 'D',
    (127, 72, 'B', 'U'): 'D',
    (127, 72, 'D', 'B'): 'U',
    (127, 72, 'D', 'F'): 'U',
    (127, 72, 'D', 'L'): 'U',
    (127, 72, 'D', 'R'): 'U',
    (127, 72, 'F', 'D'): 'D',
    (127, 72, 'F', 'L'): 'D',
    (127, 72, 'F', 'R'): 'D',
    (127, 72, 'F', 'U'): 'D',
    (127, 72, 'L', 'B'): 'U',
    (127, 72, 'L', 'D'): 'D',
    (127, 72, 'L', 'F'): 'U',
    (127, 72, 'L', 'U'): 'D',
    (127, 72, 'R', 'B'): 'U',
    (127, 72, 'R', 'D'): 'D',
    (127, 72, 'R', 'F'): 'U',
    (127, 72, 'R', 'U'): 'D',
    (127, 72, 'U', 'B'): 'U',
    (127, 72, 'U', 'F'): 'U',
    (127, 72, 'U', 'L'): 'U',
    (127, 72, 'U', 'R'): 'U',
    (129, 74, 'B', 'D'): 'U',
    (129, 74, 'B', 'L'): 'U',
    (129, 74, 'B', 'R'): 'U',
    (129, 74, 'B', 'U'): 'U',
    (129, 74, 'D', 'B'): 'D',
    (129, 74, 'D', 'F'): 'D',
    (129, 74, 'D', 'L'): 'D',
    (129, 74, 'D', 'R'): 'D',
    (129, 74, 'F', 'D'): 'U',
    (129, 74, 'F', 'L'): 'U',
    (129, 74, 'F', 'R'): 'U',
    (129, 74, 'F', 'U'): 'U',
    (129, 74, 'L', 'B'): 'D',
    (129, 74, 'L', 'D'): 'U',
    (129, 74, 'L', 'F'): 'D',
    (129, 74, 'L', 'U'): 'U',
    (129, 74, 'R', 'B'): 'D',
    (129, 74, 'R', 'D'): 'U',
    (129, 74, 'R', 'F'): 'D',
    (129, 74, 'R', 'U'): 'U',
    (129, 74, 'U', 'B'): 'D',
    (129, 74, 'U', 'F'): 'D',
    (129, 74, 'U', 'L'): 'D',
    (129, 74, 'U', 'R'): 'D',
    (131, 49, 'B', 'D'): 'U',
    (131, 49, 'B', 'L'): 'U',
    (131, 49, 'B', 'R'): 'U',
    (131, 49, 'B', 'U'): 'U',
    (131, 49, 'D', 'B'): 'D',
    (131, 49, 'D', 'F'): 'D',
    (131, 49, 'D', 'L'): 'D',
    (131, 49, 'D', 'R'): 'D',
    (131, 49, 'F', 'D'): 'U',
    (131, 49, 'F', 'L'): 'U',
    (131, 49, 'F', 'R'): 'U',
    (131, 49, 'F', 'U'): 'U',
    (131, 49, 'L', 'B'): 'D',
    (131, 49, 'L', 'D'): 'U',
    (131, 49, 'L', 'F'): 'D',
    (131, 49, 'L', 'U'): 'U',
    (131, 49, 'R', 'B'): 'D',
    (131, 49, 'R', 'D'): 'U',
    (131, 49, 'R', 'F'): 'D',
    (131, 49, 'R', 'U'): 'U',
    (131, 49, 'U', 'B'): 'D',
    (131, 49, 'U', 'F'): 'D',
    (131, 49, 'U', 'L'): 'D',
    (131, 49, 'U', 'R'): 'D',
    (135, 97, 'B', 'D'): 'D',
    (135, 97, 'B', 'L'): 'D',
    (135, 97, 'B', 'R'): 'D',
    (135, 97, 'B', 'U'): 'D',
    (135, 97, 'D', 'B'): 'U',
    (135, 97, 'D', 'F'): 'U',
    (135, 97, 'D', 'L'): 'U',
    (135, 97, 'D', 'R'): 'U',
    (135, 97, 'F', 'D'): 'D',
    (135, 97, 'F', 'L'): 'D',
    (135, 97, 'F', 'R'): 'D',
    (135, 97, 'F', 'U'): 'D',
    (135, 97, 'L', 'B'): 'U',
    (135, 97, 'L', 'D'): 'D',
    (135, 97, 'L', 'F'): 'U',
    (135, 97, 'L', 'U'): 'D',
    (135, 97, 'R', 'B'): 'U',
    (135, 97, 'R', 'D'): 'D',
    (135, 97, 'R', 'F'): 'U',
    (135, 97, 'R', 'U'): 'D',
    (135, 97, 'U', 'B'): 'U',
    (135, 97, 'U', 'F'): 'U',
    (135, 97, 'U', 'L'): 'U',
    (135, 97, 'U', 'R'): 'U',
    (141, 47, 'B', 'D'): 'D',
    (141, 47, 'B', 'L'): 'D',
    (141, 47, 'B', 'R'): 'D',
    (141, 47, 'B', 'U'): 'D',
    (141, 47, 'D', 'B'): 'U',
    (141, 47, 'D', 'F'): 'U',
    (141, 47, 'D', 'L'): 'U',
    (141, 47, 'D', 'R'): 'U',
    (141, 47, 'F', 'D'): 'D',
    (141, 47, 'F', 'L'): 'D',
    (141, 47, 'F', 'R'): 'D',
    (141, 47, 'F', 'U'): 'D',
    (141, 47, 'L', 'B'): 'U',
    (141, 47, 'L', 'D'): 'D',
    (141, 47, 'L', 'F'): 'U',
    (141, 47, 'L', 'U'): 'D',
    (141, 47, 'R', 'B'): 'U',
    (141, 47, 'R', 'D'): 'D',
    (141, 47, 'R', 'F'): 'U',
    (141, 47, 'R', 'U'): 'D',
    (141, 47, 'U', 'B'): 'U',
    (141, 47, 'U', 'F'): 'U',
    (141, 47, 'U', 'L'): 'U',
    (141, 47, 'U', 'R'): 'U',
    (145, 99, 'B', 'D'): 'U',
    (145, 99, 'B', 'L'): 'U',
    (145, 99, 'B', 'R'): 'U',
    (145, 99, 'B', 'U'): 'U',
    (145, 99, 'D', 'B'): 'D',
    (145, 99, 'D', 'F'): 'D',
    (145, 99, 'D', 'L'): 'D',
    (145, 99, 'D', 'R'): 'D',
    (145, 99, 'F', 'D'): 'U',
    (145, 99, 'F', 'L'): 'U',
    (145, 99, 'F', 'R'): 'U',
    (145, 99, 'F', 'U'): 'U',
    (145, 99, 'L', 'B'): 'D',
    (145, 99, 'L', 'D'): 'U',
    (145, 99, 'L', 'F'): 'D',
    (145, 99, 'L', 'U'): 'U',
    (145, 99, 'R', 'B'): 'D',
    (145, 99, 'R', 'D'): 'U',
    (145, 99, 'R', 'F'): 'D',
    (145, 99, 'R', 'U'): 'U',
    (145, 99, 'U', 'B'): 'D',
    (145, 99, 'U', 'F'): 'D',
    (145, 99, 'U', 'L'): 'D',
    (145, 99, 'U', 'R'): 'D',
    (147, 124, 'B', 'D'): 'U',
    (147, 124, 'B', 'L'): 'U',
    (147, 124, 'B', 'R'): 'U',
    (147, 124, 'B', 'U'): 'U',
    (147, 124, 'D', 'B'): 'D',
    (147, 124, 'D', 'F'): 'D',
    (147, 124, 'D', 'L'): 'D',
    (147, 124, 'D', 'R'): 'D',
    (147, 124, 'F', 'D'): 'U',
    (147, 124, 'F', 'L'): 'U',
    (147, 124, 'F', 'R'): 'U',
    (147, 124, 'F', 'U'): 'U',
    (147, 124, 'L', 'B'): 'D',
    (147, 124, 'L', 'D'): 'U',
    (147, 124, 'L', 'F'): 'D',
    (147, 124, 'L', 'U'): 'U',
    (147, 124, 'R', 'B'): 'D',
    (147, 124, 'R', 'D'): 'U',
    (147, 124, 'R', 'F'): 'D',
    (147, 124, 'R', 'U'): 'U',
    (147, 124, 'U', 'B'): 'D',
    (147, 124, 'U', 'F'): 'D',
    (147, 124, 'U', 'L'): 'D',
    (147, 124, 'U', 'R'): 'D',
    (149, 122, 'B', 'D'): 'D',
    (149, 122, 'B', 'L'): 'D',
    (149, 122, 'B', 'R'): 'D',
    (149, 122, 'B', 'U'): 'D',
    (149, 122, 'D', 'B'): 'U',
    (149, 122, 'D', 'F'): 'U',
    (149, 122, 'D', 'L'): 'U',
    (149, 122, 'D', 'R'): 'U',
    (149, 122, 'F', 'D'): 'D',
    (149, 122, 'F', 'L'): 'D',
    (149, 122, 'F', 'R'): 'D',
    (149, 122, 'F', 'U'): 'D',
    (149, 122, 'L', 'B'): 'U',
    (149, 122, 'L', 'D'): 'D',
    (149, 122, 'L', 'F'): 'U',
    (149, 122, 'L', 'U'): 'D',
    (149, 122, 'R', 'B'): 'U',
    (149, 122, 'R', 'D'): 'D',
    (149, 122, 'R', 'F'): 'U',
    (149, 122, 'R', 'U'): 'D',
    (149, 122, 'U', 'B'): 'U',
    (149, 122, 'U', 'F'): 'U',
    (149, 122, 'U', 'L'): 'U',
    (149, 122, 'U', 'R'): 'U'
}

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


def edges_recolor_555(state):
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
            raise Exception("We should not be here")

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


def centers_and_edges_pattern_555(state):
    state = list('x' + state)
    state = edges_recolor_555(state[:])

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

    centers = ''.join((
        state[7:10],    state[12:15],   state[17:20],
        state[32:35],   state[37:40],   state[42:45],
        state[57:60],   state[62:65],   state[67:70],
        state[82:85],   state[87:90],   state[92:95],
        state[107:110], state[112:115], state[117:120],
        state[132:135], state[137:140], state[142:145]
    ))

    return centers + edges


def LFRB_centers_and_edges_separate_555(state):
    state = 'x' + state

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

    centers = ''.join((
        state[32:35],   state[37:40],   state[42:45],
        state[57:60],   state[62:65],   state[67:70],
        state[82:85],   state[87:90],   state[92:95],
        state[107:110], state[112:115], state[117:120]
    ))

    return centers + edges


def centers_and_edges_separate_555(state):
    state = 'x' + state

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

    centers = ''.join((
        state[7:10],    state[12:15],   state[17:20],
        state[32:35],   state[37:40],   state[42:45],
        state[57:60],   state[62:65],   state[67:70],
        state[82:85],   state[87:90],   state[92:95],
        state[107:110], state[112:115], state[117:120],
        state[132:135], state[137:140], state[142:145]
    ))

    return centers + edges


def centers_666(state):
    state = 'x' + state
    state = ''.join((state[8:12]   , state[14:18]  , state[20:24]  , state[26:30],
                     state[44:48]  , state[50:54]  , state[56:60]  , state[62:66],
                     state[80:84]  , state[86:90]  , state[92:96]  , state[98:102],
                     state[116:120], state[122:126], state[128:132], state[134:138],
                     state[152:156], state[158:162], state[164:168], state[170:174],
                     state[188:192], state[194:198], state[200:204], state[206:210]))
    return state


def UFBD_centers_666(state):
    state = 'x' + state
    state = ''.join((state[8:12]   , state[14:18]  , state[20:24]  , state[26:30],
                     state[80:84]  , state[86:90]  , state[92:96]  , state[98:102],
                     state[152:156], state[158:162], state[164:168], state[170:174],
                     state[188:192], state[194:198], state[200:204], state[206:210]))
    return state


def UFBD_inner_x_centers_left_oblique_edges_666(state):
    state = 'x' + state

    state = ''.join((
        # inner-x-centers
        state[15], state[16], state[21], state[22],
        state[87], state[88], state[93], state[94],
        state[159], state[160], state[165], state[166],
        state[195], state[196], state[201], state[202],

        # left-oblique-edges
        state[9], state[17], state[20], state[28],
        state[81], state[89], state[92], state[100],
        state[153], state[161], state[164], state[172],
        state[189], state[197], state[200], state[208]))
    return state

def UFBD_inner_x_centers_right_oblique_edges_666(state):
    state = 'x' + state

    state = ''.join((
        # inner-x-centers
        state[15], state[16], state[21], state[22],
        state[87], state[88], state[93], state[94],
        state[159], state[160], state[165], state[166],
        state[195], state[196], state[201], state[202],

        # right-oblique-edges
        state[10], state[14], state[23], state[27],
        state[82], state[86], state[95], state[99],
        state[154], state[158], state[167], state[171],
        state[190], state[194], state[203], state[207]))
    return state


def oblique_edges_666(state):
    state = 'x' + state
    state = ''.join((state[9], state[10], state[14], state[17], state[20], state[23], state[27], state[28],
                     state[45], state[46], state[50], state[53], state[56], state[59], state[63], state[64],
                     state[81], state[82], state[86], state[89], state[92], state[95], state[99], state[100],
                     state[117], state[118], state[122], state[125], state[128], state[131], state[135], state[136],
                     state[153], state[154], state[158], state[161], state[164], state[167], state[171], state[172],
                     state[189], state[190], state[194], state[197], state[200], state[203], state[207], state[208]))
    return state


def UFBD_oblique_edges_666(state):
    state = 'x' + state
    state = ''.join((state[9], state[10], state[14], state[17], state[20], state[23], state[27], state[28],
                     state[81], state[82], state[86], state[89], state[92], state[95], state[99], state[100],
                     state[153], state[154], state[158], state[161], state[164], state[167], state[171], state[172],
                     state[189], state[190], state[194], state[197], state[200], state[203], state[207], state[208]))
    return state


def left_oblique_edges_666(state):
    state = 'x' + state
    state = ''.join((state[9], state[17], state[20], state[28],
                     state[45], state[53], state[56], state[64],
                     state[81], state[89], state[92], state[100],
                     state[117], state[125], state[128], state[136],
                     state[153], state[161], state[164], state[172],
                     state[189], state[197], state[200], state[208]))
    return state


def LFRB_oblique_edges_666(state):
    state = 'x' + state
    state = ''.join((state[45], state[46], state[50], state[53], state[56], state[59], state[63], state[64],
                     state[81], state[82], state[86], state[89], state[92], state[95], state[99], state[100],
                     state[117], state[118], state[122], state[125], state[128], state[131], state[135], state[136],
                     state[153], state[154], state[158], state[161], state[164], state[167], state[171], state[172]))
    return state


def LFRB_left_oblique_edges_666(state):
    state = 'x' + state
    state = ''.join((state[45], state[53], state[56], state[64],
                     state[81], state[89], state[92], state[100],
                     state[117], state[125], state[128], state[136],
                     state[153], state[161], state[164], state[172]))
    return state


def right_oblique_edges_666(state):
    state = 'x' + state
    state = ''.join((state[10], state[14], state[23], state[27],
                     state[46], state[50], state[59], state[63],
                     state[82], state[86], state[95], state[99],
                     state[118], state[122], state[131], state[135],
                     state[154], state[158], state[167], state[171],
                     state[190], state[194], state[203], state[207]))
    return state

def LFRB_right_oblique_edges_666(state):
    state = 'x' + state
    state = ''.join((state[46], state[50], state[59], state[63],
                     state[82], state[86], state[95], state[99],
                     state[118], state[122], state[131], state[135],
                     state[154], state[158], state[167], state[171]))
    return state


def LFRB_centers_666(state):
    state = 'x' + state
    state = ''.join((state[44:48]  , state[50:54]  , state[56:60]  , state[62:66],
                     state[80:84]  , state[86:90]  , state[92:96]  , state[98:102],
                     state[116:120], state[122:126], state[128:132], state[134:138],
                     state[152:156], state[158:162], state[164:168], state[170:174]))
    return state

def LFRB_inner_x_centers_666(state):
    state = 'x' + state
    state = ''.join((state[51], state[52], state[57], state[58],
                     state[87], state[88], state[93], state[94],
                     state[123], state[124], state[129], state[130],
                     state[159], state[160], state[165], state[166]))
    return state

def UD_centers_666(state):
    state = 'x' + state
    state = ''.join((state[8:12]   , state[14:18]  , state[20:24]  , state[26:30],
                     state[188:192], state[194:198], state[200:204], state[206:210]))
    return state


def LR_centers_666(state):
    state = 'x' + state
    state = ''.join((state[44:48]  , state[50:54]  , state[56:60]  , state[62:66],
                     state[116:120], state[122:126], state[128:132], state[134:138]))
    return state


def FB_centers_666(state):
    state = 'x' + state
    state = ''.join((state[80:84]  , state[86:90]  , state[92:96]  , state[98:102],
                     state[152:156], state[158:162], state[164:168], state[170:174]))
    return state


def inner_x_centers_666(state):
    state = 'x' + state
    state = ''.join((state[15], state[16], state[21], state[22],
                     state[51], state[52], state[57], state[58],
                     state[87], state[88], state[93], state[94],
                     state[123], state[124], state[129], state[130],
                     state[159], state[160], state[165], state[166],
                     state[195], state[196], state[201], state[202]))
    return state

def outer_x_centers_666(state):
    state = 'x' + state
    state = ''.join((state[8], state[11], state[26], state[29],
                     state[44], state[47], state[62], state[65],
                     state[80], state[83], state[98], state[101],
                     state[116], state[119], state[134], state[137],
                     state[152], state[155], state[170], state[173],
                     state[188], state[191], state[206], state[209]))
    return state

def x_centers_666(state):
    return outer_x_centers_666(state) + inner_x_centers_666(state)

def edges_666(state):
    state = 'x' + state
    state = ''.join((state[2:6]    , state[7]  , state[12:14]  , state[18:20]  , state[24:26]  , state[30] , state[32:36],
                     state[38:42]  , state[43] , state[48:50]  , state[54:56]  , state[60:62]  , state[66] , state[68:72],
                     state[74:78]  , state[79] , state[84:86]  , state[90:92]  , state[96:98]  , state[102], state[104:108],
                     state[110:114], state[115], state[120:122], state[126:128], state[132:134], state[138], state[140:144],
                     state[146:150], state[151], state[156:158], state[162:164], state[168:170], state[174], state[176:180],
                     state[182:186], state[187], state[192:194], state[198:200], state[204:206], state[210], state[212:216]))
    return state


def centers_777(state):
    state = 'x' + state
    state = ''.join((state[9:14]   , state[16:21]  , state[23:28]  , state[30:35]  , state[37:42],
                     state[58:63]  , state[65:70]  , state[72:77]  , state[79:84]  , state[86:91],
                     state[107:112], state[114:119], state[121:126], state[128:133], state[135:140],
                     state[156:161], state[163:168], state[170:175], state[177:182], state[184:189],
                     state[205:210], state[212:217], state[219:224], state[226:231], state[233:238],
                     state[254:259], state[261:266], state[268:273], state[275:280], state[282:287]))
    return state


def UD_centers_777(state):
    state = 'x' + state
    state = ''.join((state[9:14]   , state[16:21]  , state[23:28]  , state[30:35],   state[37:42],
                     state[254:259], state[261:266], state[268:273], state[275:280], state[282:287]))
    return state


def LFRB_centers_777(state):
    state = 'x' + state
    state = ''.join((state[58:63],
                     state[65:70],
                     state[72:77],
                     state[79:84],
                     state[86:91],

                     state[107:112],
                     state[114:119],
                     state[121:126],
                     state[128:133],
                     state[135:140],

                     state[156:161],
                     state[163:168],
                     state[170:175],
                     state[177:182],
                     state[184:189],

                     state[205:210],
                     state[212:217],
                     state[219:224],
                     state[226:231],
                     state[233:238]))
    return state


def LFRB_centers_special_777(state):
    state = 'x' + state
    state = ''.join((state[59:62],
                     state[65:70],
                     state[72:77],
                     state[79:84],
                     state[87:90],

                     state[108:111],
                     state[114:119],
                     state[121:126],
                     state[128:133],
                     state[136:139],

                     state[157:160],
                     state[163:168],
                     state[170:175],
                     state[177:182],
                     state[185:188],

                     state[206:209],
                     state[212:217],
                     state[219:224],
                     state[226:231],
                     state[234:237]))
    state = state.replace('L', '1').replace('R', '0').replace('F', '1').replace('B', '0')
    return state


def LFRB_inner_centers_777(state):
    state = 'x' + state
    state = ''.join((state[66:69],
                     state[73:76],
                     state[80:83],

                     state[115:118],
                     state[122:125],
                     state[129:132],

                     state[164:167],
                     state[171:174],
                     state[178:181],

                     state[213:216],
                     state[220:223],
                     state[227:230]))
    return state


def LR_centers_777(state):
    state = 'x' + state
    state = ''.join((state[58:63], state[65:70], state[72:77], state[79:84], state[86:91],
                     state[156:161], state[163:168], state[170:175], state[177:182], state[184:189]))
    return state


def FB_centers_777(state):
    state = 'x' + state
    state = ''.join((state[107:112], state[114:119], state[121:126], state[128:133], state[135:140],
                     state[205:210], state[212:217], state[219:224], state[226:231], state[233:238]))
    return state


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


def LFRB_oblique_edges_777(state):
    state = 'x' + state
    state = ''.join((state[59], state[60], state[61],
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
                     state[234], state[235], state[236]))

    return state


state_functions = {
    ('2x2x2', 'corners') : do_nothing,
    ('3x3x3', 'all')     : all_xxx,
    ('3x3x3', 'edges')   : edges_333,
    ('3x3x3', 'corners') : corners_333,

    ('4x4x4', 'all')                                         : all_xxx,
    ('4x4x4', 'edges')                                       : edges_444,
    ('4x4x4', 'edges-high-low-pattern-symmetry')             : edges_high_low_pattern_symmetry_444,
    ('4x4x4', 'edges-high-low-pattern')                      : edges_high_low_pattern_444,
    ('4x4x4', 'centers')                                     : centers_444,
    ('4x4x4', 'LFRB-centers')                                : LFRB_centers_444,
    ('4x4x4', 'UFBD-centers')                                : UFBD_centers_444,
    ('4x4x4', 'centers-and-edges')                           : centers_and_edges_444,
    ('4x4x4', 'centers-then-edges')                          : centers_then_edges_444,
    ('4x4x4', 'centers-and-edges-pattern')                   : centers_and_edges_pattern_444,
    ('4x4x4', 'centers-and-last-four-edges-pattern')         : centers_and_last_four_edges_pattern_444,
    ('4x4x4', 'centers-and-edges-separate')                  : centers_and_edges_separate_444,
    ('4x4x4', 'centers-and-edge-parity')                     : centers_and_edge_parity_444,
    ('4x4x4', 'last-four-edges-pattern')                     : last_four_edges_pattern_444,
    ('4x4x4', 'edges-pattern')                               : edges_pattern_444,

    ('5x5x5', 'all')                            : all_xxx,
    ('5x5x5', 'centers')                        : centers_555,
    ('5x5x5', 't-centers')                      : t_centers_555,
    ('5x5x5', 'x-centers')                      : x_centers_555,
    ('5x5x5', 'LR-t-centers')                   : LR_t_centers_555,
    ('5x5x5', 'UD-centers')                     : UD_centers_555,
    ('5x5x5', 'LFRB-centers')                   : LFRB_centers_555,
    ('5x5x5', 'LR-centers')                     : LR_centers_555,
    ('5x5x5', 'edges')                          : edges_555,
    ('5x5x5', 'edges-outside')                  : edges_outside_555,
    ('5x5x5', 'centers-and-edges')              : centers_and_edges_555,
    ('5x5x5', 'LR-centers-and-edges-outside')   : LR_centers_and_edges_outside_555,
    ('5x5x5', 'edges-outside-high-low-pattern') : edges_outside_high_low_pattern_555,
    ('5x5x5', 'centers-and-edges-pattern')      : centers_and_edges_pattern_555,
    ('5x5x5', 'centers-and-edges-separate')     : centers_and_edges_separate_555,
    ('5x5x5', 'LFRB-centers-and-edges-separate')     : LFRB_centers_and_edges_separate_555,
    ('5x5x5', 'centers-and-last-four-edges-pattern') : centers_and_last_four_edges_pattern_555,

    ('6x6x6', 'all')           : all_xxx,
    ('6x6x6', 'centers')       : centers_666,
    ('6x6x6', 'UFBD-centers')  : UFBD_centers_666,
    ('6x6x6', 'UFBD-inner-x-centers-left-oblique-edges')  : UFBD_inner_x_centers_left_oblique_edges_666,
    ('6x6x6', 'UFBD-inner-x-centers-right-oblique-edges')  : UFBD_inner_x_centers_right_oblique_edges_666,
    ('6x6x6', 'LFRB-centers')  : LFRB_centers_666,
    ('6x6x6', 'LFRB-inner-x-centers')  : LFRB_inner_x_centers_666,
    ('6x6x6', 'UD-centers')    : UD_centers_666,
    ('6x6x6', 'LR-centers')    : LR_centers_666,
    ('6x6x6', 'FB-centers')    : FB_centers_666,
    ('6x6x6', 'x-centers')     : x_centers_666,
    ('6x6x6', 'inner-x-centers') : inner_x_centers_666,
    ('6x6x6', 'outer-x-centers') : outer_x_centers_666,
    ('6x6x6', 'edges')         : edges_666,
    ('6x6x6', 'oblique-edges') : oblique_edges_666,
    ('6x6x6', 'UFBD-oblique-edges') : UFBD_oblique_edges_666,
    ('6x6x6', 'left-oblique-edges') : left_oblique_edges_666,
    ('6x6x6', 'right-oblique-edges') : right_oblique_edges_666,
    ('6x6x6', 'LFRB-oblique-edges') : LFRB_oblique_edges_666,
    ('6x6x6', 'LFRB-left-oblique-edges') : LFRB_left_oblique_edges_666,
    ('6x6x6', 'LFRB-right-oblique-edges') : LFRB_right_oblique_edges_666,

    ('7x7x7', 'all')                : all_xxx,
    ('7x7x7', 'centers')            : centers_777,
    ('7x7x7', 'UD-centers')         : UD_centers_777,
    ('7x7x7', 'LFRB-centers')       : LFRB_centers_777,
    ('7x7x7', 'LFRB-centers-special') : LFRB_centers_special_777,
    ('7x7x7', 'LFRB-inner-centers') : LFRB_inner_centers_777,
    ('7x7x7', 'LR-centers')         : LR_centers_777,
    ('7x7x7', 'FB-centers')         : FB_centers_777,
    ('7x7x7', 'oblique-edges')      : oblique_edges_777,
    ('7x7x7', 'LFRB-oblique-edges') : LFRB_oblique_edges_777,
    ('8x8x8', 'all')                : all_xxx,
    ('9x9x9', 'all')                : all_xxx,
    ('10x10x10', 'all')             : all_xxx,
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


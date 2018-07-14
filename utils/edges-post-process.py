#!/usr/bin/env python

from subprocess import check_output
import argparse
import logging
import shutil


def process_444(filename):
    data = {}

    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(':')
            steps = steps.split()

            # A line will be of the form:
            # BBBDDFFFRFxxxxRBRLxxxxxxLBxxxxLFLRxxxxxxxxDBFDxx:Bw2 L2 D F2 L2 D' Fw2
            # 000000000011111111112222222222333333333344444444
            # 012345678901234567890123456789012345678901234567
            state = 'x' + \
                    'x' + state[0] + state[1] + 'x' +\
                    state[2] + 'UU' + state[3] +\
                    state[4] + 'UU' + state[5] +\
                    'x' + state[6] + state[7] + 'x' +\
                    'x' + state[8] + state[9] + 'x' +\
                    state[10] + 'LL' + state[11] +\
                    state[12] + 'LL' + state[13] +\
                    'x' + state[14] + state[15] + 'x' +\
                    'x' + state[16] + state[17] + 'x' +\
                    state[18] + 'FF' + state[19] +\
                    state[20] + 'FF' + state[21] +\
                    'x' + state[22] + state[23] + 'x' +\
                    'x' + state[24] + state[25] + 'x' +\
                    state[26] + 'RR' + state[27] +\
                    state[28] + 'RR' + state[29] +\
                    'x' + state[30] + state[31] + 'x' +\
                    'x' + state[32] + state[33] + 'x' +\
                    state[34] + 'BB' + state[35] +\
                    state[36] + 'BB' + state[37] +\
                    'x' + state[38] + state[39] + 'x' +\
                    'x' + state[40] + state[41] + 'x' +\
                    state[42] + 'DD' + state[43] +\
                    state[44] + 'DD' + state[45] +\
                    'x' + state[46] + state[47] + 'x'

            state_list = list(state)
            has_unpaired_edge = False

            for (a, b, c, d) in ((2, 3, 67, 66),
                                 (5, 9, 18, 19),
                                 (14, 15, 34, 35),
                                 (8, 12, 51, 50),
                                 (24, 28, 37, 41),
                                 (40, 44, 53, 57),
                                 (56, 60, 69, 73),
                                 (72, 76, 21, 25),
                                 (82, 83, 46, 47),
                                 (85, 89, 31, 30),
                                 (94, 95, 79, 78),
                                 (88, 92, 62, 63)):
                # Edge is paired
                if state[a] == state[b] and state[c] == state[d]:

                    # x out paired edges
                    state_list[a] = 'x'
                    state_list[b] = 'x'
                    state_list[c] = 'x'
                    state_list[d] = 'x'
                else:
                    has_unpaired_edge = True

            state = ''.join(state_list)

            # only keep the edges
            state = state[2:4] +\
                    state[5] + state[8] +\
                    state[9] + state[12] +\
                    state[14:16] +\
                    state[18:20] +\
                    state[21] + state[24] +\
                    state[25] + state[28] +\
                    state[30:32] +\
                    state[34:36] +\
                    state[37] + state[40] +\
                    state[41] + state[44] +\
                    state[46:48] +\
                    state[50:52] +\
                    state[53] + state[56] +\
                    state[57] + state[60] +\
                    state[62:64] +\
                    state[66:68] +\
                    state[69] + state[72] +\
                    state[73] + state[76] +\
                    state[78:80] +\
                    state[82:84] +\
                    state[85] + state[88] +\
                    state[89] + state[92] +\
                    state[94:96]

            # I don't think it is possible for us to have an entry where all edges
            # are paired but filter those out just in case
            if has_unpaired_edge:
                if state in data:
                    if len(steps) < len(data[state]):
                        data[state] = steps
                else:
                    data[state] = steps

    return data


def process_555(filename):
    data = {}

    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.rstrip().split(':')
            steps = steps.split()

            # A line will be of the form:
            # BBBBBBBBFRRLUULxxxxxxLLDFFFxxxxxxxxxRDDxxxxxxURRLLRxxxxxxxxxxxxBBFBFBxxx:Fw2 B F' R U B' R' U' Fw2
            # 000000000011111111112222222222333333333344444444555555555566666666667777
            # 012345678901234567890123456789012345678901234567890123456789012345678901
            state = 'x' + \
                    'x' + state[0] + state[1] + state[2] + 'x' +\
                    state[3] + 'UUU' + state[4] +\
                    state[5] + 'UUU' + state[6] +\
                    state[7] + 'UUU' + state[8] +\
                    'x' + state[9] + state[10] + state[11] + 'x' +\
                    'x' + state[12] + state[13] + state[14] + 'x' +\
                    state[15] + 'LLL' + state[16] +\
                    state[17] + 'LLL' + state[18] +\
                    state[19] + 'LLL' + state[20] +\
                    'x' + state[21] + state[22] + state[23] + 'x' +\
                    'x' + state[24] + state[25] + state[26] + 'x' +\
                    state[27] + 'FFF' + state[28] +\
                    state[29] + 'FFF' + state[30] +\
                    state[31] + 'FFF' + state[32] +\
                    'x' + state[33] + state[34] + state[35] + 'x' +\
                    'x' + state[36] + state[37] + state[38] + 'x' +\
                    state[39] + 'RRR' + state[40] +\
                    state[41] + 'RRR' + state[42] +\
                    state[43] + 'RRR' + state[44] +\
                    'x' + state[45] + state[46] + state[47] + 'x' +\
                    'x' + state[48] + state[49] + state[50] + 'x' +\
                    state[51] + 'BBB' + state[52] +\
                    state[53] + 'BBB' + state[54] +\
                    state[55] + 'BBB' + state[56] +\
                    'x' + state[57] + state[58] + state[59] + 'x' +\
                    'x' + state[60] + state[61] + state[62] + 'x' +\
                    state[63] + 'DDD' + state[64] +\
                    state[65] + 'DDD' + state[66] +\
                    state[67] + 'DDD' + state[68] +\
                    'x' + state[69] + state[70] + state[71] + 'x'

            state_list = list(state)
            has_unpaired_edge = False

            for (a, b, c, d, e, f) in ((2, 3, 4, 104, 103, 102),
                                       (6, 11, 16, 27, 28, 29),
                                       (10, 15, 20, 79, 78, 77),
                                       (22, 23, 24, 52, 53, 54),
                                       (31, 36, 41, 110, 115, 120),
                                       (35, 40, 45, 56, 61, 66),
                                       (60, 65, 70, 81, 86, 91),
                                       (85, 90, 95, 106, 111, 116),
                                       (72, 73, 74, 127, 128, 129),
                                       (131, 136, 141, 49, 48, 47),
                                       (135, 140, 145, 97, 98, 99),
                                       (147, 148, 149, 124, 123, 122)):

                # Edge is paired
                if (state[a] == state[b] and state[b] == state[c] and
                    state[d] == state[e] and state[e] == state[f]):

                    # x out paired edges
                    state_list[a] = 'x'
                    state_list[b] = 'x'
                    state_list[c] = 'x'
                    state_list[d] = 'x'
                    state_list[e] = 'x'
                    state_list[f] = 'x'

                else:
                    has_unpaired_edge = True

            state = ''.join(state_list)

            # only keep the edges
            state = state[2:5] +\
                    state[6] + state[10] +\
                    state[11] + state[15] +\
                    state[16] + state[20] +\
                    state[22:25] +\
                    state[27:30] +\
                    state[31] + state[35] +\
                    state[36] + state[40] +\
                    state[41] + state[45] +\
                    state[47:50] +\
                    state[52:55] +\
                    state[56] + state[60] +\
                    state[61] + state[65] +\
                    state[66] + state[70] +\
                    state[72:75] +\
                    state[77:80] +\
                    state[81] + state[85] +\
                    state[86] + state[90] +\
                    state[91] + state[95] +\
                    state[97:100] +\
                    state[102:105] +\
                    state[106] + state[110] +\
                    state[111] + state[115] +\
                    state[116] + state[120] +\
                    state[122:125] +\
                    state[127:130] +\
                    state[131] + state[135] +\
                    state[136] + state[140] +\
                    state[141] + state[145] +\
                    state[147:150]

            # I don't think it is possible for us to have an entry where all edges
            # are paired but filter those out just in case
            if has_unpaired_edge:
                if state in data:
                    if len(steps) < len(data[state]):
                        data[state] = steps
                else:
                    data[state] = steps

    return data


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="file to process")
    args = parser.parse_args()

    if '4x4x4' in args.filename:
        data = process_444(args.filename)
    elif '5x5x5' in args.filename:
        data = process_555(args.filename)
    else:
        raise Exception("What kind of cube is this?")

    with open('final.txt', 'w') as fh:
        for state in sorted(data.keys()):
            steps = data[state]
            fh.write("%s:%s\n" % (state, ' '.join(steps)))
    shutil.move('final.txt', args.filename)

    check_output('./utils/pad-lines.py %s' % args.filename, shell=True)

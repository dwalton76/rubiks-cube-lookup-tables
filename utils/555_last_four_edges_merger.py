#!/usr/bin/env python3

"""
"""
import os
from subprocess import check_output

options = (
    '1111', # 4 edges

    '1110', # 3 edges
    '1101',
    '1011',
    '0111',

    '1100', # 2 edges
    '1010',
    '1001',
    '0110',
    '0101',
    '0011',

    '1000', # 1 edges
    '0100',
    '0010',
    '0001')

data = {}

for extension in options:
    filename = "lookup-table-5x5x5-step102-place-last-four-edges.txt." + extension

    if not os.path.isfile(filename):
        print("%s does not exist" % filename)
        continue

    with open(filename, 'r') as fh:
        '''
        xxxxLLLLxxxxRRRRxxxxxxxx:B2
        xxxxLLLRxxxxLRRRxxxxxxxx:Dw2 L' Fw2
        '''
        print(filename)

        for line in fh:
            (state, steps) = line.strip().split(':')
            steps_length = len(steps.split())

            if state not in data:
                data[state] = steps
            else:
                min_steps_length = len(data[state].split())

                if steps_length < min_steps_length:
                    data[state] = steps

filename = 'lookup-table-5x5x5-step102-place-last-four-edges.txt'
with open(filename, 'w') as fh:
    print("%d entries to write" % len(data.keys()))

    for state in sorted(data.keys()):
        steps = data[state]
        fh.write("%s:%s\n" % (state, steps))

check_output('./utils/pad_lines.py %s' % filename, shell=True)

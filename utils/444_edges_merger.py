#!/usr/bin/env python3

"""
"""
import os
import sys
from subprocess import check_output

data = {}

#for filename in ('lookup-table-4x4x4-step101-edges-all-turns.txt', 'lookup-table-4x4x4-step100-edges.txt'):
for filename in (sys.argv[1], sys.argv[2]):

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

filename = 'lookup-table-4x4x4-step100-edges.txt.merged'
with open(filename, 'w') as fh:
    print("%d entries to write" % len(data.keys()))

    for state in sorted(data.keys()):
        steps = data[state]
        fh.write("%s:%s\n" % (state, steps))

check_output('./utils/pad_lines.py %s' % filename, shell=True)

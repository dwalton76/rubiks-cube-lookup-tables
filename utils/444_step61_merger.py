#!/usr/bin/env python3

"""
Merge the 12 tables for tsai phase2 centers
"""
from subprocess import check_output

data = {}

for filename in ('lookup-table-4x4x4-step61-tsai-phase2-centers-table1.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table2.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table3.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table4.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table5.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table6.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table7.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table8.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table9.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table10.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table11.txt',
                 'lookup-table-4x4x4-step61-tsai-phase2-centers-table12.txt'):

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

with open('lookup-table-4x4x4-step61-tsai-phase2-centers.txt', 'w') as fh:
    for state in sorted(data.keys()):
        steps = data[state]
        fh.write("%s:%s\n" % (state, steps))

check_output('./utils/pad-lines.py lookup-table-4x4x4-step61-tsai-phase2-centers.txt', shell=True)

#!/usr/bin/env python3

import sys

filename = sys.argv[1]
filename_new = filename + ".new"
line_number = 0

# There are only 12 legal moves in this table
#   U U' U2
#   F2 B2 D2
#   2L 2L' 2L2
#   2R 2R' 2R2

move_to_number = {
    "U"   : '0',
    "U'"  : '1',
    "U2"  : '2',
    "F2"  : '3',
    "B2"  : '4',
    "D2"  : '5',
    "2L"  : '6',
    "2L'" : '7',
    "2L2" : '8',
    "2R"  : '9',
    "2R'" : 'a',
    "2R2" : 'b',
}

with open(filename, 'r') as fh_read:
    with open(filename_new, 'w') as fh_new:

        # Paired edges state:
        # OOo pPP QQq rRR sSS TTt uUU VVv WWw xXX YYy zZZ

        # We only care about six of these edges though
        # OOo pPP QQq rRR --- --- --- --- WWw --- --- zZZ

        # 000 000 000 011 111 111 112 222 222 222 333 333
        # 012 345 678 901 234 567 890 123 456 789 012 345
        # OOo pPP QQq rRR --- --- --- --- WWw --- --- zZZ

        # And of those six we only care about the wings because we never change the
        # orientation of the midges for this table.
        wings_for_horseshoe_edges_pattern_555 = (0, 2, 3, 5, 6, 8, 9, 11, 24, 26, 33, 35)

        for line in fh_read:
            (state, steps) = line.strip().split(':')
            state = ''.join([state[index] for index in wings_for_horseshoe_edges_pattern_555])

            new_steps = []
            for step in steps.split():
                new_steps.append(move_to_number[step])
            new_steps = ''.join(new_steps)
            fh_new.write("%s:%s\n" % (state, new_steps))

            line_number += 1

            if line_number % 1000000 == 0:
                print(line_number)

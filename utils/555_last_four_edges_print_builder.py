#!/usr/bin/env python3

"""
Here a 1 represents an unpaired edge.  These are all of the combinations of
unpaired edges you can have:

0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111

1-edge
0001
0010
0100
1000

2-edges
0011
0101
0110
1001
1010
1100

3-edges
0111
1011
1101
1110

4-edges
1111
"""

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

for option in options:
    print("make clean; ./builder.py --cores 4 --depth 20 --type 5x5x5-place-last-four-edges --option %s" % option)
print("./utils/555_last_four_edges_merger.py")

print("\n\n\n")

# for generating the noturn solution list
for option in options:
    print("make clean; ./builder.py --cores 1 --depth 1 --type 5x5x5-place-last-four-edges --noturn --option %s" % option)
print("./utils/555_last_four_edges_merger.py")

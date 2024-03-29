#!/usr/bin/env python3

# standard libraries
import sys


def edge_count_444(state):

    # The facelets are numbered:
    #
    #               - 02 03 -
    #              05  - -  08
    #              09  - -  12
    #               - 14 15 -
    #
    #  - 18 19 -    - 34 35 -    - 50 51 -    - 66 67 -
    # 21  - -  24  37  - -  40  53  - -  56  69  - -  72
    # 25  - -  28  41  - -  44  57  - -  60  73  - -  76
    #  - 30 31 -    - 46 47 -    - 62 63 -    - 78 79 -
    #
    #               - 82 83 -
    #              85  - -  88
    #              89  - -  92
    #               - 94 95 -
    #
    #
    # The wings are labeled 0123456789abcdefghijklmn
    #
    #               -  0 1  -
    #               2  - -  3
    #               4  - -  5
    #               -  6 7 -
    #
    #  -  2 4  -    -  6 7  -    -  5 3  -    -  1 0  -
    #  8  - -  9    9  - -  c    c  - -  d    d  - -  8
    #  a  - -  b    b  - -  e    e  - -  f    f  - -  a
    #  -  k i  -    -  g h  -    -  j l  -    -  n m  -
    #
    #               -  g h  -
    #               i  - -  j
    #               k  - -  l
    #               -  m n  -
    #
    # 'state' goes wing by # wing and records the location of where the sibling wing is located.
    #
    # Example: nmjalk76jlib395876be9chgkaefcd24mnfid301hg825410
    # means that the wing at location (2, 67) has its sibling at wing n (95, 78)
    #
    # state: 0123456789abcdefghijklmn
    #
    # index: 000000000011111111112222
    #        012345678901234567890123
    paired_edges_count = 0
    unpaired_edges_count = 0

    # Upper
    if state[0] == "1":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[2] == "4":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[3] == "5":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[6] == "7":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    # Left
    if state[8] == "a":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[9] == "b":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    # Right
    if state[12] == "e":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[13] == "f":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    # Down
    if state[16] == "h":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[18] == "k":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[19] == "l":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    if state[22] == "n":
        paired_edges_count += 1
    else:
        unpaired_edges_count += 1

    return (paired_edges_count, unpaired_edges_count)


def edge_count_555(state):
    raise Exception("ImplementThis")
    return 0


filename = sys.argv[1]
stats = {}
edge_stats = {}
edge_stats2 = {}

linecount = 0

if "step101-edges" in filename:
    do_edges = True
else:
    do_edges = False
do_edges = False

for x in range(0, 30):
    stats[x] = 0

with open(filename, "r") as fh:
    for line in fh:
        line = line.rstrip()

        try:
            (state, steps) = line.split(":")
        except Exception:
            state = None
            steps = line

        if "," in steps:
            steps = steps.split(",")[0]

        if steps.isdigit():
            len_steps = int(steps)
        else:
            steps = steps.split()
            len_steps = len(steps)

        if len_steps == 0:
            print(line)

        stats[len_steps] += 1

        # Edge stats
        if do_edges:

            if "4x4x4-step101" in filename:
                (paired_count, unpaired_count) = edge_count_444(state)
            elif "5x5x5-step101" in filename:
                (paired_count, unpaired_count) = edge_count_555(state)
            else:
                raise Exception("We should not be here")

            if unpaired_count not in edge_stats:
                edge_stats[unpaired_count] = 0
            edge_stats[unpaired_count] += 1

            if unpaired_count not in edge_stats2:
                edge_stats2[unpaired_count] = {}

            if len_steps not in edge_stats2[unpaired_count]:
                edge_stats2[unpaired_count][len_steps] = 0
            edge_stats2[unpaired_count][len_steps] += 1

        linecount += 1

print("\n    " + filename)
print("    " + "=" * len(filename))

prev = None
total_steps = 0
for key in sorted(stats.keys()):

    if not stats[key]:
        continue

    if prev is None:
        delta = float(0)
    else:
        delta = float(stats[key] / prev)

    print(
        "    {} steps has {:,} entries ({} percent, {:.2f}x previous step)".format(
            key, stats[key], int(float(stats[key] / linecount) * 100), delta
        )
    )
    total_steps += key * stats[key]
    prev = stats[key]

if do_edges:

    print("\n\nEdge Stats")
    for key in sorted(edge_stats.keys()):
        print(
            "%d unpaired edges, %d entries (%d percent)"
            % (key, edge_stats[key], int(float(edge_stats[key] / linecount) * 100))
        )

        for len_steps in sorted(edge_stats2[key].keys()):
            len_steps_count = edge_stats2[key][len_steps]
            print("    %d steps has %d entries" % (len_steps, len_steps_count))

print(f"\n    Total: {linecount:,} entries")

if linecount:
    print(f"    Average: {float(total_steps / linecount):.2f} moves\n\n")

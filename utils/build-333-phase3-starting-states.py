#!/usr/bin/env python3


# Start with this and overlay the corners state from step142-corners.txt
'''
        x F x
        x U x
        x F x

 x x x  x F x  x x x  x F x
 x L x  x F x  x R x  x B x
 x x x  x F x  x x x  x F x

        x F x
        x D x
        x F x


xFxxUxxFxxxxxLxxxxxFxxFxxFxxxxxRxxxxxFxxBxxFxxFxxDxxFx
'''

CORNERS = (
    1, 3, 7, 9,
    10, 12, 16, 18,
    19, 21, 25, 27,
    28, 30, 34, 36,
    37, 39, 43, 45,
    46, 48, 52, 54,
)

starting_state = list("xFxxUxxFxxxxxLxxxxxFxxFxxFxxxxxRxxxxxFxxBxxFxxFxxDxxFx")
print(len(starting_state))

with open("lookup-table-3x3x3-step142-corners.txt", "r") as fh:
    for line in fh:
        line = line.strip()
        (corners_state, _) = line.split(":")
        state = starting_state[:]

        for (i, j) in zip(CORNERS, list(corners_state)):
            state[i-1] = j

        print("    ('" + "".join(state) + "', 'ULFRBD'),")


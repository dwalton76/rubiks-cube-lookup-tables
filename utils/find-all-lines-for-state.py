#!/usr/bin/env python3

from buildercore import find_all_lines_for_state

filename = "centers_solutions_555.txt"
linecount = 22013658

with open(filename, "r") as fh:
    first_line = next(fh)
    width = len(first_line)
    

    results = find_all_lines_for_state(fh, linecount, width, "BBBUUUBBBLLLLLLLLLUFUUFUUFURRRRRRRRRDDDBBBDDDFDFFDFFDF")
    print("\n".join(results))


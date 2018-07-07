#!/usr/bin/env python3

import sys

filename = sys.argv[1]

if len(sys.argv) > 2:
    hex_digits = int(sys.argv[2])
    hex_format = '%' + "0%dx" % hex_digits
else:
    hex_digits = None

result = []
with open(filename, 'r') as fh:
    for line in fh:
        line = line.strip()
        line = line.replace(" 'ULFRBD'),", "")
        line = line.replace("(", "")
        line = line.replace(".", "")

        if hex_digits:
            line = line.replace('x', '0').replace('U', '1').replace('L', '1').replace('F', '1').replace('R', '1').replace('B', '1').replace('D', '1')
            line = line.replace("'", "")
            line = line.replace(",", "")
            #print("             %0dx," % hex(int(line, 2))[2:])
            result.append("             '" + hex_format % int(line, 2) + "',")
        else:
            result.append("             %s" % line)

print('\n'.join(sorted(result)))
print("%d entries" % len(result))

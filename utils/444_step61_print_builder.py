#!/usr/bin/env python3

for x in range(1, 13):
    print("make clean; ./builder.py --cores 4 --depth 20 --type 4x4x4-tsai-phase2-centers-table%d" % x)

#!/usr/bin/env python3

import sys

for option1 in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c'):
    for option2 in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c'):
        print("make clean; ./builder.py --mac --cores 4 --depth 20 --type 4x4x4-tsai-phase4-centers --option %s%s" % (option1, option2))
print("./utils/444_step403_merger.py")
print("\n\n\n")

# for generating the noturn solution list
for option1 in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c'):
    for option2 in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c'):
        print("make clean; ./builder.py --mac --cores 1 --depth 1 --type 4x4x4-tsai-phase4-centers --noturn --option %s%s" % (option1, option2))
print("./utils/444_step403_merger.py")

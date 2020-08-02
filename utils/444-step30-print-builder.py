#!/usr/bin/env python3

# standard libraries
import itertools

permutation = (
    "ULFRBD",
    "UFRBLD",
    "URBLFD",
    "UBLFRD",
    "DLBRFU",
    "DBRFLU",
    "DRFLBU",
    "DFLBRU",
    "LUBDFR",
    "LBDFUR",
    "LDFUBR",
    "LFUBDR",
    "FLDRUB",
    "FDRULB",
    "FRULDB",
    "FULDRB",
    "RDBUFL",
    "RBUFDL",
    "RUFDBL",
    "RFDBUL",
    "BURDLF",
    "BRDLUF",
    "BDLURF",
    "BLURDF",
)

for x in permutation:
    print("make clean; ./builder.py --cores 2 --depth 20 --type 4x4x4-ULFRBD-centers-solve --option %s" % "".join(x))
print("./utils/444_step30_merger.py")

print("\n\n\n")

# for generating the noturn solution list
for x in permutation:
    print(
        "make clean; ./builder.py --cores 1 --depth 1 --type 4x4x4-ULFRBD-centers-solve --noturn --option %s"
        % "".join(x)
    )
print("./utils/444_step30_merger.py")

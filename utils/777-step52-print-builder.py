#!/usr/bin/env python3

# standard libraries
import itertools

permutation = []
for x in itertools.permutations("UUUUDDDD"):
    permutation.append(x)
permutation = sorted(list(set(permutation)))

for x in permutation:
    print(
        "make clean; ./builder.py --cores 4 --depth 20 --type 7x7x7-UD-solve-inner-center-and-oblique-edges-edges-only --option %s"
        % "".join(x)
    )
print("./utils/777_step52_merger.py")

print("\n\n\n")

# for generating the noturn solution list
for x in permutation:
    print(
        "make clean; ./builder.py --cores 1 --depth 1 --type 7x7x7-UD-solve-inner-center-and-oblique-edges-edges-only --noturn --option %s"
        % "".join(x)
    )
print("./utils/777_step52_merger.py")

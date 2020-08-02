#!/usr/bin/env python3

# standard libraries
import itertools

permutation = []
for x in itertools.permutations("UUUUDDDD"):
    permutation.append(x)
permutation = sorted(list(set(permutation)))

for x in permutation:
    print(
        "make clean; ./builder.py --cores 4 --depth 6 --type 7x7x7-UD-solve-inner-center-and-oblique-edges --option %s"
        % "".join(x)
    )
print("./utils/777_step50_merger.py")

print("\n\n\n")

# for generating the noturn solution list
for x in permutation:
    print(
        "make clean; ./builder.py --cores 1 --depth 1 --type 7x7x7-UD-solve-inner-center-and-oblique-edges --noturn --option %s"
        % "".join(x)
    )
print("./utils/777_step50_merger.py")

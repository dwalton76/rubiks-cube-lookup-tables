#!/usr/bin/env python3

# standard libraries
import os
import sys

# third party libraries
from pyhashxx import hashxx

if len(sys.argv) != 4:
    print("ERROR: To use './hash-lookup.py FILENAME KEY BUCKETCOUNT'")
    sys.exit(1)

filename = sys.argv[1]
key = sys.argv[2]
bucketcount = int(sys.argv[3])

if not os.path.isfile(filename):
    print(f"ERROR: {filename} does not exist")
    sys.exit(1)

hash_raw = hashxx(key.encode("utf-8"))
hash_index = int(hash_raw % bucketcount)

with open(filename, "rb") as fh:
    content = fh.read()
    cost = int(chr(content[hash_index]), 16)

    print(f"hash_raw: {hash_raw}")
    print(f"hash_index: {hash_index}")
    print(f"cost: {cost}")

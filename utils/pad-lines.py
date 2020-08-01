#!/usr/bin/env python3

# standard libraries
import shutil
import subprocess
import sys

filename = sys.argv[1]
filename_pad = filename + '.pad'

# Use "wc --max-line-length" to get the width of the longest line in the file
max_length = int(subprocess.check_output("wc --max-line-length %s" % filename, shell=True).decode("utf-8").strip().split()[0])
print("%s max_length: %d" % (filename, max_length))

line_number = 0
WRITE_BATCH_SIZE = 1000000
to_write = []
to_write_count = 0

with open(filename_pad, 'w') as fh_pad:
    with open(filename, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            spaces_to_add = max_length - len(line)

            if spaces_to_add:
                line = line + " " * spaces_to_add

            to_write.append(line)
            to_write_count += 1

            if to_write_count >= WRITE_BATCH_SIZE:
                fh_pad.write("\n".join(to_write))
                fh_pad.write("\n")
                to_write = []
                to_write_count = 0

            line_number += 1

    if to_write_count:
        fh_pad.write("\n".join(to_write))
        fh_pad.write("\n")
        to_write = []
        to_write_count = 0

shutil.move(filename_pad, filename)

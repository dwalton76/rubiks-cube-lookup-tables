#!/usr/bin/env python3

import sys
import shutil
import subprocess

filename = sys.argv[1]
filename_pad = filename + '.pad'

# Use wc to get the width of the longest line in the file
max_length = int(subprocess.check_output("wc --max-line-length %s" % filename, shell=True).decode("utf-8").strip().split()[0])
print("%s max_length: %d" % (filename, max_length))

line_number = 0
WRITE_BATCH_SIZE = 1000000
to_write = []
to_write_count = 0

with open(filename_pad, 'w') as fh_pad:
    with open(filename, 'r') as fh:
        for line in fh:
            line = line.strip()
            length = len(line)
            spaces_to_add = max_length - length

            if spaces_to_add:
                line = line + ' ' * spaces_to_add

            to_write.append(line)
            to_write_count += 1

            if to_write_count >= WRITE_BATCH_SIZE:
                fh_pad.write("\n".join(to_write))
                fh_pad.write("\n")
                to_write = []
                to_write_count = 0

            line_number += 1

            #if line_number % 100000 == 0:
            #    print(line_number)

    if to_write_count:
        fh_pad.write("\n".join(to_write))
        fh_pad.write("\n")
        to_write = []
        to_write_count = 0

shutil.move(filename_pad, filename)

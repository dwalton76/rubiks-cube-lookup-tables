"""
Create a .new copy of the lookup table that keep solutions
up to a specified length
"""

# standard libraries
import subprocess
import sys

filename = sys.argv[1]
filename_new = filename + ".new"
step_limit = int(sys.argv[2])
keepers = {}
line_number = 0

with open(filename_new, "w") as fh_new:
    with open(filename, "r") as fh:
        for line in fh:
            (state, steps) = line.strip().split(":")

            if steps.isdigit():
                steps_len = int(steps)
            else:
                steps_len = len(steps.split())

            if steps_len <= step_limit:
                fh_new.write(f"{state}:{steps}\n")

            line_number += 1

            if line_number % 1000000 == 0:
                print("WRITE: %d" % line_number)

subprocess.check_output(f"./utils/pad-lines.py {filename_new}", shell=True)

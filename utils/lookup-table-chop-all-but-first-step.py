"""
Only keep the first step of the solution
"""

# standard libraries
import shutil
import subprocess
import sys

count = 0

filename = sys.argv[1]
filename_small = filename + ".small"

with open(filename, "r") as fh_read:
    with open(filename_small, "w") as fh:
        for line in fh_read:
            (state, steps) = line.strip().split(":")
            steps = steps.split()

            if steps:
                fh.write(f"{state}:{steps[0]}\n")
            else:
                fh.write(f"{state}:\n")

            count += 1

            if count % 1000000 == 0:
                print(count)

shutil.move(filename_small, filename)
subprocess.check_output(f"./utils/pad-lines.py {filename}", shell=True)

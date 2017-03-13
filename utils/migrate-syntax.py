#!/usr/bin/env python3

import subprocess
import sys

filename = sys.argv[1]
filename_new = "foo.txt"

with open(filename_new, 'w') as fh_new:
    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            steps = steps.split()

            steps_new = []
            for step in steps:
                if "2U" in step:
                    step = step.replace("2U", "Uw")
                elif "2L" in step:
                    step = step.replace("2L", "Lw")
                elif "2F" in step:
                    step = step.replace("2F", "Fw")
                elif "2R" in step:
                    step = step.replace("2R", "Rw")
                elif "2B" in step:
                    step = step.replace("2B", "Bw")
                elif "2D" in step:
                    step = step.replace("2D", "Dw")
                
                elif "3U" in step:
                    step = step.replace("3U", "3Uw")
                elif "3L" in step:
                    step = step.replace("3L", "3Lw")
                elif "3F" in step:
                    step = step.replace("3F", "3Fw")
                elif "3R" in step:
                    step = step.replace("3R", "3Rw")
                elif "3B" in step:
                    step = step.replace("3B", "3Bw")
                elif "3D" in step:
                    step = step.replace("3D", "3Dw")
                steps_new.append(step)

            fh_new.write("%s:%s\n" % (state, ' '.join(steps_new)))

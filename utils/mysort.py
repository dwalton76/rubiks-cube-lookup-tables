#!/usr/bin/env python3

import os
import sys
import subprocess

filename = sys.argv[1]

if not os.path.exists(filename):
    print("ERROR: %s does not exist" % filename)
    sys.exit(1)

subprocess.check_output("LC_ALL=C sort --temporary-directory=./tmp/ --output %s %s " % (filename, filename), shell=True)

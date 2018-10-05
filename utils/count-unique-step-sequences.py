#!/usr/bin/env python3

import sys

filename = sys.argv[1]

all_steps = set()
all_states = set()

with open(filename, 'r') as fh:
    for line in fh:
        (state, steps) = line.split(':')
        steps = steps.rstrip()
        all_states.add(state)
        all_steps.add(steps)

print("%d states" % len(all_states))
print("%d step sequences" % len(all_steps))

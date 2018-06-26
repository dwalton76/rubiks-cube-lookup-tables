#!/usr/bin/env python3

from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)20s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)


with open('lookup-table-4x4x4-step500-tsai-phase5.txt', 'r') as fh_read, \
    open('builder444ss.py', 'w') as fh_write:

    cube = RubiksCube444(solved_444, 'URFDLB')
    fh_write.write("starting_states_step400 = (\n")

    for (line_number, line) in enumerate(fh_read):
        (state, steps_to_solve) = line.rstrip().split(':')
        steps_to_solve = steps_to_solve.split()

        if len(steps_to_solve) <= 4:
            cube.re_init()
            steps_to_scramble = reverse_steps(steps_to_solve)

            for step in steps_to_scramble:
                cube.rotate(step)

            fh_write.write("             ('%s', 'ascii'),\n" % ''.join(cube.state[1:]))

        if line_number % 100000 == 0:
            log.info("LINE: %d" % line_number)

    fh_write.write(")\n")

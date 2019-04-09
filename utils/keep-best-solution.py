#!/usr/bin/env python3

import logging
import sys
import shutil

log = logging.getLogger(__name__)


def keep_best_solutions(filename):
    """
    filename will contain multiple entries for a given state, keep
    the line for each state that has the shortest solution
    """
    filename_final = filename + ".final"
    state_min_solution_len = None
    state_min_solution = None
    prev_state = None

    with open(filename_final, "w") as fh_final:
        with open(filename, "r") as fh:
            for (line_number, line) in enumerate(fh):
                (state, steps_to_solve) = line.strip().split(":")
                solution_len = len(steps_to_solve.split())

                if prev_state is not None and state != prev_state:
                    fh_final.write("%s:%s\n" % (prev_state, state_min_solution))
                    state_min_solution_len = None
                    state_min_solution = None

                if state_min_solution_len is None or solution_len < state_min_solution_len:
                    state_min_solution_len = solution_len
                    state_min_solution = steps_to_solve

                prev_state = state

                #if line_number % 1000000 == 0:
                #    log.info("{:,}".format(line_number))
            fh_final.write("%s:%s\n" % (prev_state, state_min_solution))

    shutil.move(filename_final, filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    keep_best_solutions(sys.argv[1])

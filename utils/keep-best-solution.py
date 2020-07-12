#!/usr/bin/env python3

import logging
import re
import sys
import shutil

log = logging.getLogger(__name__)


def keep_best_solutions(filename):
    """
    filename will contain multiple entries for a given state, keep
    the line for each state that has the shortest solution
    """
    filename_final = filename + ".final"
    state_min_solution_len = 99
    state_min_solution = None
    prev_state = ""
    use_edges_pattern = None
    to_write = []
    to_write_count = 0

    re_line = re.compile("^(.*):(.*?)\s*$")

    with open(filename, "r") as fh:
        line = next(fh)

        if line.count(":") == 1:
            use_regex = False
        else:
            use_regex = True

    with open(filename_final, "w") as fh_final:
        with open(filename, "r") as fh:
            for line in fh:
                if use_regex:
                    match = re_line.match(line)
                    state = match.group(1)
                    steps_to_solve = match.group(2)
                else:
                    (state, steps_to_solve) = line.rstrip().split(":")

                # solution_len = len(steps_to_solve.split())
                solution_len = steps_to_solve.count(" ") + 1

                if state != prev_state and prev_state:
                    to_write.append("%s:%s\n" % (prev_state, state_min_solution))
                    to_write_count += 1
                    state_min_solution_len = 99
                    state_min_solution = None

                    if to_write_count >= 100000:
                        fh_final.write("".join(to_write))
                        to_write = []
                        to_write_count = 0

                if solution_len < state_min_solution_len:
                    state_min_solution_len = solution_len
                    state_min_solution = steps_to_solve

                prev_state = state

            to_write.append("%s:%s\n" % (prev_state, state_min_solution))
            to_write_count += 1

        if to_write_count:
            fh_final.write("".join(to_write))
            to_write = []
            to_write_count = 0

    shutil.move(filename_final, filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    keep_best_solutions(sys.argv[1])

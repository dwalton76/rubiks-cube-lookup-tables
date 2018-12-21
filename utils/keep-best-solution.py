#!/usr/bin/env python3

import logging
import sys

log = logging.getLogger(__name__)


def keep_best_solutions(filename):
    """
    filename will contain multiple entries for a given edges_state, keep
    the line for each edges_state that has the shortest solution
    """
    filename_final = filename + ".final"
    edges_state_min_solution_len = None
    edges_state_min_solution = None
    prev_edges_state = None

    with open(filename_final, "w") as fh_final:
        with open(filename, "r") as fh:
            for (line_number, line) in enumerate(fh):
                (edges_state, steps_to_solve) = line.strip().split(":")
                solution_len = len(steps_to_solve.split())

                if prev_edges_state is not None and edges_state != prev_edges_state:
                    fh_final.write("%s:%s\n" % (prev_edges_state, edges_state_min_solution))
                    edges_state_min_solution_len = None
                    edges_state_min_solution = None

                if edges_state_min_solution_len is None or solution_len < edges_state_min_solution_len:
                    edges_state_min_solution_len = solution_len
                    edges_state_min_solution = steps_to_solve

                prev_edges_state = edges_state

                if line_number % 1000000 == 0:
                    log.info(line_number)
            fh_final.write("%s:%s\n" % (prev_edges_state, edges_state_min_solution))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    keep_best_solutions(sys.argv[1])

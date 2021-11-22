#!/usr/bin/env python3

# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import reverse_steps
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    edge_orbit_0_555,
    edge_orbit_1_555,
    edges_recolor_pattern_555,
    midge_indexes,
    solved_555,
    wings_for_edges_pattern_555,
)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    logger = logging.getLogger(__name__)

    cube = RubiksCube555(solved_555, "URFDLB")
    cube.nuke_corners()
    cube.nuke_centers()

    three_edges = (31, 36, 41, 35, 40, 45, 56, 61, 66, 60, 65, 70, 81, 86, 91, 110, 115, 120)

    for x in list(edge_orbit_0_555) + list(edge_orbit_1_555):
        if x not in three_edges:
            cube.state[x] = "-"

    cube.print_cube("init")
    nuke_state = cube.state[:]

    filename = "lookup-tables/lookup-table-5x5x5-step55-phase5-three-edges-wings.txt"
    filename_new = filename + ".new"

    with open(filename, "r") as fh:
        with open(filename_new, "w") as fh_new:
            for index, line in enumerate(fh):
                state, steps_to_solve = line.rstrip().split(":")
                steps_to_solve_str = steps_to_solve
                steps_to_solve = steps_to_solve.split()
                steps_to_scramble = reverse_steps(steps_to_solve)

                for step in steps_to_scramble:
                    cube.rotate(step)

                tmp_state = edges_recolor_pattern_555(cube.state[:])
                edges_state = []

                for x in wings_for_edges_pattern_555:
                    if x in midge_indexes:
                        edges_state.append("-")
                    else:
                        edges_state.append(tmp_state[x])

                edges_state = "".join(edges_state)
                fh_new.write(f"{edges_state}:{steps_to_solve_str}\n")

                # cube.print_cube(f"{index}: {steps_to_scramble} {edges_state}")
                cube.state = nuke_state[:]
                cube.solution = []

                if index % 10000 == 0:
                    logger.info(f"{index:,}")

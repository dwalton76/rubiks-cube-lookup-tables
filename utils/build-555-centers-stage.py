#!/usr/bin/env python3

# standard libraries
import logging

# rubiks cube libraries
from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

cube = RubiksCube555(solved_555, "URFDLB")
cube.lt_init()
# cube.print_cube_layout()

# create the base state for staging centers via one phase
# - nuke edges
# - nuke corners
# - nuke the dead centers
# - make F and B centers "x"
# - make R centers L
# - make D centers U
cube.nuke_edges()
cube.nuke_corners()

for x in [13, 38, 63, 88, 113, 138]:
    cube.state[x] = "."

for side in cube.sides.values():
    for x in side.center_pos:
        if cube.state[x] == "F" or cube.state[x] == "B":
            cube.state[x] = "x"
        elif cube.state[x] == "R":
            cube.state[x] = "L"
        elif cube.state[x] == "D":
            cube.state[x] = "U"

original_state = cube.state[:]

to_write = []
to_write_count = 0
debug = False
filename = "lookup-tables/lookup-table-5x5x5-step14-centers-stage.txt.6-deep"
eglt_filename = "lookup-tables/lookup-table-5x5x5-step14-centers-stage-eglt.txt"
with open(filename, "r") as fh, open(eglt_filename, "w") as fh_eglt:
    for index, line in enumerate(fh):
        (state, steps_to_solve) = line.strip().split(":")
        steps_to_solve = steps_to_solve.split()
        steps_to_scramble = reverse_steps(steps_to_solve)

        for step in steps_to_scramble:
            cube.rotate(step)

        if debug:
            cube.print_cube()

            print(
                f"state {cube.lt_LR_t_centers_stage.state()} is state_index {cube.lt_LR_t_centers_stage.state_index()}"
            )
            print(
                f"state {cube.lt_LR_x_centers_stage.state()} is state_index {cube.lt_LR_x_centers_stage.state_index()}"
            )
            print(
                f"state {cube.lt_UD_t_centers_stage.state()} is state_index {cube.lt_UD_t_centers_stage.state_index()}"
            )
            print(
                f"state {cube.lt_UD_x_centers_stage.state()} is state_index {cube.lt_UD_x_centers_stage.state_index()}"
            )

            # for step in steps_to_solve:
            #     cube.rotate(step)
            # cube.print_cube()

        to_write.append(
            f"{cube.lt_LR_t_centers_stage.state_index()}-{cube.lt_LR_x_centers_stage.state_index()}-{cube.lt_UD_t_centers_stage.state_index()}-{cube.lt_UD_x_centers_stage.state_index()}:{len(steps_to_solve)}"
        )
        to_write_count += 1

        cube.state = original_state[:]
        cube.solution = []

        if to_write_count == 10000:
            log.info(f"{index + 1:,}")
            fh_eglt.write("\n".join(to_write))
            fh_eglt.write("\n")
            to_write = []
            to_write_count = 0

    if to_write:
        fh_eglt.write("\n".join(to_write))
        fh_eglt.write("\n")
        to_write = []
        to_write_count = 0

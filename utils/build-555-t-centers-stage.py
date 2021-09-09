#!/usr/bin/env python3

# standard libraries
import logging
import random

# rubiks cube libraries
from rubikscubennnsolver.LookupTable import get_file_vitals
from rubikscubennnsolver.misc import print_stats_median
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, t_centers_555

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

dead_centers = [13, 38, 63, 88, 113, 138]
for x in dead_centers:
    cube.state[x] = "."

for side in cube.sides.values():
    for x in side.center_pos:
        if x not in t_centers_555:
            cube.state[x] = "."
        elif cube.state[x] == "F" or cube.state[x] == "B":
            cube.state[x] = "x"
        elif cube.state[x] == "R":
            cube.state[x] = "L"
        elif cube.state[x] == "D":
            cube.state[x] = "U"
original_state = cube.state[:]
# cube.print_cube()
data = {}

t_centers_minus_dead_centers = []
for x in t_centers_555:
    if x not in dead_centers:
        t_centers_minus_dead_centers.append(x)

filename = "/storage/dwalton76/lookup-table-5x5x5-step15-centers-stage-t-center-only.txt"
line_width, state_width, line_count = get_file_vitals(filename)
print(f"filename {filename}, line_width {line_width}, state_width {state_width}, line_count {line_count:,}")
lines_to_process = 10000

with open(filename, "r") as fh:
    for x in range(lines_to_process):
        line_index = random.randint(0, line_count - 1)
        fh.seek(line_index * line_width)
        line = fh.read(line_width).rstrip()
        # log.info(f"line_index {line_index:,} is {line}")

        cube.state = original_state[:]
        cube.solution = []

        state, steps_to_solve = line.rstrip().split(":")
        state = state.replace("F", "x")
        steps_to_solve = steps_to_solve.split()
        steps_count = len(steps_to_solve)
        cost = steps_count

        # put the cube in the desired state
        for pos, value in zip(t_centers_minus_dead_centers, state):
            cube.state[pos] = value
        # cube.print_cube()

        lr_state = cube.lt_LR_t_centers_stage.state()
        lr_cost = cube.lt_LR_t_centers_stage.steps_cost(lr_state)
        ud_state = cube.lt_UD_t_centers_stage.state()
        ud_cost = cube.lt_UD_t_centers_stage.steps_cost(ud_state)
        # log.info(f"INIT LR t-centers cost {lr_cost}, UD t-centers cost {ud_cost}")

        if (lr_cost, ud_cost) not in data:
            data[(lr_cost, ud_cost)] = []
        data[(lr_cost, ud_cost)].append(cost)

        # now solve the cube where for each step we note the LR t-centers cost and the UD t-centers cose
        for step_index, step in enumerate(steps_to_solve):
            cube.rotate(step)
            lr_state = cube.lt_LR_t_centers_stage.state()
            lr_cost = cube.lt_LR_t_centers_stage.steps_cost(lr_state)
            ud_state = cube.lt_UD_t_centers_stage.state()
            ud_cost = cube.lt_UD_t_centers_stage.steps_cost(ud_state)
            cost -= 1

            if (lr_cost, ud_cost) not in data:
                data[(lr_cost, ud_cost)] = []
            data[(lr_cost, ud_cost)].append(cost)
            # log.info(f"{step_index+1}/{steps_count} {step} LR t-centers cost {lr_cost}, UD t-centers cost {ud_cost}, cost {cost}")

        # cube.print_cube()

        if x % 100 == 0:
            log.info(f"{x} lines processed")
            print_stats_median(data)

print_stats_median(data)

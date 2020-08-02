#!/usr/bin/env python3


# standard libraries
import logging

# rubiks cube libraries
from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, centers_444, edges_444, moves_444, rotate_444, solved_444

log = logging.getLogger(__name__)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)30s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    filename = "/home/dwalton/rubiks-cube/rubiks-cube-lookup-tables/lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt"
    filename_nn = filename + ".nn"
    cube = RubiksCube444(solved_444, "URFDLB")
    cube.cpu_mode = "normal"
    cube.lt_init()

    cube.re_init()
    # cube.nuke_corners()
    # cube.nuke_edges()

    for x in centers_444:
        if cube.state[x] == "D":
            cube.state[x] = "U"
        elif cube.state[x] == "R":
            cube.state[x] = "L"
        elif cube.state[x] == "B":
            cube.state[x] = "F"

    # BATCH_SIZE = 10000
    BATCH_SIZE = 10
    to_write = []
    to_write_count = 0
    original_state = cube.state[:]
    count = 0

    with open(filename_nn, "w") as fh_nn:

        # do 10000 random cubes for now
        for x in range(10000):
            cube.state = original_state[:]
            cube.randomize()
            cube.solution = []

            (_, UD_cost) = cube.lt_UD_centers_stage.ida_heuristic()
            (_, LR_cost) = cube.lt_LR_centers_stage.ida_heuristic()
            (_, FB_cost) = cube.lt_FB_centers_stage.ida_heuristic()
            cube.lt_ULFRBD_centers_stage.solve()
            steps_to_resolve_len = len(cube.solution)

            if steps_to_resolve_len <= 5:
                continue

            log.info("%s has len %d" % (" ".join(cube.solution), steps_to_resolve_len))

            nn_line = [UD_cost, LR_cost, FB_cost]
            nn_line.append(steps_to_resolve_len)

            to_write.append(",".join(map(str, nn_line)))
            to_write_count += 1

            if to_write_count >= BATCH_SIZE:
                log.info("*" * 50)
                fh_nn.write("\n".join(to_write) + "\n")
                fh_nn.flush()
                to_write = []
                to_write_count = 0

            if x and x % BATCH_SIZE == 0:
                log.info("{:,}".format(x))

        if to_write_count:
            fh_nn.write("\n".join(to_write) + "\n")
            fh_nn.flush()
            to_write = []
            to_write_count = 0

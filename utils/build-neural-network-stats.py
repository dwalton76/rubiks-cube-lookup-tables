#!/usr/bin/env python3


from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444, centers_444, edges_444
import logging

log = logging.getLogger(__name__)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)30s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    filename = "lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt"
    filename_nn = filename + ".nn"
    cube = RubiksCube444(solved_444, 'URFDLB')

    cube.re_init()
    cube.nuke_corners()
    cube.nuke_edges()

    for x in centers_444:
        if cube.state[x] == "D":
            cube.state[x] = "U"
        elif cube.state[x] == "R":
            cube.state[x] = "L"
        elif cube.state[x] == "B":
            cube.state[x] = "F"

    BATCH_SIZE = 10000
    to_write = []
    to_write_count = 0
    original_state = cube.state[:]
    count = 0

    with open(filename, "r") as fh:
        with open(filename_nn, "w") as fh_nn:
            for (line_number, line) in enumerate(fh):
                cube.state = original_state[:]
                cube.solution = []
                (state, steps_to_resolve) = line.rstrip().split(":")
                steps_to_resolve = steps_to_resolve.split()
                steps_to_scramble = reverse_steps(steps_to_resolve) 
                steps_to_resolve_len = len(steps_to_resolve)

                # Do not bother with depths 1 through 4
                if steps_to_resolve_len <= 4:
                    continue
                count += 1

                for step in steps_to_scramble:
                    cube.rotate(step)

                (centers_one_color, centers_horizontal_bars, centers_vertical_bars, centers_l_pattern, centers_single_horizontal_bar, centers_single_vertical_bar) = cube.centers_staged_stats()

                nn_line = [centers_one_color, centers_horizontal_bars, centers_vertical_bars, centers_l_pattern, centers_single_horizontal_bar, centers_single_vertical_bar]
                nn_line.append(steps_to_resolve_len)

                to_write.append(",".join(map(str, nn_line)))
                to_write_count += 1

                if to_write_count == BATCH_SIZE:
                    fh_nn.write("\n".join(to_write) + "\n")
                    to_write = []
                    to_write_count = 0

                #if steps_to_resolve_len == 5:
                #    log.info(" ".join(steps_to_scramble))
                #    cube.print_cube()

                if line_number % BATCH_SIZE == 0:
                    log.info("{:,}".format(line_number))

                #if count == 100000:
                #    break

            if to_write_count:
                fh_nn.write("\n".join(to_write) + "\n")
                to_write = []
                to_write_count = 0

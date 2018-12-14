#!/usr/bin/env python3


from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555, centers_555, edges_555, edges_recolor_pattern_555, wings_for_edges_pattern_555
from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver import reverse_steps

cube = RubiksCube555(solved_555, order='URFDLB')
cube.nuke_corners()


with open("foo.txt", "w") as fh:
    to_write = []
    to_write_count = 0
    BATCH_SIZE = 100000

    for move1 in moves_555:

        if "w" not in move1:
            continue

        cube.re_init()
        cube.rotate(move1)
        move1_cube_state = cube.state[:]
        move1_cube_solution = cube.solution[:]

        steps_to_solve = reverse_steps(cube.solution)
        centers_state = ''.join([cube.state[x] for x in centers_555])
        to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
        to_write_count += 1

        # took 600ms, found 612
        for move2 in moves_555:

            if steps_on_same_face_and_layer(move1, move2):
                continue

            cube.state = move1_cube_state[:]
            cube.solution = move1_cube_solution[:]
            cube.rotate(move2)
            move2_cube_state = cube.state[:]
            move2_cube_solution = cube.solution[:]

            steps_to_solve = reverse_steps(cube.solution)
            centers_state = ''.join([cube.state[x] for x in centers_555])
            to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
            to_write_count += 1


            # took 1.6s, found 20214
            for move3 in moves_555:

                if steps_on_same_face_and_layer(move2, move3):
                    continue

                cube.state = move2_cube_state[:]
                cube.solution = move2_cube_solution[:]
                cube.rotate(move3)
                move3_cube_state = cube.state[:]
                move3_cube_solution = cube.solution[:]

                steps_to_solve = reverse_steps(cube.solution)
                centers_state = ''.join([cube.state[x] for x in centers_555])
                to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                to_write_count += 1


                # took 32s (20x move3), found 667,080
                for move4 in moves_555:

                    if steps_on_same_face_and_layer(move3, move4):
                        continue

                    cube.state = move3_cube_state[:]
                    cube.solution = move3_cube_solution[:]
                    cube.rotate(move4)
                    move4_cube_state = cube.state[:]
                    move4_cube_solution = cube.solution[:]

                    steps_to_solve = reverse_steps(cube.solution)
                    centers_state = ''.join([cube.state[x] for x in centers_555])
                    to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                    to_write_count += 1

                    # took 17m 16s (32x move4), found 22,013,658
                    for move5 in moves_555:

                        if steps_on_same_face_and_layer(move4, move5):
                            continue

                        cube.state = move4_cube_state[:]
                        cube.solution = move4_cube_solution[:]
                        cube.rotate(move5)
                        move5_cube_state = cube.state[:]
                        move5_cube_solution = cube.solution[:]

                        steps_to_solve = reverse_steps(cube.solution)
                        centers_state = ''.join([cube.state[x] for x in centers_555])
                        to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                        to_write_count += 1

                        if to_write_count >= BATCH_SIZE:
                            fh.write("\n".join(to_write) + "\n")
                            fh.flush()
                            to_write = []
                            to_write_count = 0

    if to_write_count:
        fh.write("\n".join(to_write) + "\n")
        to_write_count = 0

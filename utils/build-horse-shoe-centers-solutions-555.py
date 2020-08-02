#!/usr/bin/env python3


# rubiks cube libraries
from rubikscubennnsolver import reverse_steps
from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    centers_555,
    edges_555,
    edges_recolor_pattern_555,
    rotate_555,
    solved_555,
    wings_for_edges_pattern_555,
)

cube = RubiksCube555(solved_555, order="URFDLB")
cube.nuke_corners()


legal_moves = (
    "U",
    "U'",
    "U2",
    "F2",
    "B2",
    "D2",
    "2L",
    "2L'",
    "2L2",
    "2R",
    "2R'",
    "2R2",
    # middle layer slice
    "3L",
    "3L'",
    "3L2",
    # BTM slices
    # "2-3Lw", "2-3Lw'", "2-3Lw2",
    # "2-3Rw", "2-3Rw'", "2-3Rw2",
    # "2-4Lw", "2-4Lw'", "2-4Lw2",
)


with open("horse_shoe_centers_solutions_555.txt.D-on-top", "w") as fh:
    to_write = []
    to_write_count = 0
    BATCH_SIZE = 100000

    for move1 in legal_moves:

        # Do not bother starting out with an outer layer move
        if move1 in ("U", "U'", "U2", "F2", "B2", "D2"):
            continue

        cube.re_init()

        # Put F on top
        # cube.rotate("x")

        # Put D on top
        cube.rotate("x")
        cube.rotate("x")

        # Put B on top
        # cube.rotate("x")
        # cube.rotate("x")
        # cube.rotate("x")

        cube.rotate(move1)
        move1_cube_state = cube.state[:]
        move1_cube_solution = cube.solution[:]

        steps_to_solve = reverse_steps(cube.solution)
        centers_state = "".join([cube.state[x] for x in centers_555])
        to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
        to_write_count += 1

        for move2 in legal_moves:

            if steps_on_same_face_and_layer(move1, move2):
                continue

            cube.state = move1_cube_state[:]
            cube.solution = move1_cube_solution[:]
            cube.rotate(move2)
            move2_cube_state = cube.state[:]
            move2_cube_solution = cube.solution[:]

            steps_to_solve = reverse_steps(cube.solution)
            centers_state = "".join([cube.state[x] for x in centers_555])
            to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
            to_write_count += 1

            for move3 in legal_moves:

                if steps_on_same_face_and_layer(move2, move3):
                    continue

                cube.state = move2_cube_state[:]
                cube.solution = move2_cube_solution[:]
                cube.rotate(move3)
                move3_cube_state = cube.state[:]
                move3_cube_solution = cube.solution[:]

                steps_to_solve = reverse_steps(cube.solution)
                centers_state = "".join([cube.state[x] for x in centers_555])
                to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                to_write_count += 1

                for move4 in legal_moves:

                    if steps_on_same_face_and_layer(move3, move4):
                        continue

                    cube.state = move3_cube_state[:]
                    cube.solution = move3_cube_solution[:]
                    cube.rotate(move4)
                    move4_cube_state = cube.state[:]
                    move4_cube_solution = cube.solution[:]

                    steps_to_solve = reverse_steps(cube.solution)
                    centers_state = "".join([cube.state[x] for x in centers_555])
                    to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                    to_write_count += 1

                    if to_write_count >= BATCH_SIZE:
                        fh.write("\n".join(to_write) + "\n")
                        fh.flush()
                        to_write = []
                        to_write_count = 0

                    # took 6s, found 53,286
                    for move5 in legal_moves:

                        if steps_on_same_face_and_layer(move4, move5):
                            continue

                        cube.state = move4_cube_state[:]
                        cube.solution = move4_cube_solution[:]
                        cube.rotate(move5)
                        move5_cube_state = cube.state[:]
                        move5_cube_solution = cube.solution[:]

                        steps_to_solve = reverse_steps(cube.solution)
                        centers_state = "".join([cube.state[x] for x in centers_555])
                        to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                        to_write_count += 1

                        if to_write_count >= BATCH_SIZE:
                            fh.write("\n".join(to_write) + "\n")
                            fh.flush()
                            to_write = []
                            to_write_count = 0

                        """
                        # took 52s, found 509,820
                        for move6 in legal_moves:

                            if steps_on_same_face_and_layer(move5, move6):
                                continue

                            cube.state = move5_cube_state[:]
                            cube.solution = move5_cube_solution[:]
                            cube.rotate(move6)
                            move6_cube_state = cube.state[:]
                            move6_cube_solution = cube.solution[:]

                            steps_to_solve = reverse_steps(cube.solution)
                            centers_state = ''.join([cube.state[x] for x in centers_555])
                            to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                            to_write_count += 1

                            if to_write_count >= BATCH_SIZE:
                                fh.write("\n".join(to_write) + "\n")
                                fh.flush()
                                to_write = []
                                to_write_count = 0

                            # took 8min, found 4,877,862
                            for move7 in legal_moves:

                                if steps_on_same_face_and_layer(move6, move7):
                                    continue

                                cube.state = move6_cube_state[:]
                                cube.solution = move6_cube_solution[:]
                                cube.rotate(move7)
                                move7_cube_state = cube.state[:]
                                move7_cube_solution = cube.solution[:]

                                steps_to_solve = reverse_steps(cube.solution)
                                centers_state = ''.join([cube.state[x] for x in centers_555])
                                to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                                to_write_count += 1

                                if to_write_count >= BATCH_SIZE:
                                    fh.write("\n".join(to_write) + "\n")
                                    fh.flush()
                                    to_write = []
                                    to_write_count = 0

                                # took 71 min, found 46,670,208 states
                                for move8 in legal_moves:

                                    if steps_on_same_face_and_layer(move7, move8):
                                        continue

                                    cube.state = move7_cube_state[:]
                                    cube.solution = move7_cube_solution[:]
                                    cube.rotate(move8)
                                    move8_cube_state = cube.state[:]
                                    move8_cube_solution = cube.solution[:]

                                    steps_to_solve = reverse_steps(cube.solution)
                                    centers_state = ''.join([cube.state[x] for x in centers_555])
                                    to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                                    to_write_count += 1

                                    if to_write_count >= BATCH_SIZE:
                                        fh.write("\n".join(to_write) + "\n")
                                        fh.flush()
                                        to_write = []
                                        to_write_count = 0

                                    # 9-deep
                                    # finished overnight...probably took 10 or 12 hours
                                    # found 446,529,606 states
                                    for move9 in legal_moves:

                                        if steps_on_same_face_and_layer(move8, move9):
                                            continue

                                        cube.state = move8_cube_state[:]
                                        cube.solution = move8_cube_solution[:]
                                        cube.rotate(move9)
                                        move9_cube_state = cube.state[:]
                                        move9_cube_solution = cube.solution[:]

                                        steps_to_solve = reverse_steps(cube.solution)
                                        centers_state = ''.join([cube.state[x] for x in centers_555])
                                        to_write.append("{}:{}".format(centers_state, " ".join(steps_to_solve)))
                                        to_write_count += 1


                                        if to_write_count >= BATCH_SIZE:
                                            fh.write("\n".join(to_write) + "\n")
                                            fh.flush()
                                            to_write = []
                                            to_write_count = 0
                        """

    if to_write_count:
        fh.write("\n".join(to_write) + "\n")
        to_write_count = 0

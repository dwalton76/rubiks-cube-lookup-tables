#!/usr/bin/env python3

# standard libraries
import logging
import os

# third party libraries
import click

# rubiks cube libraries
from rubikscubennnsolver.RubiksCube666 import (
    RubiksCube666,
    UFBD_inner_x_centers_666,
    UFBD_left_oblique_edges_666,
    UFBD_right_oblique_edges_666,
    solved_666,
)
from rubikscubennnsolver.RubiksCube777 import (
    RubiksCube777,
    UFBD_inner_t_centers_777,
    UFBD_inner_x_centers_777,
    UFBD_left_oblique_777,
    UFBD_middle_oblique_777,
    UFBD_right_oblique_777,
    solved_777,
)

logger = logging.getLogger(__name__)


@click.command()
@click.argument("file-in", type=str)
@click.option("--file-out", type=str, default=None, help="perfect hash filename")
def main(file_in: str, file_out: str) -> None:
    """
    \b
    Example:
        python ./utils/build-perfect-hash.py lookup-tables/lookup-table-6x6x6-step16-UD-left-oblique-inner-x-centers.txt
    """
    if not os.path.exists(file_in):
        raise FileNotFoundError(file_in)

    if file_out is None:
        file_out = file_in.replace(".txt", ".perfect-hash")

    if file_in.endswith("lookup-table-6x6x6-step16-UD-left-oblique-inner-x-centers.txt"):
        cube = RubiksCube666(solved_666, "URFDLB")
        cube.lt_init()

        lt_file_a = cube.lt_UD_inner_x_centers_stage
        lt_file_b = cube.lt_UD_left_oblique_edges_stage
        positions = sorted(list(UFBD_inner_x_centers_666) + list(UFBD_left_oblique_edges_666))

    elif file_in.endswith("lookup-table-6x6x6-step17-UD-right-oblique-inner-x-centers.txt"):
        cube = RubiksCube666(solved_666, "URFDLB")
        cube.lt_init()

        lt_file_a = cube.lt_UD_inner_x_centers_stage
        lt_file_b = cube.lt_UD_right_oblique_edges_stage
        positions = sorted(list(UFBD_inner_x_centers_666) + list(UFBD_right_oblique_edges_666))

    elif file_in.endswith("lookup-table-6x6x6-step15-UD-oblique-centers.txt"):
        cube = RubiksCube666(solved_666, "URFDLB")
        cube.lt_init()

        lt_file_a = cube.lt_UD_left_oblique_edges_stage
        lt_file_b = cube.lt_UD_right_oblique_edges_stage
        positions = sorted(list(UFBD_left_oblique_edges_666) + list(UFBD_right_oblique_edges_666))

    elif file_in.endswith("lookup-table-7x7x7-phase4-inner-centers.txt"):
        cube = RubiksCube777(solved_777, "URFDLB")
        cube.lt_init()

        lt_file_a = cube.lt_UD_inner_t_centers
        lt_file_b = cube.lt_UD_inner_x_centers
        positions = sorted(list(UFBD_inner_t_centers_777) + list(UFBD_inner_x_centers_777))

    elif file_in.endswith("lookup-table-7x7x7-phase5-left-right-oblique.txt"):
        cube = RubiksCube777(solved_777, "URFDLB")
        cube.lt_init()

        lt_file_a = cube.lt_phase5_left_oblique
        lt_file_b = cube.lt_phase5_right_oblique
        positions = sorted(list(UFBD_left_oblique_777) + list(UFBD_right_oblique_777))

    elif file_in.endswith("lookup-table-7x7x7-phase5-left-middle-oblique.txt"):
        cube = RubiksCube777(solved_777, "URFDLB")
        cube.lt_init()

        lt_file_a = cube.lt_phase5_left_oblique
        lt_file_b = cube.lt_phase5_middle_oblique
        positions = sorted(list(UFBD_left_oblique_777) + list(UFBD_middle_oblique_777))

    else:
        raise NotImplementedError(file_in)

    lt_file_a.load_state_index_cache()
    lt_file_b.load_state_index_cache()
    cube.nuke_corners()
    cube.nuke_edges()
    cube.nuke_centers()

    perfect_hash_size = lt_file_a.linecount * lt_file_b.linecount
    perfect_hash = ["0"] * perfect_hash_size
    logger.info(
        f"{file_out} will have {lt_file_a.linecount:,} x {lt_file_b.linecount:,} = {perfect_hash_size:,} entries"
    )

    with open(file_in, "r") as fh:
        for line_index, line in enumerate(fh):
            state, steps_to_solve = line.strip().split(":")
            steps_to_solve = steps_to_solve.split()

            # encode the cost in hex (max of 15 to limit to one character)
            cost = len(steps_to_solve)

            if cost >= 15:
                cost = "f"
            else:
                cost = hex(cost)[2:]

            # populate the cube.state per the state in the lookup table
            for (pos, pos_state) in zip(positions, state):
                cube.state[pos] = pos_state

            perfect_hash_index = (lt_file_a.state_index() * lt_file_b.linecount) + lt_file_b.state_index()
            perfect_hash[perfect_hash_index] = cost

            if line_index and line_index % 1000000 == 0:
                logger.info(f"{line_index:,}/{perfect_hash_size:,}")

    with open(file_out, "w") as fh:
        fh.write("".join(perfect_hash))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    main()

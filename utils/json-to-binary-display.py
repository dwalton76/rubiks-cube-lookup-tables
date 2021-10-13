#!/usr/bin/env python3

# standard libraries
import json
import logging
import os
import struct
from typing import Dict, List

# third party libraries
import click

log = logging.getLogger(__name__)

# fmt: off
moves_777 = (
    "U", "U'", "U2", "Uw", "Uw'", "Uw2", "3Uw", "3Uw'", "3Uw2",
    "L", "L'", "L2", "Lw", "Lw'", "Lw2", "3Lw", "3Lw'", "3Lw2",
    "F", "F'", "F2", "Fw", "Fw'", "Fw2", "3Fw", "3Fw'", "3Fw2",
    "R", "R'", "R2", "Rw", "Rw'", "Rw2", "3Rw", "3Rw'", "3Rw2",
    "B", "B'", "B2", "Bw", "Bw'", "Bw2", "3Bw", "3Bw'", "3Bw2",
    "D", "D'", "D2", "Dw", "Dw'", "Dw2", "3Dw", "3Dw'", "3Dw2",
)
# fmt: on


def print_node(
    states: Dict[int, str], legal_moves: List[str], ROW_LENGTH: int, bindata: bytes, state_index: int
) -> None:
    """
    Display the contents of a cube state in a .bin file
    """
    # The starting position of the data for the cube state we want to display
    i = state_index * ROW_LENGTH

    # cost takes 1 byte
    cost = bindata[i]
    i += 1

    state = states[state_index]
    title = f"state {state_index:06d} ({state}) cost {cost}"

    print(title)
    print("=" * len(title))

    for step in legal_moves:

        # the next state_index takes 4 bytes
        next_state_index = struct.unpack("<L", bindata[i : i + 4])[0]
        next_state = states[next_state_index]
        i += 4

        # cost takes 1 byte
        next_state_cost = bindata[i]
        i += 1

        print(f"{step:4s} -> {next_state_index:06d} ({next_state}) with cost {next_state_cost}")

    print("\n")


@click.command(context_settings={"show_default": True})
@click.argument("json-filename", type=str)
@click.argument("binary-filename", type=str)
@click.argument("to-display", type=str)
def main(json_filename: str, binary_filename: str, to_display: str) -> None:
    """
    Display the contents of a series of cube states in a .bin file

    \b
    Example:
        python utils/json-to-binary-display.py lookup-tables/lookup-table-4x4x4-step11-UD-centers-stage.json lookup-tables/lookup-table-4x4x4-step11-UD-centers-stage.bin 504670,504670,520941
    """
    assert json_filename.endswith(".json")
    assert binary_filename.endswith(".bin")
    to_display = list(map(int, to_display.split(",")))

    for filename in (json_filename, binary_filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} does not exist")

    log.info(f"load the JSON contents")
    with open(json_filename, "r") as fh:
        data = json.load(fh)

    log.info("build a dictionary that translates a state to its index among all states")
    states = sorted(data.keys())

    # extract a list of the moves that are encoded in the .bin file
    first_state = states[0]
    legal_moves = list(data[first_state]["edges"].keys())
    legal_moves_str = " ".join(legal_moves)
    legal_move_count = len(legal_moves)
    log.info(f"legal_moves {legal_moves_str}")
    log.info(f"legal_move_count {legal_move_count}")

    # calculate the number of bytes used to store each cube state
    COST_LENGTH = 1
    STATE_LENGTH = 4
    ROW_LENGTH = COST_LENGTH + ((STATE_LENGTH + COST_LENGTH) * legal_move_count)

    with open(binary_filename, "rb") as fh:
        bindata = fh.read()

    log.info(f"bindata is {len(bindata)} bytes / ROW_LENGTH {ROW_LENGTH} is {len(bindata) / ROW_LENGTH}\n")

    # display each cube state
    for state_index in to_display:
        print_node(states, legal_moves, ROW_LENGTH, bindata, state_index)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    main()

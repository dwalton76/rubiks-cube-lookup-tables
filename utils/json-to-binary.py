#!/usr/bin/env python3

# standard libraries
import json
import logging
import os
import struct
import sys

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


def convert_json_to_binary(filename: str, state_is_hex: bool) -> None:
    assert filename.endswith(".json")
    filename_state_index = filename.replace(".json", ".state_index")

    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist")
        sys.exit(1)

    log.info(f"load the json contents from {filename}")
    with open(filename, "r") as fh:
        data = json.load(fh)

    log.info("build a dictionary that translates a state to its index among all states")
    states = []
    state_to_index = {}

    with open(filename_state_index, "r") as fh:
        for line in fh:
            (state, state_index) = line.rstrip().split(":")
            state_to_index[state] = int(state_index)
            states.append(state)

    binary_filename = filename.replace(".json", ".bin")

    log.info(f"write {binary_filename}")
    with open(binary_filename, "wb") as fh:

        for (i, state) in enumerate(states):
            node = data[state]
            cost = node["cost"]
            edges = node["edges"]

            # write the cost_to_goal (1 byte)
            fh.write(struct.pack("B", cost))

            # write all of the step/next_state pairs
            for step in moves_777:
                next_state = edges.get(step)

                if next_state is not None:
                    next_state_index = state_to_index[next_state]
                    fh.write(struct.pack("<L", next_state_index))

                    next_node = data[next_state]
                    next_node_cost = next_node["cost"]
                    fh.write(struct.pack("B", next_node_cost))

            if i % 100000 == 0:
                log.info(f"{i:,}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    filename = sys.argv[1]
    convert_json_to_binary(filename, True)

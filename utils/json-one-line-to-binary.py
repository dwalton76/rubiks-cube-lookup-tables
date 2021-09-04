#!/usr/bin/env python3

# standard libraries
import logging
import os
import struct
import sys

log = logging.getLogger(__name__)
moves_777 = (
    "U",
    "U'",
    "U2",
    "Uw",
    "Uw'",
    "Uw2",
    "3Uw",
    "3Uw'",
    "3Uw2",
    "L",
    "L'",
    "L2",
    "Lw",
    "Lw'",
    "Lw2",
    "3Lw",
    "3Lw'",
    "3Lw2",
    "F",
    "F'",
    "F2",
    "Fw",
    "Fw'",
    "Fw2",
    "3Fw",
    "3Fw'",
    "3Fw2",
    "R",
    "R'",
    "R2",
    "Rw",
    "Rw'",
    "Rw2",
    "3Rw",
    "3Rw'",
    "3Rw2",
    "B",
    "B'",
    "B2",
    "Bw",
    "Bw'",
    "Bw2",
    "3Bw",
    "3Bw'",
    "3Bw2",
    "D",
    "D'",
    "D2",
    "Dw",
    "Dw'",
    "Dw2",
    "3Dw",
    "3Dw'",
    "3Dw2",
)


def convert_json_one_line_to_binary(filename: str, state_is_hex: bool) -> None:
    assert filename.endswith(".json-one-line")

    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist")
        sys.exit(1)

    # build a dictionary that translates a state to its index among all states
    log.info("load .state_index begin")
    state_index_filename = filename.replace(".json-one-line", ".state_index")
    state_to_index = {}

    with open(state_index_filename, "r") as fh:
        for line in fh:
            (state, state_index) = line.rstrip().split(":")
            state_to_index[state] = int(state_index)
    log.info("load .state_index end")

    binary_filename = filename.replace(".json-one-line", ".bin")

    with open(filename, "r") as fh:
        log.info("load data begin")
        data = eval(next(fh))
        log.info("load data end")

    with open(binary_filename, "wb") as fh_bin:
        count = 0

        for state, node in data.items():
            cost = node["cost"]
            edges = node["edges"]

            # write the cost_to_goal (1 byte)
            fh_bin.write(struct.pack(">B", cost))

            # write all of the step/next_state pairs
            for step in moves_777:
                next_state = edges.get(step)

                if next_state:
                    next_state_index = state_to_index[next_state]
                    fh_bin.write(struct.pack(">L", next_state_index))

                    next_node = data[next_state]
                    next_node_cost = next_node["cost"]
                    fh.write(struct.pack(">B", next_node_cost))

            count += 1

            if count % 10000 == 0:
                log.info(count)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    filename = sys.argv[1]
    convert_json_one_line_to_binary(filename, True)

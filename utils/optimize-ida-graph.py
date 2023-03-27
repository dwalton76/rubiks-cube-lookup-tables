#!/usr/bin/env python3

"""
./utils/json-to-binary.py will later be used to create a .bin file that contains the graph that
is stored in the .json file. It reads in the .json file and .state_index file and uses struct.pack()
to put the graph into a .bin file.  When the solver runs it will read that .bin into memory and will
traverse the graph in search of a path that takes the cube to the goal state.  The .bin will be
small enough to fit in RAM but it will be much too large to fit in the CPU cache.  If we can
construct the .bin in a way that increases the percentage of CPU cache hits that will allow the
solver to run faster.

I tried a few different ways of sorting the node before writing the graph to the .bin but could
never come up with anything that resulted in the solver running faster.
"""

# standard libraries
import argparse
import json
import logging
import os
import subprocess
from collections import deque
from typing import Dict, List

log = logging.getLogger(__name__)


def state_order_via_breadth_first_search(data: Dict, solved_state: str) -> List[str]:
    """
    I tried this for optimizing the 555 phase1 tables but it didn't move the needle at all
    """
    in_order = []
    visited = set()
    queue = deque([solved_state])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            in_order.append(node)
            # print(f"Visited: {node}, Cost: {graph[node]['cost']}")

            # Add connected nodes to the queue
            for edge in data[node]["edges"].values():
                if edge not in visited:
                    queue.append(edge)

    in_order = reversed(in_order)
    return in_order


def state_order_via_depth_first_search(data: Dict, solved_state: str) -> List[str]:
    """
    I tried this for optimizing the 555 phase1 tables but it didn't move the needle at
    all...it only reduced the cache misses by 0.5%
    """

    in_order = [solved_state]
    stack = [solved_state]
    explored_nodes = set()
    explored_nodes.add(solved_state)

    while stack:
        node = stack.pop()

        # log.info(f"node {node}, cost {data[node]['cost']}")
        for move, peer_node in data[node]["edges"].items():
            if peer_node not in explored_nodes:
                explored_nodes.add(peer_node)
                stack.append(peer_node)
                in_order.append(peer_node)

    in_order = reversed(in_order)
    return in_order


def main(filename_json: str, solved_state: str) -> None:
    if not filename_json.endswith(".json"):
        raise ValueError(f"{filename_json} must end with .json")

    if not os.path.exists(filename_json):
        raise FileNotFoundError(filename_json)

    with open(filename_json, mode="r", encoding="utf-8") as fh:
        log.info(f"begin load {filename_json}")
        data = json.load(fh)
        log.info(f"end load {filename_json}")

    # There isn't a definative optimal way to arrange the nodes in the .bin file, you could be starting
    # from any node so what would be optimal for one starting node would be sub-optimal for another.
    # Experiment with some different strategies here to see what works best.
    states_abc_order = sorted(data.keys())
    states_new_order = state_order_via_breadth_first_search(data, solved_state)
    # states_new_order = state_order_via_depth_first_search(data, solved_state)
    state_to_index = {}
    new_data = {}

    for index, state in enumerate(states_new_order):
        state_to_index[state] = index
        new_data[state] = data[state]

    # update the .state_index file
    filename_state_index = filename_json.replace(".json", ".state_index")

    with open(filename_state_index, mode="w", encoding="utf-8") as fh:
        for state in states_abc_order:
            fh.write(f"{state}:{state_to_index[state]}\n")

        fh.flush()
    subprocess.check_output(f"./utils/pad-lines.py {filename_state_index}", shell=True)

    # update the .json file
    with open(filename_json, mode="w", encoding="utf-8") as fh:
        json.dump(new_data, fh, indent=4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)24s %(levelname)8s: %(message)s")

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="The JSON file to process")
    parser.add_argument("solved_state", type=str, help="the state string of the solved cube")

    args = parser.parse_args()
    main(args.filename, args.solved_state)

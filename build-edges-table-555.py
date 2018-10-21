#!/usr/bin/env python3


from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, wings_for_edges_pattern_555, edges_recolor_pattern_555
from rubikscubennnsolver import reverse_steps
import json
import logging
import os
import subprocess
import sys


def get_outer_layer_steps():
    """
    Each of the cycles-outer-layer-XYZ1-deep.json contains a list
    of outer layer moves where we never perform two moves back-to-back
    on the same layer...so no U U2, D D', etc
    """

    with open("utils/cycles-outer-layer-1-deep.json", "r") as fh:
        outer_layer_1deep = json.load(fh)

    with open("utils/cycles-outer-layer-2-deep.json", "r") as fh:
        outer_layer_2deep = json.load(fh)

    with open("utils/cycles-outer-layer-3-deep.json", "r") as fh:
        outer_layer_3deep = json.load(fh)

    with open("utils/cycles-outer-layer-4-deep.json", "r") as fh:
        outer_layer_4deep = json.load(fh)

    with open("utils/cycles-outer-layer-5-deep.json", "r") as fh:
        outer_layer_5deep = json.load(fh)

    #with open("utils/cycles-outer-layer-6-deep.json", "r") as fh:
    #    outer_layer_6deep = json.load(fh)

    outer_layer_steps =\
        outer_layer_1deep +\
        outer_layer_2deep +\
        outer_layer_3deep
        # outer_layer_4deep +\
        # outer_layer_5deep +\
        # outer_layer_6deep
    outer_layer_steps.append([])

    return outer_layer_steps


# sanity check what we built
def sanity_check(filename):
    """
    Sanity check the contents of the edges table we just built
    """

    with open(filename, "r") as fh:
        for line in fh:
            (lt_edges_state, steps_to_solve) = line.strip().split(":")
            steps_to_solve = steps_to_solve.split()
            steps_to_scramble = reverse_steps(steps_to_solve)
            cube.re_init()

            for step in steps_to_scramble:
                cube.rotate(step)

            state = edges_recolor_pattern_555(cube.state[:])
            edges_state = ''.join([state[index] for index in wings_for_edges_pattern_555])
            assert edges_state == lt_edges_state, "{} != {}".format(edges_state, lt_edges_state)

            #log.info("steps_to_scramble: {}".format(steps_to_scramble))
            #log.info(edges_state)
            #cube.print_cube()

            for step in steps_to_solve:
                cube.rotate(step)

            state = edges_recolor_pattern_555(cube.state[:])
            edges_state = ''.join([state[index] for index in wings_for_edges_pattern_555])

            #log.info("steps_to_solve: {}".format(steps_to_solve))
            #log.info(edges_state)
            #cube.print_cube()

            # OOopPPQQqrRRsSSTTtuUUVVvWWwxXXYYyzZZ
            assert cube.centers_solved(), "centers should be solved but are not"
            assert cube.edges_paired(), "edges should be paired but are not"
            #break


def get_cycle_steps():
    """
    Each of the cycles*.txt files will contain a three phase seq
    phase1 - some wide turn
    phase2 - three or more outer layer turns
    phase3 - a wide turn to bring the centers back to solved
    """
    results = []

    with open("utils/cycles-5-deep.txt", "r") as fh:
        for line in fh:
            steps_in_cycle = line.strip().split()
            results.append(steps_in_cycle)

    with open("utils/cycles-6-deep.txt", "r") as fh:
        for line in fh:
            steps_in_cycle = line.strip().split()
            results.append(steps_in_cycle)

    return results


def keep_best_solutions(filename):
    """
    filename will contain multiple entries for a given edges_state, keep
    the line for each edges_state that has the shortest solution
    """
    filename_final = filename + ".final"
    edges_state_min_solution_len = None
    edges_state_min_solution = None
    prev_edges_state = None

    with open(filename_final, "w") as fh_final:
        with open(filename, "r") as fh:
            for line in fh:
                (edges_state, steps_to_solve) = line.strip().split(":")
                solution_len = len(steps_to_solve.split())

                if prev_edges_state is not None and edges_state != prev_edges_state:
                    fh_final.write("%s:%s\n" % (prev_edges_state, edges_state_min_solution))
                    edges_state_min_solution_len = None
                    edges_state_min_solution = None

                if edges_state_min_solution_len is None or solution_len < edges_state_min_solution_len:
                    edges_state_min_solution_len = solution_len
                    edges_state_min_solution = steps_to_solve
                
                prev_edges_state = edges_state
            fh_final.write("%s:%s\n" % (prev_edges_state, edges_state_min_solution))

    os.rename(filename_final, filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)20s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    # Color the errors and warnings in red
    logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

    # outer_layer_steps will be a list of outer layer moves where
    # we never perform two moves back-to-back on the same layer...so
    # no U U2, D D', etc
    outer_layer_steps = get_outer_layer_steps()
    log.info("{:,} outer layer sequences".format(len(outer_layer_steps)))

    cycle_steps = get_cycle_steps()
    log.info("{:,} cycle sequences".format(len(cycle_steps)))

    index_target = len(outer_layer_steps) * len(cycle_steps)

    results_filename = "lookup-table-555-step800-edges.txt"
    cube = RubiksCube555(solved_555, 'URFDLB')

    with open(results_filename, "w") as fh:
        index = 0
        to_write = []
        to_write_count = 0
        BATCH_SIZE = 100000

        for steps_in_cycle in cycle_steps:
            for outer_steps in outer_layer_steps:
                cube.re_init()
                steps_to_solve = outer_steps + steps_in_cycle
                steps_to_scramble = reverse_steps(steps_to_solve)

                for step in steps_to_scramble:
                    cube.rotate(step)

                #assert cube.centers_solved(), "centers should be solved but are not"
                state = edges_recolor_pattern_555(cube.state[:])
                edges_state = ''.join([state[index] for index in wings_for_edges_pattern_555])

                to_write.append("%s:%s" % (edges_state, " ".join(steps_to_solve)))
                to_write_count += 1
                index += 1

                if to_write_count >= BATCH_SIZE:
                    fh.write("\n".join(to_write) + "\n")
                    to_write = []
                    to_write_count = 0
                    log.info("{:,}/{:,}".format(index, index_target))
                    break

            if index >= BATCH_SIZE:
                break

    subprocess.check_output("LC_ALL=C sort --temporary-directory=./tmp/ --output %s %s " %
        (results_filename, results_filename), shell=True)
    #sanity_check(results_filename)

    keep_best_solutions(results_filename)
    subprocess.check_output("./utils/pad-lines.py %s" % results_filename, shell=True)

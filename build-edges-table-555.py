#!/usr/bin/env python3


from rubikscubennnsolver.LookupTable import steps_cancel_out, steps_on_same_face_and_layer
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, wings_for_edges_pattern_555, edges_recolor_pattern_555, rotate_555
from rubikscubennnsolver import reverse_steps
import json
import logging
import os
import subprocess
import sys

def file_line_count(filename):
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename) as fh:
            for (i, l) in enumerate(fh):
                pass
        return i + 1
    else:
        return 0


def get_outer_layer_steps():
    """
    Each of the cycles-outer-layer-XYZ1-deep.json contains a list
    of outer layer moves where we never perform two moves back-to-back
    on the same layer...so no U U2, D D', etc

    1-deep : 18 sequences
    2-deep : 270 sequences
    3-deep : 4,050 sequences
    4-deep : 60,750 sequences
    5-deep : 911,250 sequences
    6-deep : 13,668,750 sequences
    """

    # 2-deep x the number of cycles we have yeilds a 1G file with 15 million entries...we just cannot go any deeper or the file size will get out of control
    with open("utils/cycles-outer-layer-1-deep.json", "r") as fh:
        outer_layer_1deep = json.load(fh)

    #with open("utils/cycles-outer-layer-2-deep.json", "r") as fh:
    #    outer_layer_2deep = json.load(fh)

    #with open("utils/cycles-outer-layer-3-deep.json", "r") as fh:
    #    outer_layer_3deep = json.load(fh)

    #with open("utils/cycles-outer-layer-4-deep.json", "r") as fh:
    #    outer_layer_4deep = json.load(fh)

    #with open("utils/cycles-outer-layer-5-deep.json", "r") as fh:
    #    outer_layer_5deep = json.load(fh)

    #with open("utils/cycles-outer-layer-6-deep.json", "r") as fh:
    #    outer_layer_6deep = json.load(fh)

    outer_layer_steps = []
    #outer_layer_steps = outer_layer_1deep
    #outer_layer_steps += outer_layer_2deep
    #outer_layer_steps += outer_layer_3deep
    #outer_layer_steps += outer_layer_4deep
    #outer_layer_steps += outer_layer_5deep
    #outer_layer_steps += outer_layer_6deep
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
                #cube.rotate(step)
                cube.state = rotate_555(cube.state[:], step)

            state = edges_recolor_pattern_555(cube.state[:])
            edges_state = ''.join([state[index] for index in wings_for_edges_pattern_555])
            assert edges_state == lt_edges_state, "{} != {}".format(edges_state, lt_edges_state)

            #log.info("steps_to_scramble: {}".format(steps_to_scramble))
            #log.info(edges_state)
            #cube.print_cube()

            for step in steps_to_solve:
                #cube.rotate(step)
                cube.state = rotate_555(cube.state[:], step)

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
    cycles = []

    for filename in (
            "utils/cycles-5-deep.txt",
            "utils/cycles-6-deep.txt",
            "utils/cycles-7-deep.txt",
            "utils/cycles-8-deep.txt",
        ):

        with open(filename, "r") as fh:
            for line in fh:
                steps_in_cycle = line.strip()
                cycles.append(steps_in_cycle)

    with open("lookup-table-5x5x5-step900-edges.txt", "r") as fh:
        for line in fh:
            (_state, steps_in_cycle) = line.strip().split(":")
            cycles.append(steps_in_cycle)

    cycles = list(set(cycles))

    results = []
    for x in cycles:
        results.append(x.split())

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

    cube = RubiksCube555(solved_555, 'URFDLB')
    step800_filename = "lookup-table-555-step800-edges.txt"

    if not os.path.exists(step800_filename):
        cycle_steps = get_cycle_steps()
        log.info("{:,} cycle sequences".format(len(cycle_steps)))
        index_target = len(cycle_steps)

        with open(step800_filename, "w") as fh:
            index = 0
            to_write = []
            to_write_count = 0
            BATCH_SIZE = 100000

            for steps_to_solve in cycle_steps:
                cube.re_init()
                steps_to_scramble = reverse_steps(steps_to_solve)

                for step in steps_to_scramble:
                    cube.state = rotate_555(cube.state[:], step)

                cube.edges_flip_to_original_orientation()
                #assert cube.centers_solved(), "centers should be solved but are not"
                state = edges_recolor_pattern_555(cube.state[:], uppercase_paired_edges=False)
                edges_state = ''.join([state[index] for index in wings_for_edges_pattern_555])

                to_write.append("%s:%s" % (edges_state, " ".join(steps_to_solve)))
                to_write_count += 1
                index += 1

                if to_write_count >= BATCH_SIZE:
                    fh.write("\n".join(to_write) + "\n")
                    to_write = []
                    to_write_count = 0
                    log.info("{:,}/{:,}".format(index, index_target))

            if to_write_count:
                fh.write("\n".join(to_write) + "\n")
                to_write = []
                to_write_count = 0
                log.info("{:,}/{:,}".format(index, index_target))

        subprocess.check_output("LC_ALL=C sort --temporary-directory=./tmp/ --output %s %s " %
            (step800_filename, step800_filename), shell=True)
        #sanity_check(step800_filename)

        keep_best_solutions(step800_filename)
        subprocess.check_output("./utils/pad-lines.py %s" % step800_filename, shell=True)


    step810_filename = "lookup-table-555-step810-edges.txt"

    if not os.path.exists(step810_filename):
        # outer_layer_steps will be a list of outer layer moves where
        # we never perform two moves back-to-back on the same layer...so
        # no U U2, D D', etc
        outer_layer_steps = get_outer_layer_steps()
        log.info("{:,} outer layer sequences".format(len(outer_layer_steps)))

        cycle_count = file_line_count(step800_filename)
        log.info("{:,} cycle sequences".format(cycle_count))

        index_target = len(outer_layer_steps) * cycle_count
        log.info("{:,} outer layer + cycle combos".format(index_target))

        with open(step800_filename, "r") as fh_read:
            with open(step810_filename, "w") as fh:
                index = 0
                to_write = []
                to_write_count = 0
                BATCH_SIZE = 100000

                for line in fh_read:
                    (_state, steps_in_cycle) = line.strip().split(":")
                    steps_in_cycle = steps_in_cycle.split()

                    for outer_steps in outer_layer_steps:
                        cube.re_init()
                        steps_to_solve = outer_steps + steps_in_cycle
                        steps_to_scramble = reverse_steps(steps_to_solve)

                        for step in steps_to_scramble:
                            cube.state = rotate_555(cube.state[:], step)

                        cube.edges_flip_to_original_orientation()
                        #assert cube.centers_solved(), "centers should be solved but are not"
                        state = edges_recolor_pattern_555(cube.state[:], uppercase_paired_edges=False)
                        edges_state = ''.join([state[index] for index in wings_for_edges_pattern_555])

                        to_write.append("%s:%s" % (edges_state, " ".join(steps_to_solve)))
                        to_write_count += 1
                        index += 1

                        if to_write_count >= BATCH_SIZE:
                            fh.write("\n".join(to_write) + "\n")
                            to_write = []
                            to_write_count = 0
                            log.info("{:,}/{:,}".format(index, index_target))

                if to_write_count:
                    fh.write("\n".join(to_write) + "\n")
                    to_write = []
                    to_write_count = 0
                    log.info("{:,}/{:,}".format(index, index_target))

        subprocess.check_output("LC_ALL=C sort --temporary-directory=./tmp/ --output %s %s " %
            (step810_filename, step810_filename), shell=True)
        #sanity_check(step810_filename)

        keep_best_solutions(step810_filename)
        subprocess.check_output("./utils/pad-lines.py %s" % step810_filename, shell=True)

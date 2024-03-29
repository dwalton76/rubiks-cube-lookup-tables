#!/usr/bin/env python3

# standard libraries
import argparse
import datetime as dt
import importlib
import logging
import shutil

# rubiks cube libraries
from rubikscubelookuptables.buildercore import FAST_TMP, SLOW_TMP


def get_class(kls):
    """
    Given a string that is the name of a class, import and return that class
    """
    m = None
    print(kls)

    if "777" in kls:
        m = importlib.import_module("rubikscubelookuptables.builder777")
    elif "666" in kls:
        m = importlib.import_module("rubikscubelookuptables.builder666")
    elif "555" in kls:
        m = importlib.import_module("rubikscubelookuptables.builder555")
    elif "444" in kls:
        m = importlib.import_module("rubikscubelookuptables.builder444")
    elif "333" in kls:
        m = importlib.import_module("rubikscubelookuptables.builder333")
    elif "222" in kls:
        m = importlib.import_module("rubikscubelookuptables.builder222")
    else:
        raise Exception("we should not be here")

    m = getattr(m, kls)
    return m


start_time = dt.datetime.now()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)24s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, f"[91m   {logging.getLevelName(logging.ERROR)}[0m")
logging.addLevelName(logging.WARNING, f"[91m {logging.getLevelName(logging.WARNING)}[0m")

parser = argparse.ArgumentParser()
parser.add_argument("type", type=str, help="The type of lookup table to build")
parser.add_argument("--depth", type=int, default=99, help="The number of moves deep to explore")
parser.add_argument("--cores", type=int, default=4, help="The number of cores to use")
parser.add_argument("--code-gen", default=False, action="store_true", help="Print python classes for IDA")
args = parser.parse_args()
builder = get_class(args.type)()

if SLOW_TMP == FAST_TMP:
    if not FAST_TMP.exists():
        FAST_TMP.mkdir(parents=True, exist_ok=False)
else:
    if FAST_TMP:
        if FAST_TMP.exists():
            shutil.rmtree(FAST_TMP)
        FAST_TMP.mkdir(parents=True, exist_ok=False)

    if not SLOW_TMP.exists():
        SLOW_TMP.mkdir(parents=True, exist_ok=False)

log.info("")
log.info("")
log.info("")
log.info("************************************")
log.info(args.type)
log.info("************************************")

if args.code_gen:
    builder.code_gen()
else:
    builder.search(args.depth, args.cores)
    # builder.search_new(args.depth, args.cores)

    if args.type.startswith("Starting"):
        builder.save_starting_states()
    else:
        builder.save()

    end_time = dt.datetime.now()

    total_time = int((end_time - start_time).total_seconds())

    # Avoid divide by 0 if this ran in less than 1s
    if total_time == 0:
        total_time = 1

    accounted_time = (
        builder.time_in_sort
        + builder.time_in_file_delete
        + builder.time_in_building_workq
        + builder.time_in_crunching_workq
        + builder.time_in_save
        + builder.time_in_find_new_states
        + builder.time_in_keep_best_solution
    )
    unaccounted_time = total_time - accounted_time

    print("")
    print(
        "Time in crunching workq    : %ds (%d%%)"
        % (builder.time_in_crunching_workq, (builder.time_in_crunching_workq / total_time) * 100)
    )
    print("Time in sort               : %ds (%d%%)" % (builder.time_in_sort, (builder.time_in_sort / total_time) * 100))
    print(
        "Time in file delete        : %ds (%d%%)"
        % (builder.time_in_file_delete, (builder.time_in_file_delete / total_time) * 100)
    )

    if builder.time_in_keep_best_solution:
        print(
            "Time in keep-best-solution : %ds (%d%%)"
            % (builder.time_in_keep_best_solution, (builder.time_in_keep_best_solution / total_time) * 100)
        )

    print(
        "Time in find-new-states    : %ds (%d%%)"
        % (builder.time_in_find_new_states, (builder.time_in_find_new_states / total_time) * 100)
    )
    print(
        "Time in building workq     : %ds (%d%%)"
        % (builder.time_in_building_workq, (builder.time_in_building_workq / total_time) * 100)
    )
    print("Time in save               : %ds (%d%%)" % (builder.time_in_save, (builder.time_in_save / total_time) * 100))
    print("Time not accounted for     : %ds (%d%%)" % (unaccounted_time, (unaccounted_time / total_time) * 100))
    print("Time total                 : %ds" % total_time)
    print("")

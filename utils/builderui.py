#!/usr/bin/env python3

# standard libraries
import argparse
import datetime as dt
import importlib
import logging
import shutil

# rubiks cube libraries
from rubikscubelookuptables.buildercore import LOOKUP_TABLE_DIR, TMPDIR


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
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)24s:%(lineno)-4d %(levelname)8s: %(message)s")
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

# Start every build with an empty tmp directory
if TMPDIR.exists():
    shutil.rmtree(TMPDIR)
TMPDIR.mkdir(parents=True, exist_ok=False)

if not LOOKUP_TABLE_DIR.exists():
    LOOKUP_TABLE_DIR.mkdir(parents=True, exist_ok=False)

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

    # Keep this as a float. Truncating it to a whole second used to make the report look
    # like it was missing up to a second of work.
    total_time = (end_time - start_time).total_seconds()

    # Avoid divide by 0 if this ran in almost no time at all
    if total_time == 0:
        total_time = 1

    # Each of these covers a section of the build that does not overlap any of the others,
    # so they add up to the time we can account for
    rows = [
        ("Time in crunching workq", builder.time_in_crunching_workq),
        ("Time in sort", builder.time_in_sort),
        ("Time in file delete", builder.time_in_file_delete),
    ]

    if builder.time_in_keep_best_solution:
        rows.append(("Time in keep-best-solution", builder.time_in_keep_best_solution))

    rows.append(("Time in find-new-states", builder.time_in_find_new_states))
    rows.append(("Time in building workq", builder.time_in_building_workq))
    rows.append(("Time in save", builder.time_in_save))

    accounted_time = sum(seconds for (_, seconds) in rows)
    rows.append(("Time not accounted for", total_time - accounted_time))

    print("")

    for label, seconds in rows:
        print("%-27s: %6.1fs (%d%%)" % (label, seconds, (seconds / total_time) * 100))

    print("%-27s: %6.1fs" % ("Time total", total_time))
    print("")

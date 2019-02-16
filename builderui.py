#!/usr/bin/env python3

import datetime as dt
import argparse
import logging
import sys

def get_class( kls ):
    """
    Given a string that is the name of a class, import and return that class
    """
    m = None

    if '444' in kls:
        m = __import__('builder444')
    elif '333' in kls:
        m = __import__('builder333')
    elif '555' in kls:
        m = __import__('builder555')
    elif '666' in kls:
        m = __import__('builder666')
    elif '777' in kls:
        m = __import__('builder777')
    elif '222' in kls:
        m = __import__('builder222')
    else:
        raise Exception("we should not be here")

    m = getattr(m, kls)
    return m


start_time = dt.datetime.now()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

parser = argparse.ArgumentParser()
parser.add_argument('type', type=str, help='The type of lookup table to build')
parser.add_argument('--depth', type=int, default=None, help='The number of moves deep to explore')
parser.add_argument('--cores', type=int, default=4, help='The number of cores to use')
parser.add_argument('--code-gen', default=False, action='store_true', help='Print python classes for IDA')
args = parser.parse_args()

builder = get_class(args.type)()

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

    if args.type.startswith('Starting'):
        builder.save_starting_states()
    else:
        builder.save()

    end_time = dt.datetime.now()

    total_time = int((end_time - start_time).total_seconds())

    # Avoid divide by 0 if this ran in less than 1s
    if total_time == 0:
        total_time = 1

    accounted_time =\
        builder.time_in_sort +\
        builder.time_in_building_workq +\
        builder.time_in_crunching_workq +\
        builder.time_in_save +\
        builder.time_in_find_new_states
    unaccounted_time = total_time - accounted_time

    print("")
    print("Time in crunching workq : %ds (%d%%)" % (builder.time_in_crunching_workq, (builder.time_in_crunching_workq / total_time) * 100))
    print("Time in sort            : %ds (%d%%)" % (builder.time_in_sort, (builder.time_in_sort / total_time) * 100))
    print("Time in find-new-states : %ds (%d%%)" % (builder.time_in_find_new_states, (builder.time_in_find_new_states / total_time) * 100))
    print("Time in building workq  : %ds (%d%%)" % (builder.time_in_building_workq, (builder.time_in_building_workq / total_time) * 100))
    print("Time in save            : %ds (%d%%)" % (builder.time_in_save, (builder.time_in_save / total_time) * 100))
    print("Time not accounted for  : %ds (%d%%)" % (unaccounted_time, (unaccounted_time / total_time) * 100))
    print("Time total              : %ds" % total_time)
    print("")

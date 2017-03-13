#!/usr/bin/env python3

from builder444 import (
    StartingStates444UDCentersStage,
    StartingStates444LRCentersStage,
    StartingStates444FBCentersStage,
    StartingStates444ULFRBDCentersStage,
    Build444UDCentersStage,
    Build444LRCentersStage,
    Build444FBCentersStage,
    Build444ULFRBDCentersStage,
    Build444TsaiPhase1Centers,
    Build444TsaiPhase2Centers,
    Build444TsaiPhase2EdgesAndLRCenters,
    StartingStates444TsaiPhase4SolveEdges64,
    Build444TsaiPhase4SolveEdges64,
    StartingStates444TsaiPhase4SolveCorners64,
    Build444TsaiPhase4SolveCorners64,
)
from builder666 import (
    StartingStates666UDObliqueEdgesStage,
    Build666UDObliqueEdgesStage,

    StartingStates666UDObliqueEdgesStageLeftOnly,
    Build666UDObliqueEdgesStageLeftOnly,

    StartingStates666UDObliqueEdgesStageRightOnly,
    Build666UDObliqueEdgesStageRightOnly,

    Build666LFRBInnerXCenterAndObliqueEdges,
    Build666LRInnerXCenterAndObliqueEdges,
    StartingStates666Step60,
    StartingStates666Step61,
)
from builder777 import (
    Build777StageLRObliqueEdges,
    Build777StageLRObliqueEdges31,
    Build777Step80,
    Build777Step81,
    Build777Step90,
    Build777Step91,
)
import datetime as dt
import argparse
import logging
import sys


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
args = parser.parse_args()

# =====
# 4x4x4
# =====
if args.type == 'ss4x4x4-UD-centers-stage':
    builder = StartingStates444UDCentersStage()

elif args.type == '4x4x4-UD-centers-stage':
    builder = Build444UDCentersStage()

elif args.type == 'ss4x4x4-LR-centers-stage':
    builder = StartingStates444LRCentersStage()

elif args.type == '4x4x4-LR-centers-stage':
    builder = Build444LRCentersStage()

elif args.type == 'ss4x4x4-FB-centers-stage':
    builder = StartingStates444FBCentersStage()

elif args.type == '4x4x4-FB-centers-stage':
    builder = Build444FBCentersStage()

elif args.type == 'ss4x4x4-ULFRBD-centers-stage':
    builder = StartingStates444ULFRBDCentersStage()

elif args.type == '4x4x4-ULFRBD-centers-stage':
    builder = Build444ULFRBDCentersStage()

elif args.type == '4x4x4-tsai-phase1-centers':
    builder = Build444TsaiPhase1Centers()

elif args.type == '4x4x4-tsai-phase2-centers':
    builder = Build444TsaiPhase2Centers()

elif args.type == '4x4x4-tsai-phase2-edges-and-LR-centers':
    builder = Build444TsaiPhase2EdgesAndLRCenters()

elif args.type == 'ss4x4x4-tsai-phase4-edges64':
    builder = StartingStates444TsaiPhase4SolveEdges64()

elif args.type == '4x4x4-tsai-phase4-edges64':
    builder = Build444TsaiPhase4SolveEdges64()

elif args.type == 'ss4x4x4-tsai-phase4-corners64':
    builder = StartingStates444TsaiPhase4SolveCorners64()

elif args.type == '4x4x4-tsai-phase4-corners64':
    builder = Build444TsaiPhase4SolveCorners64()


# =====
# 6x6x6
# =====
elif args.type == 'ss6x6x6-UD-oblique-edges-stage':
    builder = StartingStates666UDObliqueEdgesStage()

elif args.type == '6x6x6-UD-oblique-edges-stage':
    builder = Build666UDObliqueEdgesStage()

elif args.type == 'ss6x6x6-UD-oblique-edges-stage-left-only':
    builder = StartingStates666UDObliqueEdgesStageLeftOnly()

elif args.type == '6x6x6-UD-oblique-edges-stage-left-only':
    builder = Build666UDObliqueEdgesStageLeftOnly()

elif args.type == 'ss6x6x6-UD-oblique-edges-stage-right-only':
    builder = StartingStates666UDObliqueEdgesStageRightOnly()

elif args.type == '6x6x6-UD-oblique-edges-stage-right-only':
    builder = Build666UDObliqueEdgesStageRightOnly()

elif args.type == '6x6x6-LFRB-solve-inner-x-center-and-oblique-edges':
    builder = Build666LFRBInnerXCenterAndObliqueEdges()

elif args.type == '6x6x6-LR-solve-inner-x-center-and-oblique-edges':
    builder = Build666LRInnerXCenterAndObliqueEdges()


# =====
# 7x7x7
# =====
elif args.type == '7x7x7-step30':
    builder = Build777StageLRObliqueEdges()

elif args.type == '7x7x7-step31':
    builder = Build777StageLRObliqueEdges31()

elif args.type == '7x7x7-step80':
    builder = Build777Step80()

elif args.type == '7x7x7-step81':
    builder = Build777Step81()

elif args.type == '7x7x7-step90':
    builder = Build777Step90()

elif args.type == '7x7x7-step91':
    builder = Build777Step91()

else:
    print("ERROR: %s is not a supported type" % args.type)
    sys.exit(1)

builder.search(args.depth, args.cores)

if args.type.startswith('ss'):
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

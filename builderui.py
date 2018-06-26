#!/usr/bin/env python3

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
    from builder444 import StartingStates444UDCentersStage
    builder = StartingStates444UDCentersStage()

elif args.type == '4x4x4-UD-centers-stage':
    from builder444 import Build444UDCentersStage
    builder = Build444UDCentersStage()

elif args.type == 'ss4x4x4-LR-centers-stage':
    from builder444 import StartingStates444LRCentersStage
    builder = StartingStates444LRCentersStage()

elif args.type == '4x4x4-LR-centers-stage':
    from builder444 import Build444LRCentersStage
    builder = Build444LRCentersStage()

elif args.type == 'ss4x4x4-FB-centers-stage':
    from builder444 import StartingStates444FBCentersStage
    builder = StartingStates444FBCentersStage()

elif args.type == '4x4x4-FB-centers-stage':
    from builder444 import Build444FBCentersStage
    builder = Build444FBCentersStage()

elif args.type == 'ss4x4x4-ULFRBD-centers-stage':
    from builder444 import StartingStates444ULFRBDCentersStage
    builder = StartingStates444ULFRBDCentersStage()

elif args.type == '4x4x4-ULFRBD-centers-stage':
    from builder444 import Build444ULFRBDCentersStage
    builder = Build444ULFRBDCentersStage()

elif args.type == '4x4x4-tsai-phase1-centers':
    from builder444 import Build444TsaiPhase1Centers
    builder = Build444TsaiPhase1Centers()

elif args.type == '4x4x4-tsai-phase2-centers':
    from builder444 import Build444TsaiPhase2Centers
    builder = Build444TsaiPhase2Centers()

elif args.type == '4x4x4-tsai-phase2-edges-and-LR-centers':
    from builder444 import Build444TsaiPhase2EdgesAndLRCenters
    builder = Build444TsaiPhase2EdgesAndLRCenters()

elif args.type == 'ss4x4x4-tsai-phase4-edges64':
    from builder444 import StartingStates444TsaiPhase4SolveEdges64
    builder = StartingStates444TsaiPhase4SolveEdges64()

elif args.type == '4x4x4-tsai-phase4-edges64':
    from builder444 import Build444TsaiPhase4SolveEdges64
    builder = Build444TsaiPhase4SolveEdges64()

elif args.type == 'ss4x4x4-tsai-phase4-corners64':
    from builder444 import StartingStates444TsaiPhase4SolveCorners64
    builder = StartingStates444TsaiPhase4SolveCorners64()

elif args.type == '4x4x4-tsai-phase4-corners64':
    from builder444 import Build444TsaiPhase4SolveCorners64
    builder = Build444TsaiPhase4SolveCorners64()

elif args.type == '4x4x4-tsai-phase4':
    from builder444 import Build444TsaiPhase4
    builder = Build444TsaiPhase4()


# =====
# 6x6x6
# =====
elif args.type == 'ss6x6x6-UD-oblique-edges-stage':
    from builder666 import StartingStates666UDObliqueEdgesStage
    builder = StartingStates666UDObliqueEdgesStage()

elif args.type == '6x6x6-UD-oblique-edges-stage':
    from builder666 import Build666UDObliqueEdgesStage
    builder = Build666UDObliqueEdgesStage()

elif args.type == 'ss6x6x6-UD-oblique-edges-stage-left-only':
    from builder666 import StartingStates666UDObliqueEdgesStageLeftOnly
    builder = StartingStates666UDObliqueEdgesStageLeftOnly()

elif args.type == '6x6x6-UD-oblique-edges-stage-left-only':
    from builder666 import Build666UDObliqueEdgesStageLeftOnly
    builder = Build666UDObliqueEdgesStageLeftOnly()

elif args.type == 'ss6x6x6-UD-oblique-edges-stage-right-only':
    from builder666 import StartingStates666UDObliqueEdgesStageRightOnly
    builder = StartingStates666UDObliqueEdgesStageRightOnly()

elif args.type == '6x6x6-UD-oblique-edges-stage-right-only':
    from builder666 import Build666UDObliqueEdgesStageRightOnly
    builder = Build666UDObliqueEdgesStageRightOnly()

elif args.type == '6x6x6-LFRB-solve-inner-x-center-and-oblique-edges':
    from builder666 import Build666LFRBInnerXCenterAndObliqueEdges
    builder = Build666LFRBInnerXCenterAndObliqueEdges()

elif args.type == '6x6x6-LR-solve-inner-x-center-and-oblique-edges':
    from builder666 import Build666LRInnerXCenterAndObliqueEdges
    builder = Build666LRInnerXCenterAndObliqueEdges()


# =====
# 7x7x7
# =====
elif args.type == '7x7x7-step30':
    from builder777 import Build777StageLRObliqueEdges
    builder = Build777StageLRObliqueEdges()

elif args.type == '7x7x7-step31':
    from builder777 import Build777StageLRObliqueEdges31
    builder = Build777StageLRObliqueEdges31()

elif args.type == '7x7x7-step80':
    from builder777 import Build777Step80
    builder = Build777Step80()

elif args.type == '7x7x7-step81':
    from builder777 import Build777Step81
    builder = Build777Step81()

elif args.type == '7x7x7-step90':
    from builder777 import Build777Step90
    builder = Build777Step90()

elif args.type == '7x7x7-step91':
    from builder777 import Build777Step91
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

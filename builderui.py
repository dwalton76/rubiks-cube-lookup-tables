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

# phase1
elif args.type == '4x4x4-tsai-phase1-centers':
    from builder444 import Build444TsaiPhase1Centers
    builder = Build444TsaiPhase1Centers()

# phase2
elif args.type == 'ss4x4x4-tsai-phase2-centers':
    from builder444 import StartingStates444TsaiPhase2Centers
    builder = StartingStates444TsaiPhase2Centers()

elif args.type == '4x4x4-tsai-phase2-centers':
    from builder444 import Build444TsaiPhase2Centers
    builder = Build444TsaiPhase2Centers()

elif args.type == 'ss4x4x4-tsai-phase2-edges-and-LR-centers':
    from builder444 import StartingStates444TsaiPhase2EdgesAndLRCenters
    builder = StartingStates444TsaiPhase2EdgesAndLRCenters()

elif args.type == '4x4x4-tsai-phase2-edges-and-LR-centers':
    from builder444 import Build444TsaiPhase2EdgesAndLRCenters
    builder = Build444TsaiPhase2EdgesAndLRCenters()

elif args.type == 'ss4x4x4-tsai-phase2':
    from builder444 import StartingStates444TsaiPhase2
    builder = StartingStates444TsaiPhase2()

elif args.type == '4x4x4-tsai-phase2':
    from builder444 import Build444TsaiPhase2
    builder = Build444TsaiPhase2()


# phase 3
elif args.type == '4x4x4-phase3-edges':
    from builder444 import Build444Phase3Edges
    builder = Build444Phase3Edges()


# =====
# 5x5x5
# =====
elif args.type == '5x5x5-EO-outer-orbit':
    from builder555 import Build555EdgeOrientOuterOrbit
    builder = Build555EdgeOrientOuterOrbit()

elif args.type == 'ss5x5x5-LR-center-stage':
    from builder555 import StartingStates555LRCenterStage
    builder = StartingStates555LRCenterStage()

elif args.type == '5x5x5-LR-center-stage':
    from builder555 import Build555LRCenterStage
    builder = Build555LRCenterStage()

elif args.type == 'ss5x5x5-edge-orient-LR-center-stage':
    from builder555 import StartingState555EdgeOrientOuterOrbitLRCenterStage
    builder = StartingState555EdgeOrientOuterOrbitLRCenterStage()

elif args.type == '5x5x5-edge-orient-LR-center-stage':
    from builder555 import Build555EdgeOrientOuterOrbitLRCenterStage
    builder = Build555EdgeOrientOuterOrbitLRCenterStage()

elif args.type == 'ss5x5x5-FB-center-stage':
    from builder555 import StartingStates555FBCenterStage
    builder = StartingStates555FBCenterStage()

elif args.type == '5x5x5-FB-center-stage':
    from builder555 import Build555FBCenterStage
    builder = Build555FBCenterStage()

# phase4
elif args.type == 'ss5x5x5-x-plane-outer-edges-stage':
    from builder555 import StartingStates555XPlaneOuterEdgesStage
    builder = StartingStates555XPlaneOuterEdgesStage()

elif args.type == '5x5x5-x-plane-outer-edges-stage':
    from builder555 import Build555XPlaneOuterEdgesStage
    builder = Build555XPlaneOuterEdgesStage()

elif args.type == '5x5x5-x-plane-inner-edges-stage':
    from builder555 import Build555XPlaneInnerEdgesStage
    builder = Build555XPlaneInnerEdgesStage()

elif args.type == 'ss5x5x5-phase4':
    from builder555 import StartingStates555Phase4
    builder = StartingStates555Phase4()

elif args.type == '5x5x5-phase4':
    from builder555 import Build555Phase4
    builder = Build555Phase4()

# phase5
elif args.type == 'ss5x5x5-phase5-LFRB-centers-stage':
    from builder555 import StartingStates555Phase5LFRBCenterStage
    builder = StartingStates555Phase5LFRBCenterStage()

elif args.type == '5x5x5-phase5-LFRB-centers-stage':
    from builder555 import Build555Phase5LFRBCenterStage
    builder = Build555Phase5LFRBCenterStage()

# =====
# 6x6x6
# =====
elif args.type == '6x6x6-UD-centers-stage':
    from builder666 import Build666UDCentersStage
    builder = Build666UDCentersStage()

elif args.type == '6x6x6-UD-oblique-edges-stage':
    from builder666 import Build666UDObliqueEdgesStage
    builder = Build666UDObliqueEdgesStage()

elif args.type == '6x6x6-LFRB-solve-inner-x-center-and-oblique-edges':
    from builder666 import Build666LFRBInnerXCenterAndObliqueEdges
    builder = Build666LFRBInnerXCenterAndObliqueEdges()

elif args.type == '6x6x6-LR-solve-inner-x-center-and-oblique-edges':
    from builder666 import Build666LRInnerXCenterAndObliqueEdges
    builder = Build666LRInnerXCenterAndObliqueEdges()

elif args.type == '6x6x6-EO-inner-orbit':
    from builder666 import Build666EdgeOrientInnerOrbit
    builder = Build666EdgeOrientInnerOrbit()

elif args.type == '6x6x6-EO-outer-orbit':
    from builder666 import Build666EdgeOrientOuterOrbit
    builder = Build666EdgeOrientOuterOrbit()

elif args.type == 'ss6x6x6-LR-centers-edge-orient':
    from builder666 import StartingStates666LRCenterEdgeOrient
    builder = StartingStates666LRCenterEdgeOrient()

elif args.type == '6x6x6-LR-centers-edge-orient':
    from builder666 import Build666LRCenterEdgeOrient
    builder = Build666LRCenterEdgeOrient()


# =====
# 7x7x7
# =====
elif args.type == 'ss7x7x7-UD-oblique-edges-stage':
    from builder777 import StartingStates777UDObliqueEdgesStage
    builder = StartingStates777UDObliqueEdgesStage()

elif args.type == '7x7x7-UD-oblique-edges-stage':
    from builder777 import Build777UDObliqueEdgesStage
    builder = Build777UDObliqueEdgesStage()

elif args.type == 'ss7x7x7-UD-outside-oblique-edges-stage':
    from builder777 import StartingStates777UDOutsideObliqueEdgesStage
    builder = StartingStates777UDOutsideObliqueEdgesStage()

elif args.type == '7x7x7-UD-outside-oblique-edges-stage':
    from builder777 import Build777UDOutsideObliqueEdgesStage
    builder = Build777UDOutsideObliqueEdgesStage()


elif args.type == 'ss7x7x7-LR-oblique-edges-stage':
    from builder777 import StartingStates777LRObliqueEdgesStage
    builder = StartingStates777LRObliqueEdgesStage()

elif args.type == '7x7x7-LR-oblique-edges-stage':
    from builder777 import Build777LRObliqueEdgesStage
    builder = Build777LRObliqueEdgesStage()

elif args.type == 'ss7x7x7-LR-outside-oblique-edges-stage':
    from builder777 import StartingStates777LROutsideObliqueEdgesStage
    builder = StartingStates777LROutsideObliqueEdgesStage()

elif args.type == '7x7x7-LR-outside-oblique-edges-stage':
    from builder777 import Build777LROutsideObliqueEdgesStage
    builder = Build777LROutsideObliqueEdgesStage()


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


log.info("")
log.info("")
log.info("")
log.info("************************************")
log.info(args.type)
log.info("************************************")
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

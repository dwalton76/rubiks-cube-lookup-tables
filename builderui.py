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
if args.type == 'StartingStates444UDCentersStage':
    from builder444 import StartingStates444UDCentersStage
    builder = StartingStates444UDCentersStage()

elif args.type == 'Build444UDCentersStage':
    from builder444 import Build444UDCentersStage
    builder = Build444UDCentersStage()

elif args.type == 'StartingStates444LRCentersStage':
    from builder444 import StartingStates444LRCentersStage
    builder = StartingStates444LRCentersStage()

elif args.type == 'Build444LRCentersStage':
    from builder444 import Build444LRCentersStage
    builder = Build444LRCentersStage()

elif args.type == 'StartingStates444FBCentersStage':
    from builder444 import StartingStates444FBCentersStage
    builder = StartingStates444FBCentersStage()

elif args.type == 'Build444FBCentersStage':
    from builder444 import Build444FBCentersStage
    builder = Build444FBCentersStage()

elif args.type == 'StartingStates444ULFRBDCentersStage':
    from builder444 import StartingStates444ULFRBDCentersStage
    builder = StartingStates444ULFRBDCentersStage()

elif args.type == 'Build444ULFRBDCentersStage':
    from builder444 import Build444ULFRBDCentersStage
    builder = Build444ULFRBDCentersStage()

# phase0
elif args.type == 'StartingStates444TsaiPhase0LRCentersStage':
    from builder444 import StartingStates444TsaiPhase0LRCentersStage
    builder = StartingStates444TsaiPhase0LRCentersStage()

elif args.type == 'Build444TsaiPhase0LRCentersStage':
    from builder444 import Build444TsaiPhase0LRCentersStage
    builder = Build444TsaiPhase0LRCentersStage()

# phase1
elif args.type == 'Build444TsaiPhase1Centers':
    from builder444 import Build444TsaiPhase1Centers
    builder = Build444TsaiPhase1Centers()

# phase2
elif args.type == 'StartingStates444TsaiPhase2Centers':
    from builder444 import StartingStates444TsaiPhase2Centers
    builder = StartingStates444TsaiPhase2Centers()

elif args.type == 'Build444TsaiPhase2Centers':
    from builder444 import Build444TsaiPhase2Centers
    builder = Build444TsaiPhase2Centers()

elif args.type == 'Build444TsaiPhase2Edges':
    from builder444 import Build444TsaiPhase2Edges
    builder = Build444TsaiPhase2Edges()

# phase 3
elif args.type == 'Build444Phase3Edges':
    from builder444 import Build444Phase3Edges
    builder = Build444Phase3Edges()

elif args.type == 'StartingStates444Phase3Centers':
    from builder444 import StartingStates444Phase3Centers
    builder = StartingStates444Phase3Centers()

elif args.type == 'Build444Phase3Centers':
    from builder444 import Build444Phase3Centers
    builder = Build444Phase3Centers()

elif args.type == 'StartingStates444Phase3':
    from builder444 import StartingStates444Phase3
    builder = StartingStates444Phase3()

elif args.type == 'Build444Phase3':
    from builder444 import Build444Phase3
    builder = Build444Phase3()


# =====
# 5x5x5
# =====
elif args.type == 'Build555LRTCenterStage':
    from builder555 import Build555LRTCenterStage
    builder = Build555LRTCenterStage()

elif args.type == 'Build555EdgeOrientOuterOrbit':
    from builder555 import Build555EdgeOrientOuterOrbit
    builder = Build555EdgeOrientOuterOrbit()

elif args.type == 'StartingStates555LRCenterStage':
    from builder555 import StartingStates555LRCenterStage
    builder = StartingStates555LRCenterStage()

elif args.type == 'Build555LRCenterStage':
    from builder555 import Build555LRCenterStage
    builder = Build555LRCenterStage()

elif args.type == 'StartingState555EdgeOrientOuterOrbitLRCenterStage':
    from builder555 import StartingState555EdgeOrientOuterOrbitLRCenterStage
    builder = StartingState555EdgeOrientOuterOrbitLRCenterStage()

elif args.type == 'Build555EdgeOrientOuterOrbitLRCenterStage':
    from builder555 import Build555EdgeOrientOuterOrbitLRCenterStage
    builder = Build555EdgeOrientOuterOrbitLRCenterStage()

elif args.type == 'StartingStates555FBCenterStage':
    from builder555 import StartingStates555FBCenterStage
    builder = StartingStates555FBCenterStage()

elif args.type == 'Build555FBCenterStage':
    from builder555 import Build555FBCenterStage
    builder = Build555FBCenterStage()

elif args.type == 'Build555InsideOrbit':
    from builder555 import Build555InsideOrbit
    builder = Build555InsideOrbit()


# phase4
elif args.type == 'StartingStates555XPlaneOuterEdgesStage':
    from builder555 import StartingStates555XPlaneOuterEdgesStage
    builder = StartingStates555XPlaneOuterEdgesStage()

elif args.type == 'Build555XPlaneOuterEdgesStage()':
    from builder555 import Build555XPlaneOuterEdgesStage
    builder = Build555XPlaneOuterEdgesStage()

elif args.type == 'StartingStates555XPlaneHighMiddelEdgesStage':
    from builder555 import StartingStates555XPlaneHighMiddelEdgesStage
    builder = StartingStates555XPlaneHighMiddelEdgesStage()

elif args.type == 'Build555XPlaneHighMiddelEdgesStage':
    from builder555 import Build555XPlaneHighMiddelEdgesStage
    builder = Build555XPlaneHighMiddelEdgesStage()

elif args.type == 'StartingStates555XPlaneLowMiddelEdgesStage':
    from builder555 import StartingStates555XPlaneLowMiddelEdgesStage
    builder = StartingStates555XPlaneLowMiddelEdgesStage()

elif args.type == 'Build555XPlaneLowMiddelEdgesStage':
    from builder555 import Build555XPlaneLowMiddelEdgesStage
    builder = Build555XPlaneLowMiddelEdgesStage()

elif args.type == 'Build555XPlaneInnerEdgesStage':
    from builder555 import Build555XPlaneInnerEdgesStage
    builder = Build555XPlaneInnerEdgesStage()

elif args.type == 'StartingStates555Phase4':
    from builder555 import StartingStates555Phase4
    builder = StartingStates555Phase4()

elif args.type == 'Build555Phase4':
    from builder555 import Build555Phase4
    builder = Build555Phase4()

# phase5
elif args.type == 'StartingStates555Phase5LFRBCenterStage':
    from builder555 import StartingStates555Phase5LFRBCenterStage
    builder = StartingStates555Phase5LFRBCenterStage()

elif args.type == 'Build555Phase5LFRBCenterStage':
    from builder555 import Build555Phase5LFRBCenterStage
    builder = Build555Phase5LFRBCenterStage()

# =====
# 6x6x6
# =====
elif args.type == 'StartingStates666UDInnerXCentersStage':
    from builder666 import StartingStates666UDInnerXCentersStage
    builder = StartingStates666UDInnerXCentersStage()

elif args.type == 'Build666UDInnerXCentersStage':
    from builder666 import Build666UDInnerXCentersStage
    builder = Build666UDInnerXCentersStage()

elif args.type == 'StartingStates666UDObliqueEdgesStage':
    from builder666 import StartingStates666UDObliqueEdgesStage
    builder = StartingStates666UDObliqueEdgesStage()

elif args.type == 'Build666UDObliqueEdgesStage':
    from builder666 import Build666UDObliqueEdgesStage
    builder = Build666UDObliqueEdgesStage()

elif args.type == 'StartingStates666LRInnerXCentersObliqueEdgesStage':
    from builder666 import StartingStates666LRInnerXCentersObliqueEdgesStage
    builder = StartingStates666LRInnerXCentersObliqueEdgesStage()

elif args.type == 'Build666LRInnerXCentersObliqueEdgesStage':
    from builder666 import Build666LRInnerXCentersObliqueEdgesStage
    builder = Build666LRInnerXCentersObliqueEdgesStage()


elif args.type == 'StartingStates666LRObliqueEdgesStage':
    from builder666 import StartingStates666LRObliqueEdgesStage
    builder = StartingStates666LRObliqueEdgesStage()

elif args.type == 'Build666LRObliqueEdgesStage':
    from builder666 import Build666LRObliqueEdgesStage
    builder = Build666LRObliqueEdgesStage()

elif args.type == 'Build666LRInnerXCenterStage':
    from builder666 import Build666LRInnerXCenterStage
    builder = Build666LRInnerXCenterStage()

elif args.type == 'Build666LFRBInnerXCenterAndObliqueEdges':
    from builder666 import Build666LFRBInnerXCenterAndObliqueEdges
    builder = Build666LFRBInnerXCenterAndObliqueEdges()

elif args.type == 'Build666LRInnerXCenterAndObliqueEdges':
    from builder666 import Build666LRInnerXCenterAndObliqueEdges
    builder = Build666LRInnerXCenterAndObliqueEdges()

elif args.type == 'Build666EdgeOrientInnerOrbit':
    from builder666 import Build666EdgeOrientInnerOrbit
    builder = Build666EdgeOrientInnerOrbit()

elif args.type == 'Build666EdgeOrientOuterOrbit':
    from builder666 import Build666EdgeOrientOuterOrbit
    builder = Build666EdgeOrientOuterOrbit()

elif args.type == 'StartingStates666LRCenterEdgeOrient':
    from builder666 import StartingStates666LRCenterEdgeOrient
    builder = StartingStates666LRCenterEdgeOrient()

elif args.type == 'Build666LRCenterEdgeOrient':
    from builder666 import Build666LRCenterEdgeOrient
    builder = Build666LRCenterEdgeOrient()


# =====
# 7x7x7
# =====
elif args.type == 'StartingStates777UDObliqueEdgesStage':
    from builder777 import StartingStates777UDObliqueEdgesStage
    builder = StartingStates777UDObliqueEdgesStage()

elif args.type == 'Build777UDObliqueEdgesStage':
    from builder777 import Build777UDObliqueEdgesStage
    builder = Build777UDObliqueEdgesStage()

elif args.type == 'StartingStates777UDOutsideObliqueEdgesStage':
    from builder777 import StartingStates777UDOutsideObliqueEdgesStage
    builder = StartingStates777UDOutsideObliqueEdgesStage()

elif args.type == 'Build777UDOutsideObliqueEdgesStage':
    from builder777 import Build777UDOutsideObliqueEdgesStage
    builder = Build777UDOutsideObliqueEdgesStage()


elif args.type == 'StartingStates777LRObliqueEdgesStage':
    from builder777 import StartingStates777LRObliqueEdgesStage
    builder = StartingStates777LRObliqueEdgesStage()

elif args.type == 'Build777LRObliqueEdgesStage':
    from builder777 import Build777LRObliqueEdgesStage
    builder = Build777LRObliqueEdgesStage()

elif args.type == 'StartingStates777LRLeftMiddleObliqueEdgesStage':
    from builder777 import StartingStates777LRLeftMiddleObliqueEdgesStage
    builder = StartingStates777LRLeftMiddleObliqueEdgesStage()

elif args.type == 'Build777LRLeftMiddleObliqueEdgesStage':
    from builder777 import Build777LRLeftMiddleObliqueEdgesStage
    builder = Build777LRLeftMiddleObliqueEdgesStage()

elif args.type == 'StartingStates777LRRightMiddleObliqueEdgesStage':
    from builder777 import StartingStates777LRRightMiddleObliqueEdgesStage
    builder = StartingStates777LRRightMiddleObliqueEdgesStage()

elif args.type == 'Build777LRRightMiddleObliqueEdgesStage':
    from builder777 import Build777LRRightMiddleObliqueEdgesStage
    builder = Build777LRRightMiddleObliqueEdgesStage()

elif args.type == 'StartingStates777LROutsideObliqueEdgesStage':
    from builder777 import StartingStates777LROutsideObliqueEdgesStage
    builder = StartingStates777LROutsideObliqueEdgesStage()

elif args.type == 'Build777LROutsideObliqueEdgesStage':
    from builder777 import Build777LROutsideObliqueEdgesStage
    builder = Build777LROutsideObliqueEdgesStage()


elif args.type == 'Build777Step80':
    from builder777 import Build777Step80
    builder = Build777Step80()

elif args.type == 'Build777Step81':
    from builder777 import Build777Step81
    builder = Build777Step81()

elif args.type == 'Build777Step90':
    from builder777 import Build777Step90
    builder = Build777Step90()

elif args.type == 'Build777Step91':
    from builder777 import Build777Step91
    builder = Build777Step91()

elif args.type == 'StartingStates777Step200':
    from builder777 import StartingStates777Step200
    builder = StartingStates777Step200()

elif args.type == 'Build777Step200':
    from builder777 import Build777Step200
    builder = Build777Step200()

elif args.type == 'StartingStates777Step201':
    from builder777 import StartingStates777Step201
    builder = StartingStates777Step201()

elif args.type == 'Build777Step201':
    from builder777 import Build777Step201
    builder = Build777Step201()

elif args.type == 'StartingStates777Step202':
    from builder777 import StartingStates777Step202
    builder = StartingStates777Step202()

elif args.type == 'Build777Step202':
    from builder777 import Build777Step202
    builder = Build777Step202()

elif args.type == 'StartingStates777Step210':
    from builder777 import StartingStates777Step210
    builder = StartingStates777Step210()

elif args.type == 'Build777Step210':
    from builder777 import Build777Step210
    builder = Build777Step210()

elif args.type == 'StartingStates777Step211':
    from builder777 import StartingStates777Step211
    builder = StartingStates777Step211()

elif args.type == 'Build777Step211':
    from builder777 import Build777Step211
    builder = Build777Step211()

elif args.type == 'StartingStates777Step212':
    from builder777 import StartingStates777Step212
    builder = StartingStates777Step212()

elif args.type == 'Build777Step212':
    from builder777 import Build777Step212
    builder = Build777Step212()

elif args.type == 'Build777Step220':
    from builder777 import Build777Step220
    builder = Build777Step220()

elif args.type == 'Build777Step221':
    from builder777 import Build777Step221
    builder = Build777Step221()

elif args.type == 'Build777Step222':
    from builder777 import Build777Step222
    builder = Build777Step222()


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

#!/usr/bin/env python3

# standard libraries
import logging
import sys

# rubiks cube libraries
from rubikscubennnsolver.RubiksCube444 import (
    LookupTable444FBCentersStage,
    LookupTable444LRCentersStage,
    LookupTable444UDCentersStage,
    RubiksCube444,
    solved_444,
)
from rubikscubennnsolver.RubiksCube555 import (
    LookupTable555EdgeOrientOuterOrbit,
    LookupTable555FBTCenterStage,
    LookupTable555FBXCenterStage,
    LookupTable555LRCenterStageEOInnerOrbit,
    LookupTable555LRTCenterStage,
    LookupTable555LRXCenterStage,
    LookupTable555Phase5Centers,
    LookupTable555Phase5FBCenters,
    RubiksCube555,
    solved_555,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

lt_class = sys.argv[1]

if lt_class.startswith("Build444"):
    cube = RubiksCube444(solved_444, "URFDLB")
    cube.cpu_mode = "normal"

    if lt_class == "Build444UDCentersStage":
        cube.lt = LookupTable444UDCentersStage(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    elif lt_class == "Build444LRCentersStage":
        cube.lt = LookupTable444LRCentersStage(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    elif lt_class == "Build444FBCentersStage":
        cube.lt = LookupTable444FBCentersStage(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    else:
        raise ValueError(lt_class)

elif lt_class.startswith("Build555"):
    cube = RubiksCube555(solved_555, "URFDLB")
    cube.cpu_mode = "normal"

    # phase 1
    if lt_class == "Build555LRCenterStageTCenter":
        cube.lt = LookupTable555LRTCenterStage(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    elif lt_class == "Build555LRCenterStageXCenter":
        cube.lt = LookupTable555LRXCenterStage(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    # phase 2
    elif lt_class == "Build555FBTCenterStage":
        cube.lt = LookupTable555FBTCenterStage(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    elif lt_class == "Build555FBXCenterStage":
        cube.lt = LookupTable555FBXCenterStage(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    # phase 3
    elif lt_class == "Build555LRCenterStageEOInnerOrbit":
        cube.lt = LookupTable555LRCenterStageEOInnerOrbit(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    elif lt_class == "Build555EdgeOrientOuterOrbit":
        cube.lt = LookupTable555EdgeOrientOuterOrbit(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    # phase 5
    elif lt_class == "Build555Phase5Centers":
        cube.lt = LookupTable555Phase5Centers(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    elif lt_class == "Build555Phase5FBCenters":
        cube.lt = LookupTable555Phase5FBCenters(cube, build_state_index=True)
        cube.lt.build_ida_graph()

    else:
        raise ValueError(lt_class)
else:
    raise ValueError(lt_class)

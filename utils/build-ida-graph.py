#!/usr/bin/env python3

# standard libraries
import logging
import sys

# rubiks cube libraries
from rubikscubennnsolver.RubiksCube444 import (
    LookupTable444HighLowEdgesCenters,
    LookupTable444HighLowEdgesEdges,
    LookupTable444LRCentersStage,
    LookupTable444Reduce333Centers,
    LookupTable444Reduce333FirstFourEdges,
    LookupTable444Reduce333FirstTwoCenters,
    LookupTable444Reduce333LastEightEdges,
    LookupTable444UDCentersStage,
    RubiksCube444,
    solved_444,
)
from rubikscubennnsolver.RubiksCube555 import (
    LookupTable555EdgeOrientInnerOrbit,
    LookupTable555EdgeOrientOuterOrbit,
    LookupTable555FBCenterSolve,
    LookupTable555FBTCenterStage,
    LookupTable555FBXCenterStage,
    LookupTable555LRCenterSolve,
    LookupTable555LRTCenterStage,
    LookupTable555LRXCenterStage,
    LookupTable555Phase2LRCenterStage,
    LookupTable555Phase3LRCenterStage,
    LookupTable555Phase5Centers,
    LookupTable555Phase5FBCenters,
    LookupTable555Phase5HighEdgeMidge,
    LookupTable555Phase5LowEdgeMidge,
    LookupTable555Phase6Centers,
    LookupTable555Phase6HighEdgeMidge,
    LookupTable555Phase6LowEdgeMidge,
    LookupTable555UDCenterSolve,
    RubiksCube555,
    solved_555,
)
from rubikscubennnsolver.RubiksCube666 import (
    LookupTable666FBInnerXCenterAndObliqueEdges,
    LookupTable666LRInnerXCenterAndObliqueEdges,
    LookupTable666LRInnerXCentersStage,
    LookupTable666UDInnerXCentersStage,
    LookupTable666UDLeftObliqueCentersStage,
    LookupTable666UDObliqueEdges,
    LookupTable666UDRightObliqueCentersStage,
    LookupTable666UDXCentersStage,
    RubiksCube666,
    solved_666,
)
from rubikscubennnsolver.RubiksCube777 import (
    LookupTable777Step41,
    LookupTable777Step42,
    LookupTable777Step43,
    LookupTable777Step44,
    LookupTable777Step51,
    LookupTable777Step52,
    LookupTable777Step53,
    LookupTable777Step54,
    LookupTable777Step55,
    LookupTable777Step61,
    LookupTable777Step62,
    LookupTable777Step65,
    LookupTable777Step66,
    LookupTable777Step71,
    LookupTable777Step72,
    LookupTable777Step75,
    LookupTable777Step76,
    LookupTable777UDInnerTcenters,
    LookupTable777UDInnerXcenters,
    RubiksCube777,
    solved_777,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

lt_class = sys.argv[1]

if lt_class.startswith("Build444"):  # noqa: C901
    cube = RubiksCube444(solved_444, "URFDLB")

    # phase 1
    if lt_class == "Build444UDCentersStage":
        cube.lt = LookupTable444UDCentersStage(cube, build_state_index=True)

    elif lt_class == "Build444LRCentersStage":
        cube.lt = LookupTable444LRCentersStage(cube, build_state_index=True)

    # phase 2
    elif lt_class == "Build444HighLowEdgesEdges":
        cube.lt = LookupTable444HighLowEdgesEdges(cube, build_state_index=True)

    elif lt_class == "Build444HighLowEdgesCenters":
        cube.lt = LookupTable444HighLowEdgesCenters(cube, build_state_index=True)

    # phase 3
    elif lt_class == "Build444Reduce333FirstTwoCenters":
        cube.lt = LookupTable444Reduce333FirstTwoCenters(cube, build_state_index=True)

    elif lt_class == "Build444Reduce333FirstFourEdges":
        cube.lt = LookupTable444Reduce333FirstFourEdges(cube, build_state_index=True)

    # phase 4
    elif lt_class == "Build444Reduce333Centers":
        cube.lt = LookupTable444Reduce333Centers(cube, build_state_index=True)

    elif lt_class == "Build444Reduce333LastEightEdges":
        cube.lt = LookupTable444Reduce333LastEightEdges(cube, build_state_index=True)

    else:
        raise ValueError(lt_class)

elif lt_class.startswith("Build555"):
    cube = RubiksCube555(solved_555, "URFDLB")

    # phase 1
    if lt_class == "Build555LRCenterStageTCenter":
        cube.lt = LookupTable555LRTCenterStage(cube, build_state_index=True)

    elif lt_class == "Build555LRCenterStageXCenter":
        cube.lt = LookupTable555LRXCenterStage(cube, build_state_index=True)

    # phase 2
    elif lt_class == "Build555FBTCenterStage":
        cube.lt = LookupTable555FBTCenterStage(cube, build_state_index=True)

    elif lt_class == "Build555FBXCenterStage":
        cube.lt = LookupTable555FBXCenterStage(cube, build_state_index=True)

    elif lt_class == "Build555Phase2LRCenterStage":
        cube.lt = LookupTable555Phase2LRCenterStage(cube, build_state_index=True)

    # phase 3
    elif lt_class == "Build555Phase3LRCenterStage":
        cube.lt = LookupTable555Phase3LRCenterStage(cube, build_state_index=True)

    elif lt_class == "Build555EdgeOrientOuterOrbit":
        cube.lt = LookupTable555EdgeOrientOuterOrbit(cube, build_state_index=True)

    elif lt_class == "Build555EdgeOrientInnerOrbit":
        cube.lt = LookupTable555EdgeOrientInnerOrbit(cube, build_state_index=True)

    # phase 5
    elif lt_class == "Build555Phase5Centers":
        cube.lt = LookupTable555Phase5Centers(cube, build_state_index=True)

    elif lt_class == "Build555Phase5HighEdgeMidge":
        cube.lt = LookupTable555Phase5HighEdgeMidge(cube, build_state_index=True)

    elif lt_class == "Build555Phase5LowEdgeMidge":
        cube.lt = LookupTable555Phase5LowEdgeMidge(cube, build_state_index=True)

    elif lt_class == "Build555Phase5FBCenters":
        cube.lt = LookupTable555Phase5FBCenters(cube, build_state_index=True)

    # phase 6
    elif lt_class == "Build555Phase6Centers":
        cube.lt = LookupTable555Phase6Centers(cube, build_state_index=True)

    elif lt_class == "Build555Phase6HighEdgeMidge":
        cube.lt = LookupTable555Phase6HighEdgeMidge(cube, build_state_index=True)

    elif lt_class == "Build555Phase6LowEdgeMidge":
        cube.lt = LookupTable555Phase6LowEdgeMidge(cube, build_state_index=True)

    # solve staged centers
    elif lt_class == "Build555UDCenterSolve":
        cube.lt = LookupTable555UDCenterSolve(cube, build_state_index=True)

    elif lt_class == "Build555LRCenterSolve":
        cube.lt = LookupTable555LRCenterSolve(cube, build_state_index=True)

    elif lt_class == "Build555FBCenterSolve":
        cube.lt = LookupTable555FBCenterSolve(cube, build_state_index=True)

    else:
        raise NotImplementedError(lt_class)

elif lt_class.startswith("Build666"):
    cube = RubiksCube666(solved_666, "URFDLB")

    # phase 1
    if lt_class == "Build666LRInnerXCentersStage":
        cube.lt = LookupTable666LRInnerXCentersStage(cube, build_state_index=True)

    # dwalton
    # phase 3
    elif lt_class == "Build666UDInnerXCentersStage":
        cube.lt = LookupTable666UDInnerXCentersStage(cube, build_state_index=True)

    elif lt_class == "Build666UDLeftObliqueCentersStage":
        cube.lt = LookupTable666UDLeftObliqueCentersStage(cube, build_state_index=True)

    elif lt_class == "Build666UDRightObliqueCentersStage":
        cube.lt = LookupTable666UDRightObliqueCentersStage(cube, build_state_index=True)

    elif lt_class == "Build666UDXCentersStage":
        cube.lt = LookupTable666UDXCentersStage(cube, build_state_index=True)

    # phase 6
    elif lt_class == "Build666LRInnerXCenterAndObliqueEdges":
        cube.lt = LookupTable666LRInnerXCenterAndObliqueEdges(cube, build_state_index=True)

    elif lt_class == "Build666FBInnerXCenterAndObliqueEdges":
        cube.lt = LookupTable666FBInnerXCenterAndObliqueEdges(cube, build_state_index=True)

    elif lt_class == "Build666UDObliqueEdges":
        cube.lt = LookupTable666UDObliqueEdges(cube, build_state_index=True)

    else:
        raise NotImplementedError(lt_class)

elif lt_class.startswith("Build777"):
    cube = RubiksCube777(solved_777, "URFDLB")

    # phase 7
    if lt_class == "Build777Step41":
        cube.lt = LookupTable777Step41(cube, build_state_index=True)

    elif lt_class == "Build777Step42":
        cube.lt = LookupTable777Step42(cube, build_state_index=True)

    elif lt_class == "Build777Step43":
        cube.lt = LookupTable777Step43(cube, build_state_index=True)

    elif lt_class == "Build777Step44":
        cube.lt = LookupTable777Step44(cube, build_state_index=True)

    # phase 8
    elif lt_class == "Build777Step51":
        cube.lt = LookupTable777Step51(cube, build_state_index=True)

    elif lt_class == "Build777Step52":
        cube.lt = LookupTable777Step52(cube, build_state_index=True)

    elif lt_class == "Build777Step53":
        cube.lt = LookupTable777Step53(cube, build_state_index=True)

    elif lt_class == "Build777Step54":
        cube.lt = LookupTable777Step54(cube, build_state_index=True)

    elif lt_class == "Build777Step55":
        cube.lt = LookupTable777Step55(cube, build_state_index=True)

    # phase 9
    elif lt_class == "Build777Step61":
        cube.lt = LookupTable777Step61(cube, build_state_index=True)

    elif lt_class == "Build777Step62":
        cube.lt = LookupTable777Step62(cube, build_state_index=True)

    elif lt_class == "Build777Step65":
        cube.lt = LookupTable777Step65(cube, build_state_index=True)

    elif lt_class == "Build777Step66":
        cube.lt = LookupTable777Step66(cube, build_state_index=True)

    # solve t-centers
    elif lt_class == "Build777Step71":
        cube.lt = LookupTable777Step71(cube, build_state_index=True)

    elif lt_class == "Build777Step72":
        cube.lt = LookupTable777Step72(cube, build_state_index=True)

    elif lt_class == "Build777Step75":
        cube.lt = LookupTable777Step75(cube, build_state_index=True)

    elif lt_class == "Build777Step76":
        cube.lt = LookupTable777Step76(cube, build_state_index=True)

    elif lt_class == "Build777UDInnerTcenters":
        cube.lt = LookupTable777UDInnerTcenters(cube, build_state_index=True)

    elif lt_class == "Build777UDInnerXcenters":
        cube.lt = LookupTable777UDInnerXcenters(cube, build_state_index=True)

    else:
        raise NotImplementedError(lt_class)

else:
    raise NotImplementedError(lt_class)

cube.lt.build_ida_graph()

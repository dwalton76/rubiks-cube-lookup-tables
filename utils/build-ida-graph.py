#!/usr/bin/env python3

# standard libraries
import logging
import sys

# rubiks cube libraries
from rubikscubennnsolver.RubiksCube444 import (
    LookupTable444UDCentersStage,
    LookupTable444LRCentersStage,
    LookupTable444FBCentersStage,
    RubiksCube444,
    solved_444,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

lt_class = sys.argv[1]

if lt_class.startswith("Build444"):
    cube = RubiksCube444(solved_444, "URFDLB")
    cube.cpu_mode = "normal"

    if lt_class == "Build444UDCentersStage":
        cube.lt_UD_centers_stage = LookupTable444UDCentersStage(cube, build_state_index=True)
        cube.lt_UD_centers_stage.build_ida_graph()

    elif lt_class == "Build444LRCentersStage":
        cube.lt_LR_centers_stage = LookupTable444LRCentersStage(cube, build_state_index=True)
        cube.lt_LR_centers_stage.build_ida_graph()

    elif lt_class == "Build444FBCentersStage":
        cube.lt_FB_centers_stage = LookupTable444FBCentersStage(cube, build_state_index=True)
        cube.lt_FB_centers_stage.build_ida_graph()

    else:
        raise ValueError(lt_class)

else:
    raise ValueError(lt_class)

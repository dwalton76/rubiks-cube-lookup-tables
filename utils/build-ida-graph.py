#!/usr/bin/env python3

from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, LookupTable444UDCentersStage
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    solved_555,
    edges_partner_555,
)
from rubikscubennnsolver.RubiksCube666 import (
    RubiksCube666,
    moves_666,
    solved_666,
    rotate_666,
)
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

lt_class = sys.argv[1]

if lt_class.startswith("Build444"):
    cube = RubiksCube444(solved_444, "URFDLB")
    cube.cpu_mode = "normal"

    if lt_class == "Build444UDCentersStage":
        cube.lt_UD_centers_stage = LookupTable444UDCentersStage(cube, build_state_index=True)
        cube.lt_UD_centers_stage.build_ida_graph()
    else:
        raise ValueError(lt_class)
else:
    raise ValueError(lt_class)

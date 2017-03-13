#!/usr/bin/env python3

from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_222, moves_222, rotate_222
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333, moves_333, rotate_333
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444
from rubikscubennnsolver.RubiksCube555 import RubiksCube555, solved_555, moves_555, rotate_555
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666, moves_666, rotate_666
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777, moves_777, rotate_777
from buildercore import parse_ascii_444

import logging
import sys

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    log = logging.getLogger(__name__)

    state = parse_ascii_444("""
          . . . .
          . U U .
          . U U .
          . . . .
 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . F F .
 . L L .  . F F .  . R R .  . F F .
 . . . .  . . . .  . . . .  . . . .
          . . . .
          . U U .
          . U U .
          . . . .
""")

    cube = RubiksCube444(state, 'ULFRBD')

#!/usr/bin/e nv python3

from buildercore import BFS
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333, moves_333, rotate_333
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)



class Build333SolveWithoutLRFBQuarterTurnsEdgesOnly(BFS):
    """
    If only L L' R R' are restricted there are 12! or 479,001,600 states
    If F F' B B' are also restricted there are 967,679 states
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-solve-without-LRFB-quarter-edges-only',
            ("L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),
            '3x3x3',
            'lookup-table-3x3x3-step21-solve-without-LRFB-quarter-edges-only.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        . U .
        U U U
        . U .

 . L .  . F .  . R .  . B .
 L L L  F F F  R R R  B B B
 . L .  . F .  . R .  . B .

        . D .
        D D D
        . D .""", 'ascii'),),
        )


class Build333SolveWithoutLRFBQuarterTurnsCornersOnly(BFS):
    """
    If only L L' R R' are restricted there are ??? states
    If F F' B B' are also restricted there are 40,320 states
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-solve-without-LRFB-quarter-corners-only',
            ("L", "L'",
             "R", "R'",
             #"F", "F'",
             #"B", "B'",
            ),
            '3x3x3',
            'lookup-table-3x3x3-step21-solve-without-LRFB-quarter-corners-only.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        U . U
        . U .
        U . U

 L . L  F . F  R . R  B . B
 . L .  . F .  . R .  . B .
 L . L  F . F  R . R  B . B

        D . D
        . D .
        D . D""", 'ascii'),),
        )



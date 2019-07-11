from buildercore import BFS
from rubikscubennnsolver.RubiksCube333 import RubiksCube333, solved_333, moves_333, rotate_333
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)


class Build333Ultimate(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-ultimate',

            # illegal moves
            (),

            '3x3x3',
            'lookup-table-3x3x3-step00-ultimate.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        U U U
        U U U
        U U U

 L L L  F F F  R R R  B B B
 L L L  F F F  R R R  B B B
 L L L  F F F  R R R  B B B

        D D D
        D D D
        D D D""", 'ascii'),),
        )


class Build333Phase1(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase1',

            # illegal moves
            (),

            '3x3x3',
            'lookup-table-3x3x3-step110.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        1 1 1
        1 U 1
        1 1 1

 1 1 1  1 1 1  1 1 1  1 1 1
 1 L 1  1 F 1  1 R 1  1 B 1
 1 1 1  1 1 1  1 1 1  1 1 1

        1 1 1
        1 D 1
        1 1 1""", 'ascii'),),
        )


class Build333Phase2(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase2',

            # illegal moves
            ("L", "L'", "R", "R'"),

            '3x3x3',
            'lookup-table-3x3x3-step120.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        1 x 1
        x U x
        1 x 1

 1 x 1  1 x 1  1 x 1  1 x 1
 L L L  L F L  L R L  L B L
 1 x 1  1 x 1  1 x 1  1 x 1

        1 x 1
        x D x
        1 x 1""", 'ascii'),),
        )


class Build333Phase3(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase3',

            # illegal moves
            ("L", "L'", "R", "R'", "F", "F'", "B", "B'"),

            '3x3x3',
            'lookup-table-3x3x3-step130.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        1 F 1
        x U x
        1 F 1

 1 x 1  1 F 1  1 x 1  1 F 1
 x L x  x F x  x R x  x B x
 1 x 1  1 F 1  1 x 1  1 F 1

        1 F 1
        x D x
        1 F 1""", 'ascii'),),
        )


class Build333Phase4(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase4',

            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'", "U", "U'", "D", "D'"),

            '3x3x3',
            'lookup-table-3x3x3-step140.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        U U U
        U U U
        U U U

 L L L  F F F  R R R  B B B
 L L L  F F F  R R R  B B B
 L L L  F F F  R R R  B B B

        D D D
        D D D
        D D D""", 'ascii'),),
        )

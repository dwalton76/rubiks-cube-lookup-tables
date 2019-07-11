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


'''
4-phase solver overview

phase 1 - EO the edges and corners
    - make the edges and corners solveable without L L' R R'
    - (2^12)/2 or 2048 states
    - (2^8)/2 or 128 states
    - 2048 * 128 is 262,144 states
    - averages 6.37 moves

phase 2 - Remove F F' B B'
    - LB LF RB RF edges must be staged to x-plane
        12!/(8!*4!) is 495
    - EO the corners again
        - (2^8)/2 or 128 states
    - 128 * 495 is 63,360
    - averages 6.42 moves

phase 3 - Remove U U' D D'
    move 4 edges to y-plane, this in turn moves the other 4-edges to z-plane
    There must also be some corner manipulation done here
    - 8!/(4!*4!) is 70 for the edges
    - 8!/(4!*4!) is 70 for the corners (I think)
    - 70 * 70 is 4900
    - averages 6.70 moves

phase 4 - solve cube
    - all quarter turns have been removed by this point
    - (4!^3)/2 is 6912 for the edges
    - 4!^2 is 576 for the corners
        it is actually 96 though (I got 96 by building the corners table)
        576/6 is 96 not sure if that means anything

    - 6912 * 96 is 663,552
    - averages 10.13 moves

This should averge 29 moves
'''
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

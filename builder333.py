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

phase 1 - EO the edges
    - make the edges solveable without L L' R R'
    - (2^12)/2 or 2048 states
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
        x 1 x
        1 U 1
        x 1 x

 x 1 x  x 1 x  x 1 x  x 1 x
 1 L 1  1 F 1  1 R 1  1 B 1
 x 1 x  x 1 x  x 1 x  x 1 x

        x 1 x
        1 D 1
        x 1 x""", 'ascii'),),
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
        U x U
        x U x
        U x U

 x x x  x x x  x x x  x x x
 1 L 1  1 F 1  1 R 1  1 B 1
 x x x  x x x  x x x  x x x

        U x U
        x D x
        U x U""", 'ascii'),),
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
            (('DFDxUxDFDLxLxLxLxLBFBxFxBFBRxRxRxRxRFFFxBxFFFUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxDFDLxLxLxRxRBFBxFxFFFRxRxRxLxLFFFxBxBFBUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxDFDLxRxLxLxRFFBxFxFFBRxLxRxRxLBFFxBxBFFUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxDFDLxRxLxRxLFFBxFxBFFRxLxRxLxRBFFxBxFFBUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxDFDRxLxLxLxRBFFxFxFFBLxRxRxRxLFFBxBxBFFUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxDFDRxLxLxRxLBFFxFxBFFLxRxRxLxRFFBxBxFFBUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxDFDRxRxLxLxLFFFxFxBFBLxLxRxRxRBFBxBxFFFUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxDFDRxRxLxRxRFFFxFxFFFLxLxRxLxLBFBxBxBFBUFUxDxUFU', 'ULFRBD'),
             ('DFDxUxUFULxLxLxLxLFFFxFxBFBRxRxRxRxRFFFxBxBFBUFUxDxDFD', 'ULFRBD'),
             ('DFDxUxUFULxLxLxRxRFFBxFxBFFLxLxRxRxRBFFxBxFFBDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFULxLxLxRxRFFBxFxFFBLxLxRxRxRBFFxBxBFFUFUxDxDFD', 'ULFRBD'),
             ('DFDxUxUFULxLxLxRxRFFFxFxBFBRxRxRxLxLFFFxBxBFBDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFULxRxLxLxRBFBxFxBFBLxRxRxLxRFFFxBxFFFDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFULxRxLxLxRBFBxFxFFFLxRxRxLxRFFFxBxBFBUFUxDxDFD', 'ULFRBD'),
             ('DFDxUxUFULxRxLxLxRBFFxFxBFFRxLxRxRxLBFFxBxBFFDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFULxRxLxRxLBFFxFxBFFRxLxRxLxRBFFxBxBFFUFUxDxDFD', 'ULFRBD'),
             ('DFDxUxUFURxLxLxLxRFFBxFxFFBLxRxRxRxLFFBxBxFFBUFUxDxDFD', 'ULFRBD'),
             ('DFDxUxUFURxLxLxRxLFFBxFxFFBLxRxRxLxRFFBxBxFFBDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFURxLxLxRxLFFFxFxBFBRxLxRxRxLBFBxBxFFFUFUxDxDFD', 'ULFRBD'),
             ('DFDxUxUFURxLxLxRxLFFFxFxFFFRxLxRxRxLBFBxBxBFBDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFURxRxLxLxLBFBxFxFFFLxLxRxRxRBFBxBxFFFDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFURxRxLxLxLBFFxFxBFFRxRxRxLxLFFBxBxFFBUFUxDxDFD', 'ULFRBD'),
             ('DFDxUxUFURxRxLxLxLBFFxFxFFBRxRxRxLxLFFBxBxBFFDFDxDxUFU', 'ULFRBD'),
             ('DFDxUxUFURxRxLxRxRBFBxFxFFFLxLxRxLxLBFBxBxFFFUFUxDxDFD', 'ULFRBD'),
             ('DFUxUxDFULxLxLxLxLBFFxFxBFFRxRxRxRxRBFFxBxBFFUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxDFULxLxLxRxRBFBxFxBFBLxLxRxRxRFFFxBxFFFDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFULxLxLxRxRBFBxFxFFFLxLxRxRxRFFFxBxBFBUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxDFULxLxLxRxRBFFxFxBFFRxRxRxLxLBFFxBxBFFDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFULxRxLxLxRFFBxFxBFFLxRxRxLxRBFFxBxFFBDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFULxRxLxLxRFFBxFxFFBLxRxRxLxRBFFxBxBFFUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxDFULxRxLxLxRFFFxFxBFBRxLxRxRxLFFFxBxBFBDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFULxRxLxRxLFFFxFxBFBRxLxRxLxRFFFxBxBFBUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxDFURxLxLxLxRBFBxFxFFFLxRxRxRxLBFBxBxFFFUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxDFURxLxLxRxLBFBxFxFFFLxRxRxLxRBFBxBxFFFDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFURxLxLxRxLBFFxFxBFFRxLxRxRxLFFBxBxFFBUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxDFURxLxLxRxLBFFxFxFFBRxLxRxRxLFFBxBxBFFDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFURxRxLxLxLFFBxFxFFBLxLxRxRxRFFBxBxFFBDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFURxRxLxLxLFFFxFxBFBRxRxRxLxLBFBxBxFFFUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxDFURxRxLxLxLFFFxFxFFFRxRxRxLxLBFBxBxBFBDFUxDxDFU', 'ULFRBD'),
             ('DFUxUxDFURxRxLxRxRFFBxFxFFBLxLxRxLxLFFBxBxFFBUFDxDxUFD', 'ULFRBD'),
             ('DFUxUxUFDLxLxLxLxLFFBxFxBFFRxRxRxRxRBFFxBxFFBUFDxDxDFU', 'ULFRBD'),
             ('DFUxUxUFDLxLxLxRxRFFBxFxFFBRxRxRxLxLBFFxBxBFFUFDxDxDFU', 'ULFRBD'),
             ('DFUxUxUFDLxRxLxLxRBFBxFxFFFRxLxRxRxLFFFxBxBFBUFDxDxDFU', 'ULFRBD'),
             ('DFUxUxUFDLxRxLxRxLBFBxFxBFBRxLxRxLxRFFFxBxFFFUFDxDxDFU', 'ULFRBD'),
             ('DFUxUxUFDRxLxLxLxRFFFxFxFFFLxRxRxRxLBFBxBxBFBUFDxDxDFU', 'ULFRBD'),
             ('DFUxUxUFDRxLxLxRxLFFFxFxBFBLxRxRxLxRBFBxBxFFFUFDxDxDFU', 'ULFRBD'),
             ('DFUxUxUFDRxRxLxLxLBFFxFxBFFLxLxRxRxRFFBxBxFFBUFDxDxDFU', 'ULFRBD'),
             ('DFUxUxUFDRxRxLxRxRBFFxFxFFBLxLxRxLxLFFBxBxBFFUFDxDxDFU', 'ULFRBD'),
             ('UFDxUxDFULxLxLxLxLBFFxFxFFBRxRxRxRxRFFBxBxBFFDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxDFULxLxLxRxRBFFxFxBFFRxRxRxLxLFFBxBxFFBDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxDFULxRxLxLxRFFFxFxBFBRxLxRxRxLBFBxBxFFFDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxDFULxRxLxRxLFFFxFxFFFRxLxRxLxRBFBxBxBFBDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxDFURxLxLxLxRBFBxFxBFBLxRxRxRxLFFFxBxFFFDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxDFURxLxLxRxLBFBxFxFFFLxRxRxLxRFFFxBxBFBDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxDFURxRxLxLxLFFBxFxFFBLxLxRxRxRBFFxBxBFFDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxDFURxRxLxRxRFFBxFxBFFLxLxRxLxLBFFxBxFFBDFUxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDLxLxLxLxLFFBxFxFFBRxRxRxRxRFFBxBxFFBDFUxDxDFU', 'ULFRBD'),
             ('UFDxUxUFDLxLxLxRxRFFBxFxFFBRxRxRxLxLFFBxBxFFBUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDLxLxLxRxRFFFxFxBFBLxLxRxRxRBFBxBxFFFDFUxDxDFU', 'ULFRBD'),
             ('UFDxUxUFDLxLxLxRxRFFFxFxFFFLxLxRxRxRBFBxBxBFBUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDLxRxLxLxRBFBxFxFFFRxLxRxRxLBFBxBxFFFUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDLxRxLxLxRBFFxFxBFFLxRxRxLxRFFBxBxFFBDFUxDxDFU', 'ULFRBD'),
             ('UFDxUxUFDLxRxLxLxRBFFxFxFFBLxRxRxLxRFFBxBxBFFUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDLxRxLxRxLBFBxFxFFFRxLxRxLxRBFBxBxFFFDFUxDxDFU', 'ULFRBD'),
             ('UFDxUxUFDRxLxLxLxRFFFxFxBFBLxRxRxRxLFFFxBxBFBDFUxDxDFU', 'ULFRBD'),
             ('UFDxUxUFDRxLxLxRxLFFBxFxBFFRxLxRxRxLBFFxBxFFBUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDRxLxLxRxLFFBxFxFFBRxLxRxRxLBFFxBxBFFDFUxDxDFU', 'ULFRBD'),
             ('UFDxUxUFDRxLxLxRxLFFFxFxBFBLxRxRxLxRFFFxBxBFBUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDRxRxLxLxLBFBxFxBFBRxRxRxLxLFFFxBxFFFUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDRxRxLxLxLBFBxFxFFFRxRxRxLxLFFFxBxBFBDFUxDxDFU', 'ULFRBD'),
             ('UFDxUxUFDRxRxLxLxLBFFxFxBFFLxLxRxRxRBFFxBxBFFUFDxDxUFD', 'ULFRBD'),
             ('UFDxUxUFDRxRxLxRxRBFFxFxBFFLxLxRxLxLBFFxBxBFFDFUxDxDFU', 'ULFRBD'),
             ('UFUxUxDFDLxLxLxLxLBFBxFxFFFRxRxRxRxRBFBxBxFFFDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxDFDLxLxLxRxRBFBxFxFFFRxRxRxLxLBFBxBxFFFUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDLxLxLxRxRBFFxFxBFFLxLxRxRxRFFBxBxFFBDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxDFDLxLxLxRxRBFFxFxFFBLxLxRxRxRFFBxBxBFFUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDLxRxLxLxRFFBxFxFFBRxLxRxRxLFFBxBxFFBUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDLxRxLxLxRFFFxFxBFBLxRxRxLxRBFBxBxFFFDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxDFDLxRxLxLxRFFFxFxFFFLxRxRxLxRBFBxBxBFBUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDLxRxLxRxLFFBxFxFFBRxLxRxLxRFFBxBxFFBDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxDFDRxLxLxLxRBFFxFxBFFLxRxRxRxLBFFxBxBFFDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxDFDRxLxLxRxLBFBxFxBFBRxLxRxRxLFFFxBxFFFUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDRxLxLxRxLBFBxFxFFFRxLxRxRxLFFFxBxBFBDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxDFDRxLxLxRxLBFFxFxBFFLxRxRxLxRBFFxBxBFFUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDRxRxLxLxLFFBxFxBFFRxRxRxLxLBFFxBxFFBUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDRxRxLxLxLFFBxFxFFBRxRxRxLxLBFFxBxBFFDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxDFDRxRxLxLxLFFFxFxBFBLxLxRxRxRFFFxBxBFBUFUxDxDFD', 'ULFRBD'),
             ('UFUxUxDFDRxRxLxRxRFFFxFxBFBLxLxRxLxLFFFxBxBFBDFDxDxUFU', 'ULFRBD'),
             ('UFUxUxUFULxLxLxLxLFFFxFxFFFRxRxRxRxRBFBxBxBFBDFDxDxDFD', 'ULFRBD'),
             ('UFUxUxUFULxLxLxRxRFFFxFxBFBRxRxRxLxLBFBxBxFFFDFDxDxDFD', 'ULFRBD'),
             ('UFUxUxUFULxRxLxLxRBFFxFxBFFRxLxRxRxLFFBxBxFFBDFDxDxDFD', 'ULFRBD'),
             ('UFUxUxUFULxRxLxRxLBFFxFxFFBRxLxRxLxRFFBxBxBFFDFDxDxDFD', 'ULFRBD'),
             ('UFUxUxUFURxLxLxLxRFFBxFxBFFLxRxRxRxLBFFxBxFFBDFDxDxDFD', 'ULFRBD'),
             ('UFUxUxUFURxLxLxRxLFFBxFxFFBLxRxRxLxRBFFxBxBFFDFDxDxDFD', 'ULFRBD'),
             ('UFUxUxUFURxRxLxLxLBFBxFxFFFLxLxRxRxRFFFxBxBFBDFDxDxDFD', 'ULFRBD'),
             ('UFUxUxUFURxRxLxRxRBFBxFxBFBLxLxRxLxLFFFxBxFFFDFDxDxDFD', 'ULFRBD'),
            )
        )


class Build333Phase3Corners(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase3Corners',

            # illegal moves
            ("L", "L'", "R", "R'", "F", "F'", "B", "B'"),

            '3x3x3',
            'lookup-table-3x3x3-step132-corners.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        U x U
        x U x
        U x U

 L x L  F x F  R x R  B x B
 x L x  x F x  x R x  x B x
 L x L  F x F  R x R  B x B

        D x D
        x D x
        D x D""", 'ascii'),),
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


class Build333Phase4Edges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase4-edges',

            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'", "U", "U'", "D", "D'"),

            '3x3x3',
            'lookup-table-3x3x3-step141-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        . U .
        U . U
        . U .

 . L .  . F .  . R .  . B .
 L . L  F . F  R . R  B . B
 . L .  . F .  . R .  . B .

        . D .
        D . D
        . D .""", 'ascii'),),
        )


class Build333Phase4Corners(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase4-corners',

            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'", "U", "U'", "D", "D'"),

            '3x3x3',
            'lookup-table-3x3x3-step142-corners.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        U . U
        . . .
        U . U

 L . L  F . F  R . R  B . B
 . . .  . . .  . . .  . . .
 L . L  F . F  R . R  B . B

        D . D
        . . .
        D . D""", 'ascii'),),
        )

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
            ("L", "L'", "R", "R'"),

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


class Build333Phase2Edges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase2-edges',

            # illegal moves
            ("L", "L'", "R", "R'"),

            '3x3x3',
            'lookup-table-3x3x3-step121-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        . x .
        x . x
        . x .

 . x .  . x .  . x .  . x .
 1 . 1  1 . 1  1 . 1  1 . 1
 . x .  . x .  . x .  . x .

        . x .
        x . x
        . x .""", 'ascii'),),
        )


class Build333Phase2Corners(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase2-corners',

            # illegal moves
            ("L", "L'", "R", "R'"),

            '3x3x3',
            'lookup-table-3x3x3-step122-corners.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        U . U
        . . .
        U . U

 x . x  x . x  x . x  x . x
 . . .  . . .  . . .  . . .
 x . x  x . x  x . x  x . x

        U . U
        . . .
        U . U""", 'ascii'),),
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


class Build333Phase3Edges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase-edges',

            # illegal moves
            ("L", "L'", "R", "R'", "F", "F'", "B", "B'"),

            '3x3x3',
            'lookup-table-3x3x3-step131-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        . F .
        x . x
        . F .

 . x .  . F .  . x .  . F .
 x . x  x . x  x . x  x . x
 . x .  . F .  . x .  . F .

        . F .
        x . x
        . F .
        """, 'ascii'),),
        )


class Build333Phase3Corners(BFS):

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase3-corners',

            # illegal moves
            ("L", "L'", "R", "R'", "F", "F'", "B", "B'"),

            '3x3x3',
            'lookup-table-3x3x3-step132-corners.txt',
            False, # store_as_hex

            # starting cubes
            (('D.D...D.DL.L...L.LB.B...B.BR.R...R.RF.F...F.FU.U...U.U', 'ULFRBD'),
             ('D.D...D.DL.L...R.RB.B...F.FR.R...L.LF.F...B.BU.U...U.U', 'ULFRBD'),
             ('D.D...D.DL.R...L.RF.B...F.BR.L...R.LB.F...B.FU.U...U.U', 'ULFRBD'),
             ('D.D...D.DL.R...R.LF.B...B.FR.L...L.RB.F...F.BU.U...U.U', 'ULFRBD'),
             ('D.D...D.DR.L...L.RB.F...F.BL.R...R.LF.B...B.FU.U...U.U', 'ULFRBD'),
             ('D.D...D.DR.L...R.LB.F...B.FL.R...L.RF.B...F.BU.U...U.U', 'ULFRBD'),
             ('D.D...D.DR.R...L.LF.F...B.BL.L...R.RB.B...F.FU.U...U.U', 'ULFRBD'),
             ('D.D...D.DR.R...R.RF.F...F.FL.L...L.LB.B...B.BU.U...U.U', 'ULFRBD'),
             ('D.D...U.UL.L...L.LF.F...B.BR.R...R.RF.F...B.BU.U...D.D', 'ULFRBD'),
             ('D.D...U.UL.L...R.RF.B...B.FL.L...R.RB.F...F.BD.D...U.U', 'ULFRBD'),
             ('D.D...U.UL.L...R.RF.B...F.BL.L...R.RB.F...B.FU.U...D.D', 'ULFRBD'),
             ('D.D...U.UL.L...R.RF.F...B.BR.R...L.LF.F...B.BD.D...U.U', 'ULFRBD'),
             ('D.D...U.UL.R...L.RB.B...B.BL.R...L.RF.F...F.FD.D...U.U', 'ULFRBD'),
             ('D.D...U.UL.R...L.RB.B...F.FL.R...L.RF.F...B.BU.U...D.D', 'ULFRBD'),
             ('D.D...U.UL.R...L.RB.F...B.FR.L...R.LB.F...B.FD.D...U.U', 'ULFRBD'),
             ('D.D...U.UL.R...R.LB.F...B.FR.L...L.RB.F...B.FU.U...D.D', 'ULFRBD'),
             ('D.D...U.UR.L...L.RF.B...F.BL.R...R.LF.B...F.BU.U...D.D', 'ULFRBD'),
             ('D.D...U.UR.L...R.LF.B...F.BL.R...L.RF.B...F.BD.D...U.U', 'ULFRBD'),
             ('D.D...U.UR.L...R.LF.F...B.BR.L...R.LB.B...F.FU.U...D.D', 'ULFRBD'),
             ('D.D...U.UR.L...R.LF.F...F.FR.L...R.LB.B...B.BD.D...U.U', 'ULFRBD'),
             ('D.D...U.UR.R...L.LB.B...F.FL.L...R.RB.B...F.FD.D...U.U', 'ULFRBD'),
             ('D.D...U.UR.R...L.LB.F...B.FR.R...L.LF.B...F.BU.U...D.D', 'ULFRBD'),
             ('D.D...U.UR.R...L.LB.F...F.BR.R...L.LF.B...B.FD.D...U.U', 'ULFRBD'),
             ('D.D...U.UR.R...R.RB.B...F.FL.L...L.LB.B...F.FU.U...D.D', 'ULFRBD'),
             ('D.U...D.UL.L...L.LB.F...B.FR.R...R.RB.F...B.FU.D...U.D', 'ULFRBD'),
             ('D.U...D.UL.L...R.RB.B...B.BL.L...R.RF.F...F.FD.U...D.U', 'ULFRBD'),
             ('D.U...D.UL.L...R.RB.B...F.FL.L...R.RF.F...B.BU.D...U.D', 'ULFRBD'),
             ('D.U...D.UL.L...R.RB.F...B.FR.R...L.LB.F...B.FD.U...D.U', 'ULFRBD'),
             ('D.U...D.UL.R...L.RF.B...B.FL.R...L.RB.F...F.BD.U...D.U', 'ULFRBD'),
             ('D.U...D.UL.R...L.RF.B...F.BL.R...L.RB.F...B.FU.D...U.D', 'ULFRBD'),
             ('D.U...D.UL.R...L.RF.F...B.BR.L...R.LF.F...B.BD.U...D.U', 'ULFRBD'),
             ('D.U...D.UL.R...R.LF.F...B.BR.L...L.RF.F...B.BU.D...U.D', 'ULFRBD'),
             ('D.U...D.UR.L...L.RB.B...F.FL.R...R.LB.B...F.FU.D...U.D', 'ULFRBD'),
             ('D.U...D.UR.L...R.LB.B...F.FL.R...L.RB.B...F.FD.U...D.U', 'ULFRBD'),
             ('D.U...D.UR.L...R.LB.F...B.FR.L...R.LF.B...F.BU.D...U.D', 'ULFRBD'),
             ('D.U...D.UR.L...R.LB.F...F.BR.L...R.LF.B...B.FD.U...D.U', 'ULFRBD'),
             ('D.U...D.UR.R...L.LF.B...F.BL.L...R.RF.B...F.BD.U...D.U', 'ULFRBD'),
             ('D.U...D.UR.R...L.LF.F...B.BR.R...L.LB.B...F.FU.D...U.D', 'ULFRBD'),
             ('D.U...D.UR.R...L.LF.F...F.FR.R...L.LB.B...B.BD.U...D.U', 'ULFRBD'),
             ('D.U...D.UR.R...R.RF.B...F.BL.L...L.LF.B...F.BU.D...U.D', 'ULFRBD'),
             ('D.U...U.DL.L...L.LF.B...B.FR.R...R.RB.F...F.BU.D...D.U', 'ULFRBD'),
             ('D.U...U.DL.L...R.RF.B...F.BR.R...L.LB.F...B.FU.D...D.U', 'ULFRBD'),
             ('D.U...U.DL.R...L.RB.B...F.FR.L...R.LF.F...B.BU.D...D.U', 'ULFRBD'),
             ('D.U...U.DL.R...R.LB.B...B.BR.L...L.RF.F...F.FU.D...D.U', 'ULFRBD'),
             ('D.U...U.DR.L...L.RF.F...F.FL.R...R.LB.B...B.BU.D...D.U', 'ULFRBD'),
             ('D.U...U.DR.L...R.LF.F...B.BL.R...L.RB.B...F.FU.D...D.U', 'ULFRBD'),
             ('D.U...U.DR.R...L.LB.F...B.FL.L...R.RF.B...F.BU.D...D.U', 'ULFRBD'),
             ('D.U...U.DR.R...R.RB.F...F.BL.L...L.LF.B...B.FU.D...D.U', 'ULFRBD'),
             ('U.D...D.UL.L...L.LB.F...F.BR.R...R.RF.B...B.FD.U...U.D', 'ULFRBD'),
             ('U.D...D.UL.L...R.RB.F...B.FR.R...L.LF.B...F.BD.U...U.D', 'ULFRBD'),
             ('U.D...D.UL.R...L.RF.F...B.BR.L...R.LB.B...F.FD.U...U.D', 'ULFRBD'),
             ('U.D...D.UL.R...R.LF.F...F.FR.L...L.RB.B...B.BD.U...U.D', 'ULFRBD'),
             ('U.D...D.UR.L...L.RB.B...B.BL.R...R.LF.F...F.FD.U...U.D', 'ULFRBD'),
             ('U.D...D.UR.L...R.LB.B...F.FL.R...L.RF.F...B.BD.U...U.D', 'ULFRBD'),
             ('U.D...D.UR.R...L.LF.B...F.BL.L...R.RB.F...B.FD.U...U.D', 'ULFRBD'),
             ('U.D...D.UR.R...R.RF.B...B.FL.L...L.LB.F...F.BD.U...U.D', 'ULFRBD'),
             ('U.D...U.DL.L...L.LF.B...F.BR.R...R.RF.B...F.BD.U...D.U', 'ULFRBD'),
             ('U.D...U.DL.L...R.RF.B...F.BR.R...L.LF.B...F.BU.D...U.D', 'ULFRBD'),
             ('U.D...U.DL.L...R.RF.F...B.BL.L...R.RB.B...F.FD.U...D.U', 'ULFRBD'),
             ('U.D...U.DL.L...R.RF.F...F.FL.L...R.RB.B...B.BU.D...U.D', 'ULFRBD'),
             ('U.D...U.DL.R...L.RB.B...F.FR.L...R.LB.B...F.FU.D...U.D', 'ULFRBD'),
             ('U.D...U.DL.R...L.RB.F...B.FL.R...L.RF.B...F.BD.U...D.U', 'ULFRBD'),
             ('U.D...U.DL.R...L.RB.F...F.BL.R...L.RF.B...B.FU.D...U.D', 'ULFRBD'),
             ('U.D...U.DL.R...R.LB.B...F.FR.L...L.RB.B...F.FD.U...D.U', 'ULFRBD'),
             ('U.D...U.DR.L...L.RF.F...B.BL.R...R.LF.F...B.BD.U...D.U', 'ULFRBD'),
             ('U.D...U.DR.L...R.LF.B...B.FR.L...R.LB.F...F.BU.D...U.D', 'ULFRBD'),
             ('U.D...U.DR.L...R.LF.B...F.BR.L...R.LB.F...B.FD.U...D.U', 'ULFRBD'),
             ('U.D...U.DR.L...R.LF.F...B.BL.R...L.RF.F...B.BU.D...U.D', 'ULFRBD'),
             ('U.D...U.DR.R...L.LB.B...B.BR.R...L.LF.F...F.FU.D...U.D', 'ULFRBD'),
             ('U.D...U.DR.R...L.LB.B...F.FR.R...L.LF.F...B.BD.U...D.U', 'ULFRBD'),
             ('U.D...U.DR.R...L.LB.F...B.FL.L...R.RB.F...B.FU.D...U.D', 'ULFRBD'),
             ('U.D...U.DR.R...R.RB.F...B.FL.L...L.LB.F...B.FD.U...D.U', 'ULFRBD'),
             ('U.U...D.DL.L...L.LB.B...F.FR.R...R.RB.B...F.FD.D...U.U', 'ULFRBD'),
             ('U.U...D.DL.L...R.RB.B...F.FR.R...L.LB.B...F.FU.U...D.D', 'ULFRBD'),
             ('U.U...D.DL.L...R.RB.F...B.FL.L...R.RF.B...F.BD.D...U.U', 'ULFRBD'),
             ('U.U...D.DL.L...R.RB.F...F.BL.L...R.RF.B...B.FU.U...D.D', 'ULFRBD'),
             ('U.U...D.DL.R...L.RF.B...F.BR.L...R.LF.B...F.BU.U...D.D', 'ULFRBD'),
             ('U.U...D.DL.R...L.RF.F...B.BL.R...L.RB.B...F.FD.D...U.U', 'ULFRBD'),
             ('U.U...D.DL.R...L.RF.F...F.FL.R...L.RB.B...B.BU.U...D.D', 'ULFRBD'),
             ('U.U...D.DL.R...R.LF.B...F.BR.L...L.RF.B...F.BD.D...U.U', 'ULFRBD'),
             ('U.U...D.DR.L...L.RB.F...B.FL.R...R.LB.F...B.FD.D...U.U', 'ULFRBD'),
             ('U.U...D.DR.L...R.LB.B...B.BR.L...R.LF.F...F.FU.U...D.D', 'ULFRBD'),
             ('U.U...D.DR.L...R.LB.B...F.FR.L...R.LF.F...B.BD.D...U.U', 'ULFRBD'),
             ('U.U...D.DR.L...R.LB.F...B.FL.R...L.RB.F...B.FU.U...D.D', 'ULFRBD'),
             ('U.U...D.DR.R...L.LF.B...B.FR.R...L.LB.F...F.BU.U...D.D', 'ULFRBD'),
             ('U.U...D.DR.R...L.LF.B...F.BR.R...L.LB.F...B.FD.D...U.U', 'ULFRBD'),
             ('U.U...D.DR.R...L.LF.F...B.BL.L...R.RF.F...B.BU.U...D.D', 'ULFRBD'),
             ('U.U...D.DR.R...R.RF.F...B.BL.L...L.LF.F...B.BD.D...U.U', 'ULFRBD'),
             ('U.U...U.UL.L...L.LF.F...F.FR.R...R.RB.B...B.BD.D...D.D', 'ULFRBD'),
             ('U.U...U.UL.L...R.RF.F...B.BR.R...L.LB.B...F.FD.D...D.D', 'ULFRBD'),
             ('U.U...U.UL.R...L.RB.F...B.FR.L...R.LF.B...F.BD.D...D.D', 'ULFRBD'),
             ('U.U...U.UL.R...R.LB.F...F.BR.L...L.RF.B...B.FD.D...D.D', 'ULFRBD'),
             ('U.U...U.UR.L...L.RF.B...B.FL.R...R.LB.F...F.BD.D...D.D', 'ULFRBD'),
             ('U.U...U.UR.L...R.LF.B...F.BL.R...L.RB.F...B.FD.D...D.D', 'ULFRBD'),
             ('U.U...U.UR.R...L.LB.B...F.FL.L...R.RF.F...B.BD.D...D.D', 'ULFRBD'),
             ('U.U...U.UR.R...R.RB.B...B.BL.L...L.LF.F...F.FD.D...D.D', 'ULFRBD'),
            )
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

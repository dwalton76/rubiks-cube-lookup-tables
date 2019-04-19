#!/usr/bin/e nv python3

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



# Implement your own kociemba two-phase 3x3x3 solver someday...
# http://kociemba.org/math/twophase.htm
# https://ruwix.com/the-rubiks-cube/herbert-kociemba-optimal-cube-solver-cube-explorer/

# phase1
# - the orientations of all corners and all edges are 0.
# - the four edges in the UD-slice (between the U-face and D-face) stay isolated in that slice
class Build333KociembaPhase1EdgesOnly(BFS):
    """
    TODO when we build this table we need to change a UU edge to DD when the orientation flips.
    EO for an edge would flip if
    - it is at LF/LB and you do a L or L'
    - it is as RF/RB and you do a R or R'
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase1-edges-only',

            # illegal moves
            (),

            '3x3x3',
            'lookup-table-3x3x3-step11-phase1-edges-only.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        . U .
        U U U
        . U .

 . U .  . U .  . U .  . U .
 - L -  - F -  - R -  - B -
 . U .  . U .  . U .  . U .

        . U .
        U D U
        . U .""", 'ascii'),),
        )



class StartingStates333KociembaPhase1XPlaneEdgesOnly(BFS):
    """
    We need the x-plane edges to be in the x-plane and EOed
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase1-x-plane-edges-only',

            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'"),

            '3x3x3',
            'starting-states-lookup-table-3x3x3-step12-phase1-x-plane-edges-only.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        . - .
        - U -
        . - .

 . - .  . - .  . - .  . - .
 L L L  F F F  R R R  B B B
 . - .  . - .  . - .  . - .

        . - .
        - D -
        . - .""", 'ascii'),),
        )


class Build333KociembaPhase1XPlaneEdgesOnly(BFS):
    """
    lookup-table-3x3x3-step12-phase1-x-plane-edges-only.txt
    =======================================================
    1 steps has 120 entries (0 percent, 0.00x previous step)
    2 steps has 1,200 entries (0 percent, 10.00x previous step)
    3 steps has 10,944 entries (5 percent, 9.12x previous step)
    4 steps has 46,896 entries (24 percent, 4.29x previous step)
    5 steps has 92,736 entries (48 percent, 1.98x previous step)
    6 steps has 36,456 entries (19 percent, 0.39x previous step)
    7 steps has 1,728 entries (0 percent, 0.05x previous step)

    Total: 190,080 entries
    Average: 4.83 moves
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase1-x-plane-edges-only',

            # illegal moves
            (),

            '3x3x3',
            'lookup-table-3x3x3-step12-phase1-x-plane-edges-only.txt',
            False, # store_as_hex

            # starting cubes
            (('.-.-U-.-..-.LLL.-..-.BFB.-..-.RRR.-..-.FBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLL.-..-.BFF.-..-.RRR.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLL.-..-.FFB.-..-.RRR.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLL.-..-.FFF.-..-.RRR.-..-.BBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.BFB.-..-.LRR.-..-.FBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.BFF.-..-.LRR.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.BFF.-..-.RRL.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.BFF.-..-.RRL.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.FFB.-..-.LRR.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.FFB.-..-.RRL.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.FFB.-..-.RRL.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.LLR.-..-.FFF.-..-.LRR.-..-.BBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.BFB.-..-.RRL.-..-.FBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.BFF.-..-.LRR.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.BFF.-..-.LRR.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.BFF.-..-.RRL.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.FFB.-..-.LRR.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.FFB.-..-.LRR.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.FFB.-..-.RRL.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLL.-..-.FFF.-..-.RRL.-..-.BBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLR.-..-.BFB.-..-.LRL.-..-.FBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLR.-..-.BFF.-..-.LRL.-..-.BBF.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLR.-..-.FFB.-..-.LRL.-..-.FBB.-..-.-D-.-.', 'ULFRBD'),
             ('.-.-U-.-..-.RLR.-..-.FFF.-..-.LRL.-..-.BBB.-..-.-D-.-.', 'ULFRBD'))
        )


class Build333KociembaPhase1CornersOnly(BFS):
    """
    TODO: A corner can be at orientation 0, 1 or 2...we need to be able to cycle
    between them as we are building this table.
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase1-corners-only',

            # illegal moves
            (),

            '3x3x3',
            'lookup-table-3x3x3-step13-phase1-corners-only.txt',
            False, # store_as_hex

            # starting cubes
            (("""
        0 . 0
        . U .
        0 . 0

 0 . 0  0 . 0  0 . 0  0 . 0
 . L .  . F .  . R .  . B .
 0 . 0  0 . 0  0 . 0  0 . 0

        0 . 0
        . D .
        0 . 0""", 'ascii'),),
        )


class Build333KociembaPhase2EdgesOnly(BFS):
    """
    lookup-table-3x3x3-step21-phase2-edges-only.txt
    ===============================================
    1 steps has 10 entries (0 percent, 0.00x previous step)
    2 steps has 67 entries (0 percent, 6.70x previous step)
    3 steps has 456 entries (0 percent, 6.81x previous step)
    4 steps has 3,063 entries (0 percent, 6.72x previous step)
    5 steps has 18,202 entries (1 percent, 5.94x previous step)
    6 steps has 86,691 entries (8 percent, 4.76x previous step)
    7 steps has 290,812 entries (30 percent, 3.35x previous step)
    8 steps has 434,814 entries (44 percent, 1.50x previous step)
    9 steps has 120,488 entries (12 percent, 0.28x previous step)
    10 steps has 11,818 entries (1 percent, 0.10x previous step)
    11 steps has 1,114 entries (0 percent, 0.09x previous step)
    12 steps has 144 entries (0 percent, 0.13x previous step)

    Total: 967,679 entries
    Average: 7.60 moves
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase2-edges-only',

            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'"),

            '3x3x3',
            'lookup-table-3x3x3-step21-phase2-edges-only.txt',
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


class Build333KociembaPhase2CornersOnly(BFS):
    """
    lookup-table-3x3x3-step22-phase2-corners-only.txt
    =================================================
    1 steps has 10 entries (0 percent, 0.00x previous step)
    2 steps has 67 entries (0 percent, 6.70x previous step)
    3 steps has 330 entries (0 percent, 4.93x previous step)
    4 steps has 752 entries (1 percent, 2.28x previous step)
    5 steps has 1,400 entries (3 percent, 1.86x previous step)
    6 steps has 2,752 entries (6 percent, 1.97x previous step)
    7 steps has 4,384 entries (10 percent, 1.59x previous step)
    8 steps has 6,208 entries (15 percent, 1.42x previous step)
    9 steps has 7,136 entries (17 percent, 1.15x previous step)
    10 steps has 8,064 entries (20 percent, 1.13x previous step)
    11 steps has 6,528 entries (16 percent, 0.81x previous step)
    12 steps has 2,432 entries (6 percent, 0.37x previous step)
    13 steps has 256 entries (0 percent, 0.11x previous step)

    Total: 40,319 entries
    Average: 8.86 moves
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase2-corners-only',

            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'"),

            '3x3x3',
            'lookup-table-3x3x3-step22-phase2-corners-only.txt',
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


class Build333KociembaPhase2(BFS):
    """
    lookup-table-3x3x3-step20-phase2.txt
    ====================================
    1 steps has 10 entries (0 percent, 0.00x previous step)
    2 steps has 67 entries (0 percent, 6.70x previous step)
    3 steps has 456 entries (0 percent, 6.81x previous step)
    4 steps has 3,079 entries (0 percent, 6.75x previous step)
    5 steps has 19,948 entries (2 percent, 6.48x previous step)
    6 steps has 123,074 entries (13 percent, 6.17x previous step)
    7 steps has 736,850 entries (83 percent, 5.99x previous step)

    Total: 883,484 entries
    """

    def __init__(self):
        BFS.__init__(self,
            '3x3x3-phase2',

            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'"),

            '3x3x3',
            'lookup-table-3x3x3-step20-phase2.txt',
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

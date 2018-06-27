#!/usr/bin/env python3

from buildercore import BFS
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)


class StartingStates444UDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-UD-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step11-UD-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . x x .  . x x .  . x x .
 . x x .  . x x .  . x x .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class StartingStates444LRCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LR-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step12-LR-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . L L .  . x x .
 . L L .  . x x .  . L L .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class StartingStates444FBCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-FB-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step13-FB-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . F F .  . x x .  . F F .
 . x x .  . F F .  . x x .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class StartingStates444ULFRBDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-ULFRBD-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step10-ULFRBD-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . L L .  . F F .
 . L L .  . F F .  . L L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class Build444UDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-UD-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step11-UD-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('.....UU..UU..........xx..xx..........xx..xx..........xx..xx..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....xx..xx..........UU..UU..........xx..xx..........UU..UU..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........xx..xx..........UU..UU..........xx..xx..........UU..UU..........xx..xx.....', 'ULFRBD')),
            use_cost_only=True
        )


class Build444LRCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LR-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step12-LR-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('.....LL..LL..........xx..xx..........xx..xx..........xx..xx..........xx..xx..........LL..LL.....', 'ULFRBD'),
             ('.....xx..xx..........LL..LL..........xx..xx..........LL..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........xx..xx..........LL..LL..........xx..xx..........LL..LL..........xx..xx.....', 'ULFRBD')),
            use_cost_only=True
        )


class Build444FBCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-FB-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step13-FB-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('.....FF..FF..........xx..xx..........xx..xx..........xx..xx..........xx..xx..........FF..FF.....', 'ULFRBD'),
             ('.....xx..xx..........FF..FF..........xx..xx..........FF..FF..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........xx..xx..........FF..FF..........xx..xx..........FF..FF..........xx..xx.....', 'ULFRBD'),),
            use_cost_only=True
        )


class Build444ULFRBDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-ULFRBD-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (('.....FF..FF..........LL..LL..........UU..UU..........LL..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........UU..UU..........LL..LL..........UU..UU..........LL..LL..........FF..FF.....', 'ULFRBD'),
             ('.....LL..LL..........FF..FF..........UU..UU..........FF..FF..........UU..UU..........LL..LL.....', 'ULFRBD'),
             ('.....LL..LL..........UU..UU..........FF..FF..........UU..UU..........FF..FF..........LL..LL.....', 'ULFRBD'),
             ('.....UU..UU..........FF..FF..........LL..LL..........FF..FF..........LL..LL..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..LL..........FF..FF..........LL..LL..........FF..FF..........UU..UU.....', 'ULFRBD'))
        )



class Build444TsaiPhase1Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase1-centers',
            (),
            '4x4x4',
            'lookup-table-4x4x4-step50-tsai-phase1.txt',
            True, # store_as_hex

            # starting cubes
            (
             ("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . L L .  . x x .
 . L L .  . x x .  . L L .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),
            ))


class Build444TsaiPhase2Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-centers',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'lookup-table-4x4x4-step61-tsai-phase2-centers.txt',
            False, # store_as_hex

            # starting cubes
            (
            # There are 12 goal states for LR centers
            # goal 1 - LR centers solved
             ("""
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
          . . . .""", 'ascii'),

            # goal 2 - LR centers swapped
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R R .  . F F .  . L L .  . F F .
 . R R .  . F F .  . L L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 3 - horizontal bars 1
            # https://alg.cubing.net/?puzzle=4x4x4&setup=R2_2F2_2U2_2F2_2U2_R2
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R R .  . F F .  . L L .  . F F .
 . L L .  . F F .  . R R .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 4 - horizontal bars 2
            # https://alg.cubing.net/?puzzle=4x4x4&setup=R2_2F2_2U2_2F2_2U2_R2
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R R .  . F F .  . R R .  . F F .
 . L L .  . F F .  . L L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 5 - horizontal bars 3
            # https://alg.cubing.net/?puzzle=4x4x4&setup=R2_2F2_2D2_2F2_2D2_R2
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . L L .  . F F .
 . R R .  . F F .  . R R .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 6 - horizontal bars 4
            # https://alg.cubing.net/?puzzle=4x4x4&setup=2F2_2D2_2F2_2D2
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . F F .
 . R R .  . F F .  . L L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),


            # goal 7 - vertical bars 1
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R L .  . F F .  . R L .  . F F .
 . R L .  . F F .  . R L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 8 - vertical bars 2
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R L .  . F F .  . L R .  . F F .
 . R L .  . F F .  . L R .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 9 - vertical bars 3
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L R .  . F F .  . R L .  . F F .
 . L R .  . F F .  . R L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 10 - vertical bars 4
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L R .  . F F .  . L R .  . F F .
 . L R .  . F F .  . L R .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 11 - checkerboard 1
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R L .  . F F .  . L R .  . F F .
 . L R .  . F F .  . R L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            # goal 12 - checkerboard 2
             ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L R .  . F F .  . R L .  . F F .
 . R L .  . F F .  . L R .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),
            ))


class StartingStates444TsaiPhase2EdgesAndLRCenters(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-edges-and-LR-centers',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'", "R", "R'",
             "Lw", "Lw'", "Rw", "Rw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step62-tsai-phase2-edges-and-LR-centers.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U . . D  D R R U  U . . D
 U L L D  D . . U  U R R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .""", 'ascii'),)
        )


class Build444TsaiPhase2EdgesAndLRCenters(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-edges-and-LR-centers',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'lookup-table-4x4x4-step62-tsai-phase2-edges-and-LR-centers.txt',
            False, # store_as_hex

            # starting cubes
            (
            # There are 12 goal states for the center
            # goal 1 - LR centers solved
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U . . D  D R R U  U . . D
 U L L D  D . . U  U R R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 2 - LR centers swapped
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D R R U  U . . D  D L L U  U . . D
 U R R D  D . . U  U L L D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 3 - horizontal bars 1
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D R R U  U . . D  D L L U  U . . D
 U L L D  D . . U  U R R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 4 - horizontal bars 2
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D R R U  U . . D  D R R U  U . . D
 U L L D  D . . U  U L L D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 5 - horizontal bars 3
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U . . D  D L L U  U . . D
 U R R D  D . . U  U R R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 6 - horizontal bars 4
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U . . D  D R R U  U . . D
 U R R D  D . . U  U L L D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 7 - vertical bars 1
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D R L U  U . . D  D R L U  U . . D
 U R L D  D . . U  U R L D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 8 - vertical bars 2
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D R L U  U . . D  D L R U  U . . D
 U R L D  D . . U  U L R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 9 - vertical bars 3
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L R U  U . . D  D R L U  U . . D
 U L R D  D . . U  U R L D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 10 - vertical bars 4
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L R U  U . . D  D L R U  U . . D
 U L R D  D . . U  U L R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 11 - checkerboard 1
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D R L U  U . . D  D L R U  U . . D
 U L R D  D . . U  U R L D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii'),

            # goal 12 - checkerboard 2
             ("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L R U  U . . D  D R L U  U . . D
 U R L D  D . . U  U L R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .
              """, 'ascii')
            ))


class StartingStatesBuild444Phase3Edges(BFS):
    """
    There should be 80,640 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase3-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step71-edges-split.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U U .
          U . . U
          U . . U
          . U U .

 . L L .  . F F .  . R R .  . B B .
 L . . L  F . . F  R . . R  B . . B
 L . . L  F . . F  R . . R  B . . B
 . L L .  . F F .  . R R .  . B B .

          . D D .
          D . . D
          D . . D
          . D D .""", 'ascii'),),
            use_edges_pattern=True
        )


class Build444Phase3Edges(BFS):
    """
    This is the TPR phase3 edges table. We will use this table to put the edges
    into one of 80,640 states that can be solved when F, F', B, B' are restricted.
    This table will have ~239 million entries.
    """

    def __init__(self):
        from builder444ss import starting_states_phase3_step71_edges

        BFS.__init__(self,
            '4x4x4-phase3-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step71-edges.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_phase3_step71_edges,
            use_edges_pattern=True
        )


class StartingStates444Phase3Corners(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase3-corners',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step72-corners.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_phase4_step72_corners
        )


class Build444Phase3Corners(BFS):
    """
    """
    # dwalton

    def __init__(self):
        from builder444ss import starting_states_phase3_step72_corners
        BFS.__init__(self,
            '4x4x4-phase3-corners',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step72-corners.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_phase3_step72_corners
        )


class Build444Phase4Edges(BFS):
    """
    """
    # dwalton

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase4-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),
            '4x4x4',
            'lookup-table-4x4x4-step81-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U U .
          U . . U
          U . . U
          . U U .

 . L L .  . F F .  . R R .  . B B .
 L . . L  F . . F  R . . R  B . . B
 L . . L  F . . F  R . . R  B . . B
 . L L .  . F F .  . R R .  . B B .

          . D D .
          D . . D
          D . . D
          . D D .""", 'ascii'),),
            use_edges_pattern=True
        )


class Build444Phase4Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase4-centers',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),
            '4x4x4',
            'lookup-table-4x4x4-step82-centers.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . B B .
 . L L .  . F F .  . R R .  . B B .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . D D .
          . D D .
          . . . .""", 'ascii'),),
        )

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


class StartingStates444TsaiPhase4SolveEdges64(BFS):
    """
    There should be 64 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-edges-stage64',
            ("U", "U'",
             "L", "L'",
             "F", "F'",
             "R", "R'",
             "B", "B'",
             "D", "D'",

             "Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             ),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step402-edges-stage64.txt',
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


class Build444TsaiPhase4SolveEdges64(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase4-edges64',
            ("Fw", "Fw'",
             "Uw", "Uw'",
             "Rw", "Rw'",
             "Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2",
             "R", "R'",
             "L", "L'"),
            '4x4x4',
            'lookup-table-4x4x4-step402-edges-stage64.txt',
            False, # store_as_hex

            # starting cubes
            (('.DD.D..DU..U.UU..LL.L..LR..R.RR..FF.F..BB..F.BB..LL.L..LR..R.RR..FF.B..FF..B.BB..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RL..R.LR..FF.B..FB..F.FF..RL.R..LR..L.RL..BB.B..FB..F.BB..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.DD..LL.L..LR..R.RR..BB.B..BF..F.FF..LL.L..LR..R.RR..FF.F..FB..B.BB..UU.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RR..L.RL..FF.B..FB..F.BB..RL.R..LL..R.LR..BB.B..FB..F.FF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DD.U..UU..U.UU..LL.L..LR..R.RR..FF.F..FB..B.BB..RR.R..RL..L.LL..FF.F..FB..B.BB..DD.D..DD..D.UU.', 'ULFRBD'),
             ('.DD.U..UU..U.UU..LL.R..LR..L.LL..FF.F..FF..F.FF..RR.R..LR..L.RR..BB.B..BB..B.BB..DD.D..DD..D.UU.', 'ULFRBD'),
             ('.UU.D..UD..U.UU..RR.R..RL..L.LL..FF.F..FB..B.BB..RR.R..RL..L.LL..BB.B..BF..F.FF..DD.U..DU..D.DD.', 'ULFRBD'),
             ('.UU.U..UU..U.UU..LL.L..LR..R.RR..FF.F..FB..B.BB..RR.R..RL..L.LL..BB.B..BF..F.FF..DD.D..DD..D.DD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LL.L..LR..R.RR..FF.F..FB..B.BB..RR.R..RL..L.LL..FF.F..FB..B.BB..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..RL.R..LR..L.RL..FF.F..FF..F.FF..RL.R..LR..L.RL..BB.B..BB..B.BB..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..UD..U.UU..LR.L..RR..L.RL..FF.F..FB..B.BB..RL.R..LL..R.LR..FF.F..FB..B.BB..DD.U..DU..D.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.DD..LL.L..LR..R.RR..BB.B..BF..F.FF..RR.R..RL..L.LL..FF.F..FB..B.BB..UU.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LL.L..LL..L.LL..FF.F..FB..B.BB..RR.R..RR..R.RR..FF.F..FB..B.BB..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..RL.R..LR..L.RL..FF.F..FF..F.BB..RL.R..LR..L.RL..BB.B..BB..B.FF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DD.D..UU..D.UU..RL.R..LR..L.RL..FF.F..FB..B.BB..LR.L..RL..R.LR..BB.B..BF..F.FF..UU.U..DD..U.DD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..RL.R..LR..L.RL..FF.F..FB..B.BB..RL.R..LR..L.RL..BB.B..BF..F.FF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DD.D..DD..D.DD..LR.L..LR..R.RL..FB.F..BB..F.BF..RL.L..LR..R.LR..BF.B..FF..B.FB..UU.U..UU..U.UU.', 'ULFRBD'),
             ('.DD.D..DD..D.DD..LR.L..RL..R.LR..FB.F..BF..B.FB..RL.R..LR..L.RL..BF.B..FB..F.BF..UU.U..UU..U.UU.', 'ULFRBD'),
             ('.DD.D..DD..D.DD..RL.R..LL..R.LR..BF.B..BF..F.FB..LR.L..RR..L.RL..FB.B..BF..F.BF..UU.U..UU..U.UU.', 'ULFRBD'),
             ('.DD.D..DD..D.DD..LR.L..RR..L.RL..FB.F..BB..F.BF..RL.R..LL..R.LR..BF.B..FF..B.FB..UU.U..UU..U.UU.', 'ULFRBD'),
             ('.DU.D..DD..D.DU..RR.R..RL..L.LL..BB.B..BF..F.FF..LL.L..LR..R.RR..BB.B..BF..F.FF..UD.U..UU..U.UD.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LL.L..RL..R.LL..FB.F..BF..B.FB..RR.L..RL..R.RR..BF.B..FB..F.BF..UD.U..DU..D.UD.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..RR.L..RR..L.LL..FF.F..FB..B.BB..RR.R..LL..R.LL..FF.F..FB..B.BB..UD.U..DU..D.UD.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LL.L..RL..R.RR..FB.F..BB..F.BF..RR.L..RL..R.LL..BF.B..FF..B.FB..DU.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..DU..U.DU..RR.R..RL..L.LL..BB.B..BF..F.FF..LL.L..LR..R.RR..BB.B..BF..F.FF..UD.D..DU..U.UD.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LR.L..RL..R.LR..FB.F..BF..B.FB..LR.L..RL..R.LR..BF.B..FB..F.BF..UD.U..DU..D.UD.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LR.L..RR..L.RL..FF.F..FB..B.BB..RL.R..LL..R.LR..FF.F..FB..B.BB..UD.U..DU..D.UD.', 'ULFRBD'),
             ('.DD.D..UD..U.DD..RL.R..LL..R.LR..BF.B..FF..B.FB..LR.L..RR..L.RL..FB.F..BB..F.BF..UU.U..DU..D.UU.', 'ULFRBD'),
             ('.DU.D..DU..U.DU..RL.R..RR..R.RL..BB.B..BF..F.FF..RL.L..LL..L.RL..BB.B..BF..F.FF..DU.U..UD..D.DU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LR.L..RL..R.LR..FB.F..BF..B.BF..LR.L..RL..R.LR..BF.B..FB..F.FB..DU.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LR.L..RL..R.LR..FB.F..FB..B.BF..RL.R..LR..L.RL..BF.F..FB..B.FB..DU.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LR.L..RL..R.LR..FB.F..BB..F.BF..LR.L..RL..R.LR..BF.B..FF..B.FB..DU.D..UD..U.DU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LL.L..LR..R.RR..FB.F..BB..F.BF..LL.L..LR..R.RR..BF.B..FF..B.FB..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RL..R.LR..BF.B..FB..F.BF..RL.R..LR..L.RL..BF.B..FB..F.BF..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DU.D..DU..U.DU..LL.L..LR..R.RR..BB.B..BF..F.FF..LL.L..LR..R.RR..FF.F..FB..B.BB..UD.D..DU..U.UD.', 'ULFRBD'),
             ('.DD.D..DD..D.UU..LR.L..RR..L.RL..FB.F..BB..F.BF..RL.R..LL..R.LR..BF.B..FF..B.FB..DD.U..UU..U.UU.', 'ULFRBD'),
             ('.DD.D..UD..U.UU..RR.R..RL..L.LL..BF.B..FF..B.FB..RR.R..RL..L.LL..FB.F..BB..F.BF..DD.U..DU..D.UU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LL.L..LL..L.LL..BF.B..FB..F.BF..RR.R..RR..R.RR..BF.B..FB..F.BF..UD.U..DU..D.UD.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..RR.R..RL..L.LL..FF.F..FB..B.BB..RR.R..RL..L.LL..BB.B..BF..F.FF..UD.U..DU..D.UD.', 'ULFRBD'),
             ('.DU.D..DD..D.DU..RR.R..RL..L.LL..FF.F..FB..B.BB..LL.L..LR..R.RR..BB.B..BF..F.FF..UD.U..UU..U.UD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LL.L..LR..R.RR..FB.F..FB..B.BF..RR.R..RL..L.LL..BF.F..FB..B.FB..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RL..R.LR..BF.B..BB..B.BF..LR.L..RL..R.LR..BF.F..FF..F.BF..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LR.L..LR..R.RL..BB.B..BF..F.FF..RL.L..LR..R.LR..FF.F..FB..B.BB..UD.U..DU..D.UD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RL..R.LR..BF.B..BF..F.BF..LR.L..RL..R.LR..BF.F..FB..B.BF..DD.D..DU..U.UU.', 'ULFRBD'),
             ('.DU.D..UD..U.UD..LR.L..LL..L.LR..FB.F..BB..F.BF..LR.R..RR..R.LR..BF.B..FF..B.FB..UD.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..UU..D.UD..RL.R..LR..L.RL..FF.F..BF..B.BB..LR.L..RL..R.LR..BB.F..BF..B.FF..UD.U..DD..U.DU.', 'ULFRBD'),
             ('.DU.D..UU..D.UD..RL.R..LR..L.RL..FF.F..FB..B.BB..LR.L..RL..R.LR..BB.B..BF..F.FF..UD.U..DD..U.DU.', 'ULFRBD'),
             ('.DU.D..DU..U.UD..RL.R..LR..L.RL..FF.F..FB..B.BB..RL.R..LR..L.RL..BB.B..BF..F.FF..UD.U..UD..D.DU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LL.L..LR..R.RR..FB.F..BB..F.FB..LL.L..LR..R.RR..BF.B..FF..B.BF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RL..R.RL..BF.B..FB..F.BF..RL.R..LR..L.LR..BF.B..FB..F.BF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DU.D..DU..U.DU..LL.L..LR..R.RR..BB.B..BB..B.BB..LL.L..LR..R.RR..FF.F..FF..F.FF..DU.U..UD..D.DU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RR..L.RL..BF.B..FB..F.BF..RL.R..LL..R.LR..BF.B..FB..F.BF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DU.D..UD..U.UD..LL.L..LR..R.RR..FB.F..BF..B.FB..RR.R..RL..L.LL..BF.B..FB..F.BF..UD.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LL.L..LL..L.RR..BF.B..FB..F.BF..RR.R..RR..R.LL..BF.B..FB..F.BF..DU.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LL.L..LR..R.RR..BB.B..BB..B.BB..LL.L..LR..R.RR..FF.F..FF..F.FF..DU.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..UD..U.DU..LL.L..LR..R.RR..BF.B..FB..F.BF..RR.R..RL..L.LL..BF.B..FB..F.BF..DU.D..UD..U.DU.', 'ULFRBD'),
             ('.DU.D..UU..D.UD..LL.L..LR..R.RR..FB.F..BF..B.FB..RR.R..RL..L.LL..BF.B..FB..F.BF..UD.U..DD..U.DU.', 'ULFRBD'),
             ('.DU.D..UU..D.UD..LL.L..RL..R.RR..FB.F..BF..B.FB..RR.L..RL..R.LL..BF.B..FB..F.BF..UD.U..DD..U.DU.', 'ULFRBD'),
             ('.DD.D..UU..D.UU..LR.L..RR..L.RL..BF.B..BB..B.BF..RL.R..LL..R.LR..BF.F..FF..F.BF..UU.U..DD..U.DD.', 'ULFRBD'),
             ('.DU.D..UU..D.DU..LL.L..LR..R.RR..BF.B..FB..F.BF..RR.R..RL..L.LL..BF.B..FB..F.BF..DU.U..DD..U.DU.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LL.L..LL..L.LL..FB.F..FB..B.FB..RR.R..RR..R.RR..BF.F..FB..B.BF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RL..R.LR..BF.B..BB..B.BF..LR.L..RL..R.LR..BF.F..FF..F.BF..UU.U..UD..D.DD.', 'ULFRBD'),
             ('.DD.D..UU..D.UU..LR.L..RL..R.LR..BF.B..BF..F.BF..RL.R..LR..L.RL..BF.F..FB..B.BF..UU.U..DD..U.DD.', 'ULFRBD'),
             ('.DD.D..DU..U.UU..LR.L..RL..R.LR..BF.B..BF..F.BF..LR.L..RL..R.LR..BF.F..FB..B.BF..UU.U..UD..D.DD.', 'ULFRBD'),
            ),
            use_edges_pattern=True
        )


class StartingStates444TsaiPhase4SolveCorners64(BFS):
    """
    There should be 64 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-corners-stage64',
            ("U", "U'",
             "L", "L'",
             "F", "F'",
             "R", "R'",
             "B", "B'",
             "D", "D'",

             "Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             ),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step404-corners-stage64.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          U . . U
          . . . .
          . . . .
          U . . U

 L . . L  F . . F  R . . R  B . . B
 . . . .  . . . .  . . . .  . . . .
 . . . .  . . . .  . . . .  . . . .
 L . . L  F . . F  R . . R  B . . B

          D . . D
          . . . .
          . . . .
          D . . D""", 'ascii'),),
        )


class Build444TsaiPhase4SolveCorners64(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase4-corners64',
            ("Fw", "Fw'",
             "Uw", "Uw'",
             "Rw", "Rw'",
             "Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2",
             "R", "R'",
             "L", "L'"),
            '4x4x4',
            'lookup-table-4x4x4-step404-corners64.txt',
            False, # store_as_hex

            # starting cubes
            (('D..D........D..DL..L........L..LB..B........B..BR..R........R..RF..F........F..FU..U........U..U', 'ULFRBD'),
             ('D..D........D..DL..L........R..RB..B........F..FR..R........L..LF..F........B..BU..U........U..U', 'ULFRBD'),
             ('D..D........D..DL..R........L..RF..B........F..BR..L........R..LB..F........B..FU..U........U..U', 'ULFRBD'),
             ('D..D........D..DL..R........R..LF..B........B..FR..L........L..RB..F........F..BU..U........U..U', 'ULFRBD'),
             ('D..D........D..DR..L........L..RB..F........F..BL..R........R..LF..B........B..FU..U........U..U', 'ULFRBD'),
             ('D..D........D..DR..L........R..LB..F........B..FL..R........L..RF..B........F..BU..U........U..U', 'ULFRBD'),
             ('D..D........D..DR..R........L..LF..F........B..BL..L........R..RB..B........F..FU..U........U..U', 'ULFRBD'),
             ('D..D........D..DR..R........R..RF..F........F..FL..L........L..LB..B........B..BU..U........U..U', 'ULFRBD'),
             ('D..D........U..UL..L........L..LF..F........B..BR..R........R..RF..F........B..BU..U........D..D', 'ULFRBD'),
             ('D..D........U..UL..L........R..RF..B........B..FL..L........R..RB..F........F..BD..D........U..U', 'ULFRBD'),
             ('D..D........U..UL..L........R..RF..B........F..BL..L........R..RB..F........B..FU..U........D..D', 'ULFRBD'),
             ('D..D........U..UL..L........R..RF..F........B..BR..R........L..LF..F........B..BD..D........U..U', 'ULFRBD'),
             ('D..D........U..UL..R........L..RB..B........B..BL..R........L..RF..F........F..FD..D........U..U', 'ULFRBD'),
             ('D..D........U..UL..R........L..RB..B........F..FL..R........L..RF..F........B..BU..U........D..D', 'ULFRBD'),
             ('D..D........U..UL..R........L..RB..F........B..FR..L........R..LB..F........B..FD..D........U..U', 'ULFRBD'),
             ('D..D........U..UL..R........R..LB..F........B..FR..L........L..RB..F........B..FU..U........D..D', 'ULFRBD'),
             ('D..D........U..UR..L........L..RF..B........F..BL..R........R..LF..B........F..BU..U........D..D', 'ULFRBD'),
             ('D..D........U..UR..L........R..LF..B........F..BL..R........L..RF..B........F..BD..D........U..U', 'ULFRBD'),
             ('D..D........U..UR..L........R..LF..F........B..BR..L........R..LB..B........F..FU..U........D..D', 'ULFRBD'),
             ('D..D........U..UR..L........R..LF..F........F..FR..L........R..LB..B........B..BD..D........U..U', 'ULFRBD'),
             ('D..D........U..UR..R........L..LB..B........F..FL..L........R..RB..B........F..FD..D........U..U', 'ULFRBD'),
             ('D..D........U..UR..R........L..LB..F........B..FR..R........L..LF..B........F..BU..U........D..D', 'ULFRBD'),
             ('D..D........U..UR..R........L..LB..F........F..BR..R........L..LF..B........B..FD..D........U..U', 'ULFRBD'),
             ('D..D........U..UR..R........R..RB..B........F..FL..L........L..LB..B........F..FU..U........D..D', 'ULFRBD'),
             ('D..U........D..UL..L........L..LB..F........B..FR..R........R..RB..F........B..FU..D........U..D', 'ULFRBD'),
             ('D..U........D..UL..L........R..RB..B........B..BL..L........R..RF..F........F..FD..U........D..U', 'ULFRBD'),
             ('D..U........D..UL..L........R..RB..B........F..FL..L........R..RF..F........B..BU..D........U..D', 'ULFRBD'),
             ('D..U........D..UL..L........R..RB..F........B..FR..R........L..LB..F........B..FD..U........D..U', 'ULFRBD'),
             ('D..U........D..UL..R........L..RF..B........B..FL..R........L..RB..F........F..BD..U........D..U', 'ULFRBD'),
             ('D..U........D..UL..R........L..RF..B........F..BL..R........L..RB..F........B..FU..D........U..D', 'ULFRBD'),
             ('D..U........D..UL..R........L..RF..F........B..BR..L........R..LF..F........B..BD..U........D..U', 'ULFRBD'),
             ('D..U........D..UL..R........R..LF..F........B..BR..L........L..RF..F........B..BU..D........U..D', 'ULFRBD'),
             ('D..U........D..UR..L........L..RB..B........F..FL..R........R..LB..B........F..FU..D........U..D', 'ULFRBD'),
             ('D..U........D..UR..L........R..LB..B........F..FL..R........L..RB..B........F..FD..U........D..U', 'ULFRBD'),
             ('D..U........D..UR..L........R..LB..F........B..FR..L........R..LF..B........F..BU..D........U..D', 'ULFRBD'),
             ('D..U........D..UR..L........R..LB..F........F..BR..L........R..LF..B........B..FD..U........D..U', 'ULFRBD'),
             ('D..U........D..UR..R........L..LF..B........F..BL..L........R..RF..B........F..BD..U........D..U', 'ULFRBD'),
             ('D..U........D..UR..R........L..LF..F........B..BR..R........L..LB..B........F..FU..D........U..D', 'ULFRBD'),
             ('D..U........D..UR..R........L..LF..F........F..FR..R........L..LB..B........B..BD..U........D..U', 'ULFRBD'),
             ('D..U........D..UR..R........R..RF..B........F..BL..L........L..LF..B........F..BU..D........U..D', 'ULFRBD'),
             ('D..U........U..DL..L........L..LF..B........B..FR..R........R..RB..F........F..BU..D........D..U', 'ULFRBD'),
             ('D..U........U..DL..L........R..RF..B........F..BR..R........L..LB..F........B..FU..D........D..U', 'ULFRBD'),
             ('D..U........U..DL..R........L..RB..B........F..FR..L........R..LF..F........B..BU..D........D..U', 'ULFRBD'),
             ('D..U........U..DL..R........R..LB..B........B..BR..L........L..RF..F........F..FU..D........D..U', 'ULFRBD'),
             ('D..U........U..DR..L........L..RF..F........F..FL..R........R..LB..B........B..BU..D........D..U', 'ULFRBD'),
             ('D..U........U..DR..L........R..LF..F........B..BL..R........L..RB..B........F..FU..D........D..U', 'ULFRBD'),
             ('D..U........U..DR..R........L..LB..F........B..FL..L........R..RF..B........F..BU..D........D..U', 'ULFRBD'),
             ('D..U........U..DR..R........R..RB..F........F..BL..L........L..LF..B........B..FU..D........D..U', 'ULFRBD'),
             ('U..D........D..UL..L........L..LB..F........F..BR..R........R..RF..B........B..FD..U........U..D', 'ULFRBD'),
             ('U..D........D..UL..L........R..RB..F........B..FR..R........L..LF..B........F..BD..U........U..D', 'ULFRBD'),
             ('U..D........D..UL..R........L..RF..F........B..BR..L........R..LB..B........F..FD..U........U..D', 'ULFRBD'),
             ('U..D........D..UL..R........R..LF..F........F..FR..L........L..RB..B........B..BD..U........U..D', 'ULFRBD'),
             ('U..D........D..UR..L........L..RB..B........B..BL..R........R..LF..F........F..FD..U........U..D', 'ULFRBD'),
             ('U..D........D..UR..L........R..LB..B........F..FL..R........L..RF..F........B..BD..U........U..D', 'ULFRBD'),
             ('U..D........D..UR..R........L..LF..B........F..BL..L........R..RB..F........B..FD..U........U..D', 'ULFRBD'),
             ('U..D........D..UR..R........R..RF..B........B..FL..L........L..LB..F........F..BD..U........U..D', 'ULFRBD'),
             ('U..D........U..DL..L........L..LF..B........F..BR..R........R..RF..B........F..BD..U........D..U', 'ULFRBD'),
             ('U..D........U..DL..L........R..RF..B........F..BR..R........L..LF..B........F..BU..D........U..D', 'ULFRBD'),
             ('U..D........U..DL..L........R..RF..F........B..BL..L........R..RB..B........F..FD..U........D..U', 'ULFRBD'),
             ('U..D........U..DL..L........R..RF..F........F..FL..L........R..RB..B........B..BU..D........U..D', 'ULFRBD'),
             ('U..D........U..DL..R........L..RB..B........F..FR..L........R..LB..B........F..FU..D........U..D', 'ULFRBD'),
             ('U..D........U..DL..R........L..RB..F........B..FL..R........L..RF..B........F..BD..U........D..U', 'ULFRBD'),
             ('U..D........U..DL..R........L..RB..F........F..BL..R........L..RF..B........B..FU..D........U..D', 'ULFRBD'),
             ('U..D........U..DL..R........R..LB..B........F..FR..L........L..RB..B........F..FD..U........D..U', 'ULFRBD'),
             ('U..D........U..DR..L........L..RF..F........B..BL..R........R..LF..F........B..BD..U........D..U', 'ULFRBD'),
             ('U..D........U..DR..L........R..LF..B........B..FR..L........R..LB..F........F..BU..D........U..D', 'ULFRBD'),
             ('U..D........U..DR..L........R..LF..B........F..BR..L........R..LB..F........B..FD..U........D..U', 'ULFRBD'),
             ('U..D........U..DR..L........R..LF..F........B..BL..R........L..RF..F........B..BU..D........U..D', 'ULFRBD'),
             ('U..D........U..DR..R........L..LB..B........B..BR..R........L..LF..F........F..FU..D........U..D', 'ULFRBD'),
             ('U..D........U..DR..R........L..LB..B........F..FR..R........L..LF..F........B..BD..U........D..U', 'ULFRBD'),
             ('U..D........U..DR..R........L..LB..F........B..FL..L........R..RB..F........B..FU..D........U..D', 'ULFRBD'),
             ('U..D........U..DR..R........R..RB..F........B..FL..L........L..LB..F........B..FD..U........D..U', 'ULFRBD'),
             ('U..U........D..DL..L........L..LB..B........F..FR..R........R..RB..B........F..FD..D........U..U', 'ULFRBD'),
             ('U..U........D..DL..L........R..RB..B........F..FR..R........L..LB..B........F..FU..U........D..D', 'ULFRBD'),
             ('U..U........D..DL..L........R..RB..F........B..FL..L........R..RF..B........F..BD..D........U..U', 'ULFRBD'),
             ('U..U........D..DL..L........R..RB..F........F..BL..L........R..RF..B........B..FU..U........D..D', 'ULFRBD'),
             ('U..U........D..DL..R........L..RF..B........F..BR..L........R..LF..B........F..BU..U........D..D', 'ULFRBD'),
             ('U..U........D..DL..R........L..RF..F........B..BL..R........L..RB..B........F..FD..D........U..U', 'ULFRBD'),
             ('U..U........D..DL..R........L..RF..F........F..FL..R........L..RB..B........B..BU..U........D..D', 'ULFRBD'),
             ('U..U........D..DL..R........R..LF..B........F..BR..L........L..RF..B........F..BD..D........U..U', 'ULFRBD'),
             ('U..U........D..DR..L........L..RB..F........B..FL..R........R..LB..F........B..FD..D........U..U', 'ULFRBD'),
             ('U..U........D..DR..L........R..LB..B........B..BR..L........R..LF..F........F..FU..U........D..D', 'ULFRBD'),
             ('U..U........D..DR..L........R..LB..B........F..FR..L........R..LF..F........B..BD..D........U..U', 'ULFRBD'),
             ('U..U........D..DR..L........R..LB..F........B..FL..R........L..RB..F........B..FU..U........D..D', 'ULFRBD'),
             ('U..U........D..DR..R........L..LF..B........B..FR..R........L..LB..F........F..BU..U........D..D', 'ULFRBD'),
             ('U..U........D..DR..R........L..LF..B........F..BR..R........L..LB..F........B..FD..D........U..U', 'ULFRBD'),
             ('U..U........D..DR..R........L..LF..F........B..BL..L........R..RF..F........B..BU..U........D..D', 'ULFRBD'),
             ('U..U........D..DR..R........R..RF..F........B..BL..L........L..LF..F........B..BD..D........U..U', 'ULFRBD'),
             ('U..U........U..UL..L........L..LF..F........F..FR..R........R..RB..B........B..BD..D........D..D', 'ULFRBD'),
             ('U..U........U..UL..L........R..RF..F........B..BR..R........L..LB..B........F..FD..D........D..D', 'ULFRBD'),
             ('U..U........U..UL..R........L..RB..F........B..FR..L........R..LF..B........F..BD..D........D..D', 'ULFRBD'),
             ('U..U........U..UL..R........R..LB..F........F..BR..L........L..RF..B........B..FD..D........D..D', 'ULFRBD'),
             ('U..U........U..UR..L........L..RF..B........B..FL..R........R..LB..F........F..BD..D........D..D', 'ULFRBD'),
             ('U..U........U..UR..L........R..LF..B........F..BL..R........L..RB..F........B..FD..D........D..D', 'ULFRBD'),
             ('U..U........U..UR..R........L..LB..B........F..FL..L........R..RF..F........B..BD..D........D..D', 'ULFRBD'),
             ('U..U........U..UR..R........R..RB..B........B..BL..L........L..LF..F........F..FD..D........D..D', 'ULFRBD')
            ),
        )


class Build444TsaiPhase4(BFS):

    def __init__(self):
        from builder444ss import starting_states_step400
        BFS.__init__(self,
            '4x4x4-tsai-phase4',
            ("Fw", "Fw'",
             "Uw", "Uw'",
             "Rw", "Rw'",
             "Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2",
             "R", "R'",
             "L", "L'"),
            '4x4x4',
            'lookup-table-4x4x4-step400.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_step400
        )

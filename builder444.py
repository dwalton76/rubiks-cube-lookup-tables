#!/usr/bin/e nv python3

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
            ("Lw", "Lw'", "Lw2", # can skip these for 4x4x4 cubes
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
            ("Lw", "Lw'", "Lw2", # can skip these for 4x4x4 cubes
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
            ("Lw", "Lw'", "Lw2", # can skip these for 4x4x4 cubes
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
            ("Lw", "Lw'", "Lw2", # can skip these for 4x4x4 cubes
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


class StartingStates444HighLowEdges(BFS):
    """
    Combine tsai phases 1 and 2
    - Need all 3 opposite side pairs to be elligible for 12 states
    - Need those to happen at any of 24 rotations
    - Need high/low edges in this too
    """

    def __init__(self):
        BFS.__init__(self,
            '444-highlow-edges',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step20-highlow-edges.txt',
            False, # store_as_hex

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


class StartingStates444HighLowEdgesCenters(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '444-highlow-edges-centers',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
            "L", "L'",
            "R", "R'"),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step21-highlow-edges-centers.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          . . . .
          . . . .
          . . . .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . . . .  . R R .  . . . .
 . L L .  . . . .  . R R .  . . . .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . . . .
          . . . .
          . . . .""", 'ascii'),)
        )


class Build444HighLowEdgesEdges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-highlow-edges-edges',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '4x4x4',
            'lookup-table-4x4x4-step21-highlow-edges-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D . . U  U . . D  D . . U  U . . D
 U . . D  D . . U  U . . D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .""", 'ascii'),)
        )


class Build444HighLowEdgesCenters(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-highlow-edges-centers',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),
            '4x4x4',
            'lookup-table-4x4x4-step22-highlow-edges-centers.txt',
            False, # store_as_hex

            # starting cubes
            (('.....................LL..LL..........................RR..RR.....................................', 'ULFRBD'),
             ('.....................LL..RR..........................LL..RR.....................................', 'ULFRBD'),
             ('.....................LL..RR..........................RR..LL.....................................', 'ULFRBD'),
             ('.....................LR..LR..........................LR..LR.....................................', 'ULFRBD'),
             ('.....................LR..LR..........................RL..RL.....................................', 'ULFRBD'),
             ('.....................LR..RL..........................RL..LR.....................................', 'ULFRBD'),
             ('.....................RL..LR..........................LR..RL.....................................', 'ULFRBD'),
             ('.....................RL..RL..........................LR..LR.....................................', 'ULFRBD'),
             ('.....................RL..RL..........................RL..RL.....................................', 'ULFRBD'),
             ('.....................RR..LL..........................LL..RR.....................................', 'ULFRBD'),
             ('.....................RR..LL..........................RR..LL.....................................', 'ULFRBD'),
             ('.....................RR..RR..........................LL..LL.....................................', 'ULFRBD'))
        )


class Build444HighLowEdges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-highlow-edges',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),
            '4x4x4',
            'lookup-table-4x4x4-step20-highlow-edges.txt',
            False, # store_as_hex

            # starting cubes
            (('.UD.D..UU..D.DU..DU.DLLUULLD.UD..DU.U..DD..U.UD..DU.DRRUURRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DLLUURRD.UD..DU.U..DD..U.UD..DU.DLLUURRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DLLUURRD.UD..DU.U..DD..U.UD..DU.DRRUULLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DLRUULRD.UD..DU.U..DD..U.UD..DU.DLRUULRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DLRUULRD.UD..DU.U..DD..U.UD..DU.DRLUURLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DLRUURLD.UD..DU.U..DD..U.UD..DU.DRLUULRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DRLUULRD.UD..DU.U..DD..U.UD..DU.DLRUURLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DRLUURLD.UD..DU.U..DD..U.UD..DU.DLRUULRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DRLUURLD.UD..DU.U..DD..U.UD..DU.DRLUURLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DRRUULLD.UD..DU.U..DD..U.UD..DU.DLLUURRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DRRUULLD.UD..DU.U..DD..U.UD..DU.DRRUULLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'),
             ('.UD.D..UU..D.DU..DU.DRRUURRD.UD..DU.U..DD..U.UD..DU.DLLUULLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD')),
            use_centers_then_edges=True
        )


class Build444Reduce333Edges(BFS):
    """
    This is the TPR edges table.
    This table will have ~239 million entries.
    """

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step31-reduce333-edges.txt',
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

            use_edges_pattern=True,
        )


class StartingStates444Reduce333Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333-centers',
            moves_444,
            '4x4x4',
            'lookup-table-4x4x4-step32-reduce333-centers.txt',
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
            legal_moves=("", "x2", "y2", "z2"),
        )


class Build444Reduce333Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333-centers',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step32-reduce333-centers.txt',
            False, # store_as_hex

            # starting cubes
            (('.....UU..UU..........LL..LL..........FF..FF..........RR..RR..........BB..BB..........DD..DD.....', 'ULFRBD'),
             ('.....UU..UU..........RR..RR..........BB..BB..........LL..LL..........FF..FF..........DD..DD.....', 'ULFRBD'),
             ('.....DD..DD..........LL..LL..........BB..BB..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....DD..DD..........RR..RR..........FF..FF..........LL..LL..........BB..BB..........UU..UU.....', 'ULFRBD'))
        )


class StartingStates444Reduce333(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333',
            moves_444,
            '4x4x4',
            'lookup-table-4x4x4-step30-reduce333.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U U .
          U U U U
          U U U U
          . U U .

 . L L .  . F F .  . R R .  . B B .
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 . L L .  . F F .  . R R .  . B B .

          . D D .
          D D D D
          D D D D
          . D D .  """, 'ascii'),),
            use_edges_pattern=True,
            legal_moves=("", "x2", "y2", "z2"),
        )


class Build444Reduce333(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step30-reduce333.txt',
            False, # store_as_hex

            # starting cubes
            (('.UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU.', 'ULFRBD')),
            use_edges_pattern=True
        )



class Build444PairXPlaneEdges(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '444-pair-x-plane-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step301-pair-x-plane-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . - - .
          - . . -
          - . . -
          . - - .

 . - - .  . - - .  . - - .  . - - .
 L . . L  F . . F  R . . R  B . . B
 L . . L  F . . F  R . . R  B . . B
 . - - .  . - - .  . - - .  . - - .

          . - - .
          - . . -
          - . . -
          . - - .""", 'ascii'),),
            use_edges_pattern=True,
        )


# brainstorm 1
'''
phase 1
- stage UD centers
- stage FB centers
- stage LR centers
10 moves

phase 2
- LR centers to one of 12 states
    70
- EO all edges to final orienation
    24!/(12!*12!) = 2,704,156 states
- Orient the corners to states that can be solved without L L' R R'
    Each of the eight corners can be in 3 positions so
    3^8 = 6,561 states

- total states
2704156*6561*70 = 1241937726120

70*2,704,156 = 189,290,920 pt

(70*2704156)/1241937726120 = 0.000 152
IDA is doable
8 moves??


phase3
- reduce to 333
14 moves


phase4 - solve reduced 333
    Will be solveable without L L' R R' how much difference will this make?
        12! or 479,001,600 edge states
        ? corner states..I know it is as least 35 million (built it 9-deep)
        so this IDA would be brutal

    Would need to use the optimal cube explorer solver
    12 moves????

Would be 44 moves total but I am guessing at how many steps solving 333 would
be
'''



# brainstorm 2
'''
phase 1
- stage UD centers
- stage FB centers
- stage LR centers
10 moves

phase 2
- LR centers to one of 12 states
    70
- EO all edges to final orienation
    24!/(12!*12!) = 2,704,156 states
- Orient the corners to states that can be solved without L L' R R'
    Each of the eight corners can be in 3 positions so
    3^8 = 6,561 states

- total states
2704156*6561*70 = 1241937726120

70*2,704,156 = 189,290,920 pt

(70*2704156)/1241937726120 = 0.000 152
IDA is doable
8 moves??

phase3
- LR centers to vertical bars
    12 states

- FB centers to vertical bars
    70 states

- pair 4-edges in x-plane
    12*11*10*9 * 12!/(8!*4!) = 5,880,600

- Orient the corners to states that can be solved without L L' R R' F F' B B'
    Each of the eight corners can be in 2 positions??? not sure on this
    2^8 = 256 states

- edges will also need to be placed so they can be solved without L L' R R' F F' B B'
    There are 967,679 target states but there has to be a better way to represent this?

- total states
    12 * 70 * 70,567,200 * 256 = 15,174,770,688,000

70567200/15174770688000 = 0.000 004
12 moves?

phase4...reduce to 333
- LR centers solve
    4 states
- FB centers solve
    4 states
- UD centers solve
    70 states
- pair 8-edges in y-plane and z-plane
12 moves???


phase 5 - solved reduced 333 without L L' R R' F F' B B'
    - 40,320 corner states
    - 967,679 edge states

    40320 * 967679 = 39016817280

    967679/39016817280  = 0.000 024
  
11 moves???
  
That would be 53 moves....not worth it
'''

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

# brainstorm 1
'''
phase1
- stage UD centers

phase2
- LR centers to vertical bars
- FB centers to vertical bars
    63,063,000 LR FB states
- pair 4-edges and place in x-plane
- EO remaining 8-edges in y-plane and y-plane

phase3
- pair 8-edges
- solve centers
'''

# brainstorm 2
'''
phase1
- stage UD centers
- stage FB centers
- stage LR centers to one of 12 states
- at least 4-edges must be pairable without L L' R R'

phase2
- LR centers to horizontal bars
    12 states

- pair 4-edges in z-plane
    ((12*11*10*9)^2)/2 = 70,567,200 states

phase 3
- FB centers to vertical bars
    70 states

- EO remaining 8-edges in y-plane and z-plane
    16!/(8!*8!) = 12,870

- 70 * 12870 = 900,900 states
- L and R' to move LR centers to vertical bars

- orient corners to reduce 333 solve? Corners would
  need to be placed into a position they can solve from
  without L2 F2 R2 B2...how many is that?

phase4
- pair 8-edges
    8! / 2 = 20160
    I am not 100% sure this is correct...would be easy to build to test though
    Even if it is (8!^2)/2 that is still buildable (800 million)

- solve centers
    4 * 4 * 70 = 1120

I think this would only be worth it if something can be done with the
corners so that you reduce the 333 solution to a single phase.
'''

#!/usr/bin/e nv python3

from buildercore import BFS
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)


class Build444Ultimate(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-ultimate',
            (),
            '4x4x4',
            'lookup-table-4x4x4-step00-ultimate.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          U U U U
          U U U U
          U U U U
          U U U U

 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B

          D D D D
          D D D D
          D D D D
          D D D D""", 'ascii'),),
        )


class Build444CentersSolveUnstaged(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-ultimate',
            (),
            '4x4x4',
            'lookup-table-4x4x4-step200-centers.txt',
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
          . . . .  """, 'ascii'),),
        )




# ===============================
# --fast, --normal, --slow tables
# ===============================
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
             "Rw", "Rw'",
            ),


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


# ======================
# --normal/--slow tables
# ======================
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


# =============
# --fast tables
# =============
class Build444UDCentersStageFast(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-UD-centers-stage-fast',
            (),
            '4x4x4',
            'lookup-table-4x4x4-step110-UD-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (('.....UU..UU..........xx..xx..........xx..xx..........xx..xx..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....xx..xx..........UU..UU..........xx..xx..........UU..UU..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........xx..xx..........UU..UU..........xx..xx..........UU..UU..........xx..xx.....', 'ULFRBD')),
        )


class Build444LRFBCentersStage(BFS):

    """
    UD must already be staged
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LRFB-centers-stage',
            ("Lw", "Lw'", "Rw", "Rw'",
             "Fw", "Fw'", "Bw", "Bw'"),
            '4x4x4',
            'lookup-table-4x4x4-step120-LRFB-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . . . .
          . . . .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . L L .  . x x .
 . L L .  . x x .  . L L .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . . . .
          . . . .
          . . . .""", 'ascii'),

             ("""
          . . . .
          . . . .
          . . . .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . L L .  . x x .  . L L .
 . x x .  . L L .  . x x .  . L L .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . . . .
          . . . .
          . . . .""", 'ascii'))
        )


class Build444LRFBCentersSolve(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LRFB-centers-solve',
            ("Lw", "Lw'", "Rw", "Rw'",
             "Fw", "Fw'", "Bw", "Bw'",
             "Uw", "Uw'", "Dw", "Dw'"),
            '4x4x4',
            'lookup-table-4x4x4-step130-LRFB-centers-solve.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . . . .
          . . . .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . B B .
 . L L .  . F F .  . R R .  . B B .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . . . .
          . . . .
          . . . .""", 'ascii'),)
        )


class Build444FirstFourEdgesEdgesOnly(BFS):
    """
    Solve the first 4-edges in x-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '444-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step141.txt',
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


class StartingStates444FirstFourEdgesCentersOnly(BFS):
    """
    LR FB to vertical bars
    """

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333',
            moves_444,
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step142.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . . . .
          . . . .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . B B .
 . L L .  . F F .  . R R .  . B B .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . . . .
          . . . .
          . . . .""", 'ascii'),),
            legal_moves=(
                "L2", "F2", "R2", "B2",
                "Lw2", "Fw2", "Rw2", "Bw2",
            )
        )


class Build444FirstFourEdgesCentersOnly(BFS):
    """
    LR FB to vertical bars
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
            'lookup-table-4x4x4-step142.txt',
            False, # store_as_hex

            # starting cubes
            (('.....................LL..LL..........BB..BB..........RR..RR..........FF..FF.....................', 'ULFRBD'),
             ('.....................LL..LL..........BF..BF..........RR..RR..........BF..BF.....................', 'ULFRBD'),
             ('.....................LL..LL..........BF..BF..........RR..RR..........FB..FB.....................', 'ULFRBD'),
             ('.....................LL..LL..........FB..FB..........RR..RR..........BF..BF.....................', 'ULFRBD'),
             ('.....................LL..LL..........FB..FB..........RR..RR..........FB..FB.....................', 'ULFRBD'),
             ('.....................LL..LL..........FF..FF..........RR..RR..........BB..BB.....................', 'ULFRBD'),
             ('.....................LR..LR..........BB..BB..........LR..LR..........FF..FF.....................', 'ULFRBD'),
             ('.....................LR..LR..........BB..BB..........RL..RL..........FF..FF.....................', 'ULFRBD'),
             ('.....................LR..LR..........BF..BF..........LR..LR..........BF..BF.....................', 'ULFRBD'),
             ('.....................LR..LR..........BF..BF..........LR..LR..........FB..FB.....................', 'ULFRBD'),
             ('.....................LR..LR..........BF..BF..........RL..RL..........BF..BF.....................', 'ULFRBD'),
             ('.....................LR..LR..........BF..BF..........RL..RL..........FB..FB.....................', 'ULFRBD'),
             ('.....................LR..LR..........FB..FB..........LR..LR..........BF..BF.....................', 'ULFRBD'),
             ('.....................LR..LR..........FB..FB..........LR..LR..........FB..FB.....................', 'ULFRBD'),
             ('.....................LR..LR..........FB..FB..........RL..RL..........BF..BF.....................', 'ULFRBD'),
             ('.....................LR..LR..........FB..FB..........RL..RL..........FB..FB.....................', 'ULFRBD'),
             ('.....................LR..LR..........FF..FF..........LR..LR..........BB..BB.....................', 'ULFRBD'),
             ('.....................LR..LR..........FF..FF..........RL..RL..........BB..BB.....................', 'ULFRBD'),
             ('.....................RL..RL..........BB..BB..........LR..LR..........FF..FF.....................', 'ULFRBD'),
             ('.....................RL..RL..........BB..BB..........RL..RL..........FF..FF.....................', 'ULFRBD'),
             ('.....................RL..RL..........BF..BF..........LR..LR..........BF..BF.....................', 'ULFRBD'),
             ('.....................RL..RL..........BF..BF..........LR..LR..........FB..FB.....................', 'ULFRBD'),
             ('.....................RL..RL..........BF..BF..........RL..RL..........BF..BF.....................', 'ULFRBD'),
             ('.....................RL..RL..........BF..BF..........RL..RL..........FB..FB.....................', 'ULFRBD'),
             ('.....................RL..RL..........FB..FB..........LR..LR..........BF..BF.....................', 'ULFRBD'),
             ('.....................RL..RL..........FB..FB..........LR..LR..........FB..FB.....................', 'ULFRBD'),
             ('.....................RL..RL..........FB..FB..........RL..RL..........BF..BF.....................', 'ULFRBD'),
             ('.....................RL..RL..........FB..FB..........RL..RL..........FB..FB.....................', 'ULFRBD'),
             ('.....................RL..RL..........FF..FF..........LR..LR..........BB..BB.....................', 'ULFRBD'),
             ('.....................RL..RL..........FF..FF..........RL..RL..........BB..BB.....................', 'ULFRBD'),
             ('.....................RR..RR..........BB..BB..........LL..LL..........FF..FF.....................', 'ULFRBD'),
             ('.....................RR..RR..........BF..BF..........LL..LL..........BF..BF.....................', 'ULFRBD'),
             ('.....................RR..RR..........BF..BF..........LL..LL..........FB..FB.....................', 'ULFRBD'),
             ('.....................RR..RR..........FB..FB..........LL..LL..........BF..BF.....................', 'ULFRBD'),
             ('.....................RR..RR..........FB..FB..........LL..LL..........FB..FB.....................', 'ULFRBD'),
             ('.....................RR..RR..........FF..FF..........LL..LL..........BB..BB.....................', 'ULFRBD'))
        )


class StartingStates444FirstFourEdges(BFS):
    """
    Solve the first 4-edges in x-plane
    LR FB to vertical bars
    """

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333',
            moves_444,
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step140.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . - - .
          - . . -
          - . . -
          . - - .

 . - - .  . - - .  . - - .  . - - .
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 . - - .  . - - .  . - - .  . - - .

          . - - .
          - . . -
          - . . -
          . - - .""", 'ascii'),),
            use_edges_pattern=True,
            legal_moves=(
                "L2", "F2", "R2", "B2",
                "Lw2", "Fw2", "Rw2", "Bw2",
            )
        )


class Build444FirstFourEdges(BFS):
    """
    Solve the first 4-edges in x-plane
    LR FB to vertical bars
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
            'lookup-table-4x4x4-step140.txt',
            False, # store_as_hex

            # starting cubes
            (('.--.-..--..-.--..--.LLLLLLLL.--..--.BBBBBBBB.--..--.RRRRRRRR.--..--.FFFFFFFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLLLLLLL.--..--.BBFFBBFF.--..--.RRRRRRRR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLLLLLLL.--..--.BFFFBFFF.--..--.RRRRRRRR.--..--.BBBFBBBF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLLLLLLL.--..--.FFBBFFBB.--..--.RRRRRRRR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLLRLLLR.--..--.BBFFBBFF.--..--.LRRRLRRR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLLRLLLR.--..--.FFBBFFBB.--..--.LRRRLRRR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRLLLRL.--..--.BBBBBBBB.--..--.RRLRRRLR.--..--.FFFFFFFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRLLLRL.--..--.BBFFBBFF.--..--.RLRRRLRR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRLLLRL.--..--.FFBBFFBB.--..--.RLRRRLRR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.BBBBBBBB.--..--.LLRRLLRR.--..--.FFFFFFFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.BBFFBBFF.--..--.LLRRLLRR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.BBFFBBFF.--..--.RRLLRRLL.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.BBFFBBFF.--..--.RRLLRRLL.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.BFFFBFFF.--..--.RRLLRRLL.--..--.BBBFBBBF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.FFBBFFBB.--..--.LLRRLLRR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.FFBBFFBB.--..--.RRLLRRLL.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.FFBBFFBB.--..--.RRLLRRLL.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LLRRLLRR.--..--.FFFFFFFF.--..--.LLRRLLRR.--..--.BBBBBBBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LRLLLRLL.--..--.BBBBBBBB.--..--.RLRRRLRR.--..--.FFFFFFFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LRLLLRLL.--..--.BBFFBBFF.--..--.RRLRRRLR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LRLLLRLL.--..--.FFBBFFBB.--..--.RRLRRRLR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LRRRLRRR.--..--.BBFFBBFF.--..--.LLLRLLLR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.LRRRLRRR.--..--.FFBBFFBB.--..--.LLLRLLLR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.BBBBBBBB.--..--.RRLLRRLL.--..--.FFFFFFFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.BBFFBBFF.--..--.LLRRLLRR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.BBFFBBFF.--..--.LLRRLLRR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.BBFFBBFF.--..--.RRLLRRLL.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.BFFFBFFF.--..--.LLRRLLRR.--..--.BBBFBBBF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.FFBBFFBB.--..--.LLRRLLRR.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.FFBBFFBB.--..--.LLRRLLRR.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.FFBBFFBB.--..--.RRLLRRLL.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRLLRRLL.--..--.FFFFFFFF.--..--.RRLLRRLL.--..--.BBBBBBBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRRRRRRR.--..--.BBBBBBBB.--..--.LLLLLLLL.--..--.FFFFFFFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRRRRRRR.--..--.BBFFBBFF.--..--.LLLLLLLL.--..--.BBFFBBFF.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRRRRRRR.--..--.FFBBFFBB.--..--.LLLLLLLL.--..--.FFBBFFBB.--..--.-..--..-.--.', 'ULFRBD'),
             ('.--.-..--..-.--..--.RRRRRRRR.--..--.FFFFFFFF.--..--.LLLLLLLL.--..--.BBBBBBBB.--..--.-..--..-.--.', 'ULFRBD')),
            use_edges_pattern=True,
        )


class Build444LastEightEdgesEdgesOnly(BFS):
    """
    Solve the last 8-edges in z-plane and y-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333-edges',
            ("Uw", "Uw'", "Uw2",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-step161.txt',
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

class Build444LastEightEdgesCentersOnly(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333-centers',
            ("Uw", "Uw'", "Uw2",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-step162.txt',
            False, # store_as_hex

            # starting cubes
            (('.....UU..UU..........LL..LL..........FF..FF..........RR..RR..........BB..BB..........DD..DD.....', 'ULFRBD'),
             ('.....UU..UU..........RR..RR..........BB..BB..........LL..LL..........FF..FF..........DD..DD.....', 'ULFRBD'),
             ('.....DD..DD..........LL..LL..........BB..BB..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....DD..DD..........RR..RR..........FF..FF..........LL..LL..........BB..BB..........UU..UU.....', 'ULFRBD'))
        )


class Build444LastEightEdges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-reduce333',
            ("Uw", "Uw'", "Uw2",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-step160.txt',
            False, # store_as_hex

            # starting cubes
            (('.UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU.', 'ULFRBD')),
            use_edges_pattern=True
        )


class Build444Phase5(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-phase5',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
             "U", "U'",
             "D", "D'",
             "U2", "D2",
             # "U2", "D2", "Uw2", "Dw2",
            ),
            '4x4x4',
            'lookup-table-4x4x4-step950-phase5.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          U U U U
          U U U U
          U U U U
          U U U U

 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B

          D D D D
          D D D D
          D D D D
          D D D D""", 'ascii'),),
        )


class Build444Phase5Edges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-phase5-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
             "U", "U'",
             "D", "D'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-step951-phase5-edges.txt',
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
        )


class Build444Phase5CentersCorners(BFS):

    def __init__(self):
        BFS.__init__(self,
            '444-phase5-centers-corners',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
             "U", "U'",
             "D", "D'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-step952-phase5-centers-corners.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          U . . U
          . U U .
          . U U .
          U . . U

 L . . L  F . . F  R . . R  B . . B
 . L L .  . F F .  . R R .  . B B .
 . L L .  . F F .  . R R .  . B B .
 L . . L  F . . F  R . . R  B . . B

          D . . D
          . D D .
          . D D .
          D . . D""", 'ascii'),),
        )


# dwalton
"""
phase 1 - stage the LR centers
    6 moves

phase 2 - remove L L' R R'...EO the edges, stage UD centers, LR centers to 1 of 12 states
    ~9 moves?
    
phase 3 - remove F F' B B'...x-plane edges to x-plane, FB centers to 1 of 12 states, stage UD corners
    2187 corner states
    245025 edge states
    70 center states
    245025 * 2187 * 70 = 37,510,877,250

    edges + centers prune table
    70 * 245025 = 17151750
    17151750/37510877250 = 0.000 457


phase 4 - remove U U' D D'...y-plane edges to y-plane, UD centers to 1 of 12 states, corners to one of 96 states
    on 333 this averages 8.70 moves

phase 5 - solve entire cube
    884,736 edges states
    165,888 centers + corners states
    884736/(884736 * 165888) = 0.000 006

    lookup-table-4x4x4-step950-phase5.txt
    =====================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 12 entries (0 percent, 12.00x previous step)
    2 steps has 114 entries (0 percent, 9.50x previous step)
    3 steps has 954 entries (0 percent, 8.37x previous step)
    4 steps has 7,316 entries (0 percent, 7.67x previous step)
    5 steps has 51,552 entries (2 percent, 7.05x previous step)
    6 steps has 337,330 entries (13 percent, 6.54x previous step)
    7 steps has 2,061,576 entries (83 percent, 6.11x previous step)
    extrapolate from here
    8 steps has 11,771,598 entries (5.71x previous step)
    9 steps has 62,507,185 entries (5.31x previous step)
    10 steps has 306,910,278 entries (4.91x previous step)
    11 steps has 1,384,165,353 entries (4.51x previous step)
    12 steps has 5,688,919,600 entries (4.11x previous step)
    13 steps has 21,105,891,715 entries (3.71x previous step)
    14 steps has 69,860,501,576 entries (3.31x previous step)
    15 steps has 48,343,959,408 entries (0.69x previous step)

    Average: 14.068561025110347
    Total  : 146,767,085,568

So if phase3+4 had the exact same move count as 333 (which they won't) we would
be looking at 45.5 moves.
    - Could phase3 and phase4 be combined? This is currently 16.5 moves at least.
      - corners can be any of 24*21*18*15*12*9*6 = 88,179,840 states
      - centers can be 12 * 70 * 70 = 58,800 states
      - edges can be (12!/(4!*4!*4!))^2 = 1,200,622,500
      - so no...they could not be combined
    - Could we do more in phase4 to reduce the phase5 move count?
      In phase5 if you restrict U2 D2 Uw2 Dw2 that drops the average down to 7.85 moves.
      In phase5 if you restrict U2 D2 that drops the average down to 10.6 moves.

333 notes...
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

"""


class Build444NewPhase1(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase1',
            (),
            '4x4x4',
            'lookup-table-4x4x4-phase1.txt',
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
          . . . .""", 'ascii'),)
        )


class StartingStates444NewPhase2(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase2',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
        
            ),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-phase2.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          . U D .
          D U U U
          U U U D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U x x D  D R R U  U x x D
 U L L D  D x x U  U R R D  D x x U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D U U U
          U U U D
          . D U .""", 'ascii'),)
        )


class Build444NewPhase2(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase2',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-phase2.txt',
            False, # store_as_hex
            # starting cubes
            (('.UD.DUUUUUUD.DU..DU.DLLUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUURRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUULRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUURLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUULLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
            )
        )


class Build444NewPhase2Edges(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '444-phase2-edges',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-phase2-edges.txt',
            False, # store_as_hex

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


class StartingStates444NewPhase2Centers(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase2-centers',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-phase2-centers.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . R R .  . x x .
 . L L .  . x x .  . R R .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .  """, 'ascii'),)
        )


class Build444NewPhase2Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '444-phase2-centers',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-phase2-centers.txt',
            False, # store_as_hex

            (('.....UU..UU..........LL..LL..........xx..xx..........RR..RR..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..RR..........xx..xx..........LL..RR..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..RR..........xx..xx..........RR..LL..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..LR..........xx..xx..........LR..LR..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..LR..........xx..xx..........RL..RL..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..RL..........xx..xx..........RL..LR..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..LR..........xx..xx..........LR..RL..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..RL..........xx..xx..........LR..LR..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..RL..........xx..xx..........RL..RL..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..LL..........xx..xx..........LL..RR..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..LL..........xx..xx..........RR..LL..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..RR..........xx..xx..........LL..LL..........xx..xx..........UU..UU.....', 'ULFRBD'),
            ),
        )

# dwalton
class StartingStates444NewPhase3(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase3',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-phase3.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          U x x U
          x x x x
          x x x x
          U x x U

 x x x x  x x x x  x x x x  x x x x
 L x x L  x F F x  L x x L  x B B x
 L x x L  x F F x  L x x L  x B B x
 x x x x  x x x x  x x x x  x x x x

          U x x U
          x x x x
          x x x x
          U x x U""", 'ascii'),)
        )


class Build444NewPhase3(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase3',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-phase3.txt',
            False, # store_as_hex
            # starting cubes
            (('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxBBxxBBxxxxxxxxxLxxLLxxLxxxxxxxxxFFxxFFxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxBBxxFFxxxxxxxxxLxxLLxxLxxxxxxxxxBBxxFFxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxBBxxFFxxxxxxxxxLxxLLxxLxxxxxxxxxFFxxBBxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxBFxxBFxxxxxxxxxLxxLLxxLxxxxxxxxxBFxxBFxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxBFxxBFxxxxxxxxxLxxLLxxLxxxxxxxxxFBxxFBxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxBFxxFBxxxxxxxxxLxxLLxxLxxxxxxxxxFBxxBFxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxFBxxBFxxxxxxxxxLxxLLxxLxxxxxxxxxBFxxFBxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxFBxxFBxxxxxxxxxLxxLLxxLxxxxxxxxxBFxxBFxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxFBxxFBxxxxxxxxxLxxLLxxLxxxxxxxxxFBxxFBxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxFFxxBBxxxxxxxxxLxxLLxxLxxxxxxxxxBBxxFFxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxFFxxBBxxxxxxxxxLxxLLxxLxxxxxxxxxFFxxBBxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
             ('UxxUxxxxxxxxUxxUxxxxLxxLLxxLxxxxxxxxxFFxxFFxxxxxxxxxLxxLLxxLxxxxxxxxxBBxxBBxxxxxUxxUxxxxxxxxUxxU', 'ULFRBD'),
            ),
        )


class Build444NewPhase3EdgesCorners(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase3-edges-corners',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-phase3-edges-corners.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          U x x U
          x . . x
          x . . x
          U x x U

 x x x x  x x x x  x x x x  x x x x
 L . . L  x . . x  L . . L  x . . x
 L . . L  x . . x  L . . L  x . . x
 x x x x  x x x x  x x x x  x x x x

          U x x U
          x . . x
          x . . x
          U x x U""", 'ascii'),)
        )


class Build444NewPhase3Edges(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase3-edges',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-phase3-edges.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          . x x .
          x . . x
          x . . x
          . x x .

 . x x .  . x x .  . x x .  . x x .
 L . . L  x . . x  L . . L  x . . x
 L . . L  x . . x  L . . L  x . . x
 . x x .  . x x .  . x x .  . x x .

          . x x .
          x . . x
          x . . x
          . x x .""", 'ascii'),)
        )

class Build444NewPhase3Corners(BFS):
    """  
    """

    def __init__(self):
        BFS.__init__(self,
            '444-stage-phase3-corners',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),
            '4x4x4',
            'lookup-table-4x4x4-phase3-corners.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          U . . U
          . . . .
          . . . .
          U . . U

 x . . x  x . . x  x . . x  x . . x
 . . . .  . . . .  . . . .  . . . .
 . . . .  . . . .  . . . .  . . . .
 x . . x  x . . x  x . . x  x . . x

          U . . U
          . . . .
          . . . .
          U . . U""", 'ascii'),)
        )

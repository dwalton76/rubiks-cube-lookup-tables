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


# The following is a two phase alternative to the
# step30, 31, 32 phase above.  This is to be used
# by smaller platforms (raspberry pi) with less
# cpu/memory.
# ==================================================
# Pair the last eight EOed edges
# ==================================================
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
            'lookup-table-4x4x4-step41.txt',
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
            'starting-states-lookup-table-4x4x4-step42.txt',
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
            'lookup-table-4x4x4-step42.txt',
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
            'starting-states-lookup-table-4x4x4-step40.txt',
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
            'lookup-table-4x4x4-step40.txt',
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


# ==================================================
# Pair the last eight EOed edges
# ==================================================
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
            'lookup-table-4x4x4-step51.txt',
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
            'lookup-table-4x4x4-step52.txt',
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
            'lookup-table-4x4x4-step50.txt',
            False, # store_as_hex

            # starting cubes
            (('.UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU.', 'ULFRBD')),
            use_edges_pattern=True
        )

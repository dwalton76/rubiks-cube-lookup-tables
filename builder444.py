#!/usr/bin/env python3

from buildercore import BFS
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)


# dwalton
# Combine tsai phases 1 and 2?
class StartingStates444TsaiPhase0LRCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LR-centers-stage',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "L", "L'", "Lw", "Lw'",
             "R", "R'", "Rw", "Rw'"),
            '4x4x4',
            'starting-states-4x4x4-step02-LR-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . R R .  . x x .
 . L L .  . x x .  . R R .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),),
        )

class Build444TsaiPhase0LRCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LR-centers-stage',
            # TPR also restricts these
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step02-LR-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('.....xx..xx..........LL..LL..........xx..xx..........RR..RR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LL..RR..........xx..xx..........LL..RR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LL..RR..........xx..xx..........RR..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LR..LR..........xx..xx..........LR..LR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LR..LR..........xx..xx..........RL..RL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LR..RL..........xx..xx..........RL..LR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RL..LR..........xx..xx..........LR..RL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RL..RL..........xx..xx..........LR..LR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RL..RL..........xx..xx..........RL..RL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RR..LL..........xx..xx..........LL..RR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RR..LL..........xx..xx..........RR..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RR..RR..........xx..xx..........LL..LL..........xx..xx..........xx..xx.....', 'ULFRBD'))
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


class StartingStates444TsaiPhase2Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-centers',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'", "R", "R'",
             "Lw", "Lw'", "Rw", "Rw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step61-tsai-phase2-centers.txt',
            False, # store_as_hex

            # starting cubes
           (("""
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
          . . . .""", 'ascii'),),

        )

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
            (('.....UU..UU..........LL..LL..........FF..FF..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..RR..........FF..FF..........LL..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..RR..........FF..FF..........RR..LL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..LR..........FF..FF..........LR..LR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..LR..........FF..FF..........RL..RL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..RL..........FF..FF..........RL..LR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..LR..........FF..FF..........LR..RL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..RL..........FF..FF..........LR..LR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..RL..........FF..FF..........RL..RL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..LL..........FF..FF..........LL..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..LL..........FF..FF..........RR..LL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..RR..........FF..FF..........LL..LL..........FF..FF..........UU..UU.....', 'ULFRBD'))
        )


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
             ('.UD.D..UU..D.DU..DU.DRRUURRD.UD..DU.U..DD..U.UD..DU.DLLUULLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.', 'ULFRBD'))
        ) 


class StartingStates444TsaiPhase2(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'", "R", "R'",
             "Lw", "Lw'", "Rw", "Rw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step60-tsai-phase2.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U D .
          D U U U
          U U U D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U F F D  D R R U  U F F D
 U L L D  D F F U  U R R D  D F F U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D U U U
          U U U D
          . D U .""", 'ascii'),)
        )


class Build444TsaiPhase2(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'lookup-table-4x4x4-step60-tsai-phase2.txt',
            False, # store_as_hex

            # starting cubes
            (('.UD.DUUUUUUD.DU..DU.DLLUULLD.UD..DU.UFFDDFFU.UD..DU.DRRUURRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUURLD.UD..DU.UFFDDFFU.UD..DU.DRLUULRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUULRD.UD..DU.UFFDDFFU.UD..DU.DLRUURLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUURRD.UD..DU.UFFDDFFU.UD..DU.DLLUULLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'))
        )



class Build444Phase3Edges(BFS):
    """
    This is the TPR phase3 edges table.
    This table will have ~239 million entries.
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
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step71-tsai-phase3-edges.txt',
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

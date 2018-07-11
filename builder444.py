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
          . L L .
          . L L .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . x x .  . x x .  . x x .
 . x x .  . x x .  . x x .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . L L .
          . L L .
          . . . .""", 'ascii'),

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

             ("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . L L .  . x x .  . L L .
 . x x .  . L L .  . x x .  . L L .
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
          . . . .""", 'ascii'),

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


            ("""
          . . . .
          . F F .
          . F F .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . U U .  . R R .  . U U .
 . L L .  . U U .  . R R .  . U U .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . F F .
          . F F .
          . . . .""", 'ascii'),

            ("""
          . . . .
          . F F .
          . F F .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R R .  . U U .  . L L .  . U U .
 . R R .  . U U .  . L L .  . U U .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . F F .
          . F F .
          . . . .""", 'ascii')),
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
            (('.....FF..FF..........LL..LL..........UU..UU..........RR..RR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LL..RR..........UU..UU..........LL..RR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LL..RR..........UU..UU..........RR..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LR..LR..........UU..UU..........LR..LR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LR..LR..........UU..UU..........RL..RL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LR..RL..........UU..UU..........RL..LR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RL..LR..........UU..UU..........LR..RL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RL..RL..........UU..UU..........LR..LR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RL..RL..........UU..UU..........RL..RL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RR..LL..........UU..UU..........LL..RR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RR..LL..........UU..UU..........RR..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RR..RR..........UU..UU..........LL..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....UU..UU..........LL..LL..........FF..FF..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
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


class Build444TsaiPhase2Edges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-edges',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'lookup-table-4x4x4-step62-tsai-phase2-edges.txt',
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


class StartingStates444Phase3Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase3-centers',
            moves_444,
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step72-tsai-phase3-centers.txt',
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
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class Build444Phase3Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase3-centers',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step72-tsai-phase3-centers.txt',
            False, # store_as_hex

            # starting cubes
            (('.....BB..BB..........LL..LL..........UU..UU..........RR..RR..........DD..DD..........FF..FF.....', 'ULFRBD'),
             ('.....BB..BB..........RR..RR..........DD..DD..........LL..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....DD..DD..........LL..LL..........BB..BB..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....DD..DD..........RR..RR..........FF..FF..........LL..LL..........BB..BB..........UU..UU.....', 'ULFRBD'),
             ('.....FF..FF..........LL..LL..........DD..DD..........RR..RR..........UU..UU..........BB..BB.....', 'ULFRBD'),
             ('.....FF..FF..........RR..RR..........UU..UU..........LL..LL..........DD..DD..........BB..BB.....', 'ULFRBD'),
             ('.....UU..UU..........LL..LL..........FF..FF..........RR..RR..........BB..BB..........DD..DD.....', 'ULFRBD'),
             ('.....UU..UU..........RR..RR..........BB..BB..........LL..LL..........FF..FF..........DD..DD.....', 'ULFRBD'))
        )


class StartingStates444Phase3(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase3',
            moves_444,
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step70-tsai-phase3.txt',
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
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
#            use_edges_pattern=True
        )


class Build444Phase3(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase3',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step70-tsai-phase3.txt',
            False, # store_as_hex

            # starting cubes
            (('.BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD.', 'ULFRBD')),
            use_edges_pattern=True
        )

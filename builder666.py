#!/usr/bin/env python3

from buildercore import BFS
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, solved_666, moves_666, rotate_666
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)


class StartingStates666UDInnerXCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '6x6x6-UD-inner-x-centers-stage',
            moves_666,
            '6x6x6',
            'starting-states-6x6x6-step10-UD-inner-x-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . x x . .  . . x x . .  . . x x . .  . . x x . .
 . . x x . .  . . x x . .  . . x x . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . . """, 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class Build666UDInnerXCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '6x6x6-UD-inner-x-centers-stage',
            (),
            '6x6x6',
            'lookup-table-6x6x6-step10-UD-inner-x-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('..............UU....UU............................xx....xx............................xx....xx............................xx....xx............................xx....xx............................UU....UU..............', 'ULFRBD'),
             ('..............xx....xx............................UU....UU............................xx....xx............................UU....UU............................xx....xx............................xx....xx..............', 'ULFRBD'),
             ('..............xx....xx............................xx....xx............................UU....UU............................xx....xx............................UU....UU............................xx....xx..............', 'ULFRBD'),),
        )


class StartingStates666UDObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '6x6x6-UD-oblique-edges-stage',

            # illegal_moves
            ("3Fw", "3Fw'", "3Fw2",
             "3Bw", "3Bw'", "3Bw2",
             "3Lw", "3Lw'", "3Lw2",
             "3Rw", "3Rw'", "3Rw2",
             "3Uw", "3Uw'", "3Uw2",
             "3Dw", "3Dw'", "3Dw2",
            ),
            '6x6x6',
            'starting-states-6x6x6-step20-UD-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
              . . . . . .
              . . U U . .
              . U . . U .
              . U . . U .
              . . U U . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . x x . .  . . x x . .  . . x x . .  . . x x . .
 . x . . x .  . x . . x .  . x . . x .  . x . . x .
 . x . . x .  . x . . x .  . x . . x .  . x . . x .
 . . x x . .  . . x x . .  . . x x . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . U U . .
              . U . . U .
              . U . . U .
              . . U U . .
              . . . . . . """, 'ascii'),),
        )


class Build666UDObliqueEdgesStage(BFS):

    def __init__(self):
        from builder666ss import starting_states_step20
        BFS.__init__(self,
            '6x6x6-UD-oblique-edges-stage',

            # illegal_moves
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'"),
            '6x6x6',
            'lookup-table-6x6x6-step20-UD-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            starting_states_step20,
        )


class StartingStates666LRInnerXCentersObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '6x6x6-LR-inner-x-centers-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "3Uw", "3Uw'", "3Uw2",
             "3Dw", "3Dw'", "3Dw2",
             "3Lw2", "3Rw2", "3Bw2", "3Fw2"),
            '6x6x6',
            'starting-states-6x6x6-step30-LR-inner-x-centers-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . L L L L .  . x x x x .  . L L L L .  . x x x x .
 . L L L L .  . x x x x .  . L L L L .  . x x x x .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . . """, 'ascii'),

             ("""
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . x x . .  . . L L . .  . . x x . .  . . L L . .
 . x x x x .  . L L L L .  . x x x x .  . L L L L .
 . x x x x .  . L L L L .  . x x x x .  . L L L L .
 . . x x . .  . . L L . .  . . x x . .  . . L L . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . . """, 'ascii')),
        )


class Build666LRInnerXCentersObliqueEdgesStage(BFS):

    def __init__(self):
        from builder666ss import starting_states_step30
        BFS.__init__(self,
            '6x6x6-LR-inner-x-centers-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),
            '6x6x6',
            'lookup-table-6x6x6-step30-LR-inner-x-centers-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            starting_states_step30,
        )


class StartingStates666LRObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '6x6x6-LR-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "3Uw", "3Uw'", "3Uw2",
             "3Dw", "3Dw'", "3Dw2",
             "3Lw2", "3Rw2", "3Bw2", "3Fw2"),
            '6x6x6',
            'starting-states-6x6x6-step31-LR-oblique-edges-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . L . . L .  . x . . x .  . L . . L .  . x . . x .
 . L . . L .  . x . . x .  . L . . L .  . x . . x .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . . """, 'ascii'),),
        )


class Build666LRObliqueEdgesStage(BFS):

    def __init__(self):
        from builder666ss import starting_states_step31
        BFS.__init__(self,
            '6x6x6-LR-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),
            '6x6x6',
            'lookup-table-6x6x6-step31-LR-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            starting_states_step31
        )


class Build666LRInnerXCenterStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '6x6x6-LR-inner-x-center-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),
            '6x6x6',
            'lookup-table-6x6x6-step32-LR-inner-x-center-stage.txt',
            True, # store_as_hex

            # starting cubes
            (
             ("""
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . . """, 'ascii'),

             ("""
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . x x . .  . . L L . .  . . x x . .  . . L L . .
 . . x x . .  . . L L . .  . . x x . .  . . L L . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . . """, 'ascii')
            ),
        )


#!/usr/bin/env python3

from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)


# =======
# Phase 3
# =======
class Build555EdgeOrientOuterOrbit(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-EO-outer-orbit',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step42-edge-orient.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . U . D .
            D . . . U
            . . . . .
            U . . . D
            . D . U .

 . D . U .  . D . U .  . D . U .  . D . U .
 D . . . U  U . . . D  D . . . U  U . . . D
 . . . . .  . . . . .  . . . . .  . . . . .
 U . . . D  D . . . U  U . . . D  D . . . U
 . U . D .  . U . D .  . U . D .  . U . D .

            . U . D .
            D . . . U
            . . . . .
            U . . . D
            . D . U .""", "ascii"),)
        )


class StartingStates555LRCenterStage(BFS):
    """
    There should be 432 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step41-LR-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . . . . .  . R R R .  . . . . .
 . L L L .  . . . . .  . R R R .  . . . . .
 . L L L .  . . . . .  . R R R .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),)
        )


class Build555LRCenterStage(BFS):

    def __init__(self):
        from builder555ss import starting_states_step41
        BFS.__init__(self,
            '5x5x5-LR-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step41-LR-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_step41
        )


class StartingState555EdgeOrientOuterOrbitLRCenterStage(BFS):
    """
    There should be 432 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edge-orient-LR-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step40-edge-orient-LR-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . U . D .
            D . . . U
            . . . . .
            U . . . D
            . D . U .

 . D . U .  . D . U .  . D . U .  . D . U .
 D L L L U  U . . . D  D R R R U  U . . . D
 . L L L .  . . . . .  . R R R .  . . . . .
 U L L L D  D . . . U  U R R R D  D . . . U
 . U . D .  . U . D .  . U . D .  . U . D .

            . U . D .
            D . . . U
            . . . . .
            U . . . D
            . D . U .""", "ascii"),)
        )


class Build555EdgeOrientOuterOrbitLRCenterStage(BFS):

    def __init__(self):
        from builder555ss import starting_states_step40
        BFS.__init__(self,
            '5x5x5-edge-orient-outer-orbit-LR-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step40-edge-orient-LR-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_step40
        )


# =======
# Phase 4
# =======
class StartingStates555FBCenterStage(BFS):
    """
    There should be 432 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-FB-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step51-FB-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),)
        )


class Build555FBCenterStage(BFS):

    def __init__(self):
        from builder555ss import starting_states_step51
        BFS.__init__(self,
            '5x5x5-FB-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'lookup-table-5x5x5-step51-FB-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_step51
        )


class StartingStates555XPlaneEdgesStage(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-edges-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step52-x-plane-edges-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .

 . x x x .  . x x x .  . x x x .  . x x x .
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 . x x x .  . x x x .  . x x x .  . x x x .

            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .""", "ascii"),),
            use_edges_pattern=True
        )


class Build555XPlaneEdgesStage(BFS):

    def __init__(self):
        from builder555ss import starting_states_step52
        BFS.__init__(self,
            '5x5x5-x-plane-edges-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'lookup-table-5x5x5-step52-x-plane-edges-stage.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_step52,
            use_edges_pattern=True
        )

'''
class StartingStates555XPlaneOuterEdgesStage(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-outer-edges-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step52-x-plane-outer-edges-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .

 . x x x .  . x x x .  . x x x .  . x x x .
 L . . . L  F . . . F  R . . . R  B . . . B
 x . . . x  x . . . x  x . . . x  x . . . x
 L . . . L  F . . . F  R . . . R  B . . . B
 . x x x .  . x x x .  . x x x .  . x x x .

            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .""", "ascii"),),
            use_edges_pattern=True
        )


class Build555XPlaneOuterEdgesStage(BFS):

    def __init__(self):
        from builder555ss import starting_states_step52
        BFS.__init__(self,
            '5x5x5-x-plane-outer-edges-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'lookup-table-5x5x5-step52-x-plane-outer-edges-stage.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_step52,
            use_edges_pattern=True
        )


class StartingStates555XPlaneInnerEdgesStage(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-inner-edges-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step53-x-plane-inner-edges-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .

 . x x x .  . x x x .  . x x x .  . x x x .
 x . . . x  x . . . x  x . . . x  x . . . x
 L . . . L  F . . . F  R . . . R  B . . . B
 x . . . x  x . . . x  x . . . x  x . . . x
 . x x x .  . x x x .  . x x x .  . x x x .

            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .""", "ascii"),),
            use_edges_pattern=True
        )


class Build555XPlaneInnerEdgesStage(BFS):

    def __init__(self):
        from builder555ss import starting_states_step53
        BFS.__init__(self,
            '5x5x5-x-plane-inner-edges-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'lookup-table-5x5x5-step53-x-plane-inner-edges-stage.txt',
            False, # store_as_hex

            # starting cubes
            starting_states_step53,
            use_edges_pattern=True
        )
'''


# =======
# Phase 5
# =======
class StartingStates555Phase5LFRBCenterStage(BFS):
    """
    There should be 36 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LFRB-center-stage',

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
             "Uw2", "Dw2"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step61-LFRB-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),)
        )


class Build555Phase5LFRBCenterStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LFRB-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),

            '5x5x5',
            'lookup-table-5x5x5-step61-LFRB-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (('...............................LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............BFB..BFB..BFB............LRR..LRR..LRR............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............BFB..BFB..BFB............RRL..RRL..RRL............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............BFF..BFF..BFF............LRR..LRR..LRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............BFF..BFF..BFF............LRR..LRR..LRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............BFF..BFF..BFF............RRL..RRL..RRL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............BFF..BFF..BFF............RRL..RRL..RRL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFB..FFB..FFB............LRR..LRR..LRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFB..FFB..FFB............LRR..LRR..LRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFB..FFB..FFB............RRL..RRL..RRL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFB..FFB..FFB............RRL..RRL..RRL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............BFB..BFB..BFB............LRR..LRR..LRR............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............BFB..BFB..BFB............RRL..RRL..RRL............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............BFF..BFF..BFF............LRR..LRR..LRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............BFF..BFF..BFF............LRR..LRR..LRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............BFF..BFF..BFF............RRL..RRL..RRL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............BFF..BFF..BFF............RRL..RRL..RRL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFB..FFB..FFB............LRR..LRR..LRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFB..FFB..FFB............LRR..LRR..LRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFB..FFB..FFB............RRL..RRL..RRL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFB..FFB..FFB............RRL..RRL..RRL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR............BFB..BFB..BFB............LRL..LRL..LRL............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR............BFF..BFF..BFF............LRL..LRL..LRL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR............BFF..BFF..BFF............LRL..LRL..LRL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR............FFB..FFB..FFB............LRL..LRL..LRL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR............FFB..FFB..FFB............LRL..LRL..LRL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB...............................', 'ULFRBD'))
        )

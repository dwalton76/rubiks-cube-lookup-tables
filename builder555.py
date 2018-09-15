#!/usr/bin/env python3

from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)

# TODO
# - rebuild the step41 table on LJ's machine, it now is 2-edges anywhere
#   with any orientation...maybe I started rebuilding and the counts are all the same
#   Can't hurt but is low priority

class Build555UDCenterStage(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-UD-center-stage',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step10-UD-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . x x x .  . x x x .  . x x x .  . x x x .
 . x x x .  . x x x .  . x x x .  . x x x .
 . x x x .  . x x x .  . x x x .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .""", "ascii"),),
        )


class Build555UDCenterStageTCenterOnly(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-UD-t-center-stage',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step11-UD-centers-stage-t-center-only.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . x . .  . . x . .  . . x . .  . . x . .
 . x . x .  . x . x .  . x . x .  . x . x .
 . . x . .  . . x . .  . . x . .  . . x . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .""", "ascii"),),
        )


class Build555UDCenterStageXCenterOnly(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-UD-x-center-stage',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step12-UD-centers-stage-x-center-only.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . U . U .
            . . . . .
            . U . U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . x . x .  . x . x .  . x . x .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .
 . x . x .  . x . x .  . x . x .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . U . U .
            . . . . .
            . U . U .
            . . . . .""", "ascii"),),
        )



class Build555LRCenterStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-lr-center-stage',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step20-LR-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . x x x .  . L L L .  . x x x .
 . L L L .  . x x x .  . L L L .  . x x x .
 . L L L .  . x x x .  . L L L .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),)
        )


class Build555LRTCenterStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-lr-t-center-stage',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step21-LR-t-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . L . .  . . x . .  . . L . .  . . x . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . L . .  . . x . .  . . L . .  . . x . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),)
        )


class Build555LRXCenterStage(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-lr-x-center-stage',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step22-LR-x-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),)
        )



# This is used to build the 5x5x5-pair-last-four-edges table
class Build555ULFRBDCenterSolveUnstaged(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-centers-solve-unstaged',

            (),
            '5x5x5',
            'lookup-table-5x5x5-step30-ULFRBD-centers-solve-unstaged.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""", "ascii"),)
        )


class Build555ULFRBDCenterSolve(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-centers-solve',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),

            '5x5x5',
            'lookup-table-5x5x5-step30-ULFRBD-centers-solve.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . x x x .  . x x x .
 . L L L .  . F F F .  . x x x .  . x x x .
 . L L L .  . F F F .  . x x x .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .""", "ascii"),)
        )


class Build555ULCenterSolve(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-UL-centers-solve',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),

            '5x5x5',
            'lookup-table-5x5x5-step31-UL-centers-solve.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . . . . .  . x x x .  . . . . .
 . L L L .  . . . . .  . x x x .  . . . . .
 . L L L .  . . . . .  . x x x .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .""", "ascii"),)
        )


class Build555UFCenterSolve(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-UF-centers-solve',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),

            '5x5x5',
            'lookup-table-5x5x5-step32-UF-centers-solve.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . x x x .
 . . . . .  . F F F .  . . . . .  . x x x .
 . . . . .  . F F F .  . . . . .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .""", "ascii"),)
        )


class Build555LFCenterSolve(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LF-centers-solve',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),

            '5x5x5',
            'lookup-table-5x5x5-step33-LF-centers-solve.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . x x x .  . x x x .
 . L L L .  . F F F .  . x x x .  . x x x .
 . L L L .  . F F F .  . x x x .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),)
        )


class Build555ULFRBDTCenterSolve(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-t-centers-solve',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),

            '5x5x5',
            'lookup-table-5x5x5-step33-ULFRBD-t-centers-solve.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . L . .  . . F . .  . . R . .  . . B . .
 . L . L .  . F . F .  . R . R .  . B . B .
 . . L . .  . . F . .  . . R . .  . . B . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . D . .
            . D . D .
            . . D . .
            . . . . .""", "ascii"),)
        )


# =====================================
# Staging L4E Edges with solved centers
# =====================================
class Build555EdgesStageFirstFour(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-stage-first-four',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step200-stage-first-four-edges.txt',
            True, # store_as_hex
            (("""
            . - - - .
            - U U U -
            - U U U -
            - U U U -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - D D D -
            - D D D -
            - D D D -
            . - - - .""", "ascii"),

            ("""
            . L L L .
            - U U U -
            - U U U -
            - U U U -
            . L L L .

 . - - - .  . L L L .  . - - - .  . L L L .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . - - - .  . L L L .  . - - - .  . L L L .

            . L L L .
            - D D D -
            - D D D -
            - D D D -
            . L L L .""", "ascii"),

            ("""
            . - - - .
            L U U U L
            L U U U L
            L U U U L
            . - - - .

 . L L L .  . - - - .  . L L L .  . - - - .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . L L L .  . - - - .  . L L L .  . - - - .

            . - - - .
            L D D D L
            L D D D L
            L D D D L
            . - - - .""", "ascii"))
        )


class Build555EdgesStageSecondFour(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-stage-second-four',
            ("Rw", "Rw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "L", "L'",
             "F", "F'",
             "R", "R'",
             "B", "B'"),
            '5x5x5',
            'lookup-table-5x5x5-step210-stage-second-four-edges.txt',
            True, # store_as_hex
            (("""
            . L L L .
            - U U U -
            - U U U -
            - U U U -
            . L L L .

 . - - - .  . L L L .  . - - - .  . L L L .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . - - - .  . L L L .  . - - - .  . L L L .

            . L L L .
            - D D D -
            - D D D -
            - D D D -
            . L L L .""", "ascii"),

            ("""
            . - - - .
            L U U U L
            L U U U L
            L U U U L
            . - - - .

 . L L L .  . - - - .  . L L L .  . - - - .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . L L L .  . - - - .  . L L L .  . - - - .

            . - - - .
            L D D D L
            L D D D L
            L D D D L
            . - - - .""", "ascii"))
        )


# ==================================
# Solve last L4E with solved centers
# ==================================
class Build555ULFRBDCenterSolveUnstagedEdgesLastFourXPlane(BFS):
    """
    This is the centers table that is used for pruning when building
    the Build555EdgesLastFourXPlane table.
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-centers-solve-unstaged',

            ("Rw", "Rw'", "Rw2",
             "Lw", "Lw'", "Lw2",
             "Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "L", "L'",
             "F", "F'",
             "R", "R'",
             "B", "B'"),

            '5x5x5',
            'lookup-table-5x5x5-step220-ULFRBD-centers-solve-unstaged.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""", "ascii"),)
        )


class Build555EdgesLastFourXPlane(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-last-four-x-plane',

            ("Rw", "Rw'", "Rw2",
             "Lw", "Lw'", "Lw2",
             "Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "L", "L'",
             "F", "F'",
             "R", "R'",
             "B", "B'"),
            '5x5x5',
            'lookup-table-5x5x5-step220-edges-last-four-x-plane.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - U U U -
            - U U U -
            - U U U -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - D D D -
            - D D D -
            - D D D -
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
        )


# =================================
# New edge pairing code starts here
# =================================
class StartingStates555Step40(BFS):
    """
    Pair 4-edges anywhere
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step40',

            # illegal moves
            ("Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "Lw", "Lw'", "Lw2",
             "Rw", "Rw'", "Rw2",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step40.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
        )


class Build555Step40(BFS):
    """
    Pair 4-edges anywhere
    """

    def __init__(self):
        from builder555ss import starting_states_step40
        BFS.__init__(self,
            '5x5x5-step41',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step40.txt',
            False, # store_as_hex
            starting_states_step40,
            use_edges_pattern=True
        )


class StartingStates555Step41(BFS):
    """
    Pair 2-edges anywhere
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step41',

            # illegal moves
            ("Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "Lw", "Lw'", "Lw2",
             "Rw", "Rw'", "Rw2",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step41.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F . . . F  R . . . -  - . . . -
 - . . . L  F . . . F  R . . . -  - . . . -
 - . . . L  F . . . F  R . . . -  - . . . -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
        )


class Build555Step41(BFS):
    """
    Pair 2-edges anywhere
    """

    def __init__(self):
        from builder555ss import starting_states_step41
        BFS.__init__(self,
            '5x5x5-step41',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step41.txt',
            False, # store_as_hex
            starting_states_step41,
            use_edges_pattern=True
        )


class Build555Step50(BFS):
    """
    move 4-edges to y-plane
    """
    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step50',

            # illegal moves
            ("Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "Lw", "Lw'", "Lw2",
             "Rw", "Rw'", "Rw2",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step50.txt',
            False, # store_as_hex
            (("""
            . U U U .
            - . . . -
            - . . . -
            - . . . -
            . U U U .

 . - - - .  . F F F .  . - - - .  . B B B .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - - - .  . F F F .  . - - - .  . B B B .

            . D D D .
            - . . . -
            - . . . -
            - . . . -
            . D D D .""", "ascii"),),
            use_edges_pattern=True
        )


class StartingStates555Step60(BFS):
    """
    LR centers to horizontal bars or solved
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step60',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step60.txt',
            False, # store_as_hex
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
            . . . . .""", "ascii"),),
            legal_moves=(
                "L2", "R2",
                "2U2", "2D2",
            )
        )


class Build555Step60(BFS):
    """
    LR centers to horizontal bars or solved
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step60',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'", "Lw2",
             "Rw", "Rw'", "Rw2",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "U", "U'",
             "D", "D'",
             "F", "F'",
             "B", "B'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step60.txt',
            False, # store_as_hex
            (('...............................LLL..LLL..LLL.....................................RRR..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR.....................................LLL..RRR..LLL........................................................', 'ULFRBD'))
        )


class StartingStates555Step70(BFS):
    """
    FB centers to vertical bars or solved
    LR centers to solved
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step70',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step70.txt',
            False, # store_as_hex
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
            . . . . .""", "ascii"),),
            legal_moves=(
                "F2", "B2",
                "2L2", "2R2",
            )
        )


class Build555Step70(BFS):
    """
    FB centers to vertical bars or solved
    LR centers to solved
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step70',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "U", "U'",
             "D", "D'",
             "L", "L'",
             "R", "R'",
             "Fw2", "Bw2",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step70.txt',
            False, # store_as_hex
            (('...............................LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'))
        )


class StartingStates555Step80(BFS):
    """
    UD centers to vertical bars, horizontal bars or solved
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step80',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step80.txt',
            False, # store_as_hex
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""", "ascii"),),
            legal_moves=(
                "U2", "D2", "U", "U'", "D", "D'",
                "2L2", "2R2",
                "2F2", "2B2",
            )
        )


class Build555Step80(BFS):
    """
    UD centers to vertical bars, horizontal bars or solved
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step80',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
             "Bw2", "Fw2",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step80.txt',
            False, # store_as_hex
            (('......DDD..UUU..DDD................................................................................................................UUU..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU................................................................................................................DDD..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU................................................................................................................UUU..DDD..DDD......', 'ULFRBD'),
             ('......DUD..DUD..DUD................................................................................................................UDU..UDU..UDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU................................................................................................................DDU..DDU..DDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU................................................................................................................UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUD..UUD..UUD................................................................................................................DDU..DDU..DDU......', 'ULFRBD'),
             ('......UUD..UUD..UUD................................................................................................................UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUU..UUU..DDD................................................................................................................DDD..DDD..UUU......', 'ULFRBD'),
             ('......UUU..UUU..DDD................................................................................................................UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU................................................................................................................DDD..DDD..DDD......', 'ULFRBD'))
        )


class StartingStates555Step90(BFS):
    """
    - FB centers stay in vertical bars
    - UD centers to solved
    - pair 2-edges at DL DR
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step90',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step90.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - U U U -
            - U U U -
            - U U U -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 . L L L .  . - - - .  . R R R .  . - - - .

            . - - - .
            D D D D D
            D D D D D
            D D D D D
            . - - - .""", "ascii"),

             ("""
            . - - - .
            - U U U -
            - U U U -
            - U U U -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 . D D D .  . - - - .  . R R R .  . - - - .

            . - - - .
            L D D D D
            L D D D D
            L D D D D
            . - - - .""", "ascii"),

             ("""
            . - - - .
            - U U U -
            - U U U -
            - U U U -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 . L L L .  . - - - .  . D D D .  . - - - .

            . - - - .
            D D D D R
            D D D D R
            D D D D R
            . - - - .""", "ascii"),

             ("""
            . - - - .
            - U U U -
            - U U U -
            - U U U -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 . D D D .  . - - - .  . D D D .  . - - - .

            . - - - .
            L D D D R
            L D D D R
            L D D D R
            . - - - .""", "ascii")),

            use_edges_pattern=True,
            legal_moves=(
                "2L2",
                "2R2",
                "L2", "R2",
                "F2", "B2",
                "U", "U'", "U2",
                "D", "D'", "D2",
            )
        )


class Build555Step90(BFS):
    """
    - FB centers stay in vertical bars
    - UD centers to solved
    - pair 2-edges at DL DR
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step90',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step90.txt',
            False, # store_as_hex
            (('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-BFB--BFB--BFB-.---..---.-...--...--...-.DDD..---.-FBF--FBF--FBF-.---..---.LDDDRLDDDRLDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-BFB--BFB--BFB-.---..---.-...--...--...-.LLL..---.-FBF--FBF--FBF-.---..---.RDDDDRDDDDRDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-BFF--BFF--BFF-.---..---.-...--...--...-.DDD..---.-BBF--BBF--BBF-.---..---.LDDDRLDDDRLDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-BFF--BFF--BFF-.---..---.-...--...--...-.DDD..---.-FBB--FBB--FBB-.---..---.LDDDRLDDDRLDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-BFF--BFF--BFF-.---..---.-...--...--...-.RRR..---.-BBF--BBF--BBF-.---..---.LDDDDLDDDDLDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-BFF--BFF--BFF-.---..---.-...--...--...-.RRR..---.-FBB--FBB--FBB-.---..---.LDDDDLDDDDLDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-FFB--FFB--FFB-.---..---.-...--...--...-.DDD..---.-BBF--BBF--BBF-.---..---.LDDDRLDDDRLDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-FFB--FFB--FFB-.---..---.-...--...--...-.DDD..---.-FBB--FBB--FBB-.---..---.LDDDRLDDDRLDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-FFB--FFB--FFB-.---..---.-...--...--...-.RRR..---.-BBF--BBF--BBF-.---..---.LDDDDLDDDDLDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-FFB--FFB--FFB-.---..---.-...--...--...-.RRR..---.-FBB--FBB--FBB-.---..---.LDDDDLDDDDLDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-FFF--FFF--FFF-.---..---.-...--...--...-.DDD..---.-BBB--BBB--BBB-.---..---.LDDDRLDDDRLDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.DDD..---.-FFF--FFF--FFF-.---..---.-...--...--...-.LLL..---.-BBB--BBB--BBB-.---..---.RDDDDRDDDDRDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-BFB--BFB--BFB-.---..---.-...--...--...-.DDD..---.-FBF--FBF--FBF-.---..---.DDDDRDDDDRDDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-BFB--BFB--BFB-.---..---.-...--...--...-.RRR..---.-FBF--FBF--FBF-.---..---.DDDDDDDDDDDDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-BFF--BFF--BFF-.---..---.-...--...--...-.DDD..---.-BBF--BBF--BBF-.---..---.DDDDRDDDDRDDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-BFF--BFF--BFF-.---..---.-...--...--...-.DDD..---.-FBB--FBB--FBB-.---..---.DDDDRDDDDRDDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-BFF--BFF--BFF-.---..---.-...--...--...-.RRR..---.-BBF--BBF--BBF-.---..---.DDDDDDDDDDDDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-BFF--BFF--BFF-.---..---.-...--...--...-.RRR..---.-FBB--FBB--FBB-.---..---.DDDDDDDDDDDDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-FFB--FFB--FFB-.---..---.-...--...--...-.DDD..---.-BBF--BBF--BBF-.---..---.DDDDRDDDDRDDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-FFB--FFB--FFB-.---..---.-...--...--...-.DDD..---.-FBB--FBB--FBB-.---..---.DDDDRDDDDRDDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-FFB--FFB--FFB-.---..---.-...--...--...-.RRR..---.-BBF--BBF--BBF-.---..---.DDDDDDDDDDDDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-FFB--FFB--FFB-.---..---.-...--...--...-.RRR..---.-FBB--FBB--FBB-.---..---.DDDDDDDDDDDDDDD.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-FFF--FFF--FFF-.---..---.-...--...--...-.DDD..---.-BBB--BBB--BBB-.---..---.DDDDRDDDDRDDDDR.---.', 'ULFRBD'),
             ('.---.-UUU--UUU--UUU-.---..---.-...--...--...-.LLL..---.-FFF--FFF--FFF-.---..---.-...--...--...-.RRR..---.-BBB--BBB--BBB-.---..---.DDDDDDDDDDDDDDD.---.', 'ULFRBD')),
            use_edges_pattern=True,
            legal_moves=(
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
                "L2", "R2",
                "F2", "B2",
                "U", "U'", "U2",
                "D", "D'", "D2",
            )
        )


class Build555Step91(BFS):
    """
    Pair 2-edges at LD RD

    - 4-edges are paired and in x-plane so new math for 2-edges...
        - midges 16 * 14 = 224
        - wings 16 * 15 * 14 * 13 = 43680
        - 224 * 43680 = 9,784,320
        - 9,784,320/2 = 4,892,160
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step91',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step91.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . L L L .  . - - - .  . R R R .  . - - - .

            . - - - .
            D . . . D
            D . . . D
            D . . . D
            . - - - .""", "ascii"),

             ("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . D D D .  . - - - .  . R R R .  . - - - .

            . - - - .
            L . . . D
            L . . . D
            L . . . D
            . - - - .""", "ascii"),

             ("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . L L L .  . - - - .  . D D D .  . - - - .

            . - - - .
            D . . . R
            D . . . R
            D . . . R
            . - - - .""", "ascii"),

             ("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . D D D .  . - - - .  . D D D .  . - - - .

            . - - - .
            L . . . R
            L . . . R
            L . . . R
            . - - - .""", "ascii")),
            use_edges_pattern=True,
            legal_moves=(
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
                "L2", "R2",
                "F2", "B2",
                "U", "U'", "U2",
                "D", "D'", "D2",
            )
        )



class StartingStates555Step92(BFS):
    """
    - FB centers stay in vertical bars
    - UD centers to solved
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step92',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step92.txt',
            False, # store_as_hex
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""", "ascii"),),
            legal_moves=(
                "2L2", "2R2",
                "U", "U'", "U2",
                "D", "D'", "D2",
            )
        )


class Build555Step92(BFS):
    """
    - FB centers stay in vertical bars
    - UD centers to solved
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step92',

            # Illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step92.txt',
            False, # store_as_hex
            (('......UUU..UUU..UUU.....................................BFB..BFB..BFB.....................................FBF..FBF..FBF............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................BFF..BFF..BFF.....................................BBF..BBF..BBF............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................FFB..FFB..FFB.....................................FBB..FBB..FBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................FFF..FFF..FFF.....................................BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD')),
            legal_moves=(
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
                "L2", "R2",
                "F2", "B2",
                "U", "U'", "U2",
                "D", "D'", "D2",
            )
        )


class Build555Step100(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step100',

            # illegal moves...will list legal moves instead
            (),

            '5x5x5',
            'lookup-table-5x5x5-step100.txt',

            False, # store_as_hex
            (("""
            . U U U .
            U U U U U
            U U U U U
            U U U U U
            . U U U .

 . L L L .  . F F F .  . R R R .  . B B B .
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 - . . . -  - F F F -  - . . . -  - B B B -
 . - - - .  . F F F .  . - - - .  . B B B .

            . D D D .
            - D D D -
            - D D D -
            - D D D -
            . D D D .""", "ascii"),),
            use_edges_pattern=True,
            legal_moves=(
                "D2", "F2", "B2", "U", "U'", "U2",
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
            )
        )


class Build555Step101(BFS):
    """
    Should be 12! or 479,001,600 states
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step101',

            # illegal moves...will list legal moves instead
            (),

            '5x5x5',
            'lookup-table-5x5x5-step101.txt',
            False, # store_as_hex
            (("""
            . U U U .
            U . . . U
            U . . . U
            U . . . U
            . U U U .

 . L L L .  . F F F .  . R R R .  . B B B .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - - - .  . F F F .  . - - - .  . B B B .

            . D D D .
            - . . . -
            - . . . -
            - . . . -
            . D D D .""", "ascii"),),
            use_edges_pattern=True,
            legal_moves=(
                "D2", "F2", "B2", "U", "U'", "U2",
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
            )
        )


class Build555Step102(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step102',

            # illegal moves...will list legal moves instead
            (),

            '5x5x5',
            'lookup-table-5x5x5-step102.txt',
            False, # store_as_hex
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""", "ascii"),),
            legal_moves=(
                "D2", "F2", "B2", "U", "U'", "U2",
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
            )
        )


'''
brainstorm
==========
step10,20 - stage centers
    - 20 moves

step40
    - pair 4-edges anywhere
    - pair 2-edge prune table
        - midges 24 * 22 = 528
        - wings 24 * 23 * 22 * 21 = 255,024
        - 528 * 255,024 = 134,652,672
        - It is actually this /2, I am not sure why but have seen this pattern before
            134,652,672 / 2 = 67,326,336
    - We pair 2-edges, then pair 4-edges where we skip any move that breaks up the
      previously 2-edges
    ~13 moves


step50
    - move 4-edges to y-plane
    ~4 moves

step60
    - LR centers to horizontal bars
    - At the end of this stage do a U and D to move the 4-edges to z-plane
    ~6 moves?

step70
    - FB centers to vertical bars (4900 states)
    - LR centers solved (6 states)
    - At the end of this stage do a L and R to move the LR centers to vertical bars
    - LFRB centers will be vertical bars with 4-edges in x-plane
    ~7 moves?

    TODO Trying to pair 2-edges in step90 is just brutal.  Can we do that here and put them
    at BL BR?  Then when we do the L R move to put the 4-edges in x-plane the other 2-edges
    will be at DL DR like we need.


step80
    - UD centers to bars
    ~4 moves?
    TODO could we skip this and do it as part of step100?

step90
    - pair 2-edges at DL DR
        - 4-edges are paired and in x-plane so new math for 2-edges...
            - midges 16 * 14 = 224
            - wings 16 * 15 * 14 * 13 = 43680
            - 224 * 43680 = 9,784,320
            - 9,784,320/2 = 4,892,160
    - 4,892,160/(4,892,160 * 4900 * 6) = 0.000 034
    - (4,892,160 * 6)/(4,892,160 * 4900 * 6) = 0.000 204
    ~11 moves?

    4-edges here?
        - midges 16 * 14 * 12 * 10 = 26,880
        - wings 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 = 518,918,400
        - (26,880 * 518,918,400) / 2 = 6,974,263,296,000

step100
    - solve UFBD centers
    - pair last 6-edges
    - this will use y-plane slices to keep 4 of the unpaired edges on side U, the
      other two will be at DU DB
    - y-plane slice is only allowed if side U is solved or vertical bar
    - edges prune table should be 12! or 479,001,600
    - centers prune table is 4950
    - 479001600/(479001600*4950) = 0.000 202
    ~14 moves?


step100 pair 8-edges?
    _ 6 UD states?
    _ 4 FB states
    - 8-edges
        - midges 16 * 14 * 12 * 10 * 8 * 6 * 4 = 5,160,960
        - wings 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 = 10,461,394,944,000
       10461394944000 * 5160960 = 53990840850186240000
        NOT FEASIBVLE



This would be reduce to 333 in ~79 moves
'''

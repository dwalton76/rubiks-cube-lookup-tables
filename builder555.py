#!/usr/bin/env python3

from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)


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
    """
    Should be:

    1 steps has 19 entries (0 percent, 0.00x previous step)
    2 steps has 459 entries (0 percent, 24.16x previous step)
    3 steps has 10,818 entries (0 percent, 23.57x previous step)
    4 steps has 255,957 entries (4 percent, 23.66x previous step)
    5 steps has 6,089,454 entries (95 percent, 23.79x previous step)
    """

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


class Build555ULFRBDTCenterSolveTake(BFS):

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
            'lookup-table-5x5x5-step100-stage-first-four-edges.txt',
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


class Build555ULFRBDCenterSolveUnstagedEdgesStageSecondFour(BFS):
    """
    Solve the L4E edges in the x-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-centers-solve-unstaged',

            ("Rw", "Rw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "L", "L'",
             "F", "F'",
             "R", "R'",
             "B", "B'"),

            '5x5x5',
            'lookup-table-5x5x5-step101-ULFRBD-centers-solve-unstaged.txt',
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
            'lookup-table-5x5x5-step101-stage-second-four-edges.txt',
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
    Solve the L4E edges in the x-plane
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
            'lookup-table-5x5x5-step500-ULFRBD-centers-solve-unstaged.txt',
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
            'lookup-table-5x5x5-step500-edges-last-four-x-plane.txt',
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


# =============================================================================
# dwalton
# =============================================================================
class Build555Step41(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step41',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),
            '5x5x5',
            'lookup-table-5x5x5-step41.txt',
            True, # store_as_hex
            (("""
            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .

 . x x x .  . x x x .  . x x x .  . x x x .
 L . . . L  L . . . L  L . . . L  L . . . L
 L . . . L  L . . . L  L . . . L  L . . . L
 L . . . L  L . . . L  L . . . L  L . . . L
 . x x x .  . x x x .  . x x x .  . x x x .

            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .""", "ascii"),)
        )


class StartingStates555Step42(BFS):
    """
    There are 36 vertical bar patterns that can be made from the LFRB centers
    6 patterns for LR * 6 patterns for FB
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step42',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",

             "Uw2", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step42.txt',
            False, # store_as_hex
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
            . . . . .""", "ascii"),),
        )


class Build555Step42(BFS):
    """
    There will be 70^4 or 24,010,000 entries
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step42',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),
            '5x5x5',
            'lookup-table-5x5x5-step42.txt',
            True, # store_as_hex
            (('...............................LLL..LLL..LLL............FFF..FFF..FFF............xxx..xxx..xxx............xxx..xxx..xxx...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFx..FFx..FFx............xxx..xxx..xxx............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFx..FFx..FFx............xxx..xxx..xxx............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............xFF..xFF..xFF............xxx..xxx..xxx............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............xFF..xFF..xFF............xxx..xxx..xxx............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............xFx..xFx..xFx............xxx..xxx..xxx............FxF..FxF..FxF...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............FFF..FFF..FFF............Lxx..Lxx..Lxx............xxx..xxx..xxx...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............FFF..FFF..FFF............xxL..xxL..xxL............xxx..xxx..xxx...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............FFx..FFx..FFx............Lxx..Lxx..Lxx............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............FFx..FFx..FFx............Lxx..Lxx..Lxx............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............FFx..FFx..FFx............xxL..xxL..xxL............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............FFx..FFx..FFx............xxL..xxL..xxL............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............xFF..xFF..xFF............Lxx..Lxx..Lxx............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............xFF..xFF..xFF............Lxx..Lxx..Lxx............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............xFF..xFF..xFF............xxL..xxL..xxL............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............xFF..xFF..xFF............xxL..xxL..xxL............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............xFx..xFx..xFx............Lxx..Lxx..Lxx............FxF..FxF..FxF...............................', 'ULFRBD'),
             ('...............................LLx..LLx..LLx............xFx..xFx..xFx............xxL..xxL..xxL............FxF..FxF..FxF...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............FFF..FFF..FFF............Lxx..Lxx..Lxx............xxx..xxx..xxx...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............FFF..FFF..FFF............xxL..xxL..xxL............xxx..xxx..xxx...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............FFx..FFx..FFx............Lxx..Lxx..Lxx............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............FFx..FFx..FFx............Lxx..Lxx..Lxx............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............FFx..FFx..FFx............xxL..xxL..xxL............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............FFx..FFx..FFx............xxL..xxL..xxL............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............xFF..xFF..xFF............Lxx..Lxx..Lxx............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............xFF..xFF..xFF............Lxx..Lxx..Lxx............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............xFF..xFF..xFF............xxL..xxL..xxL............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............xFF..xFF..xFF............xxL..xxL..xxL............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............xFx..xFx..xFx............Lxx..Lxx..Lxx............FxF..FxF..FxF...............................', 'ULFRBD'),
             ('...............................xLL..xLL..xLL............xFx..xFx..xFx............xxL..xxL..xxL............FxF..FxF..FxF...............................', 'ULFRBD'),
             ('...............................xLx..xLx..xLx............FFF..FFF..FFF............LxL..LxL..LxL............xxx..xxx..xxx...............................', 'ULFRBD'),
             ('...............................xLx..xLx..xLx............FFx..FFx..FFx............LxL..LxL..LxL............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................xLx..xLx..xLx............FFx..FFx..FFx............LxL..LxL..LxL............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................xLx..xLx..xLx............xFF..xFF..xFF............LxL..LxL..LxL............Fxx..Fxx..Fxx...............................', 'ULFRBD'),
             ('...............................xLx..xLx..xLx............xFF..xFF..xFF............LxL..LxL..LxL............xxF..xxF..xxF...............................', 'ULFRBD'),
             ('...............................xLx..xLx..xLx............xFx..xFx..xFx............LxL..LxL..LxL............FxF..FxF..FxF...............................', 'ULFRBD'))
        )


class StartingStates555Step40(BFS):
    """
    There are 36 vertical bar patterns that can be made from the LFRB centers
    6 patterns for LR * 6 patterns for FB
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step40',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",

             "Uw2", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'"),
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step40.txt',
            False, # store_as_hex
            (("""
            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .

 . x x x .  . x x x .  . x x x .  . x x x .
 L L L L L  L F F F L  L x x x L  L x x x L
 L L L L L  L F F F L  L x x x L  L x x x L
 L L L L L  L F F F L  L x x x L  L x x x L
 . x x x .  . x x x .  . x x x .  . x x x .

            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .""", "ascii"),),
        )


class Build555Step40(BFS):
    """
    There are 36 vertical bar patterns that can be made from the LFRB centers
    6 patterns for LR * 6 patterns for FB
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step40',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'"),
            '5x5x5',
            'lookup-table-5x5x5-step40.txt',
            True, # store_as_hex
            (('.xxx.x...xx...xx...x.xxx..xxx.LLLLLLLLLLLLLLL.xxx..xxx.LFFFLLFFFLLFFFL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLLLLLLLLLLLLL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLLLLLLLLLLLLL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLLLLLLLLLLLLL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLLLLLLLLLLLLL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLLLLLLLLLLLLL.xxx..xxx.LxFxLLxFxLLxFxL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.LFxFLLFxFLLFxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LFFFLLFFFLLFFFL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LFFFLLFFFLLFFFL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LxFxLLxFxLLxFxL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LFxFLLFxFLLFxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LLLxLLLLxLLLLxL.xxx..xxx.LxFxLLxFxLLxFxL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LFxFLLFxFLLFxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LFFFLLFFFLLFFFL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LFFFLLFFFLLFFFL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LxFxLLxFxLLxFxL.xxx..xxx.LLxxLLLxxLLLxxL.xxx..xxx.LFxFLLFxFLLFxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLLLLxLLLLxLLL.xxx..xxx.LxFxLLxFxLLxFxL.xxx..xxx.LxxLLLxxLLLxxLL.xxx..xxx.LFxFLLFxFLLFxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLxLLxLxLLxLxL.xxx..xxx.LFFFLLFFFLLFFFL.xxx..xxx.LLxLLLLxLLLLxLL.xxx..xxx.LxxxLLxxxLLxxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLxLLxLxLLxLxL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LLxLLLLxLLLLxLL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLxLLxLxLLxLxL.xxx..xxx.LFFxLLFFxLLFFxL.xxx..xxx.LLxLLLLxLLLLxLL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLxLLxLxLLxLxL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LLxLLLLxLLLLxLL.xxx..xxx.LFxxLLFxxLLFxxL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLxLLxLxLLxLxL.xxx..xxx.LxFFLLxFFLLxFFL.xxx..xxx.LLxLLLLxLLLLxLL.xxx..xxx.LxxFLLxxFLLxxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'),
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLxLLxLxLLxLxL.xxx..xxx.LxFxLLxFxLLxFxL.xxx..xxx.LLxLLLLxLLLLxLL.xxx..xxx.LFxFLLFxFLLFxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD'))
        )



class Build555Step51(BFS):
    """
    16 wings and 8 midges
    8!/(4!*4!) midges
    16!/(8!*8!) wings
    (8!/(4!*4!))  * (16!/(8!*8!)) = 900,900

    I can only get to 343,000 of them

    lookup-table-5x5x5-step51.txt
    =============================
    1 steps has 3 entries (0 percent, 0.00x previous step)
    2 steps has 17 entries (0 percent, 5.67x previous step)
    3 steps has 82 entries (0 percent, 4.82x previous step)
    4 steps has 448 entries (0 percent, 5.46x previous step)
    5 steps has 2,390 entries (0 percent, 5.33x previous step)
    6 steps has 11,546 entries (3 percent, 4.83x previous step)
    7 steps has 41,154 entries (11 percent, 3.56x previous step)
    8 steps has 103,436 entries (30 percent, 2.51x previous step)
    9 steps has 135,516 entries (39 percent, 1.31x previous step)
    10 steps has 45,604 entries (13 percent, 0.34x previous step)
    11 steps has 2,804 entries (0 percent, 0.06x previous step)

    Total: 343,000 entries
    Average: 8.47 moves

    This should be ok as we will have 70 different combinations of edges
    to choose from to consider as the "U" edges for this table
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step51',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",

            # Do not undo the L4E group in the x-plane
            "L", "L'",
            "R", "R'",
            "F", "F'",
            "B", "B'",

            # Do not break up the vertical bars in LFRB
            "Uw2", "Dw2",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step51.txt',
            True, # store_as_hex
            (("""
            . U U U .
            x . . . x
            x . . . x
            x . . . x
            . U U U .

 . x x x .  . U U U .  . x x x .  . U U U .
 x . . . x  x . . . x  x . . . x  x . . . x
 x . . . x  x . . . x  x . . . x  x . . . x
 x . . . x  x . . . x  x . . . x  x . . . x
 . x x x .  . U U U .  . x x x .  . U U U .

            . U U U .
            x . . . x
            x . . . x
            x . . . x
            . U U U .""", "ascii"),)
        )


class StartingStates555Step52(BFS):
    """
    There are 36 vertical bar patterns that can be made from the UFBD centers
    6 patterns for UD * 6 patterns for FB
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step52',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",

            # Do not undo the L4E group in the x-plane
            "L", "L'",
            "R", "R'",
            "F", "F'",
            "B", "B'",

            "U", "U'",
            "D", "D'",
            "Fw2", "Bw2",
            "Uw2", "Dw2",
            ),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step52.txt',
            False, # store_as_hex
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
            . . . . .""", "ascii"),),
        )


class Build555Step52(BFS):
    """
    There are 36 vertical bar patterns that can be made from the UFBD centers
    6 patterns for UD * 6 patterns for FB
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step52',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",

            # Do not undo the L4E group in the x-plane
            "L", "L'",
            "R", "R'",
            "F", "F'",
            "B", "B'",

            # Do not break up the vertical bars in LFRB
            "Uw2", "Dw2",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step52.txt',
            True, # store_as_hex
            (('......UUU..UUU..UUU.....................................FFF..FFF..FFF.....................................xxx..xxx..xxx............xxx..xxx..xxx......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................FFx..FFx..FFx.....................................Fxx..Fxx..Fxx............xxx..xxx..xxx......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................FFx..FFx..FFx.....................................xxF..xxF..xxF............xxx..xxx..xxx......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................xFF..xFF..xFF.....................................Fxx..Fxx..Fxx............xxx..xxx..xxx......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................xFF..xFF..xFF.....................................xxF..xxF..xxF............xxx..xxx..xxx......', 'ULFRBD'),
             ('......UUU..UUU..UUU.....................................xFx..xFx..xFx.....................................FxF..FxF..FxF............xxx..xxx..xxx......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................FFF..FFF..FFF.....................................xxx..xxx..xxx............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................FFF..FFF..FFF.....................................xxx..xxx..xxx............xxU..xxU..xxU......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................FFx..FFx..FFx.....................................Fxx..Fxx..Fxx............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................FFx..FFx..FFx.....................................Fxx..Fxx..Fxx............xxU..xxU..xxU......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................FFx..FFx..FFx.....................................xxF..xxF..xxF............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................FFx..FFx..FFx.....................................xxF..xxF..xxF............xxU..xxU..xxU......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................xFF..xFF..xFF.....................................Fxx..Fxx..Fxx............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................xFF..xFF..xFF.....................................Fxx..Fxx..Fxx............xxU..xxU..xxU......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................xFF..xFF..xFF.....................................xxF..xxF..xxF............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................xFF..xFF..xFF.....................................xxF..xxF..xxF............xxU..xxU..xxU......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................xFx..xFx..xFx.....................................FxF..FxF..FxF............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......UUx..UUx..UUx.....................................xFx..xFx..xFx.....................................FxF..FxF..FxF............xxU..xxU..xxU......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................FFF..FFF..FFF.....................................xxx..xxx..xxx............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................FFF..FFF..FFF.....................................xxx..xxx..xxx............xxU..xxU..xxU......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................FFx..FFx..FFx.....................................Fxx..Fxx..Fxx............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................FFx..FFx..FFx.....................................Fxx..Fxx..Fxx............xxU..xxU..xxU......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................FFx..FFx..FFx.....................................xxF..xxF..xxF............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................FFx..FFx..FFx.....................................xxF..xxF..xxF............xxU..xxU..xxU......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................xFF..xFF..xFF.....................................Fxx..Fxx..Fxx............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................xFF..xFF..xFF.....................................Fxx..Fxx..Fxx............xxU..xxU..xxU......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................xFF..xFF..xFF.....................................xxF..xxF..xxF............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................xFF..xFF..xFF.....................................xxF..xxF..xxF............xxU..xxU..xxU......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................xFx..xFx..xFx.....................................FxF..FxF..FxF............Uxx..Uxx..Uxx......', 'ULFRBD'),
             ('......xUU..xUU..xUU.....................................xFx..xFx..xFx.....................................FxF..FxF..FxF............xxU..xxU..xxU......', 'ULFRBD'),
             ('......xUx..xUx..xUx.....................................FFF..FFF..FFF.....................................xxx..xxx..xxx............UxU..UxU..UxU......', 'ULFRBD'),
             ('......xUx..xUx..xUx.....................................FFx..FFx..FFx.....................................Fxx..Fxx..Fxx............UxU..UxU..UxU......', 'ULFRBD'),
             ('......xUx..xUx..xUx.....................................FFx..FFx..FFx.....................................xxF..xxF..xxF............UxU..UxU..UxU......', 'ULFRBD'),
             ('......xUx..xUx..xUx.....................................xFF..xFF..xFF.....................................Fxx..Fxx..Fxx............UxU..UxU..UxU......', 'ULFRBD'),
             ('......xUx..xUx..xUx.....................................xFF..xFF..xFF.....................................xxF..xxF..xxF............UxU..UxU..UxU......', 'ULFRBD'),
             ('......xUx..xUx..xUx.....................................xFx..xFx..xFx.....................................FxF..FxF..FxF............UxU..UxU..UxU......', 'ULFRBD'))
        )


class StartingStates555Step50(BFS):
    """
    There are 36 vertical bar patterns that can be made from the UFBD centers
    6 patterns for UD * 6 patterns for FB
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step50',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",

            # Do not undo the L4E group in the x-plane
            "L", "L'",
            "R", "R'",
            "F", "F'",
            "B", "B'",

            "U", "U'",
            "D", "D'",
            "Fw2", "Bw2",
            "Uw2", "Dw2",
            ),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step50.txt',
            False, # store_as_hex
            (("""
            . U U U .
            x U U U x
            x U U U x
            x U U U x
            . U U U .

 . x x x .  . U U U .  . x x x .  . U U U .
 x . . . x  x F F F x  x . . . x  x x x x x
 x . . . x  x F F F x  x . . . x  x x x x x
 x . . . x  x F F F x  x . . . x  x x x x x
 . x x x .  . U U U .  . x x x .  . U U U .

            . U U U .
            x x x x x
            x x x x x
            x x x x x
            . U U U .""", "ascii"),),
        )


class Build555Step50(BFS):
    """
    There are 36 vertical bar patterns that can be made from the UFBD centers
    6 patterns for UD * 6 patterns for FB
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step50',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",

            # Do not undo the L4E group in the x-plane
            "L", "L'",
            "R", "R'",
            "F", "F'",
            "B", "B'",

            # Do not break up the vertical bars in LFRB
            "Uw2", "Dw2",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step50.txt',
            True, # store_as_hex
            (('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxxxxxxxxxxxxx.UUU..UUU.xxxxxxxxxxxxxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xxxxxxxxxxxxxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xxxxxxxxxxxxxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xxxxxxxxxxxxxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xxxxxxxxxxxxxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFxxxxFxxxxFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxFxxFxFxxFxFx.UUU..UUU.xxxxxxxxxxxxxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxxxxxxxxxxxxx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxxxxxxxxxxxxx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFxxxxFxxxxFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxFxxFxFxxFxFx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xUUxxxUUxxxUUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFxxxxFxxxxFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxFxxFxFxxFxFx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxxxxxxxxxxxxx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxxxxxxxxxxxxx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFxxxxFxxxxFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxFxxFxFxxFxFx.UUU..UUU.xUxxxxUxxxxUxxx.UUU.', 'ULFRBD'),
             ('.UUU.xxUUxxxUUxxxUUx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFxxxxFxxxxFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxFxxFxFxxFxFx.UUU..UUU.xxxUxxxxUxxxxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUxxxxUxxxxUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxxxxxxxxxxxxx.UUU..UUU.xUxUxxUxUxxUxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUxxxxUxxxxUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xUxUxxUxUxxUxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUxxxxUxxxxUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFFxxxFFxxxFFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xUxUxxUxUxxUxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUxxxxUxxxxUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxxxxFxxxxFxxx.UUU..UUU.xUxUxxUxUxxUxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUxxxxUxxxxUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFFxxxFFxxxFFx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxxFxxxxFxxxxFx.UUU..UUU.xUxUxxUxUxxUxUx.UUU.', 'ULFRBD'),
             ('.UUU.xxUxxxxUxxxxUxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xxFxxxxFxxxxFxx.UUU..xxx.x...xx...xx...x.xxx..UUU.xFxFxxFxFxxFxFx.UUU..UUU.xUxUxxUxUxxUxUx.UUU.', 'ULFRBD'))
        )


class StartingStates555Step401(BFS):
    """
    Pair 2-edges anywhere
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step401',

            ("Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "Lw", "Lw'", "Lw2",
             "Rw", "Rw'", "Rw2",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2",
            ),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step401.txt',
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
            use_edges_pattern=True
        )


class Build555Step401(BFS):
    """
    Pair 2-edges anywhere
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step401',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step401.txt',
            False, # store_as_hex
            (('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...L-...L-...L.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...L-...L-...L.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.L...-L...-L...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.FFF..---.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.F...-F...-F...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.FFF..LLL.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..LLL.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.F...-F...-F...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.L...-L...-L...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.L...RL...RL...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..LLL.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...L-...L-...L.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...LF...LF...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...FF...FF...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...LF...LF...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...FF...FF...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.FFF..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.LLL..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...L-...L-...L.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.L...-L...-L...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.FFF..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.RRR..LLL.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...FF...FF...F.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...LF...LF...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.FFF..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...FL...FL...F.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..LLL.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..LLL.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..LLL.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD')),
            use_edges_pattern=True
        )


class StartingStates555Step400(BFS):
    """
    Pair 3-edges anywhere
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step400',

            ("Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "Lw", "Lw'", "Lw2",
             "Rw", "Rw'", "Rw2",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2",
            ),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step400.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F . . . F  R . . . R  B . . . -
 - . . . L  F . . . F  R . . . R  B . . . -
 - . . . L  F . . . F  R . . . R  B . . . -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True
        )


class Build555Step400(BFS):
    """
    Pair 3-edges anywhere
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step400',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step400.txt',
            False, # store_as_hex
            (('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.FFF..---.-...R-...R-...R.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.L...-L...-L...-.RRR..---.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.L...-L...-L...-.FFF..---.-...B-...B-...B.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.BBB..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.RRR..---.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.BBB..---.F...-F...-F...-.LLL..---.-...R-...R-...R.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.B...-B...-B...-.FFF..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...R-...R-...R.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.BBB..LLL.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.BBB..LLL.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.LLL..RRR.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...-L...-L...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.RRR..---.L...-L...-L...-.---..RRR.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.LLL..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.LLL..---.B...-B...-B...-.---..RRR.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.BBB..FFF.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.RRR..FFF.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.BBB..FFF.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.RRR..FFF.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...B-...B-...B.---..---.R...-R...-R...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..FFF.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.FFF..---.-...L-...L-...L.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.LLL..---.-...--...--...-.RRR..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.FFF..LLL.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.FFF..---.-...--...--...-.---..RRR.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...FR...FR...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...RR...RR...R.---..---.F...-F...-F...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.FFF..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...FR...FR...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...BL...BL...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..---.-...--...--...-.LLL..---.-...R-...R-...R.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.L...-L...-L...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.BBB..---.L...-L...-L...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.B...-B...-B...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.LLL..---.B...-B...-B...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.BBB..---.R...-R...-R...-.LLL..---.-...--...--...-.---..RRR.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.BBB..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...RR...RR...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.L...-L...-L...-.RRR..---.-...--...--...-.---..BBB.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.BBB..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.RRR..---.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.RRR..---.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...BF...BF...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...BF...BF...B.FFF..---.R...-R...-R...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.RRR..---.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.RRR..---.B...-B...-B...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.RRR..---.-...--...--...-.---..RRR.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...BF...BF...B.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...RF...RF...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.BBB..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...RF...RF...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...FF...FF...F.RRR..---.L...-L...-L...-.---..---.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.F...-F...-F...-.BBB..---.-...--...--...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.B...-B...-B...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.F...-F...-F...-.---..---.-...--...--...-.BBB..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.F...-F...-F...-.RRR..---.-...--...--...-.---..FFF.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.F...FF...FF...F.---..---.L...-L...-L...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.R...LR...LR...L.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.R...LR...LR...L.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.R...FR...FR...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.FFF..---.R...-R...-R...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.L...-L...-L...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.RRR..LLL.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..LLL.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.R...-R...-R...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.R...-R...-R...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...R-...R-...R.LLL..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.LLL..---.R...BR...BR...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.L...-L...-L...-.---..---.R...BR...BR...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.LLL..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.B...-B...-B...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.BBB..LLL.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.---..LLL.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.L...-L...-L...-.---..BBB.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..LLL.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.F...RF...RF...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR..---.F...RF...RF...R.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.F...FF...FF...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.RRR..---.F...BF...BF...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.BBB..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.BBB..---.F...-F...-F...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.B...-B...-B...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.BBB..RRR.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.F...BF...BF...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...B-...B-...B.---..---.R...-R...-R...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.BBB..FFF.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...--...--...-.---..FFF.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...--...--...-.---..BBB.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...B-...B-...B.---..---.R...-R...-R...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...B-...B-...B.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.BBB..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..---.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...BR...BR...B.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.B...-B...-B...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.B...RB...RB...R.---..---.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.BBB..---.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.RRR..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.B...-B...-B...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.L...-L...-L...-.---..---.B...RB...RB...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.B...-B...-B...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.F...FF...FF...F.---..---.L...-L...-L...-.---..---.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...L-...L-...L.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF..---.-...F-...F-...F.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...F-...F-...F.FFF..---.R...-R...-R...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.RRR..LLL.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..LLL.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...F-...F-...F.---..---.R...-R...-R...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.R...FR...FR...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...LR...LR...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...LR...LR...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...LR...LR...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...LR...LR...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...RR...RR...R.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...RR...RR...R.FFF..---.F...-F...-F...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.L...-L...-L...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...FR...FR...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.F...-F...-F...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..LLL.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...FL...FL...F.---..---.R...RR...RR...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.RRR..---.-...F-...F-...F.---..---.L...-L...-L...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...LR...LR...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.BBB..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.BBB..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR..---.-...R-...R-...R.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.BBB..---.F...-F...-F...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.RRR..---.B...-B...-B...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..---.-...R-...R-...R.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.BBB..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.BBB..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...B-...B-...B.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...BF...BF...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...BF...BF...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...BF...BF...B.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...BF...BF...B.RRR..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.BBB..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.BBB..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...FB...FB...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...RB...RB...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.FFF..---.B...-B...-B...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.RRR..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.B...-B...-B...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.F...BF...BF...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.BBB..---.-...--...--...-.---..---.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...BF...BF...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..LLL.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.LLL..---.-...R-...R-...R.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.FFF..---.-...F-...F-...F.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.FFF..---.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.R...RR...RR...R.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.L...RL...RL...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...RF...RF...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.LLL..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...R-...R-...R.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...R-...R-...R.---..LLL.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...RL...RL...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...R-...R-...R.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...R-...R-...R.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...RR...RR...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...RF...RF...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.FFF..FFF.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...F-...F-...F.---..---.L...FL...FL...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...R-...R-...R.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.F...RF...RF...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...R-...R-...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.L...FL...FL...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.FFF..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...RF...RF...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...-B...-B...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...FB...FB...F.FFF..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.F...RF...RF...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.---..---.F...RF...RF...R.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.B...LB...LB...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...L-...L-...L.FFF..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...LB...LB...L.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...RB...RB...R.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...LB...LB...L.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...L-...L-...L.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...LB...LB...L.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...L-...L-...L.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.B...RB...RB...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...L-...L-...L.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..---.-...L-...L-...L.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...L-...L-...L.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...LB...LB...L.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...-F...-F...-.LLL..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...BF...BF...B.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...FF...FF...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...FF...FF...F.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.B...RB...RB...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...FF...FF...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...LF...LF...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.F...LF...LF...L.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.RRR..---.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.RRR..---.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...FR...FR...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...FR...FR...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...FB...FB...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.B...FB...FB...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...F-...F-...F.---..RRR.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...FB...FB...F.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.BBB..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.RRR..BBB.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...F-...F-...F.---..BBB.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...B-...B-...B.---..---.R...FR...FR...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.B...FB...FB...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...F-...F-...F.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..---.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..---.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.B...RB...RB...R.---..---.F...FF...FF...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...F-...F-...F.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.BBB..---.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.RRR..---.B...-B...-B...-.---..---.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.BBB..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.B...-B...-B...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.B...FB...FB...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...BL...BL...B.RRR..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...RL...RL...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...F-...F-...F.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...RL...RL...R.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.L...RL...RL...R.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...B-...B-...B.FFF..---.-...R-...R-...R.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...B-...B-...B.LLL..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...BL...BL...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...B-...B-...B.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...B-...B-...B.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.L...BL...BL...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...B-...B-...B.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...BR...BR...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...B-...B-...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...B-...B-...B.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...-R...-R...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...B-...B-...B.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...FR...FR...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...B-...B-...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...LR...LR...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...LR...LR...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...B-...B-...B.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...LR...LR...L.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...BR...BR...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...LR...LR...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...LR...LR...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.---..---.R...LR...LR...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...R-...R-...R.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...L-...L-...L.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF..---.-...F-...F-...F.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.FFF..---.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.FFF..---.R...-R...-R...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.RRR..LLL.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..LLL.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...F-...F-...F.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...RF...RF...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.L...-L...-L...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.L...RL...RL...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.L...FL...FL...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..LLL.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.LLL..RRR.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.F...-F...-F...-.LLL.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.FFF..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...F-...F-...F.LLL..RRR.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...L-...L-...L.---..RRR.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...L-...L-...L.---..RRR.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.-...L-...L-...L.RRR..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...L-...L-...L.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...LR...LR...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.F...LF...LF...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...-F...-F...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...FF...FF...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.F...LF...LF...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.F...FF...FF...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.---..RRR.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...-L...-L...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.BBB..---.L...FL...FL...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...F-...F-...F.---..---.R...RR...RR...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.BBB..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...--...--...-.FFF..LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...B-...B-...B.---..LLL.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...L-...L-...L.---..RRR.F...-F...-F...-.BBB..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...L-...L-...L.---..RRR.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.-...L-...L-...L.BBB..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.B...-B...-B...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.R...-R...-R...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.FFF..---.R...LR...LR...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.RRR..---.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...B-...B-...B.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.FFF..BBB.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...--...--...-.---..BBB.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...B-...B-...B.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...FB...FB...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.RRR..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.BBB..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.BBB..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.BBB..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.BBB..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.BBB..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.R...BR...BR...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.B...-B...-B...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.B...-B...-B...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.B...RB...RB...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...--...--...-.RRR..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...B-...B-...B.---..FFF.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...B-...B-...B.FFF..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...BR...BR...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...RR...RR...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...F-...F-...F.RRR..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...R-...R-...R.---..FFF.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...R-...R-...R.---..FFF.B...RB...RB...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...R-...R-...R.FFF..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.-...R-...R-...R.RRR..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...-B...-B...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...-B...-B...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...-B...-B...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.B...FB...FB...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...RB...RB...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.F...-F...-F...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.F...-F...-F...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.F...RF...RF...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...B-...B-...B.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...B-...B-...B.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...BR...BR...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...B-...B-...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...-R...-R...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.LLL..---.R...FR...FR...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.LLL..---.B...-B...-B...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.LLL..---.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.LLL..BBB.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.LLL..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.F...BF...BF...B.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.LLL..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...--...--...-.LLL..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...L-...L-...L.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...L-...L-...L.---..BBB.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...L-...L-...L.---..BBB.F...-F...-F...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...L-...L-...L.---..BBB.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.-...L-...L-...L.---..BBB.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.B...-B...-B...-.LLL..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.L...-L...-L...-.---..BBB.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.L...RL...RL...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...--...--...-.RRR..---.R...-R...-R...-.LLL..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...L-...L-...L.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF..---.-...F-...F-...F.LLL.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.FFF..---.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.FFF..---.R...-R...-R...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.RRR..LLL.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.RRR..---.-...--...--...-.---..LLL.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.LLL.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..RRR.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..RRR.L...-L...-L...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...RF...RF...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..RRR.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..RRR.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.L...-L...-L...-.RRR.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..LLL.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.F...-F...-F...-.LLL.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.F...LF...LF...L.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.FFF..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...R-...R-...R.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...L-...L-...L.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.L...RL...RL...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...RF...RF...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...L-...L-...L.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...-F...-F...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...FF...FF...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.F...LF...LF...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...FR...FR...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...F-...F-...F.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..LLL.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..LLL.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.---..RRR.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.FFF..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...--...--...-.LLL..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.F...-F...-F...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.FFF..---.L...-L...-L...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...--...--...-.RRR..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.LLL..---.F...-F...-F...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...B-...B-...B.RRR..---.L...-L...-L...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...L-...L-...L.RRR.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.FFF..LLL.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.BBB..LLL.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.---..---.-...F-...F-...F.---..LLL.R...RR...RR...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.R...LR...LR...L.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.BBB..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..RRR.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.---..---.R...LR...LR...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.BBB..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...F-...F-...F.RRR..---.-...--...--...-.---..BBB.-...F-...F-...F.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..LLL.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...F-...F-...F.RRR..---.-...L-...L-...L.---..BBB.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.BBB..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.BBB..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.RRR..---.-...--...--...-.---..BBB.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..FFF.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...RR...RR...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...FB...FB...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..FFF.B...-B...-B...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..FFF.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.BBB..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.BBB..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.BBB..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.BBB..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.R...BR...BR...B.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.B...-B...-B...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.BBB.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.B...RB...RB...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...-R...-R...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...F-...F-...F.RRR..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.---..---.F...RF...RF...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.-...R-...R-...R.BBB..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...R-...R-...R.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...R-...R-...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...-B...-B...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...FB...FB...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.B...RB...RB...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...RB...RB...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...B-...B-...B.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...B-...B-...B.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...FR...FR...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...B-...B-...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...B-...B-...B.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...--...--...-.---..RRR.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...--...--...-.---..RRR.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.FFF..---.-...--...--...-.---..RRR.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.B...-B...-B...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...L-...L-...L.RRR..---.R...-R...-R...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...R-...R-...R.---..---.F...-F...-F...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.LLL..---.B...-B...-B...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.LLL..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.---..---.-...B-...B-...B.LLL..FFF.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.---..---.-...F-...F-...F.---..BBB.R...FR...FR...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.---..---.-...L-...L-...L.---..FFF.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.LLL..---.-...--...--...-.---..BBB.-...--...--...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..BBB.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..BBB.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..BBB.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.L...-L...-L...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.---..---.R...-R...-R...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.BBB..---.-...--...--...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.FFF..---.-...--...--...-.---..LLL.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.FFF..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.FFF..---.L...-L...-L...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.-...R-...R-...R.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..BBB.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.LLL..---.-...--...--...-.---..FFF.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.LLL..---.-...--...--...-.BBB..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.LLL..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.-...R-...R-...R.RRR..---.-...--...--...-.LLL..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...L-...L-...L.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.R...-R...-R...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..LLL.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.LLL..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.FFF..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...F-...F-...F.FFF..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.F...-F...-F...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.F...-F...-F...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.F...FF...FF...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.F...LF...LF...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.L...-L...-L...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.---..RRR.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.FFF..RRR.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.FFF..RRR.-...--...--...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.FFF..RRR.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.FFF..RRR.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.FFF..RRR.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.LLL..RRR.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.RRR..RRR.-...--...--...-.---..FFF.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...-B...-B...-.RRR..RRR.-...--...--...-.LLL..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...FB...FB...F.---..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...FB...FB...F.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...FB...FB...F.---..RRR.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...FB...FB...F.---..RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...LB...LB...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.B...RB...RB...R.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...B-...B-...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...B-...B-...B.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...R-...R-...R.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.-...R-...R-...R.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...RF...RF...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.B...-B...-B...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...B-...B-...B.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...B-...B-...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..LLL.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.---..RRR.F...-F...-F...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...--...--...-.---..RRR.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..LLL.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.BBB..RRR.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.FFF..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.RRR..LLL.-...--...--...-.---..BBB.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.RRR..LLL.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...-F...-F...-.RRR..LLL.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.RRR..LLL.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...-F...-F...-.RRR..RRR.-...L-...L-...L.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..LLL.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.FFF..LLL.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...BF...BF...B.RRR..LLL.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...FF...FF...F.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.F...LF...LF...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...RF...RF...R.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...RF...RF...R.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...RF...RF...R.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...RF...RF...R.FFF..LLL.-...--...--...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.F...RF...RF...R.RRR..LLL.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...B-...B-...B.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.RRR..---.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...B-...B-...B.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.FFF..BBB.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..---.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...--...--...-.---..BBB.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.FFF..---.B...-B...-B...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.RRR..---.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.BBB..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.R...BR...BR...B.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.B...-B...-B...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.F...-F...-F...-.BBB.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.B...RB...RB...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.B...-B...-B...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...--...--...-.RRR..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.---..---.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...R-...R-...R.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.-...R-...R-...R.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...-B...-B...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.B...FB...FB...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...RB...RB...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...B-...B-...B.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...B-...B-...B.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...BR...BR...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...B-...B-...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.---..FFF.R...RR...RR...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.---..RRR.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.BBB..FFF.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..BBB.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..BBB.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...-L...-L...-.RRR..FFF.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...BL...BL...B.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...FL...FL...F.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..BBB.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.FFF..FFF.-...--...--...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.L...RL...RL...R.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...--...--...-.LLL..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.F...LF...LF...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..BBB.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.LLL..---.B...-B...-B...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.B...-B...-B...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...FB...FB...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.---..FFF.R...-R...-R...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.BBB..FFF.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.FFF..BBB.-...--...--...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.FFF..BBB.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.LLL..BBB.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.LLL..BBB.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.LLL..BBB.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.RRR..BBB.-...--...--...-.LLL..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...-R...-R...-.RRR..BBB.-...F-...F-...F.---..FFF.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...BR...BR...B.---..FFF.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.---.R...BR...BR...B.---..FFF.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...FR...FR...F.---..BBB.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...FR...FR...F.---..FFF.-...--...--...-.---..---.-...--...--...-.---..LLL.-...R-...R-...R.---..---.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.---.R...RR...RR...R.---..BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.FFF..---.-...L-...L-...L.RRR.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.RRR..---.-...L-...L-...L.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.FFF..---.-...F-...F-...F.LLL.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..RRR.L...-L...-L...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.LLL..RRR.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..RRR.F...-F...-F...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.RRR..LLL.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..RRR.-...--...--...-.---..RRR.-...L-...L-...L.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..RRR.-...--...--...-.---..LLL.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..RRR.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..RRR.-...--...--...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.FFF..FFF.-...--...--...-.LLL.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.FFF..---.R...-R...-R...-.---..RRR.-...--...--...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.FFF..RRR.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.L...-L...-L...-.RRR.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.LLL..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.R...LR...LR...L.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..LLL.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.L...-L...-L...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.FFF..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.F...-F...-F...-.LLL.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.F...LF...LF...L.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...F-...F-...F.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...L-...L-...L.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...L-...L-...L.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.L...RL...RL...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...L-...L-...L.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...R-...R-...R.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...-F...-F...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...FF...FF...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.F...LF...LF...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...F-...F-...F.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...FR...FR...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.F...FF...FF...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...F-...F-...F.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.---..---.L...FL...FL...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.FFF..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...--...--...-.LLL..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.FFF..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...--...--...-.LLL..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..RRR.-...--...--...-.---..LLL.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...--...--...-.---..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...--...--...-.---..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.L...-L...-L...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...F-...F-...F.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...R-...R-...R.---..---.L...-L...-L...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.-...R-...R-...R.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.FFF..LLL.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...-F...-F...-.LLL..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...FF...FF...F.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.F...LF...LF...L.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.L...-L...-L...-.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.BBB.R...-R...-R...-.---..FFF.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..LLL.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.BBB..LLL.F...-F...-F...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..LLL.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..LLL.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..LLL.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..LLL.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..LLL.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...B-...B-...B.LLL..---.R...-R...-R...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.BBB..RRR.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.-...L-...L-...L.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.B...-B...-B...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..LLL.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...L-...L-...L.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..LLL.B...RB...RB...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.L...-L...-L...-.BBB..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..LLL.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.---..---.R...LR...LR...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...--...--...-.RRR..---.-...L-...L-...L.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..LLL.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.FFF.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..LLL.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.FFF.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.LLL..RRR.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..LLL.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...B-...B-...B.---..LLL.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...R-...R-...R.---..LLL.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.-...R-...R-...R.---..---.-...--...--...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...L-...L-...L.---.', 'ULFRBD'),
             ('.FFF.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.F...-F...-F...-.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.FFF.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...-R...-R...-.---..BBB.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...-R...-R...-.---..BBB.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..LLL.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...-R...-R...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...-R...-R...-.LLL..BBB.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...BR...BR...B.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.FFF.R...LR...LR...L.---..BBB.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.BBB..---.-...R-...R-...R.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.RRR..---.-...R-...R-...R.BBB.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.BBB..---.-...F-...F-...F.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.R...-R...-R...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.R...-R...-R...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..FFF.R...-R...-R...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.RRR..FFF.R...-R...-R...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.FFF..FFF.B...-B...-B...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..FFF.B...-B...-B...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.BBB..RRR.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.BBB..FFF.-...--...--...-.---..RRR.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..FFF.-...--...--...-.---..RRR.-...B-...B-...B.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.BBB..FFF.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.BBB..FFF.-...--...--...-.---..FFF.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.BBB..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.RRR..FFF.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.BBB..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.RRR..---.B...-B...-B...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.R...-R...-R...-.FFF.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.R...RR...RR...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.R...FR...FR...F.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.BBB..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.BBB..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.BBB..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.BBB..---.R...-R...-R...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..BBB.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.BBB..---.F...-F...-F...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.BBB..FFF.-...--...--...-.---..---.F...RF...RF...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...--...--...-.RRR..---.-...R-...R-...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...B-...B-...B.---..---.R...-R...-R...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...B-...B-...B.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...B-...B-...B.FFF..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...B-...B-...B.RRR..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...RR...RR...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.B...-B...-B...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.BBB..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...R-...R-...R.---..---.F...RF...RF...R.---..---.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.-...R-...R-...R.BBB..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.B...-B...-B...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...R-...R-...R.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.B...-B...-B...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.R...RR...RR...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...RB...RB...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...R-...R-...R.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.F...-F...-F...-.BBB..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...B-...B-...B.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.R...-R...-R...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...BR...BR...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.R...-R...-R...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...B-...B-...B.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.R...-R...-R...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.R...-R...-R...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.---..---.R...FR...FR...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.FFF..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...--...--...-.RRR..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.-...F-...F-...F.---..RRR.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.BBB..---.F...-F...-F...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.FFF..---.R...-R...-R...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.RRR..---.-...--...--...-.---..BBB.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...--...--...-.RRR..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.FFF..RRR.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...--...--...-.---..---.-...--...--...-.RRR..RRR.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...--...--...-.FFF..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...B-...B-...B.---..---.F...-F...-F...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...F-...F-...F.---..---.-...--...--...-.---..---.-...R-...R-...R.---..RRR.B...-B...-B...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...R-...R-...R.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.BBB.', 'ULFRBD'),
             ('.LLL.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...R-...R-...R.---..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.-...R-...R-...R.---..---.-...--...--...-.---..---.-...B-...B-...B.---..FFF.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...--...--...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...-B...-B...-.FFF..RRR.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.B...RB...RB...R.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..FFF.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.BBB..---.-...--...--...-.RRR.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...-R...-R...-.BBB..FFF.-...--...--...-.---..RRR.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...BR...BR...B.---..FFF.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.LLL.R...RR...RR...R.---..BBB.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.LLL..---.-...F-...F-...F.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..BBB.F...-F...-F...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..BBB.-...--...--...-.LLL..RRR.-...--...--...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..---.-...F-...F-...F.---..BBB.L...-L...-L...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..BBB.-...--...--...-.RRR..FFF.-...--...--...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..BBB.-...--...--...-.---..FFF.-...F-...F-...F.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.LLL..---.-...R-...R-...R.---..BBB.F...-F...-F...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.RRR..BBB.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...--...--...-.LLL..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.---..---.R...FR...FR...F.---..BBB.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...F-...F-...F.LLL..---.R...-R...-R...-.---..BBB.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.---..---.F...RF...RF...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.---..---.-...L-...L-...L.FFF..---.F...-F...-F...-.---..BBB.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..---.-...F-...F-...F.---..BBB.L...-L...-L...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.RRR..---.F...-F...-F...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.---..---.F...FF...FF...F.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.---..---.-...R-...R-...R.---..BBB.F...-F...-F...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.FFF..---.-...--...--...-.---..BBB.-...--...--...-.---..RRR.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...--...--...-.RRR..---.-...--...--...-.---..BBB.-...--...--...-.---..FFF.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...--...--...-.LLL..---.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.L...-L...-L...-.FFF..---.-...--...--...-.---..BBB.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...F-...F-...F.---..BBB.L...-L...-L...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..BBB.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...R-...R-...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.RRR..---.-...--...--...-.---..BBB.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.---..---.F...FF...FF...F.---..---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.-...L-...L-...L.RRR..---.F...-F...-F...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.B...-B...-B...-.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..FFF.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.B...LB...LB...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...L-...L-...L.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.F...-F...-F...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..BBB.-...L-...L-...L.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.F...-F...-F...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.F...FF...FF...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..BBB.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...F-...F-...F.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...F-...F-...F.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..BBB.F...FF...FF...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...-L...-L...-.---..---.-...--...--...-.RRR..---.-...--...--...-.---..BBB.-...F-...F-...F.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...-L...-L...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...-L...-L...-.RRR..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...F-...F-...F.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.---..---.L...RL...RL...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..BBB.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.BBB..---.-...L-...L-...L.---..RRR.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..---.-...R-...R-...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.FFF..---.-...--...--...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.RRR..---.-...--...--...-.FFF.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..BBB.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.RRR..BBB.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..---.-...F-...F-...F.---..BBB.R...-R...-R...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..BBB.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.RRR..---.-...--...--...-.---..BBB.-...--...--...-.---..FFF.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...--...--...-.FFF..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.-...F-...F-...F.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.F...-F...-F...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.LLL..---.R...-R...-R...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...--...--...-.RRR..---.-...--...--...-.LLL..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...F-...F-...F.---..---.-...--...--...-.---..---.-...--...--...-.---..LLL.-...R-...R-...R.---..FFF.B...-B...-B...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...F-...F-...F.---..---.-...--...--...-.---..---.-...F-...F-...F.---..LLL.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...F-...F-...F.---..---.-...--...--...-.LLL..---.-...--...--...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...F-...F-...F.---..---.-...L-...L-...L.---..---.F...-F...-F...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...F-...F-...F.---..---.L...-L...-L...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..BBB.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...F-...F-...F.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...F-...F-...F.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.FFF..BBB.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...--...--...-.RRR..BBB.-...--...--...-.---..---.-...F-...F-...F.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.-...--...--...-.---..---.-...--...--...-.FFF..FFF.-...--...--...-.---..BBB.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.-...--...--...-.---..---.-...R-...R-...R.---..FFF.F...-F...-F...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.-...--...--...-.FFF..---.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.-...R-...R-...R.---..---.F...-F...-F...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.F...-F...-F...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...R-...R-...R.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.---..---.R...-R...-R...-.---..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...L-...L-...L.RRR..---.-...--...--...-.---..FFF.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.-...R-...R-...R.---..---.-...--...--...-.LLL..---.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.-...R-...R-...R.FFF..---.-...--...--...-.---..LLL.-...--...--...-.---..FFF.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.B...-B...-B...-.---..RRR.L...-L...-L...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...F-...F-...F.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...--...--...-.---..---.-...R-...R-...R.---..BBB.F...-F...-F...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.F...-F...-F...-.---..LLL.-...--...--...-.---..---.-...F-...F-...F.---..---.R...-R...-R...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.F...-F...-F...-.---..LLL.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.F...-F...-F...-.RRR..LLL.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.F...FF...FF...F.---..LLL.-...--...--...-.---..---.-...--...--...-.---..RRR.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..---.-...--...--...-.FFF..BBB.-...--...--...-.---..---.-...R-...R-...R.---.', 'ULFRBD'),
             ('.RRR.L...-L...-L...-.---..FFF.-...--...--...-.---..---.-...--...--...-.FFF..---.-...--...--...-.---..BBB.-...--...--...-.---..RRR.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.L...-L...-L...-.---..FFF.-...--...--...-.FFF..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.R...-R...-R...-.---.', 'ULFRBD'),
             ('.RRR.L...-L...-L...-.---..FFF.-...F-...F-...F.---..---.R...-R...-R...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.L...-L...-L...-.---..FFF.-...R-...R-...R.---..---.F...-F...-F...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.L...-L...-L...-.---..FFF.R...-R...-R...-.---..---.-...--...--...-.---..---.-...--...--...-.---..FFF.-...B-...B-...B.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.L...-L...-L...-.RRR..FFF.-...--...--...-.---..FFF.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.-...--...--...-.---.', 'ULFRBD'),
             ('.RRR.R...-R...-R...-.---..FFF.-...--...--...-.LLL..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...--...--...-.---..---.F...-F...-F...-.---.', 'ULFRBD'),
             ('.RRR.R...-R...-R...-.---..FFF.F...-F...-F...-.---..---.-...--...--...-.---..---.-...--...--...-.---..BBB.-...L-...L-...L.---..---.-...--...--...-.---.', 'ULFRBD')),
            use_edges_pattern=True
        )



class Build555EdgesLastSixEdges(BFS):
    """
    Should be 12! or 479,001,600 states
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-last-six-edges',

            # illegal moves...will list legal moves instead
            (),

            '5x5x5',
            'lookup-table-5x5x5-step601-edges-last-six-edges.txt',
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
                "l", "l'", "l2",
                "r", "r'", "r2",
            )
        )


class Build555EdgesLastSixCenters(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-last-six-centers',

            # illegal moves...will list legal moves instead
            (),

            '5x5x5',
            'lookup-table-5x5x5-step602-edges-last-six-centers.txt',
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
                "l", "l'", "l2",
                "r", "r'", "r2",
            )
        )


'''
DONE - rethink the thing where you consider a paired edge state the same regardless of orientation

- Need IDA tables for solving centers and pairing edges in L4E. The difference in this vs the "solve
  last four edges" table that we have today is that it requires the centers to be solved but our
  centers are going to be in bars.

- step60 attempt to pair all three L4E at once
    - only allow a w turn if there is an L4E group in that plane
    - only allow a w turn if all four centers involved are either solved or in bars



brainstorm #1
=============
step10,20 - stage centers
    - 20 moves

step40 - solve any 3-edges with 2-edge prune table

    - solving any 3-edges anywhere
        - 12!/(9!*3!) = 220 starting positions
        - midges 24 * 22 * 20 = 10,560
        - wings 24 * 23 * 22 * 21 * 20 * 19 = 96,909,120
        - 10,560 * 96,909,120 = 1,023,360,307,200

    - solving any 2-edges anywhere
        - 12!/(10!*2!) = 66 starting positions
        - midges 24 * 22 = 528
        - wings 24 * 23 * 22 * 21 = 255,024
        - 528 * 255,024 = 134,652,672
        ***************************************************
        - This table is building now...hope math checks out
        ***************************************************

    - 134652672/1023360307200 = 0.000 131 5789473684
    - ~8 moves?

step50 - solve another 3-edges
    - IDA with 2-edge prune table
    - do not break up any of the 3-edges from step40
    ~8 moves?

step60
    - do not break up 6-paired edges
    - solve UD centers
    - FB centers to horizontal bars or solved
    - L centers to horizontal bars or solved
    - R centers to horizontal bars, vertical bars or solved
    - 70^6 = 117,649,000,000 center states
    - multiple 24,010,000 center prune tables

    - place 6 paired edges in y-plane and LU LD
    - 12!/(6!*6!) = 924 edge states
    - 24010000/(924*117,649,000,000) = 0.000 000 220
    - If this is too slow you can always just do the centers and
      move the edges via another phase.

    - FEASIBLE
    ~12 moves?

step70
    - solve LFRB centers
    - pair last 6-edges
    - this will use x-plane slices to keep 4 of the unpaired edges on side R, the
      other two will be at LB LF
    - x-plane slice is only allowed if side R is solved or horizontal bar
    - edges prune table should be 12! or 479,001,600
        ***************************************************
        - This table is building now...hope math checks out
        ***************************************************
    - centers prune table should be 8!/(2*2*2*2) or 2520. It may be ~2x that
      since the R centers can also be vertical bars...not huge though.
    - 479001600/(479001600*2520*2) = 0.000 198

    ~16 moves?

This would reduce to 333 in ~64 steps so solve in ~84...that would be awesome
There are slices in here though and each of those really counts as two.



brainstorm #2
=============
- stage centers

step40 - pair 2-edges
    ~6 moves

step50 - pair 2-edges
    ~6 moves

step60
    - LR and FB centers to vertical bars
    - move 4-edges to x-plane
    ~ 10 moves

step70
    - UD centers to solved, vertical bars or horizontal bars
    - L4E the y-plane of edges
    ~ 10 moves

step80
    - do y-plane and z-plane L4E at the same time?
    - I have the tables but am not sure how short the solutions will be since
      you can only switch from solving y-plane to z-plane (or vice versa)
      when the UD centers are solved. I don't think that would happen a ton
      during a solve.  If you did them one plane at a time they would average
      11 moves each so 22 moves is the worst case.
    - you could test this today with the current edges strategy
    ~17 moves?

This would reduce to 333 in ~69 steps



math on last 4-edges
====================
    midges 8 * 6 * 4 = 192
    wings 8*7*6*5*4*3 = 20,160
    192 * 20,160 = 3,870,720
    But I know the answer is really 40,320

    Each midge is one of 4 letters, lower or upper case depending on orientation
    So 2^4 or 16 possibilties there...not 192. But I think it is really 2^3 because
    you can't flip the O of the last midge by itself.

    There are 8 wings that can be one of 4 letters (upper and lower case)
    8! is 40,320...that is it!!

'''

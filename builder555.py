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


# =====
# Edges
# =====
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


# ===============================================
# - solve 1st four without L4E staging
# - solve 2nd four without breaking up first four
# - solve 3rd four via L4E
# ===============================================
class Build555EdgesSolveFirstFour(BFS):
    """
    Get 4-edges paired in the x, y or z plane but once they are paired
    always rotate them around to be in the x-plane.  This is needed
    for solving the next four edges.
    """

    def __init__(self):

        BFS.__init__(self,
            '5x5x5-edges-first-four',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step700-edges-first-four.txt',
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
            . - - - .""", "ascii"),

            ("""
            . U U U .
            - U U U -
            - U U U -
            - U U U -
            . U U U .

 . - - - .  . F F F .  . - - - .  . B B B .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . - - - .  . F F F .  . - - - .  . B B B .

            . D D D .
            - D D D -
            - D D D -
            - D D D -
            . D D D .""", "ascii"),

            ("""
            . - - - .
            U U U U U
            U U U U U
            U U U U U
            . - - - .

 . L L L .  . - - - .  . R R R .  . - - - .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . L L L .  . - - - .  . R R R .  . - - - .

            . - - - .
            D D D D D
            D D D D D
            D D D D D
            . - - - .""", "ascii")),
            use_edges_pattern=True,
        )


class Build555EdgesSolveSecondFour(BFS):
    """
    Pair the 2nd four edges in the y or z plane.  When we are building
    the table we will not perform any move that would break up the four
    paired edges (LB, LF, RF, RB) that we paired in the previous phase.
    """

    def __init__(self):

        BFS.__init__(self,
            '5x5x5-edges-second-four',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step800-edges-second-four.txt',
            False, # store_as_hex
            (("""
            . U U U .
            - U U U -
            - U U U -
            - U U U -
            . U U U .

 . - - - .  . F F F .  . - - - .  . B B B .
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 . - - - .  . F F F .  . - - - .  . B B B .

            . D D D .
            - D D D -
            - D D D -
            - D D D -
            . D D D .""", "ascii"),

            ("""
            . - - - .
            U U U U U
            U U U U U
            U U U U U
            . - - - .

 . L L L .  . - - - .  . R R R .  . - - - .
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 . L L L .  . - - - .  . R R R .  . - - - .

            . - - - .
            D D D D D
            D D D D D
            D D D D D
            . - - - .""", "ascii"),




),
            use_edges_pattern=True,
        )


# =========
# L4E
# =========
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
# =============================================================================
# dwalton
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
            'starting-states-lookup-table-5x5x5-step52.txt',
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
            'starting-states-lookup-table-5x5x5-step50.txt',
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


'''
Can we solve all three L4E groups and the centers at once?  Probably not but thinking outloud...

step60 table would be all centers solved and edges paired using edges_patterns
- any w move is allowed (this is a MUST for solving a L4E group) but...
- only allow a w move if
    - there is a L4E group in that plane
    - the centers in the plane are either solved or in bars and the w move will not break up the bars


step61 edges prune table

step62 centers prune table
- any w move is allowed (this is a MUST for solving a L4E group) but...
- only allow a w move if
    - the centers in the plane are either solved or in bars and the w move will not break up the bars
- not sure how big this table will go but my gut says it is buildable. There are only 6 vertical bar
    patterns per side
'''

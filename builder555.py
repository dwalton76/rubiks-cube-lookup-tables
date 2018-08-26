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
            . U U U .
            . U U U .
            . U U U .
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
            False, # store_as_hex
            (('......UUU..UUU..UUU............LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............BFB..BFB..BFB............LRR..LRR..LRR............FBF..FBF..FBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............BFB..BFB..BFB............RRL..RRL..RRL............FBF..FBF..FBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............BFF..BFF..BFF............LRR..LRR..LRR............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............BFF..BFF..BFF............LRR..LRR..LRR............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............BFF..BFF..BFF............RRL..RRL..RRL............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............BFF..BFF..BFF............RRL..RRL..RRL............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFB..FFB..FFB............LRR..LRR..LRR............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFB..FFB..FFB............LRR..LRR..LRR............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFB..FFB..FFB............RRL..RRL..RRL............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFB..FFB..FFB............RRL..RRL..RRL............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............BFB..BFB..BFB............LRR..LRR..LRR............FBF..FBF..FBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............BFB..BFB..BFB............RRL..RRL..RRL............FBF..FBF..FBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............BFF..BFF..BFF............LRR..LRR..LRR............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............BFF..BFF..BFF............LRR..LRR..LRR............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............BFF..BFF..BFF............RRL..RRL..RRL............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............BFF..BFF..BFF............RRL..RRL..RRL............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFB..FFB..FFB............LRR..LRR..LRR............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFB..FFB..FFB............LRR..LRR..LRR............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFB..FFB..FFB............RRL..RRL..RRL............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFB..FFB..FFB............RRL..RRL..RRL............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLR..RLR..RLR............BFB..BFB..BFB............LRL..LRL..LRL............FBF..FBF..FBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLR..RLR..RLR............BFF..BFF..BFF............LRL..LRL..LRL............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLR..RLR..RLR............BFF..BFF..BFF............LRL..LRL..LRL............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLR..RLR..RLR............FFB..FFB..FFB............LRL..LRL..LRL............BBF..BBF..BBF............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLR..RLR..RLR............FFB..FFB..FFB............LRL..LRL..LRL............FBB..FBB..FBB............UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB............UUU..UUU..UUU......', 'ULFRBD')),
        )


class StartingStates555Step40(BFS):
    """
    There are 36 vertical bar patterns that can be made from the LFRB centers
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
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .""", "ascii"),),
        )


class Build555Step40(BFS):
    """
    There are 36 vertical bar patterns that can be made from the LFRB centers
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
            False, # store_as_hex
            (('......UUU..UUU..UUU...........LLLLLLLLLLLLLLL..........LBFBLLBFBLLBFBL..........LRRRLLRRRLLRRRL..........LFBFLLFBFLLFBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLLLLLLLLLLLLL..........LBFFLLBFFLLBFFL..........LRRRLLRRRLLRRRL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLLLLLLLLLLLLL..........LBFFLLBFFLLBFFL..........LRRRLLRRRLLRRRL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLLLLLLLLLLLLL..........LFFBLLFFBLLFFBL..........LRRRLLRRRLLRRRL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLLLLLLLLLLLLL..........LFFBLLFFBLLFFBL..........LRRRLLRRRLLRRRL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLLLLLLLLLLLLL..........LFFFLLFFFLLFFFL..........LRRRLLRRRLLRRRL..........LBBBLLBBBLLBBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LBFBLLBFBLLBFBL..........LLRRLLLRRLLLRRL..........LFBFLLFBFLLFBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LBFBLLBFBLLBFBL..........LRRLLLRRLLLRRLL..........LFBFLLFBFLLFBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LBFFLLBFFLLBFFL..........LLRRLLLRRLLLRRL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LBFFLLBFFLLBFFL..........LLRRLLLRRLLLRRL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LBFFLLBFFLLBFFL..........LRRLLLRRLLLRRLL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LBFFLLBFFLLBFFL..........LRRLLLRRLLLRRLL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LFFBLLFFBLLFFBL..........LLRRLLLRRLLLRRL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LFFBLLFFBLLFFBL..........LLRRLLLRRLLLRRL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LFFBLLFFBLLFFBL..........LRRLLLRRLLLRRLL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LFFBLLFFBLLFFBL..........LRRLLLRRLLLRRLL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LFFFLLFFFLLFFFL..........LLRRLLLRRLLLRRL..........LBBBLLBBBLLBBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LLLRLLLLRLLLLRL..........LFFFLLFFFLLFFFL..........LRRLLLRRLLLRRLL..........LBBBLLBBBLLBBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LBFBLLBFBLLBFBL..........LLRRLLLRRLLLRRL..........LFBFLLFBFLLFBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LBFBLLBFBLLBFBL..........LRRLLLRRLLLRRLL..........LFBFLLFBFLLFBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LBFFLLBFFLLBFFL..........LLRRLLLRRLLLRRL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LBFFLLBFFLLBFFL..........LLRRLLLRRLLLRRL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LBFFLLBFFLLBFFL..........LRRLLLRRLLLRRLL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LBFFLLBFFLLBFFL..........LRRLLLRRLLLRRLL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LFFBLLFFBLLFFBL..........LLRRLLLRRLLLRRL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LFFBLLFFBLLFFBL..........LLRRLLLRRLLLRRL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LFFBLLFFBLLFFBL..........LRRLLLRRLLLRRLL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LFFBLLFFBLLFFBL..........LRRLLLRRLLLRRLL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LFFFLLFFFLLFFFL..........LLRRLLLRRLLLRRL..........LBBBLLBBBLLBBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLLLLRLLLLRLLL..........LFFFLLFFFLLFFFL..........LRRLLLRRLLLRRLL..........LBBBLLBBBLLBBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLRLLRLRLLRLRL..........LBFBLLBFBLLBFBL..........LLRLLLLRLLLLRLL..........LFBFLLFBFLLFBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLRLLRLRLLRLRL..........LBFFLLBFFLLBFFL..........LLRLLLLRLLLLRLL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLRLLRLRLLRLRL..........LBFFLLBFFLLBFFL..........LLRLLLLRLLLLRLL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLRLLRLRLLRLRL..........LFFBLLFFBLLFFBL..........LLRLLLLRLLLLRLL..........LBBFLLBBFLLBBFL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLRLLRLRLLRLRL..........LFFBLLFFBLLFFBL..........LLRLLLLRLLLLRLL..........LFBBLLFBBLLFBBL...........UUU..UUU..UUU......', 'ULFRBD'),
             ('......UUU..UUU..UUU...........LRLRLLRLRLLRLRL..........LFFFLLFFFLLFFFL..........LLRLLLLRLLLLRLL..........LBBBLLBBBLLBBBL...........UUU..UUU..UUU......', 'ULFRBD')),
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
            "B", "B'"),

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
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""", "ascii"),),
        )


class Build555Step52(BFS):
    """
    There are 36 vertical bar patterns that can be made from the UFBD centers
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
            "B", "B'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step52.txt',
            False, # store_as_hex
            (('......DUD..DUD..DUD............LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF............UDU..UDU..UDU......', 'ULFRBD'),
             ('......DUD..DUD..DUD............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF............UDU..UDU..UDU......', 'ULFRBD'),
             ('......DUD..DUD..DUD............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB............UDU..UDU..UDU......', 'ULFRBD'),
             ('......DUD..DUD..DUD............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF............UDU..UDU..UDU......', 'ULFRBD'),
             ('......DUD..DUD..DUD............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB............UDU..UDU..UDU......', 'ULFRBD'),
             ('......DUD..DUD..DUD............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............UDU..UDU..UDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF............DDU..DDU..DDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF............UDD..UDD..UDD......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF............DDU..DDU..DDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF............UDD..UDD..UDD......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB............DDU..DDU..DDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB............UDD..UDD..UDD......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF............DDU..DDU..DDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF............UDD..UDD..UDD......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB............DDU..DDU..DDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB............UDD..UDD..UDD......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............DDU..DDU..DDU......', 'ULFRBD'),
             ('......DUU..DUU..DUU............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF............DDU..DDU..DDU......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF............UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF............DDU..DDU..DDU......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF............UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB............DDU..DDU..DDU......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB............UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF............DDU..DDU..DDU......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF............UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB............DDU..DDU..DDU......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB............UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............DDU..DDU..DDU......', 'ULFRBD'),
             ('......UUD..UUD..UUD............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............UDD..UDD..UDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD')),
        )


class StartingStates555Step50(BFS):
    """
    There are 36 vertical bar patterns that can be made from the UFBD centers
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
 x L L L x  x F F F x  x R R R x  x B B B x
 x L L L x  x F F F x  x R R R x  x B B B x
 x L L L x  x F F F x  x R R R x  x B B B x
 . x x x .  . U U U .  . x x x .  . U U U .

            . U U U .
            x D D D x
            x D D D x
            x D D D x
            . U U U .""", "ascii"),),
        )


class Build555Step50(BFS):
    """
    There are 36 vertical bar patterns that can be made from the UFBD centers
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
            ),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step50.txt',
            False, # store_as_hex
            (('.UUU.xDUDxxDUDxxDUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFBxxBFBxxBFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBFxxFBFxxFBFx.UUU..UUU.xUDUxxUDUxxUDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUDxxDUDxxDUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xUDUxxUDUxxUDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUDxxDUDxxDUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xUDUxxUDUxxUDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUDxxDUDxxDUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xUDUxxUDUxxUDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUDxxDUDxxDUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xUDUxxUDUxxUDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUDxxDUDxxDUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBBxxBBBxxBBBx.UUU..UUU.xUDUxxUDUxxUDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFBxxBFBxxBFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBFxxFBFxxFBFx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFBxxBFBxxBFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBFxxFBFxxFBFx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBBxxBBBxxBBBx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xDUUxxDUUxxDUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBBxxBBBxxBBBx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFBxxBFBxxBFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBFxxFBFxxFBFx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFBxxBFBxxBFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBFxxFBFxxFBFx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBBxxBBBxxBBBx.UUU..UUU.xDDUxxDDUxxDDUx.UUU.', 'ULFRBD'),
             ('.UUU.xUUDxxUUDxxUUDx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBBxxBBBxxBBBx.UUU..UUU.xUDDxxUDDxxUDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFBxxBFBxxBFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBFxxFBFxxFBFx.UUU..UUU.xDDDxxDDDxxDDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xDDDxxDDDxxDDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xBFFxxBFFxxBFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xDDDxxDDDxxDDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBFxxBBFxxBBFx.UUU..UUU.xDDDxxDDDxxDDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFBxxFFBxxFFBx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xFBBxxFBBxxFBBx.UUU..UUU.xDDDxxDDDxxDDDx.UUU.', 'ULFRBD'),
             ('.UUU.xUUUxxUUUxxUUUx.UUU..xxx.xLLLxxLLLxxLLLx.xxx..UUU.xFFFxxFFFxxFFFx.UUU..xxx.xRRRxxRRRxxRRRx.xxx..UUU.xBBBxxBBBxxBBBx.UUU..UUU.xDDDxxDDDxxDDDx.UUU.', 'ULFRBD'))
        )

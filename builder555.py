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


# =================================
# New edge pairing code starts here
# =================================
class StartingStates555Step40(BFS):
    """
    LR centers to horizontal bars or solved (4900 states)
    Pair 2-edges at LU LD
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step40',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step40.txt',
            False, # store_as_hex
            (("""
            . - - - .
            U . . . -
            U . . . -
            U . . . -
            . - - - .

 . L L L .  . - - - .  . - - - .  . - - - .
 - L L L -  - . . . -  - R R R -  - . . . -
 - L L L -  - . . . -  - R R R -  - . . . -
 - L L L -  - . . . -  - R R R -  - . . . -
 . L L L .  . - - - .  . - - - .  . - - - .

            . - - - .
            D . . . -
            D . . . -
            D . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
            legal_moves=(
                "L2", "R2",
                "2U2", "2D2",
            )
        )


class Build555Step40(BFS):
    """
    LR centers to horizontal bars or solved (4900 states)
    Pair 2-edges at LU LD
    """

    def __init__(self):
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
            (('.---.D...-D...-D...-.---..LLL.-LLL--LLL--LLL-.LLL..---.-...--...--...-.---..---.-RRR--RRR--RRR-.---..---.-...--...--...-.---..---.U...-U...-U...-.---.', 'ULFRBD'),
             ('.---.D...-D...-D...-.---..LLL.-LLL--LLL--RRR-.LLL..---.-...--...--...-.---..---.-LLL--RRR--RRR-.---..---.-...--...--...-.---..---.U...-U...-U...-.---.', 'ULFRBD'),
             ('.---.D...-D...-D...-.---..LLL.-RRR--LLL--LLL-.LLL..---.-...--...--...-.---..---.-RRR--RRR--LLL-.---..---.-...--...--...-.---..---.U...-U...-U...-.---.', 'ULFRBD'),
             ('.---.U...-U...-U...-.---..LLL.-LLL--LLL--RRR-.LLL..---.-...--...--...-.---..---.-RRR--RRR--LLL-.---..---.-...--...--...-.---..---.D...-D...-D...-.---.', 'ULFRBD'),
             ('.---.U...-U...-U...-.---..LLL.-RRR--LLL--LLL-.LLL..---.-...--...--...-.---..---.-LLL--RRR--RRR-.---..---.-...--...--...-.---..---.D...-D...-D...-.---.', 'ULFRBD'),
             ('.---.U...-U...-U...-.---..LLL.-RRR--LLL--RRR-.LLL..---.-...--...--...-.---..---.-LLL--RRR--LLL-.---..---.-...--...--...-.---..---.D...-D...-D...-.---.', 'ULFRBD')),
            use_edges_pattern=True
        )


class Build555Step41(BFS):
    """
    Pair 2-edges at LU LD
    """

    def __init__(self):
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
            (("""
            . - - - .
            U . . . -
            U . . . -
            U . . . -
            . - - - .

 . L L L .  . - - - .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . L L L .  . - - - .  . - - - .  . - - - .

            . - - - .
            D . . . -
            D . . . -
            D . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True
        )


class StartingStates555Step42(BFS):
    """
    LR centers to bars or solved
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step42',

            # illegal moves
            (),

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


class Build555Step42(BFS):
    """
    LR centers to horizontal bars or solved
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
            ),

            '5x5x5',
            'lookup-table-5x5x5-step42.txt',
            False, # store_as_hex
            (('...............................LLL..LLL..LLL.....................................RRR..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR.....................................LLL..RRR..LLL........................................................', 'ULFRBD'))
        )


class StartingStates555Step50(BFS):
    """
    LR centers to horizontal bars or solved
    FB centers to vertical bars or solved (4900 states)
    pair 2-edges at RU RD
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step50',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step50.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - . . . U
            - . . . U
            - . . . U
            . - - - .

 . - - - .  . - - - .  . R R R .  . - - - .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . - - - .  . - - - .  . R R R .  . - - - .

            . - - - .
            - . . . D
            - . . . D
            - . . . D
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
            legal_moves=(
                "2R2", "2L2",
                "F2", "B2",
                "L2", "R2",
                "2U2", "2D2",
            )
        )


class Build555Step50(BFS):
    """
    LR centers to horizontal bars or solved
    FB centers to vertical bars or solved (4900 states)
    pair 2-edges at RU RD
    """

    def __init__(self):

        BFS.__init__(self,
            '5x5x5-step50',

             # illegal moves
             (),

            '5x5x5',
            'lookup-table-5x5x5-step50.txt',
            False, # store_as_hex
            (('.---.-...D-...D-...D.---..---.-LLL--LLL--LLL-.---..---.-FFF--FFF--FFF-.---..RRR.-RRR--RRR--RRR-.RRR..---.-BBB--BBB--BBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-BFB--BFB--BFB-.---..RRR.-LLL--RRR--RRR-.RRR..---.-FBF--FBF--FBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-BFB--BFB--BFB-.---..RRR.-RRR--RRR--LLL-.RRR..---.-FBF--FBF--FBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-BFF--BFF--BFF-.---..RRR.-LLL--RRR--RRR-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-BFF--BFF--BFF-.---..RRR.-LLL--RRR--RRR-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-BFF--BFF--BFF-.---..RRR.-RRR--RRR--LLL-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-BFF--BFF--BFF-.---..RRR.-RRR--RRR--LLL-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-FFB--FFB--FFB-.---..RRR.-LLL--RRR--RRR-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-FFB--FFB--FFB-.---..RRR.-LLL--RRR--RRR-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-FFB--FFB--FFB-.---..RRR.-RRR--RRR--LLL-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-FFB--FFB--FFB-.---..RRR.-RRR--RRR--LLL-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-FFF--FFF--FFF-.---..RRR.-LLL--RRR--RRR-.RRR..---.-BBB--BBB--BBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-LLL--LLL--RRR-.---..---.-FFF--FFF--FFF-.---..RRR.-RRR--RRR--LLL-.RRR..---.-BBB--BBB--BBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-BFB--BFB--BFB-.---..RRR.-LLL--RRR--RRR-.RRR..---.-FBF--FBF--FBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-BFB--BFB--BFB-.---..RRR.-RRR--RRR--LLL-.RRR..---.-FBF--FBF--FBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-BFF--BFF--BFF-.---..RRR.-LLL--RRR--RRR-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-BFF--BFF--BFF-.---..RRR.-LLL--RRR--RRR-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-BFF--BFF--BFF-.---..RRR.-RRR--RRR--LLL-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-BFF--BFF--BFF-.---..RRR.-RRR--RRR--LLL-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-FFB--FFB--FFB-.---..RRR.-LLL--RRR--RRR-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-FFB--FFB--FFB-.---..RRR.-LLL--RRR--RRR-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-FFB--FFB--FFB-.---..RRR.-RRR--RRR--LLL-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-FFB--FFB--FFB-.---..RRR.-RRR--RRR--LLL-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-FFF--FFF--FFF-.---..RRR.-LLL--RRR--RRR-.RRR..---.-BBB--BBB--BBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--LLL-.---..---.-FFF--FFF--FFF-.---..RRR.-RRR--RRR--LLL-.RRR..---.-BBB--BBB--BBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--RRR-.---..---.-BFB--BFB--BFB-.---..RRR.-LLL--RRR--LLL-.RRR..---.-FBF--FBF--FBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--RRR-.---..---.-BFF--BFF--BFF-.---..RRR.-LLL--RRR--LLL-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--RRR-.---..---.-BFF--BFF--BFF-.---..RRR.-LLL--RRR--LLL-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--RRR-.---..---.-FFB--FFB--FFB-.---..RRR.-LLL--RRR--LLL-.RRR..---.-BBF--BBF--BBF-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--RRR-.---..---.-FFB--FFB--FFB-.---..RRR.-LLL--RRR--LLL-.RRR..---.-FBB--FBB--FBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...D-...D-...D.---..---.-RRR--LLL--RRR-.---..---.-FFF--FFF--FFF-.---..RRR.-LLL--RRR--LLL-.RRR..---.-BBB--BBB--BBB-.---..---.-...U-...U-...U.---.', 'ULFRBD'),
             ('.---.-...U-...U-...U.---..---.-LLL--LLL--LLL-.---..---.-BFB--BFB--BFB-.---..RRR.-RRR--RRR--RRR-.RRR..---.-FBF--FBF--FBF-.---..---.-...D-...D-...D.---.', 'ULFRBD'),
             ('.---.-...U-...U-...U.---..---.-LLL--LLL--LLL-.---..---.-BFF--BFF--BFF-.---..RRR.-RRR--RRR--RRR-.RRR..---.-BBF--BBF--BBF-.---..---.-...D-...D-...D.---.', 'ULFRBD'),
             ('.---.-...U-...U-...U.---..---.-LLL--LLL--LLL-.---..---.-BFF--BFF--BFF-.---..RRR.-RRR--RRR--RRR-.RRR..---.-FBB--FBB--FBB-.---..---.-...D-...D-...D.---.', 'ULFRBD'),
             ('.---.-...U-...U-...U.---..---.-LLL--LLL--LLL-.---..---.-FFB--FFB--FFB-.---..RRR.-RRR--RRR--RRR-.RRR..---.-BBF--BBF--BBF-.---..---.-...D-...D-...D.---.', 'ULFRBD'),
             ('.---.-...U-...U-...U.---..---.-LLL--LLL--LLL-.---..---.-FFB--FFB--FFB-.---..RRR.-RRR--RRR--RRR-.RRR..---.-FBB--FBB--FBB-.---..---.-...D-...D-...D.---.', 'ULFRBD')),
            use_edges_pattern=True,
            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2",
                "R", "R'", "R2",
                "Lw2", "Rw2",
                "2U2", "2D2",
                "2L2", "2R2",
            )
        )


class Build555Step51(BFS):
    """
    pair 2-edges at RU RD

    - midges 20 * 18 = 360
    - wings 20 * 19 * 18 * 17 = 116,280
    - 360 * 116,280 = 41,860,800
    41,860,800 / 2 = 20,930,400
    """

    def __init__(self):

        BFS.__init__(self,
            '5x5x5-step51',

             # illegal moves
             (),

            '5x5x5',
            'lookup-table-5x5x5-step51.txt',
            False, # store_as_hex
            (("""
            . - - - .
            - . . . U
            - . . . U
            - . . . U
            . - - - .

 . - - - .  . - - - .  . R R R .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - - - .  . - - - .  . R R R .  . - - - .

            . - - - .
            - . . . D
            - . . . D
            - . . . D
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2",
                "R", "R'", "R2",
                "Lw2", "Rw2",
                "2U2", "2D2",
                "2L2", "2R2",
            )
        )

class StartingStates555Step52(BFS):
    """
    LR centers to horizontal bars or solved
    FB centers to vertical bars or solved (4900 states)
    """

    def __init__(self):
        BFS.__init__(self,
            'starting-states-5x5x5-step52',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step52.txt',
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
                "L2", "R2",
                "2U2", "2D2",
            )
        )


class Build555Step52(BFS):
    """
    LR centers to horizontal bars or solved
    FB centers to vertical bars or solved (4900 states)
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step52',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step52.txt',
            False, # store_as_hex
            (('...............................LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BFB..BFB..BFB............LLL..RRR..RRR............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BFB..BFB..BFB............RRR..RRR..LLL............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BFF..BFF..BFF............LLL..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BFF..BFF..BFF............LLL..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BFF..BFF..BFF............RRR..RRR..LLL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BFF..BFF..BFF............RRR..RRR..LLL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFB..FFB..FFB............LLL..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFB..FFB..FFB............LLL..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFB..FFB..FFB............RRR..RRR..LLL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFB..FFB..FFB............RRR..RRR..LLL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............LLL..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............RRR..RRR..LLL............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BFB..BFB..BFB............LLL..RRR..RRR............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BFB..BFB..BFB............RRR..RRR..LLL............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BFF..BFF..BFF............LLL..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BFF..BFF..BFF............LLL..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BFF..BFF..BFF............RRR..RRR..LLL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BFF..BFF..BFF............RRR..RRR..LLL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFB..FFB..FFB............LLL..RRR..RRR............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFB..FFB..FFB............LLL..RRR..RRR............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFB..FFB..FFB............RRR..RRR..LLL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFB..FFB..FFB............RRR..RRR..LLL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............LLL..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............RRR..RRR..LLL............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............BFB..BFB..BFB............LLL..RRR..LLL............FBF..FBF..FBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............BFF..BFF..BFF............LLL..RRR..LLL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............BFF..BFF..BFF............LLL..RRR..LLL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............FFB..FFB..FFB............LLL..RRR..LLL............BBF..BBF..BBF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............FFB..FFB..FFB............LLL..RRR..LLL............FBB..FBB..FBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............FFF..FFF..FFF............LLL..RRR..LLL............BBB..BBB..BBB...............................', 'ULFRBD')),
            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2",
                "R", "R'", "R2",
                "Lw2", "Rw2",
                "2U2", "2D2",
                "2L2", "2R2",
            )
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
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
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
    - LR centers to horizontal bars or solved (4900 states)
    - pair 2-edges at LU LD
        - midges 24 * 22 = 528
        - wings 24 * 23 * 22 * 21 = 255,024
        - 528 * 255,024 = 134,652,672
        - It is actually this /2, I am not sure why but have seen this pattern before
            134,652,672 / 2 = 67,326,336
    ~7 moves?


step50
    - FB centers to vertical bars or solved (4900 states)
    - pair 2-edges at RU RD
    - at the end of this stage to a L and R move to rotate those
      horizontal bars to vertical.  This will also put the 4-edges
      that are paired in the x-plane
    ~9 moves?

step60
    - solve LR centers (6 states)
    - D centers to vertical bars
    - U centers to solved or bars
        - 4900 states
    - pair 2-edges at DL DR
        - 4-edges are paired and in x-plane so new math for 2-edges...
            - midges 16 * 14 = 224
            - wings 16 * 15 * 14 * 13 = 43680
            - 224 * 43680 = 9,784,320
            - 9,784,320/2 = 4,892,160
    - 4,892,160/(4,892,160 * 4900 * 6) = 0.000 034
    - (4,892,160 * 6)/(4,892,160 * 4900 * 6) = 0.000 204
    ~10 moves?


step80
    - solve UFBD centers
    - pair last 6-edges
    - this will use y-plane slices to keep 4 of the unpaired edges on side U, the
      other two will be at DU DB
    - y-plane slice is only allowed if side U is solved or vertical bar
    - edges prune table should be 12! or 479,001,600
    - centers prune table is 4950
    - 479001600/(479001600*4950) = 0.000 202
    ~14 moves?

This would be reduce to 333 in ~65 moves
'''

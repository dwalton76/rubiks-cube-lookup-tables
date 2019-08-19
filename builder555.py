#!/usr/bin/env python3

from rubikscubennnsolver.RubiksCube333 import moves_333
from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)


class Build555Ultimate(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-ultimate',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step00-ultimate.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            U U U U U
            U U U U U
            U U U U U
            U U U U U
            U U U U U

 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B

            D D D D D
            D D D D D
            D D D D D
            D D D D D
            D D D D D""", "ascii"),),
        )

class Build555UltimateCenters(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-ultimate',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step00-ultimate-centers.txt',
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
            . . . . .""", "ascii"),),

            legal_moves = (
                # OBTM 36 moves
                "U", "U'", "U2", "Uw", "Uw'", "Uw2",
                "L", "L'", "L2", "Lw", "Lw'", "Lw2",
                "F" , "F'", "F2", "Fw", "Fw'", "Fw2",
                "R" , "R'", "R2", "Rw", "Rw'", "Rw2",
                "B" , "B'", "B2", "Bw", "Bw'", "Bw2",
                "D" , "D'", "D2", "Dw", "Dw'", "Dw2",

                # SSTM 36 moves
                #"U", "U'", "U2",
                #"L", "L'", "L2",
                #"F" , "F'", "F2",
                #"R" , "R'", "R2",
                #"B" , "B'", "B2",
                #"D" , "D'", "D2",
                #"2U", "2U'", "2U2", "2D", "2D'", "2D2",
                #"2L", "2L'", "2L2", "2R", "2R'", "2R2",
                #"2F", "2F'", "2F2", "2B", "2B'", "2B2"

                # BTM is both, 54 moves
                #"U", "U'", "U2", "Uw", "Uw'", "Uw2",
                #"L", "L'", "L2", "Lw", "Lw'", "Lw2",
                #"F" , "F'", "F2", "Fw", "Fw'", "Fw2",
                #"R" , "R'", "R2", "Rw", "Rw'", "Rw2",
                #"B" , "B'", "B2", "Bw", "Bw'", "Bw2",
                #"D" , "D'", "D2", "Dw", "Dw'", "Dw2",
                #"2U", "2U'", "2U2", "2D", "2D'", "2D2",
                #"2L", "2L'", "2L2", "2R", "2R'", "2R2",
                #"2F", "2F'", "2F2", "2B", "2B'", "2B2"
            )
        )


class Build555LRCenterStage(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step10-LR-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . x x x .  . L L L .  . x x x .
 . L L L .  . x x x .  . L L L .  . x x x .
 . L L L .  . x x x .  . L L L .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .""", "ascii"),),
        )


class Build555LRCenterStageTCenterOnly(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-t-center-stage',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step11-LR-centers-stage-t-center-only.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . L . .  . . x . .  . . L . .  . . x . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . L . .  . . x . .  . . L . .  . . x . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .""", "ascii"),),
        )


class Build555LRCenterStageXCenterOnly(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-x-center-stage',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step12-LR-centers-stage-x-center-only.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .""", "ascii"),),
        )



class Build555FBCenterStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-FB-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'"),

            '5x5x5',
            'lookup-table-5x5x5-step20-FB-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .""", "ascii"),)
        )


class Build555FBTCenterStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-FB-t-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'"),

            '5x5x5',
            'lookup-table-5x5x5-step21-FB-t-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . F . .  . . . . .  . . F . .
 . . . . .  . F . F .  . . . . .  . F . F .
 . . . . .  . . F . .  . . . . .  . . F . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .""", "ascii"),)
        )


class Build555FBXCenterStage(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-FB-x-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'"),

            '5x5x5',
            'lookup-table-5x5x5-step22-FB-x-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F . F .  . . . . .  . F . F .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F . F .  . . . . .  . F . F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .""", "ascii"),)
        )


class Build555FBCenterStageLRCenterSolve(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-FB-center-stage-LR-center-solve',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'"),

            '5x5x5',
            'lookup-table-5x5x5-step23-LR-centers-solve.txt',
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


class Build555ULFRBDCenterSolveWithoutLR(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-centers-solve-without-LR',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step30-ULFRBD-centers-solve-without-LR.txt',
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



# =============================
# Pair first 4-edges in z-plane
# LR centers to horizontal bars
# =============================
class Build555EdgesZPlaneEdgesOnly(BFS):
    """
    Pair 3-edges in z-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-z-plane-edges-only',

            # illegal moves
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
            ),
            '5x5x5',
            'lookup-table-5x5x5-step341-edges-z-plane-edges-only.txt',
            False, # store_as_hex

            (("""
            . - - - .
            U . . . U
            U . . . U
            U . . . U
            . - - - .

 . L L L .  . - - - .  . R R R .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . L L L .  . - - - .  . - - - .  . - - - .

            . - - - .
            D . . . -
            D . . . -
            D . . . -
            . - - - .""", "ascii"),

            ("""
            . - - - .
            U . . . U
            U . . . U
            U . . . U
            . - - - .

 . L L L .  . - - - .  . R R R .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - - - .  . - - - .  . R R R .  . - - - .

            . - - - .
            - . . . D
            - . . . D
            - . . . D
            . - - - .""", "ascii"),

            ("""
            . - - - .
            - . . . U
            - . . . U
            - . . . U
            . - - - .

 . - - - .  . - - - .  . R R R .  . - - - .
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
            U . . . -
            U . . . -
            U . . . -
            . - - - .

 . L L L .  . - - - .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . L L L .  . - - - .  . R R R .  . - - - .

            . - - - .
            D . . . D
            D . . . D
            D . . . D
            . - - - .""", "ascii")),
            use_edges_pattern=True,
        )


class StartingStates555EdgesZPlaneCentersOnly(BFS):
    """
    LR centers to horizontal bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-z-plane-centers-only',

            # illegal moves
            (),
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step342-edges-z-plane-centers-only.txt',
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
                "L2", "R2", "2U2", "2D2",
            )
        )


class Build555EdgesZPlaneCentersOnly(BFS):
    """
    LR centers to horizontal bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-z-plane-centers-only',

            # illegal moves
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
            ),
            '5x5x5',
            'lookup-table-5x5x5-step342-edges-z-plane-centers-only.txt',
            False, # store_as_hex
            (('...............................LLL..LLL..LLL.....................................RRR..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR.....................................LLL..RRR..LLL........................................................', 'ULFRBD')),
        )


class StartingStates555EdgesZPlane(BFS):
    """
    LR centers to horizontal bars
    Pair 4-edges in z-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-z-plane',

            # illegal moves
            (),
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step340-edges-z-plane.txt',
            False, # store_as_hex

            (("""
            . - - - .
            U . . . U
            U . . . U
            U . . . U
            . - - - .

 . L L L .  . - - - .  . R R R .  . - - - .
 - L L L -  - . . . -  - R R R -  - . . . -
 - L L L -  - . . . -  - R R R -  - . . . -
 - L L L -  - . . . -  - R R R -  - . . . -
 . L L L .  . - - - .  . R R R .  . - - - .

            . - - - .
            D . . . D
            D . . . D
            D . . . D
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
            legal_moves=(
                "L2", "R2", "2U2", "2D2",
            )
        )


class Build555EdgesZPlane(BFS):
    """
    LR centers to horizontal bars
    Pair 4-edges in z-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-z-plane',

            # illegal moves
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'",
            ),
            '5x5x5',
            'lookup-table-5x5x5-step340-edges-z-plane.txt',
            False, # store_as_hex
            (('.---.D...UD...UD...U.---..LLL.-LLL--LLL--LLL-.LLL..---.-...--...--...-.---..RRR.-RRR--RRR--RRR-.RRR..---.-...--...--...-.---..---.U...DU...DU...D.---.', 'ULFRBD'),
             ('.---.D...UD...UD...U.---..LLL.-LLL--LLL--RRR-.LLL..---.-...--...--...-.---..RRR.-LLL--RRR--RRR-.RRR..---.-...--...--...-.---..---.U...DU...DU...D.---.', 'ULFRBD'),
             ('.---.D...UD...UD...U.---..LLL.-RRR--LLL--LLL-.LLL..---.-...--...--...-.---..RRR.-RRR--RRR--LLL-.RRR..---.-...--...--...-.---..---.U...DU...DU...D.---.', 'ULFRBD'),
             ('.---.U...UU...UU...U.---..LLL.-LLL--LLL--RRR-.LLL..---.-...--...--...-.---..RRR.-RRR--RRR--LLL-.RRR..---.-...--...--...-.---..---.D...DD...DD...D.---.', 'ULFRBD'),
             ('.---.U...UU...UU...U.---..LLL.-RRR--LLL--LLL-.LLL..---.-...--...--...-.---..RRR.-LLL--RRR--RRR-.RRR..---.-...--...--...-.---..---.D...DD...DD...D.---.', 'ULFRBD'),
             ('.---.U...UU...UU...U.---..LLL.-RRR--LLL--RRR-.LLL..---.-...--...--...-.---..RRR.-LLL--RRR--LLL-.RRR..---.-...--...--...-.---..---.D...DD...DD...D.---.', 'ULFRBD')),
            use_edges_pattern=True
        )


# ==============================================
# Pair last 8-edges in y-plane and z-plane
# Solve center (LR and FB will be vertical bars)
# ==============================================
class Build555PairLastEightEdgesEdgesOnly(BFS):
    """
    Should be (8!^2)/2 812,851,200
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-pair-last-eight-edges-edges-only',

            # illegal moves
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step501-pair-last-eight-edges-edges-only.txt',
            False, # store_as_hex

            # starting cubes
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
 . L L L .  . F F F .  . R R R .  . B B B .

            . D D D .
            D . . . D
            D . . . D
            D . . . D
            . D D D .""", "ascii"),),
            use_edges_pattern=True
        )


class Build555PairLastEightEdgesCentersOnly(BFS):
    """
    Should be 6 x 6 x 4900 = 176,400
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-pair-last-eight-edges-centers-only',

            # illegal moves
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step502-pair-last-eight-edges-centers-only.txt',
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


class Build555PairLastEightEdges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-pair-last-eight-edges',

            # illegal moves
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "Uw", "Uw'", "Uw2",
             "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step500-pair-last-eight-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . U U U .
            U U U U U
            U U U U U
            U U U U U
            . U U U .

 . L L L .  . F F F .  . R R R .  . B B B .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . L L L .  . F F F .  . R R R .  . B B B .

            . D D D .
            D D D D D
            D D D D D
            D D D D D
            . D D D .""", "ascii"),),
            use_edges_pattern=True
        )


# ==========================
# L4E last-four-edges tables
# ==========================
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
            False, # store_as_hex
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


class Build555EdgesXPlaneEdgesOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-x-plane-edges-only',
             (), # illegal moves
            '5x5x5',
            'lookup-table-5x5x5-step301-edges-x-plane-edges-only.txt',
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
            legal_moves = (
                "L2", "F2", "R2", "B2",
                "Uw", "Uw'", "Uw2",
                "Dw", "Dw'", "Dw2",
            )
        )


class Build555EdgesXPlaneCentersOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-x-plane-centers-only',
             (), # illegal moves
            '5x5x5',
            'lookup-table-5x5x5-step302-edges-x-plane-centers-only.txt',
            False, # store_as_hex
            # starting cubes
            (("""
            . . . . .
            - . . . -
            - . . . -
            - . . . -
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            - . . . -
            - . . . -
            - . . . -
            . . . . .""", "ascii"),),
            legal_moves = (
                "L2", "F2", "R2", "B2",
                "Uw", "Uw'", "Uw2",
                "Dw", "Dw'", "Dw2",
            )
        )


class Build555EdgesXPlane(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-x-plane',
             (), # illegal moves
            '5x5x5',
            'lookup-table-5x5x5-step300-edges-x-plane.txt',
            False, # store_as_hex

            (("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
            legal_moves = (
                "L2", "F2", "R2", "B2",
                "Uw", "Uw'", "Uw2",
                "Dw", "Dw'", "Dw2",
            )
        )


# brainstorm #1
'''
phase 1
    stage LR centers
    10 moves

phase 2
    stage FB centers
    10 moves

phase 3 - 
    EO the wings, 2,704,156 states
    EO the midges, 2048 states
    LR centers to 1/432, 4900 states

    (4900 * 2048) / (4900 * 2048 * 2,704,156) = 0.000 000 369
    10.8 moves

phase 4
    LR and FB centers to vertical bars
    pair x-plane edges

    432 LR centers * 4900 FB centers

    x-plane edges
        (12*11*10*9)^2 is how many states the wings can be in
        12!/(8!*4!) is how many states the midges can be in
        (12*11*10*9)^2 * 12!/(8!*4!) = 69,861,528,000

    - A 3-edge prune table is
        (12*11*10)^2 is how many states the wings can be in
        12!/(9!*3!) is how many states the midges can be in
        (12*11*10)^2 * 12!/(9!*3!) = 383,328,000

    - A 2-edge prune table is
        (12*11)^2 * 12!/(10!*2!) = 1,149,984

    383,328,000 / (432 * 4900 * 69,861,528,000) = 0.000 000 002
    That is just brutal...we could break this up into two phases:

phase 4a
    L4Eed x-plane edges
    LR centers to horizontal bars
    FB centers to horizontal bars

    432 LR center states
    4900 FB center states
    (12!/(4!*8!))^3 = 121,287,375 edge states

    432 * 4900 is 2,116,800

phase 4b
    LR and FB centers to solved (vertical bars would be fine but not possible)
    6 LR states
    6 FB states

    pair x-plane edges
    4!^3 = 13824 edge states

    6 * 6 * 13824 = 497,664

phase 5
    pair last 8 edges
    solve all centers

    8!^2/2 = 812,851,200 edge states
    6 * 6 * 4900 = 176,400 center states

    -16 moves

that would be ~61 moves
'''

class StartingState555EdgeOrientOuterOrbitLRCenterStage(BFS):
    """
    There should be 432 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-EO-both-orbits',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step900-edge-orient-LR-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . U U D .
            D . . . U
            U . . . U
            U . . . D
            . D U U .

 . D U U .  . D U U .  . D U U .  . D U U .
 D L L L U  U . . . D  D R R R U  U . . . D
 U L L L U  U . . . U  U R R R U  U . . . U
 U L L L D  D . . . U  U R R R D  D . . . U
 . U U D .  . U U D .  . U U D .  . U U D .

            . U U D .
            D . . . U
            U . . . U
            U . . . D
            . D U U .""", "ascii"),)
        )


class Build555LRCenterStageEOBothOrbits(BFS):
    """
    2048 * 4900 * 2704156 = 27,136,746,291,200

    lookup-table-5x5x5-step900-edge-orient-LR-center-stage.txt
    ==========================================================
    0 steps has 78 entries (0 percent, 0.00x previous step)
    1 steps has 1,218 entries (0 percent, 15.62x previous step)
    2 steps has 14,256 entries (0 percent, 11.70x previous step)
    3 steps has 172,288 entries (0 percent, 12.09x previous step)
    4 steps has 1,948,920 entries (7 percent, 11.31x previous step)
    5 steps has 24,348,560 entries (91 percent, 12.49x previous step)
    extrapolate from here
    6 steps has 291,939,234 entries (11.99x previous step)
    7 steps has 3,354,381,798 entries (11.49x previous step)
    8 steps has 36,864,655,960 entries (10.99x previous step)
    9 steps has 386,710,241,020 entries (10.49x previous step)
    10 steps has 3,863,235,307,789 entries (9.99x previous step)
    11 steps has 22,846,263,280,079 entries (5.91x previous step)

    Average: 10.824502972151256
    Total  : 27,136,746,291,200

    phase1+2 ~20 moves
    phase3 11.5 moves
    phase4 ~14 moves
    phase5 ~16 moves
    solve 333 20 moves

    81.5 total
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-EO-both-orbits',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step900-edge-orient-LR-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
             ('.UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.', 'ULFRBD'),
            )
        )

class StartingStates555LRCenterStageEOInnerOrbit(BFS):
    """
    There should be 432 of them
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-EO-inner-orbit',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'"),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . U . .
            . . . . .
            U . . . U
            . . . . .
            . . U . .

 . . U . .  . . U . .  . . U . .  . . U . .
 . L L L .  . . . . .  . R R R .  . . . . .
 U L L L U  U . . . U  U R R R U  U . . . U
 . L L L .  . . . . .  . R R R .  . . . . .
 . . U . .  . . U . .  . . U . .  . . U . .

            . . U . .
            . . . . .
            U . . . U
            . . . . .
            . . U . .""", "ascii"),)
        )


class Build555LRCenterStageEOInnerOrbit(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-EO-inner-orbit',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.txt',
            False, # store_as_hex

            # starting cubes
            (
             ('..U.......U...U.......U....U...LLL.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.LRL...U....U.......U...U.......U....U...RRR.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.RLR...U....U.......U...U.......U....U...RRR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.LRL...U....U.......U...U.......U....U...RRR.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.RLR...U....U.......U...U.......U....U...RRR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.LLR...U....U.......U...U.......U....U...RRL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLLU.RRL...U....U.......U...U.......U....U...RRL.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.LLR...U....U.......U...U.......U....U...RRL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LLR.URLRU.RRL...U....U.......U...U.......U....U...RRL.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.LLL...U....U.......U...U.......U....U...RLR.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLLU.RRR...U....U.......U...U.......U....U...RLR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.LLL...U....U.......U...U.......U....U...RLR.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRL.URLRU.RRR...U....U.......U...U.......U....U...RLR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.LRR...U....U.......U...U.......U....U...RLL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.RLL...U....U.......U...U.......U....U...RLL.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.LRR...U....U.......U...U.......U....U...RLL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.RLL...U....U.......U...U.......U....U...RLL.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...LRR.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.LRR...U....U.......U...U.......U....U...LRR.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.RLL...U....U.......U...U.......U....U...LRR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.LRR...U....U.......U...U.......U....U...LRR.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.RLL...U....U.......U...U.......U....U...LRR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.LLL...U....U.......U...U.......U....U...LRL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLLU.RRR...U....U.......U...U.......U....U...LRL.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.LLL...U....U.......U...U.......U....U...LRL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RLR.URLRU.RRR...U....U.......U...U.......U....U...LRL.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.LLR...U....U.......U...U.......U....U...LLR.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.RRL...U....U.......U...U.......U....U...LLR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.LLR...U....U.......U...U.......U....U...LLR.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.RRL...U....U.......U...U.......U....U...LLR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRL.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.LRL...U....U.......U...U.......U....U...LLL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.RLR...U....U.......U...U.......U....U...LLL.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.LRL...U....U.......U...U.......U....U...LLL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.RLR...U....U.......U...U.......U....U...LLL.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
             ('..U.......U...U.......U....U...RRR.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..', 'ULFRBD'),
            )
        )


class StartingStates555LRCenterStage(BFS):
    """
    There should be 432 of them
    """

    # dwalton
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
            'starting-states-lookup-table-5x5x5-step901-LR-center-stage.txt',
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
        BFS.__init__(self,
            '5x5x5-LR-center-stage',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step901-LR-center-stage.txt',
            False, # store_as_hex

            # starting cubes
            (
             ('...............................LLL..LLL..LLL.....................................RRR..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..LRL.....................................RLR..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..LRL.....................................RRR..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RLR.....................................LRL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RLR.....................................RRR..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................LRL..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................RLR..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..LLL.....................................RRR..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..LLL.....................................RRR..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL.....................................RLR..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL.....................................RLR..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL.....................................RRR..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL.....................................RRR..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR.....................................LRL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR.....................................LRL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR.....................................RRR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR.....................................RRR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..LLL.....................................RRR..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..LLL.....................................RRR..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL.....................................RLR..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL.....................................RLR..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL.....................................RRR..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL.....................................RRR..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR.....................................LRL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR.....................................LRL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR.....................................RRR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR.....................................RRR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..LLL.....................................RRR..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..LRL.....................................RLR..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..LRL.....................................RRR..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..RLR.....................................LRL..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..RLR.....................................RRR..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR.....................................LLL..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR.....................................LRL..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR.....................................RLR..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR.....................................RRR..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..LLR.....................................LRR..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..LLR.....................................RRL..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR.....................................LLR..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR.....................................LRR..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR.....................................RLL..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR.....................................RRL..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..RLL.....................................RRL..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..RRL.....................................RLL..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLL..RRL.....................................RRL..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR.....................................LRR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR.....................................LRR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR.....................................RRL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR.....................................RRL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..RLL.....................................RRL..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..RLL.....................................RRL..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL.....................................RLL..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL.....................................RLL..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL.....................................RRL..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL.....................................RRL..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR.....................................LRR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR.....................................LRR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR.....................................RRL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR.....................................RRL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..RLL.....................................RRL..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..RLL.....................................RRL..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL.....................................RLL..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL.....................................RLL..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL.....................................RRL..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL.....................................RRL..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..LLR.....................................LRR..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..LLR.....................................RRL..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR.....................................LLR..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR.....................................LRR..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR.....................................RLL..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR.....................................RRL..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..RLL.....................................RRL..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..RRL.....................................RLL..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................LLR..RLR..RRL.....................................RRL..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..LLL.....................................RLR..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..LLL.....................................RRR..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..LRL.....................................RLR..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR.....................................LRL..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR.....................................RLR..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..RRR.....................................LLL..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLL..RRR.....................................RLR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL.....................................RLR..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL.....................................RLR..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL.....................................RRR..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL.....................................RRR..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..LRL.....................................RLR..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..LRL.....................................RLR..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR.....................................LLL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR.....................................LLL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR.....................................RLR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR.....................................RLR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL.....................................RLR..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL.....................................RLR..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL.....................................RRR..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL.....................................RRR..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..LRL.....................................RLR..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..LRL.....................................RLR..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR.....................................LLL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR.....................................LLL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR.....................................RLR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR.....................................RLR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..LLL.....................................RLR..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..LLL.....................................RRR..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..LRL.....................................RLR..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR.....................................LLL..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR.....................................LRL..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR.....................................RLR..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR.....................................RRR..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..RRR.....................................LLL..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................LRL..RLR..RRR.....................................RLR..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR.....................................LLR..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR.....................................LRR..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR.....................................RLL..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR.....................................RRL..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..LRR.....................................LLR..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..LRR.....................................RLL..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..RLL.....................................RLL..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..RLL.....................................RRL..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLL..RRL.....................................RLL..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR.....................................LLR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR.....................................LLR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR.....................................RLL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR.....................................RLL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL.....................................RLL..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL.....................................RLL..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL.....................................RRL..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL.....................................RRL..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..RRL.....................................RLL..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..LLR..RRL.....................................RLL..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR.....................................LLR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR.....................................LLR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR.....................................RLL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR.....................................RLL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL.....................................RLL..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL.....................................RLL..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL.....................................RRL..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL.....................................RRL..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..RRL.....................................RLL..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLL..RRL.....................................RLL..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR.....................................LLR..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR.....................................LRR..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR.....................................RLL..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR.....................................RRL..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..LRR.....................................LLR..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..LRR.....................................RLL..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..RLL.....................................RLL..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..RLL.....................................RRL..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................LRR..RLR..RRL.....................................RLL..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..LLR.....................................LRR..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..LRR.....................................LLR..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..LRR.....................................LRR..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..RLL.....................................LRR..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..RLL.....................................RRL..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL.....................................LLR..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL.....................................LRR..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL.....................................RLL..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL.....................................RRL..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..LLR.....................................LRR..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..LLR.....................................LRR..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR.....................................LLR..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR.....................................LLR..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR.....................................LRR..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR.....................................LRR..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL.....................................LRR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL.....................................LRR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL.....................................RRL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL.....................................RRL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..LLR.....................................LRR..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..LLR.....................................LRR..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR.....................................LLR..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR.....................................LLR..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR.....................................LRR..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR.....................................LRR..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL.....................................LRR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL.....................................LRR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL.....................................RRL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL.....................................RRL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..LLR.....................................LRR..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..LRR.....................................LLR..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..LRR.....................................LRR..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..RLL.....................................LRR..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..RLL.....................................RRL..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL.....................................LLR..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL.....................................LRR..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL.....................................RLL..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL.....................................RRL..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..LLL.....................................LRL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..LLL.....................................RRR..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL.....................................LRL..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL.....................................RLR..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..RLR.....................................LRL..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..RRR.....................................LLL..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLL..RRR.....................................LRL..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL.....................................LRL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL.....................................LRL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL.....................................RRR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL.....................................RRR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..RLR.....................................LRL..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..RLR.....................................LRL..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR.....................................LLL..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR.....................................LLL..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR.....................................LRL..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR.....................................LRL..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL.....................................LRL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL.....................................LRL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL.....................................RRR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL.....................................RRR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..RLR.....................................LRL..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..RLR.....................................LRL..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR.....................................LLL..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR.....................................LLL..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR.....................................LRL..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR.....................................LRL..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..LLL.....................................LRL..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..LLL.....................................RRR..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL.....................................LLL..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL.....................................LRL..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL.....................................RLR..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL.....................................RRR..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR.....................................LRL..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..RRR.....................................LLL..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................RLR..RLR..RRR.....................................LRL..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..LLR.....................................LLR..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..LLR.....................................LRR..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..LRR.....................................LLR..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL.....................................LLR..RRR..LRR........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL.....................................LRR..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL.....................................RLL..RRR..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL.....................................RRL..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..RRL.....................................LLR..RRR..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..LLL..RRL.....................................RLL..RRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR.....................................LLR..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR.....................................LLR..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR.....................................LRR..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR.....................................LRR..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..LRR.....................................LLR..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..LRR.....................................LLR..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL.....................................LLR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL.....................................LLR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL.....................................RLL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL.....................................RLL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR.....................................LLR..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR.....................................LLR..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR.....................................LRR..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR.....................................LRR..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..LRR.....................................LLR..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..LRR.....................................LLR..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................LLR..LRR..LRR........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................LLR..RRL..LRR........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................LRR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................LRR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................RLL..LRR..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................RLL..RRL..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................RRL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL.....................................RRL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL.....................................LLR..LRR..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL.....................................LLR..RRL..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL.....................................RLL..LRR..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL.....................................RLL..RRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..LLR.....................................LLR..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..LLR.....................................LRR..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..LRR.....................................LLR..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL.....................................LLR..LRL..LRR........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL.....................................LRR..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL.....................................RLL..LRL..RRL........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL.....................................RRL..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..RRL.....................................LLR..LRL..LLR........................................................', 'ULFRBD'),
             ('...............................RRL..RLR..RRL.....................................RLL..LRL..RLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................LLL..RRR..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................LRL..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................RLR..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL.....................................RRR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LRL.....................................LLL..RRR..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..LRL.....................................RLR..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..RLR.....................................LLL..RRR..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..RLR.....................................LRL..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR.....................................LLL..RRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL.....................................LLL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL.....................................LLL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL.....................................RLR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL.....................................RLR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR.....................................LLL..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR.....................................LLL..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR.....................................LRL..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR.....................................LRL..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..RRR.....................................LLL..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..LLR..RRR.....................................LLL..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................LLL..LRR..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................LLL..RRL..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................LRL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................LRL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................RLR..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................RLR..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................RRR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL.....................................RRR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL.....................................LLL..LRR..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL.....................................LLL..RRL..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL.....................................RLR..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL.....................................RLR..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR.....................................LLL..LRR..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR.....................................LLL..RRL..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR.....................................LRL..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR.....................................LRL..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..RRR.....................................LLL..LRR..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLL..RRR.....................................LLL..RRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL.....................................LLL..LRL..RRR........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL.....................................LRL..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL.....................................RLR..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL.....................................RRR..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..LRL.....................................LLL..LRL..RLR........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..LRL.....................................RLR..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..RLR.....................................LLL..LRL..LRL........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..RLR.....................................LRL..LRL..LLL........................................................', 'ULFRBD'),
             ('...............................RRR..RLR..RRR.....................................LLL..LRL..LLL........................................................', 'ULFRBD'),
            )
        )


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
            'lookup-table-5x5x5-step902-EO-outer-orbit.txt',
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


class Build555EdgeOrientInnerOrbit(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-EO-inner-orbit',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step903-EO-inner-orbit.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . U . .
            . . . . .
            U . . . U
            . . . . .
            . . U . .

 . . U . .  . . U . .  . . U . .  . . U . .
 . . . . .  . . . . .  . . . . .  . . . . .
 U . . . U  U . . . U  U . . . U  U . . . U
 . . . . .  . . . . .  . . . . .  . . . . .
 . . U . .  . . U . .  . . U . .  . . U . .

            . . U . .
            . . . . .
            U . . . U
            . . . . .
            . . U . .""", "ascii"),)
        )


# dwalton
class StartingStatesBuild555Phase4Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-phase4-centers',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'", "Fw2",
             "Bw", "Bw'", "Bw2",
             "Lw", "Lw'", "Lw2",
             "Rw", "Rw'", "Rw2",
             "L", "L'",
             "R", "R'",
             "F", "F'",
             "B", "B'",
            ),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step41-phase4-centers.txt',
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
            . . . . .""", "ascii"),),
        )


class Build555Phase4Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-phase4-centers',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step41-phase4-centers.txt',
            False, # store_as_hex

            # starting cubes
            (
             ('...............................LLL..LLL..LLL............BBB..FFF..BBB............RRR..RRR..RRR............FFF..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BBB..FFF..FFF............RRR..RRR..RRR............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............BBB..FFF..FFF............RRR..RRR..RRR............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFF..FFF..BBB............RRR..RRR..RRR............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFF..FFF..BBB............RRR..RRR..RRR............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BBB..FFF..BBB............LLL..RRR..RRR............FFF..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BBB..FFF..BBB............RRR..RRR..LLL............FFF..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BBB..FFF..FFF............LLL..RRR..RRR............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BBB..FFF..FFF............LLL..RRR..RRR............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BBB..FFF..FFF............RRR..RRR..LLL............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............BBB..FFF..FFF............RRR..RRR..LLL............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..BBB............LLL..RRR..RRR............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..BBB............LLL..RRR..RRR............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..BBB............RRR..RRR..LLL............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..BBB............RRR..RRR..LLL............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............LLL..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............RRR..RRR..LLL............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BBB..FFF..BBB............LLL..RRR..RRR............FFF..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BBB..FFF..BBB............RRR..RRR..LLL............FFF..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BBB..FFF..FFF............LLL..RRR..RRR............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BBB..FFF..FFF............LLL..RRR..RRR............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BBB..FFF..FFF............RRR..RRR..LLL............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............BBB..FFF..FFF............RRR..RRR..LLL............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..BBB............LLL..RRR..RRR............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..BBB............LLL..RRR..RRR............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..BBB............RRR..RRR..LLL............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..BBB............RRR..RRR..LLL............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............LLL..RRR..RRR............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............RRR..RRR..LLL............BBB..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............BBB..FFF..BBB............LLL..RRR..LLL............FFF..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............BBB..FFF..FFF............LLL..RRR..LLL............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............BBB..FFF..FFF............LLL..RRR..LLL............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............FFF..FFF..BBB............LLL..RRR..LLL............BBB..BBB..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............FFF..FFF..BBB............LLL..RRR..LLL............FFF..BBB..BBB...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............FFF..FFF..FFF............LLL..RRR..LLL............BBB..BBB..BBB...............................', 'ULFRBD'),
            )
        )


class Build555Phase4Wings(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-phase4-wings',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step42-phase4-wings.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . x . x .
            x . . . x
            . . . . .
            x . . . x
            . x . x .

 . x . x .  . x . x .  . x . x .  . x . x .
 L . . . L  L . . . L  L . . . L  L . . . L
 . . . . .  . . . . .  . . . . .  . . . . .
 L . . . L  L . . . L  L . . . L  L . . . L
 . x . x .  . x . x .  . x . x .  . x . x .

            . x . x .
            x . . . x
            . . . . .
            x . . . x
            . x . x .""", "ascii"),),
        )


class Build555Phase4Midges(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-phase4-midges',

            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'",
             "L", "L'",
             "R", "R'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step42-phase4-midges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . x . .
            . . . . .
            x . . . x
            . . . . .
            . . x . .

 . . x . .  . . x . .  . . x . .  . . x . .
 . . . . .  . . . . .  . . . . .  . . . . .
 L . . . L  L . . . L  L . . . L  L . . . L
 . . . . .  . . . . .  . . . . .  . . . . .
 . . x . .  . . x . .  . . x . .  . . x . .

            . . x . .
            . . . . .
            x . . . x
            . . . . .
            . . x . .  """, "ascii"),),
        )

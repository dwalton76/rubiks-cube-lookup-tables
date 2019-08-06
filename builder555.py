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


# =====================================
# Stage LR centers to one of 432 states
# =====================================
class StartingStates555LRCenterStage432XCentersOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-432-x-centers-only',
            (), # illegal moves
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step41-LR-centers-stage-432-x-centers-only.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . F . F .  . R . R .  . F . F .
 . . L . .  . . F . .  . . R . .  . . F . .
 . L . L .  . F . F .  . R . R .  . F . F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),),
            legal_moves = (
                "L2", "R2",
                "Uw2", "Dw2", "Fw2", "Bw2",
            )
        )

class Build555LRCenterStage432XCentersOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-432-x-centers-only',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step41-LR-centers-stage-432-x-centers-only.txt',
            False, # store_as_hex

            # starting cubes
            (('...............................L.L...L...L.L............F.F...F...F.F............R.R...R...R.R............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................L.L...L...R.R............F.F...F...F.F............L.L...R...R.R............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................L.L...L...R.R............F.F...F...F.F............R.R...R...L.L............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................L.R...L...L.R............F.F...F...F.F............L.R...R...L.R............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................L.R...L...L.R............F.F...F...F.F............R.L...R...R.L............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................L.R...L...R.L............F.F...F...F.F............R.L...R...L.R............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................R.L...L...L.R............F.F...F...F.F............L.R...R...R.L............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................R.L...L...R.L............F.F...F...F.F............L.R...R...L.R............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................R.L...L...R.L............F.F...F...F.F............R.L...R...R.L............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................R.R...L...L.L............F.F...F...F.F............L.L...R...R.R............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................R.R...L...L.L............F.F...F...F.F............R.R...R...L.L............F.F...F...F.F...............................', 'ULFRBD'),
             ('...............................R.R...L...R.R............F.F...F...F.F............L.L...R...L.L............F.F...F...F.F...............................', 'ULFRBD'))
        )


class StartingStates555LRCenterStage432TCentersOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-432-t-centers-only',
            (), # illegal moves
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step42-LR-centers-stage-432-t-centers-only.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . L . .  . . F . .  . . R . .  . . F . .
 . L L L .  . F F F .  . R R R .  . F F F .
 . . L . .  . . F . .  . . R . .  . . F . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),),
            legal_moves = (
                "L2", "R2",
                "Uw2", "Dw2", "Fw2", "Bw2",
            )
        )

class Build555LRCenterStage432TCentersOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-432-t-centers-only',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step42-LR-centers-stage-432-t-centers-only.txt',
            False, # store_as_hex

            # starting cubes
            (('................................L...LLL...L..............F...FFF...F..............R...RRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLL...R..............F...FFF...F..............L...RRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLL...R..............F...FFF...F..............R...RRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLR...L..............F...FFF...F..............R...LRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLR...L..............F...FFF...F..............R...RRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLR...R..............F...FFF...F..............L...LRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLR...R..............F...FFF...F..............L...RRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLR...R..............F...FFF...F..............R...LRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...LLR...R..............F...FFF...F..............R...RRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLL...L..............F...FFF...F..............R...LRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLL...L..............F...FFF...F..............R...RRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLL...R..............F...FFF...F..............L...LRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLL...R..............F...FFF...F..............L...RRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLL...R..............F...FFF...F..............R...LRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLL...R..............F...FFF...F..............R...RRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLR...L..............F...FFF...F..............R...LRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLR...R..............F...FFF...F..............L...LRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................L...RLR...R..............F...FFF...F..............R...LRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLL...L..............F...FFF...F..............L...RRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLL...L..............F...FFF...F..............R...RRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLL...R..............F...FFF...F..............L...RRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLR...L..............F...FFF...F..............L...LRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLR...L..............F...FFF...F..............L...RRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLR...L..............F...FFF...F..............R...LRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLR...L..............F...FFF...F..............R...RRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLR...R..............F...FFF...F..............L...LRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...LLR...R..............F...FFF...F..............L...RRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLL...L..............F...FFF...F..............L...LRR...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLL...L..............F...FFF...F..............L...RRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLL...L..............F...FFF...F..............R...LRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLL...L..............F...FFF...F..............R...RRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLL...R..............F...FFF...F..............L...LRR...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLL...R..............F...FFF...F..............L...RRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLR...L..............F...FFF...F..............L...LRL...R..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLR...L..............F...FFF...F..............R...LRL...L..............F...FFF...F................................', 'ULFRBD'),
             ('................................R...RLR...R..............F...FFF...F..............L...LRL...L..............F...FFF...F................................', 'ULFRBD'))
        )


class Build555LRCenterStage432PairOneEdge(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-432-pair-one-edge',

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
            'lookup-table-5x5x5-step43-LR-centers-stage-432-pair-one-edge.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . U U U .

 . - - - .  . F F F .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii"),

            ("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . F F F .

 . - - - .  . U U U .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii")),

            use_edges_pattern=True,
        )


class StartingStates555LRCenterStage432(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-LR-center-stage-432',
            (), # illegal moves
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step40-LR-centers-stage-432.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . F F F .
 . L L L .  . F F F .  . R R R .  . F F F .
 . L L L .  . F F F .  . R R R .  . F F F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),),
            legal_moves = (
                "L2", "R2",
                "Uw2", "Dw2", "Fw2", "Bw2",
            )
        )


class Build555LRCenterStage432(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-lr-center-stage-432',

            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Lw", "Lw'",
             "Rw", "Rw'"),

            '5x5x5',
            'lookup-table-5x5x5-step40-LR-centers-stage-432.txt',
            False, # store_as_hex

            # starting cubes
            (('...............................LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LRL............FFF..FFF..FFF............RLR..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..LRL............FFF..FFF..FFF............RRR..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RLR............FFF..FFF..FFF............LRL..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RLR............FFF..FFF..FFF............RRR..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............LLL..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............LRL..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............RLR..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLL..RRR............FFF..FFF..FFF............RRR..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..LLL............FFF..FFF..FFF............RRR..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..LLL............FFF..FFF..FFF............RRR..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL............FFF..FFF..FFF............RLR..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL............FFF..FFF..FFF............RLR..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL............FFF..FFF..FFF............RRR..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..LRL............FFF..FFF..FFF............RRR..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR............FFF..FFF..FFF............LRL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR............FFF..FFF..FFF............LRL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR............FFF..FFF..FFF............RRR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RLR............FFF..FFF..FFF............RRR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..LLR..RRR............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..LLL............FFF..FFF..FFF............RRR..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..LLL............FFF..FFF..FFF............RRR..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL............FFF..FFF..FFF............RLR..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL............FFF..FFF..FFF............RLR..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL............FFF..FFF..FFF............RRR..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..LRL............FFF..FFF..FFF............RRR..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR............FFF..FFF..FFF............LRL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR............FFF..FFF..FFF............LRL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR............FFF..FFF..FFF............RRR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RLR............FFF..FFF..FFF............RRR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLL..RRR............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..LLL............FFF..FFF..FFF............RRR..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..LRL............FFF..FFF..FFF............RLR..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..LRL............FFF..FFF..FFF............RRR..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..RLR............FFF..FFF..FFF............LRL..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..RLR............FFF..FFF..FFF............RRR..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR............FFF..FFF..FFF............LLL..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR............FFF..FFF..FFF............LRL..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR............FFF..FFF..FFF............RLR..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLL..RLR..RRR............FFF..FFF..FFF............RRR..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..LLR............FFF..FFF..FFF............LRR..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..LLR............FFF..FFF..FFF............RRL..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR............FFF..FFF..FFF............LLR..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR............FFF..FFF..FFF............LRR..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR............FFF..FFF..FFF............RLL..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..LRR............FFF..FFF..FFF............RRL..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..RLL............FFF..FFF..FFF............RRL..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..RRL............FFF..FFF..FFF............RLL..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLL..RRL............FFF..FFF..FFF............RRL..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFF..FFF..FFF............LRR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFF..FFF..FFF............RRL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..LRR............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..RLL............FFF..FFF..FFF............RRL..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..RLL............FFF..FFF..FFF............RRL..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL............FFF..FFF..FFF............RLL..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL............FFF..FFF..FFF............RLL..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL............FFF..FFF..FFF............RRL..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..LLR..RRL............FFF..FFF..FFF............RRL..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR............FFF..FFF..FFF............LRR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR............FFF..FFF..FFF............LRR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR............FFF..FFF..FFF............RRL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LLR............FFF..FFF..FFF............RRL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..LRR............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..RLL............FFF..FFF..FFF............RRL..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..RLL............FFF..FFF..FFF............RRL..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL............FFF..FFF..FFF............RLL..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL............FFF..FFF..FFF............RLL..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL............FFF..FFF..FFF............RRL..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLL..RRL............FFF..FFF..FFF............RRL..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..LLR............FFF..FFF..FFF............LRR..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..LLR............FFF..FFF..FFF............RRL..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR............FFF..FFF..FFF............LLR..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR............FFF..FFF..FFF............LRR..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR............FFF..FFF..FFF............RLL..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..LRR............FFF..FFF..FFF............RRL..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..RLL............FFF..FFF..FFF............RRL..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..RRL............FFF..FFF..FFF............RLL..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LLR..RLR..RRL............FFF..FFF..FFF............RRL..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..LLL............FFF..FFF..FFF............RLR..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..LRL............FFF..FFF..FFF............RLR..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR............FFF..FFF..FFF............LLL..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR............FFF..FFF..FFF............LRL..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR............FFF..FFF..FFF............RLR..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..RLR............FFF..FFF..FFF............RRR..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..RRR............FFF..FFF..FFF............LLL..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLL..RRR............FFF..FFF..FFF............RLR..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL............FFF..FFF..FFF............RLR..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL............FFF..FFF..FFF............RLR..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL............FFF..FFF..FFF............RRR..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..LLL............FFF..FFF..FFF............RRR..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..LRL............FFF..FFF..FFF............RLR..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..LRL............FFF..FFF..FFF............RLR..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RLR............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR............FFF..FFF..FFF............LLL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR............FFF..FFF..FFF............LLL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR............FFF..FFF..FFF............RLR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..LLR..RRR............FFF..FFF..FFF............RLR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL............FFF..FFF..FFF............RLR..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL............FFF..FFF..FFF............RLR..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL............FFF..FFF..FFF............RRR..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..LLL............FFF..FFF..FFF............RRR..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..LRL............FFF..FFF..FFF............RLR..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..LRL............FFF..FFF..FFF............RLR..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RLR............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR............FFF..FFF..FFF............LLL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR............FFF..FFF..FFF............LLL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR............FFF..FFF..FFF............RLR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLL..RRR............FFF..FFF..FFF............RLR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..LLL............FFF..FFF..FFF............RLR..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..LLL............FFF..FFF..FFF............RRR..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..LRL............FFF..FFF..FFF............RLR..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR............FFF..FFF..FFF............LLL..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR............FFF..FFF..FFF............LRL..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR............FFF..FFF..FFF............RLR..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..RLR............FFF..FFF..FFF............RRR..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..RRR............FFF..FFF..FFF............LLL..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRL..RLR..RRR............FFF..FFF..FFF............RLR..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR............FFF..FFF..FFF............LLR..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR............FFF..FFF..FFF............LRR..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR............FFF..FFF..FFF............RLL..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..LLR............FFF..FFF..FFF............RRL..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..LRR............FFF..FFF..FFF............LLR..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..LRR............FFF..FFF..FFF............RLL..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..RLL............FFF..FFF..FFF............RLL..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..RLL............FFF..FFF..FFF............RRL..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLL..RRL............FFF..FFF..FFF............RLL..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR............FFF..FFF..FFF............LLR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR............FFF..FFF..FFF............LLR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR............FFF..FFF..FFF............RLL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..LRR............FFF..FFF..FFF............RLL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL............FFF..FFF..FFF............RLL..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL............FFF..FFF..FFF............RLL..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL............FFF..FFF..FFF............RRL..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..RLL............FFF..FFF..FFF............RRL..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..RRL............FFF..FFF..FFF............RLL..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..LLR..RRL............FFF..FFF..FFF............RLL..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LLR............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR............FFF..FFF..FFF............LLR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR............FFF..FFF..FFF............LLR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR............FFF..FFF..FFF............RLL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..LRR............FFF..FFF..FFF............RLL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL............FFF..FFF..FFF............RLL..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL............FFF..FFF..FFF............RLL..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL............FFF..FFF..FFF............RRL..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..RLL............FFF..FFF..FFF............RRL..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..RRL............FFF..FFF..FFF............RLL..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLL..RRL............FFF..FFF..FFF............RLL..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR............FFF..FFF..FFF............LLR..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR............FFF..FFF..FFF............LRR..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR............FFF..FFF..FFF............RLL..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..LLR............FFF..FFF..FFF............RRL..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..LRR............FFF..FFF..FFF............LLR..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..LRR............FFF..FFF..FFF............RLL..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..RLL............FFF..FFF..FFF............RLL..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..RLL............FFF..FFF..FFF............RRL..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................LRR..RLR..RRL............FFF..FFF..FFF............RLL..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..LLR............FFF..FFF..FFF............LRR..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..LRR............FFF..FFF..FFF............LLR..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..LRR............FFF..FFF..FFF............LRR..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..RLL............FFF..FFF..FFF............LRR..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..RLL............FFF..FFF..FFF............RRL..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL............FFF..FFF..FFF............LLR..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL............FFF..FFF..FFF............LRR..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL............FFF..FFF..FFF............RLL..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLL..RRL............FFF..FFF..FFF............RRL..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..LLR............FFF..FFF..FFF............LRR..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..LLR............FFF..FFF..FFF............LRR..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR............FFF..FFF..FFF............LLR..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR............FFF..FFF..FFF............LLR..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR............FFF..FFF..FFF............LRR..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..LRR............FFF..FFF..FFF............LRR..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL............FFF..FFF..FFF............LRR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL............FFF..FFF..FFF............LRR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL............FFF..FFF..FFF............RRL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RLL............FFF..FFF..FFF............RRL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..LLR..RRL............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..LLR............FFF..FFF..FFF............LRR..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..LLR............FFF..FFF..FFF............LRR..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR............FFF..FFF..FFF............LLR..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR............FFF..FFF..FFF............LLR..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR............FFF..FFF..FFF............LRR..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..LRR............FFF..FFF..FFF............LRR..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFF..FFF..FFF............LRR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFF..FFF..FFF............RRL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLL..RRL............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..LLR............FFF..FFF..FFF............LRR..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..LRR............FFF..FFF..FFF............LLR..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..LRR............FFF..FFF..FFF............LRR..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..RLL............FFF..FFF..FFF............LRR..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..RLL............FFF..FFF..FFF............RRL..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL............FFF..FFF..FFF............LLR..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL............FFF..FFF..FFF............LRR..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL............FFF..FFF..FFF............RLL..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLL..RLR..RRL............FFF..FFF..FFF............RRL..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..LLL............FFF..FFF..FFF............LRL..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..LLL............FFF..FFF..FFF............RRR..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL............FFF..FFF..FFF............LLL..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL............FFF..FFF..FFF............LRL..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL............FFF..FFF..FFF............RLR..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..LRL............FFF..FFF..FFF............RRR..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..RLR............FFF..FFF..FFF............LRL..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..RRR............FFF..FFF..FFF............LLL..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLL..RRR............FFF..FFF..FFF............LRL..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL............FFF..FFF..FFF............LRL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL............FFF..FFF..FFF............LRL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL............FFF..FFF..FFF............RRR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LLL............FFF..FFF..FFF............RRR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..LRL............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..RLR............FFF..FFF..FFF............LRL..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..RLR............FFF..FFF..FFF............LRL..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR............FFF..FFF..FFF............LLL..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR............FFF..FFF..FFF............LLL..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR............FFF..FFF..FFF............LRL..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..LLR..RRR............FFF..FFF..FFF............LRL..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL............FFF..FFF..FFF............LRL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL............FFF..FFF..FFF............LRL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL............FFF..FFF..FFF............RRR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LLL............FFF..FFF..FFF............RRR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..LRL............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..RLR............FFF..FFF..FFF............LRL..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..RLR............FFF..FFF..FFF............LRL..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR............FFF..FFF..FFF............LLL..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR............FFF..FFF..FFF............LLL..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR............FFF..FFF..FFF............LRL..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLL..RRR............FFF..FFF..FFF............LRL..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..LLL............FFF..FFF..FFF............LRL..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..LLL............FFF..FFF..FFF............RRR..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL............FFF..FFF..FFF............LLL..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL............FFF..FFF..FFF............LRL..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL............FFF..FFF..FFF............RLR..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..LRL............FFF..FFF..FFF............RRR..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RRR............FFF..FFF..FFF............LLL..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RLR..RLR..RRR............FFF..FFF..FFF............LRL..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..LLR............FFF..FFF..FFF............LLR..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..LLR............FFF..FFF..FFF............LRR..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..LRR............FFF..FFF..FFF............LLR..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL............FFF..FFF..FFF............LLR..RRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL............FFF..FFF..FFF............LRR..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL............FFF..FFF..FFF............RLL..RRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..RLL............FFF..FFF..FFF............RRL..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..RRL............FFF..FFF..FFF............LLR..RRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLL..RRL............FFF..FFF..FFF............RLL..RRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR............FFF..FFF..FFF............LLR..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR............FFF..FFF..FFF............LLR..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR............FFF..FFF..FFF............LRR..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..LLR............FFF..FFF..FFF............LRR..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..LRR............FFF..FFF..FFF............LLR..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..LRR............FFF..FFF..FFF............LLR..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RLL............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL............FFF..FFF..FFF............LLR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL............FFF..FFF..FFF............LLR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL............FFF..FFF..FFF............RLL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..LLR..RRL............FFF..FFF..FFF............RLL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR............FFF..FFF..FFF............LLR..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR............FFF..FFF..FFF............LLR..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR............FFF..FFF..FFF............LRR..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..LLR............FFF..FFF..FFF............LRR..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..LRR............FFF..FFF..FFF............LLR..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..LRR............FFF..FFF..FFF............LLR..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............LLR..LRR..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............LLR..RRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............LRR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............RLL..LRR..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............RLL..RRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............RRL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL............FFF..FFF..FFF............LLR..LRR..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL............FFF..FFF..FFF............LLR..RRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL............FFF..FFF..FFF............RLL..LRR..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLL..RRL............FFF..FFF..FFF............RLL..RRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..LLR............FFF..FFF..FFF............LLR..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..LLR............FFF..FFF..FFF............LRR..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..LRR............FFF..FFF..FFF............LLR..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL............FFF..FFF..FFF............LLR..LRL..LRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL............FFF..FFF..FFF............LRR..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL............FFF..FFF..FFF............RLL..LRL..RRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..RLL............FFF..FFF..FFF............RRL..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..RRL............FFF..FFF..FFF............LLR..LRL..LLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRL..RLR..RRL............FFF..FFF..FFF............RLL..LRL..RLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............LLL..RRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............LRL..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............RLR..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LLL............FFF..FFF..FFF............RRR..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LRL............FFF..FFF..FFF............LLL..RRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..LRL............FFF..FFF..FFF............RLR..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RLR............FFF..FFF..FFF............LLL..RRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RLR............FFF..FFF..FFF............LRL..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLL..RRR............FFF..FFF..FFF............LLL..RRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LLL............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL............FFF..FFF..FFF............LLL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL............FFF..FFF..FFF............LLL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL............FFF..FFF..FFF............RLR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..LRL............FFF..FFF..FFF............RLR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR............FFF..FFF..FFF............LLL..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR............FFF..FFF..FFF............LLL..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR............FFF..FFF..FFF............LRL..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..RLR............FFF..FFF..FFF............LRL..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..RRR............FFF..FFF..FFF............LLL..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..LLR..RRR............FFF..FFF..FFF............LLL..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............LLL..LRR..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............LLL..RRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............LRL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............LRL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............RLR..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............RLR..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............RRR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LLL............FFF..FFF..FFF............RRR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL............FFF..FFF..FFF............LLL..LRR..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL............FFF..FFF..FFF............LLL..RRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL............FFF..FFF..FFF............RLR..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..LRL............FFF..FFF..FFF............RLR..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR............FFF..FFF..FFF............LLL..LRR..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR............FFF..FFF..FFF............LLL..RRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR............FFF..FFF..FFF............LRL..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..RLR............FFF..FFF..FFF............LRL..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..RRR............FFF..FFF..FFF............LLL..LRR..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLL..RRR............FFF..FFF..FFF............LLL..RRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL............FFF..FFF..FFF............LLL..LRL..RRR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL............FFF..FFF..FFF............LRL..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL............FFF..FFF..FFF............RLR..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..LLL............FFF..FFF..FFF............RRR..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..LRL............FFF..FFF..FFF............LLL..LRL..RLR............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..LRL............FFF..FFF..FFF............RLR..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..RLR............FFF..FFF..FFF............LLL..LRL..LRL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'),
             ('...............................RRR..RLR..RRR............FFF..FFF..FFF............LLL..LRL..LLL............FFF..FFF..FFF...............................', 'ULFRBD'))
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
# EO remaining 8 edges via slices so they can be
# solved without L L' R R' F F' B B'
# ==============================================
class StartingStates555XPlaneYPlaneEdgesOrientEdgesOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient-edges-only',

            # illegal moves
            (),
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step351-x-plane-y-plane-edges-orient-edges-only.txt',
            False, # store_as_hex
            (("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D . . . U  U . . . D  D . . . U
 D . . . D  D . . . D  D . . . D  D . . . D
 D . . . U  U . . . D  D . . . U  U . . . D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii"),),

            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",

                "2U2", "2D2",
                "2L2",
                "2R2",
            )
        )


class Build555XPlaneYPlaneEdgesOrientEdgesOnly(BFS):

    def __init__(self):
        from builder555ss import starting_states_step351
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient-edges-only',

            # illegal moves
            (),
            '5x5x5',
            'lookup-table-5x5x5-step351-x-plane-y-plane-edges-orient-edges-only.txt',
            False, # store_as_hex
            starting_states_step351,
            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",

                "2U2", "2D2",
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
            )
        )


class Build555XPlaneYPlaneEdgesOrientStageCentersOnly(BFS):
    """
    (16!/(8!*8!))^2 = 165,636,900 states

    We can only get to 6,370,650 of them though
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient-centers-only',

            # illegal moves
            (),
            '5x5x5',
            'lookup-table-5x5x5-step352-x-plane-y-plane-edges-orient-centers-only.txt',
            False, # store_as_hex
            (("""
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .""", "ascii"),),

            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",

                "2U2", "2D2",
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
            )
        )


class Build555XPlaneYPlaneEdgesOrientPairOneEdge(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient-one-edge',

            # illegal moves
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
            ),

            '5x5x5',
            'lookup-table-5x5x5-step353-x-plane-y-plane-edges-orient-pair-one-edge.txt',
            False, # store_as_hex

            # starting cubes
            (("""
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . U U U .

 . - - - .  . F F F .  . - - - .  . - - - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
        )


class StartingStates555XPlaneYPlaneEdgesOrient(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient',

            # illegal moves
            (),
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step350-x-plane-y-plane-edges-orient.txt',
            False, # store_as_hex
            (("""
            . U U D .
            U U U U D
            D U U U D
            D U U U U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D F F F U  U . . . D  D F F F U
 D . . . D  D F F F D  D . . . D  D F F F D
 D . . . U  U F F F D  D . . . U  U F F F D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U U U U D
            D U U U D
            D U U U U
            . D U U .""", "ascii"),),

            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",

                "2U2", "2D2",
                "2L2",
                "2R2",
            )
        )

class Build555XPlaneYPlaneEdgesOrient(BFS):
    """
    """

    def __init__(self):
        from builder555ss import starting_states_step350
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient',

            # illegal moves
            (),
            '5x5x5',
            'lookup-table-5x5x5-step350-x-plane-y-plane-edges-orient.txt',
            False, # store_as_hex
            starting_states_step350,
            use_centers_then_edges=True,
            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",

                "2U2", "2D2",
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",
            )
        )


# step360 starts here
class Build555XPlaneYPlaneEdgesOrientFBCentersEdgesOnly(BFS):
    """
    To build the ascii starting_state for this table we
    - took a solved cube
    - applied L' R
    - got the following

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D . . . U  U . . . D  D . . . U
 D . . . D  D . . . D  D . . . D  D . . . D
 D . . . U  U . . . D  D . . . U  U . . . D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

    We did this because when this phase runs the LR centers are in horizontal bars with
    the z-plane edges paired.  After this phase we will do a L R' to move the LR centers
    to vertical bars with the x-plane edges paired.  After that L R' we need the remaining
    8-edges to be EOed.  So that is why we are starting with the following table.

    I Xed out the z-plane edges...no need to track those
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient-fb-centers-edges-only',
            # illegal moves
            (),
            '5x5x5',
            'lookup-table-5x5x5-step361-x-plane-y-plane-edges-orient-fb-centers-edges-only.txt',
            False, # store_as_hex
            (("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D . . . U  U . . . D  D . . . U
 D . . . D  D . . . D  D . . . D  D . . . D
 D . . . U  U . . . D  D . . . U  U . . . D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii"),),

            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",
            )
        )


class Build555XPlaneYPlaneEdgesOrientFBCentersOnly(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient-fb-centers',

            # illegal moves
            (),
            '5x5x5',
            'lookup-table-5x5x5-step362-x-plane-y-plane-edges-orient-fb-centers-only.txt',
            False, # store_as_hex
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
            . . . . .""", "ascii"),

            ("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . B F B .  . . . . .  . F B F .
 . . . . .  . B F B .  . . . . .  . F B F .
 . . . . .  . B F B .  . . . . .  . F B F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),

            ("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . B F F .  . . . . .  . B B F .
 . . . . .  . B F F .  . . . . .  . B B F .
 . . . . .  . B F F .  . . . . .  . B B F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),

            ("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . B F F .  . . . . .  . F B B .
 . . . . .  . B F F .  . . . . .  . F B B .
 . . . . .  . B F F .  . . . . .  . F B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),

            ("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F B .  . . . . .  . B B F .
 . . . . .  . F F B .  . . . . .  . B B F .
 . . . . .  . F F B .  . . . . .  . B B F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii"),

            ("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F B .  . . . . .  . F B B .
 . . . . .  . F F B .  . . . . .  . F B B .
 . . . . .  . F F B .  . . . . .  . F B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""", "ascii")),
            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",
            )
        )


class Build555XPlaneYPlaneEdgesOrientFBCenters(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-x-plane-y-plane-edges-orient-fb-centers',

            # illegal moves
            (),
            '5x5x5',
            'lookup-table-5x5x5-step360-x-plane-y-plane-edges-orient-fb-centers.txt',
            False, # store_as_hex
            (("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D F F F U  U . . . D  D B B B U
 D . . . D  D F F F D  D . . . D  D B B B D
 D . . . U  U F F F D  D . . . U  U B B B D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii"),

            ("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D B F B U  U . . . D  D F B F U
 D . . . D  D B F B D  D . . . D  D F B F D
 D . . . U  U B F B D  D . . . U  U F B F D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii"),

            ("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D B F F U  U . . . D  D B B F U
 D . . . D  D B F F D  D . . . D  D B B F D
 D . . . U  U B F F D  D . . . U  U B B F D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii"),

            ("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D B F F U  U . . . D  D F B B U
 D . . . D  D B F F D  D . . . D  D F B B D
 D . . . U  U B F F D  D . . . U  U F B B D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii"),

            ("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D F F B U  U . . . D  D B B F U
 D . . . D  D F F B D  D . . . D  D B B F D
 D . . . U  U F F B D  D . . . U  U B B F D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii"),

            ("""
            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .

 . U D D .  . D U U .  . U D D .  . D U U .
 U . . . D  D F F B U  U . . . D  D F B B U
 D . . . D  D F F B D  D . . . D  D F B B D
 D . . . U  U F F B D  D . . . U  U F B B D
 . D D U .  . U U D .  . D D U .  . U U D .

            . U U D .
            U . . . D
            D . . . D
            D . . . U
            . D U U .""", "ascii")),

            use_centers_then_edges=True,
            legal_moves=(
                "F", "F'", "F2",
                "B", "B'", "B2",
                "L2", "R2", "U2", "B2",

                "Uw2", "Dw2",
                "Lw2", "Rw2",
            )
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


# ================================
# six-edges (aka horseshoe) tables
# ================================
class Build555EdgesStageFirstSix(BFS):
    """
    (24!/(12!*12!)) * (12!/(6!*6!)) = 2,498,640,144 states
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-stage-first-six',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step100-stage-first-six-edges.txt',
            False, # store_as_hex
            (
            # Horseshoes where 4-edges are on top, 2-edges are on bottom
            ("""
            - L L L -
            L U U U L
            L U U U L
            L U U U L
            - L L L -

 - L L L -  - L L L -  - L L L -  - L L L -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - - - - -  - L L L -  - - - - -  - L L L -

            - L L L -
            - D D D -
            - D D D -
            - D D D -
            - L L L -""", "ascii"),

            ("""
            - L L L -
            L U U U L
            L U U U L
            L U U U L
            - L L L -

 - L L L -  - L L L -  - L L L -  - L L L -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - - - - -  - L L L -  - - - - -

            - - - - -
            L D D D L
            L D D D L
            L D D D L
            - - - - -""", "ascii"),

            # Horseshoes where 4-edges are on bottom, 2-edges are on top
            ("""
            - L L L -
            - U U U -
            - U U U -
            - U U U -
            - L L L -

 - - - - -  - L L L -  - - - - -  - L L L -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - L L L -  - L L L -  - L L L -

            - L L L -
            L D D D L
            L D D D L
            L D D D L
            - L L L -""", "ascii"),

            ("""
            - - - - -
            L U U U L
            L U U U L
            L U U U L
            - - - - -

 - L L L -  - - - - -  - L L L -  - - - - -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - L L L -  - L L L -  - L L L -

            - L L L -
            L D D D L
            L D D D L
            L D D D L
            - L L L -""", "ascii"),

            # Horseshoes where 4-edges are on left, 2-edges are on right
            ("""
            - - - - -
            L U U U -
            L U U U -
            L U U U -
            - - - - -

 - L L L -  - - - - -  - - - - -  - - - - -
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 - L L L -  - - - - -  - - - - -  - - - - -

            - - - - -
            L D D D -
            L D D D -
            L D D D -
            - - - - -""", "ascii"),

            ("""
            - - - - -
            L U U U L
            L U U U L
            L U U U L
            - - - - -

 - L L L -  - - - - -  - L L L -  - - - - -
 L L L L L  L F F F -  - R R R -  - B B B L
 L L L L L  L F F F -  - R R R -  - B B B L
 L L L L L  L F F F -  - R R R -  - B B B L
 - L L L -  - - - - -  - L L L -  - - - - -

            - - - - -
            L D D D L
            L D D D L
            L D D D L
            - - - - -""", "ascii"),

            # Horseshoes where 4-edges are on right, 2-edges are on left
            ("""
            - - - - -
            - U U U L
            - U U U L
            - U U U L
            - - - - -

 - - - - -  - - - - -  - L L L -  - - - - -
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 - - - - -  - - - - -  - L L L -  - - - - -

            - - - - -
            - D D D L
            - D D D L
            - D D D L
            - - - - -""", "ascii"),

            ("""
            - - - - -
            L U U U L
            L U U U L
            L U U U L
            - - - - -

 - L L L -  - - - - -  - L L L -  - - - - -
 - L L L -  - F F F L  L R R R L  L B B B -
 - L L L -  - F F F L  L R R R L  L B B B -
 - L L L -  - F F F L  L R R R L  L B B B -
 - L L L -  - - - - -  - L L L -  - - - - -

            - - - - -
            L D D D L
            L D D D L
            L D D D L
            - - - - -""", "ascii"),

            # Horseshoes where 4-edges are on front, 2-edges are on back
            ("""
            - - - - -
            - U U U -
            - U U U -
            - U U U -
            - L L L -

 - - - - -  - L L L -  - - - - -  - - - - -
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 - - - - -  - L L L -  - - - - -  - - - - -

            - L L L -
            - D D D -
            - D D D -
            - D D D -
            - - - - -""", "ascii"),

            ("""
            - L L L -
            - U U U -
            - U U U -
            - U U U -
            - L L L -

 - - - - -  - L L L -  - - - - -  - L L L -
 - L L L L  L F F F L  L R R R -  - B B B -
 - L L L L  L F F F L  L R R R -  - B B B -
 - L L L L  L F F F L  L R R R -  - B B B -
 - - - - -  - L L L -  - - - - -  - L L L -

            - L L L -
            - D D D -
            - D D D -
            - D D D -
            - L L L -""", "ascii"),

            # Horseshoes where 4-edges are on back, 2-edges are on front
            ("""
            - L L L -
            - U U U -
            - U U U -
            - U U U -
            - - - - -

 - - - - -  - - - - -  - - - - -  - L L L -
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 - - - - -  - - - - -  - - - - -  - L L L -

            - - - - -
            - D D D -
            - D D D -
            - D D D -
            - L L L -""", "ascii"),

            ("""
            - L L L -
            - U U U -
            - U U U -
            - U U U -
            - L L L -

 - - - - -  - L L L -  - - - - -  - L L L -
 L L L L -  - F F F -  - R R R L  L B B B L
 L L L L -  - F F F -  - R R R L  L B B B L
 L L L L -  - F F F -  - R R R L  L B B B L
 - - - - -  - L L L -  - - - - -  - L L L -

            - L L L -
            - D D D -
            - D D D -
            - D D D -
            - L L L -""", "ascii"),
            )
        )


class Build555EdgesSolveFirstSix(BFS):
    """
    12! = 479,001,600 states
    """
    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-solve-first-six',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step100-solve-first-six-edges.txt',
            False, # store_as_hex
            (
            ("""
            - U U U -
            U U U U U
            U U U U U
            U U U U U
            - U U U -

 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - - - - -  - F F F -  - - - - -  - B B B -

            - D D D -
            - D D D -
            - D D D -
            - D D D -
            - D D D -""", "ascii"),

            ("""
            - U U U -
            U F F F U
            U F F F U
            U F F F U
            - U U U -

 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - D D D -  - R R R -  - U U U -
 - L L L -  - D D D -  - R R R -  - U U U -
 - L L L -  - D D D -  - R R R -  - U U U -
 - - - - -  - F F F -  - - - - -  - B B B -

            - D D D -
            - B B B -
            - B B B -
            - B B B -
            - D D D -""", "ascii"),

            ("""
            - U U U -
            U D D D U
            U D D D U
            U D D D U
            - U U U -

 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - B B B -  - R R R -  - F F F -
 - L L L -  - B B B -  - R R R -  - F F F -
 - L L L -  - B B B -  - R R R -  - F F F -
 - - - - -  - F F F -  - - - - -  - B B B -

            - D D D -
            - U U U -
            - U U U -
            - U U U -
            - D D D -""", "ascii"),

            ("""
            - U U U -
            U B B B U
            U B B B U
            U B B B U
            - U U U -

 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - U U U -  - R R R -  - D D D -
 - L L L -  - U U U -  - R R R -  - D D D -
 - L L L -  - U U U -  - R R R -  - D D D -
 - - - - -  - F F F -  - - - - -  - B B B -

            - D D D -
            - F F F -
            - F F F -
            - F F F -
            - D D D -""", "ascii")),
            use_edges_pattern=True,
            legal_moves = (
                "U", "U'", "U2",
                "F2", "B2", "D2",
                "2L", "2L'", "2L2",
                "2R", "2R'", "2R2",

                # middle layer slices
                #"3L", "3L'", "3L2",
            )
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


# =========================================
# solving edges when centers are NOT paired
# =========================================
# today we do the following (this is fairly new)
'''
phase 1 - stage UD
    10 moves

phase 2 - stage LR to 432 but with 4-edges EO
    11 moves

phase 3 - LR to horizontal bars and pair 4-edges in z-plane

    - A 2-edge prune table is
        (12*11)^2 is how many states the wings can be in
        12!/(10!*2!) is how many states the midges can be in
        (12*11)^2 * 12!/(10!*2!) = 1,149,984

    - A 3-edge prune table is
        (12*11*10)^2 is how many states the wings can be in
        12!/(9!*3!) is how many states the midges can be in
        (12*11*10)^2 * 12!/(9!*3!) = 383,328,000

    - A 4-edge prune table is
        (12*11*10*9)^2 * 12!/(8!*4!) = 69,861,528,000

    - 69,861,528,000 * 432 = 30,180,180,096,000 states

    Using a 3-edge pt
    383,328,000/30,180,180,096,000 = 0.000 012

    ~14 moves??? Educated guess based on xyzzy solves here:
    http://cubesolvingprograms.freeforums.net/thread/37/results-5x5x5-fewest-moves-challenge

phase 4 - partialy EO the remaining 8-edges
    There are 900,900 EO states but phase 5 can only get to 343,000 of them so put the
    edges into one of those 343,000 states by using slices.  Keep the UD and FB centers
    staged.
    ~5 moves

phase 5 - LR and FB to vertical bars, EO remaining 8 edges via slices so they can be solved without L L' R R' F F' B B'
    - keep z-plane edges paired
    - keep LR in horiztonal bars
    - keep UD and FB staged
    - Two things for wings
        - they must be split into high/low groups
        - they must match the orienation of their midge

    - midges can be in (2^8)/2 = 128 states...maybe???
        I do not think we need to change the midge orientation. As long as we
        are not slicing the middle layer it should not change.

    - edges can be in one of 900,900 states
    - centers can be in one of 6,370,650 states
    - end with L and R moves to put paired edges in x-plane and flip LR horizontal bars to vertical
    ~10 moves?

phase 6 - solve all centers and pair all edges
    - 6 x 6 x 4900 x (8!^2)/2 = 143,386,951,680,000
    - (8!^2)/2 = 812851200
    - 812851200/143386951680000 = 0.000 005
    ~16 moves???

~66 moves to reduce to 333
'''


# =====================================
# solving edges when centers are paired
# =====================================
'''
phase 1 - stage 1st L4E group
phase 2 - solve 1st L4E group
phase 3 - stage 2nd L4E group
phase 4 - solve 2nd L4E group
phase 5 - solve 3rd L4E group

This normally takes ~52 steps
'''


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

    383,328,000 / (432 * 4900 * 69,861,528,000) = 0.000 000 002
    That is just brutal

phase 5
    pair last 8 edges
    solve all centers

    8!^2/2 = 812,851,200 edge states
    6 * 6 * 4900 = 176,400 center states

    -16 moves

that would be ~61 moves
'''

# brainstorm #2
'''
If phase2 were to also solve the LR centers (should be cheap) that makes phase3
doable. We would just need to IDA all 2.7million outer orbit EO solutions. That
might take 6 months though.

phase4 is just insane...this IDA would take hours...maybe xyzzy did just that.
What if we L4Eed all 3 planes here?
    FB and UD centers would need to go to one of 432 states
    4900 FB centers * 4900 UD centers = 24,010,000

    (12!(4!*4!*4!)) ^3 = 41,601,569,625,000
    not feasible


What if we L4Eed x-plane here?
    FB centers to one of 432 states

    4900 FB center states
    (12!/(4!*8!))^3 = 121,287,375 edge states

phase4b
    LR and FB centers to vertical bars
    432 * 432 states

    pair x-plane edges
    4!^3 = 13824 edge states

    432 * 432 * 13824 = 2579890176

    (432*432)/2579890176 = 0.000 072
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
            'starting-states-lookup-table-5x5x5-step901-LR-center-stage.txt',
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

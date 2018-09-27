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
            . D D D .""", "ascii"),)
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
            . D D D .""", "ascii"),)
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


class Build555Step51(BFS):
    """
    L4E group to x-plane
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
             "L", "L'",
             "R", "R'",
            ),

            '5x5x5',
            'lookup-table-5x5x5-step51.txt',
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



class StartingStates555Step52(BFS):
    """
    LR and FB to vertical bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step52',
            (), # illegal moves
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step52.txt',
            False, # store_as_hex

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
            . . . . .""", "ascii"),),
            legal_moves = (
                "L2", "R2", "F2", "B2",
                "2L2", "2R2", "2F2", "2B2",
            )
        )


class Build555Step52(BFS):
    """
    LR and FB to vertical bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step52',

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
            'lookup-table-5x5x5-step52.txt',
            True, # store_as_hex

            # starting cubes
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


class StartingStates555Step50(BFS):
    """
    LR and FB to vertical bars
    L4E group to x-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step50',
            (), # illegal moves
            '5x5x5',
            'starting-states-lookup-table-5x5x5-step50.txt',
            False, # store_as_hex

            # starting cubes
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
            legal_moves = (
                "L2", "R2", "F2", "B2",
                "2L2", "2R2", "2F2", "2B2",
            )
        )


class Build555Step50(BFS):
    """
    LR and FB to vertical bars
    L4E group to x-plane
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-step50',

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
            'lookup-table-5x5x5-step50.txt',
            True, # store_as_hex

            # starting cubes
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
             ('.xxx.x...xx...xx...x.xxx..xxx.LxLxLLxLxLLxLxL.xxx..xxx.LxFxLLxFxLLxFxL.xxx..xxx.LLxLLLLxLLLLxLL.xxx..xxx.LFxFLLFxFLLFxFL.xxx..xxx.x...xx...xx...x.xxx.', 'ULFRBD')),
            use_centers_then_edges=True
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


class Build555EdgesYPlaneEdgesOnly(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-edges-y-plane-only',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step201-edges-y-plane-edges-only.txt',
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
            use_edges_pattern=True,
            legal_moves = (
                "U", "U'", "U2",
                "D", "D'", "D2",
                "L2", "F2", "R2", "B2",
                "Lw2", "Fw2", "Rw2", "Bw2",
            )
        )


class StartingStates555EdgesYPlaneCentersOnly(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.

    FB centers to solved
    LR centers to vertical bars
    UD centers to horizontal bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-y-plane-centers-only',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step202-edges-y-plane-centers-only.txt',
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
                "2F2", "2B2",
                "U2", "D2", "L2", "R2",
            )
        )


class Build555EdgesYPlaneCentersOnly(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.

    FB centers to solved
    LR centers to vertical bars
    UD centers to horizontal bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-y-plane-centers-only',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step202-edges-y-plane-centers-only.txt',
            False, # store_as_hex

            # starting cubes
            (('......DDD..UUU..DDD............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............UUU..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..DDD............LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..DDD............LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..DDD............RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..DDD............RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..DDD............RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB............UUU..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......DDD..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......DDD..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......DDD..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......DDD..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......DDD..UUU..UUU............RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......DDD..UUU..UUU............RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..DDD............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......UUU..UUU..DDD............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..DDD............LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......UUU..UUU..DDD............LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..DDD............LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......UUU..UUU..DDD............LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..DDD............RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......UUU..UUU..DDD............RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..DDD............RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......UUU..UUU..DDD............RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..DDD............RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB............DDD..DDD..UUU......', 'ULFRBD'),
             ('......UUU..UUU..DDD............RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB............UUU..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD'),
             ('......UUU..UUU..UUU............RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB............DDD..DDD..DDD......', 'ULFRBD')),
            legal_moves = (
                "U", "U'", "U2",
                "D", "D'", "D2",
                "L2", "F2", "R2", "B2",
                "Lw2", "Fw2", "Rw2", "Bw2",
            )
        )


class StartingStates555EdgesYPlane(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.

    FB centers to solved
    LR centers to vertical bars
    UD centers to horizontal bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-y-plane',

            # illegal moves
            (),

            '5x5x5',
            'starting-states-lookup-table-5x5x5-step200-edges-y-plane.txt',
            False, # store_as_hex
            (("""
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
            . D D D .""", "ascii"),),
            legal_moves = (
                "2F2", "2B2",
                "U2", "D2", "L2", "R2",
            )
        )


class Build555EdgesYPlane(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.

    FB centers to solved
    LR centers to vertical bars
    UD centers to horizontal bars
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-y-plane',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step200-edges-y-plane.txt',
            False, # store_as_hex
            (('.UUU.-DDD--UUU--DDD-.UUU..---.-LLL--LLL--LLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRR--RRR--RRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--DDD-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--DDD-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--DDD-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--DDD-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--DDD-.UUU..---.-RLR--RLR--RLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRL--LRL--LRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-LLL--LLL--LLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRR--RRR--RRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-LLL--LLL--LLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRR--RRR--RRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-RLR--RLR--RLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRL--LRL--LRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-DDD--UUU--UUU-.UUU..---.-RLR--RLR--RLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRL--LRL--LRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-LLL--LLL--LLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRR--RRR--RRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-LLL--LLL--LLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRR--RRR--RRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-RLR--RLR--RLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRL--LRL--LRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--UUU-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--DDD-.UUU..---.-RLR--RLR--RLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRL--LRL--LRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-UUU--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--UUU-.UUU..---.-LLL--LLL--LLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRR--RRR--RRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--UUU-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--UUU-.UUU..---.-LLR--LLR--LLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--UUU-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRR--LRR--LRR-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--UUU-.UUU..---.-RLL--RLL--RLL-.---..FFF.-FFF--FFF--FFF-.FFF..---.-RRL--RRL--RRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--DDD-.DDD.', 'ULFRBD'),
             ('.UUU.-UUU--UUU--UUU-.UUU..---.-RLR--RLR--RLR-.---..FFF.-FFF--FFF--FFF-.FFF..---.-LRL--LRL--LRL-.---..BBB.-BBB--BBB--BBB-.BBB..DDD.-DDD--DDD--DDD-.DDD.', 'ULFRBD')),
            use_edges_pattern=True,
            legal_moves = (
                "U", "U'", "U2",
                "D", "D'", "D2",
                "L2", "F2", "R2", "B2",
                "Lw2", "Fw2", "Rw2", "Bw2",
            )
        )


# ==================================
# Solve last L4E with solved centers
# ==================================
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


class Build555EdgesXPlaneWithSolvedCenters(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-x-plane-with-solved-centers',
             (), # illegal moves
            '5x5x5',
            'lookup-table-5x5x5-step310-edges-x-plane-with-solved-centers.txt',
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


class Build555EdgesZPlane(BFS):

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
            'lookup-table-5x5x5-step341-edges-z-plane.txt',
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
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""", "ascii"),),
            use_edges_pattern=True,
        )
'''
'''



'''
TODO

Getting LR and FB centers to vertical bars
with L4E in x-plane needs two approaches
------------------------------------------
# centers are NOT solved
- when we reduce LR to 432 we need to also split edges into high/low groups. This
  will make step50 faster as it will have way more wing_str_combos to choose from.
        - (16!/(4!*4!*8!))^2 = 811,620,810,000
        - (16!/(8!*8!))^2 = 165,636,900 would be a "stage LR and FB" prune table
        - 165636900 / 811620810000 = 0.000 204
- step50 will put LR/FB centers in vertical bars and L4E in x-plane
    - if there are 8-edges in high/low could we solve 4-edges in the x-plane here instead?
      Probably not as this IDA is already slow.  That would be cool though.

# centers are solved...this will be the case for any larger cube using a fake_555
- keep using the pre-built "stage L4E to x-plane while maintaining centers" table
    - build a version of this that solves 4-edges?
- keep trying solutions until we find one where at least 4-edges are oriented
  so they can be solved without L L' R R'
- today this code path brings the tables back to solved but we do not need that, we
  only need LR/FB in vertical bars and UD can be anything.  We could save some moves
  here.


step50 notes:
    - LR and FB centers to vertical bars
    - UD centers to anything
    - stage the 1st L4E group to one of
        - the x-plane
        - outside the x-plane so we can use the "second L4E" table
        - which is better? Outside the x-plane would have many more goal
          states and would be more flexible.
    - the edges table here is (12!/(8!*4!))^3 or 121,287,375
    - 121287375/(121287375 * 432 * 4900) = 0.000 000 472 so slow but might be doable
        given the flexibility we have in picking which 4-edges to stage.



make the step50 tables take less space so you can build it one step deeper
'''

# brainstorm #2
'''
The problem with the strategy above is:
- some of the searches are pretty slow, it takes 8x longer to solve 50 5x5x5 cubes
  with this edge strat vs the strat in master where I L4E 3x
- it ONLY helps with 5x5x5, for the larger cubes that are using 5x5x5 there is no savings :(
  This is because all of these cubes are solving the centers beforehand.

New thinking
- stage UD centers
- stage LR centers
  20 moves
- solve centers
    - could potentially EO the outer orbit of edges here to save
      some moves when using fake_444 to pair outer orbit of edges.
  12 moves

- use fake_444 to pair outer orbit of edges
  ~20 moves unless they were already EOed then it would be ~14
  DID NOT WORK...it breaks up the t-centers :(  That kind of kills
  this entire strategy

then

- use middle layer slices to pair x-plane edges, keep centers solved
    24*22*20*18 = 190,080 states for the wings

- pair last 8-edges, keep centers solved
    16*14*12*10*8*6*4 = 5,160,960 states for the wings

or
- use middle layer slices to pair 6-edges (x-plane, DL and DR), keep centers solved
    24*22*20*18*16*14 = 42,577,920

- pair last 6-edges, keep centers solved
    12*10*8*6*4 = 23,040

    This opens the door for also doing something with the corners in this phase? That
    could reduce the move count for solving 333.

'''

# brainstorm #3
'''
stage UD
    10 moves

stage LR to 432 but with 4-edges EO
    - something to think about here is can we also but FB into one of 432 states? If
      we did then in the next phase we might be able to do LR vertical, FB vertical
      and paired to x-plane. That all depends on how much my math is off on the 3-edge
      prune table though...need to figure that out first. We would need to rebuild the
      PairOneEdge table that we use to ID the 4-edges in EO to also not use F F' B B'.
      If we ended up doing this we would need to build 6 "EO remaining 8 edges via slices"
      tables (one for each FB vertical bar pattern) but that is minor.

      I gave this a quick try, when you restrict F F' B B' it reduces the number of edge
      states by a good bit. It makes this phase very very slow.
    11 moves

LR to horizontal bars and pair 4-edges in z-plane
    option 1 - do this in one phase
    - A 2-edge prune table is
        ((12*11)^2/2) is how many states the wings can be in.  The wings are in high/low groups
            of 12 but there is a parity constraint thus the /2
        12!/10! = 132 is how many states the midges can be in.  I thought this would have been 12!/(10!/2!) = 66 though.
            I need to dig into this more, this makes a big difference.
        ((12*11)^2/2) * (12!/10!) = 1,149,984
        if I have a bug this would be
        ((12*11)^2/2) * (12!/(10!*2!)) = 574,992

    - A 3-edge prune table is
        ((12*11*10)^2/2) * (12!/9!) = 1,149,984,000

    - A 4-edge prune table is
        ((12*11*10*9)^2/2) * (12!/8!) = 838,338,336,000

    - So 838,338,336,000 * 432 = 362,162,161,152,000 states

    Using a 2-edge pt
    1149984/362162161152000 = 0.000 000 003

    Using a 3-edge pt
    1149984000/362162161152000 = 0.000 003
    So this is feasible but it would take 1.2G of RAM to load this pt


    option 2 - pair 4-edges then in another phase do the LR centers
    Using a 2-edge pt
    1149984/838338336000 = 0.000 001

    A pt of just the wings for 4-edges would be
    ((12*11*10*9)^2/2) = 70,567,200
    70567200/838338336000 = 0.000 084

    You would have to put these in the y-plane so that you could bar the LR centers (~5 moves)
    then move these to the z-plane (2 moves).  You figure it was probably already 12 or 13 moves
    to pair the 4-edges so you are looking at close to 20 moves here.

    For now assume we do option 1, 1.2G of RAM isn't that crazy these days.
    ~13 moves??? Educated guess based on xyzzy solves here:
    http://cubesolvingprograms.freeforums.net/thread/37/results-5x5x5-fewest-moves-challenge

EO remaining 8 edges via slices so they can be solved without L L' R R' F F' B B'
    - keep z-plane edges paired
    - keep LR in horiztonal bars
    - keep UD and FB staged
    - midges can be in (2^8)/2 = 128 states
    - wings can be in 16!/(8!*8!) = 12,870 states
        once F F' B B' are restricted can we get to all 12,870 states?
        # dwalton figure this out next
    - 128 * 12,870 = 1,647,360
    - We will need to prebuild this table as it will require unstaging the UD FB centers
      This will be similar to how the "stage L4E" tables were built
    - legal moves
        F F' F2
        B B' B2
        L2 R2 U2 B2

        Uw2 Dw2
        Lw2 Rw2

        2U2 2D2
        2L 2L' 2L2
        2R 2R' 2R2
        3L 3L' 3L2  ?? This would complicate things as the center squares would move. Would that
            really hurt anything though? It would make the solution short and you can always rotate
            the entire cube to get the center squares back in place. One downside is there is no way
            for say a 7x7x7 to slice the 3 layers in the middle in one move. You have to do 2 moves
            plus a rotate to do that for 7x7x7.

            It is probably worth building the table with/without this to see how much difference it makes
            and then decide whether or not to use it.

            If we dot NOT use this then the orientation of the midges would never change so at that point
            we only have to EO the wings relative to the midge orientation.  That becomes just 12,870 states!!
            This sounds almost too good to be true.

    - 8 moves?


FB to vertical bars
    - could we do this as part of the previous "EO 8-edges phase"?
        1,647,360 * 4900 = 8,072,064,000 so we could not prebuild that
        Would have to find a way to make the previous phase work via IDA...worry about this later
    - if you made this IDA you could explore a bunch of options that setup the edges nicely for the final phase
    5 moves

L and R to put paired edges in x-plane and flip LR horizontal bars to vertical
    2 moves

At this point
    - LR and FB in vertical bars
    - x-plane edges solved
    - 8-edges EOed
~49 moves to here

solve all centers and pair all edges
    - 6 x 6 x 4900 x (8!^2)/2 = 143,386,951,680,000
    - (8!^2)/2 = 812851200
    - 812851200/143386951680000 = 0.000 005
    ~15 moves??? Another educated guess based on xyzzy numbers

~64 moves to reduce to 333

'''


# brainstorm #5
'''
- stage UD centers
    10 moves

- stage LR centers but do so such that
    - LR centers are in one of 432 states that can be solved without L L' R R'
    - There are at least 6-edges that can be solved without L L' R R'
    11 moves

- LR to vertical bars and pair 4-edges in x-plane
    ~13 moves??? Educated guess based on xyzzy solves here:
    http://cubesolvingprograms.freeforums.net/thread/37/results-5x5x5-fewest-moves-challenge

- phase4
    LR centers to solved
    UD centers to bars
    pair 2-edges at DL DR
    14 moves??

At this point LR solved, UD bars, FB staged and there are 6-edges unpaired in y-plane and UL UR
    ~48 moves

Need to get FB centers to vertical bars but this will be tricky since we cannot move paired edges out of x-plane
    ~10 moves?

Pair the last 6-edges and solve UD FB centers
    ~18 moves

~76 moves to reduce to 333 yuck!!
'''

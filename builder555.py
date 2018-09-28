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
            . D D D .""", "ascii"),),
            use_edges_pattern=True
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
            . - - - .""", "ascii"),),
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

# brainstorm #3
'''
stage UD
    10 moves

stage LR to 432 but with 4-edges EO
    11 moves

LR to horizontal bars and pair 4-edges in z-plane

    - A 3-edge prune table is
        ((12*11*10)^2/2) is how many states the wings can be in.  The wings are in high/low groups
            of 12 but there is a parity constraint thus the /2
        ((12!/(9!*3!)) * 2) is how many states the midges can be in
        ((12*11*10)^2/2) * ((12!/(9!*3!)) * 2) = 383,328,000

    - A 4-edge prune table is
        ((12*11*10*9)^2/2) * ((12!/(8!*4!)) * 2) = 69,861,528,000

    - 69,861,528,000 * 432 = 30,180,180,096,000 states

    Using a 3-edge pt
    383,328,000/30,180,180,096,000 = 0.000 012

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

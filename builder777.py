#!/usr/bin/env python3

from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)


class Build777UDCentersStage(BFS):
    """
    (16!/(8!*8!))^3 or 2,131,746,903,000
    """

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-centers-stage',
            ("3Uw", "3Uw'",
             "3Dw", "3Dw'",
             "3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",

             # used for "fake" move to speed up IDA
             "Fw", "Fw'", "Bw", "Bw'",
             "3Uw", "3Uw'", "3Dw", "3Dw'", "Uw", "Uw'", "Dw", "Dw'",

             # can skip these for 7x7x7 cubes
             "3Lw2", "3Dw2", "3Bw2"),
            '7x7x7',
            'lookup-table-7x7x7-step10-UD-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . .""", "ascii"),)
        )


class Build777UDObliqueEdgesStage(BFS):
    """
    (16!/(8!*8!))^2 or 165,636,900
    """

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage',
            ("3Uw", "3Uw'",
             "3Dw", "3Dw'",
             "3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",

             # used for "fake" move to speed up IDA
             "Fw", "Fw'", "Bw", "Bw'",
             "3Uw", "3Uw'", "3Dw", "3Dw'", "Uw", "Uw'", "Dw", "Dw'",

             # can skip these for 7x7x7 cubes
             "3Lw2", "3Dw2", "3Bw2"),
            '7x7x7',
            'lookup-table-7x7x7-step11-UD-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            (("""
                . . . . . . .
                . . U . U . .
                . U . . . U .
                . . . . . . .
                . U . . . U .
                . . U . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . U . .
                . U . . . U .
                . . . . . . .
                . U . . . U .
                . . U . U . .
                . . . . . . .""", "ascii"),)
        )






class Build777StageLRObliqueEdges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step30',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'"),

            '7x7x7',
            'lookup-table-7x7x7-step30-stage-lr-oblique-edges.txt',
            True, # store_as_hex

            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . x x x . .  . . L L L . .  . . x x x . .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . . L L L . .  . . x x x . .  . . L L L . .  . . x x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )


class Build777StageLRObliqueEdges31(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step31',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'"),

            '7x7x7',
            'lookup-table-7x7x7-step31-stage-lr-oblique-edges.txt',
            True, # store_as_hex

            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L . L . .  . . x . x . .  . . L . L . .  . . x . x . .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . . L . L . .  . . x . x . .  . . L . L . .  . . x . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )



class Build777Step80(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step80',

            ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'", "3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged centers
             "Rw", "Rw'", "Lw", "Lw'", "Fw", "Fw'", "Bw", "Bw'", "Uw", "Uw'", "Dw", "Dw'",             # do not mess up staged centers
             "3Rw2", "3Lw2", "3Fw2", "3Bw2"),                                                          # do not mess up solved UD

            '7x7x7',
            'lookup-table-7x7x7-step80.txt',
            True, # store_as_hex

            # starting cubes, generated this list of tuples from "./builder-print-starting-cube-states.py 7x7x7-step80"
            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . . . . . .  . . x x x . .  . . . . . . .
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
 . . L L L . .  . . . . . . .  . . x x x . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .""", "ascii"),)

        )


class Build777Step81(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step81',

            ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'", "3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged centers
             "Rw", "Rw'", "Lw", "Lw'", "Fw", "Fw'", "Bw", "Bw'", "Uw", "Uw'", "Dw", "Dw'",             # do not mess up staged centers
             "3Rw2", "3Lw2", "3Fw2", "3Bw2"),                                                          # do not mess up solved UD

            '7x7x7',
            'lookup-table-7x7x7-step81.txt',
            True, # store_as_hex

            # starting cubes, generated this list of tuples from "./builder-print-starting-cube-states.py 7x7x7-step82"
            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L . . . .  . . . . . . .  . . x . . . .  . . . . . . .
 . . L L L L .  . . . . . . .  . . x x x x .  . . . . . . .
 . . L L L . .  . . . . . . .  . . x x x . .  . . . . . . .
 . L L L L . .  . . . . . . .  . x x x x . .  . . . . . . .
 . . . . L . .  . . . . . . .  . . . . x . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .""", "ascii"),)
        )



class Build777Step90(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step90',

            ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'", "3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged centers
             "Rw", "Rw'", "Lw", "Lw'", "Fw", "Fw'", "Bw", "Bw'", "Uw", "Uw'", "Dw", "Dw'",             # do not mess up staged centers
             "3Rw2", "3Lw2", "3Fw2", "3Bw2",                                                           # do not mess up solved UD
             "Lw", "Lw'", "Lw2", "Rw", "Rw'", "Rw2", "Fw2", "Bw2",                                     # do not mess up solved LR
             "L", "L'", "L2", "R", "R'", "R2"),

            '7x7x7',
            'lookup-table-7x7x7-step90.txt',
            False, # store_as_hex

            # starting cubes, generated this list of tuples from "./builder-print-starting-cube-states.py 7x7x7-step80"
            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . F F F . .  . . R R R . .  . . B B B . .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . . L L L . .  . . F F F . .  . . R R R . .  . . B B B . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .""", "ascii"),)
        )


class Build777Step91(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step90',

            ("3Rw", "3Rw'", "3Lw", "3Lw'", "3Fw", "3Fw'", "3Bw", "3Bw'", "3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged centers
             "Rw", "Rw'", "Lw", "Lw'", "Fw", "Fw'", "Bw", "Bw'", "Uw", "Uw'", "Dw", "Dw'",             # do not mess up staged centers
             "3Rw2", "3Lw2", "3Fw2", "3Bw2",                                                           # do not mess up solved UD
             "Lw", "Lw'", "Lw2", "Rw", "Rw'", "Rw2", "Fw2", "Bw2",                                     # do not mess up solved LR
             "L", "L'", "L2", "R", "R'", "R2"),

            '7x7x7',
            'lookup-table-7x7x7-step91.txt',
            True, # store_as_hex

            # starting cubes, generated this list of tuples from "./builder-print-starting-cube-states.py 7x7x7-step80"
            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . F . . . .  . . . . . . .  . . x . . . .
 . . . . . . .  . . F F F F .  . . . . . . .  . . x x x x .
 . . . . . . .  . . F F F . .  . . . . . . .  . . x x x . .
 . . . . . . .  . F F F F . .  . . . . . . .  . x x x x . .
 . . . . . . .  . . . . F . .  . . . . . . .  . . . . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .""", "ascii"),)
        )

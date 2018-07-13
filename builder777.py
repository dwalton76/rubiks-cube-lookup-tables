#!/usr/bin/env python3

from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)

class StartingStates777UDObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage',
            ("3Uw", "3Uw'", "3Uw2",
             "3Lw", "3Lw'", "3Lw2",
             "3Fw", "3Fw'", "3Fw2",
             "3Rw", "3Rw'", "3Rw2",
             "3Bw", "3Bw'", "3Bw2",
             "3Dw", "3Dw'", "3Dw2",
            ),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step00-UD-oblique-edges-stage.txt',
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
 . . x x x . .  . . x x x . .  . . x x x . .  . . x x x . .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . . x x x . .  . . x x x . .  . . x x x . .  . . x x x . .
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

    def __init__(self):
        from builder777ss import starting_states_step00_777
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step00-UD-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            starting_states_step00_777
        )


'''
class StartingStates777UDObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",

             # used for "fake" move to speed up IDA
             "Fw", "Fw'", "Bw", "Bw'",
             "3Uw", "3Uw'", "3Dw", "3Dw'", "Uw", "Uw'", "Dw", "Dw'",

             "3Uw", "3Uw'", "3Uw2",
             "3Dw", "3Dw'", "3Dw2",
             "3Fw2", "3Bw2", "3Rw2", "3Lw2"
            ),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step10-UD-oblique-edges-stage.txt',
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


class StartingStates777UDOutsideObliqueEdgesStage(BFS):
    """
    (16!/(8!*8!))^2 or 165,636,900
    """

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-outside-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",

             # used for "fake" move to speed up IDA
             "Fw", "Fw'", "Bw", "Bw'",
             "3Uw", "3Uw'", "3Dw", "3Dw'", "Uw", "Uw'", "Dw", "Dw'",

             "3Uw", "3Uw'", "3Uw2",
             "3Dw", "3Dw'", "3Dw2",
             "3Fw2", "3Bw2", "3Rw2", "3Lw2"
            ),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step11-UD-outside-oblique-edges-stage.txt',
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


class Build777UDObliqueEdgesStage(BFS):
    """
    (16!/(8!*8!))^2 or 165,636,900
    """

    def __init__(self):
        from builder777ss import starting_states_step10_777
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",

             # used for "fake" move to speed up IDA
             "Fw", "Fw'", "Bw", "Bw'",
             "3Uw", "3Uw'", "3Dw", "3Dw'", "Uw", "Uw'", "Dw", "Dw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step10-UD-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            starting_states_step10_777
        )


class Build777UDOutsideObliqueEdgesStage(BFS):
    """
    (16!/(8!*8!))^2 or 165,636,900
    """

    def __init__(self):
        from builder777ss import starting_states_step11_777
        BFS.__init__(self,
            '7x7x7-UD-outside-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",

             # used for "fake" move to speed up IDA
             "Fw", "Fw'", "Bw", "Bw'",
             "3Uw", "3Uw'", "3Dw", "3Dw'", "Uw", "Uw'", "Dw", "Dw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step11-UD-outside-oblique-edges-stage.txt',
            True, # store_as_hex

            # starting cubes
            starting_states_step11_777
        )
'''


class StartingStates777LRObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step30',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'",

             "3Uw2", "3Dw2", "3Fw2", "3Bw2", "3Rw2", "3Lw2"
            ),

            '7x7x7',
            'starting-states-lookup-table-7x7x7-step30-stage-lr-oblique-edges.txt',
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


class StartingStates777LROutsideObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step31',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'",

             "3Uw2", "3Dw2", "3Fw2", "3Bw2", "3Rw2", "3Lw2"
            ),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step31-stage-lr-oblique-edges.txt',
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


class StartingStates777LRLeftMiddleObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step32',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'",

             "3Uw2", "3Dw2", "3Fw2", "3Bw2", "3Rw2", "3Lw2"
            ),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step32-stage-lr-left-middle-oblique-edges.txt',
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
 . . L L . . .  . . x x . . .  . . L L . . .  . . x x . . .
 . . . . . L .  . . . . . x .  . . . . . L .  . . . . . x .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . L . . . . .  . x . . . . .  . L . . . . .  . x . . . . .
 . . . L L . .  . . . x x . .  . . . L L . .  . . . x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )


class StartingStates777LRRightMiddleObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step33',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'",

             "3Uw2", "3Dw2", "3Fw2", "3Bw2", "3Rw2", "3Lw2"
            ),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step33-stage-lr-right-middle-oblique-edges.txt',
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
 . . . L L . .  . . . x x . .  . . . L L . .  . . . x x . .
 . L . . . . .  . x . . . . .  . L . . . . .  . x . . . . .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . . . . . L .  . . . . . x .  . . . . . L .  . . . . . x .
 . . L L . . .  . . x x . . .  . . L L . . .  . . x x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )



class Build777LRObliqueEdgesStage(BFS):

    def __init__(self):
        from builder777ss import starting_states_step30_777
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
            # starting states
            starting_states_step30_777
        )


class Build777LROutsideObliqueEdgesStage(BFS):

    def __init__(self):
        from builder777ss import starting_states_step31_777
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

            # starting states
            starting_states_step31_777
        )


class Build777LRLeftMiddleObliqueEdgesStage(BFS):

    def __init__(self):
        from builder777ss import starting_states_step32_777
        BFS.__init__(self,
            '7x7x7-step32',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'"),

            '7x7x7',
            'lookup-table-7x7x7-step32-stage-lr-left-middle-oblique-edges.txt',
            True, # store_as_hex

            # starting states
            starting_states_step32_777
        )


class Build777LRRightMiddleObliqueEdgesStage(BFS):

    def __init__(self):
        from builder777ss import starting_states_step33_777
        BFS.__init__(self,
            '7x7x7-step33',

            ("3Uw", "3Uw'", "3Dw", "3Dw'", # do not mess up staged inner-x-centers
             "3Lw", "3Lw'", "3Rw", "3Rw'",
             "3Fw", "3Fw'", "3Bw", "3Bw'",
             "Rw", "Rw'", "Lw", "Lw'",     # do not mess up staged UD oblique pairs
             "Fw", "Fw'", "Bw", "Bw'"),

            '7x7x7',
            'lookup-table-7x7x7-step33-stage-lr-right-middle-oblique-edges.txt',
            True, # store_as_hex

            # starting states
            starting_states_step33_777
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


class StartingStates777Step40(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step40',

            #("3Uw", "3Uw'", "3Uw2", "Uw", "Uw'", "Uw2",
            # "3Lw", "3Lw'", "3Lw2", "Lw", "Lw'", "Lw2",
            # "3Fw", "3Fw'", "3Fw2", "Fw", "Fw'", "Fw2",
            # "3Rw", "3Rw'", "3Rw2", "Rw", "Rw'", "Rw2",
            # "3Bw", "3Bw'", "3Bw2", "Bw", "Bw'", "Bw2",
            # "3Dw", "3Dw'", "3Dw2", "Dw", "Dw'", "Dw2"),

            ("3Uw", "3Uw'", "3Uw2", "Uw", "Uw'", "Uw2",
             "3Lw", "3Lw'", "3Lw2", "Lw", "Lw'", "Lw2",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "3Rw2", "Rw", "Rw'", "Rw2",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "3Dw2", "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'"),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step40.txt',
            False, # store_as_hex

            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )

class Build777Step40(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step40',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'"),

            '7x7x7',
            'lookup-table-7x7x7-step40.txt',
            False, # store_as_hex
            (             ('.........................................................LLLLL..LLLLL..LLLLL..LLLLL..LLLLL.................................................................RRRRR..RRRRR..RRRRR..RRRRR..RRRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLLR..LLLLR..LLLLR..LLLLR..LLLLR.................................................................LRRRR..LRRRR..LRRRR..LRRRR..LRRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLLR..LLLLR..LLLLR..LLLLR..LLLLR.................................................................RRRRL..RRRRL..RRRRL..RRRRL..RRRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLRL..LLLRL..LLLRL..LLLRL..LLLRL.................................................................RLRRR..RLRRR..RLRRR..RLRRR..RLRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLRL..LLLRL..LLLRL..LLLRL..LLLRL.................................................................RRRLR..RRRLR..RRRLR..RRRLR..RRRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLRR..LLLRR..LLLRR..LLLRR..LLLRR.................................................................LLRRR..LLRRR..LLRRR..LLRRR..LLRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLRR..LLLRR..LLLRR..LLLRR..LLLRR.................................................................LRRLR..LRRLR..LRRLR..LRRLR..LRRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLRR..LLLRR..LLLRR..LLLRR..LLLRR.................................................................RLRRL..RLRRL..RLRRL..RLRRL..RLRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLRR..LLLRR..LLLRR..LLLRR..LLLRR.................................................................RRRLL..RRRLL..RRRLL..RRRLL..RRRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLLL..LRLLL..LRLLL..LRLLL..LRLLL.................................................................RLRRR..RLRRR..RLRRR..RLRRR..RLRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLLL..LRLLL..LRLLL..LRLLL..LRLLL.................................................................RRRLR..RRRLR..RRRLR..RRRLR..RRRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLLR..LRLLR..LRLLR..LRLLR..LRLLR.................................................................LLRRR..LLRRR..LLRRR..LLRRR..LLRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLLR..LRLLR..LRLLR..LRLLR..LRLLR.................................................................LRRLR..LRRLR..LRRLR..LRRLR..LRRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLLR..LRLLR..LRLLR..LRLLR..LRLLR.................................................................RLRRL..RLRRL..RLRRL..RLRRL..RLRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLLR..LRLLR..LRLLR..LRLLR..LRLLR.................................................................RRRLL..RRRLL..RRRLL..RRRLL..RRRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLRL..LRLRL..LRLRL..LRLRL..LRLRL.................................................................RLRLR..RLRLR..RLRLR..RLRLR..RLRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLRR..LRLRR..LRLRR..LRLRR..LRLRR.................................................................LLRLR..LLRLR..LLRLR..LLRLR..LLRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................LRLRR..LRLRR..LRLRR..LRLRR..LRLRR.................................................................RLRLL..RLRLL..RLRLL..RLRLL..RLRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLLL..RLLLL..RLLLL..RLLLL..RLLLL.................................................................LRRRR..LRRRR..LRRRR..LRRRR..LRRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLLL..RLLLL..RLLLL..RLLLL..RLLLL.................................................................RRRRL..RRRRL..RRRRL..RRRRL..RRRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLLR..RLLLR..RLLLR..RLLLR..RLLLR.................................................................LRRRL..LRRRL..LRRRL..LRRRL..LRRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLRL..RLLRL..RLLRL..RLLRL..RLLRL.................................................................LLRRR..LLRRR..LLRRR..LLRRR..LLRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLRL..RLLRL..RLLRL..RLLRL..RLLRL.................................................................LRRLR..LRRLR..LRRLR..LRRLR..LRRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLRL..RLLRL..RLLRL..RLLRL..RLLRL.................................................................RLRRL..RLRRL..RLRRL..RLRRL..RLRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLRL..RLLRL..RLLRL..RLLRL..RLLRL.................................................................RRRLL..RRRLL..RRRLL..RRRLL..RRRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLRR..RLLRR..RLLRR..RLLRR..RLLRR.................................................................LLRRL..LLRRL..LLRRL..LLRRL..LLRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RLLRR..RLLRR..RLLRR..RLLRR..RLLRR.................................................................LRRLL..LRRLL..LRRLL..LRRLL..LRRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLLL..RRLLL..RRLLL..RRLLL..RRLLL.................................................................LLRRR..LLRRR..LLRRR..LLRRR..LLRRR..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLLL..RRLLL..RRLLL..RRLLL..RRLLL.................................................................LRRLR..LRRLR..LRRLR..LRRLR..LRRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLLL..RRLLL..RRLLL..RRLLL..RRLLL.................................................................RLRRL..RLRRL..RLRRL..RLRRL..RLRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLLL..RRLLL..RRLLL..RRLLL..RRLLL.................................................................RRRLL..RRRLL..RRRLL..RRRLL..RRRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLLR..RRLLR..RRLLR..RRLLR..RRLLR.................................................................LLRRL..LLRRL..LLRRL..LLRRL..LLRRL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLLR..RRLLR..RRLLR..RRLLR..RRLLR.................................................................LRRLL..LRRLL..LRRLL..LRRLL..LRRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLRL..RRLRL..RRLRL..RRLRL..RRLRL.................................................................LLRLR..LLRLR..LLRLR..LLRLR..LLRLR..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLRL..RRLRL..RRLRL..RRLRL..RRLRL.................................................................RLRLL..RLRLL..RLRLL..RLRLL..RLRLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................RRLRR..RRLRR..RRLRR..RRLRR..RRLRR.................................................................LLRLL..LLRLL..LLRLL..LLRLL..LLRLL..........................................................................................................', 'ULFRBD'))
        )


class StartingStates777Step41(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step41',

            ("3Uw", "3Uw'", "3Uw2", "Uw", "Uw'", "Uw2",
             "3Lw", "3Lw'", "3Lw2", "Lw", "Lw'", "Lw2",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "3Rw2", "Rw", "Rw'", "Rw2",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "3Dw2", "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'"),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step41.txt',
            False, # store_as_hex

            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )


class StartingStates777Step42(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step42',

            ("3Uw", "3Uw'", "3Uw2", "Uw", "Uw'", "Uw2",
             "3Lw", "3Lw'", "3Lw2", "Lw", "Lw'", "Lw2",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "3Rw2", "Rw", "Rw'", "Rw2",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "3Dw2", "Dw", "Dw'", "Dw2",
             "L", "L'",
             "R", "R'"),
            '7x7x7',
            'starting-states-lookup-table-7x7x7-step42.txt',
            False, # store_as_hex

            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . L . L . L .  . . . . . . .  . R . R . R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L . L . L .  . . . . . . .  . R . R . R .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )


class Build777Step41(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step41',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'"),

            '7x7x7',
            'lookup-table-7x7x7-step41.txt',
            False, # store_as_hex
            (('..........................................................L.L...LLLLL...LLL...LLLLL...L.L...................................................................R.R...RRRRR...RRR...RRRRR...R.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.L...LLLLR...LLL...LLLLR...L.L...................................................................R.R...LRRRR...RRR...LRRRR...R.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.L...LLLLR...LLL...LLLLR...L.L...................................................................R.R...RRRRL...RRR...RRRRL...R.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.L...RLLLL...LLL...RLLLL...L.L...................................................................R.R...LRRRR...RRR...LRRRR...R.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.L...RLLLL...LLL...RLLLL...L.L...................................................................R.R...RRRRL...RRR...RRRRL...R.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.L...RLLLR...LLL...RLLLR...L.L...................................................................R.R...LRRRL...RRR...LRRRL...R.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...LLLRL...LLR...LLLRL...L.R...................................................................L.R...RLRRR...LRR...RLRRR...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...LLLRL...LLR...LLLRL...L.R...................................................................R.L...RRRLR...RRL...RRRLR...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...LLLRR...LLR...LLLRR...L.R...................................................................L.R...LLRRR...LRR...LLRRR...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...LLLRR...LLR...LLLRR...L.R...................................................................L.R...RLRRL...LRR...RLRRL...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...LLLRR...LLR...LLLRR...L.R...................................................................R.L...LRRLR...RRL...LRRLR...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...LLLRR...LLR...LLLRR...L.R...................................................................R.L...RRRLL...RRL...RRRLL...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...RLLRL...LLR...RLLRL...L.R...................................................................L.R...LLRRR...LRR...LLRRR...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...RLLRL...LLR...RLLRL...L.R...................................................................L.R...RLRRL...LRR...RLRRL...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...RLLRL...LLR...RLLRL...L.R...................................................................R.L...LRRLR...RRL...LRRLR...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...RLLRL...LLR...RLLRL...L.R...................................................................R.L...RRRLL...RRL...RRRLL...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...RLLRR...LLR...RLLRR...L.R...................................................................L.R...LLRRL...LRR...LLRRL...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................L.R...RLLRR...LLR...RLLRR...L.R...................................................................R.L...LRRLL...RRL...LRRLL...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...LRLLL...RLL...LRLLL...R.L...................................................................L.R...RLRRR...LRR...RLRRR...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...LRLLL...RLL...LRLLL...R.L...................................................................R.L...RRRLR...RRL...RRRLR...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...LRLLR...RLL...LRLLR...R.L...................................................................L.R...LLRRR...LRR...LLRRR...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...LRLLR...RLL...LRLLR...R.L...................................................................L.R...RLRRL...LRR...RLRRL...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...LRLLR...RLL...LRLLR...R.L...................................................................R.L...LRRLR...RRL...LRRLR...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...LRLLR...RLL...LRLLR...R.L...................................................................R.L...RRRLL...RRL...RRRLL...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...RRLLL...RLL...RRLLL...R.L...................................................................L.R...LLRRR...LRR...LLRRR...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...RRLLL...RLL...RRLLL...R.L...................................................................L.R...RLRRL...LRR...RLRRL...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...RRLLL...RLL...RRLLL...R.L...................................................................R.L...LRRLR...RRL...LRRLR...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...RRLLL...RLL...RRLLL...R.L...................................................................R.L...RRRLL...RRL...RRRLL...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...RRLLR...RLL...RRLLR...R.L...................................................................L.R...LLRRL...LRR...LLRRL...L.R...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.L...RRLLR...RLL...RRLLR...R.L...................................................................R.L...LRRLL...RRL...LRRLL...R.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.R...LRLRL...RLR...LRLRL...R.R...................................................................L.L...RLRLR...LRL...RLRLR...L.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.R...LRLRR...RLR...LRLRR...R.R...................................................................L.L...LLRLR...LRL...LLRLR...L.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.R...LRLRR...RLR...LRLRR...R.R...................................................................L.L...RLRLL...LRL...RLRLL...L.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.R...RRLRL...RLR...RRLRL...R.R...................................................................L.L...LLRLR...LRL...LLRLR...L.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.R...RRLRL...RLR...RRLRL...R.R...................................................................L.L...RLRLL...LRL...RLRLL...L.L...........................................................................................................', 'ULFRBD'),
             ('..........................................................R.R...RRLRR...RLR...RRLRR...R.R...................................................................L.L...LLRLL...LRL...LLRLL...L.L...........................................................................................................', 'ULFRBD'))
        )

class Build777Step42(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step42',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'"),

            '7x7x7',
            'lookup-table-7x7x7-step42.txt',
            False, # store_as_hex
            (('.........................................................L.L.L...LLL...LLLLL...LLL...L.L.L.................................................................R.R.R...RRR...RRRRR...RRR...R.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.L...LLR...LLLRL...LLR...L.L.L.................................................................R.R.R...LRR...RLRRR...LRR...R.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.L...LLR...LLLRL...LLR...L.L.L.................................................................R.R.R...RRL...RRRLR...RRL...R.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.L...RLL...LRLLL...RLL...L.L.L.................................................................R.R.R...LRR...RLRRR...LRR...R.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.L...RLL...LRLLL...RLL...L.L.L.................................................................R.R.R...RRL...RRRLR...RRL...R.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.L...RLR...LRLRL...RLR...L.L.L.................................................................R.R.R...LRL...RLRLR...LRL...R.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...LLL...LLLLR...LLL...L.L.R.................................................................L.R.R...RRR...LRRRR...RRR...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...LLL...LLLLR...LLL...L.L.R.................................................................R.R.L...RRR...RRRRL...RRR...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...LLR...LLLRR...LLR...L.L.R.................................................................L.R.R...LRR...LLRRR...LRR...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...LLR...LLLRR...LLR...L.L.R.................................................................L.R.R...RRL...LRRLR...RRL...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...LLR...LLLRR...LLR...L.L.R.................................................................R.R.L...LRR...RLRRL...LRR...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...LLR...LLLRR...LLR...L.L.R.................................................................R.R.L...RRL...RRRLL...RRL...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...RLL...LRLLR...RLL...L.L.R.................................................................L.R.R...LRR...LLRRR...LRR...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...RLL...LRLLR...RLL...L.L.R.................................................................L.R.R...RRL...LRRLR...RRL...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...RLL...LRLLR...RLL...L.L.R.................................................................R.R.L...LRR...RLRRL...LRR...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...RLL...LRLLR...RLL...L.L.R.................................................................R.R.L...RRL...RRRLL...RRL...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...RLR...LRLRR...RLR...L.L.R.................................................................L.R.R...LRL...LLRLR...LRL...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................L.L.R...RLR...LRLRR...RLR...L.L.R.................................................................R.R.L...LRL...RLRLL...LRL...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...LLL...RLLLL...LLL...R.L.L.................................................................L.R.R...RRR...LRRRR...RRR...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...LLL...RLLLL...LLL...R.L.L.................................................................R.R.L...RRR...RRRRL...RRR...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...LLR...RLLRL...LLR...R.L.L.................................................................L.R.R...LRR...LLRRR...LRR...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...LLR...RLLRL...LLR...R.L.L.................................................................L.R.R...RRL...LRRLR...RRL...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...LLR...RLLRL...LLR...R.L.L.................................................................R.R.L...LRR...RLRRL...LRR...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...LLR...RLLRL...LLR...R.L.L.................................................................R.R.L...RRL...RRRLL...RRL...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...RLL...RRLLL...RLL...R.L.L.................................................................L.R.R...LRR...LLRRR...LRR...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...RLL...RRLLL...RLL...R.L.L.................................................................L.R.R...RRL...LRRLR...RRL...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...RLL...RRLLL...RLL...R.L.L.................................................................R.R.L...LRR...RLRRL...LRR...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...RLL...RRLLL...RLL...R.L.L.................................................................R.R.L...RRL...RRRLL...RRL...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...RLR...RRLRL...RLR...R.L.L.................................................................L.R.R...LRL...LLRLR...LRL...L.R.R..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.L...RLR...RRLRL...RLR...R.L.L.................................................................R.R.L...LRL...RLRLL...LRL...R.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.R...LLL...RLLLR...LLL...R.L.R.................................................................L.R.L...RRR...LRRRL...RRR...L.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.R...LLR...RLLRR...LLR...R.L.R.................................................................L.R.L...LRR...LLRRL...LRR...L.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.R...LLR...RLLRR...LLR...R.L.R.................................................................L.R.L...RRL...LRRLL...RRL...L.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.R...RLL...RRLLR...RLL...R.L.R.................................................................L.R.L...LRR...LLRRL...LRR...L.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.R...RLL...RRLLR...RLL...R.L.R.................................................................L.R.L...RRL...LRRLL...RRL...L.R.L..........................................................................................................', 'ULFRBD'),
             ('.........................................................R.L.R...RLR...RRLRR...RLR...R.L.R.................................................................L.R.L...LRL...LLRLL...LRL...L.R.L..........................................................................................................', 'ULFRBD'))
        )


class StartingStates777Step50(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step50',

            ("3Uw", "3Uw'", "3Uw2", "Uw", "Uw'", "Uw2",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "3Fw2", "Fw", "Fw'", "Fw2",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "3Bw2", "Bw", "Bw'", "Bw2",
             "3Dw", "3Dw'", "3Dw2", "Dw", "Dw'", "Dw2",
             "U", "U'", "D", "D'"),

            '7x7x7',
            'starting-states-lookup-table-7x7x7-step50.txt',
            False, # store_as_hex

            (("""
                . . . . . . .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . . . . . . . """, "ascii"),)
        )


class Build777Step50(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step50',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'",

            # keep LR in vertical stripes
            "L", "L'", "R", "R'", "3Uw2", "3Dw2", "Uw2", "Dw2"),

            '7x7x7',
            'lookup-table-7x7x7-step50.txt',
            False, # store_as_hex
            (('........DDUDD..DDUDD..DDUDD..DDUDD..DDUDD....................................................................................................................................................................................................................UUDUU..UUDUU..UUDUU..UUDUU..UUDUU........', 'ULFRBD'),
             ('........DDUDU..DDUDU..DDUDU..DDUDU..DDUDU....................................................................................................................................................................................................................DUDUU..DUDUU..DUDUU..DUDUU..DUDUU........', 'ULFRBD'),
             ('........DDUDU..DDUDU..DDUDU..DDUDU..DDUDU....................................................................................................................................................................................................................UUDUD..UUDUD..UUDUD..UUDUD..UUDUD........', 'ULFRBD'),
             ('........DDUUD..DDUUD..DDUUD..DDUUD..DDUUD....................................................................................................................................................................................................................UDDUU..UDDUU..UDDUU..UDDUU..UDDUU........', 'ULFRBD'),
             ('........DDUUD..DDUUD..DDUUD..DDUUD..DDUUD....................................................................................................................................................................................................................UUDDU..UUDDU..UUDDU..UUDDU..UUDDU........', 'ULFRBD'),
             ('........DDUUU..DDUUU..DDUUU..DDUUU..DDUUU....................................................................................................................................................................................................................DDDUU..DDDUU..DDDUU..DDDUU..DDDUU........', 'ULFRBD'),
             ('........DDUUU..DDUUU..DDUUU..DDUUU..DDUUU....................................................................................................................................................................................................................DUDDU..DUDDU..DUDDU..DUDDU..DUDDU........', 'ULFRBD'),
             ('........DDUUU..DDUUU..DDUUU..DDUUU..DDUUU....................................................................................................................................................................................................................UDDUD..UDDUD..UDDUD..UDDUD..UDDUD........', 'ULFRBD'),
             ('........DDUUU..DDUUU..DDUUU..DDUUU..DDUUU....................................................................................................................................................................................................................UUDDD..UUDDD..UUDDD..UUDDD..UUDDD........', 'ULFRBD'),
             ('........DUUDD..DUUDD..DUUDD..DUUDD..DUUDD....................................................................................................................................................................................................................UDDUU..UDDUU..UDDUU..UDDUU..UDDUU........', 'ULFRBD'),
             ('........DUUDD..DUUDD..DUUDD..DUUDD..DUUDD....................................................................................................................................................................................................................UUDDU..UUDDU..UUDDU..UUDDU..UUDDU........', 'ULFRBD'),
             ('........DUUDU..DUUDU..DUUDU..DUUDU..DUUDU....................................................................................................................................................................................................................DDDUU..DDDUU..DDDUU..DDDUU..DDDUU........', 'ULFRBD'),
             ('........DUUDU..DUUDU..DUUDU..DUUDU..DUUDU....................................................................................................................................................................................................................DUDDU..DUDDU..DUDDU..DUDDU..DUDDU........', 'ULFRBD'),
             ('........DUUDU..DUUDU..DUUDU..DUUDU..DUUDU....................................................................................................................................................................................................................UDDUD..UDDUD..UDDUD..UDDUD..UDDUD........', 'ULFRBD'),
             ('........DUUDU..DUUDU..DUUDU..DUUDU..DUUDU....................................................................................................................................................................................................................UUDDD..UUDDD..UUDDD..UUDDD..UUDDD........', 'ULFRBD'),
             ('........DUUUD..DUUUD..DUUUD..DUUUD..DUUUD....................................................................................................................................................................................................................UDDDU..UDDDU..UDDDU..UDDDU..UDDDU........', 'ULFRBD'),
             ('........DUUUU..DUUUU..DUUUU..DUUUU..DUUUU....................................................................................................................................................................................................................DDDDU..DDDDU..DDDDU..DDDDU..DDDDU........', 'ULFRBD'),
             ('........DUUUU..DUUUU..DUUUU..DUUUU..DUUUU....................................................................................................................................................................................................................UDDDD..UDDDD..UDDDD..UDDDD..UDDDD........', 'ULFRBD'),
             ('........UDUDD..UDUDD..UDUDD..UDUDD..UDUDD....................................................................................................................................................................................................................DUDUU..DUDUU..DUDUU..DUDUU..DUDUU........', 'ULFRBD'),
             ('........UDUDD..UDUDD..UDUDD..UDUDD..UDUDD....................................................................................................................................................................................................................UUDUD..UUDUD..UUDUD..UUDUD..UUDUD........', 'ULFRBD'),
             ('........UDUDU..UDUDU..UDUDU..UDUDU..UDUDU....................................................................................................................................................................................................................DUDUD..DUDUD..DUDUD..DUDUD..DUDUD........', 'ULFRBD'),
             ('........UDUUD..UDUUD..UDUUD..UDUUD..UDUUD....................................................................................................................................................................................................................DDDUU..DDDUU..DDDUU..DDDUU..DDDUU........', 'ULFRBD'),
             ('........UDUUD..UDUUD..UDUUD..UDUUD..UDUUD....................................................................................................................................................................................................................DUDDU..DUDDU..DUDDU..DUDDU..DUDDU........', 'ULFRBD'),
             ('........UDUUD..UDUUD..UDUUD..UDUUD..UDUUD....................................................................................................................................................................................................................UDDUD..UDDUD..UDDUD..UDDUD..UDDUD........', 'ULFRBD'),
             ('........UDUUD..UDUUD..UDUUD..UDUUD..UDUUD....................................................................................................................................................................................................................UUDDD..UUDDD..UUDDD..UUDDD..UUDDD........', 'ULFRBD'),
             ('........UDUUU..UDUUU..UDUUU..UDUUU..UDUUU....................................................................................................................................................................................................................DDDUD..DDDUD..DDDUD..DDDUD..DDDUD........', 'ULFRBD'),
             ('........UDUUU..UDUUU..UDUUU..UDUUU..UDUUU....................................................................................................................................................................................................................DUDDD..DUDDD..DUDDD..DUDDD..DUDDD........', 'ULFRBD'),
             ('........UUUDD..UUUDD..UUUDD..UUUDD..UUUDD....................................................................................................................................................................................................................DDDUU..DDDUU..DDDUU..DDDUU..DDDUU........', 'ULFRBD'),
             ('........UUUDD..UUUDD..UUUDD..UUUDD..UUUDD....................................................................................................................................................................................................................DUDDU..DUDDU..DUDDU..DUDDU..DUDDU........', 'ULFRBD'),
             ('........UUUDD..UUUDD..UUUDD..UUUDD..UUUDD....................................................................................................................................................................................................................UDDUD..UDDUD..UDDUD..UDDUD..UDDUD........', 'ULFRBD'),
             ('........UUUDD..UUUDD..UUUDD..UUUDD..UUUDD....................................................................................................................................................................................................................UUDDD..UUDDD..UUDDD..UUDDD..UUDDD........', 'ULFRBD'),
             ('........UUUDU..UUUDU..UUUDU..UUUDU..UUUDU....................................................................................................................................................................................................................DDDUD..DDDUD..DDDUD..DDDUD..DDDUD........', 'ULFRBD'),
             ('........UUUDU..UUUDU..UUUDU..UUUDU..UUUDU....................................................................................................................................................................................................................DUDDD..DUDDD..DUDDD..DUDDD..DUDDD........', 'ULFRBD'),
             ('........UUUUD..UUUUD..UUUUD..UUUUD..UUUUD....................................................................................................................................................................................................................DDDDU..DDDDU..DDDDU..DDDDU..DDDDU........', 'ULFRBD'),
             ('........UUUUD..UUUUD..UUUUD..UUUUD..UUUUD....................................................................................................................................................................................................................UDDDD..UDDDD..UDDDD..UDDDD..UDDDD........', 'ULFRBD'),
             ('........UUUUU..UUUUU..UUUUU..UUUUU..UUUUU....................................................................................................................................................................................................................DDDDD..DDDDD..DDDDD..DDDDD..DDDDD........', 'ULFRBD'))
        )


class StartingStates777Step51(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step51',

            ("3Uw", "3Uw'", "3Uw2", "Uw", "Uw'", "Uw2",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "3Fw2", "Fw", "Fw'", "Fw2",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "3Bw2", "Bw", "Bw'", "Bw2",
             "3Dw", "3Dw'", "3Dw2", "Dw", "Dw'", "Dw2",
             "U", "U'", "D", "D'"),

            '7x7x7',
            'starting-states-lookup-table-7x7x7-step51.txt',
            False, # store_as_hex

            (("""
                . . . . . . .
                . . U . U . .
                . U U U U U .
                . . U U U . .
                . U U U U U .
                . . U . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . D . D . .
                . D D D D D .
                . . D D D . .
                . D D D D D .
                . . D . D . .
                . . . . . . . """, "ascii"),)
        )


class Build777Step51(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step51',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'",

            # keep LR in vertical stripes
            "L", "L'", "R", "R'", "3Uw2", "3Dw2", "Uw2", "Dw2"),

            '7x7x7',
            'lookup-table-7x7x7-step51.txt',
            False, # store_as_hex
            (('.........D.D...DDUDD...DUD...DDUDD...D.D......................................................................................................................................................................................................................U.U...UUDUU...UDU...UUDUU...U.U.........', 'ULFRBD'),
             ('.........D.D...DDUDU...DUD...DDUDU...D.D......................................................................................................................................................................................................................U.U...DUDUU...UDU...DUDUU...U.U.........', 'ULFRBD'),
             ('.........D.D...DDUDU...DUD...DDUDU...D.D......................................................................................................................................................................................................................U.U...UUDUD...UDU...UUDUD...U.U.........', 'ULFRBD'),
             ('.........D.D...UDUDD...DUD...UDUDD...D.D......................................................................................................................................................................................................................U.U...DUDUU...UDU...DUDUU...U.U.........', 'ULFRBD'),
             ('.........D.D...UDUDD...DUD...UDUDD...D.D......................................................................................................................................................................................................................U.U...UUDUD...UDU...UUDUD...U.U.........', 'ULFRBD'),
             ('.........D.D...UDUDU...DUD...UDUDU...D.D......................................................................................................................................................................................................................U.U...DUDUD...UDU...DUDUD...U.U.........', 'ULFRBD'),
             ('.........D.U...DDUUD...DUU...DDUUD...D.U......................................................................................................................................................................................................................D.U...UDDUU...DDU...UDDUU...D.U.........', 'ULFRBD'),
             ('.........D.U...DDUUD...DUU...DDUUD...D.U......................................................................................................................................................................................................................U.D...UUDDU...UDD...UUDDU...U.D.........', 'ULFRBD'),
             ('.........D.U...DDUUU...DUU...DDUUU...D.U......................................................................................................................................................................................................................D.U...DDDUU...DDU...DDDUU...D.U.........', 'ULFRBD'),
             ('.........D.U...DDUUU...DUU...DDUUU...D.U......................................................................................................................................................................................................................D.U...UDDUD...DDU...UDDUD...D.U.........', 'ULFRBD'),
             ('.........D.U...DDUUU...DUU...DDUUU...D.U......................................................................................................................................................................................................................U.D...DUDDU...UDD...DUDDU...U.D.........', 'ULFRBD'),
             ('.........D.U...DDUUU...DUU...DDUUU...D.U......................................................................................................................................................................................................................U.D...UUDDD...UDD...UUDDD...U.D.........', 'ULFRBD'),
             ('.........D.U...UDUUD...DUU...UDUUD...D.U......................................................................................................................................................................................................................D.U...DDDUU...DDU...DDDUU...D.U.........', 'ULFRBD'),
             ('.........D.U...UDUUD...DUU...UDUUD...D.U......................................................................................................................................................................................................................D.U...UDDUD...DDU...UDDUD...D.U.........', 'ULFRBD'),
             ('.........D.U...UDUUD...DUU...UDUUD...D.U......................................................................................................................................................................................................................U.D...DUDDU...UDD...DUDDU...U.D.........', 'ULFRBD'),
             ('.........D.U...UDUUD...DUU...UDUUD...D.U......................................................................................................................................................................................................................U.D...UUDDD...UDD...UUDDD...U.D.........', 'ULFRBD'),
             ('.........D.U...UDUUU...DUU...UDUUU...D.U......................................................................................................................................................................................................................D.U...DDDUD...DDU...DDDUD...D.U.........', 'ULFRBD'),
             ('.........D.U...UDUUU...DUU...UDUUU...D.U......................................................................................................................................................................................................................U.D...DUDDD...UDD...DUDDD...U.D.........', 'ULFRBD'),
             ('.........U.D...DUUDD...UUD...DUUDD...U.D......................................................................................................................................................................................................................D.U...UDDUU...DDU...UDDUU...D.U.........', 'ULFRBD'),
             ('.........U.D...DUUDD...UUD...DUUDD...U.D......................................................................................................................................................................................................................U.D...UUDDU...UDD...UUDDU...U.D.........', 'ULFRBD'),
             ('.........U.D...DUUDU...UUD...DUUDU...U.D......................................................................................................................................................................................................................D.U...DDDUU...DDU...DDDUU...D.U.........', 'ULFRBD'),
             ('.........U.D...DUUDU...UUD...DUUDU...U.D......................................................................................................................................................................................................................D.U...UDDUD...DDU...UDDUD...D.U.........', 'ULFRBD'),
             ('.........U.D...DUUDU...UUD...DUUDU...U.D......................................................................................................................................................................................................................U.D...DUDDU...UDD...DUDDU...U.D.........', 'ULFRBD'),
             ('.........U.D...DUUDU...UUD...DUUDU...U.D......................................................................................................................................................................................................................U.D...UUDDD...UDD...UUDDD...U.D.........', 'ULFRBD'),
             ('.........U.D...UUUDD...UUD...UUUDD...U.D......................................................................................................................................................................................................................D.U...DDDUU...DDU...DDDUU...D.U.........', 'ULFRBD'),
             ('.........U.D...UUUDD...UUD...UUUDD...U.D......................................................................................................................................................................................................................D.U...UDDUD...DDU...UDDUD...D.U.........', 'ULFRBD'),
             ('.........U.D...UUUDD...UUD...UUUDD...U.D......................................................................................................................................................................................................................U.D...DUDDU...UDD...DUDDU...U.D.........', 'ULFRBD'),
             ('.........U.D...UUUDD...UUD...UUUDD...U.D......................................................................................................................................................................................................................U.D...UUDDD...UDD...UUDDD...U.D.........', 'ULFRBD'),
             ('.........U.D...UUUDU...UUD...UUUDU...U.D......................................................................................................................................................................................................................D.U...DDDUD...DDU...DDDUD...D.U.........', 'ULFRBD'),
             ('.........U.D...UUUDU...UUD...UUUDU...U.D......................................................................................................................................................................................................................U.D...DUDDD...UDD...DUDDD...U.D.........', 'ULFRBD'),
             ('.........U.U...DUUUD...UUU...DUUUD...U.U......................................................................................................................................................................................................................D.D...UDDDU...DDD...UDDDU...D.D.........', 'ULFRBD'),
             ('.........U.U...DUUUU...UUU...DUUUU...U.U......................................................................................................................................................................................................................D.D...DDDDU...DDD...DDDDU...D.D.........', 'ULFRBD'),
             ('.........U.U...DUUUU...UUU...DUUUU...U.U......................................................................................................................................................................................................................D.D...UDDDD...DDD...UDDDD...D.D.........', 'ULFRBD'),
             ('.........U.U...UUUUD...UUU...UUUUD...U.U......................................................................................................................................................................................................................D.D...DDDDU...DDD...DDDDU...D.D.........', 'ULFRBD'),
             ('.........U.U...UUUUD...UUU...UUUUD...U.U......................................................................................................................................................................................................................D.D...UDDDD...DDD...UDDDD...D.D.........', 'ULFRBD'),
             ('.........U.U...UUUUU...UUU...UUUUU...U.U......................................................................................................................................................................................................................D.D...DDDDD...DDD...DDDDD...D.D.........', 'ULFRBD'))
        )


class StartingStates777Step52(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step52',

            ("3Uw", "3Uw'", "3Uw2", "Uw", "Uw'", "Uw2",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "3Fw2", "Fw", "Fw'", "Fw2",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "3Bw2", "Bw", "Bw'", "Bw2",
             "3Dw", "3Dw'", "3Dw2", "Dw", "Dw'", "Dw2",
             "U", "U'", "D", "D'"),

            '7x7x7',
            'starting-states-lookup-table-7x7x7-step52.txt',
            False, # store_as_hex

            (("""
                . . . . . . .
                . U . U . U .
                . . U U U . .
                . U U U U U .
                . . U U U . .
                . U . U . U .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . D . D . D .
                . . D D D . .
                . D D D D D .
                . . D D D . .
                . D . D . D .
                . . . . . . . """, "ascii"),)
        )


class Build777Step52(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step52',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'",

            # keep LR in vertical stripes
            "L", "L'", "R", "R'", "3Uw2", "3Dw2", "Uw2", "Dw2"),

            '7x7x7',
            'lookup-table-7x7x7-step52.txt',
            False, # store_as_hex
            (('........D.U.D...DUD...DDUDD...DUD...D.U.D....................................................................................................................................................................................................................U.D.U...UDU...UUDUU...UDU...U.D.U........', 'ULFRBD'),
             ('........D.U.D...DUU...DDUUD...DUU...D.U.D....................................................................................................................................................................................................................U.D.U...DDU...UDDUU...DDU...U.D.U........', 'ULFRBD'),
             ('........D.U.D...DUU...DDUUD...DUU...D.U.D....................................................................................................................................................................................................................U.D.U...UDD...UUDDU...UDD...U.D.U........', 'ULFRBD'),
             ('........D.U.D...UUD...DUUDD...UUD...D.U.D....................................................................................................................................................................................................................U.D.U...DDU...UDDUU...DDU...U.D.U........', 'ULFRBD'),
             ('........D.U.D...UUD...DUUDD...UUD...D.U.D....................................................................................................................................................................................................................U.D.U...UDD...UUDDU...UDD...U.D.U........', 'ULFRBD'),
             ('........D.U.D...UUU...DUUUD...UUU...D.U.D....................................................................................................................................................................................................................U.D.U...DDD...UDDDU...DDD...U.D.U........', 'ULFRBD'),
             ('........D.U.U...DUD...DDUDU...DUD...D.U.U....................................................................................................................................................................................................................D.D.U...UDU...DUDUU...UDU...D.D.U........', 'ULFRBD'),
             ('........D.U.U...DUD...DDUDU...DUD...D.U.U....................................................................................................................................................................................................................U.D.D...UDU...UUDUD...UDU...U.D.D........', 'ULFRBD'),
             ('........D.U.U...DUU...DDUUU...DUU...D.U.U....................................................................................................................................................................................................................D.D.U...DDU...DDDUU...DDU...D.D.U........', 'ULFRBD'),
             ('........D.U.U...DUU...DDUUU...DUU...D.U.U....................................................................................................................................................................................................................D.D.U...UDD...DUDDU...UDD...D.D.U........', 'ULFRBD'),
             ('........D.U.U...DUU...DDUUU...DUU...D.U.U....................................................................................................................................................................................................................U.D.D...DDU...UDDUD...DDU...U.D.D........', 'ULFRBD'),
             ('........D.U.U...DUU...DDUUU...DUU...D.U.U....................................................................................................................................................................................................................U.D.D...UDD...UUDDD...UDD...U.D.D........', 'ULFRBD'),
             ('........D.U.U...UUD...DUUDU...UUD...D.U.U....................................................................................................................................................................................................................D.D.U...DDU...DDDUU...DDU...D.D.U........', 'ULFRBD'),
             ('........D.U.U...UUD...DUUDU...UUD...D.U.U....................................................................................................................................................................................................................D.D.U...UDD...DUDDU...UDD...D.D.U........', 'ULFRBD'),
             ('........D.U.U...UUD...DUUDU...UUD...D.U.U....................................................................................................................................................................................................................U.D.D...DDU...UDDUD...DDU...U.D.D........', 'ULFRBD'),
             ('........D.U.U...UUD...DUUDU...UUD...D.U.U....................................................................................................................................................................................................................U.D.D...UDD...UUDDD...UDD...U.D.D........', 'ULFRBD'),
             ('........D.U.U...UUU...DUUUU...UUU...D.U.U....................................................................................................................................................................................................................D.D.U...DDD...DDDDU...DDD...D.D.U........', 'ULFRBD'),
             ('........D.U.U...UUU...DUUUU...UUU...D.U.U....................................................................................................................................................................................................................U.D.D...DDD...UDDDD...DDD...U.D.D........', 'ULFRBD'),
             ('........U.U.D...DUD...UDUDD...DUD...U.U.D....................................................................................................................................................................................................................D.D.U...UDU...DUDUU...UDU...D.D.U........', 'ULFRBD'),
             ('........U.U.D...DUD...UDUDD...DUD...U.U.D....................................................................................................................................................................................................................U.D.D...UDU...UUDUD...UDU...U.D.D........', 'ULFRBD'),
             ('........U.U.D...DUU...UDUUD...DUU...U.U.D....................................................................................................................................................................................................................D.D.U...DDU...DDDUU...DDU...D.D.U........', 'ULFRBD'),
             ('........U.U.D...DUU...UDUUD...DUU...U.U.D....................................................................................................................................................................................................................D.D.U...UDD...DUDDU...UDD...D.D.U........', 'ULFRBD'),
             ('........U.U.D...DUU...UDUUD...DUU...U.U.D....................................................................................................................................................................................................................U.D.D...DDU...UDDUD...DDU...U.D.D........', 'ULFRBD'),
             ('........U.U.D...DUU...UDUUD...DUU...U.U.D....................................................................................................................................................................................................................U.D.D...UDD...UUDDD...UDD...U.D.D........', 'ULFRBD'),
             ('........U.U.D...UUD...UUUDD...UUD...U.U.D....................................................................................................................................................................................................................D.D.U...DDU...DDDUU...DDU...D.D.U........', 'ULFRBD'),
             ('........U.U.D...UUD...UUUDD...UUD...U.U.D....................................................................................................................................................................................................................D.D.U...UDD...DUDDU...UDD...D.D.U........', 'ULFRBD'),
             ('........U.U.D...UUD...UUUDD...UUD...U.U.D....................................................................................................................................................................................................................U.D.D...DDU...UDDUD...DDU...U.D.D........', 'ULFRBD'),
             ('........U.U.D...UUD...UUUDD...UUD...U.U.D....................................................................................................................................................................................................................U.D.D...UDD...UUDDD...UDD...U.D.D........', 'ULFRBD'),
             ('........U.U.D...UUU...UUUUD...UUU...U.U.D....................................................................................................................................................................................................................D.D.U...DDD...DDDDU...DDD...D.D.U........', 'ULFRBD'),
             ('........U.U.D...UUU...UUUUD...UUU...U.U.D....................................................................................................................................................................................................................U.D.D...DDD...UDDDD...DDD...U.D.D........', 'ULFRBD'),
             ('........U.U.U...DUD...UDUDU...DUD...U.U.U....................................................................................................................................................................................................................D.D.D...UDU...DUDUD...UDU...D.D.D........', 'ULFRBD'),
             ('........U.U.U...DUU...UDUUU...DUU...U.U.U....................................................................................................................................................................................................................D.D.D...DDU...DDDUD...DDU...D.D.D........', 'ULFRBD'),
             ('........U.U.U...DUU...UDUUU...DUU...U.U.U....................................................................................................................................................................................................................D.D.D...UDD...DUDDD...UDD...D.D.D........', 'ULFRBD'),
             ('........U.U.U...UUD...UUUDU...UUD...U.U.U....................................................................................................................................................................................................................D.D.D...DDU...DDDUD...DDU...D.D.D........', 'ULFRBD'),
             ('........U.U.U...UUD...UUUDU...UUD...U.U.U....................................................................................................................................................................................................................D.D.D...UDD...DUDDD...UDD...D.D.D........', 'ULFRBD'),
             ('........U.U.U...UUU...UUUUU...UUU...U.U.U....................................................................................................................................................................................................................D.D.D...DDD...DDDDD...DDD...D.D.D........', 'ULFRBD'))
        )

class Build777Step60(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step60',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'",

            # keep LR in horizontal stripes
            "L", "L'", "R", "R'", "3Fw2", "3Bw2", "Fw2", "Bw2",

            # keep UD in vertical stripes
            "U", "U'", "D", "D'"),

            '7x7x7',
            'lookup-table-7x7x7-step60.txt',
            False, # store_as_hex
            (("""
                . . . . . . .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . L L L L L .  . F F F F F .  . R R R R R .  . B B B B B .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . . . . . . . """, "ascii"),)
        )


class Build777Step61(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step61',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'",

            # keep LR in horizontal stripes
            "L", "L'", "R", "R'", "3Fw2", "3Bw2", "Fw2", "Bw2",

            # keep UD in vertical stripes
            "U", "U'", "D", "D'"),

            '7x7x7',
            'lookup-table-7x7x7-step61.txt',
            False, # store_as_hex
            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
 . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
 . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )

class Build777Step62(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-step62',

            # keep all centers staged
            ("3Uw", "3Uw'", "Uw", "Uw'",
             "3Lw", "3Lw'", "Lw", "Lw'",
             "3Fw", "3Fw'", "Fw", "Fw'",
             "3Rw", "3Rw'", "Rw", "Rw'",
             "3Bw", "3Bw'", "Bw", "Bw'",
             "3Dw", "3Dw'", "Dw", "Dw'",

            # keep LR in horizontal stripes
            "L", "L'", "R", "R'", "3Fw2", "3Bw2", "Fw2", "Bw2",

            # keep UD in vertical stripes
            "U", "U'", "D", "D'"),

            '7x7x7',
            'lookup-table-7x7x7-step62.txt',
            False, # store_as_hex
            (("""
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . F . F . F .  . . . . . . .  . B . B . B .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . F . F . F .  . . . . . . .  . B . B . B .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """, "ascii"),)
        )


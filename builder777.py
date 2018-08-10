#!/usr/bin/env python3

from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)

'''
class Build777UDObliqueEdgesStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step10-UD-oblique-edges-stage.txt',
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
                . . . . . . .""", "ascii"),),
        )


class Build777UDObliqueEdgesStageLeft(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage-left',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step11-UD-oblique-edges-stage-left.txt',
            True, # store_as_hex

            # starting cubes
            (("""
                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . x . . . .  . . x . . . .  . . x . . . .  . . x . . . .
 . . . . . x .  . . . . . x .  . . . . . x .  . . . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . x . . . . .  . x . . . . .  . x . . . . .  . x . . . . .
 . . . . x . .  . . . . x . .  . . . . x . .  . . . . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . .""", "ascii"),)
        )


class Build777UDObliqueEdgesStageRight(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage-right',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step12-UD-oblique-edges-stage-right.txt',
            True, # store_as_hex

            # starting cubes
            (("""
                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . x . .  . . . . x . .  . . . . x . .  . . . . x . .
 . x . . . . .  . x . . . . .  . x . . . . .  . x . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . x .  . . . . . x .  . . . . . x .  . . . . . x .
 . . x . . . .  . . x . . . .  . . x . . . .  . . x . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . .""", "ascii"),)
        )


class Build777UDObliqueEdgesStageMiddle(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage-middle',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step13-UD-oblique-edges-stage-middle.txt',
            True, # store_as_hex

            # starting cubes
            (("""
                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . x . . .  . . . x . . .  . . . x . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . x . . .  . . . x . . .  . . . x . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . .""", "ascii"),)
        )


class Build777UDObliqueEdgesStageLeftRight(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage-left-right',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step14-UD-oblique-edges-stage-left-right.txt',
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
 . . x . x . .  . . x . x . .  . . x . x . .  . . x . x . .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . . x . x . .  . . x . x . .  . . x . x . .  . . x . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . U . .
                . U . . . U .
                . . . . . . .
                . U . . . U .
                . . U . U . .
                . . . . . . .""", "ascii"),)
        )


class Build777UDObliqueEdgesStageLeftMiddle(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage-left-middle',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step15-UD-oblique-edges-stage-left-middle.txt',
            True, # store_as_hex

            # starting cubes
            (("""
                . . . . . . .
                . . U U . . .
                . . . . . U .
                . U . . . U .
                . U . . . . .
                . . . U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . x x . . .  . . x x . . .  . . x x . . .  . . x x . . .
 . . . . . x .  . . . . . x .  . . . . . x .  . . . . . x .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . x . . . . .  . x . . . . .  . x . . . . .  . x . . . . .
 . . . x x . .  . . . x x . .  . . . x x . .  . . . x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U . . .
                . . . . . U .
                . U . . . U .
                . U . . . . .
                . . . U U . .
                . . . . . . .""", "ascii"),)
        )


class Build777UDObliqueEdgesStageRightMiddle(BFS):

    def __init__(self):
        BFS.__init__(self,
            '7x7x7-UD-oblique-edges-stage-right-middle',
            ("3Fw", "3Fw'",
             "3Bw", "3Bw'",
             "3Lw", "3Lw'",
             "3Rw", "3Rw'",
            ),
            '7x7x7',
            'lookup-table-7x7x7-step16-UD-oblique-edges-stage-right-middle.txt',
            True, # store_as_hex

            # starting cubes
            (("""
                . . . . . . .
                . . . U U . .
                . U . . . . .
                . U . . . U .
                . . . . . U .
                . . U U . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . x x . .  . . . x x . .  . . . x x . .  . . . x x . .
 . x . . . . .  . x . . . . .  . x . . . . .  . x . . . . .
 . x . . . x .  . x . . . x .  . x . . . x .  . x . . . x .
 . . . . . x .  . . . . . x .  . . . . . x .  . . . . . x .
 . . x x . . .  . . x x . . .  . . x x . . .  . . x x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . U U . .
                . U . . . . .
                . U . . . U .
                . . . . . U .
                . . U U . . .
                . . . . . . .""", "ascii"),)
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
            starting_states_step30_777,
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
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
 . L L L L L .  . . . . . . .  . x x x x x .  . . . . . . .
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
            True, # store_as_hex
            (('.........................................................LLLLL..LLLLL..LLLLL..LLLLL..LLLLL.................................................................xxxxx..xxxxx..xxxxx..xxxxx..xxxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLLx..LLLLx..LLLLx..LLLLx..LLLLx.................................................................Lxxxx..Lxxxx..Lxxxx..Lxxxx..Lxxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLLx..LLLLx..LLLLx..LLLLx..LLLLx.................................................................xxxxL..xxxxL..xxxxL..xxxxL..xxxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLxL..LLLxL..LLLxL..LLLxL..LLLxL.................................................................xLxxx..xLxxx..xLxxx..xLxxx..xLxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLxL..LLLxL..LLLxL..LLLxL..LLLxL.................................................................xxxLx..xxxLx..xxxLx..xxxLx..xxxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLxx..LLLxx..LLLxx..LLLxx..LLLxx.................................................................LLxxx..LLxxx..LLxxx..LLxxx..LLxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLxx..LLLxx..LLLxx..LLLxx..LLLxx.................................................................LxxLx..LxxLx..LxxLx..LxxLx..LxxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLxx..LLLxx..LLLxx..LLLxx..LLLxx.................................................................xLxxL..xLxxL..xLxxL..xLxxL..xLxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LLLxx..LLLxx..LLLxx..LLLxx..LLLxx.................................................................xxxLL..xxxLL..xxxLL..xxxLL..xxxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLLL..LxLLL..LxLLL..LxLLL..LxLLL.................................................................xLxxx..xLxxx..xLxxx..xLxxx..xLxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLLL..LxLLL..LxLLL..LxLLL..LxLLL.................................................................xxxLx..xxxLx..xxxLx..xxxLx..xxxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLLx..LxLLx..LxLLx..LxLLx..LxLLx.................................................................LLxxx..LLxxx..LLxxx..LLxxx..LLxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLLx..LxLLx..LxLLx..LxLLx..LxLLx.................................................................LxxLx..LxxLx..LxxLx..LxxLx..LxxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLLx..LxLLx..LxLLx..LxLLx..LxLLx.................................................................xLxxL..xLxxL..xLxxL..xLxxL..xLxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLLx..LxLLx..LxLLx..LxLLx..LxLLx.................................................................xxxLL..xxxLL..xxxLL..xxxLL..xxxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLxL..LxLxL..LxLxL..LxLxL..LxLxL.................................................................xLxLx..xLxLx..xLxLx..xLxLx..xLxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLxx..LxLxx..LxLxx..LxLxx..LxLxx.................................................................LLxLx..LLxLx..LLxLx..LLxLx..LLxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................LxLxx..LxLxx..LxLxx..LxLxx..LxLxx.................................................................xLxLL..xLxLL..xLxLL..xLxLL..xLxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLLL..xLLLL..xLLLL..xLLLL..xLLLL.................................................................Lxxxx..Lxxxx..Lxxxx..Lxxxx..Lxxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLLL..xLLLL..xLLLL..xLLLL..xLLLL.................................................................xxxxL..xxxxL..xxxxL..xxxxL..xxxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLLx..xLLLx..xLLLx..xLLLx..xLLLx.................................................................LxxxL..LxxxL..LxxxL..LxxxL..LxxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLxL..xLLxL..xLLxL..xLLxL..xLLxL.................................................................LLxxx..LLxxx..LLxxx..LLxxx..LLxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLxL..xLLxL..xLLxL..xLLxL..xLLxL.................................................................LxxLx..LxxLx..LxxLx..LxxLx..LxxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLxL..xLLxL..xLLxL..xLLxL..xLLxL.................................................................xLxxL..xLxxL..xLxxL..xLxxL..xLxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLxL..xLLxL..xLLxL..xLLxL..xLLxL.................................................................xxxLL..xxxLL..xxxLL..xxxLL..xxxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLxx..xLLxx..xLLxx..xLLxx..xLLxx.................................................................LLxxL..LLxxL..LLxxL..LLxxL..LLxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xLLxx..xLLxx..xLLxx..xLLxx..xLLxx.................................................................LxxLL..LxxLL..LxxLL..LxxLL..LxxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLLL..xxLLL..xxLLL..xxLLL..xxLLL.................................................................LLxxx..LLxxx..LLxxx..LLxxx..LLxxx..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLLL..xxLLL..xxLLL..xxLLL..xxLLL.................................................................LxxLx..LxxLx..LxxLx..LxxLx..LxxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLLL..xxLLL..xxLLL..xxLLL..xxLLL.................................................................xLxxL..xLxxL..xLxxL..xLxxL..xLxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLLL..xxLLL..xxLLL..xxLLL..xxLLL.................................................................xxxLL..xxxLL..xxxLL..xxxLL..xxxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLLx..xxLLx..xxLLx..xxLLx..xxLLx.................................................................LLxxL..LLxxL..LLxxL..LLxxL..LLxxL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLLx..xxLLx..xxLLx..xxLLx..xxLLx.................................................................LxxLL..LxxLL..LxxLL..LxxLL..LxxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLxL..xxLxL..xxLxL..xxLxL..xxLxL.................................................................LLxLx..LLxLx..LLxLx..LLxLx..LLxLx..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLxL..xxLxL..xxLxL..xxLxL..xxLxL.................................................................xLxLL..xLxLL..xLxLL..xLxLL..xLxLL..........................................................................................................', 'ULFRBD'),
             ('.........................................................xxLxx..xxLxx..xxLxx..xxLxx..xxLxx.................................................................LLxLL..LLxLL..LLxLL..LLxLL..LLxLL..........................................................................................................', 'ULFRBD'))
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
            True, # store_as_hex

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
                . x x x x x .
                . x x x x x .
                . x x x x x .
                . x x x x x .
                . x x x x x .
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
            True, # store_as_hex
            (('........xxUxx..xxUxx..xxUxx..xxUxx..xxUxx....................................................................................................................................................................................................................UUxUU..UUxUU..UUxUU..UUxUU..UUxUU........', 'ULFRBD'),
             ('........xxUxU..xxUxU..xxUxU..xxUxU..xxUxU....................................................................................................................................................................................................................xUxUU..xUxUU..xUxUU..xUxUU..xUxUU........', 'ULFRBD'),
             ('........xxUxU..xxUxU..xxUxU..xxUxU..xxUxU....................................................................................................................................................................................................................UUxUx..UUxUx..UUxUx..UUxUx..UUxUx........', 'ULFRBD'),
             ('........xxUUx..xxUUx..xxUUx..xxUUx..xxUUx....................................................................................................................................................................................................................UxxUU..UxxUU..UxxUU..UxxUU..UxxUU........', 'ULFRBD'),
             ('........xxUUx..xxUUx..xxUUx..xxUUx..xxUUx....................................................................................................................................................................................................................UUxxU..UUxxU..UUxxU..UUxxU..UUxxU........', 'ULFRBD'),
             ('........xxUUU..xxUUU..xxUUU..xxUUU..xxUUU....................................................................................................................................................................................................................xxxUU..xxxUU..xxxUU..xxxUU..xxxUU........', 'ULFRBD'),
             ('........xxUUU..xxUUU..xxUUU..xxUUU..xxUUU....................................................................................................................................................................................................................xUxxU..xUxxU..xUxxU..xUxxU..xUxxU........', 'ULFRBD'),
             ('........xxUUU..xxUUU..xxUUU..xxUUU..xxUUU....................................................................................................................................................................................................................UxxUx..UxxUx..UxxUx..UxxUx..UxxUx........', 'ULFRBD'),
             ('........xxUUU..xxUUU..xxUUU..xxUUU..xxUUU....................................................................................................................................................................................................................UUxxx..UUxxx..UUxxx..UUxxx..UUxxx........', 'ULFRBD'),
             ('........xUUxx..xUUxx..xUUxx..xUUxx..xUUxx....................................................................................................................................................................................................................UxxUU..UxxUU..UxxUU..UxxUU..UxxUU........', 'ULFRBD'),
             ('........xUUxx..xUUxx..xUUxx..xUUxx..xUUxx....................................................................................................................................................................................................................UUxxU..UUxxU..UUxxU..UUxxU..UUxxU........', 'ULFRBD'),
             ('........xUUxU..xUUxU..xUUxU..xUUxU..xUUxU....................................................................................................................................................................................................................xxxUU..xxxUU..xxxUU..xxxUU..xxxUU........', 'ULFRBD'),
             ('........xUUxU..xUUxU..xUUxU..xUUxU..xUUxU....................................................................................................................................................................................................................xUxxU..xUxxU..xUxxU..xUxxU..xUxxU........', 'ULFRBD'),
             ('........xUUxU..xUUxU..xUUxU..xUUxU..xUUxU....................................................................................................................................................................................................................UxxUx..UxxUx..UxxUx..UxxUx..UxxUx........', 'ULFRBD'),
             ('........xUUxU..xUUxU..xUUxU..xUUxU..xUUxU....................................................................................................................................................................................................................UUxxx..UUxxx..UUxxx..UUxxx..UUxxx........', 'ULFRBD'),
             ('........xUUUx..xUUUx..xUUUx..xUUUx..xUUUx....................................................................................................................................................................................................................UxxxU..UxxxU..UxxxU..UxxxU..UxxxU........', 'ULFRBD'),
             ('........xUUUU..xUUUU..xUUUU..xUUUU..xUUUU....................................................................................................................................................................................................................xxxxU..xxxxU..xxxxU..xxxxU..xxxxU........', 'ULFRBD'),
             ('........xUUUU..xUUUU..xUUUU..xUUUU..xUUUU....................................................................................................................................................................................................................Uxxxx..Uxxxx..Uxxxx..Uxxxx..Uxxxx........', 'ULFRBD'),
             ('........UxUxx..UxUxx..UxUxx..UxUxx..UxUxx....................................................................................................................................................................................................................xUxUU..xUxUU..xUxUU..xUxUU..xUxUU........', 'ULFRBD'),
             ('........UxUxx..UxUxx..UxUxx..UxUxx..UxUxx....................................................................................................................................................................................................................UUxUx..UUxUx..UUxUx..UUxUx..UUxUx........', 'ULFRBD'),
             ('........UxUxU..UxUxU..UxUxU..UxUxU..UxUxU....................................................................................................................................................................................................................xUxUx..xUxUx..xUxUx..xUxUx..xUxUx........', 'ULFRBD'),
             ('........UxUUx..UxUUx..UxUUx..UxUUx..UxUUx....................................................................................................................................................................................................................xxxUU..xxxUU..xxxUU..xxxUU..xxxUU........', 'ULFRBD'),
             ('........UxUUx..UxUUx..UxUUx..UxUUx..UxUUx....................................................................................................................................................................................................................xUxxU..xUxxU..xUxxU..xUxxU..xUxxU........', 'ULFRBD'),
             ('........UxUUx..UxUUx..UxUUx..UxUUx..UxUUx....................................................................................................................................................................................................................UxxUx..UxxUx..UxxUx..UxxUx..UxxUx........', 'ULFRBD'),
             ('........UxUUx..UxUUx..UxUUx..UxUUx..UxUUx....................................................................................................................................................................................................................UUxxx..UUxxx..UUxxx..UUxxx..UUxxx........', 'ULFRBD'),
             ('........UxUUU..UxUUU..UxUUU..UxUUU..UxUUU....................................................................................................................................................................................................................xxxUx..xxxUx..xxxUx..xxxUx..xxxUx........', 'ULFRBD'),
             ('........UxUUU..UxUUU..UxUUU..UxUUU..UxUUU....................................................................................................................................................................................................................xUxxx..xUxxx..xUxxx..xUxxx..xUxxx........', 'ULFRBD'),
             ('........UUUxx..UUUxx..UUUxx..UUUxx..UUUxx....................................................................................................................................................................................................................xxxUU..xxxUU..xxxUU..xxxUU..xxxUU........', 'ULFRBD'),
             ('........UUUxx..UUUxx..UUUxx..UUUxx..UUUxx....................................................................................................................................................................................................................xUxxU..xUxxU..xUxxU..xUxxU..xUxxU........', 'ULFRBD'),
             ('........UUUxx..UUUxx..UUUxx..UUUxx..UUUxx....................................................................................................................................................................................................................UxxUx..UxxUx..UxxUx..UxxUx..UxxUx........', 'ULFRBD'),
             ('........UUUxx..UUUxx..UUUxx..UUUxx..UUUxx....................................................................................................................................................................................................................UUxxx..UUxxx..UUxxx..UUxxx..UUxxx........', 'ULFRBD'),
             ('........UUUxU..UUUxU..UUUxU..UUUxU..UUUxU....................................................................................................................................................................................................................xxxUx..xxxUx..xxxUx..xxxUx..xxxUx........', 'ULFRBD'),
             ('........UUUxU..UUUxU..UUUxU..UUUxU..UUUxU....................................................................................................................................................................................................................xUxxx..xUxxx..xUxxx..xUxxx..xUxxx........', 'ULFRBD'),
             ('........UUUUx..UUUUx..UUUUx..UUUUx..UUUUx....................................................................................................................................................................................................................xxxxU..xxxxU..xxxxU..xxxxU..xxxxU........', 'ULFRBD'),
             ('........UUUUx..UUUUx..UUUUx..UUUUx..UUUUx....................................................................................................................................................................................................................Uxxxx..Uxxxx..Uxxxx..Uxxxx..Uxxxx........', 'ULFRBD'),
             ('........UUUUU..UUUUU..UUUUU..UUUUU..UUUUU....................................................................................................................................................................................................................xxxxx..xxxxx..xxxxx..xxxxx..xxxxx........', 'ULFRBD'))
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
            True, # store_as_hex
            (("""
                . . . . . . .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . L L L L L .  . F F F F F .  . x x x x x .  . x x x x x .
 . L L L L L .  . F F F F F .  . x x x x x .  . x x x x x .
 . L L L L L .  . F F F F F .  . x x x x x .  . x x x x x .
 . L L L L L .  . F F F F F .  . x x x x x .  . x x x x x .
 . L L L L L .  . F F F F F .  . x x x x x .  . x x x x x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . x x x x x .
                . x x x x x .
                . x x x x x .
                . x x x x x .
                . x x x x x .
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


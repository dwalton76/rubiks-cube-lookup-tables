#!/usr/bin/env python3

from buildercore import BFS
import logging
import sys

log = logging.getLogger(__name__)

# TODO
# - rebuild the step41 table on LJ's machine, it now is 2-edges anywhere
#   with any orientation...maybe I started rebuilding and the counts are all the same
#   Can't hurt but is low priority

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


# =====================================
# Staging L4E Edges with solved centers
# =====================================
class Build555EdgesStageFirstFour(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-stage-first-four',
            (),
            '5x5x5',
            'lookup-table-5x5x5-step200-stage-first-four-edges.txt',
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


class Build555EdgesSolveSecondFourEdgesOnly(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.
    """

    # dwalton - this is building now on LJs machine but is named 242...rename it when it finishes
    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-solve-second-four-edges-only',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step241-solve-second-four-edges-edges-only.txt',
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


class Build555ULFRBDCenterSolveSecondFour(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-solve-second-four-centers-only',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step242-ULFRBD-centers-solve.txt',
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
                "U", "U'", "U2",
                "D", "D'", "D2",
                "L2", "F2", "R2", "B2",
                "Lw2", "Fw2", "Rw2", "Bw2",
            )
        )




class Build555EdgesSolveSecondFour(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.
    """

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-solve-second-four',

            # illegal moves
            (),

            '5x5x5',
            'lookup-table-5x5x5-step240-solve-second-four-edges.txt',
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
class Build555EdgesLastFourXPlaneEdgesOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-last-four-x-plane-edges-only',
             (), # illegal moves
            '5x5x5',
            'lookup-table-5x5x5-step221-edges-last-four-x-plane-edges-only.txt',
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


class Build555EdgesLastFourXPlaneCentersOnly(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-last-four-x-plane-centers-only',
             (), # illegal moves
            '5x5x5',
            'lookup-table-5x5x5-step222-edges-last-four-x-plane-centers-only.txt',
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


class Build555EdgesLastFourXPlane(BFS):

    def __init__(self):
        BFS.__init__(self,
            '5x5x5-edges-last-four-x-plane',
             (), # illegal moves
            '5x5x5',
            'lookup-table-5x5x5-step220-edges-last-four-x-plane.txt',
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


'''
1st L4E brainstorm...
Can we pair the first L4E group without staging first?
    - If there are 4-edges that are spread over 8 or fewer edges then we could
      use the "pair second L4E" table. We would have to do some pre-steps to move
      those 8-edges to y-plane and z-plane in order to use the "pair second L4E"
      table.
    - No idea how many steps this would take..would not need centers solved though just
        - vertical bar LR
        - vertical bar FB
        - UD can be anything
        - This would allow us to use the 2nd L4E table
        ~5 moves??

or

- Do not solve the centers instead do:
    - LR centers to one of 432 states solveable without L L' R R'
    - FB centers staged
        - can we do this without staging these centers?
        - (16!/(4!*4!*8!))^2 = 811,620,810,000
        - (16!/(4!*4!*8!)) / (16!/(4!*4!*8!))^2 = 0.000 001
        - slow but doable

- then do
    - LR and FB centers to vertical bars
    - UD centers to anything
    - stage the 1st L4E group to one of
        - the x-plane
        - outside the x-plane so we can use the "second L4E" table
        - which is better? Outside the x-plane would have many more goal
          states and would be more flexible.
    - the edges table here is (12!/(8!*4!)) * (24!/(16!*8!)) or 364,058,145
    - 364058145 / (364058145 * 432 * 4900) = 0.000 000 472 so slow but might be doable
        given the flexibility we have in picking which 4-edges to stage.


2nd L4E brainstorm...
Can we pair the second L4E group without staging first?
    - use IDA
    - centers prune table is pretty small, it goes 9-deep and averages 6.78 moves
        176,400 states (4900 * 6 * 6)
    - midge orientation will not change so only wings change
        There should be 16*15*14*13*12*11*10*9 or 518,918,400 entries
        I think this will average ~11.5 moves...building now on LJs machine

        There will be 70 wing_str combos to choose from though so that will bring
            down the realistic average.  Say we average ~10 for this.

    - 518,918,400 / (518,918,400 * 176,400) = 0.000 005 so maybe slow but feasible
    - Do we really need to solve the UD LR centers or can we bar them?
        - if we are solving the 2nd L4E group then we need to:
            - vertical bar LR
            - horizontal bar UD
            - solve FB
            - let the 3rd L4E steps solve those centers.  The 3rd L4E will need to use IDA but that is an easy change.
            ~12 moves?
        - if we are solving the 1st L4E group then we need to
            - horizontal bar UD
            - horizontal bar FB...given move restrictions I do not think this is possible, we will have to solve FB
            - LR can be anything
            ~12 moves?

So that would be:
    17 moves for 1st L4E
    12 moves for 2nd L4E
    11 moves for 3rd L4E

40 moves...if that happened I would be very happy, it takes 50 moves today
'''

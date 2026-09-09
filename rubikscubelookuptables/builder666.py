# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)

"""
phase 1
    stage the inner-x centers via 444 solver

phase 2
    pair the LR oblique edges
    This happens via C via a heuristic formula based on unpaired LR oblique count so there is no table to build

phase 3
    stage LR centers via 555

phase 4
    pair the UD oblique edges and outer x-centers to finish staging centers

phase 5
    solve the UD inner x-centers and pair the UD oblique edges

phase 6
    solve the LR inner x-centers and pair the LR oblique edges
    solve the FB inner x-centers and pair the FB oblique edges
"""


# =======
# phase 1
# =======
class Build666LRInnerXCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-LR-inner-x-centers-stage",
            (),
            "6x6x6",
            "lookup-table-6x6x6-step00-inner-x-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . . . . .
              . . x x . .
              . . x x . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . . L L . .  . . x x . .  . . L L . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . x x . .
              . . x x . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build666InnerXCentersStageOnePhase(BFS):
    """
    Stage all 24 inner x-centers in one phase (8 UD, 8 LR, 8 FB).

    24! / (8!^3) = 9,465,511,770 states. Built as a ranked cost-only table.
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-inner-x-centers-stage-one-phase",
            (),
            "6x6x6",
            "lookup-table-6x6x6-step05-inner-x-centers-stage-one-phase.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . L L . .  . . F F . .  . . L L . .  . . F F . .
 . . L L . .  . . F F . .  . . L L . .  . . F F . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
            use_ranked_cost=True,
        )
        # fmt: on



# =======
# phase 3
# =======

PHASE3_PRESERVE_LR_AND_INNER_X_ILLEGAL_MOVES = (
    "3Uw",
    "3Uw'",
    "3Lw",
    "3Lw'",
    "3Fw",
    "3Fw'",
    "3Rw",
    "3Rw'",
    "3Bw",
    "3Bw'",
    "3Dw",
    "3Dw'",
    "Uw",
    "Uw'",
    "Dw",
    "Dw'",
    "Fw",
    "Fw'",
    "Bw",
    "Bw'",
    "L",
    "L'",
    "L2",
    "R",
    "R'",
    "R2",
)

UFBD_OUTER_X_CENTERS_666 = (
    8, 11, 26, 29,
    80, 83, 98, 101,
    152, 155, 170, 173,
    188, 191, 206, 209,
)
UFBD_LEFT_OBLIQUE_EDGES_666 = (
    9, 17, 20, 28,
    81, 89, 92, 100,
    153, 161, 164, 172,
    189, 197, 200, 208,
)
UFBD_RIGHT_OBLIQUE_EDGES_666 = (
    10, 14, 23, 27,
    82, 86, 95, 99,
    154, 158, 167, 171,
    190, 194, 203, 207,
)


class Build666Phase3UDLeftRightObliqueCentersStage(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "6x6x6-phase3-UD-left-right-oblique-centers-stage",
            PHASE3_PRESERVE_LR_AND_INNER_X_ILLEGAL_MOVES,
            "6x6x6",
            "lookup-table-6x6x6-step31-UD-left-right-oblique-centers-stage.txt",
            False,
            (
                (
                    """
              . . . . . .
              . . U U . .
              . U . . U .
              . U . . U .
              . . U U . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . x x . .  . . . . . .  . . x x . .
 . . . . . .  . x . . x .  . . . . . .  . x . . x .
 . . . . . .  . x . . x .  . . . . . .  . x . . x .
 . . . . . .  . . x x . .  . . . . . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . U U . .
              . U . . U .
              . U . . U .
              . . U U . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=(
                UFBD_LEFT_OBLIQUE_EDGES_666,
                UFBD_RIGHT_OBLIQUE_EDGES_666,
            ),
        )


class Build666Phase3UDLeftObliqueOuterXCentersStage(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "6x6x6-phase3-UD-left-oblique-outer-x-centers-stage",
            PHASE3_PRESERVE_LR_AND_INNER_X_ILLEGAL_MOVES,
            "6x6x6",
            "lookup-table-6x6x6-step32-UD-left-oblique-outer-x-centers-stage.txt",
            False,
            (
                (
                    """
              . . . . . .
              . U U . U .
              . . . . U .
              . U . . . .
              . U . U U .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . x x . x .  . . . . . .  . x x . x .
 . . . . . .  . . . . x .  . . . . . .  . . . . x .
 . . . . . .  . x . . . .  . . . . . .  . x . . . .
 . . . . . .  . x . x x .  . . . . . .  . x . x x .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . U U . U .
              . . . . U .
              . U . . . .
              . U . U U .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=(
                UFBD_LEFT_OBLIQUE_EDGES_666,
                UFBD_OUTER_X_CENTERS_666,
            ),
        )


class Build666Phase3UDRightObliqueOuterXCentersStage(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "6x6x6-phase3-UD-right-oblique-outer-x-centers-stage",
            PHASE3_PRESERVE_LR_AND_INNER_X_ILLEGAL_MOVES,
            "6x6x6",
            "lookup-table-6x6x6-step33-UD-right-oblique-outer-x-centers-stage.txt",
            False,
            (
                (
                    """
              . . . . . .
              . U . U U .
              . U . . . .
              . . . . U .
              . U U . U .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . x . x x .  . . . . . .  . x . x x .
 . . . . . .  . x . . . .  . . . . . .  . x . . . .
 . . . . . .  . . . . x .  . . . . . .  . . . . x .
 . . . . . .  . x x . x .  . . . . . .  . x x . x .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . U . U U .
              . U . . . .
              . . . . U .
              . U U . U .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=(
                UFBD_RIGHT_OBLIQUE_EDGES_666,
                UFBD_OUTER_X_CENTERS_666,
            ),
        )


class Build666UDInnerXCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-inner-x-centers-stage",
            (
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step11-UD-inner-x-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . x x . .  . . . . . .  . . x x . .
 . . . . . .  . . x x . .  . . . . . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build666UDLeftObliqueCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-left-oblique-centers-stage",
            (
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step13-UD-left-oblique-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . U . . .
              . . . . U .
              . U . . . .
              . . . U . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . x . . .  . . . . . .  . . x . . .
 . . . . . .  . . . . x .  . . . . . .  . . . . x .
 . . . . . .  . x . . . .  . . . . . .  . x . . . .
 . . . . . .  . . . x . .  . . . . . .  . . . x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . U . . .
              . . . . U .
              . U . . . .
              . . . U . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build666UDRightObliqueCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-right-oblique-centers-stage",
            (
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step14-UD-right-oblique-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . . U . .
              . U . . . .
              . . . . U .
              . . U . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . x . .  . . . . . .  . . . x . .
 . . . . . .  . x . . . .  . . . . . .  . x . . . .
 . . . . . .  . . . . x .  . . . . . .  . . . . x .
 . . . . . .  . . x . . .  . . . . . .  . . x . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . U . .
              . U . . . .
              . . . . U .
              . . U . . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


# perfect hash table
class Build666UDObliqueCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-oblique-centers-stage",
            (
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step15-UD-oblique-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . U U . .
              . U . . U .
              . U . . U .
              . . U U . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . x x . .  . . . . . .  . . x x . .
 . . . . . .  . x . . x .  . . . . . .  . x . . x .
 . . . . . .  . x . . x .  . . . . . .  . x . . x .
 . . . . . .  . . x x . .  . . . . . .  . . x x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . U U . .
              . U . . U .
              . U . . U .
              . . U U . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


# perfect hash table
class Build666UDLeftObliqueInnerXCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-left-oblique-inner-x-centers-stage",
            (
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step16-UD-left-oblique-inner-x-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . U . . .
              . . U U U .
              . U U U . .
              . . . U . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . x . . .  . . . . . .  . . x . . .
 . . . . . .  . . x x x .  . . . . . .  . . x x x .
 . . . . . .  . x x x . .  . . . . . .  . x x x . .
 . . . . . .  . . . x . .  . . . . . .  . . . x . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . U . . .
              . . U U U .
              . U U U . .
              . . . U . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


# perfect hash table
class Build666UDRightObliqueInnerXCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-right-oblique-inner-x-centers-stage",
            (
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step17-UD-right-oblique-inner-x-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . . U . .
              . U U U . .
              . . U U U .
              . . U . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . x . .  . . . . . .  . . . x . .
 . . . . . .  . x x x . .  . . . . . .  . x x x . .
 . . . . . .  . . x x x .  . . . . . .  . . x x x .
 . . . . . .  . . x . . .  . . . . . .  . . x . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . U . .
              . U U U . .
              . . U U U .
              . . U . . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


# =======
# phase 5
# =======
# - put LR centers such that they can be solved with L L' R R'
# - EO the inside oribit of edges to prep for the 444 solver to pair those edge
class StartingStates666Step50LRCenters(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-step50",
            (
                "3Uw", "3Uw'", "3Uw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Rw", "3Rw'", "3Rw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Dw", "3Dw'", "3Dw2",
                "Uw", "Uw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Rw", "Rw'",
                "Bw", "Bw'",
                "Dw", "Dw'",
                "L", "L'",
                "R", "R'",
            ),
            "6x6x6",
            "starting-states-6x6x6-step50.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ("""
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . L L . .  . . . . . .  . . x x . .  . . . . . .
 . L L L L .  . . . . . .  . x x x x .  . . . . . .
 . L L L L .  . . . . . .  . x x x x .  . . . . . .
 . . L L . .  . . . . . .  . . x x . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build666Step50LRCenters(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-step50",
            (
                "3Rw", "3Rw'",
                "3Lw", "3Lw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "Rw", "Rw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step50-LR-solve-inner-x-center-and-oblique-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ('............................................LL...LLLL..LLLL...LL....................................................xx...xxxx..xxxx...xx................................................................................', 'ULFRBD'),
                ('............................................LL...LLLL..LLLL...xx....................................................LL...xxxx..xxxx...xx................................................................................', 'ULFRBD'),
                ('............................................LL...LLLL..LLLL...xx....................................................xx...xxxx..xxxx...LL................................................................................', 'ULFRBD'),
                ('............................................LL...LLLx..LLLx...LL....................................................xx...Lxxx..Lxxx...xx................................................................................', 'ULFRBD'),
                ('............................................LL...LLLx..LLLx...LL....................................................xx...xxxL..xxxL...xx................................................................................', 'ULFRBD'),
                ('............................................LL...LLLx..LLLx...xx....................................................LL...Lxxx..Lxxx...xx................................................................................', 'ULFRBD'),
                ('............................................LL...LLLx..LLLx...xx....................................................LL...xxxL..xxxL...xx................................................................................', 'ULFRBD'),
                ('............................................LL...LLLx..LLLx...xx....................................................xx...Lxxx..Lxxx...LL................................................................................', 'ULFRBD'),
                ('............................................LL...LLLx..LLLx...xx....................................................xx...xxxL..xxxL...LL................................................................................', 'ULFRBD'),
                ('............................................LL...xLLL..xLLL...LL....................................................xx...Lxxx..Lxxx...xx................................................................................', 'ULFRBD'),
                ('............................................LL...xLLL..xLLL...LL....................................................xx...xxxL..xxxL...xx................................................................................', 'ULFRBD'),
                ('............................................LL...xLLL..xLLL...xx....................................................LL...Lxxx..Lxxx...xx................................................................................', 'ULFRBD'),
                ('............................................LL...xLLL..xLLL...xx....................................................LL...xxxL..xxxL...xx................................................................................', 'ULFRBD'),
                ('............................................LL...xLLL..xLLL...xx....................................................xx...Lxxx..Lxxx...LL................................................................................', 'ULFRBD'),
                ('............................................LL...xLLL..xLLL...xx....................................................xx...xxxL..xxxL...LL................................................................................', 'ULFRBD'),
                ('............................................LL...xLLx..xLLx...LL....................................................xx...LxxL..LxxL...xx................................................................................', 'ULFRBD'),
                ('............................................LL...xLLx..xLLx...xx....................................................LL...LxxL..LxxL...xx................................................................................', 'ULFRBD'),
                ('............................................LL...xLLx..xLLx...xx....................................................xx...LxxL..LxxL...LL................................................................................', 'ULFRBD'),
                ('............................................xx...LLLL..LLLL...LL....................................................LL...xxxx..xxxx...xx................................................................................', 'ULFRBD'),
                ('............................................xx...LLLL..LLLL...LL....................................................xx...xxxx..xxxx...LL................................................................................', 'ULFRBD'),
                ('............................................xx...LLLL..LLLL...xx....................................................LL...xxxx..xxxx...LL................................................................................', 'ULFRBD'),
                ('............................................xx...LLLx..LLLx...LL....................................................LL...Lxxx..Lxxx...xx................................................................................', 'ULFRBD'),
                ('............................................xx...LLLx..LLLx...LL....................................................LL...xxxL..xxxL...xx................................................................................', 'ULFRBD'),
                ('............................................xx...LLLx..LLLx...LL....................................................xx...Lxxx..Lxxx...LL................................................................................', 'ULFRBD'),
                ('............................................xx...LLLx..LLLx...LL....................................................xx...xxxL..xxxL...LL................................................................................', 'ULFRBD'),
                ('............................................xx...LLLx..LLLx...xx....................................................LL...Lxxx..Lxxx...LL................................................................................', 'ULFRBD'),
                ('............................................xx...LLLx..LLLx...xx....................................................LL...xxxL..xxxL...LL................................................................................', 'ULFRBD'),
                ('............................................xx...xLLL..xLLL...LL....................................................LL...Lxxx..Lxxx...xx................................................................................', 'ULFRBD'),
                ('............................................xx...xLLL..xLLL...LL....................................................LL...xxxL..xxxL...xx................................................................................', 'ULFRBD'),
                ('............................................xx...xLLL..xLLL...LL....................................................xx...Lxxx..Lxxx...LL................................................................................', 'ULFRBD'),
                ('............................................xx...xLLL..xLLL...LL....................................................xx...xxxL..xxxL...LL................................................................................', 'ULFRBD'),
                ('............................................xx...xLLL..xLLL...xx....................................................LL...Lxxx..Lxxx...LL................................................................................', 'ULFRBD'),
                ('............................................xx...xLLL..xLLL...xx....................................................LL...xxxL..xxxL...LL................................................................................', 'ULFRBD'),
                ('............................................xx...xLLx..xLLx...LL....................................................LL...LxxL..LxxL...xx................................................................................', 'ULFRBD'),
                ('............................................xx...xLLx..xLLx...LL....................................................xx...LxxL..LxxL...LL................................................................................', 'ULFRBD'),
                ('............................................xx...xLLx..xLLx...xx....................................................LL...LxxL..LxxL...LL................................................................................', 'ULFRBD'),
            ),
            use_c=True,
        )
        # fmt: on


class Build666Step50HighLowEdges(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "666-highlow-edges",
            # fmt: off
            (
                "3Rw", "3Rw'",
                "3Lw", "3Lw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "Rw", "Rw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",
            ),
            # fmt: on
            "6x6x6",
            "lookup-table-6x6x6-step51-highlow-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . U D . .
              . . . . . .
              D . . . . U
              U . . . . D
              . . . . . .
              . . D U . .

 . . D U . .  . . D U . .  . . D U . .  . . D U . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 D . . . . U  U . . . . D  D . . . . U  U . . . . D
 U . . . . D  D . . . . U  U . . . . D  D . . . . U
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . U D . .  . . U D . .  . . U D . .  . . U D . .

              . . U D . .
              . . . . . .
              D . . . . U
              U . . . . D
              . . . . . .
              . . D U . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


# =======
# phase 6
# =======
# - solve the UD inner x-centers and pair the LR oblique edges
# - solve the FB inner x-centers and pair the FB oblique edges
class Build666UDInnerXCenterAndObliqueEdges(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-solve-inner-x-center-and-oblique-edges",
            (
                # do not mess up staged centers
                "3Rw", "3Rw'",
                "3Lw", "3Lw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",

                # do not mess up staged centers
                "Rw", "Rw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",

                # do not mess up solved LR
                "3Uw2",
                "3Dw2",
                "3Fw2",
                "3Bw2",

                # do not mess up the EOed edges
                "L", "L'",
                "R", "R'",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step61-UD-solve-inner-x-center-and-oblique-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (("""
              . . . . . .
              . . U U . .
              . U U U U .
              . U U U U .
              . . U U . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . D D . .
              . D D D D .
              . D D D D .
              . . D D . .
              . . . . . .""", "ascii",
                ),
                ("""
              . . . . . .
              . . D D . .
              . D U U D .
              . D U U D .
              . . D D . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . U U . .
              . U D D U .
              . U D D U .
              . . U U . .
              . . . . . .""", "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build666FBInnerXCenterAndObliqueEdges(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-FB-solve-inner-x-center-and-oblique-edges",
            (
                # do not mess up staged centers
                "3Rw", "3Rw'",
                "3Lw", "3Lw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",

                # do not mess up staged centers
                "Rw", "Rw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",

                # do not mess up solved LR
                "3Uw2",
                "3Dw2",
                "3Fw2",
                "3Bw2",

                # do not mess up the EOed edges
                "L", "L'",
                "R", "R'",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step62-FB-solve-inner-x-center-and-oblique-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . B B . .  . . . . . .  . . F F . .
 . . . . . .  . B F F B .  . . . . . .  . F B B F .
 . . . . . .  . B F F B .  . . . . . .  . F B B F .
 . . . . . .  . . B B . .  . . . . . .  . . F F . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),
                (
                    """
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . . . . .  . . F F . .  . . . . . .  . . B B . .
 . . . . . .  . F F F F .  . . . . . .  . B B B B .
 . . . . . .  . F F F F .  . . . . . .  . B B B B .
 . . . . . .  . . F F . .  . . . . . .  . . B B . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build666LRObliqueEdges(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-LR-oblique-edges",
            (
                # do not mess up staged centers
                "3Rw", "3Rw'",
                "3Lw", "3Lw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",

                # do not mess up staged centers
                "Rw", "Rw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "Uw", "Uw'",
                "Dw", "Dw'",

                # do not mess up solved LR
                "3Uw2",
                "3Dw2",
                "3Fw2",
                "3Bw2",

                # do not mess up the EOed edges
                "L", "L'",
                "R", "R'",
            ),
            "6x6x6",
            "lookup-table-6x6x6-step63-LR-oblique-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . L L . .  . . . . . .  . . R R . .  . . . . . .
 . L . . L .  . . F F . .  . R . . R .  . . B B . .
 . L . . L .  . . F F . .  . R . . R .  . . B B . .
 . . L L . .  . . . . . .  . . R R . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . D D . .
              . . D D . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),
                (
                    """
              . . . . . .
              . . . . . .
              . . U U . .
              . . U U . .
              . . . . . .
              . . . . . .

 . . . . . .  . . . . . .  . . . . . .  . . . . . .
 . . R R . .  . . . . . .  . . L L . .  . . . . . .
 . R . . R .  . . F F . .  . L . . L .  . . B B . .
 . R . . R .  . . F F . .  . L . . L .  . . B B . .
 . . R R . .  . . . . . .  . . L L . .  . . . . . .
 . . . . . .  . . . . . .  . . . . . .  . . . . . .

              . . . . . .
              . . . . . .
              . . D D . .
              . . D D . .
              . . . . . .
              . . . . . .""",
                    "ascii",
                ),

            ),
            use_c=True,
        )
        # fmt: on

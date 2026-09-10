# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)


# fmt: off
PHASE3_PRESERVE_LR_AND_INNER_X_ILLEGAL_MOVES = (
    # keep inner x-centers and LR staging
    "3Uw", "3Uw'",
    "3Lw", "3Lw'",
    "3Fw", "3Fw'",
    "3Rw", "3Rw'",
    "3Bw", "3Bw'",
    "3Dw", "3Dw'",
    "Uw", "Uw'",
    "Dw", "Dw'",
    "Fw", "Fw'",
    "Bw", "Bw'",
    "L", "L'", "L2",
    "R", "R'", "R2",
)

PHASE5_ILLEGAL_MOVES = (
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
)

PHASE5_STARTING_STATES_ILLEGAL_MOVES = (
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
)

PHASE6_ILLEGAL_MOVES = (
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
    "3Uw2",
    "3Dw2",
    "3Fw2",
    "3Bw2",
    "L", "L'",
    "R", "R'",
)

# fmt: on


# ==================================================
# phase 1
# stage all inner x-centers and pair the LR obliques
# ==================================================
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


# ==================================================
# phase 3
# stage UD left/right obliques and outer x-centers
# ==================================================
# fmt: off
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
# fmt: on


class Build666Phase3UDLeftRightObliqueCentersStage(BFS):
    """
    (16! / (8! * 8!))^2 = 165,636,900 states

    lookup-table-6x6x6-step31-UD-left-right-oblique-centers-stage.cost-only.bin
    ===========================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 29 entries (0 percent, 14.50x previous step)
    3 steps has 286 entries (0 percent, 9.86x previous step)
    4 steps has 2,052 entries (0 percent, 7.17x previous step)
    5 steps has 16,348 entries (0 percent, 7.97x previous step)
    6 steps has 127,859 entries (0 percent, 7.82x previous step)
    7 steps has 844,248 entries (0 percent, 6.60x previous step)
    8 steps has 4,623,585 entries (2 percent, 5.48x previous step)
    9 steps has 19,019,322 entries (11 percent, 4.11x previous step)
    10 steps has 47,544,426 entries (28 percent, 2.50x previous step)
    11 steps has 61,805,656 entries (37 percent, 1.30x previous step)
    12 steps has 28,890,234 entries (17 percent, 0.47x previous step)
    13 steps has 2,722,462 entries (1 percent, 0.09x previous step)
    14 steps has 40,242 entries (0 percent, 0.01x previous step)
    15 steps has 148 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 10.58 moves
    """

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
    """
    (16! / (8! * 8!))^2 = 165,636,900 states

    lookup-table-6x6x6-step32-UD-left-oblique-outer-x-centers-stage.cost-only.bin
    =============================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 37 entries (0 percent, 18.50x previous step)
    3 steps has 426 entries (0 percent, 11.51x previous step)
    4 steps has 4,552 entries (0 percent, 10.69x previous step)
    5 steps has 48,826 entries (0 percent, 10.73x previous step)
    6 steps has 497,305 entries (0 percent, 10.19x previous step)
    7 steps has 4,366,446 entries (2 percent, 8.78x previous step)
    8 steps has 25,800,644 entries (15 percent, 5.91x previous step)
    9 steps has 71,891,909 entries (43 percent, 2.79x previous step)
    10 steps has 57,817,231 entries (34 percent, 0.80x previous step)
    11 steps has 5,204,126 entries (3 percent, 0.09x previous step)
    12 steps has 5,395 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 9.19 moves
    """

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
    """
    (16! / (8! * 8!))^2 = 165,636,900 states

    lookup-table-6x6x6-step33-UD-right-oblique-outer-x-centers-stage.cost-only.bin
    ==============================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 37 entries (0 percent, 18.50x previous step)
    3 steps has 426 entries (0 percent, 11.51x previous step)
    4 steps has 4,552 entries (0 percent, 10.69x previous step)
    5 steps has 48,826 entries (0 percent, 10.73x previous step)
    6 steps has 497,305 entries (0 percent, 10.19x previous step)
    7 steps has 4,366,446 entries (2 percent, 8.78x previous step)
    8 steps has 25,800,644 entries (15 percent, 5.91x previous step)
    9 steps has 71,891,909 entries (43 percent, 2.79x previous step)
    10 steps has 57,817,231 entries (34 percent, 0.80x previous step)
    11 steps has 5,204,126 entries (3 percent, 0.09x previous step)
    12 steps has 5,395 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 9.19 moves
    """

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


# ==================================================
# phase 5
# LR centers to daisy and EO the inside wings
# ==================================================
# - put LR centers such that they can be solved with L L' R R'
# - EO the inside oribit of edges to prep for the 444 solver to pair those edge
class StartingStates666Step50LRCenters(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-step50",
            PHASE5_STARTING_STATES_ILLEGAL_MOVES,
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
    """
    (8! / (4! * 4!))^3 = 343,000 states

    lookup-table-6x6x6-step50-LR-solve-inner-x-center-and-oblique-edges.txt
    =======================================================================
    0 steps has 36 entries (0 percent, 0.00x previous step)
    1 steps has 162 entries (0 percent, 4.50x previous step)
    2 steps has 748 entries (0 percent, 4.62x previous step)
    3 steps has 2,914 entries (0 percent, 3.90x previous step)
    4 steps has 12,388 entries (3 percent, 4.25x previous step)
    5 steps has 44,604 entries (13 percent, 3.60x previous step)
    6 steps has 109,148 entries (31 percent, 2.45x previous step)
    7 steps has 132,424 entries (38 percent, 1.21x previous step)
    8 steps has 37,920 entries (11 percent, 0.29x previous step)
    9 steps has 2,624 entries (0 percent, 0.07x previous step)
    10 steps has 32 entries (0 percent, 0.01x previous step)

    Total: 343,000 entries
    Average: 6.39 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-step50",
            PHASE5_ILLEGAL_MOVES,
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
    """
    24! / (12! * 12!) = 2,704,156 states

    lookup-table-6x6x6-step51-highlow-edges.txt
    ===========================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 29 entries (0 percent, 14.50x previous step)
    3 steps has 278 entries (0 percent, 9.59x previous step)
    4 steps has 1,934 entries (0 percent, 6.96x previous step)
    5 steps has 15,640 entries (0 percent, 8.09x previous step)
    6 steps has 124,249 entries (4 percent, 7.94x previous step)
    7 steps has 609,241 entries (22 percent, 4.90x previous step)
    8 steps has 1,224,098 entries (45 percent, 2.01x previous step)
    9 steps has 688,124 entries (25 percent, 0.56x previous step)
    10 steps has 40,560 entries (1 percent, 0.06x previous step)

    Total: 2,704,156 entries
    Average: 7.95 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "666-highlow-edges",
            PHASE5_ILLEGAL_MOVES,
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


# ==================================================
# phase 6
# solve UD/FB inner x-centers and pair remaining obliques
# ==================================================
# - solve the UD inner x-centers and pair the LR oblique edges
# - solve the FB inner x-centers and pair the FB oblique edges
class Build666UDInnerXCenterAndObliqueEdges(BFS):
    """
    (8! / (4! * 4!))^3 = 343,000 states

    lookup-table-6x6x6-step61-UD-solve-inner-x-center-and-oblique-edges.txt
    =======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 13 entries (0 percent, 6.50x previous step)
    2 steps has 68 entries (0 percent, 5.23x previous step)
    3 steps has 282 entries (0 percent, 4.15x previous step)
    4 steps has 1,218 entries (0 percent, 4.32x previous step)
    5 steps has 5,382 entries (1 percent, 4.42x previous step)
    6 steps has 20,484 entries (5 percent, 3.81x previous step)
    7 steps has 62,640 entries (18 percent, 3.06x previous step)
    8 steps has 118,196 entries (34 percent, 1.89x previous step)
    9 steps has 104,328 entries (30 percent, 0.88x previous step)
    10 steps has 29,872 entries (8 percent, 0.29x previous step)
    11 steps has 516 entries (0 percent, 0.02x previous step)

    Total: 343,001 entries
    Average: 8.11 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-UD-solve-inner-x-center-and-oblique-edges",
            PHASE6_ILLEGAL_MOVES,
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
    """
    (8! / (4! * 4!))^3 = 343,000 states

    lookup-table-6x6x6-step62-FB-solve-inner-x-center-and-oblique-edges.txt
    =======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 12 entries (0 percent, 6.00x previous step)
    2 steps has 68 entries (0 percent, 5.67x previous step)
    3 steps has 282 entries (0 percent, 4.15x previous step)
    4 steps has 1,218 entries (0 percent, 4.32x previous step)
    5 steps has 5,382 entries (1 percent, 4.42x previous step)
    6 steps has 20,484 entries (5 percent, 3.81x previous step)
    7 steps has 62,640 entries (18 percent, 3.06x previous step)
    8 steps has 118,196 entries (34 percent, 1.89x previous step)
    9 steps has 104,328 entries (30 percent, 0.88x previous step)
    10 steps has 29,872 entries (8 percent, 0.29x previous step)
    11 steps has 516 entries (0 percent, 0.02x previous step)

    Total: 343,000 entries
    Average: 8.11 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-FB-solve-inner-x-center-and-oblique-edges",
            PHASE6_ILLEGAL_MOVES,
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
    """
    6 * 6 * 4,900 = 176,400 states

    lookup-table-6x6x6-step63-LR-oblique-edges.txt
    ==============================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 12 entries (0 percent, 6.00x previous step)
    2 steps has 96 entries (0 percent, 8.00x previous step)
    3 steps has 728 entries (0 percent, 7.58x previous step)
    4 steps has 3,446 entries (1 percent, 4.73x previous step)
    5 steps has 10,036 entries (5 percent, 2.91x previous step)
    6 steps has 26,472 entries (15 percent, 2.64x previous step)
    7 steps has 44,832 entries (25 percent, 1.69x previous step)
    8 steps has 41,312 entries (23 percent, 0.92x previous step)
    9 steps has 32,560 entries (18 percent, 0.79x previous step)
    10 steps has 15,176 entries (8 percent, 0.47x previous step)
    11 steps has 1,728 entries (0 percent, 0.11x previous step)

    Total: 176,400 entries
    Average: 7.56 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "6x6x6-LR-oblique-edges",
            PHASE6_ILLEGAL_MOVES,
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

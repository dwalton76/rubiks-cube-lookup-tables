# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS
from rubikscubennnsolver.LookupTableIDAViaGraph import LookupTableIDAViaGraph

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
    """
    24! / (8! * 16!) = 735,471 states

    lookup-table-6x6x6-step00-inner-x-centers-stage.txt
    ===================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 4 entries (0 percent, 4.00x previous step)
    2 steps has 82 entries (0 percent, 20.50x previous step)
    3 steps has 1,206 entries (0 percent, 14.71x previous step)
    4 steps has 14,116 entries (1 percent, 11.70x previous step)
    5 steps has 123,404 entries (16 percent, 8.74x previous step)
    6 steps has 422,508 entries (57 percent, 3.42x previous step)
    7 steps has 173,254 entries (23 percent, 0.41x previous step)
    8 steps has 896 entries (0 percent, 0.01x previous step)

    Total: 735,471 entries
    Average: 6.03 moves
    """

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
# fmt: off
PHASE3_PRESERVE_LR_AND_INNER_X_ILLEGAL_MOVES = (
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
    "L", "L'",
    "L2",
    "R", "R'", "R2",
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
# fmt: off


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


class Build666UDInnerXCentersStage(BFS):
    """
    16! / (8! * 8!) = 12,870 states

    lookup-table-6x6x6-step11-UD-inner-x-centers-stage.txt
    ======================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 29 entries (0 percent, 14.50x previous step)
    3 steps has 234 entries (1 percent, 8.07x previous step)
    4 steps has 1,246 entries (9 percent, 5.32x previous step)
    5 steps has 4,466 entries (34 percent, 3.58x previous step)
    6 steps has 6,236 entries (48 percent, 1.40x previous step)
    7 steps has 656 entries (5 percent, 0.11x previous step)

    Total: 12,870 entries
    Average: 5.45 moves
    """

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
    """
    16! / (8! * 8!) = 12,870 states

    lookup-table-6x6x6-step13-UD-left-oblique-centers.txt
    =====================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 4 entries (0 percent, 4.00x previous step)
    2 steps has 70 entries (0 percent, 17.50x previous step)
    3 steps has 804 entries (6 percent, 11.49x previous step)
    4 steps has 4,615 entries (35 percent, 5.74x previous step)
    5 steps has 7,048 entries (54 percent, 1.53x previous step)
    6 steps has 328 entries (2 percent, 0.05x previous step)

    Total: 12,870 entries
    Average: 4.52 moves
    """

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
    """
    16! / (8! * 8!) = 12,870 states

    lookup-table-6x6x6-step14-UD-right-oblique-centers.txt
    ======================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 4 entries (0 percent, 4.00x previous step)
    2 steps has 70 entries (0 percent, 17.50x previous step)
    3 steps has 804 entries (6 percent, 11.49x previous step)
    4 steps has 4,615 entries (35 percent, 5.74x previous step)
    5 steps has 7,048 entries (54 percent, 1.53x previous step)
    6 steps has 328 entries (2 percent, 0.05x previous step)

    Total: 12,870 entries
    Average: 4.52 moves
    """

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


class LookupTableIDA666UDObliqueEdgesStage(LookupTableIDAViaGraph):
    """
    This was only used to build the lookup-table-6x6x6-step14-UD-oblique-stage.pt_state
    file which was then converted to lookup-table-6x6x6-step14-UD-oblique-stage.pt-state-perfect-hash
    lookup-table-6x6x6-step14-UD-oblique-stage.txt
    ==============================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 29 entries (0 percent, 14.50x previous step)
    3 steps has 286 entries (0 percent, 9.86x previous step)
    4 steps has 2,020 entries (0 percent, 7.06x previous step)
    5 steps has 15,992 entries (0 percent, 7.92x previous step)
    6 steps has 123,071 entries (0 percent, 7.70x previous step)
    7 steps has 805,821 entries (0 percent, 6.55x previous step)
    8 steps has 4,379,750 entries (2 percent, 5.44x previous step)
    9 steps has 18,300,990 entries (11 percent, 4.18x previous step)
    10 steps has 46,881,308 entries (28 percent, 2.56x previous step)
    11 steps has 62,357,957 entries (37 percent, 1.33x previous step)
    12 steps has 29,875,621 entries (18 percent, 0.48x previous step)
    13 steps has 2,852,222 entries (1 percent, 0.10x previous step)
    14 steps has 41,682 entries (0 percent, 0.01x previous step)
    15 steps has 148 entries (0 percent, 0.00x previous step)
    Total: 165,636,900 entries
    Average: 10.61 moves
    """
    state_targets = (
        "UUUUUUUUxxxxxxxxxxxxxxxxUUUUUUUU",
    )
    def __init__(self, parent):
        # fmt: off
        LookupTableIDAViaGraph.__init__(
            self,
            parent,
            filename="lookup-table-6x6x6-step14-UD-oblique-stage.txt",
            state_target=self.state_targets,
            linecount=165636900,
            max_depth=15,
            all_moves=moves_666,
            illegal_moves=(
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
                # we are not manipulating anything on sides L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            prune_tables=(
                parent.lt_UD_left_oblique_edges_stage,
                parent.lt_UD_right_oblique_edges_stage,
            ),
        )
        # fmt: on

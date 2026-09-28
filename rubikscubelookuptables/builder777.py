# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)


# fmt: off
PHASE2_ILLEGAL_MOVES = (
    # preserve the staged LR inner centers
    "3Uw", "3Uw'",
    "3Dw", "3Dw'",
    "3Fw", "3Fw'",
    "3Bw", "3Bw'",
)

PHASE5_ILLEGAL_MOVES = (
    # keep LR inside centers staged
    "3Uw", "3Uw'",
    "3Dw", "3Dw'",
    "3Fw", "3Fw'",
    "3Bw", "3Bw'",
    "3Lw", "3Lw'",
    "3Rw", "3Rw'",
    # keep LR centers staged
    "Uw", "Uw'",
    "Dw", "Dw'",
    "Fw", "Fw'",
    "Bw", "Bw'",
    # we are not manipulating anything on L or R
    "L", "L'", "L2",
    "R", "R'", "R2",
)

# fmt: on


# ==================================================
# phase 2
# stage UD inner t/x centers while pairing LR obliques
# ==================================================
# fmt: off
UFBD_INNER_T_CENTERS_777 = (
    18, 24, 26, 32,
    116, 122, 124, 130,
    214, 220, 222, 228,
    263, 269, 271, 277,
)
UFBD_INNER_X_CENTERS_777 = (
    17, 19, 31, 33,
    115, 117, 129, 131,
    213, 215, 227, 229,
    262, 264, 276, 278,
)
UFBD_OUTER_X_CENTERS_777 = (
    9, 13, 37, 41,
    107, 111, 135, 139,
    205, 209, 233, 237,
    254, 258, 282, 286,
)
UFBD_LEFT_OBLIQUE_EDGES_777 = (
    10, 20, 30, 40,
    108, 118, 128, 138,
    206, 216, 226, 236,
    255, 265, 275, 285,
)
UFBD_MIDDLE_OBLIQUE_EDGES_777 = (
    11, 23, 27, 39,
    109, 121, 125, 137,
    207, 219, 223, 235,
    256, 268, 272, 284,
)
UFBD_RIGHT_OBLIQUE_EDGES_777 = (
    12, 16, 34, 38,
    110, 114, 132, 136,
    208, 212, 230, 234,
    257, 261, 279, 283,
)
# fmt: on


class Build777Phase2UDInnerCentersStage(BFS):
    """
    Stage the UD inner t-centers and inner x-centers while the LR obliques pair.

    Two orbits are ranked, the inner t-centers and the inner x-centers. Each
    spans the 16 U, F, B and D squares of its kind with eight of them destined
    for U or D, so each contributes 16! / (8! * 8!) = 12,870 and the coordinate
    is (16! / (8! * 8!))^2 = 165,636,900 states. __init__ carries the ascii goal.

    lookup-table-7x7x7-step20-UD-inner-centers-stage.cost-only.bin
    ==============================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 33 entries (0 percent, 16.50x previous step)
    3 steps has 374 entries (0 percent, 11.33x previous step)
    4 steps has 3,838 entries (0 percent, 10.26x previous step)
    5 steps has 39,254 entries (0 percent, 10.23x previous step)
    6 steps has 387,357 entries (0 percent, 9.87x previous step)
    7 steps has 3,374,380 entries (2 percent, 8.71x previous step)
    8 steps has 20,851,334 entries (12 percent, 6.18x previous step)
    9 steps has 65,556,972 entries (39 percent, 3.14x previous step)
    10 steps has 66,986,957 entries (40 percent, 1.02x previous step)
    11 steps has 8,423,610 entries (5 percent, 0.13x previous step)
    12 steps has 12,788 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 9.33 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "7x7x7-phase2-UD-inner-centers-stage",
            PHASE2_ILLEGAL_MOVES,
            "7x7x7",
            "lookup-table-7x7x7-step20-UD-inner-centers-stage.txt",
            False,
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . U U U . .
                . . U . U . .
                . . U U U . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . U U U . .
                . . U . U . .
                . . U U U . .
                . . . . . . .
                . . . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=(
                UFBD_INNER_T_CENTERS_777,
                UFBD_INNER_X_CENTERS_777,
            ),
        )


# ==================================================
# combined phases 5/6
# stage UD outer x-centers and pair UD obliques
# ==================================================
def _ranked_ud_pair_starting_state_777(first_group, second_group):
    """Return a solved UD-vs-other state for two 16-sticker coordinates."""
    state = ["."] * (6 * 7 * 7)

    for square in first_group + second_group:
        # U and D occupy indexes 1..49 and 246..294 in the builder's ULFRBD numbering.
        state[square - 1] = "U" if square <= 49 or square >= 246 else "x"

    return (("".join(state), "ULFRBD"),)


class _Build777Phase56UDPairStage(BFS):
    """Shared ranked-cost setup for a pair of 12,870-state coordinates."""

    table_slug = None
    first_group = ()
    second_group = ()

    def __init__(self):
        BFS.__init__(
            self,
            f"7x7x7-phase5-6-UD-{self.table_slug}-centers-stage",
            PHASE5_ILLEGAL_MOVES,
            "7x7x7",
            f"lookup-table-7x7x7-phase5-6-UD-{self.table_slug}-centers-stage.txt",
            False,
            _ranked_ud_pair_starting_state_777(self.first_group, self.second_group),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=(self.first_group, self.second_group),
        )


class Build777Phase56UDLeftRightObliqueCentersStage(_Build777Phase56UDPairStage):
    """
    Rank the left and right oblique coordinates.

    Each orbit spans the 16 U, F, B and D squares of its kind with eight of them
    destined for U or D, so each contributes 16! / (8! * 8!) = 12,870 and the pair
    gives (16! / (8! * 8!))^2 = 165,636,900 states.

    _ranked_ud_pair_starting_state_777 encodes the single goal rather than passing
    an ascii cube, so it is drawn here:

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
                   . . . . . . .

    lookup-table-7x7x7-phase5-6-UD-left-right-oblique-centers-stage.cost-only.bin
    =============================================================================
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

    table_slug = "left-right-oblique"
    first_group = UFBD_LEFT_OBLIQUE_EDGES_777
    second_group = UFBD_RIGHT_OBLIQUE_EDGES_777


class Build777Phase56UDLeftMiddleObliqueCentersStage(_Build777Phase56UDPairStage):
    """
    Rank the left and middle oblique coordinates.

    Each orbit spans the 16 U, F, B and D squares of its kind with eight of them
    destined for U or D, so each contributes 16! / (8! * 8!) = 12,870 and the pair
    gives (16! / (8! * 8!))^2 = 165,636,900 states.

    _ranked_ud_pair_starting_state_777 encodes the single goal rather than passing
    an ascii cube, so it is drawn here:

                   . . . . . . .
                   . . U U . . .
                   . . . . . U .
                   . U . . . U .
                   . U . . . . .
                   . . . U U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . x x . . .  . . . . . . .  . . x x . . .
    . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
    . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
    . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
    . . . . . . .  . . . x x . .  . . . . . . .  . . . x x . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . U U . . .
                   . . . . . U .
                   . U . . . U .
                   . U . . . . .
                   . . . U U . .
                   . . . . . . .

    lookup-table-7x7x7-phase5-6-UD-left-middle-oblique-centers-stage.cost-only.bin
    ==============================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 33 entries (0 percent, 16.50x previous step)
    3 steps has 358 entries (0 percent, 10.85x previous step)
    4 steps has 2,934 entries (0 percent, 8.20x previous step)
    5 steps has 23,262 entries (0 percent, 7.93x previous step)
    6 steps has 155,679 entries (0 percent, 6.69x previous step)
    7 steps has 893,008 entries (0 percent, 5.74x previous step)
    8 steps has 4,447,409 entries (2 percent, 4.98x previous step)
    9 steps has 17,048,560 entries (10 percent, 3.83x previous step)
    10 steps has 41,869,962 entries (25 percent, 2.46x previous step)
    11 steps has 57,876,856 entries (34 percent, 1.38x previous step)
    12 steps has 35,846,966 entries (21 percent, 0.62x previous step)
    13 steps has 7,122,098 entries (4 percent, 0.20x previous step)
    14 steps has 346,646 entries (0 percent, 0.05x previous step)
    15 steps has 3,126 entries (0 percent, 0.01x previous step)

    Total: 165,636,900 entries
    Average: 10.74 moves
    """

    table_slug = "left-middle-oblique"
    first_group = UFBD_LEFT_OBLIQUE_EDGES_777
    second_group = UFBD_MIDDLE_OBLIQUE_EDGES_777


class Build777Phase56UDLeftObliqueOuterXCentersStage(_Build777Phase56UDPairStage):
    """
    Rank the left oblique and outer-x coordinates.

    Each orbit spans the 16 U, F, B and D squares of its kind with eight of them
    destined for U or D, so each contributes 16! / (8! * 8!) = 12,870 and the pair
    gives (16! / (8! * 8!))^2 = 165,636,900 states.

    _ranked_ud_pair_starting_state_777 encodes the single goal rather than passing
    an ascii cube, so it is drawn here:

                   . . . . . . .
                   . U U . . U .
                   . . . . . U .
                   . . . . . . .
                   . U . . . . .
                   . U . . U U .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . x x . . x .  . . . . . . .  . x x . . x .
    . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
    . . . . . . .  . x . . x x .  . . . . . . .  . x . . x x .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . U U . . U .
                   . . . . . U .
                   . . . . . . .
                   . U . . . . .
                   . U . . U U .
                   . . . . . . .

    lookup-table-7x7x7-phase5-6-UD-left-oblique-outer-x-centers-stage.cost-only.bin
    ===============================================================================
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

    table_slug = "left-oblique-outer-x"
    first_group = UFBD_LEFT_OBLIQUE_EDGES_777
    second_group = UFBD_OUTER_X_CENTERS_777


class Build777Phase56UDMiddleRightObliqueCentersStage(_Build777Phase56UDPairStage):
    """
    Rank the middle and right oblique coordinates.

    Each orbit spans the 16 U, F, B and D squares of its kind with eight of them
    destined for U or D, so each contributes 16! / (8! * 8!) = 12,870 and the pair
    gives (16! / (8! * 8!))^2 = 165,636,900 states. It mirrors the left/middle
    table, which is why the two share a histogram.

    _ranked_ud_pair_starting_state_777 encodes the single goal rather than passing
    an ascii cube, so it is drawn here:

                   . . . . . . .
                   . . . U U . .
                   . U . . . . .
                   . U . . . U .
                   . . . . . U .
                   . . U U . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . x x . .  . . . . . . .  . . . x x . .
    . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
    . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
    . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
    . . . . . . .  . . x x . . .  . . . . . . .  . . x x . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . U U . .
                   . U . . . . .
                   . U . . . U .
                   . . . . . U .
                   . . U U . . .
                   . . . . . . .

    lookup-table-7x7x7-phase5-6-UD-middle-right-oblique-centers-stage.cost-only.bin
    ===============================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 33 entries (0 percent, 16.50x previous step)
    3 steps has 358 entries (0 percent, 10.85x previous step)
    4 steps has 2,934 entries (0 percent, 8.20x previous step)
    5 steps has 23,262 entries (0 percent, 7.93x previous step)
    6 steps has 155,679 entries (0 percent, 6.69x previous step)
    7 steps has 893,008 entries (0 percent, 5.74x previous step)
    8 steps has 4,447,409 entries (2 percent, 4.98x previous step)
    9 steps has 17,048,560 entries (10 percent, 3.83x previous step)
    10 steps has 41,869,962 entries (25 percent, 2.46x previous step)
    11 steps has 57,876,856 entries (34 percent, 1.38x previous step)
    12 steps has 35,846,966 entries (21 percent, 0.62x previous step)
    13 steps has 7,122,098 entries (4 percent, 0.20x previous step)
    14 steps has 346,646 entries (0 percent, 0.05x previous step)
    15 steps has 3,126 entries (0 percent, 0.01x previous step)

    Total: 165,636,900 entries
    Average: 10.74 moves
    """

    table_slug = "middle-right-oblique"
    first_group = UFBD_MIDDLE_OBLIQUE_EDGES_777
    second_group = UFBD_RIGHT_OBLIQUE_EDGES_777


class Build777Phase56UDRightObliqueOuterXCentersStage(_Build777Phase56UDPairStage):
    """
    Rank the right oblique and outer-x coordinates.

    Each orbit spans the 16 U, F, B and D squares of its kind with eight of them
    destined for U or D, so each contributes 16! / (8! * 8!) = 12,870 and the pair
    gives (16! / (8! * 8!))^2 = 165,636,900 states. It mirrors the left
    oblique/outer-x table, which is why the two share a histogram.

    _ranked_ud_pair_starting_state_777 encodes the single goal rather than passing
    an ascii cube, so it is drawn here:

                   . . . . . . .
                   . U . . U U .
                   . U . . . . .
                   . . . . . . .
                   . . . . . U .
                   . U U . . U .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . x . . x x .  . . . . . . .  . x . . x x .
    . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
    . . . . . . .  . x x . . x .  . . . . . . .  . x x . . x .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . U . . U U .
                   . U . . . . .
                   . . . . . . .
                   . . . . . U .
                   . U U . . U .
                   . . . . . . .

    lookup-table-7x7x7-phase5-6-UD-right-oblique-outer-x-centers-stage.cost-only.bin
    ================================================================================
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

    table_slug = "right-oblique-outer-x"
    first_group = UFBD_RIGHT_OBLIQUE_EDGES_777
    second_group = UFBD_OUTER_X_CENTERS_777


class Build777Phase56UDMiddleObliqueOuterXCentersStage(_Build777Phase56UDPairStage):
    """
    Rank the middle oblique and outer-x coordinates.

    Each orbit spans the 16 U, F, B and D squares of its kind with eight of them
    destined for U or D, so each contributes 16! / (8! * 8!) = 12,870 and the pair
    gives (16! / (8! * 8!))^2 = 165,636,900 states. Both orbits are fixed by the
    mirror that swaps the left and right obliques, so this table is its own
    mirror image and matches the step20 histogram.

    _ranked_ud_pair_starting_state_777 encodes the single goal rather than passing
    an ascii cube, so it is drawn here:

                   . . . . . . .
                   . U . U . U .
                   . . . . . . .
                   . U . . . U .
                   . . . . . . .
                   . U . U . U .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . x . x . x .  . . . . . . .  . x . x . x .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . x . x . x .  . . . . . . .  . x . x . x .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . U . U . U .
                   . . . . . . .
                   . U . . . U .
                   . . . . . . .
                   . U . U . U .
                   . . . . . . .

    lookup-table-7x7x7-phase5-6-UD-middle-oblique-outer-x-centers-stage.cost-only.bin
    =================================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 33 entries (0 percent, 16.50x previous step)
    3 steps has 374 entries (0 percent, 11.33x previous step)
    4 steps has 3,838 entries (0 percent, 10.26x previous step)
    5 steps has 39,254 entries (0 percent, 10.23x previous step)
    6 steps has 387,357 entries (0 percent, 9.87x previous step)
    7 steps has 3,374,380 entries (2 percent, 8.71x previous step)
    8 steps has 20,851,334 entries (12 percent, 6.18x previous step)
    9 steps has 65,556,972 entries (39 percent, 3.14x previous step)
    10 steps has 66,986,957 entries (40 percent, 1.02x previous step)
    11 steps has 8,423,610 entries (5 percent, 0.13x previous step)
    12 steps has 12,788 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 9.33 moves
    """

    table_slug = "middle-oblique-outer-x"
    first_group = UFBD_MIDDLE_OBLIQUE_EDGES_777
    second_group = UFBD_OUTER_X_CENTERS_777


# ==================================================
# combined phases 7/8/9
# daisy-solve UD, LR, and FB centers
# ==================================================
# The post-staging move graph permits every outer turn and the half turns of
# both inner slices.  Wide quarter turns would unstage the opposite centers.
# fmt: off
DAISY_CENTERS_ILLEGAL_MOVES_777 = (
    "Uw", "Uw'", "3Uw", "3Uw'",
    "Lw", "Lw'", "3Lw", "3Lw'",
    "Fw", "Fw'", "3Fw", "3Fw'",
    "Rw", "Rw'", "3Rw", "3Rw'",
    "Bw", "Bw'", "3Bw", "3Bw'",
    "Dw", "Dw'", "3Dw", "3Dw'",
)

UD_LEFT_OBLIQUE_CENTERS_777 = (10, 20, 30, 40, 255, 265, 275, 285)
UD_MIDDLE_OBLIQUE_CENTERS_777 = (11, 23, 27, 39, 256, 268, 272, 284)
UD_RIGHT_OBLIQUE_CENTERS_777 = (12, 16, 34, 38, 257, 261, 279, 283)
UD_INNER_T_CENTERS_777 = (18, 24, 26, 32, 263, 269, 271, 277)
UD_INNER_X_CENTERS_777 = (17, 19, 31, 33, 262, 264, 276, 278)

LR_LEFT_OBLIQUE_CENTERS_777 = (59, 69, 79, 89, 157, 167, 177, 187)
LR_MIDDLE_OBLIQUE_CENTERS_777 = (60, 72, 76, 88, 158, 170, 174, 186)
LR_RIGHT_OBLIQUE_CENTERS_777 = (61, 65, 83, 87, 159, 163, 181, 185)
LR_INNER_T_CENTERS_777 = (67, 73, 75, 81, 165, 171, 173, 179)
LR_INNER_X_CENTERS_777 = (66, 68, 80, 82, 164, 166, 178, 180)

FB_LEFT_OBLIQUE_CENTERS_777 = (108, 118, 128, 138, 206, 216, 226, 236)
FB_MIDDLE_OBLIQUE_CENTERS_777 = (109, 121, 125, 137, 207, 219, 223, 235)
FB_RIGHT_OBLIQUE_CENTERS_777 = (110, 114, 132, 136, 208, 212, 230, 234)
FB_INNER_T_CENTERS_777 = (116, 122, 124, 130, 214, 220, 222, 228)
FB_INNER_X_CENTERS_777 = (115, 117, 129, 131, 213, 215, 227, 229)
# fmt: on

DAISY_CENTER_ORBITS_777 = {
    "UD": (
        ("left-oblique", UD_LEFT_OBLIQUE_CENTERS_777),
        ("middle-oblique", UD_MIDDLE_OBLIQUE_CENTERS_777),
        ("right-oblique", UD_RIGHT_OBLIQUE_CENTERS_777),
        ("inner-t", UD_INNER_T_CENTERS_777),
        ("inner-x", UD_INNER_X_CENTERS_777),
    ),
    "LR": (
        ("left-oblique", LR_LEFT_OBLIQUE_CENTERS_777),
        ("middle-oblique", LR_MIDDLE_OBLIQUE_CENTERS_777),
        ("right-oblique", LR_RIGHT_OBLIQUE_CENTERS_777),
        ("inner-t", LR_INNER_T_CENTERS_777),
        ("inner-x", LR_INNER_X_CENTERS_777),
    ),
    "FB": (
        ("left-oblique", FB_LEFT_OBLIQUE_CENTERS_777),
        ("middle-oblique", FB_MIDDLE_OBLIQUE_CENTERS_777),
        ("right-oblique", FB_RIGHT_OBLIQUE_CENTERS_777),
        ("inner-t", FB_INNER_T_CENTERS_777),
        ("inner-x", FB_INNER_X_CENTERS_777),
    ),
}

DAISY_AXIS_COLORS_777 = {"UD": ("U", "D"), "LR": ("L", "R"), "FB": ("F", "B")}
DAISY_OBLIQUE_ORBITS_777 = frozenset(("left-oblique", "middle-oblique", "right-oblique"))


def _daisy_starting_states_777(axis, selected_orbits, orientations=("native", "obliques-swapped")):
    """
    Return the requested coordinated goals projected onto `selected_orbits`.

    The native goal keeps every tracked center on its own face.  The alternate
    goal swaps all three oblique orbits between the two opposite faces while
    inner-t and inner-x stay native.  Applying the same orientation to every
    selected orbit is essential; independently flipping coordinates would add
    non-physical zero-cost goals.
    """
    primary, opposite = DAISY_AXIS_COLORS_777[axis]
    result = []

    for orientation in orientations:
        alternate = orientation == "obliques-swapped"
        state = ["."] * (6 * 7 * 7)

        for orbit_name, squares in selected_orbits:
            swap = alternate and orbit_name in DAISY_OBLIQUE_ORBITS_777
            first_color, second_color = (opposite, primary) if swap else (primary, opposite)

            for square in squares[:4]:
                state[square - 1] = first_color
            for square in squares[4:]:
                state[square - 1] = second_color

        result.append(("".join(state), "ULFRBD"))

    return tuple(result)


class _Build777DaisyCenters(BFS):
    """Shared dense ranked-cost builder for one opposite-face axis."""

    axis = None
    omitted_orbit = None
    table_slug = None
    table_prefix = "daisy"
    goal_orientations = ("native", "obliques-swapped")
    compact_center_symmetry = False

    def __init__(self):
        selected_orbits = tuple(orbit for orbit in DAISY_CENTER_ORBITS_777[self.axis] if orbit[0] != self.omitted_orbit)
        self.selected_orbits = selected_orbits

        BFS.__init__(
            self,
            f"7x7x7-{self.table_prefix}-{self.table_slug}-centers",
            DAISY_CENTERS_ILLEGAL_MOVES_777,
            "7x7x7",
            f"lookup-table-7x7x7-{self.table_prefix}-{self.table_slug}-centers.txt",
            False,
            _daisy_starting_states_777(self.axis, selected_orbits, self.goal_orientations),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, squares in selected_orbits),
            compact_center_symmetry_777=self.compact_center_symmetry,
        )


class Build777DaisyPerfectCenters(_Build777DaisyCenters):
    """
    One table for all three axes.

    The UD, LR and FB perfect tables were the same cost function written out
    three times under different square orderings, so only UD is built. The
    searcher rotates an LR or FB state onto the UD coordinate before probing.

    All five UD orbits are ranked and each puts four of its eight squares on U
    and four on D, so the coordinate is 70^5 = 1,680,700,000 states. The 16
    axis-preserving cube symmetries leave the cost unchanged, so publishing keeps
    one byte per orbit and the file on disk holds 105,356,972 of them; the
    histogram below counts raw ranks, which is what the searcher indexes.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges all three oblique
    orbits between U and D while inner-t and inner-x stay put, which is why depth
    0 holds two entries.

                   . . . . . . .
                   . . U U U . .
                   . U U U U U .
                   . U U . U U .
                   . U U U U U .
                   . . U U U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D D D . .
                   . D D D D D .
                   . D D . D D .
                   . D D D D D .
                   . . D D D . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-perfect-centers.cost-only.bin
    ======================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 762 entries (0 percent, 6.25x previous step)
    4 steps has 4,888 entries (0 percent, 6.41x previous step)
    5 steps has 32,000 entries (0 percent, 6.55x previous step)
    6 steps has 202,546 entries (0 percent, 6.33x previous step)
    7 steps has 1,247,834 entries (0 percent, 6.16x previous step)
    8 steps has 7,297,576 entries (0 percent, 5.85x previous step)
    9 steps has 38,903,378 entries (2 percent, 5.33x previous step)
    10 steps has 174,206,054 entries (10 percent, 4.48x previous step)
    11 steps has 540,471,106 entries (32 percent, 3.10x previous step)
    12 steps has 734,647,512 entries (43 percent, 1.36x previous step)
    13 steps has 181,651,516 entries (10 percent, 0.25x previous step)
    14 steps has 2,034,032 entries (0 percent, 0.01x previous step)
    15 steps has 656 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 11.49 moves
    """

    axis, table_slug = "UD", "perfect"
    compact_center_symmetry = True


# ==================================================
# solve centers to the native orientation
# used by cubes larger than 7x7
# ==================================================
class _Build777SolveCenters(_Build777DaisyCenters):
    """
    Same coordinates and move set as the daisy tables with only the native goal.

    A 7x7x7 may stop on either daisy orientation because its 5x5x5 phases still
    own those pieces. On 9x9x9 and larger every orbit these squares stand for is
    finished here, so the swapped orientation is not solved and must carry a real
    cost rather than zero.
    """

    table_prefix = "solve"
    goal_orientations = ("native",)


class Build777SolvePerfectCenters(_Build777SolveCenters):
    """
    Shared across the three axes the same way Build777DaisyPerfectCenters is.

    Same 70^5 = 1,680,700,000 coordinate and the same 105,356,972-orbit compacted
    file, but only the native goal counts as solved, so every depth shifts out by
    roughly half a move and the table runs one step deeper.

    _daisy_starting_states_777 is asked for the native orientation alone, so
    there is a single goal and depth 0 holds one entry:

                   . . . . . . .
                   . . U U U . .
                   . U U U U U .
                   . U U . U U .
                   . U U U U U .
                   . . U U U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D D D . .
                   . D D D D D .
                   . D D . D D .
                   . D D D D D .
                   . . D D D . .
                   . . . . . . .

    lookup-table-7x7x7-solve-perfect-centers.cost-only.bin
    ======================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 8 entries (0 percent, 8.00x previous step)
    2 steps has 64 entries (0 percent, 8.00x previous step)
    3 steps has 412 entries (0 percent, 6.44x previous step)
    4 steps has 2,643 entries (0 percent, 6.42x previous step)
    5 steps has 17,408 entries (0 percent, 6.59x previous step)
    6 steps has 110,881 entries (0 percent, 6.37x previous step)
    7 steps has 688,216 entries (0 percent, 6.21x previous step)
    8 steps has 4,078,714 entries (0 percent, 5.93x previous step)
    9 steps has 22,258,476 entries (1 percent, 5.46x previous step)
    10 steps has 104,656,519 entries (6 percent, 4.70x previous step)
    11 steps has 367,990,314 entries (21 percent, 3.52x previous step)
    12 steps has 715,270,228 entries (42 percent, 1.94x previous step)
    13 steps has 433,032,274 entries (25 percent, 0.61x previous step)
    14 steps has 32,512,022 entries (1 percent, 0.08x previous step)
    15 steps has 81,804 entries (0 percent, 0.00x previous step)
    16 steps has 16 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 11.90 moves
    """

    axis, table_slug = "UD", "perfect"
    compact_center_symmetry = True


# ==================================================
# inner-x spine
# all three inner-x orbits plus the left and right obliques of one axis
# ==================================================
DAISY_AXES_777 = ("UD", "LR", "FB")
DAISY_SPINE_OBLIQUE_NAMES_777 = ("left-oblique", "right-oblique")


def daisy_inner_x_spine_orbits_777(oblique_axis="UD"):
    """UD, LR, and FB inner-x, then the left and right obliques of one axis."""
    if oblique_axis not in DAISY_AXES_777:
        raise ValueError(oblique_axis)
    inner_x = tuple(
        orbit for axis in DAISY_AXES_777 for orbit in DAISY_CENTER_ORBITS_777[axis] if orbit[0] == "inner-x"
    )
    obliques = tuple(
        orbit for orbit in DAISY_CENTER_ORBITS_777[oblique_axis] if orbit[0] in DAISY_SPINE_OBLIQUE_NAMES_777
    )
    return inner_x + obliques


def _axis_owning_squares_777(squares):
    wanted = tuple(squares)
    for axis, orbits in DAISY_CENTER_ORBITS_777.items():
        for _, orbit_squares in orbits:
            if orbit_squares == wanted:
                return axis
    raise KeyError(wanted)


def _daisy_spine_starting_states_777(selected_orbits):
    """
    Native and obliques-swapped goals for a mixed-axis spine.

    Inner-x never swaps. Only the left and right obliques in the selection
    exchange their two faces, so those two orientations are the only goals.
    """
    result = []
    for swapped in (False, True):
        state = ["."] * (6 * 7 * 7)
        for orbit_name, squares in selected_orbits:
            primary, opposite = DAISY_AXIS_COLORS_777[_axis_owning_squares_777(squares)]
            exchange = swapped and orbit_name in DAISY_SPINE_OBLIQUE_NAMES_777
            first_color, second_color = (opposite, primary) if exchange else (primary, opposite)
            for square in squares[:4]:
                state[square - 1] = first_color
            for square in squares[4:]:
                state[square - 1] = second_color
        result.append(("".join(state), "ULFRBD"))
    return tuple(result)


class _Build777DaisyInnerXSpineCenters(BFS):
    """
    Dense ranked-cost 70^5 builder: every inner-x orbit plus one axis's left and right obliques.

    Five orbits of eight squares are tracked, the UD, LR, and FB inner x-centers
    plus the left and right obliques of `axis`. Middle obliques and inner-t stay
    out of this coordinate. Each orbit puts four squares on its primary face and
    four on the opposite face, so each ranks 8! / (4! * 4!) = 70 ways and the
    coordinate is 70^5 = 1,680,700,000 states. The published file is one byte
    per rank. The 16 axis-preserving symmetries used by the perfect table do not
    apply here, because these five orbits are not the five orbits of one axis.

    A cube rotation carrying UD onto LR or FB carries these five orbits onto
    that axis's spine, so this UD indexing is the only file. The other two
    probes rotate onto this square order: UD inner-x, LR inner-x, FB inner-x,
    UD left oblique, UD right oblique.

    _daisy_spine_starting_states_777 builds the goals instead of passing an
    ascii cube. Inner-x stays native in both, and the second goal exchanges the
    left and right obliques between the two faces of `axis`. This is the native
    goal for the UD table:

                   . . . . . . .
                   . . U . U . .
                   . U U . U U .
                   . . . . . . .
                   . U U . U U .
                   . . U . U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L . L . .  . . F . F . .  . . R . R . .  . . B . B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L . L . .  . . F . F . .  . . R . R . .  . . B . B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D . D . .
                   . D D . D D .
                   . . . . . . .
                   . D D . D D .
                   . . D . D . .
                   . . . . . . .
    """

    axis = None
    table_slug = None

    def __init__(self):
        selected_orbits = daisy_inner_x_spine_orbits_777(self.axis)
        self.selected_orbits = selected_orbits

        BFS.__init__(
            self,
            f"7x7x7-daisy-{self.table_slug}-centers",
            DAISY_CENTERS_ILLEGAL_MOVES_777,
            "7x7x7",
            f"lookup-table-7x7x7-daisy-{self.table_slug}-centers.txt",
            False,
            _daisy_spine_starting_states_777(selected_orbits),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, squares in selected_orbits),
        )


class Build777DaisyInnerXSpineCenters(_Build777DaisyInnerXSpineCenters):
    """
    All three inner-x orbits plus the UD left and right obliques.

    The shared goal diagram is on _Build777DaisyInnerXSpineCenters. LR and FB
    are the same cost function after a rotation onto these squares.

    lookup-table-7x7x7-daisy-inner-x-spine-centers.cost-only.bin
    ============================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 20 entries (0 percent, 10.00x previous step)
    2 steps has 292 entries (0 percent, 14.60x previous step)
    3 steps has 3,614 entries (0 percent, 12.38x previous step)
    4 steps has 35,016 entries (0 percent, 9.69x previous step)
    5 steps has 262,910 entries (0 percent, 7.51x previous step)
    6 steps has 1,678,254 entries (0 percent, 6.38x previous step)
    7 steps has 9,314,920 entries (0 percent, 5.55x previous step)
    8 steps has 42,467,206 entries (2 percent, 4.56x previous step)
    9 steps has 142,043,698 entries (8 percent, 3.34x previous step)
    10 steps has 310,836,418 entries (18 percent, 2.19x previous step)
    11 steps has 436,034,242 entries (25 percent, 1.40x previous step)
    12 steps has 404,658,064 entries (24 percent, 0.93x previous step)
    13 steps has 242,558,432 entries (14 percent, 0.60x previous step)
    14 steps has 83,622,720 entries (4 percent, 0.34x previous step)
    15 steps has 7,153,472 entries (0 percent, 0.09x previous step)
    16 steps has 30,720 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 11.24 moves
    """

    axis = "UD"
    table_slug = "inner-x-spine"


# ==================================================
# mixed-axis 70^5 coordinates
# one file per coordinate; x y and z' y' rotate it onto the other two probes
# ==================================================
# Probe 0 is the file's own square order. Probe 1 is the x y rotation and
# probe 2 is z' y'. Those are the rotations that carry a solved coloring onto
# the file's solved byte. Inner-x and inner-t have a single native goal. Any
# oblique orbit swaps between the two faces in the alternate daisy orientation,
# so those coordinates have two goals.
DAISY_MIXED_PROBES_777 = {
    "inner-x-plus-two-inner-t": (
        (
            ("UD", "inner-x"),
            ("LR", "inner-x"),
            ("FB", "inner-x"),
            ("UD", "inner-t"),
            ("LR", "inner-t"),
        ),
        (
            ("FB", "inner-x"),
            ("UD", "inner-x"),
            ("LR", "inner-x"),
            ("FB", "inner-t"),
            ("UD", "inner-t"),
        ),
        (
            ("LR", "inner-x"),
            ("FB", "inner-x"),
            ("UD", "inner-x"),
            ("LR", "inner-t"),
            ("FB", "inner-t"),
        ),
    ),
    "inner-t-plus-two-inner-x": (
        (
            ("UD", "inner-t"),
            ("LR", "inner-t"),
            ("FB", "inner-t"),
            ("UD", "inner-x"),
            ("LR", "inner-x"),
        ),
        (
            ("FB", "inner-t"),
            ("UD", "inner-t"),
            ("LR", "inner-t"),
            ("FB", "inner-x"),
            ("UD", "inner-x"),
        ),
        (
            ("LR", "inner-t"),
            ("FB", "inner-t"),
            ("UD", "inner-t"),
            ("LR", "inner-x"),
            ("FB", "inner-x"),
        ),
    ),
    "middle-plus-two-inner-t": (
        (
            ("UD", "middle-oblique"),
            ("LR", "middle-oblique"),
            ("FB", "middle-oblique"),
            ("UD", "inner-t"),
            ("LR", "inner-t"),
        ),
        (
            ("FB", "middle-oblique"),
            ("UD", "middle-oblique"),
            ("LR", "middle-oblique"),
            ("FB", "inner-t"),
            ("UD", "inner-t"),
        ),
        (
            ("LR", "middle-oblique"),
            ("FB", "middle-oblique"),
            ("UD", "middle-oblique"),
            ("LR", "inner-t"),
            ("FB", "inner-t"),
        ),
    ),
    "oblique-weave": (
        (
            ("UD", "left-oblique"),
            ("UD", "right-oblique"),
            ("LR", "left-oblique"),
            ("LR", "right-oblique"),
            ("FB", "middle-oblique"),
        ),
        (
            ("FB", "left-oblique"),
            ("FB", "right-oblique"),
            ("UD", "left-oblique"),
            ("UD", "right-oblique"),
            ("LR", "middle-oblique"),
        ),
        (
            ("LR", "left-oblique"),
            ("LR", "right-oblique"),
            ("FB", "left-oblique"),
            ("FB", "right-oblique"),
            ("UD", "middle-oblique"),
        ),
    ),
}


def _orbit_squares_777(axis, name):
    matches = [squares for orbit_name, squares in DAISY_CENTER_ORBITS_777[axis] if orbit_name == name]
    if len(matches) != 1:
        raise KeyError((axis, name))
    return matches[0]


def daisy_mixed_probe_orbits_777(table_slug):
    """Three orbit lists: the built square order, then the x y and z' y' probes."""
    if table_slug not in DAISY_MIXED_PROBES_777:
        raise ValueError(table_slug)
    return tuple(
        tuple((name, _orbit_squares_777(axis, name)) for axis, name in probe)
        for probe in DAISY_MIXED_PROBES_777[table_slug]
    )


def daisy_mixed_orbits_777(table_slug):
    """The five orbits written into the cost file, in rank order."""
    return daisy_mixed_probe_orbits_777(table_slug)[0]


def _daisy_mixed_starting_states_777(selected_orbits):
    """
    Native goal, plus the obliques-swapped goal when the coordinate tracks one.

    Inner-x and inner-t stay on their own faces. Left, middle, and right
    obliques exchange faces together, which is the daisy's second orientation.
    """
    swaps = (False, True) if any(name in DAISY_OBLIQUE_ORBITS_777 for name, _ in selected_orbits) else (False,)
    result = []
    for swapped in swaps:
        state = ["."] * (6 * 7 * 7)
        for orbit_name, squares in selected_orbits:
            primary, opposite = DAISY_AXIS_COLORS_777[_axis_owning_squares_777(squares)]
            exchange = swapped and orbit_name in DAISY_OBLIQUE_ORBITS_777
            first_color, second_color = (opposite, primary) if exchange else (primary, opposite)
            for square in squares[:4]:
                state[square - 1] = first_color
            for square in squares[4:]:
                state[square - 1] = second_color
        result.append(("".join(state), "ULFRBD"))
    return tuple(result)


class _Build777DaisyMixedCenters(BFS):
    """
    Dense ranked-cost 70^5 builder for five orbits drawn from more than one axis.

    The published file is one byte per rank, 1,680,700,000 bytes, with no
    symmetry compaction. The 16 axis-preserving symmetries fix one axis, and
    these coordinates mix axes. `table_slug` selects the square order from
    DAISY_MIXED_PROBES_777. An x y rotation and a z' y' rotation carry that
    order onto the other two probes, so each slug is one file.
    """

    table_slug = None

    def __init__(self):
        selected_orbits = daisy_mixed_orbits_777(self.table_slug)
        self.selected_orbits = selected_orbits

        BFS.__init__(
            self,
            f"7x7x7-daisy-{self.table_slug}-centers",
            DAISY_CENTERS_ILLEGAL_MOVES_777,
            "7x7x7",
            f"lookup-table-7x7x7-daisy-{self.table_slug}-centers.txt",
            False,
            _daisy_mixed_starting_states_777(selected_orbits),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, squares in selected_orbits),
        )


class Build777DaisyInnerXPlusTwoInnerTCenters(_Build777DaisyMixedCenters):
    """
    All three inner-x orbits plus the UD and LR inner t-centers.

    FB inner-t is omitted here; x y omits LR inner-t and z' y' omits UD inner-t.
    Inner-x and inner-t do not swap, so there is one goal. F and B show inner-x only.

    lookup-table-7x7x7-daisy-inner-x-plus-two-inner-t-centers.cost-only.bin
    =======================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 6 entries (0 percent, 6.00x previous step)
    2 steps has 99 entries (0 percent, 16.50x previous step)
    3 steps has 1,098 entries (0 percent, 11.09x previous step)
    4 steps has 10,874 entries (0 percent, 9.90x previous step)
    5 steps has 100,654 entries (0 percent, 9.26x previous step)
    6 steps has 832,025 entries (0 percent, 8.27x previous step)
    7 steps has 5,930,898 entries (0 percent, 7.13x previous step)
    8 steps has 34,609,474 entries (2 percent, 5.84x previous step)
    9 steps has 149,171,994 entries (8 percent, 4.31x previous step)
    10 steps has 403,406,387 entries (24 percent, 2.70x previous step)
    11 steps has 579,775,732 entries (34 percent, 1.44x previous step)
    12 steps has 399,712,478 entries (23 percent, 0.69x previous step)
    13 steps has 102,649,488 entries (6 percent, 0.26x previous step)
    14 steps has 4,490,104 entries (0 percent, 0.04x previous step)
    15 steps has 8,688 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 10.87 moves

                   . . . . . . .
                   . . . . . . .
                   . . U U U . .
                   . . U . U . .
                   . . U U U . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L L L . .  . . F . F . .  . . R R R . .  . . B . B . .
    . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
    . . L L L . .  . . F . F . .  . . R R R . .  . . B . B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . D D D . .
                   . . D . D . .
                   . . D D D . .
                   . . . . . . .
                   . . . . . . .
    """

    table_slug = "inner-x-plus-two-inner-t"


class Build777DaisyInnerTPlusTwoInnerXCenters(_Build777DaisyMixedCenters):
    """
    All three inner-t orbits plus the UD and LR inner x-centers.

    FB inner-x is omitted here; x y omits LR inner-x and z' y' omits UD inner-x.
    One goal. F and B show inner-t only.

    lookup-table-7x7x7-daisy-inner-t-plus-two-inner-x-centers.cost-only.bin
    =======================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 6 entries (0 percent, 6.00x previous step)
    2 steps has 99 entries (0 percent, 16.50x previous step)
    3 steps has 1,102 entries (0 percent, 11.13x previous step)
    4 steps has 10,991 entries (0 percent, 9.97x previous step)
    5 steps has 103,416 entries (0 percent, 9.41x previous step)
    6 steps has 888,663 entries (0 percent, 8.59x previous step)
    7 steps has 6,731,540 entries (0 percent, 7.57x previous step)
    8 steps has 42,323,665 entries (2 percent, 6.29x previous step)
    9 steps has 196,540,960 entries (11 percent, 4.64x previous step)
    10 steps has 546,068,833 entries (32 percent, 2.78x previous step)
    11 steps has 655,219,330 entries (38 percent, 1.20x previous step)
    12 steps has 220,635,638 entries (13 percent, 0.34x previous step)
    13 steps has 12,146,412 entries (0 percent, 0.06x previous step)
    14 steps has 29,344 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 10.49 moves

                   . . . . . . .
                   . . . . . . .
                   . . U U U . .
                   . . U . U . .
                   . . U U U . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L L L . .  . . . F . . .  . . R R R . .  . . . B . . .
    . . L . L . .  . . F . F . .  . . R . R . .  . . B . B . .
    . . L L L . .  . . . F . . .  . . R R R . .  . . . B . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . D D D . .
                   . . D . D . .
                   . . D D D . .
                   . . . . . . .
                   . . . . . . .
    """

    table_slug = "inner-t-plus-two-inner-x"


class Build777DaisyMiddlePlusTwoInnerTCenters(_Build777DaisyMixedCenters):
    """
    All three middle-oblique orbits plus the UD and LR inner t-centers.

    FB inner-t is omitted here; x y omits LR inner-t and z' y' omits UD inner-t.
    Middle obliques swap in the second daisy orientation and inner-t does not,
    so depth 0 holds two entries.

    lookup-table-7x7x7-daisy-middle-plus-two-inner-t-centers.cost-only.bin
    ======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 24 entries (0 percent, 12.00x previous step)
    2 steps has 516 entries (0 percent, 21.50x previous step)
    3 steps has 8,352 entries (0 percent, 16.19x previous step)
    4 steps has 117,048 entries (0 percent, 14.01x previous step)
    5 steps has 1,375,944 entries (0 percent, 11.76x previous step)
    6 steps has 13,291,732 entries (0 percent, 9.66x previous step)
    7 steps has 95,275,648 entries (5 percent, 7.17x previous step)
    8 steps has 412,978,074 entries (24 percent, 4.33x previous step)
    9 steps has 767,322,380 entries (45 percent, 1.86x previous step)
    10 steps has 369,339,248 entries (21 percent, 0.48x previous step)
    11 steps has 20,914,696 entries (1 percent, 0.06x previous step)
    12 steps has 76,336 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 8.86 moves

                   . . . . . . .
                   . . . U . . .
                   . . . U . . .
                   . U U . U U .
                   . . . U . . .
                   . . . U . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . L . . .  . . . F . . .  . . . R . . .  . . . B . . .
    . . . L . . .  . . . . . . .  . . . R . . .  . . . . . . .
    . L L . L L .  . F . . . F .  . R R . R R .  . B . . . B .
    . . . L . . .  . . . . . . .  . . . R . . .  . . . . . . .
    . . . L . . .  . . . F . . .  . . . R . . .  . . . B . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . D . . .
                   . . . D . . .
                   . D D . D D .
                   . . . D . . .
                   . . . D . . .
                   . . . . . . .
    """

    table_slug = "middle-plus-two-inner-t"


class Build777DaisyObliqueWeaveCenters(_Build777DaisyMixedCenters):
    """
    Left and right obliques of UD and LR, plus the FB middle oblique.

    x y puts the middle on LR and z' y' puts it on UD. Every tracked orbit is
    an oblique, so both daisy orientations are goals.

    lookup-table-7x7x7-daisy-oblique-weave-centers.cost-only.bin
    ============================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 24 entries (0 percent, 12.00x previous step)
    2 steps has 482 entries (0 percent, 20.08x previous step)
    3 steps has 7,284 entries (0 percent, 15.11x previous step)
    4 steps has 93,242 entries (0 percent, 12.80x previous step)
    5 steps has 952,880 entries (0 percent, 10.22x previous step)
    6 steps has 7,612,186 entries (0 percent, 7.99x previous step)
    7 steps has 45,726,268 entries (2 percent, 6.01x previous step)
    8 steps has 191,800,488 entries (11 percent, 4.19x previous step)
    9 steps has 491,712,480 entries (29 percent, 2.56x previous step)
    10 steps has 603,694,056 entries (35 percent, 1.23x previous step)
    11 steps has 291,312,896 entries (17 percent, 0.48x previous step)
    12 steps has 45,944,976 entries (2 percent, 0.16x previous step)
    13 steps has 1,842,736 entries (0 percent, 0.04x previous step)

    Total: 1,680,700,000 entries
    Average: 9.61 moves

                   . . . . . . .
                   . . U . U . .
                   . U . . . U .
                   . . . . . . .
                   . U . . . U .
                   . . U . U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L . L . .  . . . F . . .  . . R . R . .  . . . B . . .
    . L . . . L .  . . . . . . .  . R . . . R .  . . . . . . .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . L . . . L .  . . . . . . .  . R . . . R .  . . . . . . .
    . . L . L . .  . . . F . . .  . . R . R . .  . . . B . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D . D . .
                   . D . . . D .
                   . . . . . . .
                   . D . . . D .
                   . . D . D . .
                   . . . . . . .
    """

    table_slug = "oblique-weave"


class Build777DaisyLRInnerCenters(BFS):
    """
    Rank the LR inner-t orbit and the LR inner-x orbit.

    Each orbit puts four of its eight squares on L and four on R, so each
    contributes C(8, 4) = 70 and the pair is 70^2 = 4,900 states. Inner centers
    do not swap, so there is one goal. Both orbits are closed under the daisy
    moves, which makes this distance exact for those two orbits.

    lookup-table-7x7x7-daisy-lr-inner-centers.cost-only.bin
    =======================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 4 entries (0 percent, 4.00x previous step)
    2 steps has 22 entries (0 percent, 5.50x previous step)
    3 steps has 82 entries (1 percent, 3.73x previous step)
    4 steps has 292 entries (5 percent, 3.56x previous step)
    5 steps has 986 entries (20 percent, 3.38x previous step)
    6 steps has 2,001 entries (40 percent, 2.03x previous step)
    7 steps has 1,312 entries (26 percent, 0.66x previous step)
    8 steps has 200 entries (4 percent, 0.15x previous step)

    Total: 4,900 entries
    Average: 5.96 moves

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
    . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
    . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
    """

    def __init__(self):
        orbits = (
            ("inner-t", LR_INNER_T_CENTERS_777),
            ("inner-x", LR_INNER_X_CENTERS_777),
        )
        BFS.__init__(
            self,
            "7x7x7-daisy-lr-inner-centers",
            DAISY_CENTERS_ILLEGAL_MOVES_777,
            "7x7x7",
            "lookup-table-7x7x7-daisy-lr-inner-centers.txt",
            False,
            _daisy_starting_states_777("LR", orbits, ("native",)),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, squares in orbits),
        )

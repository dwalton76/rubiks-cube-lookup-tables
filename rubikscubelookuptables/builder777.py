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


class Build777DaisyUDWithoutLeftObliqueCenters(_Build777DaisyCenters):
    """
    UD daisy centers with the left obliques dropped from the coordinate.

    Four of the five UD orbits are ranked and each puts four of its eight squares
    on U and four on D, so the coordinate is 70^4 = 24,010,000 states.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between U and D while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

                   . . . . . . .
                   . . . U U . .
                   . U U U U . .
                   . U U . U U .
                   . . U U U U .
                   . . U U . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . D D . .
                   . D D D D . .
                   . D D . D D .
                   . . D D D D .
                   . . D D . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-UD-without-left-oblique-centers.cost-only.bin
    ======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 746 entries (0 percent, 6.11x previous step)
    4 steps has 4,512 entries (0 percent, 6.05x previous step)
    5 steps has 26,744 entries (0 percent, 5.93x previous step)
    6 steps has 145,826 entries (0 percent, 5.45x previous step)
    7 steps has 706,554 entries (2 percent, 4.85x previous step)
    8 steps has 2,823,472 entries (11 percent, 4.00x previous step)
    9 steps has 7,760,250 entries (32 percent, 2.75x previous step)
    10 steps has 9,776,782 entries (40 percent, 1.26x previous step)
    11 steps has 2,712,814 entries (11 percent, 0.28x previous step)
    12 steps has 52,156 entries (0 percent, 0.02x previous step)
    13 steps has 4 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.44 moves
    """

    axis, omitted_orbit, table_slug = "UD", "left-oblique", "UD-without-left-oblique"


class Build777DaisyUDWithoutMiddleObliqueCenters(_Build777DaisyCenters):
    """
    UD daisy centers with the middle obliques dropped from the coordinate.

    Four of the five UD orbits are ranked and each puts four of its eight squares
    on U and four on D, so the coordinate is 70^4 = 24,010,000 states.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between U and D while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

                   . . . . . . .
                   . . U . U . .
                   . U U U U U .
                   . . U . U . .
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
                   . . D . D . .
                   . D D D D D .
                   . . D . D . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-UD-without-middle-oblique-centers.cost-only.bin
    ========================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 106 entries (0 percent, 6.62x previous step)
    3 steps has 618 entries (0 percent, 5.83x previous step)
    4 steps has 3,556 entries (0 percent, 5.75x previous step)
    5 steps has 20,496 entries (0 percent, 5.76x previous step)
    6 steps has 112,698 entries (0 percent, 5.50x previous step)
    7 steps has 543,928 entries (2 percent, 4.83x previous step)
    8 steps has 2,194,928 entries (9 percent, 4.04x previous step)
    9 steps has 6,385,074 entries (26 percent, 2.91x previous step)
    10 steps has 9,901,620 entries (41 percent, 1.55x previous step)
    11 steps has 4,534,760 entries (18 percent, 0.46x previous step)
    12 steps has 310,934 entries (1 percent, 0.07x previous step)
    13 steps has 1,264 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.67 moves
    """

    axis, omitted_orbit, table_slug = "UD", "middle-oblique", "UD-without-middle-oblique"


class Build777DaisyUDWithoutRightObliqueCenters(_Build777DaisyCenters):
    """
    UD daisy centers with the right obliques dropped from the coordinate.

    Four of the five UD orbits are ranked and each puts four of its eight squares
    on U and four on D, so the coordinate is 70^4 = 24,010,000 states. Dropping
    the right obliques mirrors dropping the left ones, so the two tables share a
    histogram.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between U and D while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

                   . . . . . . .
                   . . U U . . .
                   . . U U U U .
                   . U U . U U .
                   . U U U U . .
                   . . . U U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D D . . .
                   . . D D D D .
                   . D D . D D .
                   . D D D D . .
                   . . . D D . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-UD-without-right-oblique-centers.cost-only.bin
    =======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 746 entries (0 percent, 6.11x previous step)
    4 steps has 4,512 entries (0 percent, 6.05x previous step)
    5 steps has 26,744 entries (0 percent, 5.93x previous step)
    6 steps has 145,826 entries (0 percent, 5.45x previous step)
    7 steps has 706,554 entries (2 percent, 4.85x previous step)
    8 steps has 2,823,472 entries (11 percent, 4.00x previous step)
    9 steps has 7,760,250 entries (32 percent, 2.75x previous step)
    10 steps has 9,776,782 entries (40 percent, 1.26x previous step)
    11 steps has 2,712,814 entries (11 percent, 0.28x previous step)
    12 steps has 52,156 entries (0 percent, 0.02x previous step)
    13 steps has 4 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.44 moves
    """

    axis, omitted_orbit, table_slug = "UD", "right-oblique", "UD-without-right-oblique"


class Build777DaisyUDWithoutInnerTCenters(_Build777DaisyCenters):
    """
    UD daisy centers with the inner t-centers dropped from the coordinate.

    Four of the five UD orbits are ranked and each puts four of its eight squares
    on U and four on D, so the coordinate is 70^4 = 24,010,000 states.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges all three oblique
    orbits between U and D while the inner x-centers stay put, which is why depth
    0 holds two entries.

                   . . . . . . .
                   . . U U U . .
                   . U U . U U .
                   . U . . . U .
                   . U U . U U .
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
                   . D D . D D .
                   . D . . . D .
                   . D D . D D .
                   . . D D D . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-UD-without-inner-t-centers.cost-only.bin
    =================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 106 entries (0 percent, 6.62x previous step)
    3 steps has 594 entries (0 percent, 5.60x previous step)
    4 steps has 3,618 entries (0 percent, 6.09x previous step)
    5 steps has 22,250 entries (0 percent, 6.15x previous step)
    6 steps has 125,604 entries (0 percent, 5.65x previous step)
    7 steps has 635,070 entries (2 percent, 5.06x previous step)
    8 steps has 2,641,982 entries (11 percent, 4.16x previous step)
    9 steps has 7,545,582 entries (31 percent, 2.86x previous step)
    10 steps has 10,110,652 entries (42 percent, 1.34x previous step)
    11 steps has 2,862,740 entries (11 percent, 0.28x previous step)
    12 steps has 61,704 entries (0 percent, 0.02x previous step)
    13 steps has 80 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.48 moves
    """

    axis, omitted_orbit, table_slug = "UD", "inner-t", "UD-without-inner-t"


class Build777DaisyUDWithoutInnerXCenters(_Build777DaisyCenters):
    """
    UD daisy centers with the inner x-centers dropped from the coordinate.

    Four of the five UD orbits are ranked and each puts four of its eight squares
    on U and four on D, so the coordinate is 70^4 = 24,010,000 states. This is the
    shallowest of the five leave-one-out tables.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges all three oblique
    orbits between U and D while the inner t-centers stay put, which is why depth
    0 holds two entries.

                   . . . . . . .
                   . . U U U . .
                   . U . U . U .
                   . U U . U U .
                   . U . U . U .
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
                   . D . D . D .
                   . D D . D D .
                   . D . D . D .
                   . . D D D . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-UD-without-inner-x-centers.cost-only.bin
    =================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 762 entries (0 percent, 6.25x previous step)
    4 steps has 4,688 entries (0 percent, 6.15x previous step)
    5 steps has 29,272 entries (0 percent, 6.24x previous step)
    6 steps has 169,770 entries (0 percent, 5.80x previous step)
    7 steps has 891,464 entries (3 percent, 5.25x previous step)
    8 steps has 3,754,714 entries (15 percent, 4.21x previous step)
    9 steps has 9,594,114 entries (39 percent, 2.56x previous step)
    10 steps has 8,472,704 entries (35 percent, 0.88x previous step)
    11 steps has 1,084,012 entries (4 percent, 0.13x previous step)
    12 steps has 8,360 entries (0 percent, 0.01x previous step)

    Total: 24,010,000 entries
    Average: 9.19 moves
    """

    axis, omitted_orbit, table_slug = "UD", "inner-x", "UD-without-inner-x"


class Build777DaisyLRWithoutLeftObliqueCenters(_Build777DaisyCenters):
    """
    LR daisy centers with the left obliques dropped from the coordinate.

    Four of the five LR orbits are ranked and each puts four of its eight squares
    on L and four on R, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the LR axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between L and R while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . L L . .  . . . . . . .  . . . R R . .  . . . . . . .
    . L L L L . .  . . . . . . .  . R R R R . .  . . . . . . .
    . L L . L L .  . . . . . . .  . R R . R R .  . . . . . . .
    . . L L L L .  . . . . . . .  . . R R R R .  . . . . . . .
    . . L L . . .  . . . . . . .  . . R R . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-LR-without-left-oblique-centers.cost-only.bin
    ======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 746 entries (0 percent, 6.11x previous step)
    4 steps has 4,512 entries (0 percent, 6.05x previous step)
    5 steps has 26,744 entries (0 percent, 5.93x previous step)
    6 steps has 145,826 entries (0 percent, 5.45x previous step)
    7 steps has 706,554 entries (2 percent, 4.85x previous step)
    8 steps has 2,823,472 entries (11 percent, 4.00x previous step)
    9 steps has 7,760,250 entries (32 percent, 2.75x previous step)
    10 steps has 9,776,782 entries (40 percent, 1.26x previous step)
    11 steps has 2,712,814 entries (11 percent, 0.28x previous step)
    12 steps has 52,156 entries (0 percent, 0.02x previous step)
    13 steps has 4 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.44 moves
    """

    axis, omitted_orbit, table_slug = "LR", "left-oblique", "LR-without-left-oblique"


class Build777DaisyLRWithoutMiddleObliqueCenters(_Build777DaisyCenters):
    """
    LR daisy centers with the middle obliques dropped from the coordinate.

    Four of the five LR orbits are ranked and each puts four of its eight squares
    on L and four on R, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the LR axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between L and R while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

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
    . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
    . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
    . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-LR-without-middle-oblique-centers.cost-only.bin
    ========================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 106 entries (0 percent, 6.62x previous step)
    3 steps has 618 entries (0 percent, 5.83x previous step)
    4 steps has 3,556 entries (0 percent, 5.75x previous step)
    5 steps has 20,496 entries (0 percent, 5.76x previous step)
    6 steps has 112,698 entries (0 percent, 5.50x previous step)
    7 steps has 543,928 entries (2 percent, 4.83x previous step)
    8 steps has 2,194,928 entries (9 percent, 4.04x previous step)
    9 steps has 6,385,074 entries (26 percent, 2.91x previous step)
    10 steps has 9,901,620 entries (41 percent, 1.55x previous step)
    11 steps has 4,534,760 entries (18 percent, 0.46x previous step)
    12 steps has 310,934 entries (1 percent, 0.07x previous step)
    13 steps has 1,264 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.67 moves
    """

    axis, omitted_orbit, table_slug = "LR", "middle-oblique", "LR-without-middle-oblique"


class Build777DaisyLRWithoutRightObliqueCenters(_Build777DaisyCenters):
    """
    LR daisy centers with the right obliques dropped from the coordinate.

    Four of the five LR orbits are ranked and each puts four of its eight squares
    on L and four on R, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the LR axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between L and R while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L L . . .  . . . . . . .  . . R R . . .  . . . . . . .
    . . L L L L .  . . . . . . .  . . R R R R .  . . . . . . .
    . L L . L L .  . . . . . . .  . R R . R R .  . . . . . . .
    . L L L L . .  . . . . . . .  . R R R R . .  . . . . . . .
    . . . L L . .  . . . . . . .  . . . R R . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-LR-without-right-oblique-centers.cost-only.bin
    =======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 746 entries (0 percent, 6.11x previous step)
    4 steps has 4,512 entries (0 percent, 6.05x previous step)
    5 steps has 26,744 entries (0 percent, 5.93x previous step)
    6 steps has 145,826 entries (0 percent, 5.45x previous step)
    7 steps has 706,554 entries (2 percent, 4.85x previous step)
    8 steps has 2,823,472 entries (11 percent, 4.00x previous step)
    9 steps has 7,760,250 entries (32 percent, 2.75x previous step)
    10 steps has 9,776,782 entries (40 percent, 1.26x previous step)
    11 steps has 2,712,814 entries (11 percent, 0.28x previous step)
    12 steps has 52,156 entries (0 percent, 0.02x previous step)
    13 steps has 4 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.44 moves
    """

    axis, omitted_orbit, table_slug = "LR", "right-oblique", "LR-without-right-oblique"


class Build777DaisyLRWithoutInnerTCenters(_Build777DaisyCenters):
    """
    LR daisy centers with the inner t-centers dropped from the coordinate.

    Four of the five LR orbits are ranked and each puts four of its eight squares
    on L and four on R, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the LR axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges all three oblique
    orbits between L and R while the inner x-centers stay put, which is why depth
    0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
    . L L . L L .  . . . . . . .  . R R . R R .  . . . . . . .
    . L . . . L .  . . . . . . .  . R . . . R .  . . . . . . .
    . L L . L L .  . . . . . . .  . R R . R R .  . . . . . . .
    . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-LR-without-inner-t-centers.cost-only.bin
    =================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 106 entries (0 percent, 6.62x previous step)
    3 steps has 594 entries (0 percent, 5.60x previous step)
    4 steps has 3,618 entries (0 percent, 6.09x previous step)
    5 steps has 22,250 entries (0 percent, 6.15x previous step)
    6 steps has 125,604 entries (0 percent, 5.65x previous step)
    7 steps has 635,070 entries (2 percent, 5.06x previous step)
    8 steps has 2,641,982 entries (11 percent, 4.16x previous step)
    9 steps has 7,545,582 entries (31 percent, 2.86x previous step)
    10 steps has 10,110,652 entries (42 percent, 1.34x previous step)
    11 steps has 2,862,740 entries (11 percent, 0.28x previous step)
    12 steps has 61,704 entries (0 percent, 0.02x previous step)
    13 steps has 80 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.48 moves
    """

    axis, omitted_orbit, table_slug = "LR", "inner-t", "LR-without-inner-t"


class Build777DaisyLRWithoutInnerXCenters(_Build777DaisyCenters):
    """
    LR daisy centers with the inner x-centers dropped from the coordinate.

    Four of the five LR orbits are ranked and each puts four of its eight squares
    on L and four on R, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the LR axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges all three oblique
    orbits between L and R while the inner t-centers stay put, which is why depth
    0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
    . L . L . L .  . . . . . . .  . R . R . R .  . . . . . . .
    . L L . L L .  . . . . . . .  . R R . R R .  . . . . . . .
    . L . L . L .  . . . . . . .  . R . R . R .  . . . . . . .
    . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-LR-without-inner-x-centers.cost-only.bin
    =================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 762 entries (0 percent, 6.25x previous step)
    4 steps has 4,688 entries (0 percent, 6.15x previous step)
    5 steps has 29,272 entries (0 percent, 6.24x previous step)
    6 steps has 169,770 entries (0 percent, 5.80x previous step)
    7 steps has 891,464 entries (3 percent, 5.25x previous step)
    8 steps has 3,754,714 entries (15 percent, 4.21x previous step)
    9 steps has 9,594,114 entries (39 percent, 2.56x previous step)
    10 steps has 8,472,704 entries (35 percent, 0.88x previous step)
    11 steps has 1,084,012 entries (4 percent, 0.13x previous step)
    12 steps has 8,360 entries (0 percent, 0.01x previous step)

    Total: 24,010,000 entries
    Average: 9.19 moves
    """

    axis, omitted_orbit, table_slug = "LR", "inner-x", "LR-without-inner-x"


class Build777DaisyFBWithoutLeftObliqueCenters(_Build777DaisyCenters):
    """
    FB daisy centers with the left obliques dropped from the coordinate.

    Four of the five FB orbits are ranked and each puts four of its eight squares
    on F and four on B, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the FB axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between F and B while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . F F . .  . . . . . . .  . . . B B . .
    . . . . . . .  . F F F F . .  . . . . . . .  . B B B B . .
    . . . . . . .  . F F . F F .  . . . . . . .  . B B . B B .
    . . . . . . .  . . F F F F .  . . . . . . .  . . B B B B .
    . . . . . . .  . . F F . . .  . . . . . . .  . . B B . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-FB-without-left-oblique-centers.cost-only.bin
    ======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 746 entries (0 percent, 6.11x previous step)
    4 steps has 4,512 entries (0 percent, 6.05x previous step)
    5 steps has 26,744 entries (0 percent, 5.93x previous step)
    6 steps has 145,826 entries (0 percent, 5.45x previous step)
    7 steps has 706,554 entries (2 percent, 4.85x previous step)
    8 steps has 2,823,472 entries (11 percent, 4.00x previous step)
    9 steps has 7,760,250 entries (32 percent, 2.75x previous step)
    10 steps has 9,776,782 entries (40 percent, 1.26x previous step)
    11 steps has 2,712,814 entries (11 percent, 0.28x previous step)
    12 steps has 52,156 entries (0 percent, 0.02x previous step)
    13 steps has 4 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.44 moves
    """

    axis, omitted_orbit, table_slug = "FB", "left-oblique", "FB-without-left-oblique"


class Build777DaisyFBWithoutMiddleObliqueCenters(_Build777DaisyCenters):
    """
    FB daisy centers with the middle obliques dropped from the coordinate.

    Four of the five FB orbits are ranked and each puts four of its eight squares
    on F and four on B, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the FB axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between F and B while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

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
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-FB-without-middle-oblique-centers.cost-only.bin
    ========================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 106 entries (0 percent, 6.62x previous step)
    3 steps has 618 entries (0 percent, 5.83x previous step)
    4 steps has 3,556 entries (0 percent, 5.75x previous step)
    5 steps has 20,496 entries (0 percent, 5.76x previous step)
    6 steps has 112,698 entries (0 percent, 5.50x previous step)
    7 steps has 543,928 entries (2 percent, 4.83x previous step)
    8 steps has 2,194,928 entries (9 percent, 4.04x previous step)
    9 steps has 6,385,074 entries (26 percent, 2.91x previous step)
    10 steps has 9,901,620 entries (41 percent, 1.55x previous step)
    11 steps has 4,534,760 entries (18 percent, 0.46x previous step)
    12 steps has 310,934 entries (1 percent, 0.07x previous step)
    13 steps has 1,264 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.67 moves
    """

    axis, omitted_orbit, table_slug = "FB", "middle-oblique", "FB-without-middle-oblique"


class Build777DaisyFBWithoutRightObliqueCenters(_Build777DaisyCenters):
    """
    FB daisy centers with the right obliques dropped from the coordinate.

    Four of the five FB orbits are ranked and each puts four of its eight squares
    on F and four on B, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the FB axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges the two remaining
    oblique orbits between F and B while inner-t and inner-x stay put, which is
    why depth 0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F . . .  . . . . . . .  . . B B . . .
    . . . . . . .  . . F F F F .  . . . . . . .  . . B B B B .
    . . . . . . .  . F F . F F .  . . . . . . .  . B B . B B .
    . . . . . . .  . F F F F . .  . . . . . . .  . B B B B . .
    . . . . . . .  . . . F F . .  . . . . . . .  . . . B B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-FB-without-right-oblique-centers.cost-only.bin
    =======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 746 entries (0 percent, 6.11x previous step)
    4 steps has 4,512 entries (0 percent, 6.05x previous step)
    5 steps has 26,744 entries (0 percent, 5.93x previous step)
    6 steps has 145,826 entries (0 percent, 5.45x previous step)
    7 steps has 706,554 entries (2 percent, 4.85x previous step)
    8 steps has 2,823,472 entries (11 percent, 4.00x previous step)
    9 steps has 7,760,250 entries (32 percent, 2.75x previous step)
    10 steps has 9,776,782 entries (40 percent, 1.26x previous step)
    11 steps has 2,712,814 entries (11 percent, 0.28x previous step)
    12 steps has 52,156 entries (0 percent, 0.02x previous step)
    13 steps has 4 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.44 moves
    """

    axis, omitted_orbit, table_slug = "FB", "right-oblique", "FB-without-right-oblique"


class Build777DaisyFBWithoutInnerTCenters(_Build777DaisyCenters):
    """
    FB daisy centers with the inner t-centers dropped from the coordinate.

    Four of the five FB orbits are ranked and each puts four of its eight squares
    on F and four on B, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the FB axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges all three oblique
    orbits between F and B while the inner x-centers stay put, which is why depth
    0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . F F . F F .  . . . . . . .  . B B . B B .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . F F . F F .  . . . . . . .  . B B . B B .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-FB-without-inner-t-centers.cost-only.bin
    =================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 106 entries (0 percent, 6.62x previous step)
    3 steps has 594 entries (0 percent, 5.60x previous step)
    4 steps has 3,618 entries (0 percent, 6.09x previous step)
    5 steps has 22,250 entries (0 percent, 6.15x previous step)
    6 steps has 125,604 entries (0 percent, 5.65x previous step)
    7 steps has 635,070 entries (2 percent, 5.06x previous step)
    8 steps has 2,641,982 entries (11 percent, 4.16x previous step)
    9 steps has 7,545,582 entries (31 percent, 2.86x previous step)
    10 steps has 10,110,652 entries (42 percent, 1.34x previous step)
    11 steps has 2,862,740 entries (11 percent, 0.28x previous step)
    12 steps has 61,704 entries (0 percent, 0.02x previous step)
    13 steps has 80 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 9.48 moves
    """

    axis, omitted_orbit, table_slug = "FB", "inner-t", "FB-without-inner-t"


class Build777DaisyFBWithoutInnerXCenters(_Build777DaisyCenters):
    """
    FB daisy centers with the inner x-centers dropped from the coordinate.

    Four of the five FB orbits are ranked and each puts four of its eight squares
    on F and four on B, so the coordinate is 70^4 = 24,010,000 states. It is the
    UD table of the same name rotated onto the FB axis, so the histogram matches.

    _daisy_starting_states_777 generates two goals rather than passing an ascii
    cube. The native one is drawn below; the second exchanges all three oblique
    orbits between F and B while the inner t-centers stay put, which is why depth
    0 holds two entries.

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . F . F . F .  . . . . . . .  . B . B . B .
    . . . . . . .  . F F . F F .  . . . . . . .  . B B . B B .
    . . . . . . .  . F . F . F .  . . . . . . .  . B . B . B .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    lookup-table-7x7x7-daisy-FB-without-inner-x-centers.cost-only.bin
    =================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 16 entries (0 percent, 8.00x previous step)
    2 steps has 122 entries (0 percent, 7.62x previous step)
    3 steps has 762 entries (0 percent, 6.25x previous step)
    4 steps has 4,688 entries (0 percent, 6.15x previous step)
    5 steps has 29,272 entries (0 percent, 6.24x previous step)
    6 steps has 169,770 entries (0 percent, 5.80x previous step)
    7 steps has 891,464 entries (3 percent, 5.25x previous step)
    8 steps has 3,754,714 entries (15 percent, 4.21x previous step)
    9 steps has 9,594,114 entries (39 percent, 2.56x previous step)
    10 steps has 8,472,704 entries (35 percent, 0.88x previous step)
    11 steps has 1,084,012 entries (4 percent, 0.13x previous step)
    12 steps has 8,360 entries (0 percent, 0.01x previous step)

    Total: 24,010,000 entries
    Average: 9.19 moves
    """

    axis, omitted_orbit, table_slug = "FB", "inner-x", "FB-without-inner-x"


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

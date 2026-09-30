# standard libraries
import os
from itertools import combinations

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

# fmt: off
PHASE2_ILLEGAL_MOVES = (
    # preserve the staged LR inner centers
    "3Uw", "3Uw'",
    "3Dw", "3Dw'",
    "3Fw", "3Fw'",
    "3Bw", "3Bw'",
)
PHASE2_ORBIT1_FLIP_MOVES = ("3Lw", "3Lw'", "3Rw", "3Rw'")

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
PHASE56_ORBIT0_FLIP_MOVES = ("Lw", "Lw'", "Rw", "Rw'")

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
        flip_moves = tuple(getattr(self, "orbit_flip_moves", ()) or ())
        BFS.__init__(
            self,
            getattr(self, "builder_name", "7x7x7-phase2-UD-inner-centers-stage"),
            PHASE2_ILLEGAL_MOVES,
            "7x7x7",
            getattr(self, "table_filename", "lookup-table-7x7x7-step20-UD-inner-centers-stage.txt"),
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
            orbit_parity_flip_moves=flip_moves or None,
        )
        if flip_moves:
            directory = os.path.dirname(self.filename)
            self.orbit_parity_even_filename = os.path.join(directory, self.even_cost_name)
            self.orbit_parity_odd_filename = os.path.join(directory, self.odd_cost_name)


class Build777Phase2UDInnerCentersOrbit1Parity(Build777Phase2UDInnerCentersStage):
    """Even and odd orbit-1 distances for the UD inner t/x centers. 3Lw and 3Rw quarters flip the bit."""

    builder_name = "7x7x7-phase2-UD-inner-centers-orbit1-parity"
    table_filename = "lookup-table-7x7x7-step20-UD-inner-centers-stage-orbit1-parity.txt"
    orbit_flip_moves = PHASE2_ORBIT1_FLIP_MOVES
    even_cost_name = "lookup-table-7x7x7-step20-UD-inner-centers-stage-orbit1-even.cost-only.bin"
    odd_cost_name = "lookup-table-7x7x7-step20-UD-inner-centers-stage-orbit1-odd.cost-only.bin"


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
    name_suffix = "centers-stage"
    orbit_flip_moves = ()

    def __init__(self):
        flip_moves = tuple(self.orbit_flip_moves or ())
        BFS.__init__(
            self,
            f"7x7x7-phase5-6-UD-{self.table_slug}-{self.name_suffix}",
            PHASE5_ILLEGAL_MOVES,
            "7x7x7",
            f"lookup-table-7x7x7-phase5-6-UD-{self.table_slug}-{self.name_suffix}.txt",
            False,
            _ranked_ud_pair_starting_state_777(self.first_group, self.second_group),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=(self.first_group, self.second_group),
            orbit_parity_flip_moves=flip_moves or None,
        )
        if flip_moves:
            directory = os.path.dirname(self.filename)
            stem = f"lookup-table-7x7x7-phase5-6-UD-{self.table_slug}-centers-stage-orbit0"
            self.orbit_parity_even_filename = os.path.join(directory, stem + "-even.cost-only.bin")
            self.orbit_parity_odd_filename = os.path.join(directory, stem + "-odd.cost-only.bin")


class _Build777Phase56UDPairOrbit0Parity(_Build777Phase56UDPairStage):
    """
    Even and odd orbit-0 distances for one UD pair. Lw and Rw quarters flip
    the parity bit. Each file uses the same product rank as the blind table.

                 . . U . U . .
                 . U . . . U .
                 . . U . U . .
    """

    orbit_flip_moves = PHASE56_ORBIT0_FLIP_MOVES
    name_suffix = "centers-stage-orbit0-parity"


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


class Build777Phase56UDLeftRightObliqueOrbit0Parity(_Build777Phase56UDPairOrbit0Parity):
    """
    lookup-table-7x7x7-phase5-6-UD-left-right-oblique-centers-stage-orbit0-even.cost-only.bin
    =========================================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 10.58 moves
    """

    table_slug = "left-right-oblique"
    first_group = UFBD_LEFT_OBLIQUE_EDGES_777
    second_group = UFBD_RIGHT_OBLIQUE_EDGES_777


class Build777Phase56UDLeftMiddleObliqueOrbit0Parity(_Build777Phase56UDPairOrbit0Parity):
    """
    lookup-table-7x7x7-phase5-6-UD-left-middle-oblique-centers-stage-orbit0-even.cost-only.bin
    ==========================================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 10.58 moves
    """

    table_slug = "left-middle-oblique"
    first_group = UFBD_LEFT_OBLIQUE_EDGES_777
    second_group = UFBD_MIDDLE_OBLIQUE_EDGES_777


class Build777Phase56UDLeftObliqueOuterXOrbit0Parity(_Build777Phase56UDPairOrbit0Parity):
    """
    lookup-table-7x7x7-phase5-6-UD-left-oblique-outer-x-centers-stage-orbit0-even.cost-only.bin
    ===========================================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 9.19 moves
    """

    table_slug = "left-oblique-outer-x"
    first_group = UFBD_LEFT_OBLIQUE_EDGES_777
    second_group = UFBD_OUTER_X_CENTERS_777


class Build777Phase56UDMiddleRightObliqueOrbit0Parity(_Build777Phase56UDPairOrbit0Parity):
    """
    lookup-table-7x7x7-phase5-6-UD-middle-right-oblique-centers-stage-orbit0-even.cost-only.bin
    ===========================================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 10.58 moves
    """

    table_slug = "middle-right-oblique"
    first_group = UFBD_MIDDLE_OBLIQUE_EDGES_777
    second_group = UFBD_RIGHT_OBLIQUE_EDGES_777


class Build777Phase56UDRightObliqueOuterXOrbit0Parity(_Build777Phase56UDPairOrbit0Parity):
    """
    lookup-table-7x7x7-phase5-6-UD-right-oblique-outer-x-centers-stage-orbit0-even.cost-only.bin
    ============================================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 9.19 moves
    """

    table_slug = "right-oblique-outer-x"
    first_group = UFBD_RIGHT_OBLIQUE_EDGES_777
    second_group = UFBD_OUTER_X_CENTERS_777


class Build777Phase56UDMiddleObliqueOuterXOrbit0Parity(_Build777Phase56UDPairOrbit0Parity):
    """
    lookup-table-7x7x7-phase5-6-UD-middle-oblique-outer-x-centers-stage-orbit0-even.cost-only.bin
    =============================================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)

    Total: 165,636,900 entries
    Average: 9.19 moves
    """

    table_slug = "middle-oblique-outer-x"
    first_group = UFBD_MIDDLE_OBLIQUE_EDGES_777
    second_group = UFBD_OUTER_X_CENTERS_777


# ==================================================
# phase 7
# LR inner-t times LR inner-x
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

# Left, middle, and right sticker of each oblique bar. Choosing which four of
# the eight bars take the primary color is the C(8, 4) = 70 paired placements.
OBLIQUE_BARS_777 = {
    "UD": (
        (10, 11, 12),
        (30, 23, 16),
        (20, 27, 34),
        (40, 39, 38),
        (255, 256, 257),
        (275, 268, 261),
        (265, 272, 279),
        (285, 284, 283),
    ),
    "FB": (
        (108, 109, 110),
        (128, 121, 114),
        (118, 125, 132),
        (138, 137, 136),
        (206, 207, 208),
        (226, 219, 212),
        (216, 223, 230),
        (236, 235, 234),
    ),
}


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


# Phase 8 keeps the phase 7 state: outer turns, the six 2-wide half turns, and
# 3Lw2 / 3Rw2. The U/D/F/B 3-wide half turns are out.
PHASE8_CENTER_ILLEGAL_MOVES_777 = DAISY_CENTERS_ILLEGAL_MOVES_777 + (
    "3Uw2",
    "3Fw2",
    "3Bw2",
    "3Dw2",
)

# The paired-bar tables match the phase 8 search, which also leaves L and R
# face turns out. Those turns move the LR centers the search has to keep.
PHASE8_PAIRED_ILLEGAL_MOVES_777 = PHASE8_CENTER_ILLEGAL_MOVES_777 + (
    "L",
    "L'",
    "L2",
    "R",
    "R'",
    "R2",
)


# A daisy lets each axis be native or oblique-swapped on its own. Inners never swap.
_PHASE8_SWAPPED_AXES_777 = {
    "native": frozenset(),
    "obliques-swapped": frozenset(("UD", "LR", "FB")),
    "ud-swapped": frozenset(("UD",)),
    "fb-swapped": frozenset(("FB",)),
}


def _phase8_starting_states_777(orbits, orientations):
    """Paint each (axis, orbit, squares) triple in one goal per orientation."""
    result = []
    for orientation in orientations:
        swap_axes = _PHASE8_SWAPPED_AXES_777[orientation]
        state = ["."] * (6 * 7 * 7)
        for axis, orbit_name, squares in orbits:
            primary, opposite = DAISY_AXIS_COLORS_777[axis]
            swap = axis in swap_axes and orbit_name in DAISY_OBLIQUE_ORBITS_777
            first_color, second_color = (opposite, primary) if swap else (primary, opposite)
            for square in squares[:4]:
                state[square - 1] = first_color
            for square in squares[4:]:
                state[square - 1] = second_color
        result.append(("".join(state), "ULFRBD"))
    return tuple(result)


def _phase8_axis_orbits(axis):
    return tuple((axis, name, squares) for name, squares in DAISY_CENTER_ORBITS_777[axis])


def _phase8_paired_bar_goals_777(axis):
    """Every paired-bar placement of one axis, with its inners native.

    Each bar is one color. Exactly four bars take the primary color, so there
    are C(8, 4) = 70 goals. The slot does not matter.
    """
    primary, opposite = DAISY_AXIS_COLORS_777[axis]
    bars = OBLIQUE_BARS_777[axis]
    inner_orbits = tuple(
        squares for name, squares in DAISY_CENTER_ORBITS_777[axis] if name not in DAISY_OBLIQUE_ORBITS_777
    )
    result = []

    for chosen in combinations(range(len(bars)), 4):
        primary_bars = set(chosen)
        state = ["."] * (6 * 7 * 7)

        for index, bar in enumerate(bars):
            color = primary if index in primary_bars else opposite
            for square in bar:
                state[square - 1] = color
        for squares in inner_orbits:
            for square in squares[:4]:
                state[square - 1] = primary
            for square in squares[4:]:
                state[square - 1] = opposite
        result.append(("".join(state), "ULFRBD"))

    return tuple(result)


def _phase8_inner_plus_oblique_orbits(inner_axis, oblique_axis):
    """Inner-t and inner-x of one axis, then the three oblique orbits of the other."""
    orbits = [
        (inner_axis, name, squares)
        for name, squares in DAISY_CENTER_ORBITS_777[inner_axis]
        if name not in DAISY_OBLIQUE_ORBITS_777
    ]
    orbits.extend(
        (oblique_axis, name, squares)
        for name, squares in DAISY_CENTER_ORBITS_777[oblique_axis]
        if name in DAISY_OBLIQUE_ORBITS_777
    )
    return tuple(orbits)


def _phase8_inner_plus_paired_oblique_goals_777(inner_axis, oblique_axis):
    """Native inners on one axis, every paired-bar placement of the other.

    The three oblique orbits move as bars. Exactly four of the eight bars take
    the primary color, so there are C(8, 4) = 70 goals. Which slot those bars
    occupy does not matter. Both inner orbits stay on their native faces.
    """
    inner_primary, inner_opposite = DAISY_AXIS_COLORS_777[inner_axis]
    oblique_primary, oblique_opposite = DAISY_AXIS_COLORS_777[oblique_axis]
    bars = OBLIQUE_BARS_777[oblique_axis]
    inner_orbits = tuple(
        squares for name, squares in DAISY_CENTER_ORBITS_777[inner_axis] if name not in DAISY_OBLIQUE_ORBITS_777
    )
    result = []

    for chosen in combinations(range(len(bars)), 4):
        primary_bars = set(chosen)
        state = ["."] * (6 * 7 * 7)

        for index, bar in enumerate(bars):
            color = oblique_primary if index in primary_bars else oblique_opposite
            for square in bar:
                state[square - 1] = color
        for squares in inner_orbits:
            for square in squares[:4]:
                state[square - 1] = inner_primary
            for square in squares[4:]:
                state[square - 1] = inner_opposite
        result.append(("".join(state), "ULFRBD"))

    return tuple(result)


class _Build777Phase8Centers(BFS):
    """Shared ranked-cost builder for one phase 8 coordinate."""

    orbits = ()
    orientations = ("native",)
    table_name = None
    filename = None

    def __init__(self):
        BFS.__init__(
            self,
            self.table_name,
            PHASE8_CENTER_ILLEGAL_MOVES_777,
            "7x7x7",
            self.filename,
            False,
            _phase8_starting_states_777(self.orbits, self.orientations),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, _, squares in self.orbits),
        )


class Build777Phase8UDAxisCenters(_Build777Phase8Centers):
    """
    UD left, middle, right, inner-t, and inner-x under the phase 8 moves.

    70^5 = 1,680,700,000. Obliques swap together, so there are two goals.

    lookup-table-7x7x7-phase8-ud-axis-centers.cost-only.bin
    =======================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 12 entries (0 percent, 6.00x previous step)
    2 steps has 76 entries (0 percent, 6.33x previous step)
    3 steps has 374 entries (0 percent, 4.92x previous step)
    4 steps has 2,074 entries (0 percent, 5.55x previous step)
    5 steps has 12,078 entries (0 percent, 5.82x previous step)
    6 steps has 66,408 entries (0 percent, 5.50x previous step)
    7 steps has 356,430 entries (0 percent, 5.37x previous step)
    8 steps has 1,828,724 entries (0 percent, 5.13x previous step)
    9 steps has 8,834,016 entries (0 percent, 4.83x previous step)
    10 steps has 38,888,198 entries (2 percent, 4.40x previous step)
    11 steps has 145,365,196 entries (8 percent, 3.74x previous step)
    12 steps has 410,286,912 entries (24 percent, 2.82x previous step)
    13 steps has 672,024,380 entries (39 percent, 1.64x previous step)
    14 steps has 373,977,944 entries (22 percent, 0.56x previous step)
    15 steps has 28,924,548 entries (1 percent, 0.08x previous step)
    16 steps has 132,588 entries (0 percent, 0.00x previous step)
    17 steps has 40 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 12.74 moves

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
    """

    table_name = "7x7x7-phase8-ud-axis-centers"
    filename = "lookup-table-7x7x7-phase8-ud-axis-centers.txt"
    orbits = _phase8_axis_orbits("UD")
    orientations = ("native", "obliques-swapped")


class _Build777Phase8PairedBars(BFS):
    """70^5 axis table whose goals are the 70 paired-bar placements."""

    axis = None
    table_name = None
    filename = None

    def __init__(self):
        orbits = _phase8_axis_orbits(self.axis)
        BFS.__init__(
            self,
            self.table_name,
            PHASE8_PAIRED_ILLEGAL_MOVES_777,
            "7x7x7",
            self.filename,
            False,
            _phase8_paired_bar_goals_777(self.axis),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, _, squares in orbits),
        )


class Build777Phase8UDPairedCenters(_Build777Phase8PairedBars):
    """
    UD left, middle, right, inner-t, and inner-x.

    70^5 = 1,680,700,000. The 70 goals are the ways to choose four primary-color
    bars. Both inner orbits stay native. L and R face turns are out, matching
    the phase 8 search.

    lookup-table-7x7x7-phase8-ud-paired-centers.cost-only.bin
    """

    axis = "UD"
    table_name = "7x7x7-phase8-ud-paired-centers"
    filename = "lookup-table-7x7x7-phase8-ud-paired-centers.txt"


class Build777Phase8FBPairedCenters(_Build777Phase8PairedBars):
    """
    FB left, middle, right, inner-t, and inner-x.

    70^5 = 1,680,700,000. The 70 goals are the ways to choose four primary-color
    bars. Both inner orbits stay native. L and R face turns are out, matching
    the phase 8 search.

    lookup-table-7x7x7-phase8-fb-paired-centers.cost-only.bin
    """

    axis = "FB"
    table_name = "7x7x7-phase8-fb-paired-centers"
    filename = "lookup-table-7x7x7-phase8-fb-paired-centers.txt"


class Build777Phase8FBAxisCenters(_Build777Phase8Centers):
    """
    FB left, middle, right, inner-t, and inner-x under the phase 8 moves.

    70^5 = 1,680,700,000. Obliques swap together, so there are two goals.
    FB is a different cost from UD because 3Lw2 and 3Rw2 are legal and the
    U/D/F/B 3-wide half turns are not.

    lookup-table-7x7x7-phase8-fb-axis-centers.cost-only.bin
    =======================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 12 entries (0 percent, 6.00x previous step)
    2 steps has 76 entries (0 percent, 6.33x previous step)
    3 steps has 374 entries (0 percent, 4.92x previous step)
    4 steps has 2,074 entries (0 percent, 5.55x previous step)
    5 steps has 12,078 entries (0 percent, 5.82x previous step)
    6 steps has 66,408 entries (0 percent, 5.50x previous step)
    7 steps has 356,430 entries (0 percent, 5.37x previous step)
    8 steps has 1,828,724 entries (0 percent, 5.13x previous step)
    9 steps has 8,834,016 entries (0 percent, 4.83x previous step)
    10 steps has 38,888,198 entries (2 percent, 4.40x previous step)
    11 steps has 145,365,196 entries (8 percent, 3.74x previous step)
    12 steps has 410,286,912 entries (24 percent, 2.82x previous step)
    13 steps has 672,024,380 entries (39 percent, 1.64x previous step)
    14 steps has 373,977,944 entries (22 percent, 0.56x previous step)
    15 steps has 28,924,548 entries (1 percent, 0.08x previous step)
    16 steps has 132,588 entries (0 percent, 0.00x previous step)
    17 steps has 40 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 12.74 moves

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
    . . . . . . .  . F F . F F .  . . . . . . .  . B B . B B .
    . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
    """

    table_name = "7x7x7-phase8-fb-axis-centers"
    filename = "lookup-table-7x7x7-phase8-fb-axis-centers.txt"
    orbits = _phase8_axis_orbits("FB")
    orientations = ("native", "obliques-swapped")


class Build777Phase8LRObliqueCenters(_Build777Phase8Centers):
    """
    Where the eight paired LR bars sit.

    Phase 8 keeps every L/R bar one color, so the middle and right stickers
    match the left sticker. The coordinate is that left orbit, C(8, 4) = 70.
    Both daisy orientations are goals.

    lookup-table-7x7x7-phase8-lr-oblique-centers.cost-only.bin
    ==========================================================
    0 steps has 2 entries (2 percent, 0.00x previous step)
    1 steps has 8 entries (11 percent, 4.00x previous step)
    2 steps has 30 entries (42 percent, 3.75x previous step)
    3 steps has 30 entries (42 percent, 1.00x previous step)

    Total: 70 entries
    Average: 2.26 moves

                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
    . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
    . . L . L . .  . . . . . . .  . . R . R . .  . . . . . . .
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

    table_name = "7x7x7-phase8-lr-oblique-centers"
    filename = "lookup-table-7x7x7-phase8-lr-oblique-centers.txt"
    orbits = (("LR", "left-oblique", LR_LEFT_OBLIQUE_CENTERS_777),)
    orientations = ("native", "obliques-swapped")


class Build777Phase8InnerInteractionCenters(_Build777Phase8Centers):
    """
    UD inner-t, UD inner-x, FB inner-t, and FB inner-x.

    70^4 = 24,010,000. Inners do not swap, so there is one goal. 3Lw2 and
    3Rw2 move the UD and FB inners in the same turn.

    lookup-table-7x7x7-phase8-inner-interaction-centers.cost-only.bin
    ==================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 25 entries (0 percent, 12.50x previous step)
    3 steps has 146 entries (0 percent, 5.84x previous step)
    4 steps has 544 entries (0 percent, 3.73x previous step)
    5 steps has 2,772 entries (0 percent, 5.10x previous step)
    6 steps has 13,681 entries (0 percent, 4.94x previous step)
    7 steps has 57,790 entries (0 percent, 4.22x previous step)
    8 steps has 227,221 entries (0 percent, 3.93x previous step)
    9 steps has 797,842 entries (3 percent, 3.51x previous step)
    10 steps has 2,318,392 entries (9 percent, 2.91x previous step)
    11 steps has 5,327,072 entries (22 percent, 2.30x previous step)
    12 steps has 7,922,750 entries (32 percent, 1.49x previous step)
    13 steps has 5,900,762 entries (24 percent, 0.74x previous step)
    14 steps has 1,378,088 entries (5 percent, 0.23x previous step)
    15 steps has 62,000 entries (0 percent, 0.04x previous step)
    16 steps has 912 entries (0 percent, 0.01x previous step)

    Total: 24,010,000 entries
    Average: 11.80 moves

                   . . . . . . .
                   . . . . . . .
                   . . U U U . .
                   . . U . U . .
                   . . U U U . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
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

    table_name = "7x7x7-phase8-inner-interaction-centers"
    filename = "lookup-table-7x7x7-phase8-inner-interaction-centers.txt"
    orbits = (
        ("UD", "inner-t", UD_INNER_T_CENTERS_777),
        ("UD", "inner-x", UD_INNER_X_CENTERS_777),
        ("FB", "inner-t", FB_INNER_T_CENTERS_777),
        ("FB", "inner-x", FB_INNER_X_CENTERS_777),
    )
    orientations = ("native",)


class Build777Phase8MiddleInteractionCenters(_Build777Phase8Centers):
    """
    UD inner-x, FB inner-x, UD middle, and FB middle.

    70^4 = 24,010,000. Each middle swaps on its own, so there are four goals.
    3Lw2 and 3Rw2 change this coordinate on both axes at once.

    lookup-table-7x7x7-phase8-middle-interaction-centers.cost-only.bin
    ===================================================================
    0 steps has 4 entries (0 percent, 0.00x previous step)
    1 steps has 32 entries (0 percent, 8.00x previous step)
    2 steps has 448 entries (0 percent, 14.00x previous step)
    3 steps has 4,104 entries (0 percent, 9.16x previous step)
    4 steps has 30,220 entries (0 percent, 7.36x previous step)
    5 steps has 209,320 entries (0 percent, 6.93x previous step)
    6 steps has 1,032,256 entries (4 percent, 4.93x previous step)
    7 steps has 3,492,320 entries (14 percent, 3.38x previous step)
    8 steps has 7,802,240 entries (32 percent, 2.23x previous step)
    9 steps has 7,284,944 entries (30 percent, 0.93x previous step)
    10 steps has 3,699,648 entries (15 percent, 0.51x previous step)
    11 steps has 454,048 entries (1 percent, 0.12x previous step)
    12 steps has 416 entries (0 percent, 0.00x previous step)

    Total: 24,010,000 entries
    Average: 8.40 moves

                   . . . . . . .
                   . . . . . . .
                   . . U . U . .
                   . . . U . . .
                   . . U . U . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . . . F . . .  . . . . . . .  . . . B . . .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . D . D . .
                   . . . D . . .
                   . . D . D . .
                   . . . . . . .
                   . . . . . . .
    """

    table_name = "7x7x7-phase8-middle-interaction-centers"
    filename = "lookup-table-7x7x7-phase8-middle-interaction-centers.txt"
    orbits = (
        ("UD", "inner-x", UD_INNER_X_CENTERS_777),
        ("FB", "inner-x", FB_INNER_X_CENTERS_777),
        ("UD", "middle-oblique", UD_MIDDLE_OBLIQUE_CENTERS_777),
        ("FB", "middle-oblique", FB_MIDDLE_OBLIQUE_CENTERS_777),
    )
    orientations = ("native", "obliques-swapped", "ud-swapped", "fb-swapped")


class Build777Phase8UDObliquesFBEdgesCenters(_Build777Phase8Centers):
    """
    UD left, middle, and right, plus FB left and FB right.

    70^5 = 1,680,700,000. These are the oblique orbits in the UD axis table
    with the two UD inners replaced by FB's edge obliques. UD and FB swap
    independently, so there are four goals.

    lookup-table-7x7x7-phase8-ud-obliques-fb-edges-centers.cost-only.bin
    =====================================================================
    0 steps has 4 entries (0 percent, 0.00x previous step)
    1 steps has 32 entries (0 percent, 8.00x previous step)
    2 steps has 400 entries (0 percent, 12.50x previous step)
    3 steps has 3,248 entries (0 percent, 8.12x previous step)
    4 steps has 23,448 entries (0 percent, 7.22x previous step)
    5 steps has 185,280 entries (0 percent, 7.90x previous step)
    6 steps has 1,359,416 entries (0 percent, 7.34x previous step)
    7 steps has 8,329,088 entries (0 percent, 6.13x previous step)
    8 steps has 40,484,952 entries (2 percent, 4.86x previous step)
    9 steps has 143,396,852 entries (8 percent, 3.54x previous step)
    10 steps has 368,888,976 entries (21 percent, 2.57x previous step)
    11 steps has 567,013,800 entries (33 percent, 1.54x previous step)
    12 steps has 424,265,120 entries (25 percent, 0.75x previous step)
    13 steps has 116,979,176 entries (6 percent, 0.28x previous step)
    14 steps has 9,612,896 entries (0 percent, 0.08x previous step)
    15 steps has 157,312 entries (0 percent, 0.02x previous step)

    Total: 1,680,700,000 entries
    Average: 10.92 moves

                   . . . . . . .
                   . . U U U . .
                   . U . . . U .
                   . U . . . U .
                   . U . . . U .
                   . . U U U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D D D . .
                   . D . . . D .
                   . D . . . D .
                   . D . . . D .
                   . . D D D . .
                   . . . . . . .
    """

    table_name = "7x7x7-phase8-ud-obliques-fb-edges-centers"
    filename = "lookup-table-7x7x7-phase8-ud-obliques-fb-edges-centers.txt"
    orbits = (
        ("UD", "left-oblique", UD_LEFT_OBLIQUE_CENTERS_777),
        ("UD", "middle-oblique", UD_MIDDLE_OBLIQUE_CENTERS_777),
        ("UD", "right-oblique", UD_RIGHT_OBLIQUE_CENTERS_777),
        ("FB", "left-oblique", FB_LEFT_OBLIQUE_CENTERS_777),
        ("FB", "right-oblique", FB_RIGHT_OBLIQUE_CENTERS_777),
    )
    orientations = ("native", "obliques-swapped", "ud-swapped", "fb-swapped")


class Build777Phase8FBObliquesUDEdgesCenters(_Build777Phase8Centers):
    """
    UD left and UD right, plus FB left, middle, and right.

    70^5 = 1,680,700,000. The FB-sided twin of the UD oblique table: FB's
    three obliques, with UD's two edge obliques in place of the FB inners.
    UD and FB swap independently, so there are four goals.

    lookup-table-7x7x7-phase8-fb-obliques-ud-edges-centers.cost-only.bin
    =====================================================================
    0 steps has 4 entries (0 percent, 0.00x previous step)
    1 steps has 32 entries (0 percent, 8.00x previous step)
    2 steps has 400 entries (0 percent, 12.50x previous step)
    3 steps has 3,248 entries (0 percent, 8.12x previous step)
    4 steps has 23,448 entries (0 percent, 7.22x previous step)
    5 steps has 185,280 entries (0 percent, 7.90x previous step)
    6 steps has 1,359,416 entries (0 percent, 7.34x previous step)
    7 steps has 8,329,088 entries (0 percent, 6.13x previous step)
    8 steps has 40,484,952 entries (2 percent, 4.86x previous step)
    9 steps has 143,396,852 entries (8 percent, 3.54x previous step)
    10 steps has 368,888,976 entries (21 percent, 2.57x previous step)
    11 steps has 567,013,800 entries (33 percent, 1.54x previous step)
    12 steps has 424,265,120 entries (25 percent, 0.75x previous step)
    13 steps has 116,979,176 entries (6 percent, 0.28x previous step)
    14 steps has 9,612,896 entries (0 percent, 0.08x previous step)
    15 steps has 157,312 entries (0 percent, 0.02x previous step)

    Total: 1,680,700,000 entries
    Average: 10.92 moves

                   . . . . . . .
                   . . U . U . .
                   . U . . . U .
                   . . . . . . .
                   . U . . . U .
                   . . U . U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D . D . .
                   . D . . . D .
                   . . . . . . .
                   . D . . . D .
                   . . D . D . .
                   . . . . . . .
    """

    table_name = "7x7x7-phase8-fb-obliques-ud-edges-centers"
    filename = "lookup-table-7x7x7-phase8-fb-obliques-ud-edges-centers.txt"
    orbits = (
        ("UD", "left-oblique", UD_LEFT_OBLIQUE_CENTERS_777),
        ("UD", "right-oblique", UD_RIGHT_OBLIQUE_CENTERS_777),
        ("FB", "left-oblique", FB_LEFT_OBLIQUE_CENTERS_777),
        ("FB", "middle-oblique", FB_MIDDLE_OBLIQUE_CENTERS_777),
        ("FB", "right-oblique", FB_RIGHT_OBLIQUE_CENTERS_777),
    )
    orientations = ("native", "obliques-swapped", "ud-swapped", "fb-swapped")


class Build777Phase8UDObliquesFBInnerTCenters(_Build777Phase8Centers):
    """
    UD left, middle, right, and inner-t, plus FB inner-t.

    70^5 = 1,680,700,000. This keeps the UD orbits that carry the axis cost
    and replaces UD inner-x with FB inner-t. Inners do not swap, so the FB
    sticker is the same in both daisy orientations and there are two goals.

    lookup-table-7x7x7-phase8-ud-obliques-fb-inner-t-centers.cost-only.bin
    ======================================================================
    0 steps has 2 entries (0 percent, 0.00x previous step)
    1 steps has 12 entries (0 percent, 6.00x previous step)
    2 steps has 104 entries (0 percent, 8.67x previous step)
    3 steps has 806 entries (0 percent, 7.75x previous step)
    4 steps has 5,914 entries (0 percent, 7.34x previous step)
    5 steps has 39,110 entries (0 percent, 6.61x previous step)
    6 steps has 242,700 entries (0 percent, 6.21x previous step)
    7 steps has 1,422,964 entries (0 percent, 5.86x previous step)
    8 steps has 7,695,544 entries (0 percent, 5.41x previous step)
    9 steps has 36,187,386 entries (2 percent, 4.70x previous step)
    10 steps has 135,939,084 entries (8 percent, 3.76x previous step)
    11 steps has 351,830,036 entries (20 percent, 2.59x previous step)
    12 steps has 563,981,174 entries (33 percent, 1.60x previous step)
    13 steps has 472,871,752 entries (28 percent, 0.84x previous step)
    14 steps has 107,356,752 entries (6 percent, 0.23x previous step)
    15 steps has 3,124,748 entries (0 percent, 0.03x previous step)
    16 steps has 1,912 entries (0 percent, 0.00x previous step)

    Total: 1,680,700,000 entries
    Average: 11.96 moves

                   . . . . . . .
                   . . U U U . .
                   . U . U . U .
                   . U U . U U .
                   . U . U . U .
                   . . U U U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . F . . .  . . . . . . .  . . . B . . .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . . . F . . .  . . . . . . .  . . . B . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D D D . .
                   . D . D . D .
                   . D D . D D .
                   . D . D . D .
                   . . D D D . .
                   . . . . . . .
    """

    table_name = "7x7x7-phase8-ud-obliques-fb-inner-t-centers"
    filename = "lookup-table-7x7x7-phase8-ud-obliques-fb-inner-t-centers.txt"
    orbits = (
        ("UD", "left-oblique", UD_LEFT_OBLIQUE_CENTERS_777),
        ("UD", "middle-oblique", UD_MIDDLE_OBLIQUE_CENTERS_777),
        ("UD", "right-oblique", UD_RIGHT_OBLIQUE_CENTERS_777),
        ("UD", "inner-t", UD_INNER_T_CENTERS_777),
        ("FB", "inner-t", FB_INNER_T_CENTERS_777),
    )
    orientations = ("native", "obliques-swapped")


class _Build777Phase8InnerPlusPairedObliques(BFS):
    """70^5 table: native inners on one axis, 70 paired oblique placements on the other."""

    inner_axis = None
    oblique_axis = None
    table_name = None
    filename = None

    def __init__(self):
        orbits = _phase8_inner_plus_oblique_orbits(self.inner_axis, self.oblique_axis)
        BFS.__init__(
            self,
            self.table_name,
            PHASE8_PAIRED_ILLEGAL_MOVES_777,
            "7x7x7",
            self.filename,
            False,
            _phase8_inner_plus_paired_oblique_goals_777(self.inner_axis, self.oblique_axis),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, _, squares in orbits),
        )


class Build777Phase8UDInnerFBObliquesCenters(_Build777Phase8InnerPlusPairedObliques):
    """
    UD inner-t, UD inner-x, and the three FB oblique orbits.

    70^5 = 1,680,700,000. The 70 goals choose which four FB bars take the
    primary color; the slot those bars occupy does not matter. Both UD inner
    orbits stay native. L and R face turns are out, matching the phase 8
    search. Rank order is UD inner-t, UD inner-x, FB left, FB middle, FB right.

    lookup-table-7x7x7-phase8-ud-inner-fb-obliques-centers.cost-only.bin

                   . . . . . . .
                   . . . . . . .
                   . . U U U . .
                   . . U . U . .
                   . . U U U . .
                   . . . . . . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . . . . . .
                   . . D D D . .
                   . . D . D . .
                   . . D D D . .
                   . . . . . . .
                   . . . . . . .
    """

    inner_axis = "UD"
    oblique_axis = "FB"
    table_name = "7x7x7-phase8-ud-inner-fb-obliques-centers"
    filename = "lookup-table-7x7x7-phase8-ud-inner-fb-obliques-centers.txt"


class Build777Phase8FBInnerUDObliquesCenters(_Build777Phase8InnerPlusPairedObliques):
    """
    FB inner-t, FB inner-x, and the three UD oblique orbits.

    70^5 = 1,680,700,000. The 70 goals choose which four UD bars take the
    primary color; the slot those bars occupy does not matter. Both FB inner
    orbits stay native. L and R face turns are out, matching the phase 8
    search. Rank order is FB inner-t, FB inner-x, UD left, UD middle, UD right.

    lookup-table-7x7x7-phase8-fb-inner-ud-obliques-centers.cost-only.bin

                   . . . . . . .
                   . . U U U . .
                   . U . . . U .
                   . . U . U . .
                   . U . . . U .
                   . . U U U . .
                   . . . . . . .

    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . F . F . .  . . . . . . .  . . B . B . .
    . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
    . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                   . . . . . . .
                   . . D D D . .
                   . D . . . D .
                   . . D . D . .
                   . D . . . D .
                   . . D D D . .
                   . . . . . . .
    """

    inner_axis = "FB"
    oblique_axis = "UD"
    table_name = "7x7x7-phase8-fb-inner-ud-obliques-centers"
    filename = "lookup-table-7x7x7-phase8-fb-inner-ud-obliques-centers.txt"

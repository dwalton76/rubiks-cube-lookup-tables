# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)


# fmt: off
PHASE2_ILLEGAL_MOVES = (
    # preserve the staged L/R inner centers
    "3Uw", "3Uw'",
    "3Dw", "3Dw'",
    "3Fw", "3Fw'",
    "3Bw", "3Bw'",
)

PHASE5_STARTING_STATES_ILLEGAL_MOVES = (
    "3Uw", "3Uw'", "3Uw2",
    "3Dw", "3Dw'", "3Dw2",
    "3Fw", "3Fw'", "3Fw2",
    "3Bw", "3Bw'", "3Bw2",
    "3Lw", "3Lw'", "3Lw2",
    "3Rw", "3Rw'", "3Rw2",
    "Uw", "Uw'",
    "Dw", "Dw'",
    "Fw", "Fw'",
    "Bw", "Bw'",
    "L", "L'", "L2",
    "R", "R'", "R2",
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
    """Build the (16! / (8! * 8!))^2 = 165,636,900-state ranked table."""

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
    """Return a solved U/D-vs-other state for two 16-sticker coordinates."""
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

    (16! / (8! * 8!))^2 = 165,636,900 states

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

    (16! / (8! * 8!))^2 = 165,636,900 states

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

    (16! / (8! * 8!))^2 = 165,636,900 states

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

    (16! / (8! * 8!))^2 = 165,636,900 states

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

    (16! / (8! * 8!))^2 = 165,636,900 states

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

    (16! / (8! * 8!))^2 = 165,636,900 states

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
        )


class Build777DaisyUDWithoutLeftObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "UD", "left-oblique", "UD-without-left-oblique"


class Build777DaisyUDWithoutMiddleObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "UD", "middle-oblique", "UD-without-middle-oblique"


class Build777DaisyUDWithoutRightObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "UD", "right-oblique", "UD-without-right-oblique"


class Build777DaisyUDWithoutInnerTCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "UD", "inner-t", "UD-without-inner-t"


class Build777DaisyUDWithoutInnerXCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "UD", "inner-x", "UD-without-inner-x"


class Build777DaisyLRWithoutLeftObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "LR", "left-oblique", "LR-without-left-oblique"


class Build777DaisyLRWithoutMiddleObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "LR", "middle-oblique", "LR-without-middle-oblique"


class Build777DaisyLRWithoutRightObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "LR", "right-oblique", "LR-without-right-oblique"


class Build777DaisyLRWithoutInnerTCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "LR", "inner-t", "LR-without-inner-t"


class Build777DaisyLRWithoutInnerXCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "LR", "inner-x", "LR-without-inner-x"


class Build777DaisyFBWithoutLeftObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "FB", "left-oblique", "FB-without-left-oblique"


class Build777DaisyFBWithoutMiddleObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "FB", "middle-oblique", "FB-without-middle-oblique"


class Build777DaisyFBWithoutRightObliqueCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "FB", "right-oblique", "FB-without-right-oblique"


class Build777DaisyFBWithoutInnerTCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "FB", "inner-t", "FB-without-inner-t"


class Build777DaisyFBWithoutInnerXCenters(_Build777DaisyCenters):
    axis, omitted_orbit, table_slug = "FB", "inner-x", "FB-without-inner-x"


class Build777DaisyUDPerfectCenters(_Build777DaisyCenters):
    axis, table_slug = "UD", "UD-perfect"


class Build777DaisyLRPerfectCenters(_Build777DaisyCenters):
    axis, table_slug = "LR", "LR-perfect"


class Build777DaisyFBPerfectCenters(_Build777DaisyCenters):
    axis, table_slug = "FB", "FB-perfect"


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


class Build777SolveUDPerfectCenters(_Build777SolveCenters):
    axis, table_slug = "UD", "UD-perfect"


class Build777SolveLRPerfectCenters(_Build777SolveCenters):
    axis, table_slug = "LR", "LR-perfect"


class Build777SolveFBPerfectCenters(_Build777SolveCenters):
    axis, table_slug = "FB", "FB-perfect"


# ==================================================
# phase 5
# pair UD oblique edges
# ==================================================
class Build777Phase5LeftOblique(BFS):
    """
    16! / (8! * 8!) = 12,870 states

    lookup-table-7x7x7-phase5-left-oblique.txt
    ==========================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 29 entries (0 percent, 14.50x previous step)
    3 steps has 238 entries (1 percent, 8.21x previous step)
    4 steps has 742 entries (5 percent, 3.12x previous step)
    5 steps has 1,836 entries (14 percent, 2.47x previous step)
    6 steps has 4,405 entries (34 percent, 2.40x previous step)
    7 steps has 3,774 entries (29 percent, 0.86x previous step)
    8 steps has 1,721 entries (13 percent, 0.46x previous step)
    9 steps has 122 entries (0 percent, 0.07x previous step)

    Total: 12,870 entries
    Average: 6.27 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-left-oblique",
            PHASE5_ILLEGAL_MOVES,
            "7x7x7",
            "lookup-table-7x7x7-phase5-left-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . . . .  . . . . . . .  . . x . . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . . x . .  . . . . . . .  . . . . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build777Phase5RightOblique(BFS):
    """
    16! / (8! * 8!) = 12,870 states

    lookup-table-7x7x7-phase5-right-oblique.txt
    ===========================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 29 entries (0 percent, 14.50x previous step)
    3 steps has 238 entries (1 percent, 8.21x previous step)
    4 steps has 742 entries (5 percent, 3.12x previous step)
    5 steps has 1,836 entries (14 percent, 2.47x previous step)
    6 steps has 4,405 entries (34 percent, 2.40x previous step)
    7 steps has 3,774 entries (29 percent, 0.86x previous step)
    8 steps has 1,721 entries (13 percent, 0.46x previous step)
    9 steps has 122 entries (0 percent, 0.07x previous step)

    Total: 12,870 entries
    Average: 6.27 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-right-oblique",
            PHASE5_ILLEGAL_MOVES,
            "7x7x7",
            "lookup-table-7x7x7-phase5-right-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . x . .  . . . . . . .  . . . . x . .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . . x . . . .  . . . . . . .  . . x . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build777Phase5MiddleOblique(BFS):
    """
    16! / (8! * 8!) = 12,870 states

    lookup-table-7x7x7-phase5-middle-oblique.txt
    ============================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 25 entries (0 percent, 12.50x previous step)
    3 steps has 210 entries (1 percent, 8.40x previous step)
    4 steps has 722 entries (5 percent, 3.44x previous step)
    5 steps has 1,752 entries (13 percent, 2.43x previous step)
    6 steps has 4,033 entries (31 percent, 2.30x previous step)
    7 steps has 4,014 entries (31 percent, 1.00x previous step)
    8 steps has 1,977 entries (15 percent, 0.49x previous step)
    9 steps has 134 entries (1 percent, 0.07x previous step)

    Total: 12,870 entries
    Average: 6.34 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-middle-oblique",
            PHASE5_ILLEGAL_MOVES,
            "7x7x7",
            "lookup-table-7x7x7-phase5-middle-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class StartingStates777Phase5LeftRightOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-left-right-oblique",
            PHASE5_STARTING_STATES_ILLEGAL_MOVES,
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase5-left-right-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
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
                . . . . . . . """,
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build777Phase5LeftRightOblique(BFS):
    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase5_left_right_oblique_ss
        BFS.__init__(
            self,
            "7x7x7-phase5",
            PHASE5_ILLEGAL_MOVES,
            "7x7x7",
            "lookup-table-7x7x7-phase5-left-right-oblique.txt",
            False,  # store_as_hex
            phase5_left_right_oblique_ss,
            use_c=True,
        )
        # fmt: on


class StartingStates777Phase5LeftMiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-left-middle-oblique",
            PHASE5_STARTING_STATES_ILLEGAL_MOVES,
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase5-left-middle-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
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
                . . . . . . . """,
                    "ascii",
                ),
            ),
            use_c=True,
        )
        # fmt: on


class Build777Phase5LeftMiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase5_left_middle_oblique_ss
        BFS.__init__(
            self,
            "7x7x7-phase5",
            PHASE5_ILLEGAL_MOVES,
            "7x7x7",
            "lookup-table-7x7x7-phase5-left-middle-oblique.txt",
            False,  # store_as_hex
            phase5_left_middle_oblique_ss,
            use_c=True,
        )
        # fmt: on

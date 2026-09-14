# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS
from rubikscubennnsolver.RubiksCube666 import inner_x_centers_666

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

# fmt: on


# ==================================================
# phase 1
# stage all inner x-centers and pair the LR obliques
# ==================================================
class Build666InnerXCentersStageOnePhase(BFS):
    """
    Stage all 24 inner x-centers in one phase (8 UD, 8 LR, 8 FB).

    24! / (8!^3) = 9,465,511,770 raw colorings, stored as the 197,221,662
    orbits under the 48 cube symmetries (same geometry as 4x4 centers).
    The live BFS still needs the 9.47 GiB canonical-rank mmap; save() then
    compact-center-symmetry-cost writes ~188 MiB plus the symmetry index.
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
            ranked_cost_type="center-symmetry-444",
            ranked_cost_square_groups=(inner_x_centers_666,),
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
# daisy-solve all centers with overlapping 70^4 ranked tables
# ==================================================
# Nine (4,4) orbits: left-oblique, right-oblique, and inner-x on each of UD, LR,
# and FB. C(9,4) = 126 tables of 24,010,000 states exist. The first attempt
# keeps the 18 tables that contain one complete axis plus one foreign orbit.

# fmt: off
DAISY_LEFT_OBLIQUE_UD_666 = (9, 17, 28, 20, 189, 197, 208, 200)
DAISY_RIGHT_OBLIQUE_UD_666 = (10, 23, 27, 14, 190, 203, 207, 194)
DAISY_INNER_X_UD_666 = (15, 16, 21, 22, 195, 196, 201, 202)
DAISY_LEFT_OBLIQUE_LR_666 = (45, 53, 64, 56, 117, 125, 136, 128)
DAISY_RIGHT_OBLIQUE_LR_666 = (46, 59, 63, 50, 118, 131, 135, 122)
DAISY_INNER_X_LR_666 = (51, 52, 57, 58, 123, 124, 129, 130)
DAISY_LEFT_OBLIQUE_FB_666 = (81, 89, 100, 92, 153, 161, 172, 164)
DAISY_RIGHT_OBLIQUE_FB_666 = (82, 95, 99, 86, 154, 167, 171, 158)
DAISY_INNER_X_FB_666 = (87, 88, 93, 94, 159, 160, 165, 166)
# fmt: on

DAISY_CENTERS_ILLEGAL_MOVES_666 = PHASE5_ILLEGAL_MOVES
DAISY_ORBIT_NAMES_666 = ("left-oblique", "right-oblique", "inner-x")
DAISY_AXES_666 = ("UD", "LR", "FB")
DAISY_AXIS_COLORS_666 = {"UD": ("U", "D"), "LR": ("L", "R"), "FB": ("F", "B")}
DAISY_OBLIQUE_ORBITS_666 = frozenset(("left-oblique", "right-oblique"))
DAISY_CENTER_ORBITS_666 = {
    "UD": (
        ("left-oblique", DAISY_LEFT_OBLIQUE_UD_666),
        ("right-oblique", DAISY_RIGHT_OBLIQUE_UD_666),
        ("inner-x", DAISY_INNER_X_UD_666),
    ),
    "LR": (
        ("left-oblique", DAISY_LEFT_OBLIQUE_LR_666),
        ("right-oblique", DAISY_RIGHT_OBLIQUE_LR_666),
        ("inner-x", DAISY_INNER_X_LR_666),
    ),
    "FB": (
        ("left-oblique", DAISY_LEFT_OBLIQUE_FB_666),
        ("right-oblique", DAISY_RIGHT_OBLIQUE_FB_666),
        ("inner-x", DAISY_INNER_X_FB_666),
    ),
}


def _daisy_orbit_token_666(orbit):
    return "".join(part.title() for part in orbit.split("-"))


def daisy_plus_table_specs_666():
    """One complete axis plus one orbit from a different axis: 3 * 6 = 18 tables."""
    specs = []
    for axis in DAISY_AXES_666:
        for extra_axis in DAISY_AXES_666:
            if extra_axis == axis:
                continue
            for orbit in DAISY_ORBIT_NAMES_666:
                slug = f"{axis}-plus-{extra_axis}-{orbit}"
                class_name = f"Build666Daisy{axis}Plus{extra_axis}{_daisy_orbit_token_666(orbit)}Centers"
                specs.append((axis, extra_axis, orbit, slug, class_name))
    return tuple(specs)


def _daisy_starting_states_666(selected_orbits):
    """
    Product of native and obliques-swapped goals for every axis that appears.

    Inner-x stays native in both orientations. Axes can be oriented independently,
    so a mixed-axis table needs the product rather than a single global swap.
    """
    axes = []
    for axis in DAISY_AXES_666:
        if any(orbit in DAISY_CENTER_ORBITS_666[axis] for orbit in selected_orbits):
            axes.append(axis)

    result = []
    for orientation_bits in range(1 << len(axes)):
        state = ["."] * (6 * 6 * 6)
        for axis_index, axis in enumerate(axes):
            swapped = bool(orientation_bits & (1 << axis_index))
            primary, opposite = DAISY_AXIS_COLORS_666[axis]
            for orbit_name, squares in selected_orbits:
                if (orbit_name, squares) not in DAISY_CENTER_ORBITS_666[axis]:
                    continue
                swap = swapped and orbit_name in DAISY_OBLIQUE_ORBITS_666
                first_color, second_color = (opposite, primary) if swap else (primary, opposite)
                for square in squares[:4]:
                    state[square - 1] = first_color
                for square in squares[4:]:
                    state[square - 1] = second_color
        result.append(("".join(state), "ULFRBD"))
    return tuple(result)


class _Build666DaisyCenters(BFS):
    """
    Dense ranked-cost 70^4 builder: one complete axis plus one foreign orbit.

    Extra oblique (four starting states). Average 8.50 moves, max 12:
    0:4 1:44 2:588 3:4,904 4:29,792 5:155,444 6:752,892 7:3,004,980
    8:7,417,368 9:8,651,032 10:3,621,656 11:369,888 12:1,408

    Extra inner-x (two starting states). Average 9.43 moves, max 13:
    0:2 1:20 2:220 3:1,746 4:11,510 5:64,150 6:316,284 7:1,274,168
    8:3,676,310 9:6,634,726 10:7,000,712 11:4,202,184 12:808,704 13:19,264
    """

    axis = None
    extra_axis = None
    extra_orbit = None
    table_slug = None

    def __init__(self):
        selected_orbits = DAISY_CENTER_ORBITS_666[self.axis] + tuple(
            orbit for orbit in DAISY_CENTER_ORBITS_666[self.extra_axis] if orbit[0] == self.extra_orbit
        )
        self.selected_orbits = selected_orbits
        self.goal_orientations = ("native", "obliques-swapped")

        BFS.__init__(
            self,
            f"6x6x6-daisy-{self.table_slug}-centers",
            DAISY_CENTERS_ILLEGAL_MOVES_666,
            "6x6x6",
            f"lookup-table-6x6x6-daisy-{self.table_slug}-centers.txt",
            False,
            _daisy_starting_states_666(selected_orbits),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, squares in selected_orbits),
        )


def _install_daisy_plus_builders_666():
    for axis, extra_axis, extra_orbit, slug, class_name in daisy_plus_table_specs_666():
        globals()[class_name] = type(
            class_name,
            (_Build666DaisyCenters,),
            {
                "axis": axis,
                "extra_axis": extra_axis,
                "extra_orbit": extra_orbit,
                "table_slug": slug,
            },
        )


_install_daisy_plus_builders_666()

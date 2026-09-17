# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS
from rubikscubennnsolver.RubiksCube666 import RubiksCube666, inner_x_centers_666, solved_666

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


def _ranked_inner_x_axis_starting_state(axis):
    cube = RubiksCube666(solved_666, "URFDLB")
    state = ["."] * len(cube.state)
    for square in inner_x_centers_666:
        state[square] = axis[0] if cube.state[square] in axis else "x"
    return (("".join(state[1:]), "ULFRBD"),)


# ==================================================
# phases 1 and 2
# phase 1 stages LR inner x; phase 2 stages UD inner x while pairing LR obliques
# ==================================================
class Build666Phase2UDInnerXCentersStageBinary(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "6x6x6-phase2-UD-inner-x-centers-stage-binary",
            (),
            "6x6x6",
            "lookup-table-6x6x6-step11-UD-inner-x-centers-stage-binary.txt",
            False,
            _ranked_inner_x_axis_starting_state("UD"),
            use_c=True,
            use_ranked_cost=True,
        )


class Build666Phase1LRInnerXCentersStageBinary(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "6x6x6-phase1-LR-inner-x-centers-stage-binary",
            (),
            "6x6x6",
            "lookup-table-6x6x6-step12-LR-inner-x-centers-stage-binary.txt",
            False,
            _ranked_inner_x_axis_starting_state("LR"),
            use_c=True,
            use_ranked_cost=True,
        )


# ==================================================
# phase 4
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
# daisy-solve all remaining centers with three 70^5 ranked tables:
# all inner-x orbits plus both obliques from one axis.
# ==================================================

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


def daisy_inner_x_spine_table_specs_666():
    """All three inner-x orbits plus both obliques from one axis: three 70^5 tables."""
    return tuple(
        (
            axis,
            f"all-inner-x-plus-{axis}-obliques",
            f"Build666DaisyAllInnerXPlus{axis}ObliquesCenters",
        )
        for axis in DAISY_AXES_666
    )


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


class _Build666DaisyInnerXSpineCenters(BFS):
    """Dense ranked-cost 70^5 builder: every inner-x orbit plus one axis's obliques."""

    axis = None
    table_slug = None

    def __init__(self):
        selected_orbits = tuple(
            orbit for axis in DAISY_AXES_666 for orbit in DAISY_CENTER_ORBITS_666[axis] if orbit[0] == "inner-x"
        ) + tuple(orbit for orbit in DAISY_CENTER_ORBITS_666[self.axis] if orbit[0] != "inner-x")
        self.selected_orbits = selected_orbits
        self.goal_orientations = ("native", "obliques-swapped")

        BFS.__init__(
            self,
            f"6x6x6-daisy-{self.table_slug}-centers",
            DAISY_CENTERS_ILLEGAL_MOVES_666,
            "6x6x6",
            f"lookup-table-6x6x6-daisy-{self.table_slug}-centers.txt",
            False,
            tuple(dict.fromkeys(_daisy_starting_states_666(selected_orbits))),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_square_groups=tuple(squares for _, squares in selected_orbits),
        )


def _install_daisy_inner_x_spine_builders_666():
    for axis, slug, class_name in daisy_inner_x_spine_table_specs_666():
        globals()[class_name] = type(
            class_name,
            (_Build666DaisyInnerXSpineCenters,),
            {
                "axis": axis,
                "table_slug": slug,
            },
        )


_install_daisy_inner_x_spine_builders_666()

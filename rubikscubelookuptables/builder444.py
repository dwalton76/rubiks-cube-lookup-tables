# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS
from rubikscubennnsolver import wing_str_map
from rubikscubennnsolver.RubiksCube444 import (
    RubiksCube444,
    centers_444,
    moves_444,
    solved_444,
    wings_for_edges_recolor_pattern_444,
)
from rubikscubennnsolver.RubiksCube444Misc import high_edges_444, low_edges_444

log = logging.getLogger(__name__)


def _edge_pairing_square_groups():
    """Order low slots so the solved all-edge matching is permutation zero."""
    solved_state = RubiksCube444(solved_444, "URFDLB").state
    high_squares = tuple(square for _, square, _ in sorted(high_edges_444))
    low_candidates = tuple(square for _, square, _ in sorted(low_edges_444))
    partner_by_square = {square: partner for _, square, partner in wings_for_edges_recolor_pattern_444}

    def edge_at(square):
        return wing_str_map[solved_state[square] + solved_state[partner_by_square[square]]]

    low_by_edge = {edge_at(square): square for square in low_candidates}
    low_squares = tuple(low_by_edge[edge_at(square)] for square in high_squares)
    partners = tuple(partner_by_square[square] for square in high_squares + low_squares)
    return high_squares, low_squares, partners


EDGE_PAIRING_HIGH_SQUARES_444, EDGE_PAIRING_LOW_SQUARES_444, EDGE_PAIRING_PARTNERS_444 = _edge_pairing_square_groups()
WING_BINARY_SQUARES_444 = tuple(square for _, square, _ in wings_for_edges_recolor_pattern_444)
WING_BINARY_PARTNERS_444 = tuple(partner for _, _, partner in wings_for_edges_recolor_pattern_444)
PHASE12_HIGHLOW_TARGET_444 = "UDDUUDDUDUDUUDUDDUUDDUUDDUDUUDUDDUUDDUUDUDDUUDDU"
PHASE2_CENTER_TARGETS_444 = (
    "UUUULLLLxxxxRRRRxxxxUUUU",
    "UUUULLRRxxxxLLRRxxxxUUUU",
    "UUUULLRRxxxxRRLLxxxxUUUU",
    "UUUULRLRxxxxLRLRxxxxUUUU",
    "UUUULRLRxxxxRLRLxxxxUUUU",
    "UUUULRRLxxxxRLLRxxxxUUUU",
    "UUUURLLRxxxxLRRLxxxxUUUU",
    "UUUURLRLxxxxLRLRxxxxUUUU",
    "UUUURLRLxxxxRLRLxxxxUUUU",
    "UUUURRLLxxxxLLRRxxxxUUUU",
    "UUUURRLLxxxxRRLLxxxxUUUU",
    "UUUURRRRxxxxLLLLxxxxUUUU",
)


def _ranked_all_axis_center_starting_state():
    cube = RubiksCube444(solved_444, "URFDLB")
    state = ["."] * len(cube.state)
    axis_by_color = {
        "U": "U",
        "D": "U",
        "L": "L",
        "R": "L",
        "F": "F",
        "B": "F",
    }
    for square in centers_444:
        state[square] = axis_by_color[cube.state[square]]
    return (("".join(state[1:]), "ULFRBD"),)


def _ranked_lr_center_starting_states():
    states = []
    for target in PHASE2_CENTER_TARGETS_444:
        state = ["."] * 97
        for square, value in zip(centers_444, target):
            state[square] = value if value in ("L", "R") else "x"
        states.append(("".join(state[1:]), "ULFRBD"))
    return tuple(states)


def _highlow_target_starting_state():
    """
    Only the canonical high/low split.

    The other 2,047 even edge mappings are equally valid goals, but they cannot
    be seeded here: this table is ranked by which *slots* hold high wings, and
    an edge mapping flips wings by *piece*. Which slots pair up as one edge
    depends on the wing permutation, so the goal set is not fixed in this
    coordinate. The solver applies the mappings at its root instead.
    """
    cube = RubiksCube444(solved_444, "URFDLB")
    state = ["."] * len(cube.state)
    for (square, _), target in zip(cube.reduce333_orient_edges_tuples, PHASE12_HIGHLOW_TARGET_444):
        state[square] = target
    return (("".join(state[1:]), "ULFRBD"),)


def _highlow_move_flip_masks():
    masks = []
    scramble = ("Uw", "L", "F2", "Rw'", "B", "D2", "Fw", "U'", "Lw2")
    for move in moves_444:
        actual = RubiksCube444(solved_444, "URFDLB")
        for step in scramble:
            actual.rotate(step)
        pattern = ["."] * len(actual.state)
        highlow_by_square = dict(
            zip(
                (square for square, _ in actual.reduce333_orient_edges_tuples),
                actual.highlow_edges_state(None),
            )
        )
        for square, value in highlow_by_square.items():
            pattern[square] = value
        pattern_cube = RubiksCube444(solved_444, "URFDLB")
        pattern_cube.state = pattern
        actual.rotate(move)
        pattern_cube.rotate(move)
        expected = dict(
            zip(
                (square for square, _ in actual.reduce333_orient_edges_tuples),
                actual.highlow_edges_state(None),
            )
        )
        mask = 0
        for index, (square, partner) in enumerate(zip(WING_BINARY_SQUARES_444, WING_BINARY_PARTNERS_444)):
            square_differs = pattern_cube.state[square] != expected[square]
            if square_differs:
                mask |= 1 << index
        masks.append(mask)
    return tuple(masks)


def _highlow_partner_flip_mask():
    cube = RubiksCube444(solved_444, "URFDLB")
    highlow_by_square = dict(
        zip(
            (square for square, _ in cube.reduce333_orient_edges_tuples),
            cube.highlow_edges_state(None),
        )
    )
    mask = 0
    for index, (square, partner) in enumerate(zip(WING_BINARY_SQUARES_444, WING_BINARY_PARTNERS_444)):
        if highlow_by_square[square] != highlow_by_square[partner]:
            mask |= 1 << index
    return mask


# fmt: off
PHASE34_ILLEGAL_MOVES = (
    "Uw", "Uw'",
    "Lw", "Lw'",
    "Fw", "Fw'",
    "Rw", "Rw'",
    "Bw", "Bw'",
    "Dw", "Dw'",
    "L", "L'",
    "R", "R'",
)

# fmt: on


# ==================================================
# phase 1
# stage LR centers
# ==================================================
class Build444AllCentersStageSymmetryRanked(BFS):
    """Exact 8/8/8 axis-center staging, quotiented by all 48 cube symmetries."""

    def __init__(self):
        BFS.__init__(
            self,
            "4x4x4-all-centers-stage-symmetry-ranked",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step12-all-centers-stage-symmetry.txt",
            False,
            _ranked_all_axis_center_starting_state(),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_type="center-symmetry-444",
        )


class Build444LRCentersStageRanked(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "4x4x4-LR-centers-stage-ranked",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step14-LR-centers-stage.txt",
            False,
            _ranked_lr_center_starting_states(),
            use_c=True,
            use_ranked_cost=True,
        )


# ==================================================
# phase 2
# stage the remaining centers and EO the wings
# ==================================================
class Build444HighLowEdgesEdgesAllMoves(BFS):
    """High/low edges with the full 4x4x4 move set for combined phase 1+2."""

    def __init__(self):
        BFS.__init__(
            self,
            "444-highlow-edges-edges-all-moves",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step23-highlow-edges-edges.txt",
            False,  # store_as_hex
            _highlow_target_starting_state(),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_type="wing-binary",
            ranked_cost_square_groups=(WING_BINARY_SQUARES_444,),
            edge_pairing_partners=WING_BINARY_PARTNERS_444,
            ranked_cost_move_flip_masks=_highlow_move_flip_masks(),
            ranked_cost_partner_flip_mask=_highlow_partner_flip_mask(),
        )


# phase 3+4
# all centers (58,800 states); all 12 edges paired
# ==================================================


class Build444Reduce333Centers(BFS):
    """
    lookup-table-4x4x4-step31-all-centers.txt
    =========================================
    0 steps has      1 entries ( 0 percent, 0.00x previous step)
    1 steps has      6 entries ( 0 percent, 6.00x previous step)
    2 steps has     83 entries ( 0 percent, 13.83x previous step)
    3 steps has    724 entries ( 1 percent, 8.72x previous step)
    4 steps has  3,851 entries ( 6 percent, 5.32x previous step)
    5 steps has 10,426 entries (17 percent, 2.71x previous step)
    6 steps has 16,693 entries (28 percent, 1.60x previous step)
    7 steps has 16,616 entries (28 percent, 1.00x previous step)
    8 steps has  8,928 entries (15 percent, 0.54x previous step)
    9 steps has  1,472 entries ( 2 percent, 0.16x previous step)

    Total: 58,800 entries
    Average: 6.31 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "444-all-centers",
            PHASE34_ILLEGAL_MOVES,
            "4x4x4",
            "lookup-table-4x4x4-step31-all-centers.txt",
            False,  # store_as_hex
            (
                (
                    """
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . B B .
 . L L .  . F F .  . R R .  . B B .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . D D .
          . D D .
          . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build444PairAllEdges(BFS):
    """
    Pair all 12 edges under the phase-3 move set.

    The coordinate is the even matching between 12 high-wing slots and 12
    low-wing slots. Named edge identities are quotiented out, giving 12! / 2
    = 239,500,800 dense states.
    """

    def __init__(self):
        BFS.__init__(
            self,
            "444-pair-all-edges",
            PHASE34_ILLEGAL_MOVES,
            "4x4x4",
            "lookup-table-4x4x4-step33-all-edges-paired.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . U U .
          U . . U
          U . . U
          . U U .

 . L L .  . F F .  . R R .  . B B .
 L . . L  F . . F  R . . R  B . . B
 L . . L  F . . F  R . . R  B . . B
 . L L .  . F F .  . R R .  . B B .

          . D D .
          D . . D
          D . . D
          . D D .""",
                    "ascii",
                ),
            ),
            use_c=True,
            use_ranked_cost=True,
            ranked_cost_type="edge-pairing-even",
            ranked_cost_square_groups=(
                EDGE_PAIRING_HIGH_SQUARES_444,
                EDGE_PAIRING_LOW_SQUARES_444,
            ),
            edge_pairing_partners=EDGE_PAIRING_PARTNERS_444,
        )

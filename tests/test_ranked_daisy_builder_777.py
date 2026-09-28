# third party libraries
import pytest

# rubiks cube libraries
from rubikscubelookuptables.builder777 import (
    DAISY_CENTER_ORBITS_777,
    DAISY_CENTERS_ILLEGAL_MOVES_777,
    Build777DaisyLRInnerCenters,
)

ORBIT_NAMES = ("left-oblique", "middle-oblique", "right-oblique", "inner-t", "inner-x")
AXES = ("UD", "LR", "FB")


def test_daisy_defines_exactly_five_disjoint_eight_sticker_orbits_per_axis():
    assert set(DAISY_CENTER_ORBITS_777) == {"UD", "LR", "FB"}

    all_groups = []
    for axis, orbits in DAISY_CENTER_ORBITS_777.items():
        assert tuple(name for name, _ in orbits) == ORBIT_NAMES
        assert all(len(squares) == len(set(squares)) == 8 for _, squares in orbits)
        assert len(set().union(*(set(squares) for _, squares in orbits))) == 40
        all_groups.extend((axis, name, squares) for name, squares in orbits)

    assert len(all_groups) == 15
    assert len(set().union(*(set(squares) for _, _, squares in all_groups))) == 120


@pytest.mark.parametrize("axis", AXES)
def test_daisy_rank_groups_are_closed_physical_center_orbits(axis):
    builder = Build777DaisyLRInnerCenters()

    assert all(builder._squares_are_closed_orbit(list(squares)) for _, squares in DAISY_CENTER_ORBITS_777[axis])


def test_lr_inner_builder_is_a_native_70_squared_table():
    builder = Build777DaisyLRInnerCenters()
    outer_moves = {f"{face}{suffix}" for face in "ULFRBD" for suffix in ("", "'", "2")}
    wide_half_turns = {f"{width}{face}w2" for width in ("", "3") for face in "ULFRBD"}

    assert builder.use_ranked_cost
    assert builder.rank_universes == (70, 70)
    assert builder.rank_universe == 70**2 == 4900
    assert len(builder.starting_cubes) == 1
    assert builder.filename.endswith("lookup-table-7x7x7-daisy-lr-inner-centers.txt")
    assert builder.illegal_moves == DAISY_CENTERS_ILLEGAL_MOVES_777
    assert set(builder.legal_moves) == outer_moves | wide_half_turns
    assert not any("w" in move and not move.endswith("2") for move in builder.legal_moves)

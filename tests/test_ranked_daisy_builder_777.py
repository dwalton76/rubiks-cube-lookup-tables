# third party libraries
import pytest

# rubiks cube libraries
from rubikscubelookuptables.builder777 import (
    DAISY_CENTER_ORBITS_777,
    DAISY_CENTERS_ILLEGAL_MOVES_777,
    PHASE8_CENTER_ILLEGAL_MOVES_777,
    PHASE8_PAIRED_ILLEGAL_MOVES_777,
    PHASE9_CENTER_ILLEGAL_MOVES_777,
    Build777DaisyLRInnerCenters,
    Build777Phase8FBAxisCenters,
    Build777Phase8FBInnerUDObliquesCenters,
    Build777Phase8FBObliquesUDEdgesCenters,
    Build777Phase8FBPairedCenters,
    Build777Phase8InnerInteractionCenters,
    Build777Phase8LRObliqueCenters,
    Build777Phase8MiddleInteractionCenters,
    Build777Phase8UDAxisCenters,
    Build777Phase8UDInnerFBObliquesCenters,
    Build777Phase8UDObliquesFBEdgesCenters,
    Build777Phase8UDObliquesFBInnerTCenters,
    Build777Phase8UDPairedCenters,
    Build777Phase9FBAxisCenters,
    Build777Phase9FBObliquesUDEdgesCenters,
    Build777Phase9InnerInteractionCenters,
    Build777Phase9LRObliqueCenters,
    Build777Phase9MiddleInteractionCenters,
    Build777Phase9UDAxisCenters,
    Build777Phase9UDObliquesFBEdgesCenters,
    Build777Phase9UDObliquesFBInnerTCenters,
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


PHASE8_BUILDERS = (
    (Build777Phase8UDAxisCenters, (70, 70, 70, 70, 70), 2),
    (Build777Phase8FBAxisCenters, (70, 70, 70, 70, 70), 2),
    (Build777Phase8UDPairedCenters, (70, 70, 70, 70, 70), 70),
    (Build777Phase8FBPairedCenters, (70, 70, 70, 70, 70), 70),
    (Build777Phase8LRObliqueCenters, (70,), 2),
    (Build777Phase8InnerInteractionCenters, (70, 70, 70, 70), 1),
    (Build777Phase8MiddleInteractionCenters, (70, 70, 70, 70), 4),
    (Build777Phase8UDObliquesFBEdgesCenters, (70, 70, 70, 70, 70), 4),
    (Build777Phase8FBObliquesUDEdgesCenters, (70, 70, 70, 70, 70), 4),
    (Build777Phase8UDObliquesFBInnerTCenters, (70, 70, 70, 70, 70), 2),
    (Build777Phase8UDInnerFBObliquesCenters, (70, 70, 70, 70, 70), 70),
    (Build777Phase8FBInnerUDObliquesCenters, (70, 70, 70, 70, 70), 70),
)


@pytest.mark.parametrize("builder_class,universes,goals", PHASE8_BUILDERS)
def test_phase8_builder_coordinate(builder_class, universes, goals):
    builder = builder_class()

    assert builder.use_ranked_cost
    assert builder.rank_universes == universes
    assert len(builder.starting_cubes) == goals
    expected_illegal = (
        PHASE8_PAIRED_ILLEGAL_MOVES_777
        if builder_class
        in (
            Build777Phase8UDPairedCenters,
            Build777Phase8FBPairedCenters,
            Build777Phase8UDInnerFBObliquesCenters,
            Build777Phase8FBInnerUDObliquesCenters,
        )
        else PHASE8_CENTER_ILLEGAL_MOVES_777
    )
    assert set(builder.illegal_moves) == set(expected_illegal)
    assert "3Lw2" in builder.legal_moves
    assert "3Rw2" in builder.legal_moves
    assert "3Uw2" not in builder.legal_moves
    ranks = [builder._ranked_state_rank(builder._state_for_workq(cube)) for cube in builder.starting_cubes]
    assert len(set(ranks)) == goals
    cube = builder.starting_cubes[0]
    original = cube.state[:]
    try:
        for move in builder.legal_moves:
            cube.state = original[:]
            cube.rotate(move)
            builder._ranked_state_rank(builder._state_for_workq(cube))
    finally:
        cube.state = original


PHASE9_BUILDERS = (
    (Build777Phase9UDAxisCenters, (70, 70, 70, 70, 70), 2),
    (Build777Phase9FBAxisCenters, (70, 70, 70, 70, 70), 2),
    (Build777Phase9LRObliqueCenters, (70,), 2),
    (Build777Phase9InnerInteractionCenters, (70, 70, 70, 70), 1),
    (Build777Phase9MiddleInteractionCenters, (70, 70, 70, 70), 4),
    (Build777Phase9UDObliquesFBEdgesCenters, (70, 70, 70, 70, 70), 4),
    (Build777Phase9FBObliquesUDEdgesCenters, (70, 70, 70, 70, 70), 4),
    (Build777Phase9UDObliquesFBInnerTCenters, (70, 70, 70, 70, 70), 2),
)


@pytest.mark.parametrize("builder_class,universes,goals", PHASE9_BUILDERS)
def test_phase9_builder_coordinate(builder_class, universes, goals):
    builder = builder_class()

    assert builder.use_ranked_cost
    assert builder.rank_universes == universes
    assert len(builder.starting_cubes) == goals
    assert set(builder.illegal_moves) == set(PHASE9_CENTER_ILLEGAL_MOVES_777)
    assert "3Lw2" not in builder.legal_moves
    assert "3Rw2" not in builder.legal_moves
    assert "Lw2" in builder.legal_moves
    assert "Rw2" in builder.legal_moves
    assert "phase9" in builder.filename
    ranks = [builder._ranked_state_rank(builder._state_for_workq(cube)) for cube in builder.starting_cubes]
    assert len(set(ranks)) == goals

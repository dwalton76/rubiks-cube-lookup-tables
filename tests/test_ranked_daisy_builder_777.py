# standard libraries
import json

# third party libraries
import pytest

# rubiks cube libraries
from rubikscubelookuptables.builder777 import (
    DAISY_AXIS_COLORS_777,
    DAISY_CENTER_ORBITS_777,
    DAISY_CENTERS_ILLEGAL_MOVES_777,
    DAISY_OBLIQUE_ORBITS_777,
    Build777DaisyPerfectCenters,
    Build777SolvePerfectCenters,
    _Build777DaisyCenters,
)

ORBIT_NAMES = ("left-oblique", "middle-oblique", "right-oblique", "inner-t", "inner-x")
AXES = ("UD", "LR", "FB")


def full_orbit_builder(axis):
    """
    The five-orbit builder for one axis.

    Only UD is built and shipped, since the searcher rotates LR and FB onto the
    UD coordinate, but the goal and orbit geometry of all three axes is still
    worth asserting.
    """
    return type(f"_Full{axis}", (_Build777DaisyCenters,), {"axis": axis, "table_slug": f"{axis}-perfect"})()


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
    builder = full_orbit_builder(axis)

    assert all(builder._squares_are_closed_orbit(list(squares)) for _, squares in DAISY_CENTER_ORBITS_777[axis])


def test_daisy_move_set_preserves_staging():
    builder = Build777DaisyPerfectCenters()
    outer_moves = {f"{face}{suffix}" for face in "ULFRBD" for suffix in ("", "'", "2")}
    wide_half_turns = {f"{width}{face}w2" for width in ("", "3") for face in "ULFRBD"}

    assert set(builder.legal_moves) == outer_moves | wide_half_turns
    assert builder.illegal_moves == DAISY_CENTERS_ILLEGAL_MOVES_777
    assert not any("w" in move and not move.endswith("2") for move in builder.legal_moves)


@pytest.mark.parametrize(
    "prefix,builder_class", (("daisy", Build777DaisyPerfectCenters), ("solve", Build777SolvePerfectCenters))
)
def test_optional_perfect_builders_are_dense_70_to_the_five(prefix, builder_class):
    builder = builder_class()

    assert builder.rank_universes == (70, 70, 70, 70, 70)
    assert builder.rank_universe == 70**5 == 1_680_700_000
    assert builder.selected_orbits == DAISY_CENTER_ORBITS_777["UD"]
    assert builder.table_slug == "perfect"
    assert builder.filename.endswith(f"lookup-table-7x7x7-{prefix}-perfect-centers.txt")


@pytest.mark.parametrize("builder_class", (Build777DaisyPerfectCenters, Build777SolvePerfectCenters))
def test_perfect_builders_publish_one_compacted_table_for_all_three_axes(builder_class):
    builder = builder_class()

    # 70^5 raw ranks fall into 105,356,972 orbits of the 16 axis-preserving
    # symmetries, so the published table is a 27th the size of the BFS scratch.
    assert builder.compact_center_symmetry_777
    assert "UD" not in builder.ranked_cost_filename
    assert builder.ranked_symmetry_index_filename == f"{builder.ranked_cost_filename}.symmetry-index.bin"


@pytest.mark.parametrize("axis", AXES)
def test_daisy_goals_have_two_coordinated_orientations(axis):
    builder = full_orbit_builder(axis)
    primary, opposite = DAISY_AXIS_COLORS_777[axis]

    assert builder.goal_orientations == ("native", "obliques-swapped")
    assert len(builder.starting_cubes) == 2

    for orientation, cube in enumerate(builder.starting_cubes):
        for orbit_name, squares in DAISY_CENTER_ORBITS_777[axis]:
            swapped = orientation == 1 and orbit_name in DAISY_OBLIQUE_ORBITS_777
            first_color, second_color = (opposite, primary) if swapped else (primary, opposite)
            assert {cube.state[square] for square in squares[:4]} == {first_color}
            assert {cube.state[square] for square in squares[4:]} == {second_color}

    ranks = [builder._ranked_state_rank(builder._state_for_workq(cube)) for cube in builder.starting_cubes]
    assert len(set(ranks)) == 2
    for cube, rank in zip(builder.starting_cubes, ranks):
        assert builder._ranked_state_unrank(rank) == builder._state_for_workq(cube)


def test_solve_builder_matches_the_perfect_daisy_shape_with_only_the_native_goal():
    axis = "UD"
    builder = Build777SolvePerfectCenters()
    daisy = Build777DaisyPerfectCenters()
    primary, opposite = DAISY_AXIS_COLORS_777[axis]

    assert builder.goal_orientations == ("native",)
    assert len(builder.starting_cubes) == 1
    assert builder.selected_orbits == DAISY_CENTER_ORBITS_777[axis]
    assert builder.illegal_moves == DAISY_CENTERS_ILLEGAL_MOVES_777
    assert set(builder.legal_moves) == set(daisy.legal_moves)

    for orbit_name, squares in DAISY_CENTER_ORBITS_777[axis]:
        assert {builder.starting_cubes[0].state[square] for square in squares[:4]} == {primary}
        assert {builder.starting_cubes[0].state[square] for square in squares[4:]} == {opposite}

    # The native goal is shared with the daisy; only the swapped goal is dropped.
    native = daisy._state_for_workq(daisy.starting_cubes[0])
    assert builder._state_for_workq(builder.starting_cubes[0]) == native
    assert daisy._state_for_workq(daisy.starting_cubes[1]) != native


def test_daisy_ranked_metadata(tmp_path):
    builder = Build777DaisyPerfectCenters()
    metadata_path = tmp_path / "daisy.cost-only.bin.json"
    builder.ranked_metadata_filename = str(metadata_path)
    builder.stats = {0: 2}

    builder._write_ranked_metadata()

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["format"] == "dense-multiset-cost-v1"
    assert metadata["cost_encoding"] == {"0": "unseen", "nonzero": "depth + 1"}
    assert metadata["rank_order"] == "left-to-right mixed radix"
    assert metadata["universe_size"] == 70**5
    assert len(metadata["rank_groups"]) == 5
    assert all(group["counts"] == [4, 4] and group["universe_size"] == 70 for group in metadata["rank_groups"])
    assert metadata["completed_depth"] == 0
    assert metadata["states_per_depth"] == {"0": 2}

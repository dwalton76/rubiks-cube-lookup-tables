# third party libraries
import pytest

# rubiks cube libraries
from rubikscubelookuptables.builder666 import (
    DAISY_AXES_666,
    DAISY_CENTER_ORBITS_666,
    DAISY_CENTERS_ILLEGAL_MOVES_666,
    DAISY_ORBIT_NAMES_666,
    _Build666DaisyInnerXSpineCenters,
    daisy_inner_x_spine_table_specs_666,
)


def _builder_class(class_name):
    module = __import__("rubikscubelookuptables.builder666", fromlist=[class_name])
    return getattr(module, class_name)


def test_daisy_defines_exactly_nine_disjoint_eight_sticker_orbits():
    assert set(DAISY_CENTER_ORBITS_666) == set(DAISY_AXES_666)
    all_squares = []
    for axis, orbits in DAISY_CENTER_ORBITS_666.items():
        assert tuple(name for name, _ in orbits) == DAISY_ORBIT_NAMES_666
        assert all(len(squares) == len(set(squares)) == 8 for _, squares in orbits)
        assert len(set().union(*(set(squares) for _, squares in orbits))) == 24
        all_squares.extend(squares for _, squares in orbits)
    assert len(all_squares) == 9
    assert len(set().union(*(set(squares) for squares in all_squares))) == 72


def test_there_are_three_inner_x_spine_tables():
    specs = daisy_inner_x_spine_table_specs_666()
    assert tuple(axis for axis, _, _ in specs) == DAISY_AXES_666
    assert len({class_name for _, _, class_name in specs}) == 3


@pytest.mark.parametrize("axis,slug,class_name", daisy_inner_x_spine_table_specs_666())
def test_inner_x_spine_builders_are_dense_70_to_the_five(axis, slug, class_name):
    builder_class = _builder_class(class_name)
    builder = builder_class()
    inner_x = tuple(
        orbit
        for candidate_axis in DAISY_AXES_666
        for orbit in DAISY_CENTER_ORBITS_666[candidate_axis]
        if orbit[0] == "inner-x"
    )
    axis_obliques = tuple(orbit for orbit in DAISY_CENTER_ORBITS_666[axis] if orbit[0] != "inner-x")

    assert issubclass(builder_class, _Build666DaisyInnerXSpineCenters)
    assert builder.use_ranked_cost
    assert builder.rank_universes == (70, 70, 70, 70, 70)
    assert builder.rank_universe == 70**5 == 1_680_700_000
    assert builder.selected_orbits == inner_x + axis_obliques
    assert builder.table_slug == slug
    assert builder.filename.endswith(f"lookup-table-6x6x6-daisy-{slug}-centers.txt")
    assert builder.illegal_moves == DAISY_CENTERS_ILLEGAL_MOVES_666
    assert len(builder.starting_cubes) == 2

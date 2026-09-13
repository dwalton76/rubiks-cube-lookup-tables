# third party libraries
import pytest

# rubiks cube libraries
from rubikscubelookuptables.builder666 import (
    DAISY_AXES_666,
    DAISY_CENTER_ORBITS_666,
    DAISY_CENTERS_ILLEGAL_MOVES_666,
    DAISY_ORBIT_NAMES_666,
    _Build666DaisyCenters,
    daisy_plus_table_specs_666,
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


def test_there_are_eighteen_axis_plus_foreign_orbit_tables():
    specs = daisy_plus_table_specs_666()
    assert len(specs) == 18
    assert len({spec[-1] for spec in specs}) == 18


@pytest.mark.parametrize("axis,extra_axis,extra_orbit,slug,class_name", daisy_plus_table_specs_666())
def test_plus_builders_are_dense_70_to_the_four(axis, extra_axis, extra_orbit, slug, class_name):
    builder = _builder_class(class_name)()
    expected_orbits = DAISY_CENTER_ORBITS_666[axis] + tuple(
        orbit for orbit in DAISY_CENTER_ORBITS_666[extra_axis] if orbit[0] == extra_orbit
    )

    assert issubclass(_builder_class(class_name), _Build666DaisyCenters)
    assert builder.use_ranked_cost
    assert builder.rank_universes == (70, 70, 70, 70)
    assert builder.rank_universe == 70**4 == 24_010_000
    assert builder.selected_orbits == expected_orbits
    assert builder.table_slug == slug
    assert builder.filename.endswith(f"lookup-table-6x6x6-daisy-{slug}-centers.txt")
    assert builder.illegal_moves == DAISY_CENTERS_ILLEGAL_MOVES_666
    assert len(builder.starting_cubes) == 4

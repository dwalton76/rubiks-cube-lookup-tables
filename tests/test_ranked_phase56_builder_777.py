# standard libraries
import json
from collections import Counter

# third party libraries
import pytest

# rubiks cube libraries
from rubikscubelookuptables.builder777 import (
    PHASE5_ILLEGAL_MOVES,
    UFBD_LEFT_OBLIQUE_EDGES_777,
    UFBD_MIDDLE_OBLIQUE_EDGES_777,
    UFBD_OUTER_X_CENTERS_777,
    UFBD_RIGHT_OBLIQUE_EDGES_777,
    Build777Phase56UDLeftMiddleObliqueCentersStage,
    Build777Phase56UDLeftObliqueOuterXCentersStage,
    Build777Phase56UDLeftRightObliqueCentersStage,
    Build777Phase56UDMiddleObliqueOuterXCentersStage,
    Build777Phase56UDMiddleRightObliqueCentersStage,
    Build777Phase56UDRightObliqueOuterXCentersStage,
)

PAIRINGS = (
    (
        Build777Phase56UDLeftRightObliqueCentersStage,
        UFBD_LEFT_OBLIQUE_EDGES_777,
        UFBD_RIGHT_OBLIQUE_EDGES_777,
        "left-right-oblique",
    ),
    (
        Build777Phase56UDLeftMiddleObliqueCentersStage,
        UFBD_LEFT_OBLIQUE_EDGES_777,
        UFBD_MIDDLE_OBLIQUE_EDGES_777,
        "left-middle-oblique",
    ),
    (
        Build777Phase56UDLeftObliqueOuterXCentersStage,
        UFBD_LEFT_OBLIQUE_EDGES_777,
        UFBD_OUTER_X_CENTERS_777,
        "left-oblique-outer-x",
    ),
    (
        Build777Phase56UDMiddleRightObliqueCentersStage,
        UFBD_MIDDLE_OBLIQUE_EDGES_777,
        UFBD_RIGHT_OBLIQUE_EDGES_777,
        "middle-right-oblique",
    ),
    (
        Build777Phase56UDRightObliqueOuterXCentersStage,
        UFBD_RIGHT_OBLIQUE_EDGES_777,
        UFBD_OUTER_X_CENTERS_777,
        "right-oblique-outer-x",
    ),
    (
        Build777Phase56UDMiddleObliqueOuterXCentersStage,
        UFBD_MIDDLE_OBLIQUE_EDGES_777,
        UFBD_OUTER_X_CENTERS_777,
        "middle-oblique-outer-x",
    ),
)


@pytest.mark.parametrize("builder_class,first_group,second_group,slug", PAIRINGS)
def test_phase56_builder_uses_two_12870_rank_groups(builder_class, first_group, second_group, slug):
    builder = builder_class()

    assert builder.use_ranked_cost
    assert builder.rank_universe == 12870 * 12870
    assert tuple(builder.rank_groups[0]["squares"]) == first_group
    assert tuple(builder.rank_groups[1]["squares"]) == second_group
    assert builder.rank_groups[0]["universe_size"] == 12870
    assert builder.rank_groups[1]["universe_size"] == 12870
    assert builder.illegal_moves == PHASE5_ILLEGAL_MOVES
    assert builder.name == f"7x7x7-phase5-6-UD-{slug}-centers-stage"
    assert builder.filename.endswith(f"lookup-table-7x7x7-phase5-6-UD-{slug}-centers-stage.txt")

    state = builder._state_for_workq(builder.starting_cubes[0])
    assert Counter(state[:16]) == Counter({"U": 8, "x": 8})
    assert Counter(state[16:]) == Counter({"U": 8, "x": 8})


def test_phase56_coordinates_are_distinct_closed_16_sticker_orbits():
    groups = (
        UFBD_LEFT_OBLIQUE_EDGES_777,
        UFBD_MIDDLE_OBLIQUE_EDGES_777,
        UFBD_RIGHT_OBLIQUE_EDGES_777,
        UFBD_OUTER_X_CENTERS_777,
    )
    builder = Build777Phase56UDLeftRightObliqueCentersStage()

    assert all(len(group) == 16 and len(set(group)) == 16 for group in groups)
    assert all(sum(square <= 49 or square >= 246 for square in group) == 8 for group in groups)
    assert all(set(first).isdisjoint(second) for index, first in enumerate(groups) for second in groups[index + 1 :])
    assert all(builder._squares_are_closed_orbit(list(group)) for group in groups)


def test_phase56_builders_share_exactly_one_legal_move_set():
    builders = [builder_class() for builder_class, _, _, _ in PAIRINGS]

    assert all(builder.illegal_moves == PHASE5_ILLEGAL_MOVES for builder in builders)
    assert all(builder.legal_moves == builders[0].legal_moves for builder in builders[1:])


def test_phase56_ranked_metadata_describes_both_coordinates(tmp_path):
    builder = Build777Phase56UDLeftRightObliqueCentersStage()
    metadata_path = tmp_path / "left-right.cost-only.bin.json"
    builder.ranked_metadata_filename = str(metadata_path)
    builder.stats = {0: 1, 1: 2}

    builder._write_ranked_metadata()

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["format"] == "dense-multiset-cost-v1"
    assert metadata["universe_size"] == 12870 * 12870
    assert [group["universe_size"] for group in metadata["rank_groups"]] == [12870, 12870]
    assert metadata["completed_depth"] == 1
    assert metadata["states_per_depth"] == {"0": 1, "1": 2}

import pytest

from rubikscubelookuptables.builder666 import (
    UFBD_LEFT_OBLIQUE_EDGES_666,
    UFBD_OUTER_X_CENTERS_666,
    UFBD_RIGHT_OBLIQUE_EDGES_666,
    Build666Phase3UDLeftObliqueOuterXCentersStage,
    Build666Phase3UDLeftRightObliqueCentersStage,
    Build666Phase3UDRightObliqueOuterXCentersStage,
)


PAIRINGS = (
    (
        Build666Phase3UDLeftRightObliqueCentersStage,
        UFBD_LEFT_OBLIQUE_EDGES_666,
        UFBD_RIGHT_OBLIQUE_EDGES_666,
    ),
    (
        Build666Phase3UDLeftObliqueOuterXCentersStage,
        UFBD_LEFT_OBLIQUE_EDGES_666,
        UFBD_OUTER_X_CENTERS_666,
    ),
    (
        Build666Phase3UDRightObliqueOuterXCentersStage,
        UFBD_RIGHT_OBLIQUE_EDGES_666,
        UFBD_OUTER_X_CENTERS_666,
    ),
)


@pytest.mark.parametrize("builder_class,first_group,second_group", PAIRINGS)
def test_phase3_builder_uses_two_12870_rank_groups(builder_class, first_group, second_group):
    builder = builder_class()

    assert builder.use_ranked_cost
    assert builder.rank_universe == 12870 * 12870
    assert tuple(builder.rank_groups[0]["squares"]) == first_group
    assert tuple(builder.rank_groups[1]["squares"]) == second_group
    assert builder.rank_groups[0]["universe_size"] == 12870
    assert builder.rank_groups[1]["universe_size"] == 12870

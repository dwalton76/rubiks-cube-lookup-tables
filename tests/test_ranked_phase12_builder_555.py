# standard libraries
import sys
from types import ModuleType

# rubiks cube libraries
from rubikscubelookuptables.builder555 import (
    Build555EdgeOrientInnerOrbit,
    Build555EdgeOrientOuterOrbit,
    Build555FBTCenterStage,
    Build555FBXCenterStage,
    Build555LRCenterStageTCenter,
    Build555LRCenterStageXCenter,
    Build555Phase3LRCenterStage,
    Build555Phase4,
    Build555Phase5Centers,
    Build555Phase5FBCentersHighEdgeMidge,
    Build555Phase5FBCentersLowEdgeMidge,
)
from rubikscubennnsolver.RubiksCube555 import (
    PHASE3_INNER_MIDGE_SQUARES_555,
    PHASE3_OUTER_WING_SQUARES_555,
    PHASE4_HIGH_EDGE_PARTNERS_555,
    PHASE4_HIGH_EDGE_SQUARES_555,
    PHASE4_LOW_EDGE_PARTNERS_555,
    PHASE4_LOW_EDGE_SQUARES_555,
    PHASE4_MIDGE_PARTNERS_555,
    PHASE4_MIDGE_SQUARES_555,
    PHASE5_XY_HIGH_SQUARES_555,
    PHASE5_XY_LOW_SQUARES_555,
    PHASE5_XY_MIDGE_SQUARES_555,
    FB_t_centers_555,
    FB_x_centers_555,
    LR_t_centers_555,
    LR_x_centers_555,
    UFBD_t_centers_555,
    UFBD_x_centers_555,
    t_centers_without_middles_555,
    x_centers_without_middles_555,
)


def test_phase1_builders_use_ranked_combination_costs():
    for builder_class, squares in (
        (Build555LRCenterStageTCenter, t_centers_without_middles_555),
        (Build555LRCenterStageXCenter, x_centers_without_middles_555),
    ):
        builder = builder_class()

        assert builder.use_ranked_cost
        assert builder.rank_universe == 735471
        assert builder.rank_symbols == "Lx"
        assert builder.rank_counts == (8, 16)
        assert tuple(builder.rank_groups[0]["squares"]) == squares


def test_phase2_builders_use_ranked_combination_costs():
    for builder_class, squares in (
        (Build555FBTCenterStage, UFBD_t_centers_555),
        (Build555FBXCenterStage, UFBD_x_centers_555),
    ):
        builder = builder_class()

        assert builder.use_ranked_cost
        assert builder.rank_universe == 12870
        assert builder.rank_symbols == "Fx"
        assert builder.rank_counts == (8, 8)
        assert tuple(builder.rank_groups[0]["squares"]) == squares


def test_phase3_builders_use_ranked_costs():
    lr = Build555Phase3LRCenterStage()
    outer = Build555EdgeOrientOuterOrbit()
    inner = Build555EdgeOrientInnerOrbit()

    assert lr.use_ranked_cost
    assert lr.rank_universe == 4900
    assert lr.rank_universes == (70, 70)
    assert tuple(lr.rank_groups[0]["squares"]) == LR_t_centers_555
    assert tuple(lr.rank_groups[1]["squares"]) == LR_x_centers_555
    assert len(lr.starting_cubes) == 432

    assert outer.use_ranked_cost
    assert outer.ranked_cost_type == "wing-binary"
    assert outer.rank_universe == 2704156
    assert tuple(outer.rank_groups[0]["squares"]) == PHASE3_OUTER_WING_SQUARES_555

    assert inner.use_ranked_cost
    assert inner.ranked_cost_type == "orientation-bits"
    assert inner.rank_universe == 4096
    assert tuple(inner.compact_squares) == PHASE3_INNER_MIDGE_SQUARES_555


def test_phase4_builder_uses_three_paired_combination_ranks(monkeypatch):
    state = ["."] * 151
    for squares in (
        PHASE4_HIGH_EDGE_SQUARES_555,
        PHASE4_MIDGE_SQUARES_555,
        PHASE4_LOW_EDGE_SQUARES_555,
    ):
        for index, square in enumerate(squares):
            state[square] = "L" if index < 4 else "x"
    for squares, partners in (
        (PHASE4_HIGH_EDGE_SQUARES_555, PHASE4_HIGH_EDGE_PARTNERS_555),
        (PHASE4_MIDGE_SQUARES_555, PHASE4_MIDGE_PARTNERS_555),
        (PHASE4_LOW_EDGE_SQUARES_555, PHASE4_LOW_EDGE_PARTNERS_555),
    ):
        for square, partner in zip(squares, partners):
            state[partner] = state[square]
    fake_starts = ModuleType("rubikscubelookuptables.builder555ss")
    fake_starts.starting_states_phase4 = (("".join(state[1:]), "ULFRBD"),)
    monkeypatch.setitem(sys.modules, "rubikscubelookuptables.builder555ss", fake_starts)
    phase4 = Build555Phase4()

    assert phase4.use_ranked_cost
    assert phase4.ranked_cost_type == "paired-multiset"
    assert phase4.rank_universe == 495**3
    assert phase4.rank_universes == (495, 495, 495)
    assert tuple(phase4.rank_groups[0]["squares"]) == PHASE4_HIGH_EDGE_SQUARES_555
    assert tuple(phase4.rank_groups[1]["squares"]) == PHASE4_MIDGE_SQUARES_555
    assert tuple(phase4.rank_groups[2]["squares"]) == PHASE4_LOW_EDGE_SQUARES_555
    assert len(phase4.starting_cubes) == 1


def test_phase5_builders_use_ranked_costs():
    centers = Build555Phase5Centers()
    high = Build555Phase5FBCentersHighEdgeMidge()
    low = Build555Phase5FBCentersLowEdgeMidge()

    assert centers.use_ranked_cost
    assert centers.rank_universe == 70**4
    assert centers.rank_universes == (70, 70, 70, 70)
    assert tuple(centers.rank_groups[0]["squares"]) == LR_t_centers_555
    assert tuple(centers.rank_groups[1]["squares"]) == LR_x_centers_555
    assert tuple(centers.rank_groups[2]["squares"]) == FB_t_centers_555
    assert tuple(centers.rank_groups[3]["squares"]) == FB_x_centers_555
    assert len(centers.starting_cubes) == 36

    for builder, wings in (
        (high, PHASE5_XY_HIGH_SQUARES_555),
        (low, PHASE5_XY_LOW_SQUARES_555),
    ):
        assert builder.use_ranked_cost
        assert builder.rank_universe == 4900 * 1680 * 70
        assert builder.rank_universes == (70, 70, 1680, 70)
        assert tuple(builder.rank_groups[0]["squares"]) == FB_t_centers_555
        assert tuple(builder.rank_groups[1]["squares"]) == FB_x_centers_555
        assert tuple(builder.rank_groups[2]["squares"]) == wings
        assert tuple(builder.rank_groups[3]["squares"]) == PHASE5_XY_MIDGE_SQUARES_555
        assert builder.ranked_cost_type == "phase5-combo-relative"
        assert len(builder.starting_cubes) == 6
        assert len({builder._ranked_state_rank(builder._state_for_workq(cube)) for cube in builder.starting_cubes}) == 6
        assert builder.rank_groups[2]["symbols"] == "ABCDx"
        assert builder.rank_groups[2]["counts"] == (1, 1, 1, 1, 4)
        assert builder.rank_groups[3]["symbols"] == "Lx"
        assert builder.rank_groups[3]["counts"] == (4, 4)

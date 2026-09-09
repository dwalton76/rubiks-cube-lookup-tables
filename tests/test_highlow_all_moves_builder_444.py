# rubiks cube libraries
from rubikscubelookuptables.builder444 import (
    Build444AllCentersStageSymmetryRanked,
    Build444HighLowEdgesEdgesAllMoves,
    Build444LRCentersStageRanked,
)
from rubikscubelookuptables.buildercore import CENTER_SYMMETRIES_444, center_symmetry_rank_444, multiset_unrank


def test_all_move_highlow_builders_use_dense_ranked_costs():
    edges = Build444HighLowEdgesEdgesAllMoves()
    lr = Build444LRCentersStageRanked()
    all_centers = Build444AllCentersStageSymmetryRanked()
    assert edges.illegal_moves == ()
    assert "Uw" in edges.legal_moves
    assert edges.use_ranked_cost
    assert edges.ranked_cost_type == "wing-binary"
    assert edges.rank_universe == 2704156
    assert len(edges.starting_cubes) == 1
    assert lr.use_ranked_cost and lr.rank_universe == 51482970
    assert lr.rank_symbols == "LRx"
    assert lr.rank_counts == (4, 4, 16)
    assert len(lr.starting_cubes) == 12
    assert all_centers.use_ranked_cost
    assert all_centers.ranked_cost_type == "center-symmetry-444"
    assert all_centers.rank_universe == 9465511770
    assert all_centers.rank_symbols == "FLU"
    assert all_centers.rank_counts == (8, 8, 8)
    assert len(all_centers.starting_cubes) == 1


def test_center_symmetry_rank_is_invariant_under_all_48_actions():
    state = multiset_unrank(123456789, "FLU", (8, 8, 8))
    expected = center_symmetry_rank_444(state)
    transformed_states = set()

    for positions, symbol_map in CENTER_SYMMETRIES_444:
        transformed = [""] * 24
        for source, destination in enumerate(positions):
            transformed[destination] = symbol_map[state[source]]
        transformed = "".join(transformed)
        transformed_states.add(transformed)
        assert center_symmetry_rank_444(transformed) == expected

    assert len(CENTER_SYMMETRIES_444) == 48
    assert len(transformed_states) == 48

"""Configuration and rank checks for the dense 5x5x5 phase-6 tables."""

# standard libraries
import json
import struct
import subprocess

# third party libraries
import pytest

# rubiks cube libraries
from rubikscubelookuptables.builder555 import (
    PHASE6_CENTER_SQUARE_GROUPS_555,
    PHASE6_EDGE_PARTNERS_555,
    PHASE6_EDGE_SQUARE_GROUPS_555,
    Build555PairLastEightEdgesEdgesOnly,
    Build555Phase6Centers,
)
from rubikscubelookuptables.buildercore import (
    even_permutation_unrank,
    permutation_unrank,
    three_edge_pairing_rank,
    three_edge_pairing_unrank,
)
from tests.builder_support import CRUNCHER, REPO_ROOT

RANKED_RECORD = struct.Struct("<QB")


def rank_zero_children(builder):
    compact = builder._ranked_state_unrank(0)
    state = ["."] * 151
    state[0] = "x"
    for square, partner, symbol in zip(builder.compact_squares, builder.edge_pairing_partners, compact):
        state[square] = symbol
        state[partner] = symbol
    result = set()
    for move in builder.legal_moves:
        child = builder.rotate_xxx(state[:], move)
        child_compact = "".join(child[square] for square in builder.compact_squares)
        child_rank = builder._ranked_state_rank(child_compact)
        if child_rank:
            result.add(child_rank)
    return result


def test_phase6_edge_builder_uses_shared_parity_coordinate():
    builder = Build555PairLastEightEdgesEdgesOnly()
    solved = builder._state_for_workq(builder.starting_cubes[0])

    assert builder.use_ranked_cost
    assert builder.ranked_dense_frontier
    assert builder.ranked_cost_type == "three-edge-pairing-parity"
    assert builder.rank_universe == 812_851_200 == (40320**2) // 2
    assert tuple(builder.ranked_cost_square_groups) == PHASE6_EDGE_SQUARE_GROUPS_555
    assert builder.edge_pairing_partners == PHASE6_EDGE_PARTNERS_555
    assert solved == "01234567" * 3
    assert builder._ranked_state_rank(solved) == 0
    assert builder._ranked_state_unrank(0) == solved


def test_phase6_edge_groups_and_partner_groups_are_closed_orbits():
    builder = Build555PairLastEightEdgesEdgesOnly()

    for group in PHASE6_EDGE_SQUARE_GROUPS_555:
        assert builder._squares_are_closed_orbit(list(group))
    for offset in range(0, len(PHASE6_EDGE_PARTNERS_555), 8):
        assert builder._squares_are_closed_orbit(list(PHASE6_EDGE_PARTNERS_555[offset : offset + 8]))


def test_phase6_edge_metadata_pins_rank_formula_and_square_order(tmp_path):
    builder = Build555PairLastEightEdgesEdgesOnly()
    metadata_path = tmp_path / "phase6-edges.cost-only.bin.json"
    builder.ranked_metadata_filename = str(metadata_path)
    builder.stats = {0: 1}
    builder._write_ranked_metadata()
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    assert metadata["format"] == "dense-three-edge-pairing-parity-cost-v1"
    assert metadata["rank_order"] == "rank(H) * (n! / 2) + even_rank(inverse(H) composed with L)"
    assert metadata["high_squares"] == list(PHASE6_EDGE_SQUARE_GROUPS_555[0])
    assert metadata["midge_squares"] == list(PHASE6_EDGE_SQUARE_GROUPS_555[1])
    assert metadata["low_squares"] == list(PHASE6_EDGE_SQUARE_GROUPS_555[2])
    assert metadata["partner_squares"] == list(PHASE6_EDGE_PARTNERS_555)
    assert metadata["universe_size"] == 812_851_200
    assert metadata["frontier_mode"] == "dense-cost-scan"


def test_dense_frontier_finish_never_materializes_multi_gigabyte_workq(tmp_path, monkeypatch):
    builder = Build555PairLastEightEdgesEdgesOnly()
    builder.ranked_workq_filename = str(tmp_path / "frontier.bin")
    builder.depth = 13
    builder.index = 0
    builder.stats = {}
    monkeypatch.setattr(builder, "_write_ranked_metadata", lambda: None)

    builder._ranked_finish_depth(262_142_742, build_workq=True)

    assert builder.workq_size == 262_142_742
    assert (tmp_path / "frontier.bin").stat().st_size == 0
    assert builder.stats[13] == 262_142_742


def test_ranked_search_lock_rejects_colliding_builder(tmp_path, monkeypatch):
    first = Build555PairLastEightEdgesEdgesOnly()
    second = Build555PairLastEightEdgesEdgesOnly()
    lock = tmp_path / "phase6.lock"
    monkeypatch.setattr(first, "_ranked_lock_filename", lambda: str(lock))
    monkeypatch.setattr(second, "_ranked_lock_filename", lambda: str(lock))

    first._acquire_ranked_search_lock()
    try:
        with pytest.raises(RuntimeError, match="another ranked build owns"):
            second._acquire_ranked_search_lock()
    finally:
        first._release_ranked_search_lock()


@pytest.mark.parametrize("high_rank", (0, 1, 17, 40319))
@pytest.mark.parametrize("delta_rank", (0, 1, 37, 20159))
def test_three_edge_rank_round_trips_both_permutations(high_rank, delta_rank):
    high = permutation_unrank(high_rank, 8)
    delta = even_permutation_unrank(delta_rank, 8)
    low = tuple(high[index] for index in delta)
    symbols = "01234567"
    state = "".join(symbols[index] for index in high) + symbols + "".join(symbols[index] for index in low)
    expected = (high_rank * 20160) + delta_rank

    assert three_edge_pairing_rank(state) == expected
    assert three_edge_pairing_unrank(expected, 8) == state


def test_three_edge_rank_rejects_different_high_low_parity():
    with pytest.raises(ValueError, match="even permutation"):
        three_edge_pairing_rank("01234567" + "01234567" + "10234567")


def test_phase6_center_builder_uses_exact_grouped_multiset_coordinate(tmp_path):
    builder = Build555Phase6Centers()

    assert builder.use_ranked_cost
    assert builder.rank_universes == (6, 6, 70, 70)
    assert builder.rank_universe == 176_400
    assert tuple(builder.ranked_cost_square_groups) == PHASE6_CENTER_SQUARE_GROUPS_555
    assert len(builder.starting_cubes) == 1
    assert all(builder._squares_are_closed_orbit(list(group)) for group in PHASE6_CENTER_SQUARE_GROUPS_555)

    metadata_path = tmp_path / "phase6-centers.cost-only.bin.json"
    builder.ranked_metadata_filename = str(metadata_path)
    builder.stats = {0: 1}
    builder._write_ranked_metadata()
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["format"] == "dense-multiset-cost-v1"
    assert metadata["universe_size"] == 176_400
    assert [group["universe_size"] for group in metadata["rank_groups"]] == [6, 6, 70, 70]


def test_c_cruncher_expands_three_edge_rank_zero(tmp_path):
    builder = Build555PairLastEightEdgesEdgesOnly()
    cost = tmp_path / "cost.bin"
    with cost.open("wb") as fh:
        fh.truncate(builder.rank_universe)
    with cost.open("r+b") as fh:
        fh.write(b"\1")
    workq = tmp_path / "workq.bin"
    workq.write_bytes(RANKED_RECORD.pack(0, 0))
    output = tmp_path / "next.bin"

    completed = subprocess.run(
        [
            str(CRUNCHER),
            "--ranked-cost",
            str(cost),
            "--ranked-input",
            str(workq),
            "--ranked-output",
            str(output),
            "--ranked-depth",
            "1",
            "--rank-type",
            builder.ranked_cost_type,
            "--rank-universe",
            str(builder.rank_universe),
            "--size",
            "5",
            "--start",
            "0",
            "--end",
            "0",
            "--moves",
            " ".join(builder.legal_moves),
            "--squares",
            ",".join(str(square) for square in builder.compact_squares),
            "--pairing-partners",
            ",".join(str(square) for square in builder.edge_pairing_partners),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stdout + completed.stderr
    records = list(RANKED_RECORD.iter_unpack(output.read_bytes()))
    actual_ranks = {rank for rank, _ in records}

    assert actual_ranks == rank_zero_children(builder)


def test_c_cruncher_scans_dense_cost_frontier_without_workq(tmp_path):
    builder = Build555PairLastEightEdgesEdgesOnly()
    cost = tmp_path / "cost.bin"
    with cost.open("wb") as fh:
        fh.truncate(builder.rank_universe)
    with cost.open("r+b") as fh:
        fh.write(b"\1")

    completed = subprocess.run(
        [
            str(CRUNCHER),
            "--ranked-cost",
            str(cost),
            "--ranked-scan-costs",
            "--ranked-no-workq",
            "--ranked-depth",
            "1",
            "--rank-type",
            builder.ranked_cost_type,
            "--rank-universe",
            str(builder.rank_universe),
            "--size",
            "5",
            "--start",
            "0",
            "--end",
            "0",
            "--moves",
            " ".join(builder.legal_moves),
            "--squares",
            ",".join(str(square) for square in builder.compact_squares),
            "--pairing-partners",
            ",".join(str(square) for square in builder.edge_pairing_partners),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stdout + completed.stderr
    claimed = int(completed.stdout)
    expected_ranks = rank_zero_children(builder)
    with cost.open("rb") as fh:
        for rank in expected_ranks:
            fh.seek(rank)
            assert fh.read(1) == b"\2"
    assert claimed == len(expected_ranks)

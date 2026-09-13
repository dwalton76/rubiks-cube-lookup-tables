"""Configuration checks for the dense 4x4x4 all-edge pairing table."""

# standard libraries
import struct
import subprocess
import tempfile
from pathlib import Path

# rubiks cube libraries
from rubikscubelookuptables.builder444 import Build444PairAllEdges
from rubikscubelookuptables.buildercore import edge_pairing_rank
from tests.builder_support import CRUNCHER, REPO_ROOT

RANKED_RECORD = struct.Struct("<QB")


def test_all_edge_pairing_builder_uses_the_even_matching_universe():
    builder = Build444PairAllEdges()

    assert builder.ranked_cost_type == "edge-pairing-even"
    assert builder.edge_pairing_pair_count == 12
    assert builder.rank_universe == 239_500_800
    assert len(builder.compact_squares) == 24
    assert len(builder.edge_pairing_partners) == 24


def test_solved_edges_are_rank_zero():
    builder = Build444PairAllEdges()
    state = builder._state_for_workq(builder.starting_cubes[0])

    assert edge_pairing_rank(state) == 0
    assert builder._ranked_state_unrank(0) == "0123456789ab0123456789ab"


def test_every_phase3_move_keeps_the_matching_in_the_even_orbit():
    builder = Build444PairAllEdges()
    with tempfile.TemporaryDirectory() as scratch:
        scratch = Path(scratch)
        cost = scratch / "cost.bin"
        with cost.open("wb") as fh:
            fh.truncate(builder.rank_universe)
        with cost.open("r+b") as fh:
            fh.write(b"\1")
        workq = scratch / "workq.bin"
        workq.write_bytes(RANKED_RECORD.pack(0, 0))
        output = scratch / "next.bin"
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
                "edge-pairing-even",
                "--rank-universe",
                str(builder.rank_universe),
                "--size",
                "4",
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
        assert records
        assert all(0 <= rank < builder.rank_universe for rank, _ in records)

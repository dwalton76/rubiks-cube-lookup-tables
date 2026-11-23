"""Each cube-size target must cover every table the solver asks for."""

# standard libraries
import ast
from pathlib import Path

# rubiks cube libraries
from rubikscubelookuptables.localbuild import (
    LR_BAR_FILENAME,
    _outputs_exist,
    _required_outputs,
    builder_for,
    builders_for_size,
)

SOLVER = Path(__file__).resolve().parents[2] / "rubiks-cube-NxNxN-solver" / "rubikscubennnsolver"
# Built by the C bar searcher, not a BFS class. make 666-tables builds it too.
C_ONLY = {LR_BAR_FILENAME}
# Built by `make 555-lr-joint` (about 36 GB of RAM), which `make 555` leaves out.
SEPARATE_TARGET = {"lookup-table-5x5x5-step13-LR-t-x-centers-joint.sym-nibble.bin"}


def _solver_table_names():
    names = set()
    for path in SOLVER.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
                continue
            text = node.value.strip()
            if "\n" in text or "{" in text or not text.startswith("lookup-tables/lookup-table-"):
                continue
            name = Path(text).name
            if not name.endswith((".bin", ".txt", ".json")):
                continue
            names.add(name)
    daisy = "lookup-table-6x6x6-daisy-all-inner-x-plus-{}-obliques-centers.cost-only.bin"
    for axis in ("UD", "LR", "FB"):
        names.add(daisy.format(axis))
    return names


def test_solver_tables_map_to_one_builder():
    covered = {}
    for size in ("3x3x3", "4x4x4", "5x5x5", "6x6x6", "7x7x7"):
        for cls in builders_for_size(size):
            covered[cls.__name__] = size
    assert "StartingStatesBuild555Phase4" not in covered
    assert covered["Build777Phase9UDAxisCenters"] == "7x7x7"

    missing = []
    for name in sorted(_solver_table_names()):
        if name in C_ONLY or name in SEPARATE_TARGET:
            continue
        try:
            cls_name = builder_for(name).__name__
        except LookupError:
            missing.append(name)
            continue
        marker = next(size for size in covered.values() if size in name)
        assert covered[cls_name] == marker
    assert missing == []


def test_phase4_presence_check_skips_the_starting_state_import(tmp_path, monkeypatch):
    cls = next(item for item in builders_for_size("555") if item.__name__ == "Build555Phase4")
    cost = tmp_path / "lookup-table-5x5x5-step40-phase4.cost-only.bin"
    cost.write_bytes(b"\x00")

    def explode(self):
        raise AssertionError("phase 4 starting states were loaded")

    monkeypatch.setattr(cls, "__init__", explode)
    assert _outputs_exist(cls, tmp_path) is True


def test_orbit_parity_is_built_when_even_and_odd_bins_exist(tmp_path):
    cls = next(item for item in builders_for_size("666") if item.__name__ == "Build666Phase2UDInnerXOrbit1Parity")
    even = tmp_path / "lookup-table-6x6x6-step11-UD-inner-x-centers-stage-orbit1-even.cost-only.bin"
    odd = tmp_path / "lookup-table-6x6x6-step11-UD-inner-x-centers-stage-orbit1-odd.cost-only.bin"
    even.write_bytes(b"\x00")
    odd.write_bytes(b"\x00")

    assert _outputs_exist(cls, tmp_path) is True
    assert [Path(path).name for path in _required_outputs(cls())] == [even.name, odd.name]


def test_missing_output_is_not_already_built(tmp_path):
    cls = next(item for item in builders_for_size("444") if item.__name__ == "Build444LRCentersStageRanked")
    assert _outputs_exist(cls, tmp_path) is False


def test_known_builders():
    assert builder_for("lookup-table-5x5x5-step11-LR-centers-stage-t-center-only.cost-only.bin").__name__ == (
        "Build555LRCenterStageTCenter"
    )
    assert builder_for(
        "lookup-table-4x4x4-step12-all-centers-stage-symmetry.cost-only.bin.symmetry-index.bin"
    ).__name__ == ("Build444AllCentersStageSymmetryRanked")
    assert builder_for("lookup-table-6x6x6-step11-UD-inner-x-centers-stage-orbit1-even.cost-only.bin").__name__ == (
        "Build666Phase2UDInnerXOrbit1Parity"
    )

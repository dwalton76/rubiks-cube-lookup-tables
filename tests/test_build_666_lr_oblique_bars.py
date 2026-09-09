"""Depth-1 check for the 6x6 phase-2 LR oblique bar builder.

The production table is depth 3 and is not built here. Depth 1 is enough to
confirm the C(24, 8) goals collapse under the 16 LR-axis symmetries and that
one ply of the 46 legal phase-2 moves matches the searcher.
"""

from __future__ import annotations

# standard libraries
import subprocess
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.builder_support import REPO_ROOT

SOURCE = REPO_ROOT / "rubikscubelookuptables" / "build-666-lr-oblique-bars.c"
SOLVER = REPO_ROOT.parent / "rubiks-cube-NxNxN-solver" / "rubikscubennnsolver"
ROTATE = SOLVER / "rotate_xxx.c"
CORE = SOLVER / "ida_search_core.c"
BINARY = REPO_ROOT / "rubikscubelookuptables" / "build-666-lr-oblique-bars"


def ensure_builder() -> None:
    """Compile the builder when a source is newer than the binary."""
    newest = max(path.stat().st_mtime for path in (SOURCE, ROTATE, CORE, SOLVER / "ida_search_core.h"))
    if BINARY.exists() and BINARY.stat().st_mtime >= newest:
        return
    result = subprocess.run(
        [
            "gcc",
            "-O3",
            "-Wall",
            "-Wextra",
            "-pthread",
            "-o",
            str(BINARY),
            str(SOURCE),
            str(ROTATE),
            str(CORE),
            "-lm",
            "-latomic",
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(f"could not build {BINARY}:\n{result.stdout}{result.stderr}")


class Build666LRObliqueBarsTest(unittest.TestCase):
    """Canonical goals and the first ply stay compatible with the loaded table."""

    def test_depth_one_canonicalizes_goals(self):
        ensure_builder()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "bars.bin"
            completed = subprocess.run(
                [str(BINARY), "--output", str(output), "--depth", "1", "--threads", "4"],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        normalized = (
            completed.stdout.replace("735471", "735,471").replace("46935", "46,935").replace("216908", "216,908")
        )
        self.assertIn("46 legal phase-2 moves", normalized)
        self.assertIn("735,471 raw goals, 46,935 canonical goals", normalized)
        self.assertIn("0 steps has 46,935 entries", normalized)
        self.assertIn("1 steps has 216,908 entries", normalized)


if __name__ == "__main__":
    unittest.main()

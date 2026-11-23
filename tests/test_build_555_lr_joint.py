"""Depth-4 build and verification of the joint LR t-center + x-center table.

The production table is 17.3 GB and is not built here. A depth-4 build writes
a sparse file of the same apparent size, so only the touched rows use disk.
``--verify`` is independent of the breadth-first search: it looks every state
up through the canonical cell and checks the goal, neighbour consistency and
the 16 LR-axis symmetries.
"""

from __future__ import annotations

# standard libraries
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.builder_support import REPO_ROOT

SOURCE = REPO_ROOT / "rubikscubelookuptables" / "build-555-lr-joint.c"
SOLVER = REPO_ROOT.parent / "rubiks-cube-NxNxN-solver" / "rubikscubennnsolver"
HEADER = SOLVER / "lr_joint_555.h"
ROTATE = SOLVER / "rotate_xxx.c"
CORE = SOLVER / "ida_search_core.c"
BINARY = REPO_ROOT / "rubikscubelookuptables" / "build-555-lr-joint"

CELLS = 46935 * 735471
PACKED_BYTES = (CELLS + 1) // 2
DEPTH = 4
# Cells per ply; the goal is one cell and its first move set collapses to one cell by symmetry.
DEPTH_COUNTS = [1, 1, 9, 158, 2968]


def ensure_builder() -> None:
    """Compile the builder when a source is newer than the binary."""
    newest = max(path.stat().st_mtime for path in (SOURCE, HEADER, ROTATE, CORE, SOLVER / "ida_search_core.h"))
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


def run(*arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [str(BINARY), *arguments],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


class Build555LRJointTest(unittest.TestCase):
    """A shallow build matches the class count, the per-ply cell counts and the verifier."""

    @classmethod
    def setUpClass(cls) -> None:
        ensure_builder()
        cls.directory = tempfile.TemporaryDirectory()
        cls.output = Path(cls.directory.name) / "joint.bin"
        cls.build = run("--output", str(cls.output), "--max-depth", str(DEPTH), "--threads", "4")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def test_build_reports_classes_and_cells(self):
        self.assertEqual(self.build.returncode, 0, self.build.stdout + self.build.stderr)
        self.assertIn("16 LR-axis symmetries, 46935 t classes", self.build.stdout)
        self.assertIn(f"46935 t classes x 735471 x ranks = {CELLS} cells", self.build.stdout)
        for depth, count in enumerate(DEPTH_COUNTS):
            self.assertIn(f"depth {depth}: {count} cells", self.build.stdout)

    def test_sidecar_and_file_size(self):
        self.assertEqual(self.output.stat().st_size, PACKED_BYTES)
        sidecar = json.loads(Path(f"{self.output}.json").read_text())
        self.assertEqual(sidecar["t_classes"], 46935)
        self.assertEqual(sidecar["cells"], CELLS)
        self.assertEqual(sidecar["bytes"], PACKED_BYTES)
        self.assertTrue(sidecar["partial"])
        self.assertEqual(sidecar["depth_counts"], DEPTH_COUNTS)

    def test_verify_accepts_the_table(self):
        completed = run("--verify", str(self.output), "--max-depth", str(DEPTH), "--samples", "100000", "--seed", "3")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("goal cell value 1", completed.stdout)
        self.assertIn(" 0 failures", completed.stdout)

    def test_verify_rejects_a_corrupt_cell(self):
        corrupt = Path(self.directory.name) / "corrupt.bin"
        subprocess.run(["cp", "--sparse=always", str(self.output), str(corrupt)], check=True)
        with open(corrupt, "r+b") as handle:
            first = os.lseek(handle.fileno(), 0, os.SEEK_DATA)
            handle.seek(first)
            data = handle.read(1 << 20)
            index = next(position for position, value in enumerate(data) if value)
            # Flip the low nibble, or the high nibble when only that one is set.
            flipped = data[index] ^ (0x0F if data[index] & 0x0F else 0xF0)
            handle.seek(first + index)
            handle.write(bytes([flipped]))
        completed = run("--verify", str(corrupt), "--max-depth", str(DEPTH), "--samples", "200000", "--seed", "3")
        self.assertNotEqual(completed.returncode, 0, completed.stdout)
        self.assertIn("FAIL", completed.stdout)


if __name__ == "__main__":
    unittest.main()

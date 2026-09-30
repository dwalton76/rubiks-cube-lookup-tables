"""Self-test for the joint L/R x-center and t-center table builder.

The production table is about 102 GiB and is not built here. This only compiles
the builder and runs the geometry check plus the depth-1 canonical expansion.
"""

from __future__ import annotations

# standard libraries
import subprocess
import unittest

# rubiks cube libraries
from tests.builder_support import REPO_ROOT

SOURCE = REPO_ROOT / "rubikscubelookuptables" / "build-555-lr-xt-centers.c"
ROTATE = REPO_ROOT / "rubikscubelookuptables" / "rotate_xxx.c"
BINARY = REPO_ROOT / "rubikscubelookuptables" / "build-555-lr-xt-centers"


def ensure_builder() -> None:
    """Compile the builder when either source is newer than the binary."""
    newest = max(SOURCE.stat().st_mtime, ROTATE.stat().st_mtime)
    if BINARY.exists() and BINARY.stat().st_mtime >= newest:
        return
    result = subprocess.run(
        [
            "gcc",
            "-O3",
            "-pthread",
            "-Irubikscubelookuptables",
            "-o",
            str(BINARY),
            str(SOURCE),
            str(ROTATE),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(f"could not build {BINARY}:\n{result.stdout}{result.stderr}")


class Build555LRXTCentersTest(unittest.TestCase):
    """The symmetry group and the 36 search moves agree before any table is built."""

    def test_self_test(self):
        ensure_builder()
        completed = subprocess.run(
            [str(BINARY), "--self-test"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("self-test ok", completed.stdout)


if __name__ == "__main__":
    unittest.main()

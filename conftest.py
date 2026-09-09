"""Test configuration for the whole repo.

The builder modules import rubikscubennnsolver, which lives in a sibling checkout
rather than in this repo, so the path has to be set up before pytest imports
anything under rubikscubelookuptables/. Set RUBIKS_CUBE_SOLVER to point somewhere
other than ../rubiks-cube-NxNxN-solver.
"""

# standard libraries
import os
from pathlib import Path

# Send test builds to tmp/ and keep them off histogram.txt. Set these before any
# builder is constructed so both in-process BFS objects and builderui subprocesses
# (which inherit os.environ) write to the same place.
_REPO_ROOT = Path(__file__).resolve().parent
os.environ.setdefault("RUBIKS_LOOKUP_TABLE_DIR", str(_REPO_ROOT / "tmp" / "test-lookup-tables"))
os.environ.setdefault("RUBIKS_SKIP_HISTOGRAM", "1")

# rubiks cube libraries
from tests.builder_support import ensure_importable  # noqa: E402

ensure_importable()

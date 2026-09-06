"""Test configuration for the whole repo.

The builder modules import rubikscubennnsolver, which lives in a sibling checkout
rather than in this repo, so the path has to be set up before pytest imports
anything under rubikscubelookuptables/. Set RUBIKS_CUBE_SOLVER to point somewhere
other than ../rubiks-cube-NxNxN-solver.
"""

# rubiks cube libraries
from tests.builder_support import ensure_importable

ensure_importable()

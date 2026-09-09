"""Integration coverage for the dense ranked-cost BFS path."""

from __future__ import annotations

# standard libraries
import json
import os
import unittest
from collections import Counter
from pathlib import Path

# rubiks cube libraries
from rubikscubelookuptables.buildercore import center_symmetry_rank_444
from tests.builder_support import REPO_ROOT, build_table, builder_class


def output_path(filename: str):
    path = Path(filename)
    return path if path.is_absolute() else REPO_ROOT / path


class RankedBuilderTests(unittest.TestCase):
    """The ranked C search agrees with orbit-min Python expansion at shallow depth."""

    def setUp(self):
        self.builder = builder_class("Build444AllCentersStageSymmetryRanked")()
        self.cost_path = output_path(self.builder.ranked_cost_filename)
        self.metadata_path = output_path(self.builder.ranked_metadata_filename)
        self.index_path = output_path(self.builder.ranked_symmetry_index_filename)
        self.addCleanup(self._remove_outputs)

    def _remove_outputs(self):
        for path in (self.cost_path, self.metadata_path, self.index_path):
            try:
                path.unlink()
            except FileNotFoundError:
                pass

    def _rotate_compact(self, state: str, move: str) -> str:
        full_size = (6 * self.builder.size_number * self.builder.size_number) + 1
        full_state = ["."] * full_size
        full_state[0] = "x"
        for index, char in zip(self.builder.compact_squares, state):
            full_state[index] = char
        rotated = self.builder.rotate_xxx(full_state, move)
        return "".join(rotated[index] for index in self.builder.compact_squares)

    def expected_states(self, max_depth: int) -> dict[str, int]:
        starting = {self.builder._state_for_workq(cube) for cube in self.builder.starting_cubes}
        depths = {state: 0 for state in starting}
        frontier = starting
        for depth in range(1, max_depth + 1):
            following = {
                self._rotate_compact(state, move) for state in frontier for move in self.builder.legal_moves
            } - depths.keys()
            depths.update((state, depth) for state in following)
            frontier = following
        return depths

    def test_all_center_builder_uses_center_symmetry(self):
        self.assertEqual(self.builder.ranked_cost_type, "center-symmetry-444")
        self.assertEqual(self.builder.rank_universe, 9_465_511_770)
        self.assertEqual(self.builder.rank_symbols, "FLU")
        self.assertEqual(self.builder.rank_counts, (8, 8, 8))

    def test_all_centers_depth_two_matches_direct_expansion(self):
        expected = self.expected_states(2)
        orbit_depth = {}
        for state, depth in expected.items():
            rank = center_symmetry_rank_444(state)
            previous = orbit_depth.get(rank)
            if previous is None or depth < previous:
                orbit_depth[rank] = depth

        status, output, timed_out = build_table("Build444AllCentersStageSymmetryRanked", depth=2, cores=4, timeout=60)
        self.assertFalse(timed_out, output)
        self.assertEqual(status, 0, output)
        self.assertEqual(os.path.getsize(self.cost_path), 9_465_511_770)

        metadata = json.loads(self.metadata_path.read_text(encoding="utf-8"))
        expected_per_depth = {str(depth): count for depth, count in sorted(Counter(orbit_depth.values()).items())}
        self.assertEqual(metadata["format"], "center-symmetry-444-cost-v1")
        self.assertEqual(metadata["states_per_depth"], expected_per_depth)

        with self.cost_path.open("rb", buffering=0) as costs:
            for rank, depth in orbit_depth.items():
                costs.seek(rank)
                self.assertEqual(costs.read(1), bytes((depth + 1,)))


if __name__ == "__main__":
    unittest.main()

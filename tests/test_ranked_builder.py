"""Integration coverage for the dense ranked-cost BFS path."""

from __future__ import annotations

# standard libraries
import json
import os
import unittest
from collections import Counter
from pathlib import Path

# rubiks cube libraries
from rubikscubelookuptables.buildercore import multiset_rank
from tests.builder_support import REPO_ROOT, build_table, builder_class


def output_path(filename: str):
    path = Path(filename)
    return path if path.is_absolute() else REPO_ROOT / path


class RankedBuilderTests(unittest.TestCase):
    """The ranked C search agrees with direct Python expansion at shallow depth."""

    def setUp(self):
        self.builder = builder_class("Build666InnerXCentersStageOnePhase")()
        self.cost_path = output_path(self.builder.ranked_cost_filename)
        self.metadata_path = output_path(self.builder.ranked_metadata_filename)
        self.addCleanup(self._remove_outputs)

    def _remove_outputs(self):
        for path in (self.cost_path, self.metadata_path):
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

    def test_inner_x_centers_depth_two_matches_direct_expansion(self):
        expected = self.expected_states(2)
        status, output, timed_out = build_table("Build666InnerXCentersStageOnePhase", depth=2, cores=4, timeout=60)
        self.assertFalse(timed_out, output)
        self.assertEqual(status, 0, output)
        self.assertEqual(os.path.getsize(self.cost_path), 9_465_511_770)

        metadata = json.loads(self.metadata_path.read_text(encoding="utf-8"))
        expected_per_depth = {str(depth): count for depth, count in sorted(Counter(expected.values()).items())}
        self.assertEqual(metadata["states_per_depth"], expected_per_depth)

        with self.cost_path.open("rb", buffering=0) as costs:
            for state, depth in expected.items():
                rank = multiset_rank(state, self.builder.rank_symbols, self.builder.rank_counts)
                costs.seek(rank)
                self.assertEqual(costs.read(1), bytes((depth + 1,)), state)


if __name__ == "__main__":
    unittest.main()

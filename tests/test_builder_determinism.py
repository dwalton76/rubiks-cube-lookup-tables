"""Pin down which parts of a built table are reproducible and which are not.

The baselines in builder_table_baselines.json record the state column and the
per-depth counts but deliberately not a whole-file md5. These cases are what
justify that split: the search always finds the same states at the same depths,
but which of several equally short solutions gets stored depends on how many
intermediate files the sort merged, and that changes with --cores.

Builders stage files in ./tmp, so these cases must run serially.
"""

from __future__ import annotations

# standard libraries
import hashlib
import unittest

# rubiks cube libraries
from tests.builder_support import build_table, builder_output_path, read_table

# Small enough to build twice quickly, big enough that several states are reachable
# by more than one shortest move sequence.
BUILDER = "Build444UDCentersStage"
DEPTH = 4


class BuilderDeterminismTests(unittest.TestCase):
    """Compare two builds of one table that differ only in --cores."""

    @classmethod
    def setUpClass(cls):
        cls.table = builder_output_path(BUILDER)
        cls.facts = {}
        cls.digests = {}

        for cores in (1, 4):
            status, output, timed_out = build_table(BUILDER, depth=DEPTH, cores=cores)
            if timed_out or status:
                raise unittest.SkipTest(f"{BUILDER} did not build with --cores {cores}\n{output}")
            cls.facts[cores] = read_table(cls.table, depth=DEPTH)
            cls.digests[cores] = hashlib.md5(cls.table.read_bytes()).hexdigest()

    def test_state_column_does_not_depend_on_cores(self):
        self.assertEqual(self.facts[1].states_md5, self.facts[4].states_md5)

    def test_states_per_depth_does_not_depend_on_cores(self):
        self.assertEqual(self.facts[1].states_per_depth, self.facts[4].states_per_depth)

    def test_line_count_does_not_depend_on_cores(self):
        self.assertEqual(self.facts[1].lines, self.facts[4].lines)

    def test_every_build_is_sorted_and_unambiguous(self):
        for cores, facts in self.facts.items():
            with self.subTest(cores=cores):
                self.assertTrue(facts.sorted_by_state)
                self.assertIsNone(facts.conflicting_state)

    def test_baselines_do_not_pin_anything_that_varies(self):
        # If this ever fails because the two md5s now agree, the baselines could
        # start pinning a whole-file md5 again. Until then they must not.
        pinned = set(self.facts[1].pinned())
        self.assertNotIn("md5", pinned)
        self.assertNotIn("bytes", pinned)


if __name__ == "__main__":
    unittest.main()

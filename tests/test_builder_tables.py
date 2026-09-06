"""Verify every builderui call in the Makefile still builds its expected table.

Each builder is rebuilt to the depth recorded in builder_table_baselines.json and
its output is compared byte for byte against that baseline. Builders stage files in
./tmp, so these cases must run serially: do not run this module with pytest-xdist.
"""

from __future__ import annotations

# standard libraries
import json
import re
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.builder_support import REPO_ROOT, SKIPPED_BUILDERS, build_table, makefile_builder_names, read_table

BASELINES_PATH = Path(__file__).with_name("builder_table_baselines.json")
BASELINES = json.loads(BASELINES_PATH.read_text(encoding="utf-8"))


# Split a class name into words without breaking up runs of digits, so that
# Build777Step53 becomes build_777_step_53 rather than build_7_7_7_step_5_3.
WORD_BOUNDARY = re.compile(
    r"(?<=[a-z])(?=[A-Z])" r"|(?<=[A-Z])(?=[A-Z][a-z])" r"|(?<=[A-Za-z])(?=\d)" r"|(?<=\d)(?=[A-Za-z])"
)


def method_name_for(builder: str) -> str:
    """Turn a builder class name into a readable test method name."""
    return f"test_{WORD_BOUNDARY.sub('_', builder).lower()}"


class BuilderTableTests(unittest.TestCase):
    """One case per Makefile builder, plus a guard on the Makefile itself."""

    def test_every_makefile_builder_is_accounted_for(self):
        makefile_builders = set(makefile_builder_names())
        self.assertTrue(makefile_builders, "found no builderui calls in the Makefile")
        self.assertEqual(set(BASELINES) | set(SKIPPED_BUILDERS), makefile_builders)

    def test_no_builder_is_both_baselined_and_skipped(self):
        self.assertEqual(set(BASELINES) & set(SKIPPED_BUILDERS), set())

    def assert_builder_matches_baseline(self, builder: str) -> None:
        expected = dict(BASELINES[builder])
        depth = expected.pop("depth")

        status, output, timed_out = build_table(builder, depth=depth)
        self.assertFalse(timed_out, f"{builder} timed out at depth {depth}\n{output}")
        self.assertEqual(status, 0, f"{builder} failed at depth {depth}\n{output}")

        table = REPO_ROOT / str(expected["filename"])
        self.assertTrue(table.is_file(), f"{builder} did not write {table}")

        facts = read_table(table, depth=depth)

        # The state column and how deep each state sits are decided by the search, so
        # they are the same on every run. Which of several equally short solutions gets
        # stored is not, so nothing here depends on the stored moves.
        self.assertEqual(facts.pinned(), expected)

        # Invariants the solver relies on, checked without pinning any exact value.
        self.assertTrue(facts.sorted_by_state, f"{table} is not sorted by state")
        self.assertIsNone(
            facts.conflicting_state,
            f"{table} stores one state at two different depths",
        )
        self.assertEqual(
            len(facts.line_widths),
            1,
            f"{table} is not padded to one width, saw widths {facts.line_widths}",
        )
        self.assertIsNone(
            facts.solution_over_depth,
            f"{table} holds a solution longer than the requested depth {depth}",
        )
        self.assertEqual(
            sum(facts.states_per_depth.values()),
            facts.lines,
            f"{table} per-depth counts do not add up to its line count",
        )


def _install_builder_cases() -> None:
    """Attach one test method per builder so failures name the builder."""
    for builder in sorted(BASELINES):
        depth = BASELINES[builder]["depth"]

        def case(self, builder=builder):
            self.assert_builder_matches_baseline(builder)

        case.__name__ = method_name_for(builder)
        case.__doc__ = f"Build {builder} to depth {depth} and compare it to its baseline."
        setattr(BuilderTableTests, case.__name__, case)

    for builder, reason in sorted(SKIPPED_BUILDERS.items()):

        def skipped(self, builder=builder):
            raise AssertionError("this case is expected to be skipped")

        skipped.__name__ = method_name_for(builder)
        skipped.__doc__ = f"{builder} is not built during tests: {reason}."
        setattr(BuilderTableTests, skipped.__name__, unittest.skip(reason)(skipped))


_install_builder_cases()


if __name__ == "__main__":
    unittest.main()

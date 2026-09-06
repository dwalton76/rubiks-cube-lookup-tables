"""Unit tests for the merge-diff that finds states the table has not seen yet.

builder-find-new-states.py walks a sorted table and a sorted cruncher output in
parallel and writes the states that only the cruncher produced, with their
scrambles reversed into solutions. The edges-pattern variant does the same thing
keyed on the pattern column instead of the cube state.
"""

from __future__ import annotations

# standard libraries
import io
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.script_support import load_lookup_script, read_lines, write_lines


class ScratchTestCase(unittest.TestCase):
    """Gives each case a private directory to write files in."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)
        self.script = load_lookup_script("builder-find-new-states.py")
        self.edges = load_lookup_script("builder-find-new-edges-pattern-states.py")

    def path(self, name: str, *lines: str) -> Path:
        return write_lines(self.scratch / name, lines)

    def diff(self, table, results, output="new.txt") -> list:
        destination = self.scratch / output
        self.script.diff_states(str(table), str(results), str(destination))
        return list(read_lines(destination))

    def diff_edges(self, table, results, output="new.txt") -> list:
        destination = self.scratch / output
        self.edges.diff_states(str(table), str(results), str(destination))
        return list(read_lines(destination))


class AdvanceFilehandleTests(ScratchTestCase):
    """Reading one line, or skipping to the next distinct state."""

    def test_reads_the_next_line(self):
        handle = io.StringIO("AAA:U\nBBB:R\n")
        self.assertEqual(self.script.advance_filehandle(handle), "AAA:U\n")
        self.assertEqual(self.script.advance_filehandle(handle), "BBB:R\n")

    def test_end_of_file_is_none(self):
        handle = io.StringIO("AAA:U\n")
        self.script.advance_filehandle(handle)
        self.assertIsNone(self.script.advance_filehandle(handle))

    def test_skips_duplicate_states(self):
        handle = io.StringIO("AAA:U R\nAAA:U F\nBBB:D\n")
        line = self.script.advance_filehandle_to_state_change(3, "AAA", handle)
        self.assertEqual(line, "BBB:D\n")

    def test_running_off_the_end_while_skipping_is_none(self):
        handle = io.StringIO("AAA:U R\nAAA:U F\n")
        self.assertIsNone(self.script.advance_filehandle_to_state_change(3, "AAA", handle))


class DiffStatesTests(ScratchTestCase):
    """States in B that are not in A, with scrambles turned into solutions."""

    def test_an_empty_results_file_writes_nothing(self):
        table = self.path("table.txt", "AAA:U")
        results = self.path("results.txt")
        self.assertEqual(self.diff(table, results), [])

    def test_a_missing_table_is_treated_as_empty(self):
        results = self.path("results.txt", "AAA:U")
        written = self.diff(self.scratch / "absent.txt", results)
        self.assertEqual(written, ["AAA:U'"])
        self.assertTrue((self.scratch / "absent.txt").is_file())

    def test_a_missing_results_file_is_rejected(self):
        table = self.path("table.txt", "AAA:U")
        with self.assertRaises(Exception):
            self.script.diff_states(str(table), str(self.scratch / "absent.txt"), str(self.scratch / "new.txt"))

    def test_every_result_is_new_when_the_table_is_empty(self):
        table = self.path("table.txt")
        results = self.path("results.txt", "AAA:U", "BBB:R F")
        self.assertEqual(self.diff(table, results), ["AAA:U'", "BBB:F' R'"])

    def test_a_state_already_in_the_table_is_dropped(self):
        table = self.path("table.txt", "AAA:U'")
        results = self.path("results.txt", "AAA:U", "BBB:R")
        self.assertEqual(self.diff(table, results), ["BBB:R'"])

    def test_a_table_state_that_is_not_in_the_results_is_skipped(self):
        table = self.path("table.txt", "AAA:U'", "CCC:D'")
        results = self.path("results.txt", "BBB:R")
        self.assertEqual(self.diff(table, results), ["BBB:R'"])

    def test_duplicate_results_for_one_state_are_kept_once(self):
        table = self.path("table.txt")
        results = self.path("results.txt", "AAA:U R", "AAA:U F", "BBB:D")
        self.assertEqual(self.diff(table, results), ["AAA:R' U'", "BBB:D'"])

    def test_new_states_after_the_end_of_the_table_are_kept(self):
        table = self.path("table.txt", "AAA:U'")
        results = self.path("results.txt", "BBB:R", "CCC:D")
        self.assertEqual(self.diff(table, results), ["BBB:R'", "CCC:D'"])


class EdgesPatternDiffTests(ScratchTestCase):
    """The edges-pattern variant keys on the pattern, not the cube state."""

    def test_skips_until_the_pattern_changes(self):
        handle = io.StringIO("PP:aaa:U R\nPP:bbb:U F\nQQ:ccc:D\n")
        line = self.edges.advance_filehandle_to_edges_pattern_change("PP", handle)
        self.assertEqual(line, "QQ:ccc:D")

    def test_a_new_pattern_is_written_with_its_solution(self):
        table = self.path("table.txt", "PP:aaa:U'")
        results = self.path("results.txt", "PP:aaa:U", "QQ:bbb:R F")
        self.assertEqual(self.diff_edges(table, results), ["QQ:bbb:F' R'"])

    def test_every_pattern_is_new_when_the_table_is_empty(self):
        table = self.path("table.txt")
        results = self.path("results.txt", "PP:aaa:U", "QQ:bbb:R")
        self.assertEqual(self.diff_edges(table, results), ["PP:aaa:U'", "QQ:bbb:R'"])

    def test_duplicate_patterns_are_kept_once(self):
        table = self.path("table.txt")
        results = self.path("results.txt", "PP:aaa:U R", "PP:bbb:U F", "QQ:ccc:D")
        self.assertEqual(self.diff_edges(table, results), ["PP:aaa:R' U'", "QQ:ccc:D'"])


if __name__ == "__main__":
    unittest.main()

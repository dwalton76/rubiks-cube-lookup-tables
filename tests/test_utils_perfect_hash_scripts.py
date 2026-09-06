"""Unit tests for the utils/ scripts that build and read perfect hash tables.

A perfect hash table here is one hex digit of cost per (pt0, pt1) pair, indexed by
pt0 * pt1_max + pt1, with a zero wherever a pair has no entry.
"""

from __future__ import annotations

# standard libraries
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.script_support import run_utils_script, write_lines


class PerfectHashTestCase(unittest.TestCase):
    """Gives each case a private directory to build hash files in."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)

    def build(self, *lines: str, pt0_max: int = 2, pt1_max: int = 2) -> str:
        # The output filename is the input with pt_state swapped out, so the input has
        # to be named accordingly.
        source = write_lines(self.scratch / "table.pt_state", lines)
        run_utils_script("convert-pt-state-to-perfect-hash.py", str(source), str(pt0_max), str(pt1_max))
        return (self.scratch / "table.pt-state-perfect-hash").read_text(encoding="utf-8")


class ConvertPtStateToPerfectHashTests(PerfectHashTestCase):
    """utils/convert-pt-state-to-perfect-hash.py lays costs out by index."""

    def test_each_pair_lands_at_its_index(self):
        # (0,0) -> index 0 and (1,1) -> index 3.
        self.assertEqual(self.build("0-0:1", "1-1:2"), "1002")

    def test_pairs_with_no_entry_are_zero(self):
        self.assertEqual(self.build("0-1:5"), "0500")

    def test_the_table_covers_every_pair(self):
        self.assertEqual(len(self.build("0-0:1", pt0_max=3, pt1_max=4)), 12)

    def test_costs_above_nine_become_hex_digits(self):
        self.assertEqual(self.build("0-0:10", "0-1:15"), "af00")

    def test_a_cost_over_fifteen_is_rejected(self):
        source = write_lines(self.scratch / "table.pt_state", ("0-0:16",))
        completed = run_utils_script(
            "convert-pt-state-to-perfect-hash.py",
            str(source),
            "2",
            "2",
            expect_success=False,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("too high", completed.stderr)

    def test_a_pair_outside_the_table_is_rejected(self):
        source = write_lines(self.scratch / "table.pt_state", ("9-9:1",))
        completed = run_utils_script(
            "convert-pt-state-to-perfect-hash.py",
            str(source),
            "2",
            "2",
            expect_success=False,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("IndexError", completed.stderr)


class ReadPerfectHashIndexTests(PerfectHashTestCase):
    """utils/read-perfect-hash-index.py reads one cost back out."""

    def setUp(self):
        super().setUp()
        self.table = self.scratch / "table.perfect-hash"
        self.table.write_text("1002", encoding="utf-8")

    def read(self, pt0_state: int, pt1_state: int, pt1_max: int = 2) -> str:
        completed = run_utils_script(
            "read-perfect-hash-index.py",
            str(self.table),
            str(pt0_state),
            str(pt1_state),
            str(pt1_max),
        )
        return completed.stdout.strip()

    def test_reads_the_first_entry(self):
        self.assertEqual(self.read(0, 0), "index 0 is 1")

    def test_reads_the_last_entry(self):
        self.assertEqual(self.read(1, 1), "index 3 is 2")

    def test_reads_a_pair_with_no_entry(self):
        self.assertEqual(self.read(0, 1), "index 1 is 0")

    def test_round_trips_what_the_writer_wrote(self):
        source = write_lines(self.scratch / "table.pt_state", ("1-0:7",))
        run_utils_script("convert-pt-state-to-perfect-hash.py", str(source), "2", "2")
        self.table = self.scratch / "table.pt-state-perfect-hash"
        self.assertEqual(self.read(1, 0), "index 2 is 7")


class BuildPerfectHashTests(PerfectHashTestCase):
    """utils/build-perfect-hash.py only handles the tables it knows about.

    Building a real one needs the solver's own lookup tables, so these cases cover
    the argument handling rather than the build itself.
    """

    def test_a_missing_input_is_rejected(self):
        completed = run_utils_script(
            "build-perfect-hash.py",
            str(self.scratch / "absent.txt"),
            expect_success=False,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("FileNotFoundError", completed.stderr)

    def test_an_unrecognised_table_is_rejected(self):
        source = write_lines(self.scratch / "some-other-table.txt", ("AAA:U",))
        completed = run_utils_script("build-perfect-hash.py", str(source), expect_success=False)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("NotImplementedError", completed.stderr)

    def test_it_documents_its_usage(self):
        completed = run_utils_script("build-perfect-hash.py", "--help")
        self.assertIn("--file-out", completed.stdout)


if __name__ == "__main__":
    unittest.main()

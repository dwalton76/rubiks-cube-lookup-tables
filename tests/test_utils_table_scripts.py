"""Unit tests for the C pad-lines helper that save() uses."""

from __future__ import annotations

# standard libraries
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.builder_support import ensure_pad_lines
from tests.script_support import read_lines, run_pad_lines, write_lines


class ScratchTableTestCase(unittest.TestCase):
    """Gives each case a private directory to build small tables in."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)
        ensure_pad_lines()

    def table(self, *lines: str, name: str = "table.txt") -> Path:
        return write_lines(self.scratch / name, lines)


class PadLinesTests(ScratchTableTestCase):
    """utils/pad-lines widens every line to match the longest one."""

    def test_every_line_is_padded_to_the_longest_line(self):
        table = self.table("AAA:U", "BBB:U R F", "CCC:U R")
        run_pad_lines(str(table))

        lines = read_lines(table)
        self.assertEqual(lines, ["AAA:U    ", "BBB:U R F", "CCC:U R  "])
        self.assertEqual({len(line) for line in lines}, {len("BBB:U R F")})

    def test_an_already_padded_file_is_unchanged(self):
        table = self.table("AAA:U R", "BBB:F L")
        before = table.read_bytes()
        run_pad_lines(str(table))
        self.assertEqual(table.read_bytes(), before)

    def test_existing_padding_sets_the_width(self):
        # The measured width counts padding that is already there, so padding a file
        # a second time keeps the wider width rather than shrinking back to the
        # longest solution.
        table = self.table("AAA:U      ", "BBB:F")
        run_pad_lines(str(table))
        self.assertEqual(read_lines(table), ["AAA:U      ", "BBB:F      "])

    def test_reports_the_width_it_used(self):
        table = self.table("AAA:U R F")
        completed = run_pad_lines(str(table))
        self.assertIn("max_length: 9", completed.stdout)

    def test_an_explicit_width_is_used_instead_of_measuring(self):
        table = self.table("AAA:U", "BBB:F")
        run_pad_lines(str(table), "8")
        self.assertEqual(read_lines(table), ["AAA:U   ", "BBB:F   "])

    def test_an_empty_file_is_left_alone(self):
        table = self.table()
        completed = run_pad_lines(str(table))
        self.assertEqual(table.read_bytes(), b"")
        self.assertIn("max_length: 0", completed.stdout)

    def test_a_line_wider_than_the_requested_width_is_rejected(self):
        table = self.table("AAA:U R F")
        completed = run_pad_lines(str(table), "3", expect_success=False)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("wider than the requested", completed.stderr)

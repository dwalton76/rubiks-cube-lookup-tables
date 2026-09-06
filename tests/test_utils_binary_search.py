"""Unit tests for utils/binary-search-lookup.py.

This is how a built table gets queried, so the cases below cover both the plain
lookup and the batched one, including the misses at either end of the file.
"""

from __future__ import annotations

# standard libraries
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.script_support import load_utils_script, write_lines

# A padded, sorted table, which is the only shape these functions accept: every line
# is the same width so a line can be found by multiplying an offset by that width.
TABLE = (
    "AAA:U      ",
    "BBB:U R    ",
    "CCC:U R F  ",
    "DDD:D2     ",
    "EEE:L' B   ",
)


class BinarySearchTestCase(unittest.TestCase):
    """Loads the script and writes the sample table once per case."""

    def setUp(self):
        self.script = load_utils_script("binary-search-lookup.py")
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.table = write_lines(Path(self._scratch.name) / "table.txt", TABLE)
        self.width, self.state_width, self.linecount = self.script.get_file_vitals(str(self.table))


class FileVitalsTests(BinarySearchTestCase):
    """get_file_vitals() derives the geometry the search relies on."""

    def test_line_width_includes_the_newline(self):
        self.assertEqual(self.width, len(TABLE[0]) + 1)

    def test_state_width_is_the_state_column(self):
        self.assertEqual(self.state_width, 3)

    def test_line_count_is_derived_from_the_file_size(self):
        self.assertEqual(self.linecount, len(TABLE))


class BinarySearchTests(BinarySearchTestCase):
    """binary_search() finds one state and returns its solution."""

    def search(self, state):
        with self.table.open("rb") as handle:
            return self.script.binary_search(handle, self.width, self.state_width, self.linecount, state)

    def test_finds_the_first_entry(self):
        value, line_number = self.search("AAA")
        self.assertEqual(value.strip(), "U")
        self.assertEqual(line_number, 0)

    def test_finds_the_last_entry(self):
        value, line_number = self.search("EEE")
        self.assertEqual(value.strip(), "L' B")
        self.assertEqual(line_number, len(TABLE) - 1)

    def test_finds_every_entry(self):
        for offset, line in enumerate(TABLE):
            state, _, moves = line.partition(":")
            with self.subTest(state=state):
                value, line_number = self.search(state)
                self.assertEqual(value.strip(), moves.strip())
                self.assertEqual(line_number, offset)

    def test_a_missing_state_returns_nothing(self):
        self.assertEqual(self.search("CCX"), (None, None))

    def test_a_state_before_the_first_entry_returns_nothing(self):
        self.assertEqual(self.search("AAA"[:2] + "0"), (None, None))

    def test_a_state_after_the_last_entry_returns_nothing(self):
        self.assertEqual(self.search("ZZZ"), (None, None))


class BinarySearchListTests(BinarySearchTestCase):
    """binary_search_list() searches an in-memory list instead of a file."""

    def states(self):
        return [line.split(":")[0] for line in TABLE]

    def test_reports_the_offset_of_a_state_it_finds(self):
        found, offset = self.script.binary_search_list(self.states(), b"CCC")
        self.assertTrue(found)
        self.assertEqual(offset, 2)

    def test_reports_the_insertion_point_of_a_state_it_does_not_find(self):
        found, offset = self.script.binary_search_list(self.states(), b"CCX")
        self.assertFalse(found)
        self.assertEqual(offset, 3)

    def test_a_state_before_everything_inserts_at_the_front(self):
        found, offset = self.script.binary_search_list(self.states(), b"000")
        self.assertFalse(found)
        self.assertEqual(offset, 0)

    def test_a_state_after_everything_inserts_at_the_end(self):
        found, offset = self.script.binary_search_list(self.states(), b"ZZZ")
        self.assertFalse(found)
        self.assertEqual(offset, len(TABLE))

    def test_an_empty_list_finds_nothing(self):
        found, offset = self.script.binary_search_list([], b"AAA")
        self.assertFalse(found)
        self.assertEqual(offset, 0)


class BinarySearchMultipleTests(BinarySearchTestCase):
    """binary_search_multiple() looks up many states in one pass."""

    def search(self, states):
        with self.table.open("rb") as handle:
            return self.script.binary_search_multiple(
                handle, self.width, self.state_width, self.linecount, list(states)
            )

    def test_finds_several_states_at_once(self):
        results = self.search(["AAA", "CCC", "EEE"])
        self.assertEqual([value.strip() for value in results], ["U", "U R F", "L' B"])

    def test_results_follow_sorted_key_order(self):
        # The function sorts its keys, so results come back in state order rather
        # than in the order they were requested.
        results = self.search(["EEE", "AAA"])
        self.assertEqual([value.strip() for value in results], ["U", "L' B"])

    def test_a_missing_state_in_the_middle_comes_back_as_none(self):
        results = self.search(["AAA", "CCX", "EEE"])
        self.assertEqual(len(results), 3)
        self.assertIsNone(results[1])

    def test_states_past_the_last_entry_are_dropped(self):
        results = self.search(["AAA", "ZZZ"])
        self.assertEqual([value.strip() for value in results], ["U"])

    def test_finds_every_state_in_the_table(self):
        results = self.search([line.split(":")[0] for line in TABLE])
        self.assertEqual(
            [value.strip() for value in results],
            [line.split(":", 1)[1].strip() for line in TABLE],
        )


class FindFirstLastTests(BinarySearchTestCase):
    """find_first_last() narrows the search window using cached reads."""

    def test_a_cached_exact_match_collapses_the_window(self):
        _, first, last = self.script.find_first_last(self.linecount, [(2, b"CCC")], b"CCC")
        self.assertEqual((first, last), (2, 2))

    def test_a_cached_smaller_state_moves_the_window_start(self):
        _, first, _ = self.script.find_first_last(self.linecount, [(1, b"BBB")], b"CCC")
        self.assertEqual(first, 1)

    def test_a_cached_larger_state_moves_the_window_end(self):
        _, _, last = self.script.find_first_last(self.linecount, [(3, b"DDD")], b"CCC")
        self.assertEqual(last, 3)

    def test_the_window_still_covers_the_target(self):
        cache = [(0, b"AAA"), (1, b"BBB"), (3, b"DDD")]
        _, first, last = self.script.find_first_last(self.linecount, list(cache), b"CCC")
        self.assertLessEqual(first, 2)
        self.assertGreaterEqual(last, 2)


if __name__ == "__main__":
    unittest.main()

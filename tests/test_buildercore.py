"""Unit tests for the helpers in rubikscubelookuptables/buildercore.py.

These used to live as doctest examples in the function docstrings. They are
ordinary TestCase methods now so a failure names the behavior, not the module.
"""

from __future__ import annotations

# standard libraries
import tempfile
import unittest
from pathlib import Path

# third party libraries
from pyhashxx import hashxx

# rubiks cube libraries
from rubikscubelookuptables.buildercore import (
    convert_state_to_hex,
    convert_to_cost_only,
    convert_to_hash_cost_only,
    get_line_number_splits,
    reverse_steps,
)


class GetLineNumberSplitsTests(unittest.TestCase):
    """How a workq is carved up across cores."""

    def test_one_core_covers_the_whole_file(self):
        self.assertEqual(get_line_number_splits(100, 1), ((0, 99),))

    def test_two_cores_split_evenly(self):
        self.assertEqual(get_line_number_splits(100, 2), ((0, 49), (50, 99)))

    def test_five_cores_split_evenly(self):
        self.assertEqual(get_line_number_splits(100, 5), ((0, 19), (20, 39), (40, 59), (60, 79), (80, 99)))

    def test_a_remainder_goes_to_the_last_core(self):
        self.assertEqual(get_line_number_splits(100, 3), ((0, 32), (33, 65), (66, 99)))

    def test_a_small_file_still_gives_the_last_core_the_tail(self):
        self.assertEqual(get_line_number_splits(10, 3), ((0, 2), (3, 5), (6, 9)))

    def test_extra_cores_get_nothing_to_do(self):
        self.assertEqual(
            get_line_number_splits(2, 4),
            ((0, 1), (None, None), (None, None), (None, None)),
        )

    def test_rejects_a_zero_line_count(self):
        with self.assertRaises(AssertionError):
            get_line_number_splits(0, 1)

    def test_rejects_a_zero_core_count(self):
        with self.assertRaises(AssertionError):
            get_line_number_splits(10, 0)


class ReverseStepsTests(unittest.TestCase):
    """Inverting a scramble, last move first."""

    def test_an_empty_scramble_stays_empty(self):
        self.assertEqual(reverse_steps([]), [])

    def test_a_quarter_turn_becomes_its_prime(self):
        self.assertEqual(reverse_steps(["U"]), ["U'"])

    def test_a_prime_becomes_a_quarter_turn(self):
        self.assertEqual(reverse_steps(["U'"]), ["U"])

    def test_a_half_turn_is_its_own_inverse(self):
        self.assertEqual(reverse_steps(["D2"]), ["D2"])

    def test_the_moves_come_out_in_reverse_order(self):
        self.assertEqual(reverse_steps(["U", "R'", "D2"]), ["D2", "R", "U'"])

    def test_a_wide_turn_keeps_its_prefix(self):
        self.assertEqual(reverse_steps(["3Uw", "Rw'"]), ["Rw", "3Uw'"])


class ConvertStateToHexTests(unittest.TestCase):
    """Packing a two-color state into hex."""

    def test_the_last_square_set_is_the_ones_bit(self):
        self.assertEqual(convert_state_to_hex("xxxU"), "1")

    def test_bits_are_grouped_into_nibbles(self):
        self.assertEqual(convert_state_to_hex("UxUx"), "a")

    def test_an_odd_length_state_is_left_padded(self):
        self.assertEqual(convert_state_to_hex("UUxUx"), "1a")

    def test_dashes_count_as_unset(self):
        self.assertEqual(convert_state_to_hex("--U-"), "2")

    def test_every_face_letter_counts_as_set(self):
        self.assertEqual(convert_state_to_hex("ULFR"), "f")

    def test_an_all_unset_state_is_zero(self):
        self.assertEqual(convert_state_to_hex("xxxx"), "0")


class ConvertToCostOnlyTests(unittest.TestCase):
    """Packing hex-keyed tables into one cost digit per state."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)

    def convert(self, *lines: str) -> str:
        table = self.scratch / "table.txt"
        table.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")
        convert_to_cost_only(str(table))
        return (self.scratch / "table.cost-only.txt").read_text(encoding="utf-8")

    def test_consecutive_hex_states_become_one_digit_each(self):
        self.assertEqual(self.convert("0:U", "1:U R", "2:U R F"), "123")

    def test_gaps_between_states_are_filled_with_zeroes(self):
        self.assertEqual(self.convert("2:U", "5:U R"), "001002")

    def test_an_empty_solution_costs_nothing(self):
        self.assertEqual(self.convert("0:"), "0")

    def test_a_numeric_cost_is_stored_as_is(self):
        self.assertEqual(self.convert("0:7"), "7")

    def test_a_cost_over_fifteen_is_capped(self):
        self.assertEqual(self.convert("0:" + " ".join(["U"] * 16)), "f")


class ConvertToHashCostOnlyTests(unittest.TestCase):
    """Packing states into a fixed-size bucket of min costs."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)

    def convert(self, *lines: str, buckets: int = 8) -> str:
        table = self.scratch / "table.txt"
        table.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")
        convert_to_hash_cost_only(str(table), buckets)
        return (self.scratch / "table.hash-cost-only.txt").read_text(encoding="utf-8")

    def bucket_for(self, state: str, buckets: int) -> int:
        return hashxx(state.encode("utf-8")) % buckets

    def test_the_file_is_one_hex_digit_per_bucket(self):
        written = self.convert("AAA:U", buckets=8)
        self.assertEqual(len(written.strip()), 8)
        self.assertTrue(written.endswith("\n"))

    def test_an_empty_bucket_is_zero(self):
        written = self.convert("AAA:U", buckets=8).strip()
        occupied = self.bucket_for("AAA", 8)
        for index, digit in enumerate(written):
            if index != occupied:
                self.assertEqual(digit, "0")

    def test_the_occupied_bucket_holds_the_cost(self):
        written = self.convert("AAA:U R F", buckets=8).strip()
        occupied = self.bucket_for("AAA", 8)
        self.assertEqual(written[occupied], "3")

    def test_a_collision_keeps_the_shorter_cost(self):
        buckets = 1
        written = self.convert("AAA:U R F", "BBB:U", buckets=buckets).strip()
        self.assertEqual(written, "1")

    def test_a_numeric_cost_is_stored_as_is(self):
        written = self.convert("AAA:7", buckets=8).strip()
        occupied = self.bucket_for("AAA", 8)
        self.assertEqual(written[occupied], "7")

    def test_a_cost_over_fifteen_is_capped(self):
        written = self.convert("AAA:" + " ".join(["U"] * 16), buckets=8).strip()
        occupied = self.bucket_for("AAA", 8)
        self.assertEqual(written[occupied], "f")


if __name__ == "__main__":
    unittest.main()

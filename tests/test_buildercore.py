"""Unit tests for the helpers in rubikscubelookuptables/buildercore.py.

These used to live as doctest examples in the function docstrings. They are
ordinary TestCase methods now so a failure names the behavior, not the module.
"""

from __future__ import annotations

# standard libraries
import json
import os
import tempfile
import unittest
from pathlib import Path

# third party libraries
from pyhashxx import hashxx

# rubiks cube libraries
from rubikscubelookuptables.buildercore import (
    BFS,
    convert_state_to_hex,
    convert_to_cost_only,
    convert_to_hash_cost_only,
    get_line_number_splits,
    lookup_table_dir,
    mixed_radix_rank,
    mixed_radix_unrank,
    multiset_rank,
    multiset_size,
    multiset_unrank,
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


class LookupTableDirTests(unittest.TestCase):
    """Finished tables can be redirected away from lookup-tables/."""

    def test_default_is_lookup_tables(self):
        previous = os.environ.pop("RUBIKS_LOOKUP_TABLE_DIR", None)
        try:
            self.assertEqual(lookup_table_dir(), Path("lookup-tables"))
        finally:
            if previous is not None:
                os.environ["RUBIKS_LOOKUP_TABLE_DIR"] = previous

    def test_env_override_is_honored(self):
        previous = os.environ.get("RUBIKS_LOOKUP_TABLE_DIR")
        os.environ["RUBIKS_LOOKUP_TABLE_DIR"] = "tmp/test-lookup-tables"
        try:
            self.assertEqual(lookup_table_dir(), Path("tmp/test-lookup-tables"))
        finally:
            if previous is None:
                os.environ.pop("RUBIKS_LOOKUP_TABLE_DIR", None)
            else:
                os.environ["RUBIKS_LOOKUP_TABLE_DIR"] = previous


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


class MultisetRankTests(unittest.TestCase):
    """Dense lexicographic ranks for states with repeated symbols."""

    def test_small_multiset_has_the_expected_size(self):
        self.assertEqual(multiset_size((2, 1)), 3)

    def test_x_center_universe_has_the_expected_size(self):
        self.assertEqual(multiset_size((8, 8, 8)), 9_465_511_770)

    def test_known_ranks(self):
        self.assertEqual(multiset_rank("AAB", "AB", (2, 1)), 0)
        self.assertEqual(multiset_rank("ABA", "AB", (2, 1)), 1)
        self.assertEqual(multiset_rank("BAA", "AB", (2, 1)), 2)

    def test_every_small_rank_round_trips(self):
        symbols = "ABC"
        counts = (2, 1, 1)
        for rank in range(multiset_size(counts)):
            state = multiset_unrank(rank, symbols, counts)
            self.assertEqual(multiset_rank(state, symbols, counts), rank)

    def test_rejects_an_out_of_range_rank(self):
        with self.assertRaises(ValueError):
            multiset_unrank(3, "AB", (2, 1))

    def test_rejects_the_wrong_symbol_counts(self):
        with self.assertRaises(ValueError):
            multiset_rank("ABB", "AB", (2, 1))

    def test_rejects_unsorted_symbols(self):
        with self.assertRaises(ValueError):
            multiset_rank("AAB", "BA", (1, 2))

    def test_two_group_mixed_radix_order(self):
        self.assertEqual(mixed_radix_rank((2, 3), (6, 6)), (2 * 6) + 3)
        self.assertEqual(mixed_radix_unrank(15, (6, 6)), (2, 3))

    def test_every_two_group_rank_round_trips(self):
        for rank in range(36):
            components = mixed_radix_unrank(rank, (6, 6))
            self.assertEqual(mixed_radix_rank(components, (6, 6)), rank)

    def test_grouped_unrank_reconstructs_the_compact_state(self):
        builder = BFS.__new__(BFS)
        builder.compact_squares = tuple(range(8))
        builder.rank_universes = (6, 6)
        builder.rank_groups = (
            {"offset": 0, "length": 4, "symbols": "AB", "counts": (2, 2)},
            {"offset": 4, "length": 4, "symbols": "AB", "counts": (2, 2)},
        )
        state = "BAABABBA"
        rank = builder._ranked_state_rank(state)
        self.assertEqual(rank, multiset_rank("BAAB", "AB", (2, 2)) * 6 + multiset_rank("ABBA", "AB", (2, 2)))
        self.assertEqual(builder._ranked_state_unrank(rank), state)

    def test_grouped_metadata_describes_both_radices(self):
        with tempfile.TemporaryDirectory() as scratch:
            builder = BFS.__new__(BFS)
            builder.ranked_metadata_filename = str(Path(scratch) / "cost.bin.json")
            builder.rank_groups = (
                {
                    "squares": [1, 2, 3, 4],
                    "offset": 0,
                    "length": 4,
                    "symbols": "AB",
                    "counts": (2, 2),
                    "universe_size": 6,
                },
                {
                    "squares": [5, 9, 13, 17],
                    "offset": 4,
                    "length": 4,
                    "symbols": "AB",
                    "counts": (2, 2),
                    "universe_size": 6,
                },
            )
            builder.rank_universe = 36
            builder.stats = {0: 1, 1: 3}
            builder._write_ranked_metadata()
            metadata = json.loads(Path(builder.ranked_metadata_filename).read_text(encoding="utf-8"))

        self.assertEqual([group["universe_size"] for group in metadata["rank_groups"]], [6, 6])
        self.assertEqual(metadata["rank_order"], "left-to-right mixed radix")
        self.assertNotIn("symbols", metadata)
        self.assertEqual(metadata["cost_encoding"], {"0": "unseen", "nonzero": "depth + 1"})

    def test_single_group_metadata_keeps_legacy_fields(self):
        with tempfile.TemporaryDirectory() as scratch:
            builder = BFS.__new__(BFS)
            builder.ranked_metadata_filename = str(Path(scratch) / "cost.bin.json")
            builder.rank_groups = (
                {
                    "squares": [1, 2, 3, 4],
                    "offset": 0,
                    "length": 4,
                    "symbols": "AB",
                    "counts": (2, 2),
                    "universe_size": 6,
                },
            )
            builder.rank_symbols = "AB"
            builder.rank_counts = (2, 2)
            builder.rank_universe = 6
            builder.stats = {0: 1}
            builder._write_ranked_metadata()
            metadata = json.loads(Path(builder.ranked_metadata_filename).read_text(encoding="utf-8"))

        self.assertEqual(metadata["symbols"], "AB")
        self.assertEqual(metadata["counts"], [2, 2])


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


class HistogramTests(unittest.TestCase):
    """Per-depth reports that both text and ranked builders append to histogram.txt."""

    def fake_builder(self, **attrs):
        builder = BFS.__new__(BFS)
        builder.stats = {}
        builder.starting_state_count = 0
        builder.use_ranked_cost = False
        for name, value in attrs.items():
            setattr(builder, name, value)
        return builder

    def test_text_tables_add_starting_states_that_are_not_in_stats(self):
        builder = self.fake_builder(stats={0: 0, 1: 4, 2: 70}, starting_state_count=1)
        self.assertEqual(builder._table_linecount(), 75)

    def test_ranked_tables_do_not_double_count_starting_states(self):
        builder = self.fake_builder(stats={0: 1, 1: 4, 2: 70}, starting_state_count=1)
        self.assertEqual(builder._table_linecount(), 75)

    def test_ranked_save_appends_histogram_txt(self):
        builder = self.fake_builder(
            stats={0: 1, 1: 4, 2: 70},
            starting_state_count=1,
            use_ranked_cost=True,
            ranked_cost_filename="lookup-table.cost-only.bin",
            time_in_save=0,
            name="histogram-test",
        )
        builder._publish_ranked_cost_file = lambda: None
        builder._write_ranked_metadata = lambda: None
        previous_skip = os.environ.pop("RUBIKS_SKIP_HISTOGRAM", None)

        try:
            with tempfile.TemporaryDirectory() as tmp:
                cwd = Path.cwd()
                try:
                    os.chdir(tmp)
                    builder.save()
                    histogram = Path("histogram.txt").read_text(encoding="utf-8")
                finally:
                    os.chdir(cwd)
        finally:
            if previous_skip is not None:
                os.environ["RUBIKS_SKIP_HISTOGRAM"] = previous_skip

        self.assertIn("lookup-table.cost-only.bin", histogram)
        self.assertIn("0 steps has 1 entries", histogram)
        self.assertIn("1 steps has 4 entries", histogram)
        self.assertIn("2 steps has 70 entries", histogram)
        self.assertIn("Total: 75 entries", histogram)

    def test_skip_histogram_env_does_not_write_histogram_txt(self):
        builder = self.fake_builder(
            stats={0: 1, 1: 4},
            starting_state_count=1,
            use_ranked_cost=True,
            ranked_cost_filename="lookup-table.cost-only.bin",
            time_in_save=0,
            name="histogram-test",
        )
        builder._publish_ranked_cost_file = lambda: None
        builder._write_ranked_metadata = lambda: None

        with tempfile.TemporaryDirectory() as tmp:
            cwd = Path.cwd()
            try:
                os.chdir(tmp)
                os.environ["RUBIKS_SKIP_HISTOGRAM"] = "1"
                builder.save()
                self.assertFalse(Path("histogram.txt").exists())
            finally:
                os.chdir(cwd)


if __name__ == "__main__":
    unittest.main()

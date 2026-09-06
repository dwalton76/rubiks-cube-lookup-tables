"""Unit tests for the utils/ scripts that rewrite a lookup-table file.

These all take a small table on disk, rewrite it in place or alongside itself, and
are checked against a hand-written expected result.
"""

from __future__ import annotations

# standard libraries
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.builder_support import ensure_pad_lines
from tests.script_support import load_utils_script, read_lines, run_pad_lines, run_utils_script, write_lines


class ScratchTableTestCase(unittest.TestCase):
    """Gives each case a private directory to build small tables in."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)
        # keep-specific-depth and keep-up-to-depth shell out to the C helper.
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


class KeepSpecificDepthTests(ScratchTableTestCase):
    """utils/keep-specific-depth.py keeps only solutions of one exact length."""

    def test_keeps_only_entries_at_the_requested_depth(self):
        table = self.table("AAA:U", "BBB:U R", "CCC:U R F", "DDD:U R")
        run_utils_script("keep-specific-depth.py", str(table), "2")

        self.assertEqual([line.rstrip() for line in read_lines(Path(f"{table}.new"))], ["BBB:U R", "DDD:U R"])

    def test_leaves_the_original_table_alone(self):
        table = self.table("AAA:U", "BBB:U R")
        before = table.read_bytes()
        run_utils_script("keep-specific-depth.py", str(table), "1")
        self.assertEqual(table.read_bytes(), before)

    def test_result_is_padded(self):
        table = self.table("AAA:U R", "BBB:U R2", "CCC:F")
        run_utils_script("keep-specific-depth.py", str(table), "2")

        lines = read_lines(Path(f"{table}.new"))
        self.assertEqual(len({len(line) for line in lines}), 1)

    def test_a_depth_no_entry_has_gives_an_empty_result(self):
        table = self.table("AAA:U", "BBB:U R")
        run_utils_script("keep-specific-depth.py", str(table), "9")
        self.assertEqual(read_lines(Path(f"{table}.new")), [])


class KeepUpToDepthTests(ScratchTableTestCase):
    """utils/keep-up-to-depth.py keeps solutions no longer than a limit."""

    def test_keeps_entries_at_or_below_the_limit(self):
        table = self.table("AAA:U", "BBB:U R", "CCC:U R F")
        run_utils_script("keep-up-to-depth.py", str(table), "2")

        self.assertEqual([line.rstrip() for line in read_lines(Path(f"{table}.new"))], ["AAA:U", "BBB:U R"])

    def test_reads_a_cost_only_table_as_a_depth(self):
        # In a table that stores a step count instead of the steps, the number is
        # the depth rather than a one move solution.
        table = self.table("AAA:1", "BBB:2", "CCC:7")
        run_utils_script("keep-up-to-depth.py", str(table), "2")

        self.assertEqual([line.rstrip() for line in read_lines(Path(f"{table}.new"))], ["AAA:1", "BBB:2"])

    def test_keeps_everything_when_the_limit_is_high(self):
        table = self.table("AAA:U", "BBB:U R", "CCC:U R F")
        run_utils_script("keep-up-to-depth.py", str(table), "99")
        self.assertEqual(len(read_lines(Path(f"{table}.new"))), 3)


class KeepBestSolutionTests(ScratchTableTestCase):
    """utils/keep-best-solution.py collapses repeated states to the shortest one."""

    def setUp(self):
        super().setUp()
        self.script = load_utils_script("keep-best-solution.py")

    def test_keeps_the_shortest_solution_for_a_repeated_state(self):
        table = self.table("AAA:U R F", "AAA:U", "BBB:F")
        self.script.keep_best_solutions(str(table))
        self.assertEqual(read_lines(table), ["AAA:U", "BBB:F"])

    def test_a_table_with_no_repeats_is_unchanged(self):
        table = self.table("AAA:U", "BBB:U R", "CCC:U R F")
        self.script.keep_best_solutions(str(table))
        self.assertEqual(read_lines(table), ["AAA:U", "BBB:U R", "CCC:U R F"])

    def test_keeps_the_shortest_of_several_repeats(self):
        table = self.table("AAA:U R F", "AAA:U R", "AAA:U R F L", "BBB:F")
        self.script.keep_best_solutions(str(table))
        self.assertEqual(read_lines(table), ["AAA:U R", "BBB:F"])

    def test_handles_a_state_that_itself_contains_a_colon(self):
        # Tables that pair centers with edges carry two colons per line, which the
        # script detects from its first line and then parses with a regex.
        table = self.table("AAA:BBB:U R F", "AAA:BBB:U", "CCC:DDD:F")
        self.script.keep_best_solutions(str(table))
        self.assertEqual(read_lines(table), ["AAA:BBB:U", "CCC:DDD:F"])

    def test_trailing_padding_is_not_counted_as_a_move(self):
        table = self.table("AAA:U      ", "AAA:U R")
        self.script.keep_best_solutions(str(table))
        self.assertEqual(read_lines(table), ["AAA:U"])


class ChopAllButFirstStepTests(ScratchTableTestCase):
    """utils/lookup-table-chop-all-but-first-step.py trims solutions to one move."""

    def test_keeps_only_the_first_move(self):
        table = self.table("AAA:U R F", "BBB:D2 L")
        run_utils_script("lookup-table-chop-all-but-first-step.py", str(table))
        self.assertEqual([line.rstrip() for line in read_lines(table)], ["AAA:U", "BBB:D2"])

    def test_an_empty_solution_stays_empty(self):
        table = self.table("AAA:", "BBB:U R")
        run_utils_script("lookup-table-chop-all-but-first-step.py", str(table))
        self.assertEqual([line.rstrip() for line in read_lines(table)], ["AAA:", "BBB:U"])

    def test_result_is_padded_to_one_width(self):
        table = self.table("AAA:U R F", "BBB:D2 L")
        run_utils_script("lookup-table-chop-all-but-first-step.py", str(table))
        self.assertEqual(len({len(line) for line in read_lines(table)}), 1)


class ConvertStepsToStepCountTests(ScratchTableTestCase):
    """utils/lookup-table-convert-steps-to-step-count.py stores a depth, not moves."""

    def test_replaces_the_solution_with_its_length(self):
        table = self.table("AAA:U", "BBB:U R", "CCC:U R F")
        run_utils_script("lookup-table-convert-steps-to-step-count.py", str(table))
        self.assertEqual(read_lines(Path(f"{table}.final")), ["AAA:1", "BBB:2", "CCC:3"])

    def test_an_empty_solution_becomes_zero(self):
        table = self.table("AAA:")
        run_utils_script("lookup-table-convert-steps-to-step-count.py", str(table))
        self.assertEqual(read_lines(Path(f"{table}.final")), ["AAA:0"])

    def test_padding_is_not_counted(self):
        table = self.table("AAA:U R    ")
        run_utils_script("lookup-table-convert-steps-to-step-count.py", str(table))
        self.assertEqual(read_lines(Path(f"{table}.final")), ["AAA:2"])


class ConvertToDictTests(ScratchTableTestCase):
    """utils/lookup-table-convert-to-dict.py writes a python dict literal."""

    def setUp(self):
        super().setUp()
        self.script = load_utils_script("lookup-table-convert-to-dict.py")

    def test_writes_a_dict_that_evaluates_to_the_table(self):
        table = self.table("AAA:U", "BBB:U R")
        self.script.convert_to_dict(str(table))

        written = (self.scratch / "table-dict.py").read_text(encoding="utf-8")
        self.assertEqual(eval(written), {"AAA": "U", "BBB": "U R"})

    def test_an_empty_table_is_an_empty_dict(self):
        table = self.table(name="empty.txt")
        self.script.convert_to_dict(str(table))

        written = (self.scratch / "empty-dict.py").read_text(encoding="utf-8")
        self.assertEqual(eval(written), {})


class CostOnlyTests(ScratchTableTestCase):
    """utils/lookup-table-convert-to-cost-only.py packs depths into hex digits."""

    def setUp(self):
        super().setUp()
        self.script = load_utils_script("lookup-table-convert-to-cost-only.py")

    def test_permutation_rank_of_the_first_permutation_is_zero(self):
        self.assertEqual(self.script.permutation_rank("BBGGGG"), 0)

    def test_permutation_rank_of_the_last_permutation_is_the_count_minus_one(self):
        # 6 choose 2 arrangements of BBGGGG, so the last one ranks 14.
        self.assertEqual(self.script.permutation_rank("GGGGBB"), 14)

    def test_permutation_rank_orders_permutations_consistently(self):
        self.assertEqual(self.script.permutation_rank("GBGGBG"), 7)

    def test_permutation_rank_is_a_bijection_over_one_words_permutations(self):
        # standard libraries
        from itertools import permutations

        ranks = {self.script.permutation_rank("".join(word)) for word in set(permutations("BBGGGG"))}
        self.assertEqual(ranks, set(range(15)))

    def test_permutation_rank_handles_a_long_word(self):
        self.assertEqual(
            self.script.permutation_rank("GGBGBBGBBBGBBBBGGGGGBBBBBGGGGBGGGBGGBGBB"),
            114581417273,
        )

    def test_hex_states_become_one_hex_digit_per_state(self):
        # Consecutive hex states, so no gaps have to be filled in.
        table = self.table("0:U", "1:U R", "2:U R F")
        self.script.convert_to_cost_only(str(table), False, [])
        self.assertEqual((self.scratch / "table.cost-only.txt").read_text(encoding="utf-8"), "123")

    def test_gaps_between_states_are_filled_with_zeroes(self):
        table = self.table("2:U", "5:U R")
        self.script.convert_to_cost_only(str(table), False, [])
        # Zeroes for states 0 and 1, the cost of state 2, zeroes for states 3 and 4,
        # then the cost of state 5.
        self.assertEqual((self.scratch / "table.cost-only.txt").read_text(encoding="utf-8"), "001002")

    def test_a_state_target_costs_nothing(self):
        table = self.table("0:U R F")
        self.script.convert_to_cost_only(str(table), False, ["0"])
        self.assertEqual((self.scratch / "table.cost-only.txt").read_text(encoding="utf-8"), "0")

    def test_a_depth_over_fifteen_is_capped(self):
        # One hex digit per state, so 16 moves cannot be represented.
        table = self.table("0:" + " ".join(["U"] * 16))
        self.script.convert_to_cost_only(str(table), False, [])
        self.assertEqual((self.scratch / "table.cost-only.txt").read_text(encoding="utf-8"), "f")

    def test_a_cost_only_input_is_read_as_a_depth(self):
        table = self.table("0:7")
        self.script.convert_to_cost_only(str(table), False, [])
        self.assertEqual((self.scratch / "table.cost-only.txt").read_text(encoding="utf-8"), "7")


class PrintHistogramTests(ScratchTableTestCase):
    """utils/print-histogram.py summarises how deep a table's entries are."""

    def test_counts_entries_at_each_depth(self):
        table = self.table("AAA:U", "BBB:U R", "CCC:U R", "DDD:U R F")
        completed = run_utils_script("print-histogram.py", str(table))

        self.assertIn("1 steps has 1 entries", completed.stdout)
        self.assertIn("2 steps has 2 entries", completed.stdout)
        self.assertIn("3 steps has 1 entries", completed.stdout)
        self.assertIn("Total: 4 entries", completed.stdout)

    def test_reports_the_average_solution_length(self):
        table = self.table("AAA:U", "BBB:U R F")
        completed = run_utils_script("print-histogram.py", str(table))
        self.assertIn("Average: 2.00 moves", completed.stdout)

    def test_reads_a_cost_only_table(self):
        table = self.table("AAA:2", "BBB:2", "CCC:5")
        completed = run_utils_script("print-histogram.py", str(table))

        self.assertIn("2 steps has 2 entries", completed.stdout)
        self.assertIn("5 steps has 1 entries", completed.stdout)


if __name__ == "__main__":
    unittest.main()

"""Unit tests for the remaining utils/ entry points.

Covers the scripts that are driven entirely from the command line, plus a check
that every script under utils/ is at least importable as valid python.
"""

from __future__ import annotations

# standard libraries
import contextlib
import io
import re
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.script_support import load_utils_script, run_utils_script, utils_scripts, write_lines


class ScratchTestCase(unittest.TestCase):
    """Gives each case a private directory to write files in."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)


class ScriptInventoryTests(unittest.TestCase):
    """Every script under utils/ should stay valid and accounted for."""

    def test_every_script_compiles(self):
        for script in utils_scripts():
            with self.subTest(script=script.name):
                source = script.read_text(encoding="utf-8")
                try:
                    compile(source, str(script), "exec")
                except SyntaxError as error:
                    self.fail(f"{script.name} does not compile: {error}")

    def test_utils_holds_the_scripts_we_expect(self):
        # A new script showing up here is a prompt to give it test coverage.
        self.assertEqual(
            {script.name for script in utils_scripts()},
            {
                "binary-search-lookup.py",
                "build-333-phase3-starting-states.py",
                "build-ida-graph.py",
                "build-perfect-hash.py",
                "builderui.py",
                "convert-pt-state-to-perfect-hash.py",
                "extrapolate.py",
                "gods-number-bound.py",
                "json-combine.py",
                "json-to-binary-display.py",
                "json-to-binary.py",
                "json-to-json-one-line.py",
                "keep-best-solution.py",
                "keep-specific-depth.py",
                "keep-up-to-depth.py",
                "lookup-table-chop-all-but-first-step.py",
                "lookup-table-compress-solution.py",
                "lookup-table-convert-steps-to-step-count.py",
                "lookup-table-convert-to-cost-only.py",
                "lookup-table-convert-to-dict.py",
                "pad-lines.py",
                "print-histogram.py",
                "print-lookup-table-states.py",
                "print-starting-states.py",
                "read-perfect-hash-index.py",
            },
        )


class BuilderUiTests(ScratchTestCase):
    """utils/builderui.py is the entry point the Makefile drives."""

    def test_it_documents_its_arguments(self):
        completed = run_utils_script("builderui.py", "--help")
        for option in ("--depth", "--cores", "--code-gen"):
            with self.subTest(option=option):
                self.assertIn(option, completed.stdout)

    def test_a_builder_name_with_no_cube_size_is_rejected(self):
        completed = run_utils_script("builderui.py", "BuildNothing", expect_success=False)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("we should not be here", completed.stderr)

    def test_an_unknown_builder_for_a_known_size_is_rejected(self):
        completed = run_utils_script("builderui.py", "Build555NoSuchTable", expect_success=False)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("AttributeError", completed.stderr)

    def test_no_builder_at_all_is_rejected(self):
        completed = run_utils_script("builderui.py", expect_success=False)
        self.assertEqual(completed.returncode, 2)
        self.assertIn("required", completed.stderr)

    def test_it_reports_where_the_time_went(self):
        # A tiny table so the run stays quick, checked for the timing summary that
        # every build prints when it finishes.
        completed = run_utils_script("builderui.py", "Build777Step71", "--depth", "2")
        for heading in ("Time in crunching workq", "Time in save", "Time total"):
            with self.subTest(heading=heading):
                self.assertIn(heading, completed.stdout)


class GodsNumberBoundTests(unittest.TestCase):
    """utils/gods-number-bound.py estimates how deep a cube's search goes."""

    def setUp(self):
        self.script = load_utils_script("gods-number-bound.py")

    def test_it_reports_a_depth_for_every_cube_size(self):
        completed = run_utils_script("gods-number-bound.py")
        for size in ("3x3x3", "4x4x4", "5x5x5"):
            with self.subTest(size=size):
                self.assertIn(f"{size} number of states is", completed.stdout)

    def test_it_stops_once_it_covers_every_state(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            # A small state count, so the table only needs a couple of rows.
            self.script.gods_number(2, 18, 100)

        rows = [line for line in buffer.getvalue().splitlines() if line.strip().startswith(("01:", "02:", "03:"))]
        self.assertTrue(rows)

    def test_it_never_counts_more_states_than_exist(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            self.script.gods_number(2, 18, 1000)

        counts = [int(value.replace(",", "")) for value in re.findall(r"^\d\d:\s+([\d,]+)$", buffer.getvalue(), re.M)]
        self.assertLessEqual(sum(counts), 1000)


class ExtrapolateTests(unittest.TestCase):
    """utils/extrapolate.py projects a histogram out to the full state count."""

    def test_it_prints_a_projected_total_and_average(self):
        completed = run_utils_script("extrapolate.py")
        self.assertIn("Total  :", completed.stdout)
        self.assertIn("Average:", completed.stdout)

    def test_it_projects_one_row_per_depth(self):
        completed = run_utils_script("extrapolate.py")
        self.assertIn("steps has", completed.stdout)


class PrintLookupTableStatesTests(ScratchTestCase):
    """utils/print-lookup-table-states.py draws the cube for each entry."""

    def test_it_prints_a_cube_per_entry(self):
        table = write_lines(
            self.scratch / "lookup-table-3x3x3-test.txt",
            ("UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB:U R",),
        )
        completed = run_utils_script("print-lookup-table-states.py", str(table))
        self.assertIn("steps_to_solve", completed.stderr + completed.stdout)

    def test_a_filename_with_no_cube_size_is_rejected(self):
        table = write_lines(self.scratch / "mystery-table.txt", ("AAA:U",))
        completed = run_utils_script("print-lookup-table-states.py", str(table), expect_success=False)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("What size cube?", completed.stderr)


class Build333Phase3StartingStatesTests(ScratchTestCase):
    """utils/build-333-phase3-starting-states.py overlays corners onto a template."""

    def test_it_prints_one_starting_state_per_corners_entry(self):
        # The script reads this exact filename from the working directory.
        write_lines(
            self.scratch / "lookup-table-3x3x3-step142-corners.txt",
            ("DDDDLLLLBBBBRRRRFFFFUUUU:R2 L2", "DDDDLLRRBBFFRRLLFFBBUUUU:D2 R2 L2"),
        )
        completed = run_utils_script("build-333-phase3-starting-states.py", cwd=self.scratch)

        rows = [line for line in completed.stdout.splitlines() if line.strip().startswith("('")]
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row.strip().endswith("'ULFRBD'),") for row in rows))

    def test_each_starting_state_is_the_template_width(self):
        write_lines(
            self.scratch / "lookup-table-3x3x3-step142-corners.txt",
            ("DDDDLLLLBBBBRRRRFFFFUUUU:R2 L2",),
        )
        completed = run_utils_script("build-333-phase3-starting-states.py", cwd=self.scratch)

        # The script prints the template width first, then the states.
        lines = completed.stdout.splitlines()
        width = int(lines[0])
        state = lines[1].strip()[2 : 2 + width]
        self.assertEqual(len(state), width)


class BuildIdaGraphTests(unittest.TestCase):
    """utils/build-ida-graph.py only knows the builders it has branches for."""

    def test_an_unknown_builder_is_rejected(self):
        completed = run_utils_script("build-ida-graph.py", "BuildNothing", expect_success=False)
        self.assertNotEqual(completed.returncode, 0)

    def test_it_needs_a_builder_name(self):
        completed = run_utils_script("build-ida-graph.py", expect_success=False)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("IndexError", completed.stderr)


class PrintStartingStatesTests(unittest.TestCase):
    """utils/print-starting-states.py is driven by a builder name."""

    def test_it_needs_arguments(self):
        completed = run_utils_script("print-starting-states.py", expect_success=False)
        self.assertNotEqual(completed.returncode, 0)


class CompressSolutionTests(ScratchTestCase):
    """utils/lookup-table-compress-solution.py merges repeated moves."""

    def test_it_combines_two_quarter_turns_into_a_half_turn(self):
        table = write_lines(self.scratch / "table.txt", ("AAA:U U",))
        run_utils_script("lookup-table-compress-solution.py", str(table))

        written = (self.scratch / "table.txt.new").read_text(encoding="utf-8")
        self.assertEqual(written.strip(), "AAA:U2")

    def test_a_solution_with_nothing_to_merge_is_unchanged(self):
        table = write_lines(self.scratch / "table.txt", ("AAA:U R F",))
        run_utils_script("lookup-table-compress-solution.py", str(table))

        written = (self.scratch / "table.txt.new").read_text(encoding="utf-8")
        self.assertEqual(written.strip(), "AAA:U R F")

    def test_moves_that_cancel_out_are_removed(self):
        table = write_lines(self.scratch / "table.txt", ("AAA:U U'",))
        run_utils_script("lookup-table-compress-solution.py", str(table))

        written = (self.scratch / "table.txt.new").read_text(encoding="utf-8")
        self.assertEqual(written.strip(), "AAA:")


if __name__ == "__main__":
    unittest.main()

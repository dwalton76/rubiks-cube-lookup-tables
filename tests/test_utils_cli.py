"""Unit tests for utils/builderui.py."""

from __future__ import annotations

# standard libraries
import unittest

# rubiks cube libraries
from tests.script_support import run_utils_script, utils_scripts


class ScriptInventoryTests(unittest.TestCase):
    """utils/ should keep the scripts the build still runs."""

    def test_every_script_compiles(self):
        for script in utils_scripts():
            with self.subTest(script=script.name):
                source = script.read_text(encoding="utf-8")
                try:
                    compile(source, str(script), "exec")
                except SyntaxError as error:
                    self.fail(f"{script.name} does not compile: {error}")

    def test_utils_holds_the_scripts_we_expect(self):
        self.assertEqual({script.name for script in utils_scripts()}, {"builderui.py"})


class BuilderUiTests(unittest.TestCase):
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
        completed = run_utils_script("builderui.py", "Build333MicroPythonPhase2Edges", "--depth", "2")
        for heading in ("Time in crunching workq", "Time in save", "Time total"):
            with self.subTest(heading=heading):
                self.assertIn(heading, completed.stdout)

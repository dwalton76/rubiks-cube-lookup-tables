"""Unit tests for expanding a workq, in Python and in C.

builder-crunch-workq.py and builder-crunch-workq.c both take a padded workq of
cube states and write every legal next state. They name their shard files
differently and the C program is given a linewidth that includes the newline, so
the tests compare the (state, moves) pairs rather than the raw files.
"""

from __future__ import annotations

# standard libraries
import subprocess
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.builder_support import CRUNCHER, REPO_ROOT, ensure_cruncher
from tests.script_support import load_lookup_script

SOLVED_222 = "xUUUURRRRFFFFDDDDLLLLBBBB"
# Wide enough for the solved 2x2x2 plus a couple of moves, plus the newline the C
# cruncher counts as part of --linewidth.
WORKQ_WIDTH = 40
LEGAL_MOVES = ["U", "R", "F"]


class ScratchTestCase(unittest.TestCase):
    """Gives each case a private directory and a loaded Python cruncher."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)
        self.script = load_lookup_script("builder-crunch-workq.py")

    def workq(self, *entries: str) -> Path:
        path = self.scratch / "workq.txt"
        lines = []
        for entry in entries:
            if len(entry) > WORKQ_WIDTH:
                raise AssertionError(f"workq entry {entry!r} is wider than {WORKQ_WIDTH}")
            lines.append(entry + " " * (WORKQ_WIDTH - len(entry)) + "\n")
        path.write_text("".join(lines), encoding="utf-8")
        return path

    def crunch_python(self, workq: Path, start: int, end: int, moves=None) -> dict:
        output = self.scratch / "python-out"
        self.script.crunch_workq(
            "2x2x2",
            str(workq),
            WORKQ_WIDTH,
            start,
            end,
            str(output),
            False,
            list(moves or LEGAL_MOVES),
        )
        return records_from_shards(self.scratch, "python-out.")

    def crunch_c(self, workq: Path, start: int, end: int, moves=None) -> dict:
        ensure_cruncher()
        output = self.scratch / "c-out"
        completed = subprocess.run(
            [
                str(CRUNCHER),
                "--size",
                "2",
                "--inputfile",
                str(workq),
                "--linewidth",
                str(WORKQ_WIDTH + 1),
                "--start",
                str(start),
                "--end",
                str(end),
                "--outputfile",
                str(output),
                "--moves",
                " ".join(moves or LEGAL_MOVES),
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode:
            raise AssertionError(f"C cruncher exited {completed.returncode}\n{completed.stdout}{completed.stderr}")
        return records_from_shards(self.scratch, "c-out-")


def records_from_shards(directory: Path, prefix: str) -> dict:
    """Read every shard into a state -> moves mapping, last write wins."""
    records = {}
    for path in sorted(directory.iterdir()):
        if not path.name.startswith(prefix):
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            state, _, moves = line.partition(":")
            records[state] = moves.strip()
    return records


class ApplyPhaseBinaryTests(ScratchTestCase):
    """The 3x3x3 and 5x5x5 phase encodings that flip a handful of stickers."""

    def test_a_333_zero_becomes_one(self):
        cube = list("x0000")
        self.assertEqual("".join(self.script.apply_333_phase_binary(cube, [1, 4])), "x1001")

    def test_a_333_one_becomes_zero(self):
        cube = list("x1111")
        self.assertEqual("".join(self.script.apply_333_phase_binary(cube, [2])), "x1011")

    def test_other_333_stickers_are_left_alone(self):
        cube = list("xU0R1")
        self.assertEqual("".join(self.script.apply_333_phase_binary(cube, [2, 4])), "xU1R0")

    def test_a_555_U_becomes_D(self):
        cube = list("xUUDD")
        self.assertEqual("".join(self.script.apply_555_phase_binary(cube, [1])), "xDUDD")

    def test_a_555_D_becomes_U(self):
        cube = list("xUUDD")
        self.assertEqual("".join(self.script.apply_555_phase_binary(cube, [4])), "xUUDU")

    def test_other_555_stickers_are_left_alone(self):
        cube = list("xULFR")
        self.assertEqual("".join(self.script.apply_555_phase_binary(cube, [1, 2])), "xDLFR")


class PythonCrunchWorkqTests(ScratchTestCase):
    """What the Python cruncher writes for a tiny 2x2x2 workq."""

    def test_a_starting_state_emits_itself_and_each_legal_move(self):
        records = self.crunch_python(self.workq(f"{SOLVED_222}:"), 0, 0)
        self.assertEqual(records[SOLVED_222], "")
        self.assertEqual(len(records), 1 + len(LEGAL_MOVES))
        self.assertEqual(set(records.values()), {"", "U", "R", "F"})

    def test_a_move_on_the_same_face_is_not_repeated(self):
        records = self.crunch_python(self.workq(f"{SOLVED_222}:U"), 0, 0)
        self.assertNotIn("U", records.values())
        self.assertIn("U R", records.values())
        self.assertIn("U F", records.values())

    def test_only_the_requested_lines_are_expanded(self):
        first = f"{SOLVED_222}:"
        # A second line that already has a move, so its children are distinct.
        second = f"{SOLVED_222}:U"
        records = self.crunch_python(self.workq(first, second), 1, 1)
        self.assertTrue(all(moves.startswith("U") for moves in records.values() if moves))
        self.assertNotIn("", records.values())

    def test_an_unknown_cube_size_is_rejected(self):
        with self.assertRaises(AssertionError):
            self.script.crunch_workq("9x9x9", "unused", 10, 0, 0, "unused", False, ["U"])


class CrunchWorkqParityTests(ScratchTestCase):
    """The C cruncher and the Python cruncher agree on the states they reach."""

    def test_a_starting_state_produces_the_same_records(self):
        workq = self.workq(f"{SOLVED_222}:")
        self.assertEqual(self.crunch_python(workq, 0, 0), self.crunch_c(workq, 0, 0))

    def test_a_line_that_already_has_a_move_produces_the_same_records(self):
        workq = self.workq(f"{SOLVED_222}:U")
        self.assertEqual(self.crunch_python(workq, 0, 0), self.crunch_c(workq, 0, 0))

    def test_a_two_line_workq_produces_the_same_records(self):
        workq = self.workq(f"{SOLVED_222}:", f"{SOLVED_222}:U")
        self.assertEqual(self.crunch_python(workq, 0, 1), self.crunch_c(workq, 0, 1))

    def test_restricting_the_line_range_produces_the_same_records(self):
        workq = self.workq(f"{SOLVED_222}:", f"{SOLVED_222}:U")
        self.assertEqual(self.crunch_python(workq, 1, 1), self.crunch_c(workq, 1, 1))


class CCruncherCliTests(ScratchTestCase):
    """builder-crunch-workq's argument handling."""

    def run_c(self, *arguments: str) -> subprocess.CompletedProcess:
        ensure_cruncher()
        return subprocess.run(
            [str(CRUNCHER), *arguments],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_help_exits_cleanly(self):
        completed = self.run_c("--help")
        self.assertEqual(completed.returncode, 0)

    def test_an_unknown_flag_is_rejected(self):
        completed = self.run_c("--not-a-flag")
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("invalid arg", completed.stdout)

    def test_a_missing_linewidth_is_rejected(self):
        completed = self.run_c("--size", "2", "--inputfile", "x", "--outputfile", "y", "--moves", "U")
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must specify --linewidth", completed.stdout)

    def test_an_unsupported_cube_size_is_rejected(self):
        completed = self.run_c(
            "--size", "9", "--linewidth", "10", "--inputfile", "x", "--outputfile", "y", "--moves", "U"
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("only 2x2x2 through 7x7x7", completed.stdout)


if __name__ == "__main__":
    unittest.main()

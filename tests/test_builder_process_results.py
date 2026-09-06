#!/usr/bin/env python3

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROCESSOR = REPO_ROOT / "rubikscubelookuptables" / "builder-process-results"


class ProcessorFixture:
    def __init__(self, root: Path):
        self.root = root

    def write(self, name: str, contents: str) -> Path:
        path = self.root / name
        path.write_text(contents, encoding="ascii")
        return path

    def manifest(self, *paths: Path) -> Path:
        path = self.root / "files0"
        path.write_bytes(b"\0".join(os.fsencode(item) for item in paths))
        return path

    def run(self, *args: object) -> subprocess.CompletedProcess:
        return subprocess.run(
            [str(PROCESSOR), *(str(arg) for arg in args)],
            check=False,
            capture_output=True,
            text=True,
        )


@unittest.skipUnless(PROCESSOR.exists(), "build builder-process-results first")
class BuilderProcessResultsTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.fixture = ProcessorFixture(self.root)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_regular_merge_join_and_workq(self):
        table = self.fixture.write("table", "AAA:D\nCCC:F\nGGG:R\n")
        shard_a = self.fixture.write("a", "AAA:U\nBBB:U2\nDDD:L F'\n")
        shard_b = self.fixture.write("b", "BBB:D\nCCC:R\nEEE:Uw2\n")
        manifest = self.fixture.manifest(shard_a, shard_b)
        output = self.root / "output"
        workq = self.root / "workq"

        result = self.fixture.run(
            "--format",
            "regular",
            "--table",
            table,
            "--files0-from",
            manifest,
            "--output-table",
            output,
            "--workq",
            workq,
            "--linewidth",
            20,
            "--buffer-size",
            "16M",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "3 8")
        self.assertEqual(
            output.read_text(encoding="ascii"),
            "AAA:D\nBBB:D'\nCCC:F\nDDD:F L'\nEEE:Uw2\nGGG:R\n",
        )
        self.assertEqual(
            workq.read_text(encoding="ascii"),
            "BBB:D               \nDDD:L F'            \nEEE:Uw2             \n",
        )

    def test_regular_winner_is_deterministic_across_manifest_order(self):
        table = self.fixture.write("table", "")
        shard_a = self.fixture.write("a", "AAA:U2\n")
        shard_b = self.fixture.write("b", "AAA:D\n")

        outputs = []
        for index, paths in enumerate(((shard_a, shard_b), (shard_b, shard_a))):
            manifest = self.root / f"files{index}"
            manifest.write_bytes(b"\0".join(os.fsencode(item) for item in paths))
            output = self.root / f"output{index}"
            result = self.fixture.run(
                "--format",
                "regular",
                "--table",
                table,
                "--files0-from",
                manifest,
                "--output-table",
                output,
                "--buffer-size",
                "16M",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            outputs.append(output.read_bytes())

        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(outputs[0], b"AAA:D'\n")

    def test_edges_use_pattern_membership_and_one_representative(self):
        table = self.fixture.write("table", "P1:OLDSTATE:U\nP4:LASTSTATE:F\n")
        shard_a = self.fixture.write(
            "a",
            "P1:NEWSTATE:D\nP2:AAASTATE:U L\nP2:BBBSTATE:F\nP3:CCCSTATE:Uw2\n",
        )
        shard_b = self.fixture.write(
            "b",
            "P2:AAASTATE:R\nP2:BBBSTATE:D L\nP3:DDDSTATE:U F\n",
        )
        manifest = self.fixture.manifest(shard_a, shard_b)
        output = self.root / "output"
        workq = self.root / "workq"

        result = self.fixture.run(
            "--format",
            "edges",
            "--table",
            table,
            "--files0-from",
            manifest,
            "--output-table",
            output,
            "--workq",
            workq,
            "--linewidth",
            24,
            "--buffer-size",
            "16M",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "2 15")
        self.assertEqual(
            output.read_text(encoding="ascii"),
            "P1:OLDSTATE:U\nP2:AAASTATE:R'\nP3:CCCSTATE:Uw2\nP4:LASTSTATE:F\n",
        )
        self.assertEqual(
            workq.read_text(encoding="ascii"),
            "P2:AAASTATE:R           \nP3:CCCSTATE:Uw2         \n",
        )

    def test_merge_only_deduplicates_without_reversing_moves(self):
        shard_a = self.fixture.write("a", "AAA:U2\nBBB:F\n")
        shard_b = self.fixture.write("b", "AAA:D\nCCC:R\n")
        manifest = self.fixture.manifest(shard_a, shard_b)
        output = self.root / "output"

        result = self.fixture.run(
            "--format",
            "regular",
            "--files0-from",
            manifest,
            "--merge-only-output",
            output,
            "--buffer-size",
            "16M",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(output.read_text(encoding="ascii"), "AAA:D\nBBB:F\nCCC:R\n")

    def test_empty_manifest_copies_table(self):
        table = self.fixture.write("table", "AAA:U\nBBB:D\n")
        manifest = self.fixture.manifest()
        output = self.root / "output"

        result = self.fixture.run(
            "--format",
            "regular",
            "--table",
            table,
            "--files0-from",
            manifest,
            "--output-table",
            output,
            "--buffer-size",
            "16M",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "0 0")
        self.assertEqual(output.read_bytes(), table.read_bytes())

    def test_rejects_unsorted_shard(self):
        table = self.fixture.write("table", "")
        shard = self.fixture.write("shard", "BBB:U\nAAA:D\n")
        manifest = self.fixture.manifest(shard)

        result = self.fixture.run(
            "--format",
            "regular",
            "--table",
            table,
            "--files0-from",
            manifest,
            "--output-table",
            self.root / "output",
            "--buffer-size",
            "16M",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("sorted", result.stderr.lower())


if __name__ == "__main__":
    unittest.main()

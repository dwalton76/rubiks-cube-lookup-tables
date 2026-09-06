"""Unit tests for the utils/ scripts that deal with the IDA graph JSON and .bin files."""

from __future__ import annotations

# standard libraries
import contextlib
import io
import json
import struct
import tempfile
import unittest
from pathlib import Path

# rubiks cube libraries
from tests.script_support import load_utils_script, run_utils_script

# Two states joined by a single legal move, which is the smallest graph that still
# has an edge to encode.
GRAPH = {
    "aa": {"cost": 1, "edges": {"U": "bb"}},
    "bb": {"cost": 0, "edges": {"U": "aa"}},
}


class ScratchTestCase(unittest.TestCase):
    """Gives each case a private directory to write files in."""

    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.scratch = Path(self._scratch.name)


class JsonToOneLineTests(ScratchTestCase):
    """utils/json-to-json-one-line.py collapses a JSON file onto one line."""

    def setUp(self):
        super().setUp()
        self.script = load_utils_script("json-to-json-one-line.py")

    def one_line(self, text: str) -> str:
        source = self.scratch / "graph.json"
        source.write_text(text, encoding="utf-8")
        self.script.convert_json_to_json_one_line(str(source))
        return (self.scratch / "graph.json-one-line").read_text(encoding="utf-8")

    def test_result_is_a_single_line(self):
        result = self.one_line(json.dumps(GRAPH, indent=2))
        self.assertEqual(result.count("\n"), 1)
        self.assertTrue(result.endswith("\n"))

    def test_content_still_parses_as_the_same_json(self):
        result = self.one_line(json.dumps(GRAPH, indent=2))
        self.assertEqual(json.loads(result), GRAPH)

    def test_blank_lines_are_dropped(self):
        result = self.one_line('{\n\n  "a": 1\n\n}\n')
        self.assertEqual(json.loads(result), {"a": 1})

    def test_an_already_one_line_file_is_unchanged(self):
        result = self.one_line('{"a": 1}\n')
        self.assertEqual(result, '{"a": 1}\n')


class JsonCombineTests(ScratchTestCase):
    """utils/json-combine.py stitches partial JSON files into one object."""

    def setUp(self):
        super().setUp()
        self.script = load_utils_script("json-combine.py")

    def part(self, name: str, body: str) -> Path:
        # Each part is a standalone JSON object. The script drops the first and last
        # line of every part, which is where the braces live.
        path = self.scratch / name
        path.write_text("{\n" + body + "\n}\n", encoding="utf-8")
        return path

    def test_combines_the_parts_into_one_object(self):
        base = self.part("graph.json", '"cc": 3')
        self.part("graph.json.1", '"aa": 1')
        self.part("graph.json.2", '"bb": 2')

        self.script.json_combine_files(str(base))
        self.assertEqual(json.loads(base.read_text(encoding="utf-8")), {"aa": 1, "bb": 2, "cc": 3})

    def test_the_base_file_is_written_last(self):
        # The base file sorts first but is moved to the end, so its entries land
        # after the numbered parts.
        base = self.part("graph.json", '"cc": 3')
        self.part("graph.json.1", '"aa": 1')

        self.script.json_combine_files(str(base))
        text = base.read_text(encoding="utf-8")
        self.assertLess(text.index('"aa"'), text.index('"cc"'))

    def test_the_parts_are_deleted(self):
        base = self.part("graph.json", '"cc": 3')
        part = self.part("graph.json.1", '"aa": 1')

        self.script.json_combine_files(str(base))
        self.assertFalse(part.exists())
        self.assertTrue(base.exists())

    def test_a_single_file_round_trips(self):
        base = self.part("graph.json", '"aa": 1')
        self.script.json_combine_files(str(base))
        self.assertEqual(json.loads(base.read_text(encoding="utf-8")), {"aa": 1})


class JsonToBinaryTests(ScratchTestCase):
    """utils/json-to-binary.py packs the graph into fixed width records."""

    def setUp(self):
        super().setUp()
        self.script = load_utils_script("json-to-binary.py")
        self.source = self.scratch / "graph.json"
        self.source.write_text(json.dumps(GRAPH), encoding="utf-8")
        (self.scratch / "graph.state_index").write_text("aa:0\nbb:1\n", encoding="utf-8")

    def convert(self) -> bytes:
        self.script.convert_json_to_binary(str(self.source), True)
        return (self.scratch / "graph.bin").read_bytes()

    def test_each_record_holds_a_cost_and_one_edge(self):
        # One cost byte, then a 4 byte state index and a 1 byte cost per legal move.
        self.assertEqual(len(self.convert()), 2 * (1 + 5))

    def test_the_cost_comes_first(self):
        data = self.convert()
        self.assertEqual(data[0], GRAPH["aa"]["cost"])
        self.assertEqual(data[6], GRAPH["bb"]["cost"])

    def test_an_edge_points_at_the_next_states_index(self):
        data = self.convert()
        self.assertEqual(struct.unpack("<L", data[1:5])[0], 1)
        self.assertEqual(struct.unpack("<L", data[7:11])[0], 0)

    def test_an_edge_carries_the_next_states_cost(self):
        data = self.convert()
        self.assertEqual(data[5], GRAPH["bb"]["cost"])
        self.assertEqual(data[11], GRAPH["aa"]["cost"])

    def test_records_follow_the_state_index_file_order(self):
        (self.scratch / "graph.state_index").write_text("bb:1\naa:0\n", encoding="utf-8")
        data = self.convert()
        self.assertEqual(data[0], GRAPH["bb"]["cost"])


class JsonToBinaryDisplayTests(ScratchTestCase):
    """utils/json-to-binary-display.py decodes one record back into text."""

    ROW_LENGTH = 1 + (4 + 1)

    # Two records: state 0 costs 1 and steps to state 1, which costs 0 and steps back.
    BINDATA = (
        struct.pack("B", 1)
        + struct.pack("<L", 1)
        + struct.pack("B", 0)
        + struct.pack("B", 0)
        + struct.pack("<L", 0)
        + struct.pack("B", 1)
    )

    def setUp(self):
        super().setUp()
        self.script = load_utils_script("json-to-binary-display.py")

    def print_node(self, state_index: int) -> str:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            self.script.print_node({0: "aa", 1: "bb"}, ["U"], self.ROW_LENGTH, self.BINDATA, state_index)
        return buffer.getvalue()

    def test_prints_the_state_and_its_cost(self):
        self.assertIn("state 000000 (aa) cost 1", self.print_node(0))

    def test_prints_where_each_move_leads_and_what_it_costs(self):
        self.assertIn("U    -> 000001 (bb) with cost 0", self.print_node(0))

    def test_seeks_to_the_record_for_a_later_state(self):
        printed = self.print_node(1)
        self.assertIn("state 000001 (bb) cost 0", printed)
        self.assertIn("U    -> 000000 (aa) with cost 1", printed)


class BinaryRoundTripTests(ScratchTestCase):
    """A graph written by json-to-binary.py reads back through the display CLI."""

    def test_the_cli_displays_a_state_written_by_the_writer(self):
        source = self.scratch / "graph.json"
        source.write_text(json.dumps(GRAPH), encoding="utf-8")
        (self.scratch / "graph.state_index").write_text("aa:0\nbb:1\n", encoding="utf-8")

        load_utils_script("json-to-binary.py").convert_json_to_binary(str(source), True)

        completed = run_utils_script(
            "json-to-binary-display.py",
            str(source),
            str(self.scratch / "graph.bin"),
            "0",
        )
        self.assertIn("(aa) cost 1", completed.stdout)

    def test_the_cli_rejects_a_missing_file(self):
        completed = run_utils_script(
            "json-to-binary-display.py",
            str(self.scratch / "absent.json"),
            str(self.scratch / "absent.bin"),
            "0",
            expect_success=False,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("FileNotFoundError", completed.stderr)


if __name__ == "__main__":
    unittest.main()

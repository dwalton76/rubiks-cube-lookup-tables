#!/usr/bin/env python3
"""Record the table signature each Makefile builder produces at its test depth.

Run this only to (re)create tests/builder_table_baselines.json, and only against a
revision whose tables are known good. The test cases read that file but never
update it.

Each builder is tried at FAST_DEPTH first. Builders that do not finish quickly are
recorded at BASE_DEPTH instead. Builds run one at a time because they all stage
intermediate files in ./tmp.
"""

from __future__ import annotations

# standard libraries
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

# third party libraries
from builder_support import (
    BASE_DEPTH,
    BASELINES_PATH,
    FAST_DEPTH,
    FAST_DEPTH_TIMEOUT,
    SKIPPED_BUILDERS,
    build_table,
    builder_output_path,
    makefile_builder_names,
    read_table,
)


def record_builder(name: str, base_depth: int, fast_depth: int, fast_timeout: float) -> Dict[str, object]:
    """Build one table at the deepest depth it can reach quickly."""
    depth = fast_depth
    status, output, timed_out = build_table(name, depth=depth, timeout=fast_timeout)

    if timed_out:
        print(f"  depth {fast_depth} exceeded {fast_timeout}s, falling back to depth {base_depth}", flush=True)
        depth = base_depth
        status, output, timed_out = build_table(name, depth=depth)

    if timed_out:
        raise RuntimeError(f"{name} timed out at depth {depth}; add it to SKIPPED_BUILDERS")

    if status:
        raise RuntimeError(f"{name} failed at depth {depth} with status {status}:\n{output}")

    output_path = builder_output_path(name)

    if not output_path.is_file():
        raise RuntimeError(f"{name} did not write {output_path}")

    facts = read_table(output_path, depth=depth)
    signature = facts.pinned()
    signature["depth"] = depth
    return signature


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("builders", nargs="*", help="Builders to record; defaults to every Makefile call")
    parser.add_argument("--base-depth", type=int, default=BASE_DEPTH)
    parser.add_argument("--fast-depth", type=int, default=FAST_DEPTH)
    parser.add_argument("--fast-timeout", type=float, default=FAST_DEPTH_TIMEOUT)
    parser.add_argument("--output", default=BASELINES_PATH, type=Path)
    parser.add_argument("--replace", action="store_true", help="Discard existing baselines instead of merging")
    args = parser.parse_args(argv)

    requested = args.builders or [name for name in makefile_builder_names() if name not in SKIPPED_BUILDERS]
    signatures: Dict[str, object] = {}

    if args.output.exists() and not args.replace:
        signatures.update(json.loads(args.output.read_text(encoding="utf-8")))

    for index, name in enumerate(requested, 1):
        print(f"[{index}/{len(requested)}] {name}", flush=True)
        try:
            signature = record_builder(name, args.base_depth, args.fast_depth, args.fast_timeout)
        except RuntimeError as error:
            print(f"  {error}", file=sys.stderr)
            return 1

        signatures[name] = signature
        args.output.write_text(json.dumps(dict(sorted(signatures.items())), indent=2) + "\n", encoding="utf-8")
        per_depth = " ".join(f"{depth}:{count:,}" for depth, count in signature["states_per_depth"].items())
        print(f"  depth {signature['depth']}, {signature['lines']:,} lines, states per depth {per_depth}", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

"""Shared infrastructure for the lookup-table builder test cases.

This module holds no test cases of its own. Builders all stage intermediate files
in ./tmp, so only one builder may run at a time; nothing here may be used to run
builds concurrently.
"""

from __future__ import annotations

# standard libraries
import gzip
import hashlib
import importlib
import logging
import os
import re
import shutil
import signal
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
MAKEFILE = REPO_ROOT / "Makefile"
BUILDER_UI = REPO_ROOT / "utils" / "builderui.py"
CRUNCHER = REPO_ROOT / "rubikscubelookuptables" / "builder-crunch-workq"
PAD_LINES = REPO_ROOT / "utils" / "pad-lines"
BASELINES_PATH = Path(__file__).with_name("builder_table_baselines.json")
BUILDER_CALL = re.compile(r"^\s*\./utils/builderui\.py\s+(Build\w+)(?:\s+.*)?$")

# Depth every table is verified at. Builders that reach FAST_DEPTH quickly are
# recorded at that depth instead, which exercises more of the search.
BASE_DEPTH = 2
FAST_DEPTH = 4

# How long a builder may take at FAST_DEPTH before it is recorded at BASE_DEPTH.
FAST_DEPTH_TIMEOUT = 15

# How long any single build may run before it is treated as a failure.
BUILD_TIMEOUT = 300

# Builders whose starting states are too large to build at a test depth. They are
# listed rather than dropped so the coverage test still accounts for every
# builderui call in the Makefile.
SKIPPED_BUILDERS = {
    "Build555Phase4": "starting states are too large to build at a test depth",
    "Build777Phase4LeftRightOblique": "starting states are too large to build at a test depth",
    "Build777Phase4LeftMiddleOblique": "starting states are too large to build at a test depth",
}


def solver_path() -> Path:
    """Where the external rubikscubennnsolver package lives."""
    override = os.environ.get("RUBIKS_CUBE_SOLVER")
    if override:
        return Path(override)
    return REPO_ROOT.parent / "rubiks-cube-NxNxN-solver"


def ensure_importable() -> None:
    """Put this repo and the external solver on sys.path.

    The builder modules import rubikscubennnsolver, which lives outside this repo.
    Doing this here means the tests do not need a preset PYTHONPATH.
    """
    for candidate in (REPO_ROOT, solver_path()):
        entry = str(candidate)
        if entry not in sys.path:
            sys.path.insert(0, entry)


def ensure_starting_state_modules() -> None:
    """Expand the checked-in generated starting-state modules when needed."""
    package_dir = REPO_ROOT / "rubikscubelookuptables"
    for name in ("builder555ss.py", "builder777ss.py"):
        module = package_dir / name
        archive = module.with_suffix(module.suffix + ".gz")
        if not module.exists() and archive.exists():
            with gzip.open(archive, "rb") as source, module.open("wb") as destination:
                shutil.copyfileobj(source, destination)


def makefile_builder_names() -> List[str]:
    """Return each builderui class named by the Makefile, in Makefile order."""
    names = []
    for line in MAKEFILE.read_text(encoding="utf-8").splitlines():
        match = BUILDER_CALL.match(line)
        if match:
            names.append(match.group(1))
    return names


def builder_class(name: str):
    """Import a builder class using builderui's class-name convention."""
    ensure_importable()
    ensure_starting_state_modules()
    # Match builderui's precedence. Some class names describe reducing a larger cube
    # to 3x3x3 and therefore contain more than one size.
    for size in ("777", "666", "555", "444", "333", "222"):
        if size in name:
            module = importlib.import_module(f"rubikscubelookuptables.builder{size}")
            return getattr(module, name)
    raise ValueError(f"cannot determine cube size from builder class {name!r}")


def builder_output_path(name: str) -> Path:
    """Return the primary lookup-table path written by a builder."""
    previous_disable_level = logging.root.manager.disable
    logging.disable(logging.CRITICAL)
    try:
        builder = builder_class(name)()
    finally:
        logging.disable(previous_disable_level)
    return REPO_ROOT / builder.filename


@dataclass
class TableFacts:
    """Everything the tests check about a built lookup-table.

    Split into two groups on purpose. The pinned values are decided by the breadth
    first search itself and so are reproducible. The structural values are checked
    for self consistency but are not pinned, because which of several equally short
    solutions gets stored depends on how many intermediate files the sort saw, and
    that changes with --cores. That also makes a whole-file md5, the byte count, and
    the padding width unsuitable as expectations.
    """

    filename: str
    lines: int
    states_per_depth: Dict[str, int]
    states_md5: str
    line_widths: Tuple[int, ...]
    sorted_by_state: bool
    conflicting_state: Optional[str]
    solution_over_depth: Optional[str]

    def pinned(self) -> Dict[str, object]:
        """The subset recorded in, and compared against, the baselines file."""
        return {
            "filename": self.filename,
            "lines": self.lines,
            "states_per_depth": self.states_per_depth,
            "states_md5": self.states_md5,
        }


def read_table(path: Path, depth: Optional[int] = None) -> TableFacts:
    """Measure a built lookup-table in a single pass.

    Every line is "state:moves" with the moves padded to a fixed width, so the
    number of whitespace separated moves gives the depth that state sits at.
    """
    digest = hashlib.md5()
    states_per_depth: Counter = Counter()
    widths = set()
    line_count = 0
    previous_state = None
    previous_move_count = None
    sorted_by_state = True
    conflicting_state = None
    solution_over_depth = None

    with path.open("rb") as table:
        for raw_line in table:
            line_count += 1
            line = raw_line.rstrip(b"\r\n")
            widths.add(len(line))
            state, separator, moves = line.rpartition(b":")

            if not separator:
                raise ValueError(f"{path} line {line_count} has no ':' separator: {raw_line!r}")
            if not state:
                raise ValueError(f"{path} line {line_count} has an empty state: {raw_line!r}")

            move_count = len(moves.split())

            # The solver binary searches this file, so the state column has to be
            # sorted. A state may legitimately appear twice, because some builders
            # start from a list of starting states that includes the same state more
            # than once, but those repeats have to agree on the depth or a lookup
            # would return a different answer depending on which line it landed on.
            if previous_state is not None:
                if state < previous_state:
                    sorted_by_state = False
                elif state == previous_state and move_count != previous_move_count and conflicting_state is None:
                    conflicting_state = state.decode("ascii", "replace")

            previous_state = state
            previous_move_count = move_count
            digest.update(state)
            digest.update(b"\n")

            states_per_depth[move_count] += 1

            if depth is not None and move_count > depth and solution_over_depth is None:
                solution_over_depth = line.decode("ascii", "replace")

    return TableFacts(
        filename=str(path.relative_to(REPO_ROOT)).replace(os.sep, "/"),
        lines=line_count,
        # Keyed by string because this round-trips through JSON. Depth 0 is the
        # starting states, which reach themselves in no moves.
        states_per_depth={str(value): states_per_depth[value] for value in sorted(states_per_depth)},
        states_md5=digest.hexdigest(),
        line_widths=tuple(sorted(widths)),
        sorted_by_state=sorted_by_state,
        conflicting_state=conflicting_state,
        solution_over_depth=solution_over_depth,
    )


def builder_environment() -> Dict[str, str]:
    """Build an environment where helper scripts use the active interpreter."""
    environment = os.environ.copy()
    # Do not resolve the executable: venv/bin/python is normally a symlink to the
    # system interpreter, but helper scripts need venv/bin at the front of PATH.
    scripts_dir = str(Path(sys.executable).parent)
    environment["PATH"] = scripts_dir + os.pathsep + environment.get("PATH", "")
    environment["PYTHONPATH"] = os.pathsep.join((str(REPO_ROOT), str(solver_path()), environment.get("PYTHONPATH", "")))
    return environment


def ensure_cruncher() -> None:
    """Build the C cruncher that every builder shells out to."""
    sources = [
        REPO_ROOT / "rubikscubelookuptables" / name
        for name in ("builder-crunch-workq.c", "ida_search_core.c", "rotate_xxx.c")
    ]
    newest_source = max(path.stat().st_mtime for path in sources)

    if CRUNCHER.exists() and CRUNCHER.stat().st_mtime >= newest_source:
        return

    result = subprocess.run(
        ["gcc", "-O3", "-o", str(CRUNCHER), *(str(path) for path in sources), "-lm"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(f"could not build {CRUNCHER}:\n{result.stdout}{result.stderr}")


def ensure_pad_lines() -> None:
    """Build the C pad-lines helper that save() and a few utils scripts call."""
    source = REPO_ROOT / "utils" / "pad-lines.c"

    if PAD_LINES.exists() and PAD_LINES.stat().st_mtime >= source.stat().st_mtime:
        return

    result = subprocess.run(
        ["gcc", "-O3", "-o", str(PAD_LINES), str(source)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(f"could not build {PAD_LINES}:\n{result.stdout}{result.stderr}")


def build_table(
    name: str,
    depth: int = BASE_DEPTH,
    cores: int = 4,
    timeout: Optional[float] = BUILD_TIMEOUT,
) -> Tuple[int, str, bool]:
    """Build one table, returning its exit status, output, and whether it timed out.

    Builders stage files in ./tmp, so callers must never run two of these at once.
    """
    ensure_starting_state_modules()
    ensure_cruncher()
    ensure_pad_lines()

    # builderui spawns crunchers of its own, so give the build its own process group
    # and signal the whole group. Killing only builderui would orphan those children
    # and let them keep writing into ./tmp.
    process = subprocess.Popen(
        [sys.executable, str(BUILDER_UI), name, "--depth", str(depth), "--cores", str(cores)],
        cwd=REPO_ROOT,
        env=builder_environment(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        start_new_session=True,
    )

    try:
        output, _ = process.communicate(timeout=timeout)
        return process.returncode, output, False
    except subprocess.TimeoutExpired:
        _terminate_group(process)
        output, _ = process.communicate()
        return process.returncode, output or "", True


def _terminate_group(process: subprocess.Popen) -> None:
    """Stop a build and every cruncher it started."""
    for send_signal in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(os.getpgid(process.pid), send_signal)
        except (ProcessLookupError, PermissionError):
            return
        try:
            process.wait(timeout=10)
            return
        except subprocess.TimeoutExpired:
            continue

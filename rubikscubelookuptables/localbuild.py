"""Build lookup tables for one cube size.

``python -m rubikscubelookuptables.localbuild 444`` builds every 4x4x4 table
into ``RUBIKS_LOOKUP_TABLE_DIR`` (or ``lookup-tables/``). The solver's
``make 444-tables`` target is that command. A file that is already present is
left alone.

The build runs with the lookup-tables repo as its working directory, because
the cruncher binaries are invoked as ./rubikscubelookuptables/<tool>.
"""

# standard libraries
import argparse
import importlib
import inspect
import logging
import os
import shutil
import subprocess
import threading
from pathlib import Path

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS, TMPDIR

log = logging.getLogger(__name__)

_LOCK = threading.Lock()
_BY_NAME = {}
_HEAVY_555 = False

# builder555.Build555Phase4 imports the 61MB generated starting-state module.
_HEAVY_555_CLASSES = {"Build555Phase4", "StartingStatesBuild555Phase4"}

_SIZE_MODULES = (
    ("2x2x2", "rubikscubelookuptables.builder333"),
    ("3x3x3", "rubikscubelookuptables.builder333"),
    ("4x4x4", "rubikscubelookuptables.builder444"),
    ("5x5x5", "rubikscubelookuptables.builder555"),
    ("6x6x6", "rubikscubelookuptables.builder666"),
    ("7x7x7", "rubikscubelookuptables.builder777"),
)

# The solver Makefile calls this module with 333, 444, 555, 666, or 777.
_SIZE_ALIASES = {
    "333": "3x3x3",
    "3x3x3": "3x3x3",
    "444": "4x4x4",
    "4x4x4": "4x4x4",
    "555": "5x5x5",
    "5x5x5": "5x5x5",
    "666": "6x6x6",
    "6x6x6": "6x6x6",
    "777": "7x7x7",
    "7x7x7": "7x7x7",
}

# Written by the C bar search, not a BFS class. A 6x6 solve loads it.
LR_BAR_FILENAME = "lookup-table-6x6x6-phase2-LR-oblique-bars.sym-depth3.hash.bin"


def build_table_if_needed(filename: str) -> None:
    """Build ``filename`` when it is absent. An existing file is left alone."""
    path = Path(filename)
    if not path.is_absolute():
        path = Path.cwd() / path
    path = path.resolve()
    if path.exists():
        return

    with _LOCK:
        if path.exists():
            return
        builder_cls = builder_for(path.name)
        log.info("building %s with %s", path.name, builder_cls.__name__)
        _build(builder_cls, path.parent)
        if not path.exists():
            raise RuntimeError(f"{builder_cls.__name__} finished without writing {path}")


def normalize_size(size: str) -> str:
    """Return the ``4x4x4`` marker for ``444``, ``4x4x4``, or ``444-tables``."""
    token = size.strip().lower().removesuffix("-tables")
    try:
        return _SIZE_ALIASES[token]
    except KeyError:
        raise ValueError(f"unknown cube size {size!r}; use 333, 444, 555, 666, or 777") from None


def builders_for_size(size: str):
    """Return every builder class that writes a table for ``size``.

    ``StartingStates*`` classes write an intermediate the generated phase-4
    module already contains. The 6x6 LR bar file is built separately.
    """
    marker = normalize_size(size)
    module_name = dict(_SIZE_MODULES)[marker]
    module = importlib.import_module(module_name)
    classes = []
    for cls in _builder_classes(module):
        if cls.__name__.startswith("Starting"):
            continue
        classes.append(cls)
    return classes


def build_tables(size: str) -> None:
    """Build every missing table for ``size`` into the requested directory."""
    marker = normalize_size(size)
    output_dir = Path(os.environ.get("RUBIKS_LOOKUP_TABLE_DIR") or "lookup-tables")
    if not output_dir.is_absolute():
        output_dir = (Path.cwd() / output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    for cls in builders_for_size(marker):
        if _outputs_exist(cls, output_dir):
            log.info("%s already built", cls.__name__)
            continue
        log.info("building %s", cls.__name__)
        _build(cls, output_dir)
    if marker == "6x6x6":
        _build_666_bars(output_dir)


def builder_for(basename: str):
    """Return the builder class that writes ``basename``."""
    if basename not in _BY_NAME:
        _index(basename)
    try:
        return _BY_NAME[basename]
    except KeyError:
        raise LookupError(f"no lookup-table builder writes {basename}") from None


def _index(basename: str) -> None:
    global _HEAVY_555

    include_heavy = "step40" in basename or basename.startswith("starting-states-")
    for marker, module_name in _SIZE_MODULES:
        if marker not in basename:
            continue
        module = importlib.import_module(module_name)
        for cls in _builder_classes(module):
            heavy = cls.__name__ in _HEAVY_555_CLASSES
            if heavy and not include_heavy:
                continue
            if heavy and _HEAVY_555:
                continue
            _remember(cls)
        if include_heavy:
            _HEAVY_555 = True
        return
    for module_name in dict(_SIZE_MODULES).values():
        module = importlib.import_module(module_name)
        for cls in _builder_classes(module):
            if cls.__name__ in _HEAVY_555_CLASSES:
                continue
            _remember(cls)


def _builder_classes(module):
    classes = []
    for name, cls in inspect.getmembers(module, inspect.isclass):
        if name.startswith("_") or cls.__module__ != module.__name__ or not issubclass(cls, BFS):
            continue
        parameters = [
            parameter
            for parameter in inspect.signature(cls.__init__).parameters.values()
            if parameter.name != "self"
            and parameter.default is inspect.Parameter.empty
            and parameter.kind in (parameter.POSITIONAL_ONLY, parameter.POSITIONAL_OR_KEYWORD)
        ]
        if parameters:
            continue
        classes.append(cls)
    return classes


def _remember(cls) -> None:
    try:
        builder = cls()
    except Exception:
        log.warning("lookup-table builder %s could not be constructed", cls.__name__, exc_info=True)
        return
    for name in _products(builder):
        previous = _BY_NAME.get(name)
        if previous is not None and previous is not cls:
            raise RuntimeError(f"{name} is built by both {previous.__name__} and {cls.__name__}")
        _BY_NAME[name] = cls


def _products(builder):
    source = Path(builder.filename)
    names = {source.name}
    if builder.use_ranked_cost and not getattr(builder, "orbit_parity_even_filename", None):
        cost = source.with_suffix(".cost-only.bin").name
        names.add(cost)
        names.add(cost + ".json")
        if builder.ranked_cost_type == "center-symmetry-444":
            names.add(cost + ".symmetry-index.bin")
    for extra in (builder.orbit_parity_even_filename, builder.orbit_parity_odd_filename):
        if extra:
            names.add(Path(extra).name)
    return names


def _build(builder_cls, output_dir: Path) -> None:
    repo = Path(__file__).resolve().parent.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    _compile_helpers(repo)
    previous_dir = os.environ.get("RUBIKS_LOOKUP_TABLE_DIR")
    previous_cwd = Path.cwd()
    os.environ["RUBIKS_LOOKUP_TABLE_DIR"] = str(output_dir)
    os.chdir(repo)
    try:
        if TMPDIR.exists():
            shutil.rmtree(TMPDIR)
        TMPDIR.mkdir()
        builder = builder_cls()
        builder.search(99, _cores())
        if builder_cls.__name__.startswith("Starting"):
            builder.save_starting_states()
        else:
            builder.save()
    finally:
        os.chdir(previous_cwd)
        if previous_dir is None:
            os.environ.pop("RUBIKS_LOOKUP_TABLE_DIR", None)
        else:
            os.environ["RUBIKS_LOOKUP_TABLE_DIR"] = previous_dir


def _compile_helpers(repo: Path) -> None:
    package = repo / "rubikscubelookuptables"
    jobs = (
        (
            package / "builder-crunch-workq",
            [package / "builder-crunch-workq.c", package / "ida_search_core.c", package / "rotate_xxx.c"],
            ["-lm"],
        ),
        (package / "compact-center-symmetry-cost", [package / "compact-center-symmetry-cost.c"], []),
        (package / "builder-find-new-states", [package / "builder-find-new-states.c"], []),
        (repo / "utils" / "pad-lines", [repo / "utils" / "pad-lines.c"], []),
    )
    for binary, sources, libraries in jobs:
        if binary.exists() and all(binary.stat().st_mtime >= source.stat().st_mtime for source in sources):
            continue
        log.info("compiling %s", binary.name)
        subprocess.check_call(["gcc", "-O3", "-o", str(binary), *map(str, sources), *libraries])


def _cores() -> int:
    return max(int(os.environ.get("RUBIKS_BUILD_CORES") or os.cpu_count() or 4), 1)


def _outputs_exist(builder_cls, output_dir: Path) -> bool:
    # Phase 4's constructor imports 343,000 starting states. The cost file name
    # is fixed, so a present file means the table is already built.
    if builder_cls.__name__ in _HEAVY_555_CLASSES:
        table = getattr(builder_cls, "table_basename", None)
        if table and (output_dir / Path(table).with_suffix(".cost-only.bin").name).is_file():
            return True
    previous_dir = os.environ.get("RUBIKS_LOOKUP_TABLE_DIR")
    os.environ["RUBIKS_LOOKUP_TABLE_DIR"] = str(output_dir)
    try:
        builder = builder_cls()
    finally:
        if previous_dir is None:
            os.environ.pop("RUBIKS_LOOKUP_TABLE_DIR", None)
        else:
            os.environ["RUBIKS_LOOKUP_TABLE_DIR"] = previous_dir
    return all(os.path.exists(path) for path in _required_outputs(builder))


def _required_outputs(builder):
    if getattr(builder, "orbit_parity_even_filename", None):
        # The combined cost array is split into these two files and removed.
        return [builder.orbit_parity_even_filename, builder.orbit_parity_odd_filename]
    if builder.use_ranked_cost:
        paths = [builder.ranked_cost_filename]
        if builder.ranked_cost_type == "center-symmetry-444":
            paths.append(builder.ranked_symmetry_index_filename)
        return paths
    return [builder.filename]


def _build_666_bars(output_dir: Path) -> None:
    output = output_dir / LR_BAR_FILENAME
    if output.exists():
        log.info("%s already built", output.name)
        return
    repo = Path(__file__).resolve().parent.parent
    solver = repo.parent / "rubiks-cube-NxNxN-solver" / "rubikscubennnsolver"
    package = repo / "rubikscubelookuptables"
    binary = package / "build-666-lr-oblique-bars"
    sources = [
        package / "build-666-lr-oblique-bars.c",
        solver / "rotate_xxx.c",
        solver / "ida_search_core.c",
    ]
    if not binary.exists() or any(binary.stat().st_mtime < source.stat().st_mtime for source in sources):
        log.info("compiling %s", binary.name)
        subprocess.check_call(
            [
                "gcc",
                "-O3",
                "-Wall",
                "-Wextra",
                "-pthread",
                "-o",
                str(binary),
                *map(str, sources),
                "-lm",
                "-latomic",
            ]
        )
    log.info("building %s", output.name)
    subprocess.check_call(
        [str(binary), "--threads", str(_cores()), "--depth", "3", "--output", str(output)],
        cwd=repo,
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build every lookup table for one cube size.")
    parser.add_argument("size", help="333, 444, 555, 666, or 777")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        build_tables(args.size)
    except ValueError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

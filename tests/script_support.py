"""Shared infrastructure for exercising the standalone scripts under utils/.

This module holds no test cases of its own.

The scripts are named with dashes and are not importable as modules, so anything
that needs one either loads it by path or runs it as a subprocess. Which of the two
applies depends on the script: the ones that guard their work behind a
__main__ check can be imported and called directly, and the rest do their work at
import time and have to be run.
"""

from __future__ import annotations

# standard libraries
import importlib.util
import logging
import subprocess
import sys
from pathlib import Path
from types import ModuleType
from typing import Iterable, Sequence

# rubiks cube libraries
from tests.builder_support import REPO_ROOT, builder_environment, ensure_importable

UTILS = REPO_ROOT / "utils"
LOOKUP_TABLES = REPO_ROOT / "rubikscubelookuptables"


def utils_scripts() -> list:
    """Every script under utils/, sorted by name."""
    return sorted(path for path in UTILS.glob("*.py"))


def load_script(path: Path) -> ModuleType:
    """Import a dashed script by path so its functions can be called directly.

    Only works for scripts that keep their work behind a __main__ check. Several of
    them call log.info() but only bind log inside that check, so a logger is
    supplied here when the script does not define one itself.
    """
    if not path.is_file():
        raise FileNotFoundError(path)

    # Some of these scripts import the external solver package.
    ensure_importable()

    module_name = path.parent.name + "_" + path.stem.replace("-", "_")
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)

    # Registered before exec so that a script importing itself by name resolves here.
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    if not hasattr(module, "log"):
        module.log = logging.getLogger(module_name)

    return module


def load_utils_script(name: str) -> ModuleType:
    """Import a utils script by path so its functions can be called directly."""
    return load_script(UTILS / name)


def load_lookup_script(name: str) -> ModuleType:
    """Import a dashed helper under rubikscubelookuptables/ by path."""
    return load_script(LOOKUP_TABLES / name)


def run_utils_script(
    name: str,
    *arguments: str,
    expect_success: bool = True,
    cwd: Path = REPO_ROOT,
) -> subprocess.CompletedProcess:
    """Run a utils script the way the Makefile does, from the repo root.

    The scripts shell out to each other with paths like ./utils/pad-lines.py, so the
    working directory defaults to the repo root. They are invoked through the current
    interpreter because several of them have no shebang line.
    """
    completed = subprocess.run(
        [sys.executable, str(UTILS / name), *arguments],
        cwd=cwd,
        env=builder_environment(),
        capture_output=True,
        text=True,
        check=False,
    )

    if expect_success and completed.returncode:
        raise AssertionError(
            f"utils/{name} {' '.join(arguments)} exited {completed.returncode}\n"
            f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        )

    return completed


def write_lines(path: Path, lines: Iterable[str]) -> Path:
    """Write a lookup-table style file, one entry per line."""
    path.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")
    return path


def read_lines(path: Path) -> Sequence[str]:
    """Read a file back as lines with the trailing newline removed."""
    return path.read_text(encoding="utf-8").splitlines()

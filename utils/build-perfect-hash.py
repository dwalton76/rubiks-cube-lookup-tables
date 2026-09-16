#!/usr/bin/env python3

# standard libraries
import logging
import os

# third party libraries
import click

logger = logging.getLogger(__name__)


@click.command()
@click.argument("file-in", type=str)
@click.option("--file-out", type=str, default=None, help="perfect hash filename")
def main(file_in: str, file_out: str) -> None:
    """
    \b
    Build a combined perfect-hash table from two prune tables.

    5x5 combo hashes are produced by convert-pt-state-to-perfect-hash.py from
    a pt-state listing. This entry point remains for Makefile / CLI compatibility.
    """
    if not os.path.exists(file_in):
        raise FileNotFoundError(file_in)

    raise NotImplementedError(file_in)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    main()

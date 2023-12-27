#!/usr/bin/env python3

# standard libraries
import logging
import os
import sys

log = logging.getLogger(__name__)


def convert_json_to_json_one_line(filename: str) -> None:
    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist")
        sys.exit(1)

    to_write = []
    to_write_count = 0
    BATCH_SIZE = 1000000
    one_line_filename = filename.replace(".json", ".json-one-line")

    with open(one_line_filename, "w") as fh_one_line:
        with open(filename, "r") as fh:
            for line_index, line in enumerate(fh):
                line = line.strip()

                if not line:
                    continue

                to_write.append(line)
                to_write_count += 1

                if to_write_count >= BATCH_SIZE:
                    log.info(f"{line_index:,}")
                    fh_one_line.write("".join(to_write))
                    to_write = []
                    to_write_count = 0

            if to_write_count:
                fh_one_line.write("".join(to_write))

            fh_one_line.write("\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    filename = sys.argv[1]
    convert_json_to_json_one_line(filename)

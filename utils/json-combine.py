#!/usr/bin/env python3

# standard libraries
import logging
import os
import shutil
import sys
from typing import List


def json_combine_files(filenames: List[str]) -> None:
    output_filename = "/tmp/json_combine_files.txt"

    with open(output_filename, "w") as fh_final:
        # start with a {
        fh_final.write("{\n")

        for (index, filename) in enumerate(filenames):
            # count the number of lines in the file without reading the entire file into memory at once
            line_count = sum(1 for line in open(filename))

            log.info(f"{filename} begin ({line_count:,} lines)")

            # If this is not the first file, write a "," to continue the json
            # from the previous file
            if index > 0:
                fh_final.write(",\n")

            with open(filename, "r") as fh:
                last_line_index = line_count - 1

                for line_index, line in enumerate(fh):
                    # chop the first and last line, they contain the opening { and closing }
                    if line_index == 0 or line_index == last_line_index:
                        continue
                    fh_final.write(f"{line}\n")

            log.info(f"{filename} end")

        # end with a }
        fh_final.write("\n}\n")

    # delete the .json files, we no longer need them
    for (index, filename) in enumerate(filenames):
        os.unlink(filename)

    # save all output to the last filename
    shutil.move(output_filename, filenames[-1])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    filenames = sys.argv[1:]
    json_combine_files(filenames)

#!/usr/bin/env python3

# standard libraries
import glob
import logging
import os
import shutil
import sys
from pathlib import Path


def json_combine_files(json_filename: str) -> None:
    output_filename = "/tmp/json_combine_files.txt"
    filenames = glob.glob(f"{Path(json_filename).absolute()}*")
    filenames.sort()
    filenames = filenames[1:] + [filenames[0]]

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
                    fh_final.write(line)

            log.info(f"{filename} end")

        # end with a }
        fh_final.write("\n}\n")

    # delete the .json files, we no longer need them
    for (index, filename) in enumerate(filenames):
        os.unlink(filename)

    # save all output to the last filename
    shutil.move(output_filename, json_filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    filename = sys.argv[1]
    json_combine_files(filename)

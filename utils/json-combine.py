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
            log.info(f"{filename} begin")

            # If this is not the first file, write a "," to continue the json
            # from the previous file
            if index > 0:
                fh_final.write(",\n")

            with open(filename, "r") as fh:
                lines = fh.readlines()

                # chop the first and last line
                lines = lines[1:-1]

                # write everything else
                fh_final.write("\n".join(lines))

            # rm the file
            os.unlink(filename)
            log.info(f"{filename} end")

        # end with a }
        fh_final.write("\n}\n")

    # save all output to the last filename
    shutil.move(output_filename, filenames[-1])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    filenames = sys.argv[1:]
    json_combine_files(filenames)

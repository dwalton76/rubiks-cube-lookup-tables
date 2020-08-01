#!/usr/bin/env python3

# standard libraries
import glob
import logging
import os
import subprocess
import time
from typing import List

# third party libraries
import psutil


def process_pids(target_name: str) -> List[int]:
    """
    Return all of the PIDs for a process named "target_name"
    """
    result = []

    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            process_id = proc.pid

            if process_name == target_name:
                result.append(process_id)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return result


def sort_merge(index: int):
    files_to_sort_filename = "tmp/files_to_sort.txt"
    output_filename = f"tmp/sort-merge-%d-core.txt" % index
    core_files = sorted(glob.glob("tmp/*core*"))

    if not core_files:
        return

    # find state_width
    first_core_file = core_files[0]

    with open(first_core_file, "r") as fh:
        line = next(fh)

        if line.count(":") != 1:
            raise Exception("Implement this")

        state = line.split(":")[0]
        state_width = len(state)

    # write a list of the files we want to sort to a files_to_sort_filename
    # we will point sort at files_to_sort_filename
    with open(files_to_sort_filename, "w") as fh:
        fh.write('\0'.join(core_files))

    size_before = 0
    for filename in core_files:
        size_before += os.stat(filename).st_size

    logger.info(f"sort {len(core_files)} files created by builder-crunch-workq processes begin")
    logger.info(f"{size_before:,} bytes before")
    cmd = "LC_ALL=C nice sort --uniq --key=1.1,1.%d --merge --temporary-directory=./tmp/ --output %s --files0-from='tmp/files_to_sort.txt'" % (state_width, output_filename)
    subprocess.check_output(cmd, shell=True)
    os.unlink(files_to_sort_filename)

    for filename in core_files:
        # logger.info(f"rm {filename}")
        os.unlink(filename)

    size_after = os.stat(output_filename).st_size
    logger.info(f"{size_after:,} bytes after")
    logger.info(f"sort {len(core_files)} files created by builder-crunch-workq processes end")


def main():
    index = 0

    while True:
        pids = process_pids("builder-crunch-workq")

        if pids:
            # logger.info(f"{len(pids)} builder-crunch-workq processes are running")
            sort_merge(index)
            time.sleep(10)
        else:
            # logger.info("all builder-crunch-workq processes have finished")
            break

        index += 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)24s %(levelname)8s: %(message)s')
    logger = logging.getLogger(__name__)

    main()

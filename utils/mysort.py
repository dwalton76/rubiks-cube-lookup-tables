# standard libraries
import bisect
from collections import deque


class FileHandle:
    def __init__(self, filename):
        self.filename = filename
        self.filehandle = open(filename, "r")
        self.line = next(self.filehandle)


def merge_sort(files_to_sort_filename: str, state_width: int) -> None:
    """
    sort --merge a list of sorted files
    """

    # build a list of files to be sorted
    files_to_sort = []
    with open(files_to_sort_filename, "r") as fh:
        for line in fh:
            files_to_sort.extend(line.split("\0"))

    # open a readonly filehandle for each file
    filehandles = []
    for filename in files_to_sort:
        filehandles.append(FileHandle(filename))

    # create a sorted list with one line from each filehandle
    current_lines = deque()
    for fh in filehandles:
        bisect.insort(current_lines, (fh.line, fh))

    # open a write filehandle for our results
    fh_write = open("tmp/dwalton.txt", "w")
    prev_state = ""
    to_write_count = 0
    to_write = []
    filehandles_count = len(filehandles)

    # loop until we have read every line from every filehandle
    while filehandles_count > 0:

        # The list of lines is sorted, popleft the first line which has the lowest value
        (first_line, first_fh) = current_lines.popleft()
        first_line_state = first_line[:state_width]

        if filehandles_count >= 2:
            (second_line, second_fh) = current_lines[0]
            second_line_state = second_line[:state_width]

        # dwalton
        while filehandles_count == 1 or first_line_state <= second_line_state:

            if first_line_state != prev_state:
                to_write.append(first_line)
                to_write_count += 1
                prev_state = first_line_state

                if to_write_count >= 100000:
                    fh_write.write("".join(to_write))
                    to_write_count = 0
                    to_write = []

            try:
                first_fh.line = next(first_fh.filehandle)
                first_line = first_fh.line
                first_line_state = first_line[:state_width]
            except StopIteration:
                filehandles.remove(first_fh)
                filehandles_count -= 1
                first_line = None
                break

        if first_line is not None:
            bisect.insort(current_lines, (first_fh.line, first_fh))

    if to_write_count:
        fh_write.write("".join(to_write))
        to_write_count = 0
        to_write = []

    # close all filehandles
    for fh in filehandles:
        fh.filehandle.close()
    fh_write.close()


if __name__ == "__main__":
    merge_sort("tmp/files_to_sort.txt", 151)

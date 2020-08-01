# standard libraries
import sys
from itertools import islice

n = 10000

# I think under the covers islice is still going line-by-line by iterating fh
with open(sys.argv[1], "r") as fh:
    # https://stackoverflow.com/questions/6335839/python-how-to-read-n-number-of-lines-at-a-time
    while True:
        batch_lines = list(islice(fh, n))

        if batch_lines:
            for line in batch_lines:
                pass
        else:
            break

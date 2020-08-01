# standard libraries
import os
import sys

filename = sys.argv[1]
size = os.path.getsize(filename)
chunk_size = 1024 * 1024 * 10
read_count = 0
print(f"{filename} is {size} bytes")

with open(sys.argv[1], "r") as fh:
    while True:
        chunk = fh.read(chunk_size)
    
        if chunk:
            read_count += 1
            for line in chunk.splitlines():
                pass
        else:
            break

print(f"took {read_count} reads")

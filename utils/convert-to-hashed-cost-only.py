#!/usr/bin/env python3

# standard libraries
import argparse
import logging

# third party libraries
from pyhashxx import hashxx

log = logging.getLogger(__name__)


def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None


def find_next_prime(n):
    return find_prime_in_range(n, 2 * n)


def convert_to_cost_only(filename, bucketcount, filename_statetargets):

    state_targets = set()
    with open(filename_statetargets, "r") as fh:
        for line in fh:
            line = line.replace("'", "").replace(",", "").strip()
            state_targets.add(line)

    filename_new = filename.replace(".txt", ".hash-cost-only.txt")

    bucket = bytearray(bucketcount)
    collisions = 0

    with open(filename, "r") as fh:
        for (line_number, line) in enumerate(fh):
            (state, steps) = line.strip().split(":")
            steps = steps.split()

            hash_raw = hashxx(state.encode("utf-8"))
            hash_index = int(hash_raw % bucketcount)

            # Write the steps_len
            if state in state_targets:
                log.info("found state_target %s, hash_raw %s, hash_index %d" % (state, hash_raw, hash_index))
                steps_len = 0
                bucket[hash_index] = steps_len
            else:
                if steps[0].isdigit():
                    steps_len = int(steps[0])
                else:
                    steps_len = len(steps)

                if not bucket[hash_index]:
                    bucket[hash_index] = steps_len
                else:
                    collisions += 1

                    # Never under estimate the cost
                    # if steps_len > bucket[hash_index]:
                    #    bucket[hash_index] = steps_len

                    # Never over estimate the cost
                    if bucket[hash_index] > steps_len:
                        bucket[hash_index] = steps_len

            if line_number and line_number % 1000000 == 0:
                log.info(line_number)

    log.info("%d collisions" % collisions)
    log.info(f"begin writing {filename_new}")
    with open(filename_new, "w") as fh_new:
        to_write = []

        for (index, x) in enumerate(bucket):

            if x > 15:
                to_write.append("f")
            else:
                # Convert steps_len to hex and ignore the 0x part of the string
                to_write.append(hex(x)[2])

            if index % 100000 == 0:
                fh_new.write("".join(to_write))
                to_write = []

        if to_write:
            fh_new.write("".join(to_write))
            to_write = []

        fh_new.write("\n")
    log.info(f"end writing {filename_new}")


if __name__ == "__main__":

    # setup logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)16s %(levelname)8s: %(message)s")
    log = logging.getLogger(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="lookup-table filename")
    parser.add_argument("bucketcount", type=int, help="number of buckets to use")
    parser.add_argument("statetargets", type=str, help="file with state_targets")
    args = parser.parse_args()

    convert_to_cost_only(args.filename, args.bucketcount, args.statetargets)

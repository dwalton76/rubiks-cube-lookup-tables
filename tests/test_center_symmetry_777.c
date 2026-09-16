/*
 * Checks center_symmetry_777.h against the uncompacted 70^5 tables.
 *
 * For each axis and each sampled state it asserts that the cost read from that
 * axis's own table equals the cost the UD table reports at the canonical rank.
 * That covers both claims at once: the 16 symmetries preserve cost, and the
 * three axes are the same function re-indexed.
 *
 * Passing a compacted table and its symmetry index also checks that the
 * compacted pair reproduces the same cost, which is what the solver will read.
 *
 * usage: test_center_symmetry_777 UD-COST LR-COST FB-COST
 *            [--compact COST INDEX] [--samples N]
 */

#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

#include "../rubikscubelookuptables/center_symmetry_777.h"

static const unsigned char *map_cost(const char *filename, uint64_t expected, int *fd)
{
    struct stat file_stat;
    const unsigned char *costs;

    *fd = open(filename, O_RDONLY);
    if (*fd < 0 || fstat(*fd, &file_stat) != 0) {
        fprintf(stderr, "ERROR: could not open %s: %s\n", filename, strerror(errno));
        exit(1);
    }
    if ((uint64_t) file_stat.st_size != expected) {
        fprintf(stderr, "ERROR: %s is %jd bytes, expected %" PRIu64 "\n",
            filename, (intmax_t) file_stat.st_size, expected);
        exit(1);
    }
    costs = mmap(NULL, expected, PROT_READ, MAP_SHARED, *fd, 0);
    if (costs == MAP_FAILED) {
        fprintf(stderr, "ERROR: could not mmap %s: %s\n", filename, strerror(errno));
        exit(1);
    }
    return costs;
}

static uint64_t next_random(uint64_t *state)
{
    *state ^= *state << 13;
    *state ^= *state >> 7;
    *state ^= *state << 17;
    return *state;
}

int main(int argc, char **argv)
{
    const unsigned char *costs[DAISY_AXIS_COUNT_777];
    const unsigned char *compact = NULL;
    const char *compact_filename = NULL;
    const char *index_filename = NULL;
    struct daisy_symmetry_index_777 index = {-1, 0, NULL, NULL, NULL, NULL};
    int fds[DAISY_AXIS_COUNT_777];
    int compact_fd = -1;
    uint64_t samples = 200000;
    uint64_t random_state = UINT64_C(0x2026091420260914);
    uint64_t mismatches = 0;
    uint64_t skipped = 0;
    uint64_t canonical_is_self = 0;

    if (argc < 4) {
        fprintf(stderr, "usage: %s UD-COST LR-COST FB-COST [--compact COST INDEX] [--samples N]\n",
            argv[0]);
        return 1;
    }
    for (int position = 4; position < argc; position++) {
        if (!strcmp(argv[position], "--compact") && position + 2 < argc) {
            compact_filename = argv[++position];
            index_filename = argv[++position];
        } else if (!strcmp(argv[position], "--samples") && position + 1 < argc) {
            samples = strtoull(argv[++position], NULL, 10);
        } else {
            fprintf(stderr, "ERROR: unexpected argument %s\n", argv[position]);
            return 1;
        }
    }
    init_center_symmetry_777();

    for (unsigned int axis = 0; axis < DAISY_AXIS_COUNT_777; axis++) {
        costs[axis] = map_cost(argv[1 + axis], DAISY_PERFECT_UNIVERSE_777, &fds[axis]);
    }
    if (compact_filename) {
        const char *problem = NULL;

        compact = map_cost(compact_filename, DAISY_PERFECT_ORBIT_COUNT_777, &compact_fd);
        if (!daisy_symmetry_index_open_777(&index, index_filename, &problem)) {
            fprintf(stderr, "ERROR: %s %s\n", index_filename, problem);
            return 1;
        }
    }

    for (uint64_t sample = 0; sample < samples; sample++) {
        uint64_t orbit_rank[DAISY_ORBIT_COUNT_777];
        uint64_t raw = 0;

        for (unsigned int orbit = 0; orbit < DAISY_ORBIT_COUNT_777; orbit++) {
            orbit_rank[orbit] = next_random(&random_state) % DAISY_GROUP_UNIVERSE_777;
            raw += orbit_rank[orbit] * daisy_group_place_777[orbit];
        }

        for (unsigned int axis = 0; axis < DAISY_AXIS_COUNT_777; axis++) {
            uint64_t canonical = daisy_canonical_rank_777(axis, orbit_rank);
            unsigned char mine;
            unsigned char shared;

            if (canonical >= DAISY_PERFECT_UNIVERSE_777) {
                fprintf(stderr, "ERROR: canonical rank %" PRIu64 " out of range\n", canonical);
                return 1;
            }
            if (canonical > raw && !axis) {
                fprintf(stderr, "ERROR: UD canonical rank rose above the raw rank\n");
                return 1;
            }
            mine = costs[axis][raw];
            shared = costs[0][canonical];
            if (mine != shared) {
                if (mismatches < 10) {
                    fprintf(stderr,
                        "MISMATCH axis %u raw %" PRIu64 " cost %u, canonical %" PRIu64 " cost %u\n",
                        axis, raw, mine, canonical, shared);
                }
                mismatches++;
            }
            if (compact) {
                uint64_t dense = daisy_symmetry_dense_rank_777(&index, canonical);

                if (dense >= DAISY_PERFECT_ORBIT_COUNT_777) {
                    fprintf(stderr, "ERROR: canonical rank %" PRIu64 " missing from the index\n",
                        canonical);
                    return 1;
                }
                if (compact[dense] != mine) {
                    if (mismatches < 10) {
                        fprintf(stderr,
                            "MISMATCH axis %u raw %" PRIu64 " cost %u, dense %" PRIu64 " cost %u\n",
                            axis, raw, mine, dense, compact[dense]);
                    }
                    mismatches++;
                }
            }
            if (!mine) {
                skipped++;
            }
            if (canonical == raw) {
                canonical_is_self++;
            }
        }
    }

    for (unsigned int axis = 0; axis < DAISY_AXIS_COUNT_777; axis++) {
        munmap((void *) costs[axis], DAISY_PERFECT_UNIVERSE_777);
        close(fds[axis]);
    }
    if (compact) {
        munmap((void *) compact, DAISY_PERFECT_ORBIT_COUNT_777);
        close(compact_fd);
        daisy_symmetry_index_close_777(&index);
    }
    printf("%" PRIu64 " samples x 3 axes%s, %" PRIu64 " mismatches, %" PRIu64 " unreached, "
           "%" PRIu64 " already canonical\n",
        samples, compact ? " against the compacted pair" : "",
        mismatches, skipped, canonical_is_self);
    return mismatches != 0;
}

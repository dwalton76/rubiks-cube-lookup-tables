/*
 * Compacts a 7x7x7 70^5 center cost table onto its symmetry orbits.
 *
 * The costs in the input are already constant on each orbit of the 16
 * axis-preserving cube symmetries, so no BFS rebuild is needed: we keep the
 * byte at every rank that is the smallest in its orbit and drop the other 15
 * out of 16.  1,680,700,000 raw ranks become 105,356,972 orbits, and a
 * rank-select index maps a canonical raw rank to its dense position.
 *
 * An Elias-Fano index would be half the size but read about three times
 * slower, because it has to walk every orbit sharing a rank's high bits. See
 * center_symmetry_777.h for the format this writes.
 *
 * usage: compact-center-symmetry-777 RAW-COST COMPACT-COST SYMMETRY-INDEX [--threads N]
 */

#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <pthread.h>
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

#include "center_symmetry_777.h"

#define MAX_THREADS 64
#define SLICE_COUNT 70

static const unsigned char *raw;
static unsigned char *compact;
static uint64_t *bitmap;
static uint64_t slice_count[SLICE_COUNT];
static uint64_t slice_start[SLICE_COUNT];
static atomic_uint next_slice;

static void fail(const char *message, const char *filename)
{
    fprintf(stderr, "ERROR: %s %s: %s\n", message, filename, strerror(errno));
    exit(1);
}

/*
 * Walk one slice of the coordinate, the 70^4 ranks sharing a left-oblique
 * rank.  Nesting the loops keeps the five group ranks free, so the only real
 * work is the canonical test.
 */
static uint64_t walk_slice(unsigned int slice, uint64_t dense)
{
    uint64_t orbit_rank[DAISY_ORBIT_COUNT_777];
    uint64_t found = 0;

    orbit_rank[0] = slice;
    for (orbit_rank[1] = 0; orbit_rank[1] < DAISY_GROUP_UNIVERSE_777; orbit_rank[1]++) {
        for (orbit_rank[2] = 0; orbit_rank[2] < DAISY_GROUP_UNIVERSE_777; orbit_rank[2]++) {
            for (orbit_rank[3] = 0; orbit_rank[3] < DAISY_GROUP_UNIVERSE_777; orbit_rank[3]++) {
                uint64_t prefix = orbit_rank[0] * daisy_group_place_777[0] +
                                  orbit_rank[1] * daisy_group_place_777[1] +
                                  orbit_rank[2] * daisy_group_place_777[2] +
                                  orbit_rank[3] * daisy_group_place_777[3];

                for (orbit_rank[4] = 0; orbit_rank[4] < DAISY_GROUP_UNIVERSE_777; orbit_rank[4]++) {
                    uint64_t rank = prefix + orbit_rank[4];

                    if (daisy_canonical_rank_777(0, orbit_rank) != rank) {
                        continue;
                    }
                    if (compact) {
                        compact[dense] = raw[rank];
                        /* Neighbouring slices share the word at their boundary,
                         * and bits are only ever set, so a relaxed or is enough. */
                        __atomic_fetch_or(&bitmap[rank >> 6],
                            UINT64_C(1) << (rank & 63), __ATOMIC_RELAXED);
                    }
                    dense++;
                    found++;
                }
            }
        }
    }
    return found;
}

static void *worker(void *argument)
{
    (void) argument;
    while (1) {
        unsigned int slice = atomic_fetch_add(&next_slice, 1);

        if (slice >= SLICE_COUNT) {
            break;
        }
        if (compact) {
            walk_slice(slice, slice_start[slice]);
        } else {
            slice_count[slice] = walk_slice(slice, 0);
        }
    }
    return NULL;
}

static void run_pass(unsigned int thread_count)
{
    pthread_t threads[MAX_THREADS];

    atomic_store(&next_slice, 0);
    for (unsigned int index = 0; index < thread_count; index++) {
        if (pthread_create(&threads[index], NULL, worker, NULL) != 0) {
            fprintf(stderr, "ERROR: could not create thread %u\n", index);
            exit(1);
        }
    }
    for (unsigned int index = 0; index < thread_count; index++) {
        pthread_join(threads[index], NULL);
    }
}

int main(int argc, char **argv)
{
    struct stat input_stat;
    struct daisy_symmetry_index_header_777 header;
    long detected_cpus = sysconf(_SC_NPROCESSORS_ONLN);
    unsigned int thread_count = detected_cpus > 0 ? (unsigned int) detected_cpus : 1;
    const char *raw_filename = NULL;
    const char *compact_filename = NULL;
    const char *index_filename = NULL;
    unsigned char *index_map;
    uint32_t *block_rank;
    uint64_t orbit_count = 0;
    uint64_t index_size;
    uint64_t running = 0;
    int input_fd;
    int compact_fd;
    int index_fd;

    for (int index = 1; index < argc; index++) {
        if (!strcmp(argv[index], "--threads") && index + 1 < argc) {
            thread_count = (unsigned int) atoi(argv[++index]);
        } else if (!raw_filename) {
            raw_filename = argv[index];
        } else if (!compact_filename) {
            compact_filename = argv[index];
        } else if (!index_filename) {
            index_filename = argv[index];
        } else {
            index_filename = NULL;
            break;
        }
    }
    if (!raw_filename || !compact_filename || !index_filename ||
            !thread_count || thread_count > MAX_THREADS) {
        fprintf(stderr, "usage: %s RAW-COST COMPACT-COST SYMMETRY-INDEX [--threads N]\n", argv[0]);
        return 1;
    }

    input_fd = open(raw_filename, O_RDONLY);
    if (input_fd < 0 || fstat(input_fd, &input_stat) != 0) {
        fail("could not open", raw_filename);
    }
    if ((uint64_t) input_stat.st_size != DAISY_PERFECT_UNIVERSE_777) {
        fprintf(stderr, "ERROR: %s is %jd bytes, expected %" PRIu64 "\n",
            raw_filename, (intmax_t) input_stat.st_size, DAISY_PERFECT_UNIVERSE_777);
        return 1;
    }
    raw = mmap(NULL, DAISY_PERFECT_UNIVERSE_777, PROT_READ, MAP_SHARED, input_fd, 0);
    if (raw == MAP_FAILED) {
        fail("could not mmap", raw_filename);
    }
    init_center_symmetry_777();

    run_pass(thread_count);
    for (unsigned int slice = 0; slice < SLICE_COUNT; slice++) {
        slice_start[slice] = orbit_count;
        orbit_count += slice_count[slice];
    }
    if (orbit_count != DAISY_PERFECT_ORBIT_COUNT_777) {
        fprintf(stderr, "ERROR: counted %" PRIu64 " orbits, expected %" PRIu64 "\n",
            orbit_count, DAISY_PERFECT_ORBIT_COUNT_777);
        return 1;
    }

    memset(&header, 0, sizeof(header));
    memcpy(header.magic, DAISY_RANK_INDEX_MAGIC_777, sizeof(header.magic));
    header.raw_universe = DAISY_PERFECT_UNIVERSE_777;
    header.orbit_count = orbit_count;
    header.block_count = daisy_symmetry_block_count_777(DAISY_PERFECT_UNIVERSE_777);
    header.word_count = header.block_count * DAISY_RANK_BLOCK_WORDS_777;

    compact_fd = open(compact_filename, O_RDWR | O_CREAT | O_TRUNC, 0644);
    index_fd = open(index_filename, O_RDWR | O_CREAT | O_TRUNC, 0644);
    if (compact_fd < 0 || index_fd < 0) {
        fail("could not create", compact_fd < 0 ? compact_filename : index_filename);
    }
    index_size = daisy_symmetry_index_size_777(header.block_count);
    if (ftruncate(compact_fd, (off_t) orbit_count) != 0) {
        fail("could not size", compact_filename);
    }
    if (ftruncate(index_fd, (off_t) index_size) != 0) {
        fail("could not size", index_filename);
    }

    compact = mmap(NULL, orbit_count, PROT_READ | PROT_WRITE, MAP_SHARED, compact_fd, 0);
    index_map = mmap(NULL, index_size, PROT_READ | PROT_WRITE, MAP_SHARED, index_fd, 0);
    if (compact == MAP_FAILED || index_map == MAP_FAILED) {
        fail("could not mmap", compact == MAP_FAILED ? compact_filename : index_filename);
    }
    memcpy(index_map, &header, sizeof(header));
    bitmap = (uint64_t *) (index_map + sizeof(header));
    block_rank = (uint32_t *) (bitmap + header.word_count);

    run_pass(thread_count);

    for (uint64_t block = 0; block < header.block_count; block++) {
        block_rank[block] = (uint32_t) running;
        for (unsigned int word = 0; word < DAISY_RANK_BLOCK_WORDS_777; word++) {
            running += (unsigned int) __builtin_popcountll(
                bitmap[block * DAISY_RANK_BLOCK_WORDS_777 + word]);
        }
    }
    if (running != orbit_count) {
        fprintf(stderr, "ERROR: bitmap holds %" PRIu64 " ranks, expected %" PRIu64 "\n",
            running, orbit_count);
        return 1;
    }

    msync(compact, orbit_count, MS_SYNC);
    msync(index_map, index_size, MS_SYNC);
    munmap((void *) raw, DAISY_PERFECT_UNIVERSE_777);
    munmap(compact, orbit_count);
    munmap(index_map, index_size);
    close(input_fd);
    close(compact_fd);
    close(index_fd);
    printf("compacted %" PRIu64 " raw ranks into %" PRIu64 " symmetry orbits, "
           "%" PRIu64 " byte rank-select index\n",
        DAISY_PERFECT_UNIVERSE_777, orbit_count, index_size);
    return 0;
}

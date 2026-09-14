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

#define RAW_UNIVERSE UINT64_C(9465511770)
#define LOW_BITS 5U
#define ZERO_SAMPLE_RATE 512U
#define INDEX_MAGIC "CS444EF1"

struct index_header {
    char magic[8];
    uint64_t raw_universe;
    uint64_t orbit_count;
    uint64_t low_word_count;
    uint64_t high_bit_count;
    uint64_t high_word_count;
    uint64_t zero_sample_count;
    uint32_t low_bits;
    uint32_t zero_sample_rate;
};

static void fail(const char *message, const char *filename)
{
    fprintf(stderr, "ERROR: %s %s: %s\n", message, filename, strerror(errno));
    exit(1);
}

int main(int argc, char **argv)
{
    struct stat input_stat;
    struct index_header header;
    int input_fd;
    int cost_fd;
    int index_fd;
    unsigned char *raw;
    unsigned char *costs;
    unsigned char *index_map;
    uint64_t *low;
    uint64_t *high;
    uint32_t *samples;
    uint64_t dense = 0;
    uint64_t orbit_count = 0;
    uint64_t zeros = 0;

    if (argc != 4) {
        fprintf(stderr, "usage: %s RAW-COST COMPACT-COST SYMMETRY-INDEX\n", argv[0]);
        return 1;
    }
    input_fd = open(argv[1], O_RDONLY);
    if (input_fd < 0 || fstat(input_fd, &input_stat) != 0) {
        fail("could not open", argv[1]);
    }
    if ((uint64_t) input_stat.st_size != RAW_UNIVERSE) {
        fprintf(stderr, "ERROR: %s is %jd bytes, expected %" PRIu64 "\n",
            argv[1], (intmax_t) input_stat.st_size, RAW_UNIVERSE);
        return 1;
    }

    raw = mmap(NULL, RAW_UNIVERSE, PROT_READ, MAP_SHARED, input_fd, 0);
    if (raw == MAP_FAILED) {
        fail("could not mmap", argv[1]);
    }
    for (uint64_t rank = 0; rank < RAW_UNIVERSE; rank++) {
        orbit_count += raw[rank] != 0;
    }

    memset(&header, 0, sizeof(header));
    memcpy(header.magic, INDEX_MAGIC, sizeof(header.magic));
    header.raw_universe = RAW_UNIVERSE;
    header.orbit_count = orbit_count;
    header.low_bits = LOW_BITS;
    header.zero_sample_rate = ZERO_SAMPLE_RATE;
    header.low_word_count = (orbit_count * LOW_BITS + 63) / 64;
    header.high_bit_count = (RAW_UNIVERSE >> LOW_BITS) + orbit_count + 1;
    header.high_word_count = (header.high_bit_count + 63) / 64;
    header.zero_sample_count =
        (((header.high_bit_count - orbit_count) - 1) / ZERO_SAMPLE_RATE) + 1;

    cost_fd = open(argv[2], O_RDWR | O_CREAT | O_TRUNC, 0644);
    index_fd = open(argv[3], O_RDWR | O_CREAT | O_TRUNC, 0644);
    if (cost_fd < 0 || index_fd < 0) {
        fail("could not create output for", cost_fd < 0 ? argv[2] : argv[3]);
    }
    uint64_t index_size = sizeof(header) +
        (header.low_word_count * sizeof(uint64_t)) +
        (header.high_word_count * sizeof(uint64_t)) +
        (header.zero_sample_count * sizeof(uint32_t));
    if (ftruncate(cost_fd, orbit_count) != 0 ||
            ftruncate(index_fd, (off_t) index_size) != 0) {
        fail("could not size output", argv[2]);
    }

    costs = mmap(NULL, orbit_count, PROT_READ | PROT_WRITE, MAP_SHARED, cost_fd, 0);
    index_map = mmap(NULL, index_size, PROT_READ | PROT_WRITE, MAP_SHARED, index_fd, 0);
    if (raw == MAP_FAILED || costs == MAP_FAILED || index_map == MAP_FAILED) {
        fail("could not mmap", argv[1]);
    }
    memcpy(index_map, &header, sizeof(header));
    low = (uint64_t *) (index_map + sizeof(header));
    high = low + header.low_word_count;
    samples = (uint32_t *) (high + header.high_word_count);

    for (uint64_t rank = 0; rank < RAW_UNIVERSE; rank++) {
        unsigned char encoded = raw[rank];
        if (!encoded) {
            continue;
        }
        if (dense >= orbit_count) {
            fprintf(stderr, "ERROR: more than %" PRIu64 " symmetry orbits\n", orbit_count);
            return 1;
        }
        costs[dense] = encoded;

        uint64_t low_bit = dense * LOW_BITS;
        uint64_t low_value = rank & ((UINT64_C(1) << LOW_BITS) - 1);
        low[low_bit >> 6] |= low_value << (low_bit & 63);
        if ((low_bit & 63) > 64 - LOW_BITS) {
            low[(low_bit >> 6) + 1] |= low_value >> (64 - (low_bit & 63));
        }

        uint64_t high_bit = (rank >> LOW_BITS) + dense;
        high[high_bit >> 6] |= UINT64_C(1) << (high_bit & 63);
        dense++;
    }
    if (dense != orbit_count) {
        fprintf(stderr, "ERROR: found %" PRIu64 " symmetry orbits, expected %" PRIu64 "\n",
            dense, orbit_count);
        return 1;
    }

    for (uint64_t bit = 0; bit < header.high_bit_count; bit++) {
        if (!(high[bit >> 6] & (UINT64_C(1) << (bit & 63)))) {
            if (!(zeros % ZERO_SAMPLE_RATE)) {
                samples[zeros / ZERO_SAMPLE_RATE] = (uint32_t) bit;
            }
            zeros++;
        }
    }
    if (zeros != header.high_bit_count - orbit_count) {
        fprintf(stderr, "ERROR: Elias-Fano zero count mismatch\n");
        return 1;
    }

    msync(costs, orbit_count, MS_SYNC);
    msync(index_map, index_size, MS_SYNC);
    munmap(raw, RAW_UNIVERSE);
    munmap(costs, orbit_count);
    munmap(index_map, index_size);
    close(input_fd);
    close(cost_fd);
    close(index_fd);
    printf("compacted %" PRIu64 " raw ranks into %" PRIu64 " symmetry orbits\n",
        RAW_UNIVERSE, orbit_count);
    return 0;
}

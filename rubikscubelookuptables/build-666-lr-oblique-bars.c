/*
 * Symmetry-reduced depth-3 LR oblique bar table for 6x6 phase 2.
 *
 * The key is 48 occupancy bits, one per oblique sticker, set when that sticker
 * is L or R. Goals are the C(24, 8) ways to place eight paired bars. Keys are
 * canonicalized under the 16 rotations and mirrors that keep the LR axis
 * unoriented. The file is an open-addressed hash of key | cost << 48.
 *
 * The solver loads lookup-table-6x6x6-phase2-LR-oblique-bars.sym-depth3.hash.bin
 * and rejects every other depth. This builder uses the solver's rotate and
 * move-table code so the 46 legal phase-2 moves stay the same set the search
 * uses.
 */

#include "../../rubiks-cube-NxNxN-solver/rubikscubennnsolver/ida_search_core.h"

#include <errno.h>
#include <inttypes.h>
#include <limits.h>
#include <locale.h>
#include <pthread.h>
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/time.h>
#include <unistd.h>

#define CUBE_ARRAY_SIZE 217
#define OBLIQUE_PAIR_COUNT 24
#define BAR_SQUARES 48
#define BAR_SYMMETRIES 16
#define BAR_KEY_MASK ((UINT64_C(1) << BAR_SQUARES) - 1)
#define BAR_COST_SHIFT 48
#define BAR_MAX_DEPTH 20
#define BAR_FIRST_LOG2 22
#define BAR_MAX_LOG2 31
#define BAR_COUNT_BATCH 0x10000u
#define MAX_THREADS 64

static const unsigned int all_left_oblique_squares[OBLIQUE_PAIR_COUNT] = {
    9, 20, 17, 28, 45, 56, 53, 64, 81, 92, 89, 100,
    117, 128, 125, 136, 153, 164, 161, 172, 189, 200, 197, 208,
};
static const unsigned int all_right_oblique_squares[OBLIQUE_PAIR_COUNT] = {
    10, 14, 23, 27, 46, 50, 59, 63, 82, 86, 95, 99,
    118, 122, 131, 135, 154, 158, 167, 171, 190, 194, 203, 207,
};

struct bar_header {
    char magic[8];
    uint32_t depth;
    uint32_t log2_capacity;
    uint64_t count;
    uint64_t depth_count[BAR_MAX_DEPTH + 1];
};

static const char BAR_MAGIC[8] = {'L', 'R', 'B', 'A', 'R', '6', '6', '2'};
static uint64_t bar_symmetry_byte_map[BAR_SYMMETRIES][6][256];
static unsigned char bar_symmetry_position[BAR_SYMMETRIES][BAR_SQUARES];
static unsigned int bar_move_count;
static uint64_t bar_byte_map[MOVE_COUNT_666][6][256];
static unsigned char bar_move_position[MOVE_COUNT_666][BAR_SQUARES];
static unsigned char legal_move_count[MOVE_MAX];
static unsigned char legal_move_index[MOVE_MAX][IDA_MOVE_INDEX_MAX];
static move_type inverse_move[MOVE_MAX];

static struct {
    uint64_t *slots;
    uint64_t *old_slots;
    uint64_t old_capacity;
    unsigned int log2;
    uint64_t mask;
    unsigned int shift;
    uint64_t limit;
    atomic_uint_fast64_t count;
    atomic_int overflow;
} bar_build;

struct bar_worker {
    unsigned int index;
    unsigned int threads;
    unsigned char depth;
};

static unsigned int bar_square(unsigned int bit)
{
    return bit < OBLIQUE_PAIR_COUNT ? all_left_oblique_squares[bit]
                                    : all_right_oblique_squares[bit - OBLIQUE_PAIR_COUNT];
}

static void bar_square_position(unsigned int square, int8_t position[3])
{
    unsigned int face = (square - 1) / 36;
    unsigned int offset = (square - 1) % 36;
    int row = (int)(offset / 6);
    int col = (int)(offset % 6);
    static const int8_t coordinate[6] = {-5, -3, -1, 1, 3, 5};

    switch (face) {
    case 0: position[0] = coordinate[col]; position[1] = 5; position[2] = coordinate[row]; break;
    case 1: position[0] = -5; position[1] = -coordinate[row]; position[2] = coordinate[col]; break;
    case 2: position[0] = coordinate[col]; position[1] = -coordinate[row]; position[2] = 5; break;
    case 3: position[0] = 5; position[1] = -coordinate[row]; position[2] = -coordinate[col]; break;
    case 4: position[0] = -coordinate[col]; position[1] = -coordinate[row]; position[2] = -5; break;
    default: position[0] = coordinate[col]; position[1] = -5; position[2] = -coordinate[row]; break;
    }
}

static void bar_init_symmetry(void)
{
    static const unsigned char axis_permutations[2][3] = {{0, 1, 2}, {0, 2, 1}};
    int8_t coordinates[BAR_SQUARES][3];
    unsigned int symmetry = 0;

    for (unsigned int bit = 0; bit < BAR_SQUARES; bit++) {
        bar_square_position(bar_square(bit), coordinates[bit]);
    }
    for (unsigned int permutation = 0; permutation < 2; permutation++) {
        const unsigned char *axes = axis_permutations[permutation];

        for (unsigned int sign_bits = 0; sign_bits < 8; sign_bits++, symmetry++) {
            for (unsigned int source = 0; source < BAR_SQUARES; source++) {
                int8_t image[3] = {0, 0, 0};
                unsigned int destination = BAR_SQUARES;

                for (unsigned int axis = 0; axis < 3; axis++) {
                    int sign = (sign_bits & (1u << axis)) ? 1 : -1;

                    image[axes[axis]] = (int8_t)(sign * coordinates[source][axis]);
                }
                for (unsigned int candidate = 0; candidate < BAR_SQUARES; candidate++) {
                    if (coordinates[candidate][0] == image[0] && coordinates[candidate][1] == image[1] &&
                        coordinates[candidate][2] == image[2]) {
                        destination = candidate;
                        break;
                    }
                }
                if (destination == BAR_SQUARES) {
                    fprintf(stderr, "ERROR: LR-axis symmetry leaves the oblique coordinate\n");
                    exit(1);
                }
                bar_symmetry_position[symmetry][source] = (unsigned char)destination;
            }
        }
    }
    if (symmetry != BAR_SYMMETRIES) {
        fprintf(stderr, "ERROR: expected 16 LR-axis symmetries\n");
        exit(1);
    }
    for (unsigned int map = 0; map < BAR_SYMMETRIES; map++) {
        for (unsigned int byte = 0; byte < 6; byte++) {
            for (unsigned int value = 0; value < 256; value++) {
                uint64_t transformed = 0;

                for (unsigned int bit = 0; bit < 8; bit++) {
                    if (value & (1u << bit)) {
                        transformed |= UINT64_C(1) << bar_symmetry_position[map][byte * 8 + bit];
                    }
                }
                bar_symmetry_byte_map[map][byte][value] = transformed;
            }
        }
    }
}

static inline uint64_t bar_transform(uint64_t key, unsigned int symmetry)
{
    const uint64_t (*map)[256] = bar_symmetry_byte_map[symmetry];

    return map[0][key & 0xff] | map[1][(key >> 8) & 0xff] | map[2][(key >> 16) & 0xff] |
           map[3][(key >> 24) & 0xff] | map[4][(key >> 32) & 0xff] | map[5][(key >> 40) & 0xff];
}

static inline uint64_t bar_canonical_key(uint64_t key)
{
    uint64_t canonical = UINT64_MAX;

    for (unsigned int symmetry = 0; symmetry < BAR_SYMMETRIES; symmetry++) {
        uint64_t transformed = bar_transform(key, symmetry);

        if (transformed < canonical) {
            canonical = transformed;
        }
    }
    return canonical;
}

static inline uint64_t bar_hash_index(uint64_t key, unsigned int shift)
{
    return (key * UINT64_C(0x9E3779B97F4A7C15)) >> shift;
}

static int move_is_allowed(move_type move)
{
    switch (move) {
    case threeUw:
    case threeUw_PRIME:
    case threeDw:
    case threeDw_PRIME:
    case threeFw:
    case threeFw_PRIME:
    case threeBw:
    case threeBw_PRIME:
        return 0;
    default:
        return 1;
    }
}

static inline uint64_t bar_apply_move(uint64_t key, unsigned int move_index)
{
    const uint64_t (*map)[256] = bar_byte_map[move_index];

    return map[0][key & 0xff] | map[1][(key >> 8) & 0xff] | map[2][(key >> 16) & 0xff] |
           map[3][(key >> 24) & 0xff] | map[4][(key >> 32) & 0xff] | map[5][(key >> 40) & 0xff];
}

static void bar_init_moves(void)
{
    char cube[CUBE_ARRAY_SIZE];
    char rotate_tmp[CUBE_ARRAY_SIZE];

    bar_init_symmetry();
    ida_init_move_tables(moves_666, MOVE_COUNT_666, move_is_allowed, legal_move_count, legal_move_index, inverse_move);
    bar_move_count = legal_move_count[MOVE_NONE];
    for (unsigned int move_index = 0; move_index < bar_move_count; move_index++) {
        move_type move = moves_666[legal_move_index[MOVE_NONE][move_index]];
        unsigned char destination[BAR_SQUARES];

        memset(cube, '.', sizeof(cube));
        for (unsigned int bit = 0; bit < BAR_SQUARES; bit++) {
            cube[bar_square(bit)] = (char)(64 + bit);
        }
        rotate_666_centers(cube, rotate_tmp, CUBE_ARRAY_SIZE, move);
        for (unsigned int bit = 0; bit < BAR_SQUARES; bit++) {
            int source = cube[bar_square(bit)] - 64;

            if (source < 0 || source >= BAR_SQUARES) {
                fprintf(stderr, "ERROR: %s moves a non-oblique onto an oblique square\n", move2str[move]);
                exit(1);
            }
            destination[source] = (unsigned char)bit;
            bar_move_position[move_index][source] = (unsigned char)bit;
        }
        for (unsigned int byte = 0; byte < 6; byte++) {
            for (unsigned int value = 0; value < 256; value++) {
                uint64_t moved = 0;

                for (unsigned int bit = 0; bit < 8; bit++) {
                    if (value & (1u << bit)) {
                        moved |= UINT64_C(1) << destination[byte * 8 + bit];
                    }
                }
                bar_byte_map[move_index][byte][value] = moved;
            }
        }
    }
    for (unsigned int symmetry = 0; symmetry < BAR_SYMMETRIES; symmetry++) {
        for (unsigned int move = 0; move < bar_move_count; move++) {
            int found = 0;

            for (unsigned int candidate = 0; candidate < bar_move_count && !found; candidate++) {
                found = 1;
                for (unsigned int bit = 0; bit < BAR_SQUARES; bit++) {
                    unsigned int left = bar_symmetry_position[symmetry][bar_move_position[move][bit]];
                    unsigned int right = bar_move_position[candidate][bar_symmetry_position[symmetry][bit]];

                    if (left != right) {
                        found = 0;
                        break;
                    }
                }
            }
            if (!found) {
                fprintf(
                    stderr,
                    "ERROR: LR symmetry %u does not conjugate legal move %s onto a legal move\n",
                    symmetry,
                    move2str[moves_666[legal_move_index[MOVE_NONE][move]]]
                );
                exit(1);
            }
        }
    }
}

static uint64_t *bar_allocate(unsigned int log2)
{
    size_t bytes = sizeof(uint64_t) << log2;
    void *slots = mmap(NULL, bytes, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    if (slots == MAP_FAILED) {
        fprintf(stderr, "ERROR: could not allocate %zu bytes for the LR bar table\n", bytes);
        exit(1);
    }
    return slots;
}

static void bar_use_table(uint64_t *slots, unsigned int log2, double max_load)
{
    bar_build.slots = slots;
    bar_build.log2 = log2;
    bar_build.mask = (UINT64_C(1) << log2) - 1;
    bar_build.shift = 64 - log2;
    bar_build.limit = (uint64_t)((double)(UINT64_C(1) << log2) * max_load);
}

static int bar_insert(uint64_t key, unsigned char cost)
{
    uint64_t packed = key | ((uint64_t)cost << BAR_COST_SHIFT);
    uint64_t index = bar_hash_index(key, bar_build.shift);

    while (1) {
        uint64_t slot = __atomic_load_n(&bar_build.slots[index], __ATOMIC_RELAXED);

        if (!slot) {
            uint64_t expected = 0;

            if (__atomic_compare_exchange_n(
                    &bar_build.slots[index], &expected, packed, 0, __ATOMIC_RELAXED, __ATOMIC_RELAXED)) {
                return 1;
            }
            slot = expected;
        }
        if ((slot & BAR_KEY_MASK) == key) {
            return 0;
        }
        index = (index + 1) & bar_build.mask;
    }
}

static void bar_count_inserts(uint64_t *pending, int force)
{
    if (*pending >= BAR_COUNT_BATCH || (force && *pending)) {
        uint64_t total = atomic_fetch_add(&bar_build.count, *pending) + *pending;

        *pending = 0;
        if (total > bar_build.limit) {
            atomic_store(&bar_build.overflow, 1);
        }
    }
}

static void *bar_expand_level(void *argument)
{
    struct bar_worker *worker = argument;
    uint64_t capacity = bar_build.mask + 1;
    uint64_t begin = capacity / worker->threads * worker->index;
    uint64_t end = worker->index + 1 == worker->threads ? capacity : capacity / worker->threads * (worker->index + 1);
    uint64_t pending = 0;

    for (uint64_t index = begin; index < end; index++) {
        uint64_t slot = __atomic_load_n(&bar_build.slots[index], __ATOMIC_RELAXED);
        uint64_t key;

        if (!slot || (slot >> BAR_COST_SHIFT) != worker->depth) {
            continue;
        }
        if (atomic_load_explicit(&bar_build.overflow, memory_order_relaxed)) {
            break;
        }
        key = slot & BAR_KEY_MASK;
        for (unsigned int move_index = 0; move_index < bar_move_count; move_index++) {
            pending += (uint64_t)bar_insert(bar_canonical_key(bar_apply_move(key, move_index)), (unsigned char)(worker->depth + 1));
        }
        bar_count_inserts(&pending, 0);
    }
    bar_count_inserts(&pending, 1);
    return NULL;
}

static void *bar_rehash_range(void *argument)
{
    struct bar_worker *worker = argument;
    uint64_t begin = bar_build.old_capacity / worker->threads * worker->index;
    uint64_t end = worker->index + 1 == worker->threads ? bar_build.old_capacity
                                                        : bar_build.old_capacity / worker->threads * (worker->index + 1);

    for (uint64_t index = begin; index < end; index++) {
        uint64_t slot = bar_build.old_slots[index];

        if (slot) {
            bar_insert(slot & BAR_KEY_MASK, (unsigned char)(slot >> BAR_COST_SHIFT));
        }
    }
    return NULL;
}

static void bar_run_threads(void *(*routine)(void *), unsigned int threads, unsigned char depth)
{
    pthread_t handles[MAX_THREADS];
    struct bar_worker workers[MAX_THREADS];

    for (unsigned int index = 0; index < threads; index++) {
        workers[index].index = index;
        workers[index].threads = threads;
        workers[index].depth = depth;
        if (pthread_create(&handles[index], NULL, routine, &workers[index]) != 0) {
            fprintf(stderr, "ERROR: could not create LR bar thread %u\n", index);
            exit(1);
        }
    }
    for (unsigned int index = 0; index < threads; index++) {
        pthread_join(handles[index], NULL);
    }
}

static void bar_rehash(unsigned int log2, unsigned int threads, double max_load)
{
    uint64_t old_capacity = bar_build.mask + 1;
    uint64_t *old_slots = bar_build.slots;

    bar_build.old_slots = old_slots;
    bar_build.old_capacity = old_capacity;
    bar_use_table(bar_allocate(log2), log2, max_load);
    bar_run_threads(bar_rehash_range, threads, 0);
    munmap(old_slots, sizeof(uint64_t) * old_capacity);
    bar_build.old_slots = NULL;
}

static double bar_seconds_since(const struct timeval *start)
{
    struct timeval now;

    gettimeofday(&now, NULL);
    return (double)(now.tv_sec - start->tv_sec) + (double)(now.tv_usec - start->tv_usec) / 1000000.0;
}

static int build_lr_bar_table(const char *filename, unsigned char depth, unsigned int threads)
{
    const double build_load = 0.75;
    const double file_load = 0.5;
    struct bar_header header;
    struct timeval start;
    unsigned char completed = 0;
    unsigned int file_log2;
    uint64_t raw_goals = 0;
    uint64_t goals = 0;
    char temporary[PATH_MAX];
    FILE *fh;

    memset(&header, 0, sizeof(header));
    memcpy(header.magic, BAR_MAGIC, sizeof(BAR_MAGIC));
    gettimeofday(&start, NULL);
    bar_init_moves();
    bar_use_table(bar_allocate(BAR_FIRST_LOG2), BAR_FIRST_LOG2, build_load);
    atomic_store(&bar_build.count, 0);
    atomic_store(&bar_build.overflow, 0);

    for (uint32_t pairs = 0xff; pairs < (UINT32_C(1) << OBLIQUE_PAIR_COUNT);) {
        uint32_t low = pairs & -pairs;
        uint32_t ripple = pairs + low;

        raw_goals++;
        goals += (uint64_t)bar_insert(bar_canonical_key((uint64_t)pairs | ((uint64_t)pairs << OBLIQUE_PAIR_COUNT)), 0);
        pairs = (((ripple ^ pairs) >> 2) / low) | ripple;
    }
    atomic_store(&bar_build.count, goals);
    header.depth_count[0] = goals;
    LOG(
        "LR bar table: %u legal phase-2 moves, %'llu raw goals, %'llu canonical goals\n",
        bar_move_count,
        (unsigned long long)raw_goals,
        (unsigned long long)goals
    );

    for (unsigned char level = 0; level < depth; level++) {
        uint64_t before = atomic_load(&bar_build.count);
        int full = 0;

        while (1) {
            atomic_store(&bar_build.overflow, 0);
            bar_run_threads(bar_expand_level, threads, level);
            if (!atomic_load(&bar_build.overflow)) {
                break;
            }
            if (bar_build.log2 >= BAR_MAX_LOG2) {
                full = 1;
                break;
            }
            LOG("LR bar table: growing to 2^%u slots during depth %u\n", bar_build.log2 + 1, level + 1);
            bar_rehash(bar_build.log2 + 1, threads, build_load);
            {
                uint64_t recount = 0;

                for (uint64_t index = 0; index <= bar_build.mask; index++) {
                    recount += bar_build.slots[index] != 0;
                }
                atomic_store(&bar_build.count, recount);
            }
        }
        header.depth_count[level + 1] = atomic_load(&bar_build.count) - before;
        LOG(
            "LR bar table: depth %u has %'llu entries, %'llu total, %.1fs\n",
            level + 1,
            (unsigned long long)header.depth_count[level + 1],
            (unsigned long long)atomic_load(&bar_build.count),
            bar_seconds_since(&start)
        );
        if (full) {
            fprintf(stderr, "ERROR: LR bar depth %u did not fit in 2^%u slots; no table was written\n", level + 1, BAR_MAX_LOG2);
            return 1;
        }
        completed = (unsigned char)(level + 1);
    }

    header.depth = completed;
    header.count = atomic_load(&bar_build.count);
    {
        uint64_t counted = 0;

        for (unsigned int level = 0; level <= completed; level++) {
            counted += header.depth_count[level];
        }
        if (completed != depth || counted != header.count) {
            fprintf(stderr, "ERROR: LR bar table did not complete depth %u consistently\n", depth);
            return 1;
        }
    }
    file_log2 = BAR_FIRST_LOG2;
    while (file_log2 < BAR_MAX_LOG2 && (double)header.count > (double)(UINT64_C(1) << file_log2) * file_load) {
        file_log2++;
    }
    if (file_log2 != bar_build.log2) {
        bar_rehash(file_log2, threads, 1.0);
    }
    header.log2_capacity = bar_build.log2;
    if (snprintf(temporary, sizeof(temporary), "%s.tmp.%ld", filename, (long)getpid()) >= (int)sizeof(temporary)) {
        fprintf(stderr, "ERROR: LR bar table filename is too long\n");
        return 1;
    }
    fh = fopen(temporary, "wb");
    if (!fh) {
        fprintf(stderr, "ERROR: could not write %s: %s\n", temporary, strerror(errno));
        return 1;
    }
    if (fwrite(&header, sizeof(header), 1, fh) != 1 ||
        fwrite(bar_build.slots, sizeof(uint64_t), (size_t)bar_build.mask + 1, fh) != (size_t)bar_build.mask + 1 ||
        fflush(fh) != 0 || fsync(fileno(fh)) != 0 || fclose(fh) != 0) {
        fprintf(stderr, "ERROR: could not write %s\n", temporary);
        unlink(temporary);
        return 1;
    }
    if (rename(temporary, filename) != 0) {
        fprintf(stderr, "ERROR: could not rename %s to %s: %s\n", temporary, filename, strerror(errno));
        unlink(temporary);
        return 1;
    }
    LOG(
        "LR bar table: wrote %s, depth %u, %'llu entries in 2^%u slots, %.1fs\n",
        filename,
        header.depth,
        (unsigned long long)header.count,
        header.log2_capacity,
        bar_seconds_since(&start)
    );
    for (unsigned int level = 0; level <= header.depth; level++) {
        printf("%u steps has %'llu entries\n", level, (unsigned long long)header.depth_count[level]);
    }
    return 0;
}

static void usage(const char *program)
{
    fprintf(
        stderr,
        "usage: %s --output FILE [--depth N] [--threads N]\n"
        "  write the symmetry-reduced 6x6 phase-2 LR bar table; depth defaults to 3\n",
        program
    );
}

int main(int argc, char **argv)
{
    const char *filename = NULL;
    unsigned int depth = 3;
    long detected = sysconf(_SC_NPROCESSORS_ONLN);
    unsigned int threads = detected > 0 ? (unsigned int)detected : 1;

    if (threads > MAX_THREADS) {
        threads = MAX_THREADS;
    }
    for (int index = 1; index < argc; index++) {
        if (!strcmp(argv[index], "--output") && index + 1 < argc) {
            filename = argv[++index];
        } else if (!strcmp(argv[index], "--depth") && index + 1 < argc) {
            depth = (unsigned int)strtoul(argv[++index], NULL, 10);
        } else if (!strcmp(argv[index], "--threads") && index + 1 < argc) {
            threads = (unsigned int)strtoul(argv[++index], NULL, 10);
        } else {
            usage(argv[0]);
            return 2;
        }
    }
    if (!filename || !depth || depth >= BAR_MAX_DEPTH || !threads || threads > MAX_THREADS) {
        usage(argv[0]);
        return 2;
    }
    setvbuf(stdout, NULL, _IOLBF, 0);
    setlocale(LC_NUMERIC, "");
    return build_lr_bar_table(filename, (unsigned char)depth, threads);
}

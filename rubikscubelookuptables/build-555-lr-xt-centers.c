/*
 * Joint L/R x-center and L/R t-center staging table for the 5x5x5.
 *
 * The raw coordinate is C(24,8) x C(24,8) = 540,917,591,841 states. The 16
 * cube symmetries that preserve the L/R axis leave the distance unchanged, and
 * there are 33,807,856,581 orbits. This builder classifies every raw rank once,
 * writes a rank-select index, then runs BFS directly on the dense orbits.
 *
 * Resident during the search, before queues and the operating system:
 *   rank bitmap      63.0 GiB
 *   uint64 counters   7.9 GiB
 *   dense costs      31.5 GiB
 *   total           102.3 GiB
 *
 * The frontier is sequential and stays on disk. Pass --lock to mlock the
 * tables so page cache from that frontier cannot evict them.
 *
 * Cost bytes use the ranked-table encoding: 0 = unseen, nonzero = depth + 1.
 * Raw rank is x_rank * 735471 + t_rank, with the same C(24,8) order as
 * ida_search_555_phase1.c. A lookup canonicalizes under the 16 symmetries,
 * then rank-selects that raw rank into the dense cost array.
 */

#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <time.h>
#include <unistd.h>

#include "ida_search_core.h"

void rotate_555(char *cube, char *cube_tmp, int array_size, move_type move);

#define CUBE_SIZE 151
#define GROUP_SIZE 24
#define SELECTED_COUNT 8
#define GROUP_UNIVERSE UINT64_C(735471)
#define RAW_UNIVERSE (GROUP_UNIVERSE * GROUP_UNIVERSE)
#define ORBIT_COUNT UINT64_C(33807856581)
#define SYMMETRY_COUNT 16
#define SEARCH_MOVE_COUNT 36
#define BLOCK_BITS 512
#define BLOCK_WORDS (BLOCK_BITS / 64)
#define INDEX_MAGIC "LRXT5551"
#define MAX_DEPTH 40

static const unsigned int x_squares[GROUP_SIZE] = {
    7, 9, 17, 19, 32, 34, 42, 44, 57, 59, 67, 69,
    82, 84, 92, 94, 107, 109, 117, 119, 132, 134, 142, 144,
};
static const unsigned int t_squares[GROUP_SIZE] = {
    8, 12, 14, 18, 33, 37, 39, 43, 58, 62, 64, 68,
    83, 87, 89, 93, 108, 112, 114, 118, 133, 137, 139, 143,
};

/* Face frames calibrated so geometric X, Y, and Z match rotate_555. */
static const int normal_axis[6] = {1, 0, 2, 0, 2, 1};
static const int normal_sign[6] = {1, -1, 1, 1, -1, -1};
static const int tangent0[6] = {0, 2, 0, 2, 0, 0};
static const int tangent1[6] = {2, 1, 1, 1, 1, 2};
static const int sign0[6] = {1, 1, 1, -1, -1, 1};
static const int sign1[6] = {1, -1, -1, -1, -1, -1};

struct index_header {
    char magic[8];
    uint64_t raw_universe;
    uint64_t orbit_count;
    uint64_t block_count;
    uint64_t block_bits;
    uint64_t counter_bytes;
    uint64_t unused[2];
};

_Static_assert(sizeof(struct index_header) == 64, "index header must be 64 bytes");

struct builder {
    unsigned char *index_base;
    uint64_t *bitmap;
    uint64_t *counters;
    unsigned char *costs;
    size_t index_bytes;
    size_t cost_bytes;
    uint64_t block_count;
    uint32_t *rank_of;
    uint32_t *mask_of_rank;
    uint64_t binom[GROUP_SIZE + 1][SELECTED_COUNT + 1];
    uint8_t move_perm[SEARCH_MOVE_COUNT][2][GROUP_SIZE];
    uint8_t symmetry_perm[SYMMETRY_COUNT][2][GROUP_SIZE];
    uint32_t goal_x;
    uint32_t goal_t;
    int threads;
    int lock_tables;
    char work_dir[512];
    uint64_t depth_count[MAX_DEPTH + 1];
};

static struct builder builder;
static pthread_mutex_t frontier_mutex = PTHREAD_MUTEX_INITIALIZER;

static void fail(const char *message)
{
    fprintf(stderr, "ERROR: %s%s%s\n", message, errno ? ": " : "", errno ? strerror(errno) : "");
    exit(1);
}

static uint64_t block_count_of(void)
{
    return (RAW_UNIVERSE + BLOCK_BITS - 1) / BLOCK_BITS;
}

static void init_binom(void)
{
    for (int n = 0; n <= GROUP_SIZE; n++) {
        builder.binom[n][0] = 1;
        for (int k = 1; k <= SELECTED_COUNT && k <= n; k++) {
            builder.binom[n][k] = builder.binom[n - 1][k - 1] + builder.binom[n - 1][k];
        }
    }
    if (builder.binom[GROUP_SIZE][SELECTED_COUNT] != GROUP_UNIVERSE) {
        fail("C(24,8) is not 735471");
    }
}

static uint32_t combination_rank(uint32_t selected)
{
    uint64_t rank = 0;
    unsigned int remaining = SELECTED_COUNT;

    for (unsigned int position = 0; position < GROUP_SIZE; position++) {
        unsigned int after = GROUP_SIZE - position - 1;

        if (selected & (UINT32_C(1) << position)) {
            remaining--;
        } else if (remaining) {
            rank += builder.binom[after][remaining - 1];
        }
    }
    return (uint32_t)rank;
}

static uint32_t combination_unrank(uint64_t rank)
{
    uint32_t mask = 0;
    unsigned int remaining = SELECTED_COUNT;

    for (unsigned int position = 0; position < GROUP_SIZE && remaining; position++) {
        unsigned int after = GROUP_SIZE - position - 1;
        uint64_t take = builder.binom[after][remaining - 1];

        if (rank < take) {
            mask |= UINT32_C(1) << position;
            remaining--;
        } else {
            rank -= take;
        }
    }
    return mask;
}

static void square_coord(unsigned int square, int coord[3])
{
    unsigned int face = (square - 1) / 25;
    int row = (int)(((square - 1) % 25) / 5) - 2;
    int col = (int)((square - 1) % 25) % 5 - 2;

    coord[0] = coord[1] = coord[2] = 0;
    coord[normal_axis[face]] = normal_sign[face] * 2;
    coord[tangent0[face]] = col * sign0[face];
    coord[tangent1[face]] = row * sign1[face];
}

static unsigned int square_from_coord(const int coord[3], const unsigned int squares[GROUP_SIZE])
{
    for (unsigned int position = 0; position < GROUP_SIZE; position++) {
        int actual[3];

        square_coord(squares[position], actual);
        if (actual[0] == coord[0] && actual[1] == coord[1] && actual[2] == coord[2]) {
            return position;
        }
    }
    return GROUP_SIZE;
}

static void symmetry_coord(unsigned int symmetry, const int in[3], int out[3])
{
    int x = in[0] * ((symmetry & 1) ? -1 : 1);
    int y = in[1] * ((symmetry & 2) ? -1 : 1);
    int z = in[2] * ((symmetry & 4) ? -1 : 1);

    if (symmetry & 8) {
        int swapped = y;
        y = z;
        z = swapped;
    }
    out[0] = x;
    out[1] = y;
    out[2] = z;
}

static uint32_t apply_perm(uint32_t mask, const uint8_t perm[GROUP_SIZE])
{
    uint32_t result = 0;

    for (unsigned int position = 0; position < GROUP_SIZE; position++) {
        if (mask & (UINT32_C(1) << position)) {
            result |= UINT32_C(1) << perm[position];
        }
    }
    return result;
}

static uint64_t raw_rank(uint32_t x_mask, uint32_t t_mask)
{
    return (uint64_t)builder.rank_of[x_mask] * GROUP_UNIVERSE + builder.rank_of[t_mask];
}

static void canonical_masks(uint32_t x_mask, uint32_t t_mask, uint32_t *canonical_x, uint32_t *canonical_t)
{
    uint64_t best = UINT64_MAX;

    for (unsigned int symmetry = 0; symmetry < SYMMETRY_COUNT; symmetry++) {
        uint32_t image_x = apply_perm(x_mask, builder.symmetry_perm[symmetry][0]);
        uint32_t image_t = apply_perm(t_mask, builder.symmetry_perm[symmetry][1]);
        uint64_t rank = raw_rank(image_x, image_t);

        if (rank < best) {
            best = rank;
            *canonical_x = image_x;
            *canonical_t = image_t;
        }
    }
}

static int masks_are_canonical(uint32_t x_mask, uint32_t t_mask)
{
    uint32_t canonical_x = 0;
    uint32_t canonical_t = 0;

    canonical_masks(x_mask, t_mask, &canonical_x, &canonical_t);
    return canonical_x == x_mask && canonical_t == t_mask;
}

static void build_rank_table(void)
{
    builder.rank_of = malloc(((size_t)1 << GROUP_SIZE) * sizeof(uint32_t));
    builder.mask_of_rank = malloc((size_t)GROUP_UNIVERSE * sizeof(uint32_t));
    if (!builder.rank_of || !builder.mask_of_rank) {
        fail("could not allocate combination rank table");
    }
    memset(builder.rank_of, 0xff, ((size_t)1 << GROUP_SIZE) * sizeof(uint32_t));
    for (uint64_t rank = 0; rank < GROUP_UNIVERSE; rank++) {
        uint32_t mask = combination_unrank(rank);

        if (combination_rank(mask) != rank || __builtin_popcount(mask) != SELECTED_COUNT) {
            fail("combination rank does not round-trip");
        }
        builder.rank_of[mask] = (uint32_t)rank;
        builder.mask_of_rank[rank] = mask;
    }
}

static uint32_t goal_mask(const unsigned int squares[GROUP_SIZE])
{
    uint32_t mask = 0;

    for (unsigned int position = 0; position < GROUP_SIZE; position++) {
        unsigned int face = (squares[position] - 1) / 25;

        if (face == 1 || face == 3) {
            mask |= UINT32_C(1) << position;
        }
    }
    if (__builtin_popcount(mask) != SELECTED_COUNT) {
        fail("L/R goal is not an 8-subset");
    }
    return mask;
}

static void init_symmetries(void)
{
    for (unsigned int symmetry = 0; symmetry < SYMMETRY_COUNT; symmetry++) {
        for (unsigned int kind = 0; kind < 2; kind++) {
            const unsigned int *squares = kind ? t_squares : x_squares;

            for (unsigned int position = 0; position < GROUP_SIZE; position++) {
                int coord[3];
                int image[3];
                unsigned int destination;

                square_coord(squares[position], coord);
                symmetry_coord(symmetry, coord, image);
                destination = square_from_coord(image, squares);
                if (destination >= GROUP_SIZE) {
                    fail("symmetry does not preserve the center orbit");
                }
                builder.symmetry_perm[symmetry][kind][position] = (uint8_t)destination;
            }
        }
    }
    builder.goal_x = goal_mask(x_squares);
    builder.goal_t = goal_mask(t_squares);
}

static void move_permutation(move_type move, const unsigned int squares[GROUP_SIZE], uint8_t perm[GROUP_SIZE])
{
    char cube[CUBE_SIZE];
    char scratch[CUBE_SIZE];
    int position_of[CUBE_SIZE];

    for (int square = 0; square < CUBE_SIZE; square++) {
        cube[square] = (char)square;
        position_of[square] = -1;
    }
    for (unsigned int position = 0; position < GROUP_SIZE; position++) {
        position_of[squares[position]] = (int)position;
    }
    rotate_555(cube, scratch, CUBE_SIZE, move);
    for (unsigned int source = 0; source < GROUP_SIZE; source++) {
        int destination = -1;

        for (int square = 1; square < CUBE_SIZE; square++) {
            if ((unsigned char)cube[square] == squares[source]) {
                destination = position_of[square];
                break;
            }
        }
        if (destination < 0) {
            fail("center orbit is not closed under a search move");
        }
        perm[source] = (uint8_t)destination;
    }
}

static int same_perm(const uint8_t left[GROUP_SIZE], const uint8_t right[GROUP_SIZE])
{
    return memcmp(left, right, GROUP_SIZE) == 0;
}

static void compose(const uint8_t left[GROUP_SIZE], const uint8_t right[GROUP_SIZE], uint8_t out[GROUP_SIZE])
{
    for (unsigned int position = 0; position < GROUP_SIZE; position++) {
        out[position] = left[right[position]];
    }
}

static void invert_perm(const uint8_t perm[GROUP_SIZE], uint8_t inverse[GROUP_SIZE])
{
    for (unsigned int position = 0; position < GROUP_SIZE; position++) {
        inverse[perm[position]] = (uint8_t)position;
    }
}

static int perm_matches_move(move_type move, unsigned int symmetry)
{
    uint8_t expected_x[GROUP_SIZE];
    uint8_t expected_t[GROUP_SIZE];

    move_permutation(move, x_squares, expected_x);
    move_permutation(move, t_squares, expected_t);
    return same_perm(builder.symmetry_perm[symmetry][0], expected_x) &&
           same_perm(builder.symmetry_perm[symmetry][1], expected_t);
}

static int symmetry_contains_move(move_type move)
{
    for (unsigned int symmetry = 0; symmetry < SYMMETRY_COUNT; symmetry++) {
        if (perm_matches_move(move, symmetry)) {
            return 1;
        }
    }
    return 0;
}

static void init_moves(void)
{
    /* moves_555 is the 36 outer and wide turns. The move enum inserts
     * three-wide turns before those 36 are finished, so a prefix of the enum
     * is not the 5x5 search move set. */
    for (unsigned int move = 0; move < SEARCH_MOVE_COUNT; move++) {
        move_permutation(moves_555[move], x_squares, builder.move_perm[move][0]);
        move_permutation(moves_555[move], t_squares, builder.move_perm[move][1]);
    }
}

static void check_geometry(void)
{
    /* X turns the L/R axis and is one of the 16 symmetries. Y and Z send that
     * axis to F/B or U/D, so they must stay outside this group. */
    if (!symmetry_contains_move(X) || !symmetry_contains_move(X_PRIME)) {
        fail("an L/R-axis rotation is missing from the symmetry group");
    }
    if (symmetry_contains_move(Y) || symmetry_contains_move(Z)) {
        fail("a symmetry moves the L/R axis");
    }
    for (unsigned int left = 0; left < SYMMETRY_COUNT; left++) {
        for (unsigned int right = left + 1; right < SYMMETRY_COUNT; right++) {
            if (same_perm(builder.symmetry_perm[left][0], builder.symmetry_perm[right][0]) &&
                same_perm(builder.symmetry_perm[left][1], builder.symmetry_perm[right][1])) {
                fail("two symmetry ids induce the same center permutation");
            }
        }
    }
    for (unsigned int symmetry = 0; symmetry < SYMMETRY_COUNT; symmetry++) {
        if (apply_perm(builder.goal_x, builder.symmetry_perm[symmetry][0]) != builder.goal_x ||
            apply_perm(builder.goal_t, builder.symmetry_perm[symmetry][1]) != builder.goal_t) {
            fail("a symmetry moves the L/R goal");
        }
        for (unsigned int kind = 0; kind < 2; kind++) {
            for (unsigned int move = 0; move < SEARCH_MOVE_COUNT; move++) {
                uint8_t inverse[GROUP_SIZE];
                uint8_t conjugated[GROUP_SIZE];
                uint8_t tmp[GROUP_SIZE];
                int found = 0;

                invert_perm(builder.symmetry_perm[symmetry][kind], inverse);
                compose(builder.symmetry_perm[symmetry][kind], builder.move_perm[move][kind], tmp);
                compose(tmp, inverse, conjugated);
                for (unsigned int candidate = 0; candidate < SEARCH_MOVE_COUNT; candidate++) {
                    if (same_perm(conjugated, builder.move_perm[candidate][kind])) {
                        found = 1;
                        break;
                    }
                }
                if (!found) {
                    fail("a symmetry does not conjugate a search move to a search move");
                }
            }
        }
    }
    if (!masks_are_canonical(builder.goal_x, builder.goal_t)) {
        fail("the L/R goal is not the canonical state of its orbit");
    }
}

static uint64_t dense_rank(uint64_t raw)
{
    uint64_t word = raw >> 6;
    uint64_t block = raw / BLOCK_BITS;
    uint64_t bit = raw & 63;
    uint64_t dense;

    if (raw >= RAW_UNIVERSE || !(builder.bitmap[word] & (UINT64_C(1) << bit))) {
        return UINT64_MAX;
    }
    dense = builder.counters[block];
    for (uint64_t scan = block * BLOCK_WORDS; scan < word; scan++) {
        dense += (unsigned int)__builtin_popcountll(builder.bitmap[scan]);
    }
    return dense + (unsigned int)__builtin_popcountll(builder.bitmap[word] & ((UINT64_C(1) << bit) - 1));
}

struct index_slice {
    uint64_t x_begin;
    uint64_t x_end;
};

static void *mark_canonical_slice(void *argument)
{
    struct index_slice *slice = argument;

    for (uint64_t x_rank = slice->x_begin; x_rank < slice->x_end; x_rank++) {
        uint32_t x_mask = builder.mask_of_rank[x_rank];
        uint32_t image_x[SYMMETRY_COUNT];
        uint32_t image_x_rank[SYMMETRY_COUNT];

        for (unsigned int symmetry = 0; symmetry < SYMMETRY_COUNT; symmetry++) {
            image_x[symmetry] = apply_perm(x_mask, builder.symmetry_perm[symmetry][0]);
            image_x_rank[symmetry] = builder.rank_of[image_x[symmetry]];
        }
        for (uint64_t t_rank = 0; t_rank < GROUP_UNIVERSE; t_rank++) {
            uint32_t t_mask = builder.mask_of_rank[t_rank];
            uint64_t raw = x_rank * GROUP_UNIVERSE + t_rank;
            uint64_t best = raw;

            for (unsigned int symmetry = 0; symmetry < SYMMETRY_COUNT; symmetry++) {
                uint32_t image_t = apply_perm(t_mask, builder.symmetry_perm[symmetry][1]);
                uint64_t image = (uint64_t)image_x_rank[symmetry] * GROUP_UNIVERSE + builder.rank_of[image_t];

                if (image < best) {
                    best = image;
                }
            }
            if (best == raw) {
                __atomic_fetch_or(&builder.bitmap[raw >> 6], UINT64_C(1) << (raw & 63), __ATOMIC_RELAXED);
            }
        }
        if ((x_rank % 4096) == 0) {
            fprintf(stderr, "index x-rank %" PRIu64 "/%" PRIu64 "\n", x_rank, GROUP_UNIVERSE);
        }
    }
    return NULL;
}

static void build_index(const char *path)
{
    pthread_t *threads;
    struct index_slice *slices;
    struct index_header header;
    uint64_t seen = 0;
    int fd;

    builder.block_count = block_count_of();
    builder.index_bytes = sizeof(header) + builder.block_count * BLOCK_WORDS * sizeof(uint64_t) +
                          builder.block_count * sizeof(uint64_t);
    fd = open(path, O_RDWR | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        fail("could not create symmetry index");
    }
    if (ftruncate(fd, (off_t)builder.index_bytes) != 0) {
        fail("could not size symmetry index");
    }
    builder.index_base = mmap(NULL, builder.index_bytes, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (builder.index_base == MAP_FAILED) {
        fail("could not map symmetry index");
    }
    memset(builder.index_base, 0, builder.index_bytes);
    /* The header occupies the first 64 bytes. The bitmap follows it. */
    builder.bitmap = (uint64_t *)(builder.index_base + sizeof(header));
    builder.counters = builder.bitmap + builder.block_count * BLOCK_WORDS;
    threads = calloc((size_t)builder.threads, sizeof(*threads));
    slices = calloc((size_t)builder.threads, sizeof(*slices));
    if (!threads || !slices) {
        fail("could not allocate index threads");
    }
    for (int thread = 0; thread < builder.threads; thread++) {
        slices[thread].x_begin = (GROUP_UNIVERSE * (uint64_t)thread) / (uint64_t)builder.threads;
        slices[thread].x_end = (GROUP_UNIVERSE * (uint64_t)(thread + 1)) / (uint64_t)builder.threads;
        if (pthread_create(&threads[thread], NULL, mark_canonical_slice, &slices[thread]) != 0) {
            fail("could not start index thread");
        }
    }
    for (int thread = 0; thread < builder.threads; thread++) {
        pthread_join(threads[thread], NULL);
    }
    free(threads);
    free(slices);
    for (uint64_t block = 0; block < builder.block_count; block++) {
        builder.counters[block] = seen;
        for (unsigned int word = 0; word < BLOCK_WORDS; word++) {
            seen += (unsigned int)__builtin_popcountll(builder.bitmap[block * BLOCK_WORDS + word]);
        }
    }
    if (seen != ORBIT_COUNT) {
        fprintf(stderr, "ERROR: index has %" PRIu64 " orbits, expected %" PRIu64 "\n", seen, ORBIT_COUNT);
        exit(1);
    }
    memset(&header, 0, sizeof(header));
    memcpy(header.magic, INDEX_MAGIC, sizeof(header.magic));
    header.raw_universe = RAW_UNIVERSE;
    header.orbit_count = ORBIT_COUNT;
    header.block_count = builder.block_count;
    header.block_bits = BLOCK_BITS;
    header.counter_bytes = sizeof(uint64_t);
    if (pwrite(fd, &header, sizeof(header), 0) != (ssize_t)sizeof(header)) {
        fail("could not write symmetry index header");
    }
    if (builder.lock_tables && mlock(builder.index_base, builder.index_bytes) != 0) {
        fprintf(stderr, "warning: could not lock symmetry index in RAM: %s\n", strerror(errno));
    }
    close(fd);
    fprintf(stderr, "symmetry index has %" PRIu64 " orbits\n", ORBIT_COUNT);
}

struct expand_job {
    int input_fd;
    uint64_t begin;
    uint64_t end;
    FILE *output;
    unsigned int depth;
    uint64_t claimed;
};

static void *expand_slice(void *argument)
{
    struct expand_job *job = argument;
    uint64_t record;
    uint64_t buffer[4096];
    size_t buffered = 0;

    for (uint64_t offset = job->begin; offset < job->end; offset++) {
        uint32_t x_mask;
        uint32_t t_mask;
        ssize_t got = pread(job->input_fd, &record, sizeof(record), (off_t)(offset * sizeof(record)));

        if (got != (ssize_t)sizeof(record)) {
            fail("could not read frontier");
        }
        x_mask = (uint32_t)(record >> 32);
        t_mask = (uint32_t)record;
        for (unsigned int move = 0; move < SEARCH_MOVE_COUNT; move++) {
            uint32_t child_x = apply_perm(x_mask, builder.move_perm[move][0]);
            uint32_t child_t = apply_perm(t_mask, builder.move_perm[move][1]);
            uint32_t canonical_x;
            uint32_t canonical_t;
            uint64_t dense;
            unsigned char expected = 0;

            canonical_masks(child_x, child_t, &canonical_x, &canonical_t);
            dense = dense_rank(raw_rank(canonical_x, canonical_t));
            if (dense >= ORBIT_COUNT) {
                fail("canonical state is missing from the symmetry index");
            }
            if (__atomic_compare_exchange_n(
                    &builder.costs[dense], &expected, (unsigned char)(job->depth + 1),
                    0, __ATOMIC_RELAXED, __ATOMIC_RELAXED)) {
                buffer[buffered++] = ((uint64_t)canonical_x << 32) | canonical_t;
                job->claimed++;
                if (buffered == sizeof(buffer) / sizeof(buffer[0])) {
                    pthread_mutex_lock(&frontier_mutex);
                    if (fwrite(buffer, sizeof(buffer[0]), buffered, job->output) != buffered) {
                        fail("could not write frontier");
                    }
                    pthread_mutex_unlock(&frontier_mutex);
                    buffered = 0;
                }
            }
        }
    }
    if (buffered) {
        pthread_mutex_lock(&frontier_mutex);
        if (fwrite(buffer, sizeof(buffer[0]), buffered, job->output) != buffered) {
            fail("could not write frontier");
        }
        pthread_mutex_unlock(&frontier_mutex);
    }
    return NULL;
}

static void write_metadata(const char *cost_path, unsigned int completed_depth)
{
    char path[1024];
    FILE *file;
    int wrote;

    wrote = snprintf(path, sizeof(path), "%s.json", cost_path);
    if (wrote < 0 || (size_t)wrote >= sizeof(path)) {
        fail("cost path is too long");
    }
    file = fopen(path, "w");
    if (!file) {
        fail("could not write cost metadata");
    }
    fprintf(file,
            "{\n"
            "  \"format\": \"lr-xt-symmetry-555-cost-v1\",\n"
            "  \"cost_encoding\": {\"0\": \"unseen\", \"nonzero\": \"depth + 1\"},\n"
            "  \"rank_order\": \"canonical x_rank * 735471 + t_rank under 16 L/R symmetries\",\n"
            "  \"raw_universe_size\": %" PRIu64 ",\n"
            "  \"symmetry_count\": %d,\n"
            "  \"orbit_count\": %" PRIu64 ",\n"
            "  \"completed_depth\": %u,\n"
            "  \"states_per_depth\": {",
            RAW_UNIVERSE, SYMMETRY_COUNT, ORBIT_COUNT, completed_depth);
    for (unsigned int depth = 0; depth <= completed_depth; depth++) {
        fprintf(file, "%s\n    \"%u\": %" PRIu64, depth ? "," : "", depth, builder.depth_count[depth]);
    }
    fprintf(file, "\n  }\n}\n");
    fclose(file);
}

static void build_costs(const char *cost_path)
{
    char current_path[1024];
    char next_path[1024];
    FILE *seed;
    uint64_t goal;
    int cost_fd;
    unsigned int depth;

    builder.cost_bytes = (size_t)ORBIT_COUNT;
    cost_fd = open(cost_path, O_RDWR | O_CREAT | O_TRUNC, 0644);
    if (cost_fd < 0 || ftruncate(cost_fd, (off_t)builder.cost_bytes) != 0) {
        fail("could not create cost table");
    }
    builder.costs = mmap(NULL, builder.cost_bytes, PROT_READ | PROT_WRITE, MAP_SHARED, cost_fd, 0);
    if (builder.costs == MAP_FAILED) {
        fail("could not map cost table");
    }
    if (builder.lock_tables && mlock(builder.costs, builder.cost_bytes) != 0) {
        fprintf(stderr, "warning: could not lock cost table in RAM: %s\n", strerror(errno));
    }
    close(cost_fd);
    if (snprintf(current_path, sizeof(current_path), "%s/frontier-current.bin", builder.work_dir) >= (int)sizeof(current_path)) {
        fail("work directory path is too long");
    }
    goal = ((uint64_t)builder.goal_x << 32) | builder.goal_t;
    builder.costs[dense_rank(raw_rank(builder.goal_x, builder.goal_t))] = 1;
    builder.depth_count[0] = 1;
    seed = fopen(current_path, "wb");
    if (!seed || fwrite(&goal, sizeof(goal), 1, seed) != 1) {
        fail("could not seed frontier");
    }
    fclose(seed);

    for (depth = 1; depth <= MAX_DEPTH; depth++) {
        struct stat frontier_stat;
        pthread_t *threads;
        struct expand_job *jobs;
        FILE *output;
        uint64_t records;
        uint64_t claimed = 0;
        int input_fd;

        if (snprintf(next_path, sizeof(next_path), "%s/frontier-next.bin", builder.work_dir) >= (int)sizeof(next_path)) {
            fail("work directory path is too long");
        }
        input_fd = open(current_path, O_RDONLY);
        if (input_fd < 0 || fstat(input_fd, &frontier_stat) != 0) {
            fail("could not open frontier");
        }
        records = (uint64_t)frontier_stat.st_size / sizeof(uint64_t);
        output = fopen(next_path, "wb");
        if (!output) {
            fail("could not create next frontier");
        }
        threads = calloc((size_t)builder.threads, sizeof(*threads));
        jobs = calloc((size_t)builder.threads, sizeof(*jobs));
        if (!threads || !jobs) {
            fail("could not allocate search threads");
        }
        for (int thread = 0; thread < builder.threads; thread++) {
            jobs[thread].input_fd = input_fd;
            jobs[thread].begin = (records * (uint64_t)thread) / (uint64_t)builder.threads;
            jobs[thread].end = (records * (uint64_t)(thread + 1)) / (uint64_t)builder.threads;
            jobs[thread].output = output;
            jobs[thread].depth = depth;
            if (pthread_create(&threads[thread], NULL, expand_slice, &jobs[thread]) != 0) {
                fail("could not start search thread");
            }
        }
        for (int thread = 0; thread < builder.threads; thread++) {
            pthread_join(threads[thread], NULL);
            claimed += jobs[thread].claimed;
        }
        free(threads);
        free(jobs);
        fclose(output);
        close(input_fd);
        builder.depth_count[depth] = claimed;
        fprintf(stderr, "depth %u has %" PRIu64 " new orbits\n", depth, claimed);
        if (!claimed) {
            unlink(next_path);
            break;
        }
        if (rename(next_path, current_path) != 0) {
            fail("could not rotate frontier");
        }
    }
    unlink(current_path);
    write_metadata(cost_path, depth - 1);
}

static void self_test(void)
{
    uint32_t seen_x[256];
    uint32_t seen_t[256];
    uint32_t raw_x[256];
    uint32_t raw_t[256];
    unsigned int seen = 0;
    unsigned int raw_seen = 0;
    unsigned int moves_checked = 0;

    init_binom();
    build_rank_table();
    init_symmetries();
    init_moves();
    check_geometry();
    for (unsigned int move = 0; move < SEARCH_MOVE_COUNT; move++) {
        uint32_t child_x = apply_perm(builder.goal_x, builder.move_perm[move][0]);
        uint32_t child_t = apply_perm(builder.goal_t, builder.move_perm[move][1]);
        uint32_t canonical_x;
        uint32_t canonical_t;
        int duplicate = 0;

        canonical_masks(child_x, child_t, &canonical_x, &canonical_t);
        if (!(child_x == builder.goal_x && child_t == builder.goal_t)) {
            int raw_duplicate = 0;

            for (unsigned int earlier = 0; earlier < raw_seen; earlier++) {
                if (raw_x[earlier] == child_x && raw_t[earlier] == child_t) {
                    raw_duplicate = 1;
                    break;
                }
            }
            if (!raw_duplicate) {
                if (raw_seen >= sizeof(raw_x) / sizeof(raw_x[0])) {
                    fail("depth 1 has more raw states than the self-test buffer");
                }
                raw_x[raw_seen] = child_x;
                raw_t[raw_seen] = child_t;
                raw_seen++;
            }
        }
        if (!masks_are_canonical(canonical_x, canonical_t)) {
            fail("canonical child is not stable");
        }
        if (__builtin_popcount(canonical_x) != SELECTED_COUNT || __builtin_popcount(canonical_t) != SELECTED_COUNT) {
            fail("a move changed the number of L/R centers");
        }
        for (unsigned int earlier = 0; earlier < seen; earlier++) {
            if (seen_x[earlier] == canonical_x && seen_t[earlier] == canonical_t) {
                duplicate = 1;
                break;
            }
        }
        if (!duplicate && !(canonical_x == builder.goal_x && canonical_t == builder.goal_t)) {
            if (seen >= sizeof(seen_x) / sizeof(seen_x[0])) {
                fail("depth 1 has more canonical states than the self-test buffer");
            }
            seen_x[seen] = canonical_x;
            seen_t[seen] = canonical_t;
            seen++;
        }
        moves_checked++;
    }
    if (moves_checked != SEARCH_MOVE_COUNT || raw_seen != 4 || seen != 1) {
        fail("depth 1 did not produce the four wide turns of one canonical state");
    }
    printf(
        "self-test ok: 16 symmetries, %u search moves, %u raw states at depth 1, %u canonical\n",
        SEARCH_MOVE_COUNT, raw_seen, seen);
}

static void usage(const char *program)
{
    fprintf(stderr,
            "usage: %s --cost FILE --index FILE [--threads N] [--work-dir DIR] [--lock]\n"
            "       %s --self-test\n",
            program, program);
}

int main(int argc, char **argv)
{
    const char *cost_path = NULL;
    const char *index_path = NULL;
    int self_test_only = 0;

    builder.threads = 1;
    snprintf(builder.work_dir, sizeof(builder.work_dir), "tmp/555-lr-xt-frontier");
    for (int index = 1; index < argc; index++) {
        if (!strcmp(argv[index], "--self-test")) {
            self_test_only = 1;
        } else if (!strcmp(argv[index], "--lock")) {
            builder.lock_tables = 1;
        } else if (!strcmp(argv[index], "--threads") && index + 1 < argc) {
            builder.threads = atoi(argv[++index]);
        } else if (!strcmp(argv[index], "--work-dir") && index + 1 < argc) {
            snprintf(builder.work_dir, sizeof(builder.work_dir), "%s", argv[++index]);
        } else if (!strcmp(argv[index], "--cost") && index + 1 < argc) {
            cost_path = argv[++index];
        } else if (!strcmp(argv[index], "--index") && index + 1 < argc) {
            index_path = argv[++index];
        } else {
            usage(argv[0]);
            return 1;
        }
    }
    if (builder.threads < 1) {
        fail("--threads must be positive");
    }
    if (self_test_only) {
        self_test();
        return 0;
    }
    if (!cost_path || !index_path) {
        usage(argv[0]);
        return 1;
    }
    if (mkdir(builder.work_dir, 0755) != 0 && errno != EEXIST) {
        fail("could not create work directory");
    }
    init_binom();
    build_rank_table();
    init_symmetries();
    init_moves();
    check_geometry();
    build_index(index_path);
    build_costs(cost_path);
    return 0;
}

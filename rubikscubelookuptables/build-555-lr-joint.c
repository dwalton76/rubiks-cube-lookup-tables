/*
 * Builds the joint LR t-center + x-center table for the native 5x5 phase 1.
 *
 *   build-555-lr-joint --output FILE [--threads N] [--max-depth D]
 *   build-555-lr-joint --verify FILE [--samples N] [--max-depth D] [--seed S]
 *
 * Geometry, symmetry reduction and cell indexing live in lr_joint_555.h in the
 * solver repo; the searcher includes the same header.
 *
 * The build is a level-synchronous breadth-first search over one byte per cell
 * (34.5 GB, anonymous memory). Cells are grouped into rows by t class. A row
 * holds one move's worth of work for a single target row at a time, so the
 * random writes stay inside one 735 KB row. Every write is also made to the
 * cell's stabilizer images, so every cell that stands for the same state holds
 * the same value.
 *
 * Output is packed to one nibble per cell (depth + 1, 0 = unseen) in a sparse
 * file, with a JSON sidecar. --max-depth D stops after D plies and leaves the
 * rest unseen, which the solver reads as no information; it is for tests.
 *
 * --verify checks a finished file without any search: the goal reads 1, every
 * sampled cell differs from its 36 neighbours by at most 1, every non-goal
 * cell has a neighbour one lower, and the 16 LR-axis images of a state read
 * the same. Together these pin the value to the exact breadth-first distance.
 */
#include "../../rubiks-cube-NxNxN-solver/rubikscubennnsolver/lr_joint_555.h"

#include <errno.h>
#include <fcntl.h>
#include <pthread.h>
#include <stdatomic.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <unistd.h>

#define MAX_THREADS 128
#define MAX_VALUE 31
#define PACK_CHUNK_BYTES (UINT64_C(1) << 20)

static uint8_t *cells;
static uint32_t *row_flags; /* bit v set when the row holds a cell of value v */
static uint32_t *x_trans;   /* move * 735471 + x rank -> x rank after the move */
static uint64_t level_cells[MAX_VALUE + 1];

struct level_job {
    uint32_t *rows;
    uint32_t row_count;
    unsigned int value;
    int expand;
    atomic_uint_fast32_t next;
    atomic_uint_fast64_t total;
};

static double seconds_since(const struct timeval *start)
{
    struct timeval now;

    gettimeofday(&now, NULL);
    return (double)(now.tv_sec - start->tv_sec) + (double)(now.tv_usec - start->tv_usec) / 1e6;
}

static void set_cell_value(uint32_t class_id, uint32_t x_rank_value, uint8_t value)
{
    uint8_t *row = cells + (size_t)class_id * LRJ_UNIVERSE;
    int wrote = 0;

    for (unsigned int index = 0; index < lrj.stab_count[class_id]; index++) {
        uint32_t position = lrj.x_sym_rank[lrj.stab[class_id][index]][x_rank_value];

        if (__atomic_load_n(&row[position], __ATOMIC_RELAXED) == 0) {
            __atomic_store_n(&row[position], value, __ATOMIC_RELAXED);
            wrote = 1;
        }
    }
    if (wrote) {
        __atomic_fetch_or(&row_flags[class_id], UINT32_C(1) << value, __ATOMIC_RELAXED);
    }
}

/* Offsets of every cell equal to value in a row. Racing writers only store value + 1. */
static size_t collect_frontier(const uint8_t *row, uint8_t value, uint32_t *out)
{
    const uint64_t pattern = UINT64_C(0x0101010101010101) * value;
    size_t count = 0;
    size_t index = 0;

    for (; index + 8 <= LRJ_UNIVERSE; index += 8) {
        uint64_t word;
        uint64_t difference;

        memcpy(&word, row + index, 8);
        difference = word ^ pattern;
        if ((difference - UINT64_C(0x0101010101010101)) & ~difference & UINT64_C(0x8080808080808080)) {
            for (unsigned int lane = 0; lane < 8; lane++) {
                if (row[index + lane] == value) {
                    out[count++] = (uint32_t)(index + lane);
                }
            }
        }
    }
    for (; index < LRJ_UNIVERSE; index++) {
        if (row[index] == value) {
            out[count++] = (uint32_t)index;
        }
    }
    return count;
}

static void expand_row(uint32_t class_id, const uint32_t *frontier, size_t count, uint8_t value)
{
    uint32_t representative = lrj.rep_mask[class_id];
    uint8_t next = (uint8_t)(value + 1);

    for (unsigned int move = 0; move < LRJ_MOVES; move++) {
        uint32_t entry = lrj.class_of[lrj_rank(lrj_apply_t(move, representative))];
        uint32_t child_class = entry >> 4;
        const uint32_t *moved = x_trans + (size_t)move * LRJ_UNIVERSE;
        const uint32_t *rotate = lrj.x_sym_rank[entry & 15];
        uint8_t *row = cells + (size_t)child_class * LRJ_UNIVERSE;
        unsigned int stabilizers = lrj.stab_count[child_class];
        int wrote = 0;

        if (stabilizers == 1) {
            for (size_t index = 0; index < count; index++) {
                uint32_t position = rotate[moved[frontier[index]]];

                if (__atomic_load_n(&row[position], __ATOMIC_RELAXED) == 0) {
                    __atomic_store_n(&row[position], next, __ATOMIC_RELAXED);
                    wrote = 1;
                }
            }
        } else {
            for (size_t index = 0; index < count; index++) {
                uint32_t rotated = rotate[moved[frontier[index]]];

                for (unsigned int stabilizer = 0; stabilizer < stabilizers; stabilizer++) {
                    uint32_t position = lrj.x_sym_rank[lrj.stab[child_class][stabilizer]][rotated];

                    if (__atomic_load_n(&row[position], __ATOMIC_RELAXED) == 0) {
                        __atomic_store_n(&row[position], next, __ATOMIC_RELAXED);
                        wrote = 1;
                    }
                }
            }
        }
        if (wrote) {
            __atomic_fetch_or(&row_flags[child_class], UINT32_C(1) << next, __ATOMIC_RELAXED);
        }
    }
}

static void *level_worker(void *argument)
{
    struct level_job *job = argument;
    uint32_t *frontier = malloc((size_t)LRJ_UNIVERSE * sizeof(*frontier));
    uint64_t local = 0;

    if (!frontier) {
        lrj_fail("out of memory");
    }
    for (;;) {
        uint32_t position = (uint32_t)atomic_fetch_add(&job->next, 1);
        uint32_t class_id;
        size_t count;

        if (position >= job->row_count) {
            break;
        }
        class_id = job->rows[position];
        count = collect_frontier(cells + (size_t)class_id * LRJ_UNIVERSE, (uint8_t)job->value, frontier);
        local += count;
        if (job->expand && count) {
            expand_row(class_id, frontier, count, (uint8_t)job->value);
        }
    }
    atomic_fetch_add(&job->total, local);
    free(frontier);
    return NULL;
}

static void run_threads(void *(*routine)(void *), void *argument, unsigned int threads)
{
    pthread_t handles[MAX_THREADS];

    for (unsigned int index = 0; index < threads; index++) {
        if (pthread_create(&handles[index], NULL, routine, argument)) {
            lrj_fail("could not start a thread");
        }
    }
    for (unsigned int index = 0; index < threads; index++) {
        pthread_join(handles[index], NULL);
    }
}

static void build_x_transitions(void)
{
    x_trans = malloc((size_t)LRJ_MOVES * LRJ_UNIVERSE * sizeof(*x_trans));
    if (!x_trans) {
        lrj_fail("out of memory");
    }
    for (uint32_t rank = 0; rank < LRJ_UNIVERSE; rank++) {
        uint32_t mask = lrj_unrank(rank);

        for (unsigned int move = 0; move < LRJ_MOVES; move++) {
            x_trans[(size_t)move * LRJ_UNIVERSE + rank] = lrj_rank(lrj_apply_x(move, mask));
        }
    }
}

struct pack_job {
    int fd;
    uint64_t bytes;
    uint64_t chunks;
    atomic_uint_fast64_t next;
};

static void *pack_worker(void *argument)
{
    struct pack_job *job = argument;
    unsigned char *buffer = malloc(PACK_CHUNK_BYTES);
    uint64_t total_cells = lrj_cell_count();

    if (!buffer) {
        lrj_fail("out of memory");
    }
    for (;;) {
        uint64_t chunk = atomic_fetch_add(&job->next, 1);
        uint64_t first_byte;
        uint64_t length;
        uint64_t first_row;
        uint64_t last_row;
        int any = 0;

        if (chunk >= job->chunks) {
            break;
        }
        first_byte = chunk * PACK_CHUNK_BYTES;
        length = job->bytes - first_byte < PACK_CHUNK_BYTES ? job->bytes - first_byte : PACK_CHUNK_BYTES;
        first_row = (first_byte * 2) / LRJ_UNIVERSE;
        last_row = (first_byte * 2 + length * 2 - 1) / LRJ_UNIVERSE;
        if (last_row >= lrj.classes) {
            last_row = lrj.classes - 1;
        }
        for (uint64_t row = first_row; row <= last_row && !any; row++) {
            any = row_flags[row] != 0;
        }
        if (!any) {
            continue; /* leaves a hole in the sparse file */
        }
        for (uint64_t index = 0; index < length; index++) {
            uint64_t cell = (first_byte + index) * 2;
            unsigned int low = cells[cell];
            unsigned int high = cell + 1 < total_cells ? cells[cell + 1] : 0;

            buffer[index] = (unsigned char)(low | (high << 4));
        }
        if (pwrite(job->fd, buffer, length, (off_t)first_byte) != (ssize_t)length) {
            lrj_fail("write failed");
        }
    }
    free(buffer);
    return NULL;
}

static void write_json(const char *path, unsigned int max_depth, int partial, uint64_t total)
{
    FILE *json = fopen(path, "w");
    unsigned int last = 0;

    if (!json) {
        lrj_fail("could not write the JSON sidecar");
    }
    for (unsigned int value = 1; value <= MAX_VALUE; value++) {
        if (level_cells[value]) {
            last = value;
        }
    }
    fprintf(json, "{\n");
    fprintf(json, "  \"format\": \"nibble, depth + 1, 0 unseen, cell = t_class * 735471 + x_rank\",\n");
    fprintf(json, "  \"universe\": %" PRIu64 ",\n", LRJ_UNIVERSE);
    fprintf(json, "  \"group_order\": %u,\n", LRJ_GROUP);
    fprintf(json, "  \"t_classes\": %u,\n", lrj.classes);
    fprintf(json, "  \"cells\": %" PRIu64 ",\n", total);
    fprintf(json, "  \"bytes\": %" PRIu64 ",\n", lrj_packed_bytes());
    fprintf(json, "  \"partial\": %s,\n", partial ? "true" : "false");
    fprintf(json, "  \"max_depth_limit\": %u,\n", max_depth);
    fprintf(json, "  \"deepest\": %u,\n", last ? last - 1 : 0);
    fprintf(json, "  \"depth_counts\": [");
    for (unsigned int value = 1; value <= last; value++) {
        fprintf(json, "%s%" PRIu64, value > 1 ? ", " : "", level_cells[value]);
    }
    fprintf(json, "]\n}\n");
    fclose(json);
}

static int build(const char *output, unsigned int threads, unsigned int max_depth, int limited)
{
    struct timeval start;
    uint64_t total = lrj_cell_count();
    uint64_t seen = 0;
    uint32_t goal_entry = lrj.class_of[lrj_rank(LRJ_GOAL_MASK)];
    uint32_t *rows = malloc((size_t)lrj.classes * sizeof(*rows));
    unsigned int deepest = 0;
    unsigned int any_flags = 0;

    gettimeofday(&start, NULL);
    printf("%u t classes x %" PRIu64 " x ranks = %" PRIu64 " cells\n", lrj.classes, LRJ_UNIVERSE, total);
    fflush(stdout);
    cells = mmap(NULL, total, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE, -1, 0);
    if (cells == MAP_FAILED) {
        fprintf(stderr, "ERROR: could not map %" PRIu64 " bytes: %s\n", total, strerror(errno));
        return 1;
    }
    row_flags = calloc(lrj.classes, sizeof(*row_flags));
    if (!row_flags || !rows) {
        lrj_fail("out of memory");
    }
    build_x_transitions();
    printf("x transitions ready after %.1fs\n", seconds_since(&start));
    fflush(stdout);

    /* Goal: value 1, written on every stabilizer image. */
    set_cell_value(goal_entry >> 4, lrj_rank(lrj_keeper_x(goal_entry & 15, LRJ_GOAL_MASK)), 1);

    for (unsigned int value = 1; value < MAX_VALUE; value++) {
        struct level_job job;
        uint32_t row_count = 0;

        for (uint32_t row = 0; row < lrj.classes; row++) {
            if (row_flags[row] & (UINT32_C(1) << value)) {
                rows[row_count++] = row;
            }
        }
        if (!row_count) {
            break;
        }
        job.rows = rows;
        job.row_count = row_count;
        job.value = value;
        job.expand = !limited || value - 1 < max_depth;
        atomic_init(&job.next, 0);
        atomic_init(&job.total, 0);
        run_threads(level_worker, &job, threads);
        level_cells[value] = (uint64_t)atomic_load(&job.total);
        seen += level_cells[value];
        deepest = value - 1;
        printf(
            "depth %u: %" PRIu64 " cells in %u rows (%.1fs)\n", deepest, level_cells[value], row_count,
            seconds_since(&start)
        );
        fflush(stdout);
        if (!job.expand) {
            break;
        }
    }
    for (uint32_t row = 0; row < lrj.classes; row++) {
        any_flags |= row_flags[row];
    }
    if (any_flags >> (MAX_VALUE)) {
        fprintf(stderr, "ERROR: search reached the %u-ply limit\n", MAX_VALUE - 1);
        return 1;
    }
    if (!limited && seen != total) {
        fprintf(stderr, "ERROR: %" PRIu64 " of %" PRIu64 " cells were never reached\n", total - seen, total);
        return 1;
    }
    if (any_flags >> (LRJ_MAX_NIBBLE + 1)) {
        fprintf(stderr, "ERROR: depth + 1 does not fit a nibble (deepest %u)\n", deepest);
        return 1;
    }
    printf("%" PRIu64 " of %" PRIu64 " cells reached, deepest %u\n", seen, total, deepest);

    {
        char temporary[4096];
        char sidecar[4096];
        struct pack_job pack;
        int fd;

        snprintf(temporary, sizeof(temporary), "%s.tmp", output);
        snprintf(sidecar, sizeof(sidecar), "%s.json", output);
        fd = open(temporary, O_WRONLY | O_CREAT | O_TRUNC, 0644);
        if (fd < 0 || ftruncate(fd, (off_t)lrj_packed_bytes())) {
            fprintf(stderr, "ERROR: could not create %s: %s\n", temporary, strerror(errno));
            return 1;
        }
        pack.fd = fd;
        pack.bytes = lrj_packed_bytes();
        pack.chunks = (pack.bytes + PACK_CHUNK_BYTES - 1) / PACK_CHUNK_BYTES;
        atomic_init(&pack.next, 0);
        run_threads(pack_worker, &pack, threads);
        if (close(fd) || rename(temporary, output)) {
            fprintf(stderr, "ERROR: could not finish %s: %s\n", output, strerror(errno));
            return 1;
        }
        write_json(sidecar, max_depth, limited && seen != total, total);
        printf("wrote %s (%" PRIu64 " bytes) after %.1fs\n", output, lrj_packed_bytes(), seconds_since(&start));
    }
    return 0;
}

static uint64_t rng_state = UINT64_C(88172645463325252);

static uint64_t next_random(void)
{
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 7;
    rng_state ^= rng_state << 17;
    return rng_state;
}

struct verify_totals {
    uint64_t checked;
    uint64_t unseen_skipped;
    uint64_t failures;
};

static void verify_failure(struct verify_totals *totals, const char *what, uint32_t t, uint32_t x, unsigned int value)
{
    if (totals->failures < 20) {
        printf("FAIL %s: t=%06x x=%06x value=%u\n", what, t, x, value);
    }
    totals->failures++;
}

static void verify_state(
    const unsigned char *packed,
    uint32_t t,
    uint32_t x,
    unsigned int walk_length,
    int walked,
    unsigned int max_depth,
    int limited,
    struct verify_totals *totals
)
{
    unsigned int value = lrj_nibble_get(packed, lrj_cell_index(t, x));
    unsigned int lowest = 99;
    int is_goal_image = 0;
    unsigned int symmetry = (unsigned int)(next_random() % LRJ_GROUP);

    if (!value) {
        if (!limited || (walked && walk_length <= max_depth)) {
            verify_failure(totals, "unexpected unseen cell", t, x, value);
        } else {
            totals->unseen_skipped++;
        }
        return;
    }
    totals->checked++;
    if (walked && value > walk_length + 1) {
        verify_failure(totals, "value above the walk length", t, x, value);
    }
    if (lrj_nibble_get(packed, lrj_cell_index(lrj_keeper_t(symmetry, t), lrj_keeper_x(symmetry, x))) != value) {
        verify_failure(totals, "symmetry image differs", t, x, value);
    }
    for (unsigned int index = 0; index < LRJ_GROUP && !is_goal_image; index++) {
        is_goal_image = lrj_keeper_t(index, LRJ_GOAL_MASK) == t && lrj_keeper_x(index, LRJ_GOAL_MASK) == x;
    }
    if (is_goal_image != (value == 1)) {
        verify_failure(totals, "value 1 and the goal disagree", t, x, value);
    }
    for (unsigned int move = 0; move < LRJ_MOVES; move++) {
        unsigned int child = lrj_nibble_get(packed, lrj_cell_index(lrj_apply_t(move, t), lrj_apply_x(move, x)));

        if (!child) {
            if (!limited || value != max_depth + 1) {
                verify_failure(totals, "unseen neighbour", t, x, value);
            }
            continue;
        }
        if (child + 1 < value || child > value + 1) {
            verify_failure(totals, "neighbour differs by more than 1", t, x, value);
        }
        lowest = child < lowest ? child : lowest;
    }
    if (value > 1 && lowest != value - 1) {
        verify_failure(totals, "no neighbour one lower", t, x, value);
    }
}

static int verify(const char *path, uint64_t samples, unsigned int max_depth, int limited)
{
    struct stat info;
    int fd = open(path, O_RDONLY);
    const unsigned char *packed;
    struct verify_totals totals = {0, 0, 0};
    uint32_t stabilized[8192];
    unsigned int stabilized_count = 0;

    if (fd < 0 || fstat(fd, &info)) {
        fprintf(stderr, "ERROR: could not open %s: %s\n", path, strerror(errno));
        return 1;
    }
    if ((uint64_t)info.st_size != lrj_packed_bytes()) {
        fprintf(stderr, "ERROR: %s is %" PRIu64 " bytes, expected %" PRIu64 "\n", path, (uint64_t)info.st_size, lrj_packed_bytes());
        return 1;
    }
    packed = mmap(NULL, (size_t)info.st_size, PROT_READ, MAP_SHARED, fd, 0);
    if (packed == MAP_FAILED) {
        fprintf(stderr, "ERROR: could not map %s: %s\n", path, strerror(errno));
        return 1;
    }
    for (uint32_t class_id = 0; class_id < lrj.classes && stabilized_count < 8192; class_id++) {
        if (lrj.stab_count[class_id] > 1) {
            stabilized[stabilized_count++] = class_id;
        }
    }
    {
        uint32_t entry = lrj.class_of[lrj_rank(LRJ_GOAL_MASK)];
        unsigned int goal_value = lrj_nibble_get(packed, lrj_cell_index(LRJ_GOAL_MASK, LRJ_GOAL_MASK));

        printf("goal cell value %u (expect 1), class %u\n", goal_value, entry >> 4);
        if (goal_value != 1) {
            totals.failures++;
        }
    }
    for (uint64_t sample = 0; sample < samples; sample++) {
        uint32_t t = LRJ_GOAL_MASK;
        uint32_t x = LRJ_GOAL_MASK;
        unsigned int mode = (unsigned int)(next_random() % 4);

        if (mode < 2) {
            unsigned int length = (unsigned int)(next_random() % (limited ? max_depth + 2 : 21));

            for (unsigned int step = 0; step < length; step++) {
                unsigned int move = (unsigned int)(next_random() % LRJ_MOVES);

                t = lrj_apply_t(move, t);
                x = lrj_apply_x(move, x);
            }
            verify_state(packed, t, x, length, 1, max_depth, limited, &totals);
        } else {
            if (mode == 2 && stabilized_count) {
                t = lrj.rep_mask[stabilized[next_random() % stabilized_count]];
            } else {
                t = lrj_unrank((uint32_t)(next_random() % LRJ_UNIVERSE));
            }
            x = lrj_unrank((uint32_t)(next_random() % LRJ_UNIVERSE));
            verify_state(packed, t, x, 0, 0, max_depth, limited, &totals);
        }
    }
    printf(
        "verified %" PRIu64 " states, %" PRIu64 " unseen skipped, %" PRIu64 " failures\n", totals.checked,
        totals.unseen_skipped, totals.failures
    );
    return totals.failures ? 1 : 0;
}

static void usage(const char *program)
{
    fprintf(
        stderr,
        "usage: %s --output FILE [--threads N] [--max-depth D]\n       %s --verify FILE [--samples N] [--max-depth D] [--seed S]\n",
        program, program
    );
}

int main(int argc, char **argv)
{
    const char *output = NULL;
    const char *verify_path = NULL;
    unsigned int threads = (unsigned int)sysconf(_SC_NPROCESSORS_ONLN);
    unsigned int max_depth = 0;
    int limited = 0;
    uint64_t samples = 100000;

    for (int index = 1; index < argc; index++) {
        if (!strcmp(argv[index], "--output") && index + 1 < argc) {
            output = argv[++index];
        } else if (!strcmp(argv[index], "--verify") && index + 1 < argc) {
            verify_path = argv[++index];
        } else if (!strcmp(argv[index], "--threads") && index + 1 < argc) {
            threads = (unsigned int)strtoul(argv[++index], NULL, 10);
        } else if (!strcmp(argv[index], "--max-depth") && index + 1 < argc) {
            max_depth = (unsigned int)strtoul(argv[++index], NULL, 10);
            limited = 1;
        } else if (!strcmp(argv[index], "--samples") && index + 1 < argc) {
            samples = strtoull(argv[++index], NULL, 10);
        } else if (!strcmp(argv[index], "--seed") && index + 1 < argc) {
            rng_state ^= strtoull(argv[++index], NULL, 10) * UINT64_C(0x9E3779B97F4A7C15);
        } else {
            usage(argv[0]);
            return 2;
        }
    }
    if (!output == !verify_path || threads < 1 || threads > MAX_THREADS || (limited && max_depth >= MAX_VALUE - 1)) {
        usage(argv[0]);
        return 2;
    }
    lrj_init(1);
    printf("%u LR-axis symmetries, %u t classes\n", LRJ_GROUP, lrj.classes);
    fflush(stdout);
    if (verify_path) {
        return verify(verify_path, samples, max_depth, limited);
    }
    return build(output, threads, max_depth, limited);
}

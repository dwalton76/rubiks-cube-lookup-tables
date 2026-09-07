
#include <ctype.h>
#include <fcntl.h>
#include <inttypes.h>
#include <limits.h>
#include <locale.h>
#include <math.h>
#include <stdint.h>
#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>
#include "ida_search_core.h"

// If by some miracle we ever start building lookup-tables deeper than 20 moves
// then we will need to increase this constant
#define MAX_MOVE_LENGTH 20

#define MEGABYTE (1024 * 1024)

/*
 * How wide a "<state>:<moves>\n\0" line can get for a state of state_bytes squares.
 *
 * Our input already carries up to MAX_MOVE_LENGTH moves and we append one more, so the
 * moves field has to hold MAX_MOVE_LENGTH + 1 of them. Rounding the result up to a
 * multiple of 8 keeps every line in to_write aligned.
 *
 * This is deliberately a function of the table in front of us rather than a worst-case
 * constant. A compact 5x5x5 x-centers line needs 136 bytes where a full 7x7x7 needs 408,
 * so using the actual stride avoids wasting memory without changing batch boundaries.
 */
#define LINE_WIDTH_FOR_STATE(state_bytes) \
    ((((state_bytes) + 1 + (MAX_MOVE_STR_SIZE * (MAX_MOVE_LENGTH + 1)) + 2) + 7) & ~7)

// The workq lines we read are padded out to --linewidth, which get_workq_line_length()
// in buildercore.py caps at 512 before adding one for the newline. We build our output
// lines in the same buffer, so it has to hold a full output line as well.
#define MAX_WORKQ_LINE_LENGTH 1024

/*
 * This is part of the lookup-table file format in practice, not just a performance
 * setting. GNU sort --uniq --key keeps the first equal-state line it sees, so changing
 * batch boundaries changes which equally short solution is stored and therefore changes
 * the table byte-for-byte. Keep the historical boundary for reproducible tables.
 */
#define BATCH_SIZE 2000000

#define MAX_FILENAME_SIZE 128
#define MAX_COMPACT_SQUARES 255
#define MAX_SQUARES_ARG 2048
#define MAX_RANK_SYMBOLS 32
#define RANKED_RECORD_SIZE 9
#define MAX_BINOM 64
#define RANKED_IO_BUFFER (8 * 1024 * 1024)

static uint64_t binom_table[MAX_BINOM + 1][MAX_BINOM + 1];
static unsigned int binom_ready_n = 0;


// to_write holds batch_size lines, each line_width bytes from the last. process_workq()
// sizes all three once it knows how wide a line is for this table.
char *to_write = NULL;
unsigned int line_width = 0;
unsigned int batch_size = 0;

// deduplicate_to_write_buffer() sorts these pointers into to_write instead of moving the
// rows around, which makes every swap 8 bytes instead of a couple hundred
char **to_write_ptr = NULL;

#define TO_WRITE_LINE(i) (to_write + ((size_t) (i) * line_width))

// The number of bytes of state at the front of every line, set once by process_workq()
unsigned int state_width = 0;


/*
 * Order two "<state>:<moves>\n" lines.
 *
 * Only the state matters to the "sort --uniq --key=1.1,1.<state_width>" that merges our
 * output files, but we break ties on the moves so that our ordering stays total. Byte
 * <state_width> is the ":" on both lines, so this gives the same answer that strcmp() on
 * the whole line does while stopping as soon as the states differ.
 */
int
line_compare(const char *a, const char *b)
{
    int result = memcmp(a, b, state_width);

    if (result) {
        return result;
    }

    return strcmp(&a[state_width], &b[state_width]);
}

/* Remove leading and trailing whitespaces */
char *
strstrip (char *s)
{
    size_t size;
    char *end;

    size = strlen(s);

    if (!size)
        return s;

    // Removing trailing whitespaces
    end = s + size - 1;
    while (end >= s && isspace(*end))
        end--;
    *(end + 1) = '\0';

    // Remove leading whitespaces
    // The lookup table files do not have any leading whitespaces so commenting this out to save a few CPU cycles
    //while (*s && isspace(*s))
    //    s++;

    return s;
}


// https://github.com/codyryanwright/QuicksortStrings/blob/master/2dStringQuicksort.c
void
quicksort(
    char **A,
    unsigned int len)
{
    if (len < 2) {
        return;
    }

    char *pivot = A[len / 2]; // pivot is comparator

    int i = 0;
    int j = len - 1;
    char *temp = NULL;

    while (1) {
        // find first to the left of pivot that is larger than pivot
        while (line_compare(A[i], pivot) < 0) {
            ++i;
        }

        // find first to the right of pivot that is smaller than pivot
        while (line_compare(A[j], pivot) > 0) {
            --j;
        }

        // Swap if i (larger than pivot) is left of j (smaller than pivot)
        if (i < j) {
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        } else {
            break;
        }

        ++i;
        --j;
    }

    quicksort(A, i); // left half
    quicksort(A + i, len - i); // right half
}

/*
 * Sort to_write and copy one line per unique state into to_write_dedup. Returns how many
 * bytes we put there.
 */
size_t
deduplicate_to_write_buffer(
    char *to_write_dedup,
    unsigned int array_size,
    unsigned int to_write_count)
{
    unsigned int line_length = 0;
    char *to_write_dedup_ptr = to_write_dedup;

    // quicksort the contents of to_write
    for (unsigned int i = 0; i < to_write_count; i++) {
        to_write_ptr[i] = TO_WRITE_LINE(i);
    }

    quicksort(to_write_ptr, to_write_count);

    line_length = strlen(to_write_ptr[0]);
    memcpy(to_write_dedup_ptr, to_write_ptr[0], line_length);
    to_write_dedup_ptr += line_length;

    // loop over to_write and write all unique states to to_write_dedup
    for (unsigned int i = 1; i < to_write_count; i++) {

        if (memcmp(to_write_ptr[i], to_write_ptr[i-1], array_size) != 0) {
            line_length = strlen(to_write_ptr[i]);
            memcpy(to_write_dedup_ptr, to_write_ptr[i], line_length);
            // printf("KEEP %s", to_write_ptr[i]);
            to_write_dedup_ptr += line_length;
        // } else {
        //     printf("SKIP %s", to_write_ptr[i]);
        }
    }

    return (size_t) (to_write_dedup_ptr - to_write_dedup);
}

/*
 * Deduplicate everything we have buffered and write it to the next output file. Returns
 * the file_count to use for the file after this one.
 */
unsigned int
write_to_write_buffer(
    char *to_write_dedup,
    unsigned int array_size,
    unsigned int to_write_count,
    char *outputfile,
    unsigned int file_count)
{
    char tmp_outputfile[MAX_FILENAME_SIZE];
    FILE *fh_write = NULL;
    size_t dedup_length = deduplicate_to_write_buffer(to_write_dedup, array_size, to_write_count);

    snprintf(tmp_outputfile, MAX_FILENAME_SIZE, "%s-%07d", outputfile, file_count);
    fh_write = fopen(tmp_outputfile, "w");

    if (fh_write == NULL) {
        printf("ERROR: could not open %s for writing\n", tmp_outputfile);
        exit(1);
    }

    // fwrite with the length we just computed, so we do not have to zero out the
    // hundreds of MB of to_write_dedup that fputs() would need to find its terminator
    fwrite(to_write_dedup, 1, dedup_length, fh_write);
    fclose(fh_write);
    return file_count + 1;
}


void
rotate_full_cube(
    char *dest,
    char *src,
    unsigned int full_size,
    unsigned char cube_size,
    move_type move)
{
    memcpy(dest, src, full_size);

    switch (cube_size) {
    case 2:
        rotate_222(dest, src, full_size, move);
        break;
    case 3:
        rotate_333(dest, src, full_size, move);
        break;
    case 4:
        rotate_444(dest, src, full_size, move);
        break;
    case 5:
        rotate_555(dest, src, full_size, move);
        break;
    case 6:
        rotate_666(dest, src, full_size, move);
        break;
    case 7:
        rotate_777(dest, src, full_size, move);
        break;
    default:
        printf("ERROR: add support for %dx%dx%d cubes\n", cube_size, cube_size, cube_size);
        exit(1);
    }
}


unsigned int
parse_squares(char *arg, unsigned int *squares)
{
    unsigned int count = 0;
    char *ptr = strtok(arg, ",");

    while (ptr != NULL) {
        int index = atoi(ptr);

        if (count >= MAX_COMPACT_SQUARES) {
            printf("ERROR: --squares has more than %d entries\n", MAX_COMPACT_SQUARES);
            exit(1);
        }

        if (index < 1) {
            printf("ERROR: --squares entry '%s' is not a valid cube index\n", ptr);
            exit(1);
        }

        squares[count++] = (unsigned int) index;
        ptr = strtok(NULL, ",");
    }

    return count;
}

static unsigned int
parse_rank_counts(char *arg, unsigned int *counts)
{
    unsigned int count = 0;
    char *ptr = strtok(arg, ",");
    while (ptr != NULL) {
        if (count >= MAX_RANK_SYMBOLS) {
            fprintf(stderr, "ERROR: too many --rank-counts entries\n");
            exit(1);
        }
        counts[count] = (unsigned int) strtoul(ptr, NULL, 10);
        if (!counts[count]) {
            fprintf(stderr, "ERROR: ranked symbol counts must be positive\n");
            exit(1);
        }
        count++;
        ptr = strtok(NULL, ",");
    }
    return count;
}


/*
 * For each legal move, find where every interesting square lands after rotate_xxx().
 * perm[move * square_count + src] is the compact index that square src maps to.
 *
 * If any interesting square maps onto a placeholder, compact states would drop that
 * information, so we refuse to continue.
 */
unsigned int *
build_compact_permutations(
    unsigned char cube_size,
    unsigned int *squares,
    unsigned int square_count,
    move_type *moves,
    unsigned int moves_count)
{
    unsigned int full_size = (cube_size * cube_size * 6) + 1;
    unsigned int *perm = malloc(sizeof(unsigned int) * moves_count * square_count);
    unsigned int *index_of = calloc(full_size, sizeof(unsigned int));
    unsigned char *seen = malloc(square_count);
    char *probe = malloc(full_size);
    char *dest = malloc(full_size);

    if (perm == NULL || index_of == NULL || seen == NULL || probe == NULL || dest == NULL) {
        printf("ERROR: could not allocate compact-state permutation tables\n");
        exit(1);
    }

    for (unsigned int i = 0; i < square_count; i++) {
        if (squares[i] >= full_size) {
            printf("ERROR: --squares %u is outside a %dx%dx%d cube\n",
                squares[i], cube_size, cube_size, cube_size);
            exit(1);
        }

        if (index_of[squares[i]]) {
            printf("ERROR: --squares lists %u more than once\n", squares[i]);
            exit(1);
        }

        index_of[squares[i]] = i + 1;
    }

    for (unsigned int move_index = 0; move_index < moves_count; move_index++) {
        memset(probe, '.', full_size);
        probe[0] = 'x';

        for (unsigned int i = 0; i < square_count; i++) {
            probe[squares[i]] = (char) (i + 1);
        }

        rotate_full_cube(dest, probe, full_size, cube_size, moves[move_index]);
        memset(seen, 0, square_count);

        for (unsigned int k = 0; k < full_size; k++) {
            unsigned char marker = (unsigned char) dest[k];

            if (marker == 0 || marker == '.' || marker == 'x') {
                continue;
            }

            if (marker < 1 || marker > square_count) {
                printf("ERROR: unexpected marker %u at square %u under %s\n",
                    marker, k, move2str[moves[move_index]]);
                exit(1);
            }

            unsigned int src = marker - 1;

            if (!index_of[k]) {
                printf("ERROR: square %u maps to %u under %s, which is not in --squares\n",
                    squares[src], k, move2str[moves[move_index]]);
                exit(1);
            }

            if (seen[src]) {
                printf("ERROR: square %u mapped twice under %s\n",
                    squares[src], move2str[moves[move_index]]);
                exit(1);
            }

            seen[src] = 1;
            perm[(move_index * square_count) + src] = index_of[k] - 1;
        }

        for (unsigned int i = 0; i < square_count; i++) {
            if (!seen[i]) {
                printf("ERROR: square %u did not map to another --squares entry under %s\n",
                    squares[i], move2str[moves[move_index]]);
                exit(1);
            }
        }
    }

    free(index_of);
    free(seen);
    free(probe);
    free(dest);
    return perm;
}

static void
ensure_binom(unsigned int n)
{
    if (n > MAX_BINOM) {
        fprintf(stderr, "ERROR: ranked states longer than %d are not supported\n", MAX_BINOM);
        exit(1);
    }
    if (binom_ready_n >= n) {
        return;
    }

    for (unsigned int i = binom_ready_n; i <= n; i++) {
        binom_table[i][0] = 1;
        if (i > 0) {
            binom_table[i][i] = 1;
        }
        for (unsigned int k = 1; k < i; k++) {
            uint64_t a = binom_table[i - 1][k - 1];
            uint64_t b = binom_table[i - 1][k];
            if (b > UINT64_MAX - a) {
                binom_table[i][k] = 0;
            } else {
                binom_table[i][k] = a + b;
            }
        }
    }
    binom_ready_n = n;
}


static uint64_t
multiset_perms(const unsigned int *counts, unsigned int symbol_count, unsigned int slots)
{
    uint64_t permutations = 1;
    unsigned int left = slots;

    for (unsigned int symbol = 0; symbol < symbol_count; symbol++) {
        unsigned int choose = counts[symbol];
        uint64_t ways;

        if (choose > left) {
            return 0;
        }
        ways = binom_table[left][choose];
        if (!ways && choose && left) {
            fprintf(stderr, "ERROR: ranked multiset arithmetic overflow\n");
            exit(1);
        }
        if (ways && permutations > UINT64_MAX / ways) {
            fprintf(stderr, "ERROR: ranked multiset arithmetic overflow\n");
            exit(1);
        }
        permutations *= ways;
        left -= choose;
    }
    return permutations;
}


static void
multiset_unrank(
    uint64_t rank,
    unsigned char *state,
    const unsigned char *symbols,
    const unsigned int *initial_counts,
    unsigned int symbol_count,
    unsigned int state_length,
    uint64_t universe)
{
    unsigned int counts[MAX_RANK_SYMBOLS];
    memcpy(counts, initial_counts, symbol_count * sizeof(unsigned int));

    if (rank >= universe) {
        fprintf(stderr, "ERROR: rank %" PRIu64 " is outside universe %" PRIu64 "\n", rank, universe);
        exit(1);
    }

    for (unsigned int position = 0; position < state_length; position++) {
        unsigned int slots = state_length - position;

        for (unsigned int symbol = 0; symbol < symbol_count; symbol++) {
            uint64_t block;
            if (!counts[symbol]) {
                continue;
            }
            counts[symbol]--;
            block = multiset_perms(counts, symbol_count, slots - 1);
            if (rank < block) {
                state[position] = symbols[symbol];
                break;
            }
            rank -= block;
            counts[symbol]++;
        }
    }
}


static uint64_t
multiset_rank(
    const unsigned char *state,
    const int *symbol_of,
    const unsigned int *initial_counts,
    unsigned int symbol_count,
    unsigned int state_length)
{
    unsigned int counts[MAX_RANK_SYMBOLS];
    uint64_t rank = 0;
    memcpy(counts, initial_counts, symbol_count * sizeof(unsigned int));

    for (unsigned int position = 0; position < state_length; position++) {
        int selected = symbol_of[state[position]];
        unsigned int slots = state_length - position;

        if (selected < 0 || !counts[selected]) {
            fprintf(stderr, "ERROR: invalid symbol in ranked state\n");
            exit(1);
        }

        for (unsigned int symbol = 0; (int) symbol < selected; symbol++) {
            uint64_t block;
            if (!counts[symbol]) {
                continue;
            }
            counts[symbol]--;
            block = multiset_perms(counts, symbol_count, slots - 1);
            rank += block;
            counts[symbol]++;
        }
        counts[selected]--;
    }
    return rank;
}


static uint64_t
read_rank(FILE *fh)
{
    unsigned char bytes[8];
    if (fread(bytes, 1, sizeof(bytes), fh) != sizeof(bytes)) {
        fprintf(stderr, "ERROR: could not read ranked workq record\n");
        exit(1);
    }
    uint64_t rank = 0;
    for (unsigned int i = 0; i < sizeof(bytes); i++) {
        rank |= ((uint64_t) bytes[i]) << (8 * i);
    }
    return rank;
}


static void
write_rank(FILE *fh, uint64_t rank, unsigned char move)
{
    unsigned char record[RANKED_RECORD_SIZE];
    for (unsigned int i = 0; i < 8; i++) {
        record[i] = (unsigned char) (rank >> (8 * i));
    }
    record[8] = move;
    if (fwrite(record, 1, sizeof(record), fh) != sizeof(record)) {
        fprintf(stderr, "ERROR: could not write ranked workq record\n");
        exit(1);
    }
}


static void
process_ranked_workq(
    const char *inputfile,
    const char *outputfile,
    const char *cost_filename,
    uint64_t start,
    uint64_t end,
    unsigned char depth,
    unsigned char cube_size,
    move_type moves[MOVE_MAX],
    unsigned int moves_count,
    unsigned int *squares,
    unsigned int square_count,
    const unsigned char *symbols,
    const unsigned int *counts,
    unsigned int symbol_count,
    uint64_t universe,
    int write_workq)
{
    unsigned int state_length = 0;
    for (unsigned int i = 0; i < symbol_count; i++) {
        state_length += counts[i];
    }
    if (!square_count || square_count != state_length) {
        fprintf(stderr, "ERROR: ranked mode requires --squares matching --rank-counts\n");
        exit(1);
    }
    if (depth > 254) {
        fprintf(stderr, "ERROR: ranked depth must be <= 254\n");
        exit(1);
    }
    if (!__atomic_always_lock_free(1, 0)) {
        fprintf(stderr, "ERROR: this platform does not provide lock-free byte atomics\n");
        exit(1);
    }
    if (universe > SIZE_MAX) {
        fprintf(stderr, "ERROR: ranked universe is too large for this platform\n");
        exit(1);
    }

    FILE *input = fopen(inputfile, "rb");
    FILE *output = write_workq ? fopen(outputfile, "wb") : NULL;
    int cost_fd = open(cost_filename, O_RDWR);
    struct stat cost_stat;
    int symbol_of[256];
    if (!input || (write_workq && !output) || cost_fd < 0 || fstat(cost_fd, &cost_stat) != 0) {
        fprintf(stderr, "ERROR: could not open ranked input/output files\n");
        exit(1);
    }
    if ((uint64_t) cost_stat.st_size != universe) {
        fprintf(stderr, "ERROR: cost file is %jd bytes, expected %" PRIu64 "\n",
            (intmax_t) cost_stat.st_size, universe);
        exit(1);
    }
    if (write_workq && setvbuf(output, NULL, _IOFBF, RANKED_IO_BUFFER) != 0) {
        fprintf(stderr, "ERROR: could not size the ranked workq write buffer\n");
        exit(1);
    }
    if (setvbuf(input, NULL, _IOFBF, RANKED_IO_BUFFER) != 0) {
        fprintf(stderr, "ERROR: could not size the ranked workq read buffer\n");
        exit(1);
    }

    unsigned char *costs = mmap(NULL, universe, PROT_READ | PROT_WRITE, MAP_SHARED, cost_fd, 0);
    if (costs == MAP_FAILED) {
        fprintf(stderr, "ERROR: could not mmap %" PRIu64 " byte cost file\n", universe);
        exit(1);
    }
#ifdef MADV_HUGEPAGE
    /* Prefer huge pages when the kernel will use them. MADV_RANDOM was dropped
     * because it makes the kernel more willing to evict this 1-byte-per-state
     * array, which turns random CAS into disk faults (htop state D).
     */
    madvise(costs, (size_t) universe, MADV_HUGEPAGE);
#endif
    if (fseeko(input, (off_t) (start * RANKED_RECORD_SIZE), SEEK_SET) != 0) {
        fprintf(stderr, "ERROR: could not seek ranked workq\n");
        exit(1);
    }

    ensure_binom(square_count);
    memset(symbol_of, 0xff, sizeof(symbol_of));
    for (unsigned int symbol = 0; symbol < symbol_count; symbol++) {
        symbol_of[symbols[symbol]] = (int) symbol;
    }

    unsigned int *perm = build_compact_permutations(cube_size, squares, square_count, moves, moves_count);
    unsigned char *state = malloc(square_count);
    unsigned char *child = malloc(square_count);
    if (!state || !child) {
        fprintf(stderr, "ERROR: could not allocate ranked states\n");
        exit(1);
    }

    uint64_t winners = 0;
    unsigned char encoded_cost = depth + 1;
    for (uint64_t record_index = start; record_index <= end; record_index++) {
        uint64_t parent_rank = read_rank(input);
        int previous = fgetc(input);
        if (previous == EOF) {
            fprintf(stderr, "ERROR: truncated ranked workq\n");
            exit(1);
        }
        multiset_unrank(parent_rank, state, symbols, counts, symbol_count, square_count, universe);

        for (unsigned int move_index = 0; move_index < moves_count; move_index++) {
            move_type move = moves[move_index];
            unsigned char expected;
            uint64_t child_rank;
            if (steps_on_same_face_and_layer(move, (move_type) previous)) {
                continue;
            }
            for (unsigned int i = 0; i < square_count; i++) {
                child[perm[(move_index * square_count) + i]] = state[i];
            }
            if (memcmp(child, state, square_count) == 0) {
                continue;
            }

            child_rank = multiset_rank(child, symbol_of, counts, symbol_count, square_count);
            if (__atomic_load_n(&costs[child_rank], __ATOMIC_RELAXED)) {
                continue;
            }
            expected = 0;
            if (__atomic_compare_exchange_n(
                    &costs[child_rank], &expected, encoded_cost, 0,
                    __ATOMIC_RELAXED, __ATOMIC_RELAXED)) {
                winners++;
                if (write_workq) {
                    write_rank(output, child_rank, (unsigned char) move);
                }
            }
        }
    }

    printf("%" PRIu64 "\n", winners);
    free(perm);
    free(state);
    free(child);
    munmap(costs, universe);
    close(cost_fd);
    fclose(input);
    if (output) {
        fclose(output);
    }
}


void
process_workq(
    char *inputfile,
    char *outputfile,
    unsigned int linewidth,
    unsigned int start,
    unsigned int end,
    unsigned char cube_size,
    move_type moves[MOVE_MAX],
    unsigned int moves_count,
    unsigned int *squares,
    unsigned int square_count)
{
    FILE *fh_read = NULL;
    char *move_ptr = NULL;
    char *prev_move_ptr = NULL;

    int steps_to_scramble_length = 0;
    unsigned int full_size = (cube_size * cube_size * 6) + 1; // add 1 for the leading "x"
    unsigned int array_size = square_count ? square_count : full_size;
    size_t BUFFER_SIZE = 0;
    unsigned int line_length = 0;
    unsigned int sizeof_array_size = sizeof(char) * array_size;
    unsigned int to_write_count = 0;
    unsigned int file_count = 0;
    unsigned int *perm = NULL;

    unsigned char cube[array_size];
    unsigned char cube_tmp[array_size];
    unsigned char line[MAX_WORKQ_LINE_LENGTH];
    unsigned char move_index = 0;
    unsigned char move_str_length = 0;
    unsigned char read_result = 0;
    unsigned char steps_to_scramble[MAX_MOVE_STR_SIZE * MAX_MOVE_LENGTH];
    char *to_write_dedup = NULL;

    char space_delim[] = " ";

    move_type move = MOVE_NONE;
    move_type prev_move = MOVE_NONE;

    // The stride is table-specific to save memory, but BATCH_SIZE stays fixed because its
    // historical boundaries determine which equally short solution survives deduplication.
    line_width = LINE_WIDTH_FOR_STATE(array_size);
    batch_size = BATCH_SIZE;
    BUFFER_SIZE = (size_t) line_width * batch_size;

    to_write = malloc(BUFFER_SIZE);
    to_write_ptr = malloc((size_t) batch_size * sizeof(char *));
    to_write_dedup = malloc(BUFFER_SIZE);

    if (to_write == NULL || to_write_ptr == NULL || to_write_dedup == NULL) {
        printf("ERROR: process_workq could not allocate %zu bytes\n", BUFFER_SIZE);
        exit(1);
    }

    if (square_count) {
        perm = build_compact_permutations(cube_size, squares, square_count, moves, moves_count);
        LOG("compact states: %u of %u squares\n", square_count, full_size - 1);
    }

    // line_compare() needs this to know how much of each line is the state
    state_width = array_size;

    memset(line, '\0', sizeof(line));
    memset(cube, 0, sizeof_array_size);
    memset(cube_tmp, 0, sizeof_array_size);
    fh_read = fopen(inputfile, "r");

    if (fh_read == NULL) {
        printf("ERROR: process_workq could not open %s\n", inputfile);
        exit(1);
    }

    unsigned long seek_target = (unsigned long) start * (unsigned long) linewidth;
    fseek(fh_read, seek_target, SEEK_SET);

    LOG("read %dx%dx%d inputfile %s from line %d to %d, line width %d, batch %d lines, BUFFER_SIZE %zu MB\n",
        cube_size, cube_size, cube_size,
        inputfile, start, end, line_width, batch_size, (BUFFER_SIZE * 2) / MEGABYTE);

    for (unsigned int line_number = start; line_number <= end; line_number++) {
        read_result = fread(line, linewidth, 1, fh_read);

        if (!read_result) {
            printf("ERROR: process_workq read for line %d failed for %s\n", line_number, inputfile);
            exit(1);
        }

        strstrip(line);
        line_length = strlen(line);

        // We append one more move plus a "\n" and a "\0" to every line we buffer, so the
        // line we read has to leave room for all of that
        if (line_length + MAX_MOVE_STR_SIZE + 2 > line_width) {
            printf("ERROR: line %d is %d bytes, max supported is %d bytes\n",
                line_number, line_length, line_width - MAX_MOVE_STR_SIZE - 2);
            printf("%s\n", line);
            exit(1);
        }

        // Every line is "<state>:<moves>", so a missing ":" means our reads are not
        // landing on line boundaries. That happens when --linewidth disagrees with the
        // file we were handed, and without this check the misread bytes flow downstream
        // and abort() somewhere far less obvious.
        if (line_length <= array_size || line[array_size] != ':') {
            printf("ERROR: line %d has no ':' at offset %d, is --linewidth %d correct?\n",
                line_number, array_size, linewidth);
            printf("%s\n", line);
            exit(1);
        }

        memcpy(cube, line, array_size);

        // what was the last move used to get to this state?
        prev_move = MOVE_NONE;
        steps_to_scramble_length = line_length - array_size - 1;

        if (steps_to_scramble_length > 0) {

            // printf("\nBEGIN%sEND\n", line);
            // printf("line_number %d\n", line_number);
            // printf("line_length %d\n", line_length);
            // printf("steps_to_scramble_length %d\n", steps_to_scramble_length);

            // strtok() below needs a terminator, so the steps have to leave room for one.
            // Without this check an oversized steps field is a silent stack smash, and it
            // does not take a corrupt workq to get one: if --linewidth disagrees with the
            // file then every fread() lands mid-line and steps_to_scramble_length is junk.
            if ((size_t) steps_to_scramble_length >= sizeof(steps_to_scramble)) {
                printf("ERROR: line %d has %d bytes of steps, max supported is %zu bytes\n",
                    line_number, steps_to_scramble_length, sizeof(steps_to_scramble) - 1);
                printf("%s\n", line);
                exit(1);
            }

            memset(steps_to_scramble, '\0', sizeof(steps_to_scramble));
            memcpy(steps_to_scramble, &line[array_size+1], steps_to_scramble_length);
            move_ptr = strtok(steps_to_scramble, space_delim);

            // printf("steps_to_scramble %s\n", steps_to_scramble);
            // printf("move_ptr %s\n", move_ptr);
            prev_move_ptr = move_ptr;

            while (move_ptr != NULL) {
                move_ptr = strtok(NULL, space_delim);

                if (move_ptr != NULL) {
                    prev_move_ptr = move_ptr;
                }
            }

            prev_move = str2move(prev_move_ptr);

        // if this is a starting state, write the line as is
        } else if (steps_to_scramble_length == 0) {
            line[line_length] = '\n';
            line[line_length+1] = '\0';

            // copy the '\0' too, so that to_write does not have to be pre-zeroed
            memcpy(TO_WRITE_LINE(to_write_count), line, strlen(line) + 1);
            to_write_count++;

            if (to_write_count == batch_size) {
                file_count = write_to_write_buffer(
                    to_write_dedup, array_size, to_write_count, outputfile, file_count);
                to_write_count = 0;
            }

        } else {
            printf("ERROR: invalid steps_to_scramble_length %d, line_length %d, array_size %d",
                steps_to_scramble_length, line_length, array_size);
            exit(1);
        }

        // loop over all of the moves we are using to build this lookup table
        for (move_index = 0; move_index < moves_count; move_index++) {
            move = moves[move_index];

            // do not perform two moves back-to-back on the same face/layer
            if (steps_on_same_face_and_layer(move, prev_move)) {
                continue;
            }

            // copy cube to cube_tmp and apply "move" to cube_tmp
            if (perm) {
                for (unsigned int i = 0; i < square_count; i++) {
                    cube_tmp[perm[(move_index * square_count) + i]] = cube[i];
                }
            } else {
                memcpy(cube_tmp, cube, sizeof_array_size);
                rotate_full_cube((char *) cube_tmp, (char *) cube, array_size, cube_size, move);
            }

            // if nothing changed, do not bother writing this result to the file
            if (memcmp(cube_tmp, cube, sizeof_array_size) == 0) {
                continue;
            }

            // use our "line" buffer to create the output to write to the file
            // start with copying the cube_tmp state
            memcpy(line, cube_tmp, sizeof_array_size);
            move_str_length = strlen(move2str[move]);

            // then add a space (if needed) followed by the move we just performed
            if (line[line_length-1] == ':') {
                memcpy(&line[line_length], move2str[move], move_str_length);
                line[line_length + move_str_length] = '\n';
                line[line_length + move_str_length + 1] = '\0';
            } else {
                line[line_length] = ' ';
                memcpy(&line[line_length + 1], move2str[move], move_str_length);
                line[line_length + 1 + move_str_length] = '\n';
                line[line_length + 1 + move_str_length + 1] = '\0';
            }

            // copy the "line" we just contructed to our to_write buffer, including the
            // '\0' so that to_write does not have to be pre-zeroed
            memcpy(TO_WRITE_LINE(to_write_count), line, strlen(line) + 1);
            to_write_count++;

            if (to_write_count == batch_size) {
                file_count = write_to_write_buffer(
                    to_write_dedup, array_size, to_write_count, outputfile, file_count);
                to_write_count = 0;
            }
        }
    }

    if (to_write_count) {
        file_count = write_to_write_buffer(
            to_write_dedup, array_size, to_write_count, outputfile, file_count);
        to_write_count = 0;
    }

    fclose(fh_read);
    free(to_write);
    free(to_write_ptr);
    free(to_write_dedup);

    if (perm) {
        free(perm);
    }
}


int
main (int argc, char *argv[])
{
    unsigned int linewidth = 0;
    uint64_t start = 0;
    uint64_t end = 0;
    uint64_t rank_universe = 0;
    unsigned char cube_size = 0;
    unsigned int ranked_depth = 0;
    char inputfile[MAX_FILENAME_SIZE];
    char outputfile[MAX_FILENAME_SIZE];
    char ranked_cost[MAX_FILENAME_SIZE];
    char ranked_input[MAX_FILENAME_SIZE];
    char ranked_output[MAX_FILENAME_SIZE];
    char moves_buffer[512];
    char squares_buffer[MAX_SQUARES_ARG];
    char rank_symbols[MAX_RANK_SYMBOLS + 1];
    char rank_counts_buffer[MAX_SQUARES_ARG];
    unsigned int squares[MAX_COMPACT_SQUARES];
    unsigned int rank_counts[MAX_RANK_SYMBOLS];
    unsigned int square_count = 0;
    unsigned int rank_symbol_count = 0;
    int ranked_no_workq = 0;
    memset(inputfile, '\0', sizeof(char) * MAX_FILENAME_SIZE);
    memset(outputfile, '\0', sizeof(char) * MAX_FILENAME_SIZE);
    memset(ranked_cost, '\0', sizeof(ranked_cost));
    memset(ranked_input, '\0', sizeof(ranked_input));
    memset(ranked_output, '\0', sizeof(ranked_output));
    memset(squares_buffer, '\0', sizeof(squares_buffer));
    memset(rank_symbols, '\0', sizeof(rank_symbols));
    memset(rank_counts_buffer, '\0', sizeof(rank_counts_buffer));

    for (int i = 1; i < argc; i++) {
        if (strmatch(argv[i], "--inputfile")) {
            i++;
            strcpy(inputfile, argv[i]);

        } else if (strmatch(argv[i], "--outputfile")) {
            i++;
            strcpy(outputfile, argv[i]);

        } else if (strmatch(argv[i], "--start")) {
            i++;
            start = strtoull(argv[i], NULL, 10);

        } else if (strmatch(argv[i], "--end")) {
            i++;
            end = strtoull(argv[i], NULL, 10);

        } else if (strmatch(argv[i], "--linewidth")) {
            i++;
            linewidth = atoi(argv[i]);

        } else if (strmatch(argv[i], "--size")) {
            i++;
            cube_size = atoi(argv[i]);

        } else if (strmatch(argv[i], "--moves")) {
            i++;
            strcpy(moves_buffer, argv[i]);

        } else if (strmatch(argv[i], "--squares")) {
            i++;
            strncpy(squares_buffer, argv[i], MAX_SQUARES_ARG - 1);

        } else if (strmatch(argv[i], "--ranked-cost")) {
            i++;
            strncpy(ranked_cost, argv[i], MAX_FILENAME_SIZE - 1);

        } else if (strmatch(argv[i], "--ranked-input")) {
            i++;
            strncpy(ranked_input, argv[i], MAX_FILENAME_SIZE - 1);

        } else if (strmatch(argv[i], "--ranked-output")) {
            i++;
            strncpy(ranked_output, argv[i], MAX_FILENAME_SIZE - 1);

        } else if (strmatch(argv[i], "--ranked-depth")) {
            i++;
            ranked_depth = (unsigned int) strtoul(argv[i], NULL, 10);

        } else if (strmatch(argv[i], "--rank-symbols")) {
            i++;
            strncpy(rank_symbols, argv[i], MAX_RANK_SYMBOLS);

        } else if (strmatch(argv[i], "--rank-counts")) {
            i++;
            strncpy(rank_counts_buffer, argv[i], MAX_SQUARES_ARG - 1);

        } else if (strmatch(argv[i], "--rank-universe")) {
            i++;
            rank_universe = strtoull(argv[i], NULL, 10);

        } else if (strmatch(argv[i], "--ranked-no-workq")) {
            ranked_no_workq = 1;

        } else if (strmatch(argv[i], "-h") || strmatch(argv[i], "--help")) {
            printf("\nTODO\n\n");
            exit(0);

        } else {
            printf("ERROR: %s is an invalid arg\n\n", argv[i]);
            exit(1);
        }
    }

    if (cube_size < 2 || cube_size > 7) {
        printf("ERROR: only 2x2x2 through 7x7x7 cubes are supported, yours is %dx%dx%d\n", cube_size, cube_size, cube_size);
        exit(1);
    }

    if (!ranked_cost[0] && linewidth == 0) {
        printf("ERROR: must specify --linewidth\n");
        exit(1);
    }

    if (linewidth > MAX_WORKQ_LINE_LENGTH) {
        printf("ERROR: --linewidth %d is larger than our %d byte line buffer\n", linewidth, MAX_WORKQ_LINE_LENGTH);
        exit(1);
    }

    if (cube_size == 0) {
        printf("ERROR: must specify --size\n");
        exit(1);
    }

    // create the moves array
    unsigned int moves_index = 0;
    char space_delim[] = " ";
    char *move_ptr = strtok(moves_buffer, space_delim);
    move_type moves[MOVE_MAX];
    memset(moves, MOVE_MAX, sizeof(move_type) * MOVE_MAX);

    while (move_ptr != NULL) {
        moves[moves_index] = str2move(move_ptr);
        move_ptr = strtok(NULL, space_delim);
        moves_index++;
    }

    if (squares_buffer[0]) {
        square_count = parse_squares(squares_buffer, squares);
    }

    if (ranked_cost[0]) {
        rank_symbol_count = strlen(rank_symbols);
        unsigned int rank_count_count = parse_rank_counts(rank_counts_buffer, rank_counts);
        if (!ranked_input[0] || (!ranked_no_workq && !ranked_output[0]) ||
                !rank_symbol_count || rank_symbol_count != rank_count_count || !rank_universe) {
            fprintf(stderr, "ERROR: ranked mode requires input/output, symbols, counts and universe\n");
            exit(1);
        }
        for (unsigned int i = 1; i < rank_symbol_count; i++) {
            if ((unsigned char) rank_symbols[i - 1] >= (unsigned char) rank_symbols[i]) {
                fprintf(stderr, "ERROR: --rank-symbols must be unique and sorted\n");
                exit(1);
            }
        }
        if (ranked_depth > 254) {
            fprintf(stderr, "ERROR: ranked depth must be <= 254\n");
            exit(1);
        }
        process_ranked_workq(
            ranked_input, ranked_output, ranked_cost, start, end, (unsigned char) ranked_depth,
            cube_size, moves, moves_index, squares, square_count,
            (unsigned char *) rank_symbols, rank_counts, rank_symbol_count,
            rank_universe, !ranked_no_workq);
    } else {
        if (start > UINT_MAX || end > UINT_MAX) {
            fprintf(stderr, "ERROR: text workq line range exceeds UINT_MAX\n");
            exit(1);
        }
        process_workq(
            inputfile, outputfile, linewidth, (unsigned int) start, (unsigned int) end,
            cube_size, moves, moves_index, squares, square_count);
    }
}

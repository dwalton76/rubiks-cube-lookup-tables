
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
#include "center_symmetry_444.h"
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
#define MAX_RANK_GROUPS 32
#define RANKED_RECORD_SIZE 9
#define MAX_BINOM 64
#define RANKED_IO_BUFFER (8 * 1024 * 1024)

static uint64_t binom_table[MAX_BINOM + 1][MAX_BINOM + 1];
static unsigned int binom_ready_n = 0;

typedef struct {
    unsigned int offset;
    unsigned int length;
    unsigned int symbol_count;
    unsigned char symbols[MAX_RANK_SYMBOLS + 1];
    unsigned int counts[MAX_RANK_SYMBOLS];
    uint64_t universe;
} rank_group_type;

typedef enum {
    RANK_MULTISET,
    RANK_PAIRED_MULTISET,
    RANK_EDGE_PAIRING_EVEN,
    RANK_WING_BINARY,
    RANK_ORIENTATION_BITS,
    RANK_CENTER_SYMMETRY_444,
} rank_type;


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
parse_unsigned_list(char *arg, unsigned int *values, unsigned int maximum_count)
{
    unsigned int count = 0;
    char *ptr = strtok(arg, ",");
    while (ptr != NULL) {
        if (count >= maximum_count) {
            fprintf(stderr, "ERROR: too many unsigned-list entries\n");
            exit(1);
        }
        values[count++] = (unsigned int) strtoul(ptr, NULL, 10);
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
 * Parse "length:symbols:count,count:universe[;...]" into contiguous compact-state
 * groups. A single group continues to use the historical command-line options.
 */
static unsigned int
parse_rank_groups(char *arg, rank_group_type *groups)
{
    unsigned int group_count = 0;
    unsigned int offset = 0;
    char *group_save = NULL;
    char *group_arg = strtok_r(arg, ";", &group_save);

    while (group_arg != NULL) {
        char *field_save = NULL;
        char *length_arg;
        char *symbols_arg;
        char *counts_arg;
        char *universe_arg;
        rank_group_type *group;

        if (group_count >= MAX_RANK_GROUPS) {
            fprintf(stderr, "ERROR: too many --rank-groups entries\n");
            exit(1);
        }
        length_arg = strtok_r(group_arg, ":", &field_save);
        symbols_arg = strtok_r(NULL, ":", &field_save);
        counts_arg = strtok_r(NULL, ":", &field_save);
        universe_arg = strtok_r(NULL, ":", &field_save);
        if (!length_arg || !symbols_arg || !counts_arg || !universe_arg ||
                strtok_r(NULL, ":", &field_save) != NULL) {
            fprintf(stderr, "ERROR: invalid --rank-groups entry\n");
            exit(1);
        }

        group = &groups[group_count];
        memset(group, 0, sizeof(*group));
        group->offset = offset;
        group->length = (unsigned int) strtoul(length_arg, NULL, 10);
        group->symbol_count = strlen(symbols_arg);
        group->universe = strtoull(universe_arg, NULL, 10);
        if (!group->length || !group->symbol_count ||
                group->symbol_count > MAX_RANK_SYMBOLS || !group->universe) {
            fprintf(stderr, "ERROR: invalid --rank-groups values\n");
            exit(1);
        }
        memcpy(group->symbols, symbols_arg, group->symbol_count);
        if (parse_rank_counts(counts_arg, group->counts) != group->symbol_count) {
            fprintf(stderr, "ERROR: --rank-groups symbols and counts do not agree\n");
            exit(1);
        }
        for (unsigned int i = 1; i < group->symbol_count; i++) {
            if (group->symbols[i - 1] >= group->symbols[i]) {
                fprintf(stderr, "ERROR: rank group symbols must be unique and sorted\n");
                exit(1);
            }
        }
        unsigned int count_total = 0;
        for (unsigned int i = 0; i < group->symbol_count; i++) {
            count_total += group->counts[i];
        }
        if (count_total != group->length) {
            fprintf(stderr, "ERROR: rank group length and counts do not agree\n");
            exit(1);
        }

        offset += group->length;
        group_count++;
        group_arg = strtok_r(NULL, ";", &group_save);
    }
    return group_count;
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

static void
grouped_multiset_unrank(
    uint64_t rank,
    unsigned char *state,
    const rank_group_type *groups,
    unsigned int group_count,
    uint64_t universe)
{
    uint64_t component_ranks[MAX_RANK_GROUPS];

    if (rank >= universe) {
        fprintf(stderr, "ERROR: rank %" PRIu64 " is outside universe %" PRIu64 "\n", rank, universe);
        exit(1);
    }
    for (unsigned int i = group_count; i-- > 0;) {
        component_ranks[i] = rank % groups[i].universe;
        rank /= groups[i].universe;
    }
    if (rank) {
        fprintf(stderr, "ERROR: grouped rank universes do not cover the configured universe\n");
        exit(1);
    }
    for (unsigned int i = 0; i < group_count; i++) {
        multiset_unrank(
            component_ranks[i], state + groups[i].offset, groups[i].symbols,
            groups[i].counts, groups[i].symbol_count, groups[i].length, groups[i].universe);
    }
}

static uint64_t
grouped_multiset_rank(
    const unsigned char *state,
    const int symbol_of[MAX_RANK_GROUPS][256],
    const rank_group_type *groups,
    unsigned int group_count)
{
    uint64_t rank = 0;

    for (unsigned int i = 0; i < group_count; i++) {
        uint64_t component = multiset_rank(
            state + groups[i].offset, symbol_of[i], groups[i].counts,
            groups[i].symbol_count, groups[i].length);
        if (rank > (UINT64_MAX - component) / groups[i].universe) {
            fprintf(stderr, "ERROR: grouped ranked multiset arithmetic overflow\n");
            exit(1);
        }
        rank = (rank * groups[i].universe) + component;
    }
    return rank;
}

static uint64_t
center_symmetry_rank_444(
    const unsigned char *state,
    const int symbol_of[MAX_RANK_GROUPS][256],
    const rank_group_type *groups)
{
    unsigned char transformed[CENTER_SYMMETRY_STICKERS_444];
    unsigned char canonical[CENTER_SYMMETRY_STICKERS_444];

    for (unsigned int symmetry = 0; symmetry < CENTER_SYMMETRY_COUNT_444; symmetry++) {
        transform_centers_444(state, transformed, symmetry);
        if (!symmetry || memcmp(transformed, canonical, sizeof(canonical)) < 0) {
            memcpy(canonical, transformed, sizeof(canonical));
        }
    }
    return grouped_multiset_rank(canonical, symbol_of, groups, 1);
}


static uint64_t
even_permutation_universe(unsigned int length)
{
    uint64_t result = 1;
    if (length < 2) {
        fprintf(stderr, "ERROR: even permutations require at least two symbols\n");
        exit(1);
    }
    for (unsigned int value = 3; value <= length; value++) {
        if (result > UINT64_MAX / value) {
            fprintf(stderr, "ERROR: even permutation universe overflow\n");
            exit(1);
        }
        result *= value;
    }
    return result;
}


static void
even_permutation_unrank(uint64_t rank, unsigned int length, unsigned char *permutation)
{
    unsigned int digits[MAX_RANK_SYMBOLS] = {0};
    unsigned char remaining[MAX_RANK_SYMBOLS];
    uint64_t universe = even_permutation_universe(length);

    if (length > MAX_RANK_SYMBOLS || rank >= universe) {
        fprintf(stderr, "ERROR: invalid even permutation rank\n");
        exit(1);
    }
    for (unsigned int i = 0; i < length; i++) {
        remaining[i] = (unsigned char) i;
    }
    for (int i = (int) length - 3; i >= 0; i--) {
        unsigned int radix = length - (unsigned int) i;
        digits[i] = rank % radix;
        rank /= radix;
    }
    for (unsigned int i = 0; i < length - 2; i++) {
        digits[length - 2] ^= digits[i] & 1;
    }
    for (unsigned int i = 0; i < length; i++) {
        permutation[i] = remaining[digits[i]];
        memmove(
            &remaining[digits[i]], &remaining[digits[i] + 1],
            length - digits[i] - 1);
    }
}


static uint64_t
even_permutation_rank(const unsigned char *permutation, unsigned int length)
{
    unsigned char remaining[MAX_RANK_SYMBOLS];
    uint64_t rank = 0;
    unsigned int parity = 0;

    if (length < 2 || length > MAX_RANK_SYMBOLS) {
        fprintf(stderr, "ERROR: invalid even permutation length\n");
        exit(1);
    }
    for (unsigned int i = 0; i < length; i++) {
        remaining[i] = (unsigned char) i;
    }
    for (unsigned int i = 0; i < length; i++) {
        unsigned int digit = 0;
        while (digit < length - i && remaining[digit] != permutation[i]) {
            digit++;
        }
        if (digit == length - i) {
            fprintf(stderr, "ERROR: invalid edge-pairing permutation\n");
            exit(1);
        }
        parity ^= digit & 1;
        if (i < length - 2) {
            rank = (rank * (length - i)) + digit;
        }
        memmove(&remaining[digit], &remaining[digit + 1], length - i - digit - 1);
    }
    if (parity) {
        fprintf(stderr, "ERROR: edge-pairing move left the even permutation orbit\n");
        exit(1);
    }
    return rank;
}


static void
edge_pairing_unrank_cube(
    uint64_t rank,
    unsigned char *cube,
    unsigned int full_size,
    const unsigned int *squares,
    const unsigned int *partners,
    unsigned int pair_count)
{
    unsigned char permutation[MAX_RANK_SYMBOLS];
    memset(cube, '.', full_size);
    cube[0] = 'x';
    even_permutation_unrank(rank, pair_count, permutation);

    for (unsigned int high = 0; high < pair_count; high++) {
        unsigned char symbol = (unsigned char) (high + 1);
        unsigned int low = permutation[high];
        cube[squares[high]] = symbol;
        cube[partners[high]] = symbol;
        cube[squares[pair_count + low]] = symbol;
        cube[partners[pair_count + low]] = symbol;
    }
}


static uint64_t
edge_pairing_rank_cube(
    const unsigned char *cube,
    const unsigned int *squares,
    unsigned int pair_count)
{
    unsigned char low_position[256];
    unsigned char permutation[MAX_RANK_SYMBOLS];
    memset(low_position, 0xff, sizeof(low_position));

    for (unsigned int low = 0; low < pair_count; low++) {
        low_position[cube[squares[pair_count + low]]] = (unsigned char) low;
    }
    for (unsigned int high = 0; high < pair_count; high++) {
        unsigned char position = low_position[cube[squares[high]]];
        if (position == 0xff) {
            fprintf(stderr, "ERROR: high edge has no matching low edge\n");
            exit(1);
        }
        permutation[high] = position;
    }
    return even_permutation_rank(permutation, pair_count);
}


static void
wing_binary_unrank_cube(
    uint64_t rank,
    unsigned char *cube,
    unsigned int full_size,
    const unsigned int *squares,
    const unsigned int *partners,
    unsigned int partner_flip_mask,
    const rank_group_type *groups,
    unsigned int group_count,
    uint64_t universe)
{
    unsigned char compact[MAX_COMPACT_SQUARES];
    memset(cube, '.', full_size);
    cube[0] = 'x';
    grouped_multiset_unrank(rank, compact, groups, group_count, universe);
    for (unsigned int i = 0; i < groups[0].length; i++) {
        cube[squares[i]] = compact[i];
        cube[partners[i]] = (partner_flip_mask & (1U << i))
            ? (compact[i] == 'U' ? 'D' : 'U')
            : compact[i];
    }
}


static uint64_t
wing_binary_rank_cube(
    const unsigned char *cube,
    const unsigned int *squares,
    const int symbol_of[MAX_RANK_GROUPS][256],
    const rank_group_type *groups,
    unsigned int group_count)
{
    unsigned char compact[MAX_COMPACT_SQUARES];
    unsigned int square_count = 0;
    for (unsigned int group = 0; group < group_count; group++) {
        square_count += groups[group].length;
    }
    for (unsigned int i = 0; i < square_count; i++) {
        compact[i] = cube[squares[i]];
    }
    return grouped_multiset_rank(compact, symbol_of, groups, group_count);
}


static void
paired_multiset_unrank_cube(
    uint64_t rank,
    unsigned char *cube,
    unsigned int full_size,
    const unsigned int *squares,
    const unsigned int *partners,
    const rank_group_type *groups,
    unsigned int group_count,
    uint64_t universe)
{
    unsigned char compact[MAX_COMPACT_SQUARES];
    unsigned int square_count = 0;
    memset(cube, '.', full_size);
    cube[0] = 'x';
    grouped_multiset_unrank(rank, compact, groups, group_count, universe);
    for (unsigned int group = 0; group < group_count; group++) {
        square_count += groups[group].length;
    }
    for (unsigned int i = 0; i < square_count; i++) {
        cube[squares[i]] = compact[i];
        cube[partners[i]] = compact[i];
    }
}


static void
orientation_bits_unrank_cube(
    uint64_t rank,
    unsigned char *cube,
    unsigned int full_size,
    const unsigned int *squares,
    const unsigned int *partners,
    unsigned int square_count,
    unsigned int partner_flip_mask)
{
    memset(cube, '.', full_size);
    cube[0] = 'x';
    for (unsigned int i = 0; i < square_count; i++) {
        unsigned char value = (rank & (1ULL << i)) ? 'D' : 'U';
        cube[squares[i]] = value;
        cube[partners[i]] = (partner_flip_mask & (1U << i))
            ? (value == 'U' ? 'D' : 'U')
            : value;
    }
}


static uint64_t
orientation_bits_rank_cube(
    const unsigned char *cube,
    const unsigned int *squares,
    unsigned int square_count)
{
    uint64_t rank = 0;
    for (unsigned int i = 0; i < square_count; i++) {
        if (cube[squares[i]] == 'D') {
            rank |= 1ULL << i;
        }
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
    const unsigned int *pairing_partners,
    unsigned int pairing_partner_count,
    const unsigned int *wing_flip_masks,
    unsigned int wing_flip_mask_count,
    unsigned int wing_partner_flip_mask,
    rank_type configured_rank_type,
    const rank_group_type *groups,
    unsigned int group_count,
    uint64_t universe,
    int write_workq)
{
    unsigned int state_length = 0;
    uint64_t configured_universe = 1;
    unsigned int pair_count = 0;
    unsigned int full_size = (cube_size * cube_size * 6) + 1;

    if (configured_rank_type == RANK_EDGE_PAIRING_EVEN) {
        if (!square_count || square_count % 2 || pairing_partner_count != square_count) {
            fprintf(stderr, "ERROR: edge pairing requires equally sized square and partner lists\n");
            exit(1);
        }
        pair_count = square_count / 2;
        configured_universe = even_permutation_universe(pair_count);
        state_length = full_size;
        for (unsigned int i = 0; i < square_count; i++) {
            if (squares[i] >= full_size || pairing_partners[i] >= full_size) {
                fprintf(stderr, "ERROR: edge-pairing square is outside the cube\n");
                exit(1);
            }
        }
    } else if (configured_rank_type == RANK_ORIENTATION_BITS) {
        if (!square_count || square_count > 32 || pairing_partner_count != square_count ||
                wing_flip_mask_count != moves_count) {
            fprintf(stderr, "ERROR: orientation-bits rank requires partners and one flip mask per move\n");
            exit(1);
        }
        if (universe != (1ULL << square_count)) {
            fprintf(stderr, "ERROR: orientation-bits universe must be 2^square_count\n");
            exit(1);
        }
        configured_universe = universe;
        state_length = full_size;
        for (unsigned int i = 0; i < square_count; i++) {
            if (squares[i] >= full_size || pairing_partners[i] >= full_size) {
                fprintf(stderr, "ERROR: orientation-bits square is outside the cube\n");
                exit(1);
            }
        }
    } else {
        for (unsigned int i = 0; i < group_count; i++) {
            state_length += groups[i].length;
            ensure_binom(groups[i].length);
            uint64_t group_universe = multiset_perms(
                groups[i].counts, groups[i].symbol_count, groups[i].length);
            if (group_universe != groups[i].universe) {
                fprintf(stderr, "ERROR: rank group %u universe is %" PRIu64 ", expected %" PRIu64 "\n",
                    i, group_universe, groups[i].universe);
                exit(1);
            }
            if (configured_universe > UINT64_MAX / groups[i].universe) {
                fprintf(stderr, "ERROR: grouped ranked universe overflow\n");
                exit(1);
            }
            configured_universe *= groups[i].universe;
        }
        if (!group_count || !square_count || square_count != state_length) {
            fprintf(stderr, "ERROR: ranked mode requires --squares matching --rank-counts\n");
            exit(1);
        }
        if (configured_rank_type == RANK_WING_BINARY ||
                configured_rank_type == RANK_PAIRED_MULTISET) {
            if (pairing_partner_count != square_count ||
                    (configured_rank_type == RANK_WING_BINARY &&
                     (group_count != 1 || wing_flip_mask_count != moves_count))) {
                fprintf(stderr, "ERROR: paired rank requires partners (and wing-binary needs one group and flip mask per move)\n");
                exit(1);
            }
            for (unsigned int i = 0; i < square_count; i++) {
                if (squares[i] >= full_size || pairing_partners[i] >= full_size) {
                    fprintf(stderr, "ERROR: paired square is outside the cube\n");
                    exit(1);
                }
            }
            state_length = full_size;
        }
    }
    if (configured_universe != universe) {
        fprintf(stderr, "ERROR: rank group universes multiply to %" PRIu64 ", expected %" PRIu64 "\n",
            configured_universe, universe);
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
    int symbol_of[MAX_RANK_GROUPS][256];
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

    memset(symbol_of, 0xff, sizeof(symbol_of));
    for (unsigned int group = 0; group < group_count; group++) {
        for (unsigned int symbol = 0; symbol < groups[group].symbol_count; symbol++) {
            symbol_of[group][groups[group].symbols[symbol]] = (int) symbol;
        }
    }

    unsigned int *perm = (configured_rank_type == RANK_MULTISET ||
            configured_rank_type == RANK_CENTER_SYMMETRY_444)
        ? build_compact_permutations(cube_size, squares, square_count, moves, moves_count)
        : NULL;
    unsigned char *state = malloc(state_length);
    unsigned char *child = malloc(state_length);
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
        if (configured_rank_type == RANK_EDGE_PAIRING_EVEN) {
            edge_pairing_unrank_cube(
                parent_rank, state, full_size, squares, pairing_partners, pair_count);
        } else if (configured_rank_type == RANK_WING_BINARY) {
            wing_binary_unrank_cube(
                parent_rank, state, full_size, squares, pairing_partners,
                wing_partner_flip_mask,
                groups, group_count, universe);
        } else if (configured_rank_type == RANK_PAIRED_MULTISET) {
            paired_multiset_unrank_cube(
                parent_rank, state, full_size, squares, pairing_partners,
                groups, group_count, universe);
        } else if (configured_rank_type == RANK_ORIENTATION_BITS) {
            orientation_bits_unrank_cube(
                parent_rank, state, full_size, squares, pairing_partners,
                square_count, wing_partner_flip_mask);
        } else {
            grouped_multiset_unrank(parent_rank, state, groups, group_count, universe);
        }

        for (unsigned int move_index = 0; move_index < moves_count; move_index++) {
            move_type move = moves[move_index];
            unsigned char expected;
            uint64_t child_rank;
            if (steps_on_same_face_and_layer(move, (move_type) previous)) {
                continue;
            }
            if (configured_rank_type == RANK_EDGE_PAIRING_EVEN) {
                rotate_full_cube((char *) child, (char *) state, full_size, cube_size, move);
                child_rank = edge_pairing_rank_cube(child, squares, pair_count);
            } else if (configured_rank_type == RANK_PAIRED_MULTISET) {
                rotate_full_cube((char *) child, (char *) state, full_size, cube_size, move);
                child_rank = wing_binary_rank_cube(child, squares, symbol_of, groups, group_count);
            } else if (configured_rank_type == RANK_WING_BINARY ||
                    configured_rank_type == RANK_ORIENTATION_BITS) {
                rotate_full_cube((char *) child, (char *) state, full_size, cube_size, move);
                for (unsigned int i = 0; i < square_count; i++) {
                    if (wing_flip_masks[move_index] & (1U << i)) {
                        child[squares[i]] = child[squares[i]] == 'U' ? 'D' : 'U';
                        child[pairing_partners[i]] =
                            child[pairing_partners[i]] == 'U' ? 'D' : 'U';
                    }
                }
                child_rank = configured_rank_type == RANK_WING_BINARY
                    ? wing_binary_rank_cube(child, squares, symbol_of, groups, group_count)
                    : orientation_bits_rank_cube(child, squares, square_count);
            } else {
                for (unsigned int i = 0; i < square_count; i++) {
                    child[perm[(move_index * square_count) + i]] = state[i];
                }
                child_rank = configured_rank_type == RANK_CENTER_SYMMETRY_444
                    ? center_symmetry_rank_444(child, symbol_of, groups)
                    : grouped_multiset_rank(child, symbol_of, groups, group_count);
            }
            if (child_rank == parent_rank) {
                continue;
            }
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

    free(perm);
    free(state);
    free(child);
    munmap(costs, universe);
    close(cost_fd);
    fclose(input);
    if (output) {
        if (fflush(output) != 0 || fclose(output) != 0) {
            fprintf(stderr, "ERROR: could not flush ranked workq output\n");
            exit(1);
        }
    }
    printf("%" PRIu64 "\n", winners);
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
    char rank_groups_buffer[MAX_SQUARES_ARG];
    char rank_type_buffer[64];
    char pairing_partners_buffer[MAX_SQUARES_ARG];
    char wing_flip_masks_buffer[MAX_SQUARES_ARG];
    unsigned int squares[MAX_COMPACT_SQUARES];
    unsigned int pairing_partners[MAX_COMPACT_SQUARES];
    unsigned int wing_flip_masks[MOVE_MAX];
    unsigned int rank_counts[MAX_RANK_SYMBOLS];
    rank_group_type rank_groups[MAX_RANK_GROUPS];
    unsigned int square_count = 0;
    unsigned int pairing_partner_count = 0;
    unsigned int wing_flip_mask_count = 0;
    unsigned int wing_partner_flip_mask = 0;
    unsigned int rank_symbol_count = 0;
    unsigned int rank_group_count = 0;
    int ranked_no_workq = 0;
    rank_type configured_rank_type = RANK_MULTISET;
    memset(inputfile, '\0', sizeof(char) * MAX_FILENAME_SIZE);
    memset(outputfile, '\0', sizeof(char) * MAX_FILENAME_SIZE);
    memset(ranked_cost, '\0', sizeof(ranked_cost));
    memset(ranked_input, '\0', sizeof(ranked_input));
    memset(ranked_output, '\0', sizeof(ranked_output));
    memset(squares_buffer, '\0', sizeof(squares_buffer));
    memset(rank_symbols, '\0', sizeof(rank_symbols));
    memset(rank_counts_buffer, '\0', sizeof(rank_counts_buffer));
    memset(rank_groups_buffer, '\0', sizeof(rank_groups_buffer));
    memset(rank_type_buffer, '\0', sizeof(rank_type_buffer));
    memset(pairing_partners_buffer, '\0', sizeof(pairing_partners_buffer));
    memset(wing_flip_masks_buffer, '\0', sizeof(wing_flip_masks_buffer));
    memset(rank_groups, 0, sizeof(rank_groups));

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

        } else if (strmatch(argv[i], "--rank-groups")) {
            i++;
            strncpy(rank_groups_buffer, argv[i], MAX_SQUARES_ARG - 1);

        } else if (strmatch(argv[i], "--rank-type")) {
            i++;
            strncpy(rank_type_buffer, argv[i], sizeof(rank_type_buffer) - 1);

        } else if (strmatch(argv[i], "--pairing-partners")) {
            i++;
            strncpy(pairing_partners_buffer, argv[i], MAX_SQUARES_ARG - 1);

        } else if (strmatch(argv[i], "--wing-flip-masks")) {
            i++;
            strncpy(wing_flip_masks_buffer, argv[i], MAX_SQUARES_ARG - 1);

        } else if (strmatch(argv[i], "--wing-partner-flip-mask")) {
            i++;
            wing_partner_flip_mask = (unsigned int) strtoul(argv[i], NULL, 10);

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
    if (pairing_partners_buffer[0]) {
        pairing_partner_count = parse_squares(pairing_partners_buffer, pairing_partners);
    }
    if (wing_flip_masks_buffer[0]) {
        wing_flip_mask_count = parse_unsigned_list(wing_flip_masks_buffer, wing_flip_masks, MOVE_MAX);
    }

    if (ranked_cost[0]) {
        if (!rank_type_buffer[0] || strmatch(rank_type_buffer, "multiset")) {
            configured_rank_type = RANK_MULTISET;
        } else if (strmatch(rank_type_buffer, "paired-multiset")) {
            configured_rank_type = RANK_PAIRED_MULTISET;
        } else if (strmatch(rank_type_buffer, "edge-pairing-even")) {
            configured_rank_type = RANK_EDGE_PAIRING_EVEN;
        } else if (strmatch(rank_type_buffer, "wing-binary")) {
            configured_rank_type = RANK_WING_BINARY;
        } else if (strmatch(rank_type_buffer, "orientation-bits")) {
            configured_rank_type = RANK_ORIENTATION_BITS;
        } else if (strmatch(rank_type_buffer, "center-symmetry-444")) {
            configured_rank_type = RANK_CENTER_SYMMETRY_444;
        } else {
            fprintf(stderr, "ERROR: unsupported --rank-type %s\n", rank_type_buffer);
            exit(1);
        }

        if (configured_rank_type == RANK_EDGE_PAIRING_EVEN) {
            if (rank_groups_buffer[0] || rank_symbols[0] || rank_counts_buffer[0]) {
                fprintf(stderr, "ERROR: edge rank cannot use multiset rank options\n");
                exit(1);
            }
        } else if (configured_rank_type == RANK_ORIENTATION_BITS) {
            if (rank_groups_buffer[0] || rank_symbols[0] || rank_counts_buffer[0]) {
                fprintf(stderr, "ERROR: orientation-bits rank cannot use multiset rank options\n");
                exit(1);
            }
        } else if (rank_groups_buffer[0]) {
            if (rank_symbols[0] || rank_counts_buffer[0]) {
                fprintf(stderr, "ERROR: --rank-groups cannot be combined with --rank-symbols/--rank-counts\n");
                exit(1);
            }
            rank_group_count = parse_rank_groups(rank_groups_buffer, rank_groups);
        } else {
            rank_symbol_count = strlen(rank_symbols);
            unsigned int rank_count_count = parse_rank_counts(rank_counts_buffer, rank_counts);
            if (!rank_symbol_count || rank_symbol_count != rank_count_count) {
                fprintf(stderr, "ERROR: ranked mode requires matching symbols and counts\n");
                exit(1);
            }
            rank_group_count = 1;
            rank_groups[0].offset = 0;
            rank_groups[0].symbol_count = rank_symbol_count;
            memcpy(rank_groups[0].symbols, rank_symbols, rank_symbol_count);
            memcpy(rank_groups[0].counts, rank_counts, rank_symbol_count * sizeof(unsigned int));
            for (unsigned int i = 0; i < rank_symbol_count; i++) {
                rank_groups[0].length += rank_counts[i];
            }
            rank_groups[0].universe = rank_universe;
        }
        if (!ranked_input[0] || (!ranked_no_workq && !ranked_output[0]) ||
                (configured_rank_type != RANK_EDGE_PAIRING_EVEN &&
                 configured_rank_type != RANK_ORIENTATION_BITS && !rank_group_count) || !rank_universe) {
            fprintf(stderr, "ERROR: ranked mode requires input/output, symbols, counts and universe\n");
            exit(1);
        }
        if (!rank_groups_buffer[0]) {
            for (unsigned int i = 1; i < rank_symbol_count; i++) {
                if ((unsigned char) rank_symbols[i - 1] >= (unsigned char) rank_symbols[i]) {
                    fprintf(stderr, "ERROR: --rank-symbols must be unique and sorted\n");
                    exit(1);
                }
            }
        }
        if (configured_rank_type == RANK_CENTER_SYMMETRY_444) {
            if ((cube_size != 4 && cube_size != 6) || rank_group_count != 1 ||
                    rank_groups[0].length != CENTER_SYMMETRY_STICKERS_444 ||
                    strcmp((const char *) rank_groups[0].symbols, "FLU") ||
                    rank_groups[0].counts[0] != 8 ||
                    rank_groups[0].counts[1] != 8 ||
                    rank_groups[0].counts[2] != 8) {
                fprintf(stderr, "ERROR: center-symmetry-444 requires a 4x4x4 or 6x6x6 FLU 8,8,8 rank group\n");
                exit(1);
            }
            init_center_symmetry_444();
        }
        if (ranked_depth > 254) {
            fprintf(stderr, "ERROR: ranked depth must be <= 254\n");
            exit(1);
        }
        process_ranked_workq(
            ranked_input, ranked_output, ranked_cost, start, end, (unsigned char) ranked_depth,
            cube_size, moves, moves_index, squares, square_count,
            pairing_partners, pairing_partner_count, wing_flip_masks, wing_flip_mask_count,
            wing_partner_flip_mask,
            configured_rank_type,
            rank_groups, rank_group_count,
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

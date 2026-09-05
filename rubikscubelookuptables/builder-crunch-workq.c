
#include <ctype.h>
#include <locale.h>
#include <math.h>
#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "ida_search_core.h"

// If by some miracle we ever start building lookup-tables deeper than 20 moves
// then we will need to increase this constant
#define MAX_MOVE_LENGTH 20

// add 1 for the leading "x"
// add 294 for a 7x7x7 cube (7 * 7 * 6)
// add 1 for the ":" delimiter
// add (MAX_MOVE_STR_SIZE * MAX_MOVE_LENGTH) or 100
// add 1 for the newline
// add 1 for the '\0'
// That brings us to 398
// add 2 to make evenly divisble by 8
#define MAX_LINE_LENGTH 400

// The workq lines we read are padded out to --linewidth, which get_workq_line_length()
// in buildercore.py caps at 512 before adding one for the newline. We build our output
// lines in the same buffer, so it has to hold MAX_LINE_LENGTH as well.
#define MAX_WORKQ_LINE_LENGTH 1024

#define BATCH_SIZE 2000000

#define MAX_FILENAME_SIZE 128
#define MAX_COMPACT_SQUARES 255
#define MAX_SQUARES_ARG 2048


char to_write[BATCH_SIZE][MAX_LINE_LENGTH];

// deduplicate_to_write_buffer() sorts these pointers into to_write instead of moving the
// rows around, which makes every swap 8 bytes instead of a couple hundred
char *to_write_ptr[BATCH_SIZE];

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
    char to_write[][MAX_LINE_LENGTH],
    char *to_write_dedup,
    unsigned int array_size,
    unsigned int to_write_count)
{
    unsigned int line_length = 0;
    char *to_write_dedup_ptr = to_write_dedup;

    // quicksort the contents of to_write
    for (unsigned int i = 0; i < to_write_count; i++) {
        to_write_ptr[i] = to_write[i];
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
    char to_write[][MAX_LINE_LENGTH],
    char *to_write_dedup,
    unsigned int array_size,
    unsigned int to_write_count,
    char *outputfile,
    unsigned int file_count)
{
    char tmp_outputfile[MAX_FILENAME_SIZE];
    FILE *fh_write = NULL;
    size_t dedup_length = deduplicate_to_write_buffer(to_write, to_write_dedup, array_size, to_write_count);

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
    size_t BUFFER_SIZE = (size_t) MAX_LINE_LENGTH * BATCH_SIZE;
    unsigned int MEGABYTE = 1024 * 1024;
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
    to_write_dedup = malloc(BUFFER_SIZE);

    if (to_write_dedup == NULL) {
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

    LOG("read %dx%dx%d inputfile %s from line %d to %d, MAX_LINE_LENGTH %d, BUFFER_SIZE %d MB\n",
        cube_size, cube_size, cube_size,
        inputfile, start, end, MAX_LINE_LENGTH, (BUFFER_SIZE * 2)/ MEGABYTE);

    for (unsigned int line_number = start; line_number <= end; line_number++) {
        read_result = fread(line, linewidth, 1, fh_read);

        if (!read_result) {
            printf("ERROR: process_workq read for line %d failed for %s\n", line_number, inputfile);
            exit(1);
        }

        strstrip(line);
        line_length = strlen(line);

        // we append a "\n" and a "\0" to every line we buffer, so we need room for both
        if (line_length + 2 > MAX_LINE_LENGTH) {
            printf("ERROR: line %d is %d bytes, max supported is %d bytes\n", line_number, line_length, MAX_LINE_LENGTH - 2);
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
            memcpy(to_write[to_write_count], line, strlen(line) + 1);
            to_write_count++;

            if (to_write_count == BATCH_SIZE) {
                file_count = write_to_write_buffer(
                    to_write, to_write_dedup, array_size, to_write_count, outputfile, file_count);
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
            memcpy(to_write[to_write_count], line, strlen(line) + 1);
            to_write_count++;

            if (to_write_count == BATCH_SIZE) {
                file_count = write_to_write_buffer(
                    to_write, to_write_dedup, array_size, to_write_count, outputfile, file_count);
                to_write_count = 0;
            }
        }
    }

    if (to_write_count) {
        file_count = write_to_write_buffer(
            to_write, to_write_dedup, array_size, to_write_count, outputfile, file_count);
        to_write_count = 0;
    }

    fclose(fh_read);
    free(to_write_dedup);

    if (perm) {
        free(perm);
    }
}


int
main (int argc, char *argv[])
{
    unsigned int linewidth = 0;
    unsigned int start = 0;
    unsigned int end = 0;
    unsigned char cube_size = 0;
    char inputfile[MAX_FILENAME_SIZE];
    char outputfile[MAX_FILENAME_SIZE];
    char moves_buffer[512];
    char squares_buffer[MAX_SQUARES_ARG];
    unsigned int squares[MAX_COMPACT_SQUARES];
    unsigned int square_count = 0;
    memset(inputfile, '\0', sizeof(char) * MAX_FILENAME_SIZE);
    memset(outputfile, '\0', sizeof(char) * MAX_FILENAME_SIZE);
    memset(squares_buffer, '\0', sizeof(squares_buffer));

    for (int i = 1; i < argc; i++) {
        if (strmatch(argv[i], "--inputfile")) {
            i++;
            strcpy(inputfile, argv[i]);

        } else if (strmatch(argv[i], "--outputfile")) {
            i++;
            strcpy(outputfile, argv[i]);

        } else if (strmatch(argv[i], "--start")) {
            i++;
            start = atoi(argv[i]);

        } else if (strmatch(argv[i], "--end")) {
            i++;
            end = atoi(argv[i]);

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

    if (linewidth == 0) {
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

    process_workq(inputfile, outputfile, linewidth, start, end, cube_size, moves, moves_index, squares, square_count);
}


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
    char A[][MAX_LINE_LENGTH],
    unsigned int len)
{
    if (len < 2) {
        return;
    }

    char pivot[MAX_LINE_LENGTH]; // pivot is comparator
    strcpy(pivot, A[len / 2]);

    int i = 0;
    int j = len - 1;
    char temp[MAX_LINE_LENGTH];

    while (1) {
        // find first to the left of pivot that is larger than pivot
        while (strcmp(A[i], pivot) < 0) {
            ++i;
        }

        // find first to the right of pivot that is smaller than pivot
        while (strcmp(A[j], pivot) > 0) {
            --j;
        }

        // Swap if i (larger than pivot) is left of j (smaller than pivot)
        if (i < j) {
            strcpy(temp, A[i]);
            strcpy(A[i], A[j]);
            strcpy(A[j], temp);
        } else {
            break;
        }

        ++i;
        --j;
    }

    quicksort(A, i); // left half
    quicksort(A + i, len - i); // right half
}

void
deduplicate_to_write_buffer(
    char to_write[][MAX_LINE_LENGTH],
    char *to_write_dedup,
    unsigned int BUFFER_SIZE,
    unsigned int array_size,
    unsigned int to_write_count)
{
    unsigned int line_length = 0;
    char *to_write_dedup_ptr = to_write_dedup;

    memset(to_write_dedup, '\0', BUFFER_SIZE);

    // quicksort the contents of to_write
    quicksort(to_write, to_write_count);

    line_length = strlen(to_write[0]);
    memcpy(to_write_dedup_ptr, to_write[0], line_length);
    to_write_dedup_ptr += line_length;

    if (to_write_count == 1) {
        return;
    }

    // loop over to_write and write all unique states to to_write_dedup
    for (unsigned int i = 1; i < to_write_count; i++) {

        if (memcmp(to_write[i], to_write[i-1], array_size) != 0) {
            line_length = strlen(to_write[i]);
            memcpy(to_write_dedup_ptr, to_write[i], line_length);
            // printf("KEEP %s", to_write[i]);
            to_write_dedup_ptr += line_length;
        // } else {
        //     printf("SKIP %s", to_write[i]);
        }
    }
}


void
process_workq(
    char *inputfile,
    char *outputfile,
    unsigned int linewidth,
    unsigned int start,
    unsigned int end,
    unsigned int cube_size,
    move_type moves[MOVE_MAX],
    unsigned int moves_count)
{
    FILE *fh_read = NULL;
    FILE *fh_write = NULL;
    char *move_ptr = NULL;
    char *prev_move_ptr = NULL;

    int steps_to_scramble_length = 0;
    unsigned int BATCH_SIZE = 20000;
    unsigned int array_size = (cube_size * cube_size * 6) + 1; // add 1 for the leading "x"
    unsigned int BUFFER_SIZE = MAX_LINE_LENGTH * BATCH_SIZE;
    unsigned int MEGABYTE = 1024 * 1024;
    unsigned int line_length = 0;
    unsigned int sizeof_array_size = sizeof(char) * array_size;
    unsigned int to_write_count = 0;

    unsigned char cube[array_size];
    unsigned char cube_tmp[array_size];
    unsigned char line[512];
    unsigned char move_index = 0;
    unsigned char move_str_length = 0;
    unsigned char read_result = 0;
    unsigned char steps_to_scramble[MAX_MOVE_STR_SIZE * MAX_MOVE_LENGTH];
    char to_write[BATCH_SIZE][MAX_LINE_LENGTH];
    unsigned char *to_write_dedup = NULL;

    char space_delim[] = " ";

    move_type move = MOVE_NONE;
    move_type prev_move = MOVE_NONE;
    to_write_dedup = malloc(sizeof(char) * BUFFER_SIZE);

    memset(line, '\0', sizeof(char) * 512);
    memset(to_write, '\0',  BUFFER_SIZE);
    memset(cube, 0, sizeof_array_size);
    memset(cube_tmp, 0, sizeof_array_size);
    fh_read = fopen(inputfile, "r");
    fh_write = fopen(outputfile, "w");

    if (fh_read == NULL) {
        printf("ERROR: process_workq could not open %s\n", inputfile);
        exit(1);
    }

    fseek(fh_read, start * linewidth, SEEK_SET);
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

        if (line_length > MAX_LINE_LENGTH) {
            printf("ERROR: line %d is %d bytes, max supported is %d bytes\n", line_number, line_length, MAX_LINE_LENGTH);
            printf("%s\n", line);
            exit(1);
        }

        memcpy(cube, line, array_size);

        // what was the last move used to get to this state?
        prev_move = MOVE_NONE;
        steps_to_scramble_length = line_length - array_size - 1;

        if (steps_to_scramble_length > 0) {
            memset(steps_to_scramble, '\0', sizeof(char) * MAX_MOVE_STR_SIZE * MAX_MOVE_LENGTH);
            memcpy(steps_to_scramble, &line[array_size+1], steps_to_scramble_length);
            move_ptr = strtok(steps_to_scramble, space_delim);

            // printf("%s\n", line);
            // printf("line_length %d\n", line_length);
            // printf("steps_to_scramble %s\n", steps_to_scramble);
            // printf("steps_to_scramble_length %d\n", steps_to_scramble_length);
            // printf("move_ptr %s\n", move_ptr);
            prev_move_ptr = move_ptr;

            while (move_ptr != NULL) {
                move_ptr = strtok(NULL, space_delim);

                if (move_ptr != NULL) {
                    prev_move_ptr = move_ptr;
                }
            }

            prev_move = str2move(prev_move_ptr);

        } else if (steps_to_scramble_length < 0) {
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
            memcpy(cube_tmp, cube, sizeof_array_size);
            rotate_555(cube_tmp, cube, array_size, move);

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

            // copy the "line" we just contructed to our to_write buffer
            memcpy(to_write[to_write_count], line, strlen(line));
            to_write_count++;

            if (to_write_count == BATCH_SIZE) {
                deduplicate_to_write_buffer(to_write, to_write_dedup, BUFFER_SIZE, array_size, to_write_count);
                fputs(to_write_dedup, fh_write);
                memset(to_write, '\0', BUFFER_SIZE);
                to_write_count = 0;
            }
        }
    }

    if (to_write_count) {
        deduplicate_to_write_buffer(to_write, to_write_dedup, BUFFER_SIZE, array_size, to_write_count);
        fputs(to_write_dedup, fh_write);
        memset(to_write, '\0', BUFFER_SIZE);
        to_write_count = 0;
    }
}


int
main (int argc, char *argv[])
{
    unsigned int linewidth = 0;
    unsigned int start = 0;
    unsigned int end = 0;
    unsigned int cube_size = 0;
    unsigned int MAX_FILENAME_SIZE = 128;
    char inputfile[MAX_FILENAME_SIZE];
    char outputfile[MAX_FILENAME_SIZE];
    char moves_buffer[512];
    memset(inputfile, 0, sizeof(char) * MAX_FILENAME_SIZE);
    memset(outputfile, 0, sizeof(char) * MAX_FILENAME_SIZE);

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

    process_workq(inputfile, outputfile, linewidth, start, end, cube_size, moves, moves_index);
}

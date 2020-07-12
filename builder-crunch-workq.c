
#include <ctype.h>
#include <locale.h>
#include <math.h>
#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <sys/resource.h>
#include <sys/time.h>
#include "ida_search_core.h"



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
    unsigned int array_size = (cube_size * cube_size * 6) + 1;
    unsigned int line_length = 0;
    unsigned int move_index = 0;
    unsigned int move_str_length = 0;
    unsigned int MAX_LINE_WIDTH = 512;
    unsigned char line[MAX_LINE_WIDTH];
    unsigned char steps_to_scramble[MAX_MOVE_STR_SIZE * 24];
    unsigned char cube[array_size];
    unsigned char cube_tmp[array_size];
    unsigned int sizeof_array_size = sizeof(char) * array_size;
    unsigned int to_write_count = 0;
    int steps_to_scramble_length = 0;
    unsigned int BATCH_SIZE = 100000;
    unsigned char read_result = 0;
    unsigned char *to_write;
    to_write = malloc(sizeof(char) * BATCH_SIZE * MAX_LINE_WIDTH);
    unsigned char *to_write_ptr = to_write;
    char space_delim[] = " ";
    move_type move = MOVE_NONE;
    move_type prev_move = MOVE_NONE;
    char *move_ptr = NULL;
    char *prev_move_ptr = NULL;

    memset(line, '\0', sizeof(char) * MAX_LINE_WIDTH);
    memset(to_write, '\0',  sizeof(char) * MAX_LINE_WIDTH * BATCH_SIZE);
    memset(cube, 0, sizeof_array_size);
    memset(cube_tmp, 0, sizeof_array_size);
    fh_read = fopen(inputfile, "r");
    fh_write = fopen(outputfile, "w");

    if (fh_read == NULL) {
        printf("ERROR: process_workq could not open %s\n", inputfile);
        exit(1);
    }

    fseek(fh_read, start * linewidth, SEEK_SET);
    LOG("read %dx%dx%d inputfile %s from %d to %d, linewidth %d, array_size %d\n",
        cube_size, cube_size, cube_size,
        inputfile, start, end, linewidth, array_size);

    for (unsigned int line_number = start; line_number <= end; line_number++) {
        read_result = fread(line, linewidth, 1, fh_read);

        if (!read_result) {
            printf("ERROR: process_workq read for line %d failed for %s\n", line_number, inputfile);
            exit(1);
        }

        strstrip(line);
        line_length = strlen(line);

        if (line_length > MAX_LINE_WIDTH) {
            printf("ERROR: line %d is %d bytes, max supported is %d bytes\n", line_number, line_length, MAX_LINE_WIDTH);
            printf("%s\n", line);
            exit(1);
        }

        memcpy(cube, line, array_size);

        // what was the last move used to get to this state?
        prev_move = MOVE_NONE;
        steps_to_scramble_length = line_length - array_size - 1;

        if (steps_to_scramble_length > 0) {
            memset(steps_to_scramble, '\0', sizeof(char) * MAX_MOVE_STR_SIZE * 24);
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
            memcpy(to_write_ptr, line, strlen(line));
            to_write_ptr += strlen(line);
            to_write_count++;

            if (to_write_count >= BATCH_SIZE) {
                fputs(to_write, fh_write);
                memset(to_write, '\0',  sizeof(char) * MAX_LINE_WIDTH * BATCH_SIZE);
                to_write_count = 0;
                to_write_ptr = to_write;
            }
        }
    }

    if (to_write_count) {
        fputs(to_write, fh_write);
        memset(to_write, '\0',  sizeof(char) * MAX_LINE_WIDTH * BATCH_SIZE);
        to_write_count = 0;
        to_write_ptr = to_write;
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
            printf("\nida_search --kociemba KOCIEMBA_STRING --type 5x5x5-LR-centers-stage\n\n");
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

    // Print the maximum resident set size used (in MB).
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    printf("Memory usage: %lu MB\n", (unsigned long) r_usage.ru_maxrss / (1024 * 1024));
}

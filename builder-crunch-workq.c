
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
    *(end + 1) = '\n';
    *(end + 2) = '\0';

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
    move_type *moves,
    unsigned int move_count)
{
    FILE *fh_read = NULL;
    FILE *fh_write = NULL;
    unsigned int array_size = (cube_size * cube_size * 6) + 1;
    unsigned int line_length = 0;
    unsigned int move_index = 0;
    unsigned int move_str_length = 0;
    unsigned int MAX_LINE_WIDTH = 512;
    unsigned char line[MAX_LINE_WIDTH];
    unsigned char cube[array_size];
    unsigned char cube_tmp[array_size];
    unsigned int sizeof_array_size = sizeof(char) * array_size;
    unsigned int to_write_count = 0;
    unsigned int BATCH_SIZE = 100000;
    unsigned char *to_write;
    to_write = malloc(sizeof(char) * BATCH_SIZE * MAX_LINE_WIDTH);
    unsigned char *to_write_ptr = to_write;

    move_type move;

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
        if (fread(line, linewidth, 1, fh_read)) {
            strstrip(line);
            line_length = strlen(line);
            memcpy(cube, line, array_size);
            // print_cube(cube, cube_size);

            // dwalton
            for (move_index = 0; move_index < move_count; move_index++) {
                memcpy(cube_tmp, cube, sizeof_array_size);
                move = moves[move_index];
                rotate_555(cube_tmp, cube, array_size, move);

                // if nothing changed, do not bother writing this result to the file
                if (memcmp(cube_tmp, cube, sizeof_array_size) == 0) {
                    continue;
                }

                // printf("%s\n", move2str[move]);
                // print_cube(cube_tmp, cube_size);
                // printf("\n\n");
                memcpy(line, cube_tmp, sizeof_array_size);
                move_str_length = strlen(move2str[move]);

                if (line[line_length-2] == ':') {
                    memcpy(&line[line_length-1], move2str[move], move_str_length);
                    line[line_length-1 + move_str_length] = '\n';
                    line[line_length-1 + move_str_length + 1] = '\0';
                } else {
                    line[line_length-1] = ' ';
                    memcpy(&line[line_length], move2str[move], move_str_length);
                    line[line_length + move_str_length] = '\n';
                    line[line_length + move_str_length + 1] = '\0';
                }

                memcpy(to_write_ptr, line, strlen(line));
                to_write_ptr += strlen(line);
                to_write_count++;

                if (to_write_count >= BATCH_SIZE) {
                    fputs(to_write, fh_write);
                    memset(to_write, '\0',  sizeof(char) * MAX_LINE_WIDTH * BATCH_SIZE);
                    to_write_count = 0;
                    to_write_ptr = to_write;
                }
                // fputs(line, fh_write);
            }

        } else {
            printf("ERROR: process_workq read failed for %s\n", inputfile);
            exit(1);
        }
    }

    if (to_write_count) {
        fputs(to_write, fh_write);
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

    // init moves list
    unsigned int moves_index = 0;
    move_type moves[64];
    memset(moves, MOVE_MAX, sizeof(move_type) * 64);

    char delim[] = " ";
    char *move_ptr = strtok(moves_buffer, delim);

	while (move_ptr != NULL) {
		// printf("%s\n", move_ptr);

        if (strmatch(move_ptr, "U")) {
            moves[moves_index] = U;
        } else if (strmatch(move_ptr, "U'")) {
            moves[moves_index] = U_PRIME;
        } else if (strmatch(move_ptr, "U2")) {
            moves[moves_index] = U2;
        } else if (strmatch(move_ptr, "Uw")) {
            moves[moves_index] = Uw;
        } else if (strmatch(move_ptr, "Uw'")) {
            moves[moves_index] = Uw_PRIME;
        } else if (strmatch(move_ptr, "Uw2")) {
            moves[moves_index] = Uw2;
        } else if (strmatch(move_ptr, "3Uw")) {
            moves[moves_index] = threeUw;
        } else if (strmatch(move_ptr, "3Uw'")) {
            moves[moves_index] = threeUw_PRIME;
        } else if (strmatch(move_ptr, "3Uw2")) {
            moves[moves_index] = threeUw2;

        } else if (strmatch(move_ptr, "L")) {
            moves[moves_index] = L;
        } else if (strmatch(move_ptr, "L'")) {
            moves[moves_index] = L_PRIME;
        } else if (strmatch(move_ptr, "L2")) {
            moves[moves_index] = L2;
        } else if (strmatch(move_ptr, "Lw")) {
            moves[moves_index] = Lw;
        } else if (strmatch(move_ptr, "Lw'")) {
            moves[moves_index] = Lw_PRIME;
        } else if (strmatch(move_ptr, "Lw2")) {
            moves[moves_index] = Lw2;
        } else if (strmatch(move_ptr, "3Lw")) {
            moves[moves_index] = threeLw;
        } else if (strmatch(move_ptr, "3Lw'")) {
            moves[moves_index] = threeLw_PRIME;
        } else if (strmatch(move_ptr, "3Lw2")) {
            moves[moves_index] = threeLw2;

        } else if (strmatch(move_ptr, "F")) {
            moves[moves_index] = F;
        } else if (strmatch(move_ptr, "F'")) {
            moves[moves_index] = F_PRIME;
        } else if (strmatch(move_ptr, "F2")) {
            moves[moves_index] = F2;
        } else if (strmatch(move_ptr, "Fw")) {
            moves[moves_index] = Fw;
        } else if (strmatch(move_ptr, "Fw'")) {
            moves[moves_index] = Fw_PRIME;
        } else if (strmatch(move_ptr, "Fw2")) {
            moves[moves_index] = Fw2;
        } else if (strmatch(move_ptr, "3Fw")) {
            moves[moves_index] = threeFw;
        } else if (strmatch(move_ptr, "3Fw'")) {
            moves[moves_index] = threeFw_PRIME;
        } else if (strmatch(move_ptr, "3Fw2")) {
            moves[moves_index] = threeFw2;

        } else if (strmatch(move_ptr, "R")) {
            moves[moves_index] = R;
        } else if (strmatch(move_ptr, "R'")) {
            moves[moves_index] = R_PRIME;
        } else if (strmatch(move_ptr, "R2")) {
            moves[moves_index] = R2;
        } else if (strmatch(move_ptr, "Rw")) {
            moves[moves_index] = Rw;
        } else if (strmatch(move_ptr, "Rw'")) {
            moves[moves_index] = Rw_PRIME;
        } else if (strmatch(move_ptr, "Rw2")) {
            moves[moves_index] = Rw2;
        } else if (strmatch(move_ptr, "3Rw")) {
            moves[moves_index] = threeRw;
        } else if (strmatch(move_ptr, "3Rw'")) {
            moves[moves_index] = threeRw_PRIME;
        } else if (strmatch(move_ptr, "3Rw2")) {
            moves[moves_index] = threeRw2;

        } else if (strmatch(move_ptr, "B")) {
            moves[moves_index] = B;
        } else if (strmatch(move_ptr, "B'")) {
            moves[moves_index] = B_PRIME;
        } else if (strmatch(move_ptr, "B2")) {
            moves[moves_index] = B2;
        } else if (strmatch(move_ptr, "Bw")) {
            moves[moves_index] = Bw;
        } else if (strmatch(move_ptr, "Bw'")) {
            moves[moves_index] = Bw_PRIME;
        } else if (strmatch(move_ptr, "Bw2")) {
            moves[moves_index] = Bw2;
        } else if (strmatch(move_ptr, "3Bw")) {
            moves[moves_index] = threeBw;
        } else if (strmatch(move_ptr, "3Bw'")) {
            moves[moves_index] = threeBw_PRIME;
        } else if (strmatch(move_ptr, "3Bw2")) {
            moves[moves_index] = threeBw2;

        } else if (strmatch(move_ptr, "D")) {
            moves[moves_index] = D;
        } else if (strmatch(move_ptr, "D'")) {
            moves[moves_index] = D_PRIME;
        } else if (strmatch(move_ptr, "D2")) {
            moves[moves_index] = D2;
        } else if (strmatch(move_ptr, "Dw")) {
            moves[moves_index] = Dw;
        } else if (strmatch(move_ptr, "Dw'")) {
            moves[moves_index] = Dw_PRIME;
        } else if (strmatch(move_ptr, "Dw2")) {
            moves[moves_index] = Dw2;
        } else if (strmatch(move_ptr, "3Dw")) {
            moves[moves_index] = threeDw;
        } else if (strmatch(move_ptr, "3Dw'")) {
            moves[moves_index] = threeDw_PRIME;
        } else if (strmatch(move_ptr, "3Dw2")) {
            moves[moves_index] = threeDw2;

        } else {
            printf("ERROR: invalid move %s\n", move_ptr);
            exit(1);
        }

		move_ptr = strtok(NULL, delim);
        moves_index++;
	}

    process_workq(inputfile, outputfile, linewidth, start, end, cube_size, moves, moves_index);

    // Print the maximum resident set size used (in MB).
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    printf("Memory usage: %lu MB\n", (unsigned long) r_usage.ru_maxrss / (1024 * 1024));
}

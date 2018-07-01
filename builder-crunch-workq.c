
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "rotate_char_xxx.h"

/*
 * ./builder-crunch-workq 4x4x4 tmp/4x4x4-UD-centers-stage.workq.txt 198 0 330445 tmp/4x4x4-UD-centers-stage.workq.txt.core-0
 *
 *  gcc -O -o builder-crunch-workq builder-crunch-workq.c rotate_char_xxx.c
 */

int
cmpstr(const void* a, const void* b) {
    const char* aa = (const char*)a;
    const char* bb = (const char*)b;
    return strcmp(aa, bb);
}

char *
get_last_move_ptr(char *str)
{
    char *end;
    end = str + strlen(str) - 1;

    while (end > str) {
        if (*end == ' ') {
            return end + 1;
        }
        end--;
    }

    return str;
}

void
trim_trailing_spaces(char *str)
{
    char *end;

    // Trim trailing space
    end = str + strlen(str) - 1;

    while (end > str && isspace((unsigned char)*end)) {
      end--;
    }

    // Write new null terminator character
    end[1] = '\0';
}


int
main (int argc, char *argv[])
{
    // open a read input file
    // open a write output file
    // For every line in the input file load the cube and apply the move, then
    // write the resulting cube to the output file
    FILE *fh_read = NULL;
    FILE *fh_write = NULL;
    char input_filename[100];
    char output_filename_base[100];
    char output_filename[100];
    int output_filename_index = 0;
    long int start_line = 0;
    long int end_line = 0;
    long int line_width = 0;
    int cube_size = 0;
    int current_line = 0;
    int cube_state_len = 0;
    char *cube_state_ptr = NULL;
    char *moves_ptr = NULL;
    char *last_move_ptr = NULL;

    memset(input_filename, 0, sizeof(char) * 100);
    memset(output_filename_base, 0, sizeof(char) * 100);
    memset(output_filename, 0, sizeof(char) * 100);

    for (int i = 1; i < argc; i++) {
        if (strmatch(argv[i], "-i") || strmatch(argv[i], "--input")) {
            i++;
            strcpy(input_filename, argv[i]);

        } else if (strmatch(argv[i], "-o") || strmatch(argv[i], "--output")) {
            i++;
            strcpy(output_filename_base, argv[i]);

        } else if (strmatch(argv[i], "--size")) {
            i++;
            cube_size = atoi(argv[i]);

        } else if (strmatch(argv[i], "--start")) {
            i++;
            start_line = atol(argv[i]);

        } else if (strmatch(argv[i], "--end")) {
            i++;
            end_line = atol(argv[i]);

        } else if (strmatch(argv[i], "--linewidth")) {
            i++;
            line_width = atoi(argv[i]);
        }
    }

    if (cube_size < 2 || cube_size > 7) {
        printf("ERROR: --size must be 2, 3, 4, 5, 6, or 7\n");
        exit(1);
    }

    if (start_line < 0) {
        printf("ERROR: --start cannot be negative\n");
        exit(1);
    }

    if (end_line <= 0) {
        printf("ERROR: --end must be a positive number\n");
        exit(1);
    }

    if (start_line > end_line) {
        printf("ERROR: --start must be <= --end\n");
        exit(1);
    }

    if (!line_width) {
        printf("ERROR: --linewidth cannot be 0\n");
        exit(1);
    }

    // 1 for the leading x and 1 to terminate with a NULL
    int array_size = (cube_size * cube_size * 6) + 2;
    char cube[array_size];
    char cube_tmp[array_size];
    memset(cube, 0, sizeof(char) * array_size);
    memset(cube_tmp, 0, sizeof(char) * array_size);
    cube[array_size] = '\0';
    cube_tmp[array_size] = '\0';
    int MAX_LINE_WIDTH = 512;
    char line_buffer[MAX_LINE_WIDTH];

    int WRITE_BATCH_SIZE = 1000000;
    int write_batch_index = 0;
    int write_buffer_size = (WRITE_BATCH_SIZE * MAX_LINE_WIDTH) * sizeof(char);
    char *write_buffer = malloc(write_buffer_size);
    memset(write_buffer, 0, write_buffer_size);
    printf("write_buffer is %d bytes\n", write_buffer_size);

    fh_read = fopen(input_filename, "r");
    if (fh_read == NULL) {
        printf("ERROR: could not open %s\n", input_filename);
        exit(1);
    }

    // seek to our starting point so that we do not waste time looping over
    // a bunch of lines we do not care about
    long int seek_position = start_line * (line_width + 1);
    fseek(fh_read, seek_position, SEEK_SET);
    current_line = start_line;
    memset(line_buffer, 0, MAX_LINE_WIDTH);
    //printf("seek to %lu\n", seek_position);

    while (fgets(line_buffer, MAX_LINE_WIDTH, fh_read) != NULL) {

        if (current_line > end_line) {
            break;
        }

        // chop the newline and trailing whitespace
        line_buffer[strlen(line_buffer)-1] = '\0';
        trim_trailing_spaces(line_buffer);
        //printf("LINE:%s\n", line_buffer);

        // The first token is the cube state to load
        cube_state_ptr = strtok(line_buffer, ":");

        if (cube_state_len == 0) {
            cube_state_len = strlen(cube_state_ptr);
        }

        memcpy(cube, cube_state_ptr, cube_state_len * sizeof(char));

        // The second token contains the list of moves, we need to
        // extract the last move and apply it
        moves_ptr = strtok(NULL, ":");

        last_move_ptr = get_last_move_ptr(moves_ptr);
        //printf("cube_state is %lu bytes\n", strlen(cube_state_ptr));
        //printf("array_size %d\n", array_size);
        //printf("cube_state %s\n", cube_state_ptr);
        //printf("last_move %s\n", last_move_ptr);

        switch (cube_size) {
        case 2:
            rotate_222(cube, cube_tmp, array_size, last_move_ptr);
            break;
        case 3:
            rotate_333(cube, cube_tmp, array_size, last_move_ptr);
            break;
        case 4:
            rotate_444(cube, cube_tmp, array_size, last_move_ptr);
            break;
        case 5:
            rotate_555(cube, cube_tmp, array_size, last_move_ptr);
            break;
        case 6:
            rotate_666(cube, cube_tmp, array_size, last_move_ptr);
            break;
        case 7:
            rotate_777(cube, cube_tmp, array_size, last_move_ptr);
            break;
        default:
            printf("Implement rotate_xxx() for cube size %d", cube_size);
            exit(1);
        }

        sprintf(&write_buffer[write_batch_index * MAX_LINE_WIDTH], "%s:%s\n", (char *)cube, moves_ptr);
        write_batch_index++;
        current_line++;

        // Write what we have then nuke the write_buffer
        if (write_batch_index == WRITE_BATCH_SIZE) {
            sprintf(output_filename, "%s.%04d", output_filename_base, output_filename_index);
            fh_write = fopen(output_filename, "w");

            if (fh_write == NULL) {
                printf("ERROR: could not open %s\n", output_filename);
                fclose(fh_read);
                exit(1);
            }

            qsort(write_buffer, write_batch_index, sizeof(char) * MAX_LINE_WIDTH, cmpstr);

            for (int i = 0; i < write_batch_index; i++) {
                fprintf(fh_write, "%s", &write_buffer[i * MAX_LINE_WIDTH]);
            }
            fclose(fh_write);
            fh_write = NULL;

            write_batch_index = 0;
            memset(write_buffer, 0, write_buffer_size);
            output_filename_index++;
        }

        memset(line_buffer, 0, MAX_LINE_WIDTH);
    }

    /*
    printf("\n\npre  qsort\n");
    for (int i = 0; i < write_batch_index; i++) {
        printf("write_buffer[%d]: %s", i, write_buffer[i]);
    }
    */

    if (write_batch_index > 0) {
        sprintf(output_filename, "%s.%04d", output_filename_base, output_filename_index);
        fh_write = fopen(output_filename, "w");

        if (fh_write == NULL) {
            printf("ERROR: could not open %s\n", output_filename);
            fclose(fh_read);
            exit(1);
        }

        qsort(write_buffer, write_batch_index, sizeof(char) * MAX_LINE_WIDTH, cmpstr);

        for (int i = 0; i < write_batch_index; i++) {
            fprintf(fh_write, "%s", &write_buffer[i * MAX_LINE_WIDTH]);
        }
        fclose(fh_write);
        fh_write = NULL;

        write_batch_index = 0;
        memset(write_buffer, 0, write_buffer_size);
        output_filename_index++;
    }

    free(write_buffer);
    write_buffer = NULL;
    fclose(fh_read);
}

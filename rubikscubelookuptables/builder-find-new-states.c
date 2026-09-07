
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Given the lookup-table we have built so far and the sorted results of the latest
 * round of builder-crunch-workq, find the cube states in the results that are not
 * yet in the lookup-table. Both files are sorted by cube state so we can do this in
 * a single merge walk.
 *
 * We write two files:
 * - the new states with the moves needed to solve them, to be merged into the lookup-table
 * - the workq for the next depth, with the moves that scrambled each state
 *
 * The only difference between the two is the direction of the move sequence, so doing
 * them together saves reading the new states back off disk and reversing them twice.
 *
 * The number of new states is written to stdout.
 */

// The lines we read are unpadded, so the longest is a 7x7x7 state of 295 characters
// plus the ":" and 20 moves of up to 5 characters. The padded workq lines we write go
// in a buffer twice this size, and get_workq_line_length() tops out at 512.
#define MAX_LINE_LENGTH 1024
#define MAX_MOVES 32
#define IO_BUFFER_SIZE (4 * 1024 * 1024)


/*
 * Reverse a sequence of moves and invert each one, so that the moves that scrambled
 * a cube become the moves that solve it.
 *
 *   "Uw2 R F'" -> "F R' Uw2"
 */
unsigned int
reverse_steps(char *steps, unsigned int steps_length, char *result)
{
    char *move_start[MAX_MOVES];
    unsigned int move_length[MAX_MOVES];
    unsigned int move_count = 0;
    unsigned int index = 0;
    char *result_ptr = result;

    while (index < steps_length) {

        // skip whitespace
        while (index < steps_length && steps[index] == ' ') {
            index++;
        }

        if (index >= steps_length) {
            break;
        }

        if (move_count >= MAX_MOVES) {
            fprintf(stderr, "ERROR: more than %d moves in '%.*s'\n", MAX_MOVES, steps_length, steps);
            exit(1);
        }

        move_start[move_count] = &steps[index];

        while (index < steps_length && steps[index] != ' ') {
            index++;
        }

        move_length[move_count] = (unsigned int) (&steps[index] - move_start[move_count]);
        move_count++;
    }

    for (int move_index = move_count - 1; move_index >= 0; move_index--) {
        char *move = move_start[move_index];
        unsigned int length = move_length[move_index];

        if (result_ptr != result) {
            *result_ptr++ = ' ';
        }

        // a half turn is its own inverse, otherwise toggle the "'"
        if (move[length - 1] == '2') {
            memcpy(result_ptr, move, length);
            result_ptr += length;

        } else if (move[length - 1] == '\'') {
            memcpy(result_ptr, move, length - 1);
            result_ptr += length - 1;

        } else {
            memcpy(result_ptr, move, length);
            result_ptr += length;
            *result_ptr++ = '\'';
        }
    }

    return (unsigned int) (result_ptr - result);
}


/*
 * Read one line and strip the trailing newline and any padding
 */
int
read_line(FILE *fh, char *line, unsigned int *line_length, char *filename)
{
    unsigned int length = 0;

    if (fh == NULL || fgets(line, MAX_LINE_LENGTH, fh) == NULL) {
        return 0;
    }

    length = (unsigned int) strlen(line);

    // fgets stops after MAX_LINE_LENGTH - 1 characters. If we filled the buffer without
    // reaching a newline then we only have part of the line, and silently carrying on
    // would shift every state that follows it.
    if (length == MAX_LINE_LENGTH - 1 && line[length - 1] != '\n') {
        fprintf(stderr, "ERROR: %s has a line longer than our %d byte buffer\n", filename, MAX_LINE_LENGTH);
        exit(1);
    }

    while (length && (line[length - 1] == '\n' || line[length - 1] == '\r' || line[length - 1] == ' ')) {
        length--;
    }

    line[length] = '\0';
    *line_length = length;
    return 1;
}


FILE *
open_buffered(char *filename, char *mode, char **buffer)
{
    FILE *fh = fopen(filename, mode);

    if (fh == NULL) {
        return NULL;
    }

    *buffer = malloc(IO_BUFFER_SIZE);

    if (*buffer == NULL) {
        fprintf(stderr, "ERROR: could not allocate an IO buffer for %s\n", filename);
        exit(1);
    }

    setvbuf(fh, *buffer, _IOFBF, IO_BUFFER_SIZE);
    return fh;
}


int
main(int argc, char *argv[])
{
    char *table_filename = NULL;
    char *results_filename = NULL;
    char *new_states_filename = NULL;
    char *workq_filename = NULL;
    unsigned int linewidth = 0;

    char *table_buffer = NULL;
    char *results_buffer = NULL;
    char *new_states_buffer = NULL;
    char *workq_buffer = NULL;

    FILE *fh_table = NULL;
    FILE *fh_results = NULL;
    FILE *fh_new_states = NULL;
    FILE *fh_workq = NULL;

    char line_table[MAX_LINE_LENGTH];
    char line_results[MAX_LINE_LENGTH];
    char out[MAX_LINE_LENGTH * 2];

    unsigned int line_table_length = 0;
    unsigned int line_results_length = 0;
    unsigned int state_width = 0;
    unsigned int steps_offset = 0;
    unsigned long new_states_count = 0;
    unsigned int max_new_states_line_length = 0;
    int have_table = 0;
    int have_results = 0;

    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--table") && i + 1 < argc) {
            table_filename = argv[++i];

        } else if (!strcmp(argv[i], "--results") && i + 1 < argc) {
            results_filename = argv[++i];

        } else if (!strcmp(argv[i], "--new-states") && i + 1 < argc) {
            new_states_filename = argv[++i];

        } else if (!strcmp(argv[i], "--workq") && i + 1 < argc) {
            workq_filename = argv[++i];

        } else if (!strcmp(argv[i], "--linewidth") && i + 1 < argc) {
            linewidth = (unsigned int) atoi(argv[++i]);

        } else if (!strcmp(argv[i], "-h") || !strcmp(argv[i], "--help")) {
            printf("usage: builder-find-new-states --table FILE --results FILE --new-states FILE\n");
            printf("                               [--workq FILE --linewidth N]\n");
            exit(0);

        } else {
            fprintf(stderr, "ERROR: %s is an invalid arg\n", argv[i]);
            exit(1);
        }
    }

    if (table_filename == NULL || results_filename == NULL || new_states_filename == NULL) {
        fprintf(stderr, "ERROR: --table, --results and --new-states are all required\n");
        exit(1);
    }

    if (workq_filename != NULL && linewidth == 0) {
        fprintf(stderr, "ERROR: --workq requires --linewidth\n");
        exit(1);
    }

    if (linewidth + 1 > sizeof(out)) {
        fprintf(stderr, "ERROR: --linewidth %d is larger than our %zu byte buffer\n", linewidth, sizeof(out));
        exit(1);
    }

    fh_results = open_buffered(results_filename, "r", &results_buffer);

    if (fh_results == NULL) {
        fprintf(stderr, "ERROR: could not open %s\n", results_filename);
        exit(1);
    }

    fh_new_states = open_buffered(new_states_filename, "w", &new_states_buffer);

    if (fh_new_states == NULL) {
        fprintf(stderr, "ERROR: could not open %s\n", new_states_filename);
        exit(1);
    }

    if (workq_filename != NULL) {
        fh_workq = open_buffered(workq_filename, "w", &workq_buffer);

        if (fh_workq == NULL) {
            fprintf(stderr, "ERROR: could not open %s\n", workq_filename);
            exit(1);
        }
    }

    have_results = read_line(fh_results, line_results, &line_results_length, results_filename);

    // The state is everything before the ":" and is the same width on every line
    if (have_results) {
        char *colon = strchr(line_results, ':');

        if (colon == NULL) {
            fprintf(stderr, "ERROR: no ':' in %s line '%s'\n", results_filename, line_results);
            exit(1);
        }

        state_width = (unsigned int) (colon - line_results);
        steps_offset = state_width + 1;
    }

    // The lookup-table does not exist yet when we are exploring the first depth
    fh_table = open_buffered(table_filename, "r", &table_buffer);

    if (fh_table != NULL) {
        have_table = read_line(fh_table, line_table, &line_table_length, table_filename);
    }

    while (have_results) {
        int compare = 0;

        if (line_results_length < state_width) {
            fprintf(stderr, "ERROR: %s line '%s' is shorter than the %d character state\n",
                results_filename, line_results, state_width);
            exit(1);
        }

        // Once we run out of lookup-table every remaining state is a new one
        if (!have_table) {
            compare = 1;
        } else if (line_table_length < state_width) {
            fprintf(stderr, "ERROR: %s line '%s' is shorter than the %d character state\n",
                table_filename, line_table, state_width);
            exit(1);
        } else {
            compare = memcmp(line_table, line_results, state_width);
        }

        // this state is already in the lookup-table, we found it via a shorter solution
        if (compare == 0) {
            have_table = read_line(fh_table, line_table, &line_table_length, table_filename);
            have_results = read_line(fh_results, line_results, &line_results_length, results_filename);

        // the lookup-table is behind the results file, catch it up
        } else if (compare < 0) {
            have_table = read_line(fh_table, line_table, &line_table_length, table_filename);

        // this state is not in the lookup-table yet
        } else {
            unsigned int steps_length = 0;
            unsigned int out_length = 0;

            if (line_results_length > steps_offset) {
                steps_length = line_results_length - steps_offset;
            }

            // the moves that solve this state
            memcpy(out, line_results, steps_offset);
            out_length = steps_offset;
            out_length += reverse_steps(&line_results[steps_offset], steps_length, &out[out_length]);
            if (out_length > max_new_states_line_length) {
                max_new_states_line_length = out_length;
            }

            out[out_length++] = '\n';
            fwrite(out, 1, out_length, fh_new_states);

            // the moves that scrambled this state, padded so that builder-crunch-workq
            // can seek straight to any line
            if (fh_workq != NULL) {
                if (line_results_length > linewidth) {
                    fprintf(stderr, "ERROR: line '%s' is %d bytes, --linewidth is %d\n",
                        line_results, line_results_length, linewidth);
                    exit(1);
                }

                memcpy(out, line_results, line_results_length);
                memset(&out[line_results_length], ' ', linewidth - line_results_length);
                out[linewidth] = '\n';
                fwrite(out, 1, linewidth + 1, fh_workq);
            }

            new_states_count++;
            have_results = read_line(fh_results, line_results, &line_results_length, results_filename);
        }
    }

    if (fh_table != NULL) {
        fclose(fh_table);
    }

    fclose(fh_results);
    fclose(fh_new_states);

    if (fh_workq != NULL) {
        fclose(fh_workq);
    }

    // The caller needs the width of the longest line we wrote so that it can pad the
    // finished table without re-reading it via "wc --max-line-length"
    printf("%lu %u\n", new_states_count, max_new_states_line_length);
    return 0;
}

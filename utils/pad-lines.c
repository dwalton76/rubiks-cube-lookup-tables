/*
 * Pad every line of a file out to a uniform width, in place.
 *
 * usage: pad-lines <file> [width]
 *
 * If width is omitted the longest line in the file is measured, matching
 * "wc --max-line-length" (newline not counted, existing spaces are). That is
 * the same default pad-lines.py used when it still wrapped this binary.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define IO_BUFFER (32 * 1024 * 1024)

static int
max_line_length(const char *infile, size_t *width_out)
{
    FILE *fh_read = fopen(infile, "r");
    char *in = NULL;
    size_t leftover = 0;
    size_t max = 0;

    if (fh_read == NULL) {
        fprintf(stderr, "ERROR: could not open %s for reading\n", infile);
        return 1;
    }

    in = malloc(IO_BUFFER);

    if (in == NULL) {
        fprintf(stderr, "ERROR: could not allocate %d bytes\n", IO_BUFFER);
        fclose(fh_read);
        return 1;
    }

    while (1) {
        size_t bytes_read = fread(in + leftover, 1, IO_BUFFER - leftover, fh_read);
        size_t have = leftover + bytes_read;
        size_t consumed = 0;

        if (have == 0) {
            break;
        }

        while (1) {
            char *newline = memchr(in + consumed, '\n', have - consumed);
            size_t line_length = 0;

            if (newline) {
                line_length = (size_t) (newline - (in + consumed));
            } else if (bytes_read == 0) {
                line_length = have - consumed;
            } else {
                break;
            }

            if (line_length > max) {
                max = line_length;
            }

            consumed += line_length;

            if (newline) {
                consumed++;
            }

            if (consumed == have) {
                break;
            }
        }

        leftover = have - consumed;

        if (bytes_read == 0) {
            break;
        }

        if (leftover == IO_BUFFER) {
            fprintf(stderr, "ERROR: a line of %s is longer than %d bytes\n", infile, IO_BUFFER);
            free(in);
            fclose(fh_read);
            return 1;
        }

        memmove(in, in + consumed, leftover);
    }

    fclose(fh_read);
    free(in);
    *width_out = max;
    return 0;
}


static int
pad_file(const char *infile, const char *outfile, size_t width)
{
    FILE *fh_read = fopen(infile, "r");
    FILE *fh_write = NULL;
    char *in = NULL;
    char *out = NULL;
    char *spaces = NULL;
    size_t leftover = 0;
    size_t out_length = 0;
    unsigned long line_number = 0;

    if (fh_read == NULL) {
        fprintf(stderr, "ERROR: could not open %s for reading\n", infile);
        return 1;
    }

    fh_write = fopen(outfile, "w");

    if (fh_write == NULL) {
        fprintf(stderr, "ERROR: could not open %s for writing\n", outfile);
        fclose(fh_read);
        return 1;
    }

    in = malloc(IO_BUFFER);
    out = malloc(IO_BUFFER);
    spaces = malloc(width);

    if (in == NULL || out == NULL || spaces == NULL) {
        fprintf(stderr, "ERROR: could not allocate buffers\n");
        fclose(fh_read);
        fclose(fh_write);
        free(in);
        free(out);
        free(spaces);
        return 1;
    }

    memset(spaces, ' ', width);

    while (1) {
        size_t bytes_read = fread(in + leftover, 1, IO_BUFFER - leftover, fh_read);
        size_t have = leftover + bytes_read;
        size_t consumed = 0;

        if (have == 0) {
            break;
        }

        while (1) {
            char *newline = memchr(in + consumed, '\n', have - consumed);
            size_t line_length = 0;

            if (newline) {
                line_length = (size_t) (newline - (in + consumed));
            } else if (bytes_read == 0) {
                line_length = have - consumed;
            } else {
                break;
            }

            line_number++;

            if (line_length > width) {
                fprintf(stderr, "ERROR: line %lu of %s is %zu bytes, wider than the requested %zu\n",
                    line_number, infile, line_length, width);
                fclose(fh_read);
                fclose(fh_write);
                free(in);
                free(out);
                free(spaces);
                return 1;
            }

            if (out_length + width + 1 > IO_BUFFER) {
                fwrite(out, 1, out_length, fh_write);
                out_length = 0;
            }

            memcpy(out + out_length, in + consumed, line_length);
            out_length += line_length;
            memcpy(out + out_length, spaces, width - line_length);
            out_length += width - line_length;
            out[out_length++] = '\n';

            consumed += line_length;

            if (newline) {
                consumed++;
            }

            if (consumed == have) {
                break;
            }
        }

        leftover = have - consumed;

        if (bytes_read == 0) {
            break;
        }

        if (leftover == IO_BUFFER) {
            fprintf(stderr, "ERROR: line %lu of %s is longer than %d bytes\n",
                line_number + 1, infile, IO_BUFFER);
            fclose(fh_read);
            fclose(fh_write);
            free(in);
            free(out);
            free(spaces);
            return 1;
        }

        memmove(in, in + consumed, leftover);
    }

    if (out_length) {
        fwrite(out, 1, out_length, fh_write);
    }

    if (fclose(fh_write)) {
        fprintf(stderr, "ERROR: could not finish writing %s\n", outfile);
        fclose(fh_read);
        free(in);
        free(out);
        free(spaces);
        return 1;
    }

    fclose(fh_read);
    free(in);
    free(out);
    free(spaces);
    return 0;
}


int
main(int argc, char *argv[])
{
    char *infile = NULL;
    char *padfile = NULL;
    size_t width = 0;
    int measured = 0;

    if (argc < 2 || argc > 3) {
        fprintf(stderr, "usage: %s <file> [width]\n", argv[0]);
        return 1;
    }

    infile = argv[1];

    if (argc == 3) {
        int width_arg = atoi(argv[2]);

        if (width_arg <= 0) {
            fprintf(stderr, "ERROR: width must be greater than 0, got %s\n", argv[2]);
            return 1;
        }

        width = (size_t) width_arg;
    } else {
        if (max_line_length(infile, &width)) {
            return 1;
        }

        measured = 1;
    }

    printf("%s max_length: %zu\n", infile, width);

    // An empty file, or a file of bare newlines, has nothing to pad.
    if (measured && width == 0) {
        return 0;
    }

    padfile = malloc(strlen(infile) + 5);

    if (padfile == NULL) {
        fprintf(stderr, "ERROR: could not allocate filename\n");
        return 1;
    }

    sprintf(padfile, "%s.pad", infile);

    if (pad_file(infile, padfile, width)) {
        remove(padfile);
        free(padfile);
        return 1;
    }

    if (rename(padfile, infile)) {
        fprintf(stderr, "ERROR: could not replace %s\n", infile);
        remove(padfile);
        free(padfile);
        return 1;
    }

    free(padfile);
    return 0;
}

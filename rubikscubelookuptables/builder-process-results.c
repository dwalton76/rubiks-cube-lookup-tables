/*
 * Stream sorted builder-crunch-workq shards directly into the lookup table.
 *
 * Each shard is already sorted in memory by its cruncher. A heap merges those
 * streams, removes duplicate candidates, merge-joins them against the old table,
 * and writes the updated table plus next workq without a .10-results file.
 */

#define _FILE_OFFSET_BITS 64

#include <errno.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <sys/types.h>

#define MAX_LINE_LENGTH 4096
#define MAX_MOVES 64
#define DEFAULT_BUFFER_SIZE ((size_t) 1024 * 1024 * 1024)
#define MIN_INPUT_BUFFER ((size_t) 64 * 1024)
#define MAX_INPUT_BUFFER ((size_t) 8 * 1024 * 1024)
#define OUTPUT_BUFFER_SIZE ((size_t) 32 * 1024 * 1024)
#define DEFAULT_OFFSET_STRIDE 65536

typedef enum {
    FORMAT_REGULAR,
    FORMAT_EDGES
} record_format;

typedef struct {
    char line[MAX_LINE_LENGTH];
    unsigned int length;
    unsigned int merge_key_length;
    unsigned int join_key_length;
    unsigned int moves_offset;
} record;

typedef struct {
    char *filename;
    FILE *fh;
    char *io_buffer;
    char line[MAX_LINE_LENGTH];
    char previous[MAX_LINE_LENGTH];
    unsigned int length;
    unsigned int merge_key_length;
    unsigned int join_key_length;
    unsigned int moves_offset;
    unsigned long line_number;
    int have_previous;
} input_source;

typedef struct {
    input_source *sources;
    unsigned int source_count;
    unsigned int *heap;
    unsigned int heap_count;
    record_format format;
    record pending;
    int have_pending;
} merge_state;

static void
die(const char *format, ...)
{
    va_list args;
    va_start(args, format);
    fprintf(stderr, "ERROR: ");
    vfprintf(stderr, format, args);
    fprintf(stderr, "\n");
    va_end(args);
    exit(1);
}

static void *
xmalloc(size_t size)
{
    void *result = malloc(size ? size : 1);
    if (result == NULL) {
        die("could not allocate %zu bytes", size);
    }
    return result;
}

static char *
xstrdup(const char *value)
{
    char *result = strdup(value);
    if (result == NULL) {
        die("could not duplicate string");
    }
    return result;
}

static int
key_compare(const char *a, unsigned int a_length, const char *b, unsigned int b_length)
{
    unsigned int common = a_length < b_length ? a_length : b_length;
    int result = memcmp(a, b, common);
    if (result) {
        return result;
    }
    return (a_length > b_length) - (a_length < b_length);
}

static unsigned int
strip_line(char *line)
{
    unsigned int length = (unsigned int) strlen(line);
    while (length && (
        line[length - 1] == '\n' ||
        line[length - 1] == '\r' ||
        line[length - 1] == ' ')) {
        length--;
    }
    line[length] = '\0';
    return length;
}

static void
parse_record(
    const char *line,
    unsigned int length,
    record_format format,
    unsigned int *merge_key_length,
    unsigned int *join_key_length,
    unsigned int *moves_offset,
    const char *filename,
    unsigned long line_number)
{
    const char *colon1 = memchr(line, ':', length);
    const char *colon2 = NULL;

    if (colon1 != NULL) {
        colon2 = memchr(
            colon1 + 1,
            ':',
            length - (unsigned int) (colon1 + 1 - line));
    }

    if (colon1 == NULL || colon1 == line) {
        die("malformed line %lu in %s: '%.*s'", line_number, filename, length, line);
    }

    if (format == FORMAT_REGULAR) {
        if (colon2 != NULL) {
            die("regular line %lu in %s has more than one ':'", line_number, filename);
        }
        *merge_key_length = (unsigned int) (colon1 - line);
        *join_key_length = *merge_key_length;
        *moves_offset = *merge_key_length + 1;
    } else {
        if (colon2 == NULL || colon2 == colon1 + 1 ||
            memchr(
                colon2 + 1,
                ':',
                length - (unsigned int) (colon2 + 1 - line)) != NULL) {
            die("edge line %lu in %s must be pattern:state:moves", line_number, filename);
        }
        *merge_key_length = (unsigned int) (colon2 - line);
        *join_key_length = (unsigned int) (colon1 - line);
        *moves_offset = *merge_key_length + 1;
    }
}

static int
read_source(input_source *source, record_format format)
{
    if (fgets(source->line, sizeof(source->line), source->fh) == NULL) {
        if (ferror(source->fh)) {
            die("could not read %s: %s", source->filename, strerror(errno));
        }
        return 0;
    }

    source->line_number++;
    unsigned int raw_length = (unsigned int) strlen(source->line);
    if (raw_length == sizeof(source->line) - 1 &&
        source->line[raw_length - 1] != '\n' &&
        !feof(source->fh)) {
        die("line %lu in %s exceeds %d bytes",
            source->line_number, source->filename, MAX_LINE_LENGTH - 1);
    }
    source->length = strip_line(source->line);
    parse_record(
        source->line,
        source->length,
        format,
        &source->merge_key_length,
        &source->join_key_length,
        &source->moves_offset,
        source->filename,
        source->line_number);

    if (source->have_previous && strcmp(source->previous, source->line) > 0) {
        die("%s is not sorted at line %lu: '%s' before '%s'",
            source->filename, source->line_number, source->previous, source->line);
    }
    memcpy(source->previous, source->line, source->length + 1);
    source->have_previous = 1;
    return 1;
}

static int
source_compare(const merge_state *state, unsigned int a_index, unsigned int b_index)
{
    int result = strcmp(state->sources[a_index].line, state->sources[b_index].line);
    if (result) {
        return result;
    }
    return (a_index > b_index) - (a_index < b_index);
}

static void copy_source_record(record *dest, const input_source *source);

static void
heap_push(merge_state *state, unsigned int source_index)
{
    unsigned int child = state->heap_count++;
    state->heap[child] = source_index;
    while (child) {
        unsigned int parent = (child - 1) / 2;
        if (source_compare(state, state->heap[parent], state->heap[child]) <= 0) {
            break;
        }
        unsigned int tmp = state->heap[parent];
        state->heap[parent] = state->heap[child];
        state->heap[child] = tmp;
        child = parent;
    }
}

static void
heap_sift_down(merge_state *state)
{
    unsigned int parent = 0;
    while (1) {
        unsigned int left = (parent * 2) + 1;
        unsigned int right = left + 1;
        unsigned int smallest = parent;
        if (left < state->heap_count &&
            source_compare(state, state->heap[left], state->heap[smallest]) < 0) {
            smallest = left;
        }
        if (right < state->heap_count &&
            source_compare(state, state->heap[right], state->heap[smallest]) < 0) {
            smallest = right;
        }
        if (smallest == parent) {
            break;
        }
        unsigned int tmp = state->heap[parent];
        state->heap[parent] = state->heap[smallest];
        state->heap[smallest] = tmp;
        parent = smallest;
    }
}

static void
heap_take_record(merge_state *state, record *result)
{
    unsigned int source_index = state->heap[0];
    input_source *source = &state->sources[source_index];
    copy_source_record(result, source);

    if (read_source(source, state->format)) {
        // The same stream now has a new head. It can only move down because every
        // individual shard is sorted.
        heap_sift_down(state);
    } else {
        state->heap[0] = state->heap[--state->heap_count];
        if (state->heap_count) {
            heap_sift_down(state);
        }
    }
}

static void
copy_source_record(record *dest, const input_source *source)
{
    memcpy(dest->line, source->line, source->length + 1);
    dest->length = source->length;
    dest->merge_key_length = source->merge_key_length;
    dest->join_key_length = source->join_key_length;
    dest->moves_offset = source->moves_offset;
}

static unsigned int
count_moves(const record *value)
{
    if (value->moves_offset >= value->length) {
        return 0;
    }
    unsigned int count = 1;
    for (unsigned int i = value->moves_offset; i < value->length; i++) {
        if (value->line[i] == ' ') {
            count++;
        }
    }
    return count;
}

static int
record_is_better(const record *value, const record *best, record_format format)
{
    if (format == FORMAT_EDGES) {
        unsigned int value_moves = count_moves(value);
        unsigned int best_moves = count_moves(best);
        if (value_moves != best_moves) {
            return value_moves < best_moves;
        }
    }
    return strcmp(value->line, best->line) < 0;
}

static int
next_merge_record(merge_state *state, record *result)
{
    if (!state->heap_count) {
        return 0;
    }

    heap_take_record(state, result);

    while (state->heap_count) {
        input_source *source = &state->sources[state->heap[0]];
        if (key_compare(
            source->line,
            source->merge_key_length,
            result->line,
            result->merge_key_length)) {
            break;
        }

        record current;
        heap_take_record(state, &current);
        if (record_is_better(&current, result, state->format)) {
            *result = current;
        }
    }
    return 1;
}

static int
next_join_record(merge_state *state, record *result)
{
    if (state->have_pending) {
        *result = state->pending;
        state->have_pending = 0;
    } else if (!next_merge_record(state, result)) {
        return 0;
    }

    if (state->format == FORMAT_REGULAR) {
        return 1;
    }

    while (1) {
        record current;
        if (!next_merge_record(state, &current)) {
            break;
        }
        if (key_compare(
            current.line,
            current.join_key_length,
            result->line,
            result->join_key_length)) {
            state->pending = current;
            state->have_pending = 1;
            break;
        }
        if (record_is_better(&current, result, FORMAT_EDGES)) {
            *result = current;
        }
    }
    return 1;
}

static size_t
parse_size(const char *value)
{
    char *end = NULL;
    unsigned long long amount = strtoull(value, &end, 10);
    if (end == value || !amount) {
        die("invalid buffer size '%s'", value);
    }
    if (*end == 'K' || *end == 'k') {
        amount *= 1024ULL;
        end++;
    } else if (*end == 'M' || *end == 'm') {
        amount *= 1024ULL * 1024ULL;
        end++;
    } else if (*end == 'G' || *end == 'g') {
        amount *= 1024ULL * 1024ULL * 1024ULL;
        end++;
    }
    if (*end || amount > SIZE_MAX) {
        die("invalid buffer size '%s'", value);
    }
    return (size_t) amount;
}

static char **
read_manifest(const char *filename, unsigned int *count)
{
    FILE *fh = fopen(filename, "rb");
    if (fh == NULL) {
        die("could not open manifest %s: %s", filename, strerror(errno));
    }
    if (fseek(fh, 0, SEEK_END)) {
        die("could not seek manifest %s", filename);
    }
    long file_size = ftell(fh);
    if (file_size < 0 || fseek(fh, 0, SEEK_SET)) {
        die("could not measure manifest %s", filename);
    }
    if (!file_size) {
        fclose(fh);
        *count = 0;
        return NULL;
    }

    char *contents = xmalloc((size_t) file_size + 1);
    if (fread(contents, 1, (size_t) file_size, fh) != (size_t) file_size) {
        die("could not read manifest %s", filename);
    }
    fclose(fh);
    contents[file_size] = '\0';

    unsigned int capacity = 64;
    char **paths = xmalloc(capacity * sizeof(char *));
    unsigned int path_count = 0;
    char *cursor = contents;
    char *limit = contents + file_size;
    while (cursor < limit) {
        size_t remaining = (size_t) (limit - cursor);
        size_t length = strnlen(cursor, remaining);
        if (length) {
            if (path_count == capacity) {
                capacity *= 2;
                char **grown = realloc(paths, capacity * sizeof(char *));
                if (grown == NULL) {
                    die("could not grow manifest path list");
                }
                paths = grown;
            }
            paths[path_count++] = xstrdup(cursor);
        }
        cursor += length + 1;
    }
    free(contents);
    *count = path_count;
    return paths;
}

static void
raise_file_limit(unsigned int source_count)
{
    struct rlimit limit;
    rlim_t required = (rlim_t) source_count + 16;
    if (getrlimit(RLIMIT_NOFILE, &limit)) {
        die("could not read RLIMIT_NOFILE");
    }
    if (limit.rlim_cur < required) {
        struct rlimit wanted = limit;
        wanted.rlim_cur = required <= limit.rlim_max ? required : limit.rlim_max;
        if (setrlimit(RLIMIT_NOFILE, &wanted)) {
            die("need %llu file descriptors but could not raise RLIMIT_NOFILE: %s",
                (unsigned long long) required, strerror(errno));
        }
        limit = wanted;
    }
    if (limit.rlim_cur < required) {
        die("need %llu file descriptors but limit is %llu",
            (unsigned long long) required, (unsigned long long) limit.rlim_cur);
    }
}

static void
open_merger(
    merge_state *state,
    char **filenames,
    unsigned int filename_count,
    record_format format,
    size_t total_buffer_size)
{
    memset(state, 0, sizeof(*state));
    state->format = format;
    state->source_count = filename_count;
    if (!filename_count) {
        return;
    }

    raise_file_limit(filename_count);
    state->sources = xmalloc(filename_count * sizeof(input_source));
    state->heap = xmalloc(filename_count * sizeof(unsigned int));
    memset(state->sources, 0, filename_count * sizeof(input_source));

    size_t buffer_size = total_buffer_size / filename_count;
    if (buffer_size < MIN_INPUT_BUFFER) {
        buffer_size = MIN_INPUT_BUFFER;
    } else if (buffer_size > MAX_INPUT_BUFFER) {
        buffer_size = MAX_INPUT_BUFFER;
    }

    for (unsigned int i = 0; i < filename_count; i++) {
        input_source *source = &state->sources[i];
        source->filename = filenames[i];
        source->fh = fopen(source->filename, "r");
        if (source->fh == NULL) {
            die("could not open shard %s: %s", source->filename, strerror(errno));
        }
        source->io_buffer = xmalloc(buffer_size);
        if (setvbuf(source->fh, source->io_buffer, _IOFBF, buffer_size)) {
            die("could not buffer shard %s", source->filename);
        }
        if (read_source(source, format)) {
            heap_push(state, i);
        }
    }
}

static void
close_merger(merge_state *state)
{
    for (unsigned int i = 0; i < state->source_count; i++) {
        input_source *source = &state->sources[i];
        if (fclose(source->fh)) {
            die("could not close shard %s", source->filename);
        }
        free(source->io_buffer);
    }
    free(state->sources);
    free(state->heap);
}

static FILE *
open_output(const char *filename, char **buffer)
{
    FILE *fh = fopen(filename, "w");
    if (fh == NULL) {
        die("could not open %s for writing: %s", filename, strerror(errno));
    }
    *buffer = xmalloc(OUTPUT_BUFFER_SIZE);
    if (setvbuf(fh, *buffer, _IOFBF, OUTPUT_BUFFER_SIZE)) {
        die("could not buffer %s", filename);
    }
    return fh;
}

static void
write_all(FILE *fh, const void *data, size_t length, const char *filename)
{
    if (length && fwrite(data, 1, length, fh) != length) {
        die("could not write %s: %s", filename, strerror(errno));
    }
}

static unsigned int
reverse_steps(const char *steps, unsigned int steps_length, char *result)
{
    const char *starts[MAX_MOVES];
    unsigned int lengths[MAX_MOVES];
    unsigned int count = 0;
    unsigned int index = 0;
    char *cursor = result;

    while (index < steps_length) {
        while (index < steps_length && steps[index] == ' ') {
            index++;
        }
        if (index == steps_length) {
            break;
        }
        if (count == MAX_MOVES) {
            die("move sequence exceeds %d moves", MAX_MOVES);
        }
        starts[count] = steps + index;
        while (index < steps_length && steps[index] != ' ') {
            index++;
        }
        lengths[count] = (unsigned int) (steps + index - starts[count]);
        count++;
    }

    for (unsigned int i = count; i > 0; i--) {
        const char *move = starts[i - 1];
        unsigned int length = lengths[i - 1];
        if (cursor != result) {
            *cursor++ = ' ';
        }
        if (move[length - 1] == '2') {
            memcpy(cursor, move, length);
            cursor += length;
        } else if (move[length - 1] == '\'') {
            memcpy(cursor, move, length - 1);
            cursor += length - 1;
        } else {
            memcpy(cursor, move, length);
            cursor += length;
            *cursor++ = '\'';
        }
    }
    return (unsigned int) (cursor - result);
}

static unsigned int
write_new_table_line(
    FILE *fh,
    const char *filename,
    const record *value,
    char *out,
    unsigned int pad_width)
{
    memcpy(out, value->line, value->moves_offset);
    unsigned int length = value->moves_offset;
    length += reverse_steps(
        value->line + value->moves_offset,
        value->length - value->moves_offset,
        out + length);

    unsigned int written = length;

    if (pad_width) {
        // The callers that ask for padding already know the widest line every layer
        // will produce, so a line wider than that means their width is wrong and the
        // table would sort fine while quietly breaking the solver's binary search.
        if (length > pad_width) {
            die("line '%.*s' is %u bytes, wider than --pad-width %u",
                length, out, length, pad_width);
        }
        memset(out + length, ' ', pad_width - length);
        written = pad_width;
    }

    out[written] = '\n';
    write_all(fh, out, written + 1, filename);
    return length;
}

static void
write_offsets_file(
    const char *filename,
    unsigned int stride,
    unsigned long line_count,
    const off_t *offsets,
    size_t offset_count)
{
    FILE *fh = fopen(filename, "w");
    if (fh == NULL) {
        die("could not open %s for writing: %s", filename, strerror(errno));
    }
    fprintf(fh, "%u %lu\n", stride, line_count);
    for (size_t i = 0; i < offset_count; i++) {
        fprintf(fh, "%lld\n", (long long) offsets[i]);
    }
    if (fclose(fh)) {
        die("could not finish %s", filename);
    }
}

static void
record_offset(off_t **offsets, size_t *count, size_t *capacity, off_t value)
{
    if (*count == *capacity) {
        *capacity = *capacity ? *capacity * 2 : 64;
        off_t *grown = realloc(*offsets, *capacity * sizeof(off_t));
        if (grown == NULL) {
            die("could not grow offset index");
        }
        *offsets = grown;
    }
    (*offsets)[(*count)++] = value;
}

static void
run_merge_only(merge_state *state, const char *output_filename)
{
    char *buffer = NULL;
    FILE *output = open_output(output_filename, &buffer);
    record value;
    while (next_merge_record(state, &value)) {
        write_all(output, value.line, value.length, output_filename);
        write_all(output, "\n", 1, output_filename);
    }
    if (fclose(output)) {
        die("could not finish %s", output_filename);
    }
    free(buffer);
    printf("0 0\n");
}

static void
run_layer(
    merge_state *shards,
    merge_state *tables,
    const char *output_filename,
    const char *offsets_filename,
    unsigned int offset_stride)
{
    char *output_buffer = NULL;
    FILE *output = open_output(output_filename, &output_buffer);
    char reverse_buf[MAX_LINE_LENGTH];
    record seen;
    record candidate;
    int have_seen = next_join_record(tables, &seen);
    int have_candidate = next_join_record(shards, &candidate);
    unsigned long new_count = 0;
    unsigned int max_reversed_length = 0;
    off_t *offsets = NULL;
    size_t offset_count = 0;
    size_t offset_capacity = 0;

    while (have_candidate) {
        int compare = 1;
        if (have_seen) {
            compare = key_compare(
                seen.line,
                seen.join_key_length,
                candidate.line,
                candidate.join_key_length);
        }

        if (compare < 0) {
            have_seen = next_join_record(tables, &seen);
        } else if (compare == 0) {
            have_seen = next_join_record(tables, &seen);
            have_candidate = next_join_record(shards, &candidate);
        } else {
            if (offsets_filename && new_count % offset_stride == 0) {
                record_offset(&offsets, &offset_count, &offset_capacity, ftello(output));
            }
            write_all(output, candidate.line, candidate.length, output_filename);
            write_all(output, "\n", 1, output_filename);

            unsigned int reversed = candidate.moves_offset + reverse_steps(
                candidate.line + candidate.moves_offset,
                candidate.length - candidate.moves_offset,
                reverse_buf);
            if (reversed > max_reversed_length) {
                max_reversed_length = reversed;
            }
            new_count++;
            have_candidate = next_join_record(shards, &candidate);
        }
    }

    if (fclose(output)) {
        die("could not finish layer %s", output_filename);
    }
    free(output_buffer);
    if (offsets_filename) {
        write_offsets_file(
            offsets_filename, offset_stride, new_count, offsets, offset_count);
    }
    free(offsets);
    printf("%lu %u\n", new_count, max_reversed_length);
}

static void
run_finalize(merge_state *state, const char *output_filename, unsigned int pad_width)
{
    char *output_buffer = NULL;
    FILE *output = open_output(output_filename, &output_buffer);
    char *out = xmalloc(MAX_LINE_LENGTH * 2);
    record value;
    unsigned long count = 0;
    unsigned int max_length = 0;

    while (next_merge_record(state, &value)) {
        unsigned int length = write_new_table_line(
            output, output_filename, &value, out, pad_width);
        if (length > max_length) {
            max_length = length;
        }
        count++;
    }

    if (fclose(output)) {
        die("could not finish %s", output_filename);
    }
    free(output_buffer);
    free(out);
    printf("%lu %u\n", count, max_length);
}

static void
usage(const char *program)
{
    printf(
        "usage: %s --format regular|edges --files0-from FILE [--buffer-size SIZE]\n"
        "          (--merge-only-output FILE |\n"
        "           --output-layer FILE [--tables0-from FILE] [--offsets FILE]\n"
        "            [--offset-stride N] |\n"
        "           --finalize --output-table FILE [--pad-width N])\n",
        program);
}

int
main(int argc, char *argv[])
{
    const char *format_arg = NULL;
    const char *manifest_filename = NULL;
    const char *tables_manifest = NULL;
    const char *output_filename = NULL;
    const char *merge_only_filename = NULL;
    const char *layer_filename = NULL;
    const char *offsets_filename = NULL;
    unsigned int offset_stride = DEFAULT_OFFSET_STRIDE;
    unsigned int pad_width = 0;
    int finalize = 0;
    size_t buffer_size = DEFAULT_BUFFER_SIZE;

    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--format") && i + 1 < argc) {
            format_arg = argv[++i];
        } else if (!strcmp(argv[i], "--files0-from") && i + 1 < argc) {
            manifest_filename = argv[++i];
        } else if (!strcmp(argv[i], "--tables0-from") && i + 1 < argc) {
            tables_manifest = argv[++i];
        } else if (!strcmp(argv[i], "--output-table") && i + 1 < argc) {
            output_filename = argv[++i];
        } else if (!strcmp(argv[i], "--output-layer") && i + 1 < argc) {
            layer_filename = argv[++i];
        } else if (!strcmp(argv[i], "--merge-only-output") && i + 1 < argc) {
            merge_only_filename = argv[++i];
        } else if (!strcmp(argv[i], "--offsets") && i + 1 < argc) {
            offsets_filename = argv[++i];
        } else if (!strcmp(argv[i], "--offset-stride") && i + 1 < argc) {
            unsigned long value = strtoul(argv[++i], NULL, 10);
            if (!value || value > UINT32_MAX) {
                die("invalid --offset-stride");
            }
            offset_stride = (unsigned int) value;
        } else if (!strcmp(argv[i], "--pad-width") && i + 1 < argc) {
            unsigned long value = strtoul(argv[++i], NULL, 10);
            if (!value || value >= MAX_LINE_LENGTH * 2) {
                die("invalid --pad-width");
            }
            pad_width = (unsigned int) value;
        } else if (!strcmp(argv[i], "--finalize")) {
            finalize = 1;
        } else if (!strcmp(argv[i], "--buffer-size") && i + 1 < argc) {
            buffer_size = parse_size(argv[++i]);
        } else if (!strcmp(argv[i], "-h") || !strcmp(argv[i], "--help")) {
            usage(argv[0]);
            return 0;
        } else {
            die("invalid or incomplete argument '%s'", argv[i]);
        }
    }

    if (format_arg == NULL || manifest_filename == NULL) {
        die("--format and --files0-from are required");
    }
    record_format format;
    if (!strcmp(format_arg, "regular")) {
        format = FORMAT_REGULAR;
    } else if (!strcmp(format_arg, "edges")) {
        format = FORMAT_EDGES;
    } else {
        die("--format must be regular or edges");
    }

    int mode_count = (merge_only_filename != NULL) + (layer_filename != NULL) + finalize;
    if (mode_count != 1) {
        die("choose exactly one of --merge-only-output, --output-layer, or --finalize");
    }
    if (finalize && output_filename == NULL) {
        die("--finalize requires --output-table");
    }
    if (pad_width && !finalize) {
        die("--pad-width only applies to --finalize");
    }

    unsigned int filename_count = 0;
    char **filenames = read_manifest(manifest_filename, &filename_count);
    size_t shard_budget = buffer_size;
    unsigned int table_count = 0;
    char **table_files = NULL;

    if (tables_manifest) {
        table_files = read_manifest(tables_manifest, &table_count);
        shard_budget = buffer_size / 2;
    }

    merge_state shards;
    open_merger(&shards, filenames, filename_count, format, shard_budget);

    if (merge_only_filename) {
        run_merge_only(&shards, merge_only_filename);
    } else if (finalize) {
        run_finalize(&shards, output_filename, pad_width);
    } else {
        merge_state tables;
        open_merger(&tables, table_files, table_count, format, buffer_size - shard_budget);
        run_layer(&shards, &tables, layer_filename, offsets_filename, offset_stride);
        close_merger(&tables);
        for (unsigned int i = 0; i < table_count; i++) {
            free(table_files[i]);
        }
        free(table_files);
    }

    close_merger(&shards);
    for (unsigned int i = 0; i < filename_count; i++) {
        free(filenames[i]);
    }
    free(filenames);
    return 0;
}

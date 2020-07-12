
#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>
#include "ida_search_core.h"

void LOG(const char *fmt, ...) {
    char date[20];
    struct timeval tv;
    va_list args;

    /* print the progname, version, and timestamp */
    gettimeofday(&tv, NULL);
    strftime(date, sizeof(date) / sizeof(*date), "%Y-%m-%dT%H:%M:%S", gmtime(&tv.tv_sec));
    printf("[%s.%03d] ", date, (int)tv.tv_usec / 1000);

    /* printf like normal */
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
}


void
print_cube (char *cube, int size)
{
    int squares_per_side = size * size;
    int square_count = squares_per_side * 6;
    int rows = size * 3;
    printf("\n");

    for (int row=1; row <= rows; row++) {

        // U
        if (row <= size) {
            int i = ((row-1) * size) + 1;
            int i_end = i + size - 1;

            for (int z = 0; z < size; z++) {
                printf("  ");
            }

            for ( ; i <= i_end; i++) {
                printf("%c ", cube[i]);
            }

            printf("\n");

            if (row == size) {
                printf("\n");
            }

        // D
        } else if (row > (size * 2)) {
            int i = (squares_per_side * 5) + 1 + ((row - (size*2) - 1) * size);
            int i_end = i + size - 1;

            if (row == ((size * 2) + 1)) {
                printf("\n");
            }

            for (int z = 0; z < size; z++) {
                printf("  ");
            }

            for (; i <= i_end; i++) {
                printf("%c ", cube[i]);
            }
            printf("\n");

        // L, F, R, B
        } else {

            // L
            int i_start = squares_per_side + 1 + ((row - 1 -size) * size);
            int i_end = i_start + size - 1;
            int i = i_start;
            for (; i <= i_end; i++) {
                printf("%c ", cube[i]);
            }

            // F
            i = i_start + squares_per_side;
            i_end = i + size - 1;
            for (; i <= i_end; i++) {
                printf("%c ", cube[i]);
            }

            // R
            i = i_start + (squares_per_side * 2);
            i_end = i + size - 1;
            for (; i <= i_end; i++) {
                printf("%c ", cube[i]);
            }

            // B
            i = i_start + (squares_per_side * 3);
            i_end = i + size - 1;
            for (; i <= i_end; i++) {
                printf("%c ", cube[i]);
            }

            printf("\n");
        }
    }
    printf("\n");
}

int
strmatch (char *str1, char *str2)
{
    if (strcmp(str1, str2) == 0) {
        return 1;
    }
    return 0;
}

move_type
str2move(char *str)
{
    if (strmatch(str, "U")) {
        return U;
    } else if (strmatch(str, "U'")) {
        return U_PRIME;
    } else if (strmatch(str, "U2")) {
        return U2;
    } else if (strmatch(str, "Uw")) {
        return Uw;
    } else if (strmatch(str, "Uw'")) {
        return Uw_PRIME;
    } else if (strmatch(str, "Uw2")) {
        return Uw2;
    } else if (strmatch(str, "3Uw")) {
        return threeUw;
    } else if (strmatch(str, "3Uw'")) {
        return threeUw_PRIME;
    } else if (strmatch(str, "3Uw2")) {
        return threeUw2;

    } else if (strmatch(str, "L")) {
        return L;
    } else if (strmatch(str, "L'")) {
        return L_PRIME;
    } else if (strmatch(str, "L2")) {
        return L2;
    } else if (strmatch(str, "Lw")) {
        return Lw;
    } else if (strmatch(str, "Lw'")) {
        return Lw_PRIME;
    } else if (strmatch(str, "Lw2")) {
        return Lw2;
    } else if (strmatch(str, "3Lw")) {
        return threeLw;
    } else if (strmatch(str, "3Lw'")) {
        return threeLw_PRIME;
    } else if (strmatch(str, "3Lw2")) {
        return threeLw2;

    } else if (strmatch(str, "F")) {
        return F;
    } else if (strmatch(str, "F'")) {
        return F_PRIME;
    } else if (strmatch(str, "F2")) {
        return F2;
    } else if (strmatch(str, "Fw")) {
        return Fw;
    } else if (strmatch(str, "Fw'")) {
        return Fw_PRIME;
    } else if (strmatch(str, "Fw2")) {
        return Fw2;
    } else if (strmatch(str, "3Fw")) {
        return threeFw;
    } else if (strmatch(str, "3Fw'")) {
        return threeFw_PRIME;
    } else if (strmatch(str, "3Fw2")) {
        return threeFw2;

    } else if (strmatch(str, "R")) {
        return R;
    } else if (strmatch(str, "R'")) {
        return R_PRIME;
    } else if (strmatch(str, "R2")) {
        return R2;
    } else if (strmatch(str, "Rw")) {
        return Rw;
    } else if (strmatch(str, "Rw'")) {
        return Rw_PRIME;
    } else if (strmatch(str, "Rw2")) {
        return Rw2;
    } else if (strmatch(str, "3Rw")) {
        return threeRw;
    } else if (strmatch(str, "3Rw'")) {
        return threeRw_PRIME;
    } else if (strmatch(str, "3Rw2")) {
        return threeRw2;

    } else if (strmatch(str, "B")) {
        return B;
    } else if (strmatch(str, "B'")) {
        return B_PRIME;
    } else if (strmatch(str, "B2")) {
        return B2;
    } else if (strmatch(str, "Bw")) {
        return Bw;
    } else if (strmatch(str, "Bw'")) {
        return Bw_PRIME;
    } else if (strmatch(str, "Bw2")) {
        return Bw2;
    } else if (strmatch(str, "3Bw")) {
        return threeBw;
    } else if (strmatch(str, "3Bw'")) {
        return threeBw_PRIME;
    } else if (strmatch(str, "3Bw2")) {
        return threeBw2;

    } else if (strmatch(str, "D")) {
        return D;
    } else if (strmatch(str, "D'")) {
        return D_PRIME;
    } else if (strmatch(str, "D2")) {
        return D2;
    } else if (strmatch(str, "Dw")) {
        return Dw;
    } else if (strmatch(str, "Dw'")) {
        return Dw_PRIME;
    } else if (strmatch(str, "Dw2")) {
        return Dw2;
    } else if (strmatch(str, "3Dw")) {
        return threeDw;
    } else if (strmatch(str, "3Dw'")) {
        return threeDw_PRIME;
    } else if (strmatch(str, "3Dw2")) {
        return threeDw2;

    } else {
        printf("ERROR: str2move invalid move \"%s\"\n", str);
        exit(1);
    }
}

unsigned char
steps_on_same_face_and_layer(move_type move, move_type prev_move)
{
    switch (move) {
    case U:
    case U_PRIME:
    case U2:
        switch (prev_move) {
        case U:
        case U_PRIME:
        case U2:
            return 1;
        default:
            return 0;
        }
        break;

    case L:
    case L_PRIME:
    case L2:
        switch (prev_move) {
        case L:
        case L_PRIME:
        case L2:
            return 1;
        default:
            return 0;
        }
        break;

    case F:
    case F_PRIME:
    case F2:
        switch (prev_move) {
        case F:
        case F_PRIME:
        case F2:
            return 1;
        default:
            return 0;
        }
        break;

    case R:
    case R_PRIME:
    case R2:
        switch (prev_move) {
        case R:
        case R_PRIME:
        case R2:
            return 1;
        default:
            return 0;
        }
        break;

    case B:
    case B_PRIME:
    case B2:
        switch (prev_move) {
        case B:
        case B_PRIME:
        case B2:
            return 1;
        default:
            return 0;
        }
        break;

    case D:
    case D_PRIME:
    case D2:
        switch (prev_move) {
        case D:
        case D_PRIME:
        case D2:
            return 1;
        default:
            return 0;
        }
        break;

    // 2-layer turns
    case Uw:
    case Uw_PRIME:
    case Uw2:
        switch (prev_move) {
        case Uw:
        case Uw_PRIME:
        case Uw2:
            return 1;
        default:
            return 0;
        }
        break;

    case Lw:
    case Lw_PRIME:
    case Lw2:
        switch (prev_move) {
        case Lw:
        case Lw_PRIME:
        case Lw2:
            return 1;
        default:
            return 0;
        }
        break;

    case Fw:
    case Fw_PRIME:
    case Fw2:
        switch (prev_move) {
        case Fw:
        case Fw_PRIME:
        case Fw2:
            return 1;
        default:
            return 0;
        }
        break;

    case Rw:
    case Rw_PRIME:
    case Rw2:
        switch (prev_move) {
        case Rw:
        case Rw_PRIME:
        case Rw2:
            return 1;
        default:
            return 0;
        }
        break;

    case Bw:
    case Bw_PRIME:
    case Bw2:
        switch (prev_move) {
        case Bw:
        case Bw_PRIME:
        case Bw2:
            return 1;
        default:
            return 0;
        }
        break;

    case Dw:
    case Dw_PRIME:
    case Dw2:
        switch (prev_move) {
        case Dw:
        case Dw_PRIME:
        case Dw2:
            return 1;
        default:
            return 0;
        }
        break;

    case threeUw:
    case threeUw_PRIME:
    case threeUw2:
        switch (prev_move) {
        case threeUw:
        case threeUw_PRIME:
        case threeUw2:
            return 1;
        default:
            return 0;
        }
        break;

    case threeLw:
    case threeLw_PRIME:
    case threeLw2:
        switch (prev_move) {
        case threeLw:
        case threeLw_PRIME:
        case threeLw2:
            return 1;
        default:
            return 0;
        }
        break;

    case threeFw:
    case threeFw_PRIME:
    case threeFw2:
        switch (prev_move) {
        case threeFw:
        case threeFw_PRIME:
        case threeFw2:
            return 1;
        default:
            return 0;
        }
        break;

    case threeRw:
    case threeRw_PRIME:
    case threeRw2:
        switch (prev_move) {
        case threeRw:
        case threeRw_PRIME:
        case threeRw2:
            return 1;
        default:
            return 0;
        }
        break;

    case threeBw:
    case threeBw_PRIME:
    case threeBw2:
        switch (prev_move) {
        case threeBw:
        case threeBw_PRIME:
        case threeBw2:
            return 1;
        default:
            return 0;
        }
        break;

    case threeDw:
    case threeDw_PRIME:
    case threeDw2:
        switch (prev_move) {
        case threeDw:
        case threeDw_PRIME:
        case threeDw2:
            return 1;
        default:
            return 0;
        }
        break;

    case X:
    case X_PRIME:
    case Y:
    case Y_PRIME:
    case Z:
    case Z_PRIME:
        return 0;

    default:
        printf("ERROR: steps_on_same_face_and_layer add support for %d\n", move);
        exit(1);
    }

    return 0;
}

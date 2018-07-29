
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "rotate_xxx.h"

// To compile:
//  gcc -o rotate rotate.c rotate_xxx.c
//
//  gcc -ggdb -o rotate rotate.c rotate_xxx.c

/*
 * U is 1
 * L is 2
 * F is 3
 * R is 4
 * B is 5
 * D is 6
 * x is 7
 */

typedef enum {
    NONE,

    // 4x4x4 centers
    ULFRBD_CENTERS_SOLVE_444,
    ULFRBD_CENTERS_SOLVE_UNSTAGED_444,

    // 4x4x4 edges
    EDGES_444,

    // 5x5x5
    EDGES_STAGE_FIRST_FOUR_555,
    EDGES_STAGE_SECOND_FOUR_555,
    EDGES_PAIR_LAST_FOUR_555,

    // 5x5x5 solve centers
    UL_CENTERS_SOLVE_555,
    UF_CENTERS_SOLVE_555,
    ULFRBD_T_CENTERS_SOLVE_555,
    LR_T_CENTERS_SOLVE_555,
    ULFRBD_CENTERS_SOLVE_UNSTAGED_555,
    ULFRBD_CENTERS_SOLVE_STAGE_FIRST_FOUR_EDGES_555,

    // 7x7x7
    UD_OBLIQUE_EDGE_PAIRING_777,
    UD_OBLIQUE_EDGE_PAIRING_MIDDLE_ONLY_777,
    UD_OBLIQUE_EDGE_PAIRING_LEFT_ONLY_777,
    UD_OBLIQUE_EDGE_PAIRING_RIGHT_ONLY_777,

} lookup_table_type;

void
init_cube(int *cube, int size, lookup_table_type type)
{
    int squares_per_side = size * size;
    int square_count = squares_per_side * 6;
    int U_start = 1;
    int L_start = U_start + squares_per_side;
    int F_start = L_start + squares_per_side;
    int R_start = F_start + squares_per_side;
    int B_start = R_start + squares_per_side;
    int D_start = B_start + squares_per_side;
    int side_name;

    for (int i = 1; i <= square_count; i++) {
        if (i >= D_start) {
            side_name = 6;
        } else if (i >= B_start) {
            side_name = 5;
        } else if (i >= R_start) {
            side_name = 4;
        } else if (i >= F_start) {
            side_name = 3;
        } else if (i >= L_start) {
            side_name = 2;
        } else if (i >= U_start) {
            side_name = 1;
        }
        cube[i] = side_name;
    }
}

void
print_cube(int *cube, int size)
{
    int squares_per_side = size * size;
    int square_count = squares_per_side * 6;
    int rows = size * 3;

    for (int row=1; row <= rows; row++) {

        // U
        if (row <= size) {
            int i = ((row-1) * size) + 1;
            int i_end = i + size - 1;
            printf("\t");
            for ( ; i <= i_end; i++) {
                printf("%d ", cube[i]);
            }
            printf("\n");

        // D
        } else if (row > (size * 2)) {
            int i = (squares_per_side * 5) + 1 + ((row - (size*2) - 1) * size);
            int i_end = i + size - 1;
            printf("\t");
            for (; i <= i_end; i++) {
                printf("%d ", cube[i]);
            }
            printf("\n");

        // L, F, R, B
        } else {

            // L
            int i_start = squares_per_side + 1 + ((row - 1 -size) * size);
            int i_end = i_start + size - 1;
            int i = i_start;
            for (; i <= i_end; i++) {
                printf("%d ", cube[i]);
            }

            // F
            i = i_start + squares_per_side;
            i_end = i + size - 1;
            for (; i <= i_end; i++) {
                printf("%d ", cube[i]);
            }

            // R
            i = i_start + (squares_per_side * 2);
            i_end = i + size - 1;
            for (; i <= i_end; i++) {
                printf("%d ", cube[i]);
            }

            // B
            i = i_start + (squares_per_side * 3);
            i_end = i + size - 1;
            for (; i <= i_end; i++) {
                printf("%d ", cube[i]);
            }

            printf("\n");
        }
    }
    printf("\n");
}

void
nuke_cube_corners_333(int *cube)
{
    // Upper corners
    cube[1] = 7;
    cube[3] = 7;
    cube[7] = 7;
    cube[9] = 7;

    // Left corners
    cube[10] = 7;
    cube[12] = 7;
    cube[16] = 7;
    cube[18] = 7;

    // Front corners
    cube[19] = 7;
    cube[21] = 7;
    cube[25] = 7;
    cube[27] = 7;

    // Right corners
    cube[28] = 7;
    cube[30] = 7;
    cube[34] = 7;
    cube[36] = 7;

    // Back corners
    cube[37] = 7;
    cube[39] = 7;
    cube[43] = 7;
    cube[45] = 7;

    // Down corners
    cube[46] = 7;
    cube[48] = 7;
    cube[52] = 7;
    cube[54] = 7;
}

void
nuke_cube_edges_333(int *cube)
{
    // Upper corners
    cube[2] = 7;
    cube[4] = 7;
    cube[6] = 7;
    cube[8] = 7;

    // Left corners
    cube[11] = 7;
    cube[13] = 7;
    cube[15] = 7;
    cube[17] = 7;

    // Front corners
    cube[20] = 7;
    cube[22] = 7;
    cube[24] = 7;
    cube[26] = 7;

    // Right corners
    cube[29] = 7;
    cube[31] = 7;
    cube[33] = 7;
    cube[35] = 7;

    // Back corners
    cube[38] = 7;
    cube[40] = 7;
    cube[42] = 7;
    cube[44] = 7;

    // Down corners
    cube[47] = 7;
    cube[49] = 7;
    cube[51] = 7;
    cube[53] = 7;
}

void
nuke_cube_corners_444(int *cube)
{
    // Upper corners
    cube[1] = 7;
    cube[4] = 7;
    cube[13] = 7;
    cube[16] = 7;

    // Left corners
    cube[17] = 7;
    cube[20] = 7;
    cube[29] = 7;
    cube[32] = 7;

    // Front corners
    cube[33] = 7;
    cube[36] = 7;
    cube[45] = 7;
    cube[48] = 7;

    // Right corners
    cube[49] = 7;
    cube[52] = 7;
    cube[61] = 7;
    cube[64] = 7;

    // Back corners
    cube[65] = 7;
    cube[68] = 7;
    cube[77] = 7;
    cube[80] = 7;

    // Down corners
    cube[81] = 7;
    cube[84] = 7;
    cube[93] = 7;
    cube[96] = 7;
}

void
nuke_cube_edges_444(int *cube)
{
    // Upper
    for (int i = 2; i <= 3; i++)
        cube[i] = 7;
    cube[5] = 7;
    cube[8] = 7;
    cube[9] = 7;
    cube[12] = 7;
    for (int i = 14; i <= 15; i++)
        cube[i] = 7;

    // Left
    for (int i = 18; i <= 19; i++)
        cube[i] = 7;
    cube[21] = 7;
    cube[24] = 7;
    cube[25] = 7;
    cube[28] = 7;
    for (int i = 30; i <= 31; i++)
        cube[i] = 7;

    // Front
    for (int i = 34; i <= 35; i++)
        cube[i] = 7;
    cube[37] = 7;
    cube[40] = 7;
    cube[41] = 7;
    cube[44] = 7;
    for (int i = 46; i <= 47; i++)
        cube[i] = 7;

    // Right
    for (int i = 50; i <= 51; i++)
        cube[i] = 7;
    cube[53] = 7;
    cube[56] = 7;
    cube[57] = 7;
    cube[60] = 7;
    for (int i = 62; i <= 63; i++)
        cube[i] = 7;

    // Back
    for (int i = 66; i <= 67; i++)
        cube[i] = 7;
    cube[69] = 7;
    cube[72] = 7;
    cube[73] = 7;
    cube[76] = 7;
    for (int i = 78; i <= 79; i++)
        cube[i] = 7;

    // Down
    for (int i = 82; i <= 83; i++)
        cube[i] = 7;
    cube[85] = 7;
    cube[88] = 7;
    cube[89] = 7;
    cube[92] = 7;
    for (int i = 94; i <= 95; i++)
        cube[i] = 7;
}

void
nuke_cube_centers_444(int *cube)
{
    // Upper
    cube[6] = 7;
    cube[7] = 7;
    cube[10] = 7;
    cube[11] = 7;

    // Left
    cube[22] = 7;
    cube[23] = 7;
    cube[26] = 7;
    cube[27] = 7;

    // Front
    cube[38] = 7;
    cube[39] = 7;
    cube[42] = 7;
    cube[43] = 7;

    // Right
    cube[54] = 7;
    cube[55] = 7;
    cube[58] = 7;
    cube[59] = 7;

    // Back
    cube[70] = 7;
    cube[71] = 7;
    cube[74] = 7;
    cube[75] = 7;

    // Down
    cube[86] = 7;
    cube[87] = 7;
    cube[90] = 7;
    cube[91] = 7;
}

void
nuke_cube_corners_555(int *cube)
{
    // Upper corners
    cube[1] = 7;
    cube[5] = 7;
    cube[21] = 7;
    cube[25] = 7;

    // Left corners
    cube[26] = 7;
    cube[30] = 7;
    cube[46] = 7;
    cube[50] = 7;

    // Front corners
    cube[51] = 7;
    cube[55] = 7;
    cube[71] = 7;
    cube[75] = 7;

    // Right corners
    cube[76] = 7;
    cube[80] = 7;
    cube[96] = 7;
    cube[100] = 7;

    // Back corners
    cube[101] = 7;
    cube[105] = 7;
    cube[121] = 7;
    cube[125] = 7;

    // Down corners
    cube[126] = 7;
    cube[130] = 7;
    cube[146] = 7;
    cube[150] = 7;
}

void
nuke_cube_edges_555(int *cube)
{
    // Upper
    for (int i = 2; i <= 4; i++)
        cube[i] = 7;
    cube[6] = 7;
    cube[10] = 7;
    cube[11] = 7;
    cube[15] = 7;
    cube[16] = 7;
    cube[20] = 7;
    for (int i = 22; i <= 24; i++)
        cube[i] = 7;

    // Left
    for (int i = 27; i <= 29; i++)
        cube[i] = 7;
    cube[31] = 7;
    cube[35] = 7;
    cube[36] = 7;
    cube[40] = 7;
    cube[41] = 7;
    cube[45] = 7;
    for (int i = 47; i <= 49; i++)
        cube[i] = 7;

    // Front
    for (int i = 52; i <= 54; i++)
        cube[i] = 7;
    cube[56] = 7;
    cube[60] = 7;
    cube[61] = 7;
    cube[65] = 7;
    cube[66] = 7;
    cube[70] = 7;
    for (int i = 72; i <= 74; i++)
        cube[i] = 7;

    // Right
    for (int i = 77; i <= 79; i++)
        cube[i] = 7;
    cube[81] = 7;
    cube[85] = 7;
    cube[86] = 7;
    cube[90] = 7;
    cube[91] = 7;
    cube[95] = 7;
    for (int i = 97; i <= 99; i++)
        cube[i] = 7;

    // Back
    for (int i = 102; i <= 104; i++)
        cube[i] = 7;
    cube[106] = 7;
    cube[110] = 7;
    cube[111] = 7;
    cube[115] = 7;
    cube[116] = 7;
    cube[120] = 7;
    for (int i = 122; i <= 124; i++)
        cube[i] = 7;

    // Down
    for (int i = 127; i <= 129; i++)
        cube[i] = 7;
    cube[131] = 7;
    cube[135] = 7;
    cube[136] = 7;
    cube[140] = 7;
    cube[141] = 7;
    cube[145] = 7;
    for (int i = 147; i <= 149; i++)
        cube[i] = 7;
}

void
nuke_cube_centers_555(int *cube)
{
    // Upper
    for (int i = 7; i <= 9; i++)
        cube[i] = 7;
    for (int i = 12; i <= 14; i++)
        cube[i] = 7;
    for (int i = 17; i <= 19; i++)
        cube[i] = 7;

    // Left
    for (int i = 32; i <= 34; i++)
        cube[i] = 7;
    for (int i = 37; i <= 39; i++)
        cube[i] = 7;
    for (int i = 42; i <= 44; i++)
        cube[i] = 7;

    // Front
    for (int i = 57; i <= 59; i++)
        cube[i] = 7;
    for (int i = 62; i <= 64; i++)
        cube[i] = 7;
    for (int i = 67; i <= 69; i++)
        cube[i] = 7;

    // Right
    for (int i = 82; i <= 84; i++)
        cube[i] = 7;
    for (int i = 87; i <= 89; i++)
        cube[i] = 7;
    for (int i = 92; i <= 94; i++)
        cube[i] = 7;

    // Back
    for (int i = 107; i <= 109; i++)
        cube[i] = 7;
    for (int i = 112; i <= 114; i++)
        cube[i] = 7;
    for (int i = 117; i <= 119; i++)
        cube[i] = 7;

    // Down
    for (int i = 132; i <= 134; i++)
        cube[i] = 7;
    for (int i = 137; i <= 139; i++)
        cube[i] = 7;
    for (int i = 142; i <= 144; i++)
        cube[i] = 7;
}

void
nuke_cube_corners_666(int *cube)
{
    // Upper corners
    cube[1] = 7;
    cube[6] = 7;
    cube[31] = 7;
    cube[32] = 7;

    // Left corners
    cube[37] = 7;
    cube[42] = 7;
    cube[67] = 7;
    cube[72] = 7;

    // Front corners
    cube[73] = 7;
    cube[78] = 7;
    cube[103] = 7;
    cube[108] = 7;

    // Right corners
    cube[109] = 7;
    cube[114] = 7;
    cube[139] = 7;
    cube[144] = 7;

    // Back corners
    cube[145] = 7;
    cube[150] = 7;
    cube[175] = 7;
    cube[180] = 7;

    // Down corners
    cube[181] = 7;
    cube[186] = 7;
    cube[211] = 7;
    cube[216] = 7;
}

void
nuke_cube_edges_666(int *cube)
{
    // Upper
    for (int i = 2; i <= 5; i++)
        cube[i] = 7;
    cube[7] = 7;
    cube[13] = 7;
    cube[19] = 7;
    cube[25] = 7;
    cube[12] = 7;
    cube[18] = 7;
    cube[24] = 7;
    cube[30] = 7;
    for (int i = 32; i <= 35; i++)
        cube[i] = 7;

    // Left
    for (int i = 38; i <= 41; i++)
        cube[i] = 7;
    cube[43] = 7;
    cube[49] = 7;
    cube[55] = 7;
    cube[61] = 7;
    cube[48] = 7;
    cube[54] = 7;
    cube[60] = 7;
    cube[66] = 7;
    for (int i = 68; i <= 71; i++)
        cube[i] = 7;

    // Front
    for (int i = 74; i <= 77; i++)
        cube[i] = 7;
    cube[79] = 7;
    cube[85] = 7;
    cube[91] = 7;
    cube[97] = 7;
    cube[84] = 7;
    cube[90] = 7;
    cube[96] = 7;
    cube[102] = 7;
    for (int i = 104; i <= 107; i++)
        cube[i] = 7;

    // Right
    for (int i = 110; i <= 113; i++)
        cube[i] = 7;
    cube[115] = 7;
    cube[121] = 7;
    cube[127] = 7;
    cube[133] = 7;
    cube[120] = 7;
    cube[126] = 7;
    cube[132] = 7;
    cube[138] = 7;
    for (int i = 140; i <= 143; i++)
        cube[i] = 7;

    // Back
    for (int i = 146; i <= 149; i++)
        cube[i] = 7;
    cube[151] = 7;
    cube[157] = 7;
    cube[163] = 7;
    cube[169] = 7;
    cube[156] = 7;
    cube[162] = 7;
    cube[168] = 7;
    cube[174] = 7;
    for (int i = 176; i <= 179; i++)
        cube[i] = 7;

    // Down
    for (int i = 182; i <= 185; i++)
        cube[i] = 7;
    cube[187] = 7;
    cube[193] = 7;
    cube[199] = 7;
    cube[205] = 7;
    cube[192] = 7;
    cube[198] = 7;
    cube[204] = 7;
    cube[210] = 7;
    for (int i = 212; i <= 215; i++)
        cube[i] = 7;
}


void
nuke_cube_corners_777(int *cube)
{
    // Upper corners
    cube[1] = 7;
    cube[7] = 7;
    cube[43] = 7;
    cube[49] = 7;

    // Left corners
    cube[50] = 7;
    cube[56] = 7;
    cube[92] = 7;
    cube[98] = 7;

    // Front corners
    cube[99] = 7;
    cube[105] = 7;
    cube[141] = 7;
    cube[147] = 7;

    // Right corners
    cube[148] = 7;
    cube[154] = 7;
    cube[190] = 7;
    cube[196] = 7;

    // Back corners
    cube[197] = 7;
    cube[203] = 7;
    cube[239] = 7;
    cube[245] = 7;

    // Down corners
    cube[246] = 7;
    cube[252] = 7;
    cube[288] = 7;
    cube[294] = 7;
}

void
nuke_cube_edges_777(int *cube)
{
    // Upper
    for (int i = 2; i <= 6; i++)
        cube[i] = 7;
    cube[8] = 7;
    cube[15] = 7;
    cube[22] = 7;
    cube[29] = 7;
    cube[36] = 7;
    cube[14] = 7;
    cube[21] = 7;
    cube[28] = 7;
    cube[35] = 7;
    cube[42] = 7;
    for (int i = 44; i <= 48; i++)
        cube[i] = 7;

    // Left
    for (int i = 51; i <= 55; i++)
        cube[i] = 7;
    cube[57] = 7;
    cube[64] = 7;
    cube[71] = 7;
    cube[78] = 7;
    cube[85] = 7;
    cube[63] = 7;
    cube[70] = 7;
    cube[77] = 7;
    cube[84] = 7;
    cube[91] = 7;
    for (int i = 93; i <= 97; i++)
        cube[i] = 7;

    // Front
    for (int i = 100; i <= 104; i++)
        cube[i] = 7;
    cube[106] = 7;
    cube[113] = 7;
    cube[120] = 7;
    cube[127] = 7;
    cube[134] = 7;
    cube[112] = 7;
    cube[119] = 7;
    cube[126] = 7;
    cube[133] = 7;
    cube[140] = 7;
    for (int i = 142; i <= 146; i++)
        cube[i] = 7;

    // Right
    for (int i = 149; i <= 153; i++)
        cube[i] = 7;
    cube[155] = 7;
    cube[162] = 7;
    cube[169] = 7;
    cube[176] = 7;
    cube[183] = 7;
    cube[161] = 7;
    cube[168] = 7;
    cube[175] = 7;
    cube[182] = 7;
    cube[189] = 7;
    for (int i = 191; i <= 195; i++)
        cube[i] = 7;

    // Back
    for (int i = 198; i <= 202; i++)
        cube[i] = 7;
    cube[204] = 7;
    cube[211] = 7;
    cube[218] = 7;
    cube[225] = 7;
    cube[232] = 7;
    cube[210] = 7;
    cube[217] = 7;
    cube[224] = 7;
    cube[231] = 7;
    cube[238] = 7;
    for (int i = 240; i <= 244; i++)
        cube[i] = 7;

    // Down
    for (int i = 247; i <= 251; i++)
        cube[i] = 7;
    cube[253] = 7;
    cube[260] = 7;
    cube[267] = 7;
    cube[274] = 7;
    cube[281] = 7;
    cube[259] = 7;
    cube[266] = 7;
    cube[273] = 7;
    cube[280] = 7;
    cube[287] = 7;
    for (int i = 289; i <= 293; i++)
        cube[i] = 7;
}

int
get_token_count(char *str)
{
    int count = 1;
    int i;

    for (i = 0; i < strlen(str); i++) {
        if (str[i] == ' ') {
            count++;
        }
    }

    return count;
}

/*
 * U is 1
 * L is 2
 * F is 3
 * R is 4
 * B is 5
 * D is 6
 * x is 7
 */
char *
side_name(int side_number)
{
    switch (side_number) {
    case 1:
        return "U";
    case 2:
        return "L";
    case 3:
        return "F";
    case 4:
        return "R";
    case 5:
        return "B";
    case 6:
        return "D";
    case 7:
        return "x";
    default:
        printf("Invalid side_number %d", side_number);
        exit(1);
    }
}

void
populate_777_LFRB_inner_x_centers(int *cube)
{
    // 66, 68, 74, 80, 82, 115, 117, 123, 129, 131, 164, 166, 172, 178, 180, 213, 215, 221, 227, 229

    // Left
    cube[66] = 2;
    cube[68] = 2;
    cube[74] = 2;
    cube[80] = 2;
    cube[82] = 2;

    // Front
    cube[115] = 3;
    cube[117] = 3;
    cube[123] = 3;
    cube[129] = 3;
    cube[131] = 3;

    // Right
    cube[164] = 4;
    cube[166] = 4;
    cube[172] = 4;
    cube[178] = 4;
    cube[180] = 4;

    // Back
    cube[213] = 5;
    cube[215] = 5;
    cube[221] = 5;
    cube[227] = 5;
    cube[229] = 5;
}


void
populate_777_LFRB_inner_t_centers(int *cube)
{
    // 67, 73, 74, 75, 81, 116, 122, 123, 124, 130, 165, 171, 172, 173, 179, 214, 220, 221, 222, 228

    // Left
    cube[67] = 2;
    cube[73] = 2;
    cube[74] = 2;
    cube[75] = 2;
    cube[81] = 2;

    // Front
    cube[116] = 3;
    cube[122] = 3;
    cube[123] = 3;
    cube[124] = 3;
    cube[130] = 3;

    // Right
    cube[165] = 4;
    cube[171] = 4;
    cube[172] = 4;
    cube[173] = 4;
    cube[179] = 4;

    // Back
    cube[214] = 5;
    cube[220] = 5;
    cube[221] = 5;
    cube[222] = 5;
    cube[228] = 5;
}

void
populate_777_LFRB_left_oblique_edges(int *cube)
{
    // 59, 69, 79, 89, 108, 118, 128, 138, 157, 167, 177, 187, 206, 216, 226, 236

    // Left
    cube[59] = 2;
    cube[69] = 2;
    cube[79] = 2;
    cube[89] = 2;

    // Front
    cube[108] = 3;
    cube[118] = 3;
    cube[128] = 3;
    cube[138] = 3;

    // Right
    cube[157] = 4;
    cube[167] = 4;
    cube[177] = 4;
    cube[187] = 4;

    // Back
    cube[206] = 5;
    cube[216] = 5;
    cube[226] = 5;
    cube[236] = 5;
}

void
populate_777_LFRB_middle_oblique_edges(int *cube)
{
    // 60, 72, 76, 88, 109, 121, 125, 137, 158, 170, 174, 186, 207, 219, 223, 235

    // Left
    cube[60] = 2;
    cube[72] = 2;
    cube[76] = 2;
    cube[88] = 2;

    // Front
    cube[109] = 3;
    cube[121] = 3;
    cube[125] = 3;
    cube[137] = 3;

    // Right
    cube[158] = 4;
    cube[170] = 4;
    cube[174] = 4;
    cube[186] = 4;

    // Back
    cube[207] = 5;
    cube[219] = 5;
    cube[223] = 5;
    cube[235] = 5;
}


void
populate_777_LFRB_right_oblique_edges(int *cube)
{
    // 61, 83, 87, 65, 110, 132, 136, 114, 159, 181, 185, 163, 208, 230, 234, 212

    // Left
    cube[61] = 2;
    cube[83] = 2;
    cube[87] = 2;
    cube[65] = 2;

    // Front
    cube[110] = 3;
    cube[132] = 3;
    cube[136] = 3;
    cube[114] = 3;

    // Right
    cube[159] = 4;
    cube[181] = 4;
    cube[185] = 4;
    cube[163] = 4;

    // Back
    cube[208] = 5;
    cube[230] = 5;
    cube[234] = 5;
    cube[212] = 5;
}


int
main (int argc, char *argv[])
{
    // open a read file called workq.txt
    // open a write file called workq-results.txt
    // For every line in workq.txt, run those steps and write the results to workq-results.txt
    FILE *fh_read = NULL;
    FILE *fh_write = NULL;
    char steps_buffer[255];
    char token_steps_buffer[255];
    char *token_ptr = NULL;
    int cube_size = 0;
    int state = 1;
    int token_index = 0;
    int token_count = 0;
    int start_line = 0;
    int end_line = 0;
    int current_line = 0;
    char input_filename[100];
    char output_filename[100];
    char option[100];
    memset(input_filename, 0, sizeof(char) * 100);
    memset(output_filename, 0, sizeof(char) * 100);
    memset(option, 0, sizeof(char) * 100);
    lookup_table_type type = NONE;

    for (int i = 1; i < argc; i++) {
        if (strmatch(argv[i], "-i") || strmatch(argv[i], "--input")) {
            i++;
            strcpy(input_filename, argv[i]);

        } else if (strmatch(argv[i], "-o") || strmatch(argv[i], "--output")) {
            i++;
            strcpy(output_filename, argv[i]);

        } else if (strmatch(argv[i], "--start")) {
            i++;
            start_line = atoi(argv[i]);

        } else if (strmatch(argv[i], "--end")) {
            i++;
            end_line = atoi(argv[i]);

        } else if (strmatch(argv[i], "--type")) {
            i++;

            // 4x4x4 centers
            if (strmatch(argv[i], "4x4x4-ULFRBD-centers-solve") ||
                       strmatch(argv[i], "4x4x4-ULFRBD-centers-solve-with-edges-oriented")) {
                type = ULFRBD_CENTERS_SOLVE_444;
                cube_size = 4;

            } else if (strmatch(argv[i], "4x4x4-edges")) {
                type = EDGES_444;
                cube_size = 4;

            // 5x5x5 solve centers
            } else if (strmatch(argv[i], "5x5x5-ULFRBD-t-centers-solve")) {
                type = ULFRBD_T_CENTERS_SOLVE_555;
                cube_size = 5;

            } else if (strmatch(argv[i], "5x5x5-LR-t-centers-solve")) {
                type = LR_T_CENTERS_SOLVE_555;
                cube_size = 5;

            } else if (strmatch(argv[i], "5x5x5-UL-centers-solve")) {
                type = UL_CENTERS_SOLVE_555;
                cube_size = 5;

            } else if (strmatch(argv[i], "5x5x5-UF-centers-solve")) {
                type = UF_CENTERS_SOLVE_555;
                cube_size = 5;

            } else if (strmatch(argv[i], "5x5x5-ULFRBD-centers-solve-unstaged")) {
                type = ULFRBD_CENTERS_SOLVE_UNSTAGED_555;
                cube_size = 5;

            } else if (strmatch(argv[i], "5x5x5-stage-first-four-edges")) {
                type = EDGES_STAGE_FIRST_FOUR_555;
                cube_size = 5;

            } else if (strmatch(argv[i], "5x5x5-stage-second-four-edges")) {
                type = EDGES_STAGE_SECOND_FOUR_555;
                cube_size = 5;

            } else if (strmatch(argv[i], "5x5x5-pair-last-four-edges")) {
                type = EDGES_PAIR_LAST_FOUR_555;
                cube_size = 5;

            // 7x7x7 centers
            } else if (strmatch(argv[i], "7x7x7-UD-oblique-edge-pairing")) {
                type = UD_OBLIQUE_EDGE_PAIRING_777;
                cube_size = 7;

            } else if (strmatch(argv[i], "7x7x7-UD-oblique-edge-pairing-middle-only")) {
                type = UD_OBLIQUE_EDGE_PAIRING_MIDDLE_ONLY_777;
                cube_size = 7;

            } else if (strmatch(argv[i], "7x7x7-UD-oblique-edge-pairing-left-only")) {
                type = UD_OBLIQUE_EDGE_PAIRING_LEFT_ONLY_777;
                cube_size = 7;

            } else if (strmatch(argv[i], "7x7x7-UD-oblique-edge-pairing-right-only")) {
                type = UD_OBLIQUE_EDGE_PAIRING_RIGHT_ONLY_777;
                cube_size = 7;

            } else {
                printf("%s is an invalid --type\n", argv[i]);
                exit(1);
            }

        } else if (strmatch(argv[i], "--option")) {
            i++;
            strcpy(option, argv[i]);

        } else if (strmatch(argv[i], "-h") || strmatch(argv[i], "--help")) {
            printf("\n    rotate --input INPUT_FILENAME --output OUTPUT_FILENAME\n\n");
            exit(0);
        }
    }

    if (argc < 7 || strmatch(input_filename, "") || strmatch(output_filename, "") || type == NONE) {
        printf("ERROR, to use:\n\n");
        printf("    rotate --input INPUT_FILENAME --output OUTPUT_FILENAME --type TYPE\n\n");
        exit(1);
    }

    int center_size = (cube_size  - 2) * (cube_size - 2);
    int array_size = (cube_size * cube_size * 6) + 2;
    int cube[array_size];
    int cube_original[array_size];
    int cube_tmp[array_size];
    int cube_prev_minus_last_step[array_size];
    int cube_state[cube_size * cube_size * 6];
    char cube_state_str[cube_size * cube_size * 6];
    int center_state[center_size];
    char center_state_str[center_size];

    memset(cube_tmp, 0, sizeof(int) * array_size);
    memset(cube_prev_minus_last_step, 0, sizeof(int) * array_size);

    printf("cube size %d, array_size %d\n", cube_size, array_size);
    init_cube(cube, cube_size, type);

    fh_read = fopen(input_filename, "r");
    if (fh_read == NULL) {
        printf("ERROR: could not open %s\n", input_filename);
        exit(1);
    }

    fh_write = fopen(output_filename, "w");
    if (fh_write == NULL) {
        printf("ERROR: could not open %s\n", output_filename);
        fclose(fh_read);
        exit(1);
    }

    /*
     * U is 1
     * L is 2
     * F is 3
     * R is 4
     * B is 5
     * D is 6
     * x is 7
     */

    if (type == ULFRBD_CENTERS_SOLVE_444) {
        nuke_cube_corners_444(cube);
        nuke_cube_edges_444(cube);
        nuke_cube_centers_444(cube);

        // Upper
        cube[6] = 1;
        cube[7] = 1;
        cube[10] = 1;
        cube[11] = 1;

        // Left
        cube[22] = 2;
        cube[23] = 2;
        cube[26] = 2;
        cube[27] = 2;

        // Front
        cube[38] = 3;
        cube[39] = 3;
        cube[42] = 3;
        cube[43] = 3;

        // Right
        cube[54] = 4;
        cube[55] = 4;
        cube[58] = 4;
        cube[59] = 4;

        // Back
        cube[70] = 5;
        cube[71] = 5;
        cube[74] = 5;
        cube[75] = 5;

        // Down
        cube[86] = 6;
        cube[87] = 6;
        cube[90] = 6;
        cube[91] = 6;

    // 4x4x4 edges
    } else if (type == EDGES_444) {
        nuke_cube_corners_444(cube);

    // 5x5x5
    } else if (type == ULFRBD_T_CENTERS_SOLVE_555) {
        nuke_cube_corners_555(cube);
        nuke_cube_edges_555(cube);

        // Nuke the x-centers
        // Upper
        cube[7] = 7;
        cube[9] = 7;
        cube[17] = 7;
        cube[19] = 7;

        // Left
        cube[32] = 7;
        cube[34] = 7;
        cube[42] = 7;
        cube[44] = 7;

        // Front
        cube[57] = 7;
        cube[59] = 7;
        cube[67] = 7;
        cube[69] = 7;

        // Right
        cube[82] = 7;
        cube[84] = 7;
        cube[92] = 7;
        cube[94] = 7;

        // Back
        cube[107] = 7;
        cube[109] = 7;
        cube[117] = 7;
        cube[119] = 7;

        // Down
        cube[132] = 7;
        cube[134] = 7;
        cube[142] = 7;
        cube[144] = 7;

    } else if (type == LR_T_CENTERS_SOLVE_555) {
        nuke_cube_corners_555(cube);
        nuke_cube_edges_555(cube);
        nuke_cube_centers_555(cube);

        // Left
        cube[33] = 2;
        cube[37] = 2;
        cube[38] = 2;
        cube[39] = 2;
        cube[43] = 2;

        // Right
        cube[83] = 4;
        cube[87] = 4;
        cube[88] = 4;
        cube[89] = 4;
        cube[93] = 4;

    } else if (type == UL_CENTERS_SOLVE_555) {
        nuke_cube_corners_555(cube);
        nuke_cube_edges_555(cube);

        // Make the Ls -> Us, this looks odd but we do this so the table
        // can be saved as hex which saves a lot of space
        cube[32] = 1;
        cube[33] = 1;
        cube[34] = 1;
        cube[37] = 1;
        cube[38] = 1;
        cube[39] = 1;
        cube[42] = 1;
        cube[43] = 1;
        cube[44] = 1;

        // Nuke front, right, back and down
        for (int i = 51; i <= 150; i++)
            cube[i] = 7;

    } else if (type == UF_CENTERS_SOLVE_555) {
        nuke_cube_corners_555(cube);
        nuke_cube_edges_555(cube);

        // Make the Fs -> Us, this looks odd but we do this so the table
        // can be saved as hex which saves a lot of space
        cube[57] = 1;
        cube[58] = 1;
        cube[59] = 1;
        cube[62] = 1;
        cube[63] = 1;
        cube[64] = 1;
        cube[67] = 1;
        cube[68] = 1;
        cube[69] = 1;

        // Nuke left
        for (int i = 26; i <= 50; i++)
            cube[i] = 7;

        // Nuke right, back and down
        for (int i = 76; i <= 150; i++)
            cube[i] = 7;

    } else if (type == EDGES_STAGE_FIRST_FOUR_555) {

        nuke_cube_corners_555(cube);
        nuke_cube_edges_555(cube);

        // Left
        cube[31] = 2;
        cube[36] = 2;
        cube[41] = 2;
        cube[35] = 2;
        cube[40] = 2;
        cube[45] = 2;

        // Front
        cube[56] = 2;
        cube[61] = 2;
        cube[66] = 2;
        cube[60] = 2;
        cube[65] = 2;
        cube[70] = 2;

        // Right
        cube[81] = 2;
        cube[86] = 2;
        cube[91] = 2;
        cube[85] = 2;
        cube[90] = 2;
        cube[95] = 2;

        // Back
        cube[106] = 2;
        cube[111] = 2;
        cube[116] = 2;
        cube[110] = 2;
        cube[115] = 2;
        cube[120] = 2;

    } else if (type == EDGES_STAGE_SECOND_FOUR_555) {

        nuke_cube_corners_555(cube);
        nuke_cube_edges_555(cube);

        // Upper/Back
        cube[2] = 1;
        cube[3] = 1;
        cube[4] = 1;
        cube[102] = 1;
        cube[103] = 1;
        cube[104] = 1;

        // Upper/Front
        cube[22] = 1;
        cube[23] = 1;
        cube[24] = 1;
        cube[52] = 1;
        cube[53] = 1;
        cube[54] = 1;

        // Down/Front
        cube[72] = 1;
        cube[73] = 1;
        cube[74] = 1;
        cube[127] = 1;
        cube[128] = 1;
        cube[129] = 1;

        // Down/Back
        cube[147] = 1;
        cube[148] = 1;
        cube[149] = 1;
        cube[122] = 1;
        cube[123] = 1;
        cube[124] = 1;

    } else if (type == EDGES_PAIR_LAST_FOUR_555) {
        nuke_cube_corners_555(cube);

    } else if (type == UD_OBLIQUE_EDGE_PAIRING_777) {

        // Nuke everything and repopulate the squares we care about
        for (int i = 1; i <= 294; i++)
            cube[i] = 7;

        cube[10] = 1;
        cube[11] = 1;
        cube[12] = 1;
        cube[16] = 1;
        cube[20] = 1;
        cube[23] = 1;
        cube[27] = 1;
        cube[30] = 1;
        cube[34] = 1;
        cube[38] = 1;
        cube[39] = 1;
        cube[40] = 1;

        cube[255] = 1;
        cube[256] = 1;
        cube[257] = 1;
        cube[261] = 1;
        cube[265] = 1;
        cube[268] = 1;
        cube[272] = 1;
        cube[275] = 1;
        cube[279] = 1;
        cube[283] = 1;
        cube[284] = 1;
        cube[285] = 1;

    } else if (type == UD_OBLIQUE_EDGE_PAIRING_MIDDLE_ONLY_777) {

        // Nuke everything and repopulate the squares we care about
        for (int i = 1; i <= 294; i++)
            cube[i] = 7;

        cube[11] = 1;
        cube[23] = 1;
        cube[27] = 1;
        cube[39] = 1;

        cube[256] = 1;
        cube[268] = 1;
        cube[272] = 1;
        cube[284] = 1;

    } else if (type == UD_OBLIQUE_EDGE_PAIRING_LEFT_ONLY_777) {

        // Nuke everything and repopulate the squares we care about
        for (int i = 1; i <= 294; i++)
            cube[i] = 7;

        cube[10] = 1;
        cube[20] = 1;
        cube[40] = 1;
        cube[30] = 1;

        cube[255] = 1;
        cube[265] = 1;
        cube[285] = 1;
        cube[275] = 1;

    } else if (type == UD_OBLIQUE_EDGE_PAIRING_RIGHT_ONLY_777) {

        // Nuke everything and repopulate the squares we care about
        for (int i = 1; i <= 294; i++)
            cube[i] = 7;

        cube[12] = 1;
        cube[34] = 1;
        cube[38] = 1;
        cube[16] = 1;

        cube[257] = 1;
        cube[279] = 1;
        cube[283] = 1;
        cube[261] = 1;

    /*
     * U is 1
     * L is 2
     * F is 3
     * R is 4
     * B is 5
     * D is 6
     * x is 7
     */
    } else {
        printf("Implement type == %d\n", type);
        exit(1);
    }

    memcpy(cube_original, cube, sizeof(int) * array_size);

    while (fgets(steps_buffer, 255, fh_read) != NULL) {

        // chop the newline
        steps_buffer[strlen(steps_buffer)-1] = '\0';

        // printf("LINE:s\n", steps_buffer);

        if (strcmp(steps_buffer, "INIT") == 0) {
            current_line++;
            state = 1;
            continue;
        }

        if (end_line > 0) {
            if (current_line < start_line) {
                current_line++;
                continue;
            }
            if (current_line > end_line) {
                break;
            }
        }

        // strtok modifies the buffer so make a copy
        strcpy(token_steps_buffer, steps_buffer);
        token_index = 1;
        token_count = get_token_count(token_steps_buffer);
        token_ptr = strtok(token_steps_buffer, " ");

        // state 1 means we need to re-init the cube
        if (state == 1 || token_count == 1) {
            memcpy(cube, cube_original, sizeof(int) * array_size);
            memset(cube_prev_minus_last_step, 0, sizeof(int) * array_size);
            state = 0;

            // Execute the steps in the line
            while (token_ptr != NULL) {
                // printf ("%s\n", token_ptr);

                if (cube_size == 2) {
                    rotate_222(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 3) {
                    rotate_333(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 4) {
                    rotate_444(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 5) {
                    rotate_555(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 6) {
                    rotate_666(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 7) {
                    rotate_777(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 8) {
                    rotate_888(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 9) {
                    rotate_999(cube, cube_tmp, array_size, token_ptr);

                } else if (cube_size == 10) {
                    rotate_101010(cube, cube_tmp, array_size, token_ptr);

                } else {
                    printf("Implement rotate_xxx() for cube size %d", cube_size);
                    exit(1);
                }

                if (token_index == token_count - 1) {
                    memcpy(cube_prev_minus_last_step, cube, sizeof(int) * array_size);
                }

                token_index++;
                token_ptr = strtok(NULL, " ");
            }

        // state 0 means we re-use the cube state from before and only do the last step
        } else {
            memcpy(cube, cube_prev_minus_last_step, sizeof(int) * array_size);

            // Only execute the last step
            while (token_ptr != NULL) {

                if (token_index == token_count) {
                    if (cube_size == 2) {
                        rotate_222(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 3) {
                        rotate_333(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 4) {
                        rotate_444(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 5) {
                        rotate_555(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 6) {
                        rotate_666(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 7) {
                        rotate_777(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 8) {
                        rotate_888(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 9) {
                        rotate_999(cube, cube_tmp, array_size, token_ptr);

                    } else if (cube_size == 10) {
                        rotate_101010(cube, cube_tmp, array_size, token_ptr);

                    } else {
                        printf("Implement 'Only execute the last step' for cube size %d", cube_size);
                        exit(1);
                    }
                }

                token_index++;
                token_ptr = strtok(NULL, " ");
            }
        }

        // keep it simple, print the entire cube and let process-workq-results.py
        // extract the parts that it cares about
        if (cube_size == 2) {
            sprintf(cube_state_str,
                "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s",
                side_name(cube[1]), side_name(cube[2]),
                side_name(cube[3]), side_name(cube[4]),
                side_name(cube[5]), side_name(cube[6]),
                side_name(cube[7]), side_name(cube[8]),
                side_name(cube[9]), side_name(cube[10]),
                side_name(cube[11]), side_name(cube[12]),
                side_name(cube[13]), side_name(cube[14]),
                side_name(cube[15]), side_name(cube[16]),
                side_name(cube[17]), side_name(cube[18]),
                side_name(cube[19]), side_name(cube[20]),
                side_name(cube[21]), side_name(cube[22]),
                side_name(cube[23]), side_name(cube[24]));

            fprintf(fh_write, "%s:%s\n", cube_state_str, steps_buffer);

        } else if (cube_size == 3) {
            sprintf(cube_state_str,
                "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s",
                side_name(cube[1]), side_name(cube[2]), side_name(cube[3]),
                side_name(cube[4]), side_name(cube[5]), side_name(cube[6]),
                side_name(cube[7]), side_name(cube[8]), side_name(cube[9]),
                side_name(cube[10]), side_name(cube[11]), side_name(cube[12]),
                side_name(cube[13]), side_name(cube[14]), side_name(cube[15]),
                side_name(cube[16]), side_name(cube[17]), side_name(cube[18]),
                side_name(cube[19]), side_name(cube[20]), side_name(cube[21]),
                side_name(cube[22]), side_name(cube[23]), side_name(cube[24]),
                side_name(cube[25]), side_name(cube[26]), side_name(cube[27]),
                side_name(cube[28]), side_name(cube[29]), side_name(cube[30]),
                side_name(cube[31]), side_name(cube[32]), side_name(cube[33]),
                side_name(cube[34]), side_name(cube[35]), side_name(cube[36]),
                side_name(cube[37]), side_name(cube[38]), side_name(cube[39]),
                side_name(cube[40]), side_name(cube[41]), side_name(cube[42]),
                side_name(cube[43]), side_name(cube[44]), side_name(cube[45]),
                side_name(cube[46]), side_name(cube[47]), side_name(cube[48]),
                side_name(cube[49]), side_name(cube[50]), side_name(cube[51]),
                side_name(cube[52]), side_name(cube[53]), side_name(cube[54]));

            fprintf(fh_write, "%s:%s\n", cube_state_str, steps_buffer);

        } else if (cube_size == 4) {

            sprintf(cube_state_str,
                "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s",
                side_name(cube[1]), side_name(cube[2]), side_name(cube[3]), side_name(cube[4]),
                side_name(cube[5]), side_name(cube[6]), side_name(cube[7]), side_name(cube[8]),
                side_name(cube[9]), side_name(cube[10]), side_name(cube[11]), side_name(cube[12]),
                side_name(cube[13]), side_name(cube[14]), side_name(cube[15]), side_name(cube[16]),
                side_name(cube[17]), side_name(cube[18]), side_name(cube[19]), side_name(cube[20]),
                side_name(cube[21]), side_name(cube[22]), side_name(cube[23]), side_name(cube[24]),
                side_name(cube[25]), side_name(cube[26]), side_name(cube[27]), side_name(cube[28]),
                side_name(cube[29]), side_name(cube[30]), side_name(cube[31]), side_name(cube[32]),
                side_name(cube[33]), side_name(cube[34]), side_name(cube[35]), side_name(cube[36]),
                side_name(cube[37]), side_name(cube[38]), side_name(cube[39]), side_name(cube[40]),
                side_name(cube[41]), side_name(cube[42]), side_name(cube[43]), side_name(cube[44]),
                side_name(cube[45]), side_name(cube[46]), side_name(cube[47]), side_name(cube[48]),
                side_name(cube[49]), side_name(cube[50]), side_name(cube[51]), side_name(cube[52]),
                side_name(cube[53]), side_name(cube[54]), side_name(cube[55]), side_name(cube[56]),
                side_name(cube[57]), side_name(cube[58]), side_name(cube[59]), side_name(cube[60]),
                side_name(cube[61]), side_name(cube[62]), side_name(cube[63]), side_name(cube[64]),
                side_name(cube[65]), side_name(cube[66]), side_name(cube[67]), side_name(cube[68]),
                side_name(cube[69]), side_name(cube[70]), side_name(cube[71]), side_name(cube[72]),
                side_name(cube[73]), side_name(cube[74]), side_name(cube[75]), side_name(cube[76]),
                side_name(cube[77]), side_name(cube[78]), side_name(cube[79]), side_name(cube[80]),
                side_name(cube[81]), side_name(cube[82]), side_name(cube[83]), side_name(cube[84]),
                side_name(cube[85]), side_name(cube[86]), side_name(cube[87]), side_name(cube[88]),
                side_name(cube[89]), side_name(cube[90]), side_name(cube[91]), side_name(cube[92]),
                side_name(cube[93]), side_name(cube[94]), side_name(cube[95]), side_name(cube[96]));

            fprintf(fh_write, "%s:%s\n", cube_state_str, steps_buffer);

        } else if (cube_size == 5) {
            sprintf(cube_state_str,
                "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s",
                side_name(cube[1]), side_name(cube[2]), side_name(cube[3]), side_name(cube[4]), side_name(cube[5]),
                side_name(cube[6]), side_name(cube[7]), side_name(cube[8]), side_name(cube[9]), side_name(cube[10]),
                side_name(cube[11]), side_name(cube[12]), side_name(cube[13]), side_name(cube[14]), side_name(cube[15]),
                side_name(cube[16]), side_name(cube[17]), side_name(cube[18]), side_name(cube[19]), side_name(cube[20]),
                side_name(cube[21]), side_name(cube[22]), side_name(cube[23]), side_name(cube[24]), side_name(cube[25]),

                side_name(cube[26]), side_name(cube[27]), side_name(cube[28]), side_name(cube[29]), side_name(cube[30]),
                side_name(cube[31]), side_name(cube[32]), side_name(cube[33]), side_name(cube[34]), side_name(cube[35]),
                side_name(cube[36]), side_name(cube[37]), side_name(cube[38]), side_name(cube[39]), side_name(cube[40]),
                side_name(cube[41]), side_name(cube[42]), side_name(cube[43]), side_name(cube[44]), side_name(cube[45]),
                side_name(cube[46]), side_name(cube[47]), side_name(cube[48]), side_name(cube[49]), side_name(cube[50]),

                side_name(cube[51]), side_name(cube[52]), side_name(cube[53]), side_name(cube[54]), side_name(cube[55]),
                side_name(cube[56]), side_name(cube[57]), side_name(cube[58]), side_name(cube[59]), side_name(cube[60]),
                side_name(cube[61]), side_name(cube[62]), side_name(cube[63]), side_name(cube[64]), side_name(cube[65]),
                side_name(cube[66]), side_name(cube[67]), side_name(cube[68]), side_name(cube[69]), side_name(cube[70]),
                side_name(cube[71]), side_name(cube[72]), side_name(cube[73]), side_name(cube[74]), side_name(cube[75]),

                side_name(cube[76]), side_name(cube[77]), side_name(cube[78]), side_name(cube[79]), side_name(cube[80]),
                side_name(cube[81]), side_name(cube[82]), side_name(cube[83]), side_name(cube[84]), side_name(cube[85]),
                side_name(cube[86]), side_name(cube[87]), side_name(cube[88]), side_name(cube[89]), side_name(cube[90]),
                side_name(cube[91]), side_name(cube[92]), side_name(cube[93]), side_name(cube[94]), side_name(cube[95]),
                side_name(cube[96]), side_name(cube[97]), side_name(cube[98]), side_name(cube[99]), side_name(cube[100]),

                side_name(cube[101]), side_name(cube[102]), side_name(cube[103]), side_name(cube[104]), side_name(cube[105]),
                side_name(cube[106]), side_name(cube[107]), side_name(cube[108]), side_name(cube[109]), side_name(cube[110]),
                side_name(cube[111]), side_name(cube[112]), side_name(cube[113]), side_name(cube[114]), side_name(cube[115]),
                side_name(cube[116]), side_name(cube[117]), side_name(cube[118]), side_name(cube[119]), side_name(cube[120]),
                side_name(cube[121]), side_name(cube[122]), side_name(cube[123]), side_name(cube[124]), side_name(cube[125]),

                side_name(cube[126]), side_name(cube[127]), side_name(cube[128]), side_name(cube[129]), side_name(cube[130]),
                side_name(cube[131]), side_name(cube[132]), side_name(cube[133]), side_name(cube[134]), side_name(cube[135]),
                side_name(cube[136]), side_name(cube[137]), side_name(cube[138]), side_name(cube[139]), side_name(cube[140]),
                side_name(cube[141]), side_name(cube[142]), side_name(cube[143]), side_name(cube[144]), side_name(cube[145]),
                side_name(cube[146]), side_name(cube[147]), side_name(cube[148]), side_name(cube[149]), side_name(cube[150]));

            fprintf(fh_write, "%s:%s\n", cube_state_str, steps_buffer);

        } else if (cube_size == 6) {

            sprintf(cube_state_str,
                "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s",
                side_name(cube[1]), side_name(cube[2]), side_name(cube[3]), side_name(cube[4]), side_name(cube[5]), side_name(cube[6]),
                side_name(cube[7]), side_name(cube[8]), side_name(cube[9]), side_name(cube[10]), side_name(cube[11]), side_name(cube[12]),
                side_name(cube[13]), side_name(cube[14]), side_name(cube[15]), side_name(cube[16]), side_name(cube[17]), side_name(cube[18]),
                side_name(cube[19]), side_name(cube[20]), side_name(cube[21]), side_name(cube[22]), side_name(cube[23]), side_name(cube[24]),
                side_name(cube[25]), side_name(cube[26]), side_name(cube[27]), side_name(cube[28]), side_name(cube[29]), side_name(cube[30]),
                side_name(cube[31]), side_name(cube[32]), side_name(cube[33]), side_name(cube[34]), side_name(cube[35]), side_name(cube[36]),

                side_name(cube[37]), side_name(cube[38]), side_name(cube[39]), side_name(cube[40]), side_name(cube[41]), side_name(cube[42]),
                side_name(cube[43]), side_name(cube[44]), side_name(cube[45]), side_name(cube[46]), side_name(cube[47]), side_name(cube[48]),
                side_name(cube[49]), side_name(cube[50]), side_name(cube[51]), side_name(cube[52]), side_name(cube[53]), side_name(cube[54]),
                side_name(cube[55]), side_name(cube[56]), side_name(cube[57]), side_name(cube[58]), side_name(cube[59]), side_name(cube[60]),
                side_name(cube[61]), side_name(cube[62]), side_name(cube[63]), side_name(cube[64]), side_name(cube[65]), side_name(cube[66]),
                side_name(cube[67]), side_name(cube[68]), side_name(cube[69]), side_name(cube[70]), side_name(cube[71]), side_name(cube[72]),

                side_name(cube[73]), side_name(cube[74]), side_name(cube[75]), side_name(cube[76]), side_name(cube[77]), side_name(cube[78]),
                side_name(cube[79]), side_name(cube[80]), side_name(cube[81]), side_name(cube[82]), side_name(cube[83]), side_name(cube[84]),
                side_name(cube[85]), side_name(cube[86]), side_name(cube[87]), side_name(cube[88]), side_name(cube[89]), side_name(cube[90]),
                side_name(cube[91]), side_name(cube[92]), side_name(cube[93]), side_name(cube[94]), side_name(cube[95]), side_name(cube[96]),
                side_name(cube[97]), side_name(cube[98]), side_name(cube[99]), side_name(cube[100]), side_name(cube[101]), side_name(cube[102]),
                side_name(cube[103]), side_name(cube[104]), side_name(cube[105]), side_name(cube[106]), side_name(cube[107]), side_name(cube[108]),

                side_name(cube[109]), side_name(cube[110]), side_name(cube[111]), side_name(cube[112]), side_name(cube[113]), side_name(cube[114]),
                side_name(cube[115]), side_name(cube[116]), side_name(cube[117]), side_name(cube[118]), side_name(cube[119]), side_name(cube[120]),
                side_name(cube[121]), side_name(cube[122]), side_name(cube[123]), side_name(cube[124]), side_name(cube[125]), side_name(cube[126]),
                side_name(cube[127]), side_name(cube[128]), side_name(cube[129]), side_name(cube[130]), side_name(cube[131]), side_name(cube[132]),
                side_name(cube[133]), side_name(cube[134]), side_name(cube[135]), side_name(cube[136]), side_name(cube[137]), side_name(cube[138]),
                side_name(cube[139]), side_name(cube[140]), side_name(cube[141]), side_name(cube[142]), side_name(cube[143]), side_name(cube[144]),

                side_name(cube[145]), side_name(cube[146]), side_name(cube[147]), side_name(cube[148]), side_name(cube[149]), side_name(cube[150]),
                side_name(cube[151]), side_name(cube[152]), side_name(cube[153]), side_name(cube[154]), side_name(cube[155]), side_name(cube[156]),
                side_name(cube[157]), side_name(cube[158]), side_name(cube[159]), side_name(cube[160]), side_name(cube[161]), side_name(cube[162]),
                side_name(cube[163]), side_name(cube[164]), side_name(cube[165]), side_name(cube[166]), side_name(cube[167]), side_name(cube[168]),
                side_name(cube[169]), side_name(cube[170]), side_name(cube[171]), side_name(cube[172]), side_name(cube[173]), side_name(cube[174]),
                side_name(cube[175]), side_name(cube[176]), side_name(cube[177]), side_name(cube[178]), side_name(cube[179]), side_name(cube[180]),

                side_name(cube[181]), side_name(cube[182]), side_name(cube[183]), side_name(cube[184]), side_name(cube[185]), side_name(cube[186]),
                side_name(cube[187]), side_name(cube[188]), side_name(cube[189]), side_name(cube[190]), side_name(cube[191]), side_name(cube[192]),
                side_name(cube[193]), side_name(cube[194]), side_name(cube[195]), side_name(cube[196]), side_name(cube[197]), side_name(cube[198]),
                side_name(cube[199]), side_name(cube[200]), side_name(cube[201]), side_name(cube[202]), side_name(cube[203]), side_name(cube[204]),
                side_name(cube[205]), side_name(cube[206]), side_name(cube[207]), side_name(cube[208]), side_name(cube[209]), side_name(cube[210]),
                side_name(cube[211]), side_name(cube[212]), side_name(cube[213]), side_name(cube[214]), side_name(cube[215]), side_name(cube[216]));

            fprintf(fh_write, "%s:%s\n", cube_state_str, steps_buffer);

        } else if (cube_size == 7) {
            sprintf(cube_state_str,
                    "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s",
                    side_name(cube[1]), side_name(cube[2]), side_name(cube[3]), side_name(cube[4]), side_name(cube[5]), side_name(cube[6]), side_name(cube[7]),
                    side_name(cube[8]), side_name(cube[9]), side_name(cube[10]), side_name(cube[11]), side_name(cube[12]), side_name(cube[13]), side_name(cube[14]),
                    side_name(cube[15]), side_name(cube[16]), side_name(cube[17]), side_name(cube[18]), side_name(cube[19]), side_name(cube[20]), side_name(cube[21]),
                    side_name(cube[22]), side_name(cube[23]), side_name(cube[24]), side_name(cube[25]), side_name(cube[26]), side_name(cube[27]), side_name(cube[28]),
                    side_name(cube[29]), side_name(cube[30]), side_name(cube[31]), side_name(cube[32]), side_name(cube[33]), side_name(cube[34]), side_name(cube[35]),
                    side_name(cube[36]), side_name(cube[37]), side_name(cube[38]), side_name(cube[39]), side_name(cube[40]), side_name(cube[41]), side_name(cube[42]),
                    side_name(cube[43]), side_name(cube[44]), side_name(cube[45]), side_name(cube[46]), side_name(cube[47]), side_name(cube[48]), side_name(cube[49]),

                    side_name(cube[50]), side_name(cube[51]), side_name(cube[52]), side_name(cube[53]), side_name(cube[54]), side_name(cube[55]), side_name(cube[56]),
                    side_name(cube[57]), side_name(cube[58]), side_name(cube[59]), side_name(cube[60]), side_name(cube[61]), side_name(cube[62]), side_name(cube[63]),
                    side_name(cube[64]), side_name(cube[65]), side_name(cube[66]), side_name(cube[67]), side_name(cube[68]), side_name(cube[69]), side_name(cube[70]),
                    side_name(cube[71]), side_name(cube[72]), side_name(cube[73]), side_name(cube[74]), side_name(cube[75]), side_name(cube[76]), side_name(cube[77]),
                    side_name(cube[78]), side_name(cube[79]), side_name(cube[80]), side_name(cube[81]), side_name(cube[82]), side_name(cube[83]), side_name(cube[84]),
                    side_name(cube[85]), side_name(cube[86]), side_name(cube[87]), side_name(cube[88]), side_name(cube[89]), side_name(cube[90]), side_name(cube[91]),
                    side_name(cube[92]), side_name(cube[93]), side_name(cube[94]), side_name(cube[95]), side_name(cube[96]), side_name(cube[97]), side_name(cube[98]),

                    side_name(cube[99]), side_name(cube[100]), side_name(cube[101]), side_name(cube[102]), side_name(cube[103]), side_name(cube[104]), side_name(cube[105]),
                    side_name(cube[106]), side_name(cube[107]), side_name(cube[108]), side_name(cube[109]), side_name(cube[110]), side_name(cube[111]), side_name(cube[112]),
                    side_name(cube[113]), side_name(cube[114]), side_name(cube[115]), side_name(cube[116]), side_name(cube[117]), side_name(cube[118]), side_name(cube[119]),
                    side_name(cube[120]), side_name(cube[121]), side_name(cube[122]), side_name(cube[123]), side_name(cube[124]), side_name(cube[125]), side_name(cube[126]),
                    side_name(cube[127]), side_name(cube[128]), side_name(cube[129]), side_name(cube[130]), side_name(cube[131]), side_name(cube[132]), side_name(cube[133]),
                    side_name(cube[134]), side_name(cube[135]), side_name(cube[136]), side_name(cube[137]), side_name(cube[138]), side_name(cube[139]), side_name(cube[140]),
                    side_name(cube[141]), side_name(cube[142]), side_name(cube[143]), side_name(cube[144]), side_name(cube[145]), side_name(cube[146]), side_name(cube[147]),

                    side_name(cube[148]), side_name(cube[149]), side_name(cube[150]), side_name(cube[151]), side_name(cube[152]), side_name(cube[153]), side_name(cube[154]),
                    side_name(cube[155]), side_name(cube[156]), side_name(cube[157]), side_name(cube[158]), side_name(cube[159]), side_name(cube[160]), side_name(cube[161]),
                    side_name(cube[162]), side_name(cube[163]), side_name(cube[164]), side_name(cube[165]), side_name(cube[166]), side_name(cube[167]), side_name(cube[168]),
                    side_name(cube[169]), side_name(cube[170]), side_name(cube[171]), side_name(cube[172]), side_name(cube[173]), side_name(cube[174]), side_name(cube[175]),
                    side_name(cube[176]), side_name(cube[177]), side_name(cube[178]), side_name(cube[179]), side_name(cube[180]), side_name(cube[181]), side_name(cube[182]),
                    side_name(cube[183]), side_name(cube[184]), side_name(cube[185]), side_name(cube[186]), side_name(cube[187]), side_name(cube[188]), side_name(cube[189]),
                    side_name(cube[190]), side_name(cube[191]), side_name(cube[192]), side_name(cube[193]), side_name(cube[194]), side_name(cube[195]), side_name(cube[196]),

                    side_name(cube[197]), side_name(cube[198]), side_name(cube[199]), side_name(cube[200]), side_name(cube[201]), side_name(cube[202]), side_name(cube[203]),
                    side_name(cube[204]), side_name(cube[205]), side_name(cube[206]), side_name(cube[207]), side_name(cube[208]), side_name(cube[209]), side_name(cube[210]),
                    side_name(cube[211]), side_name(cube[212]), side_name(cube[213]), side_name(cube[214]), side_name(cube[215]), side_name(cube[216]), side_name(cube[217]),
                    side_name(cube[218]), side_name(cube[219]), side_name(cube[220]), side_name(cube[221]), side_name(cube[222]), side_name(cube[223]), side_name(cube[224]),
                    side_name(cube[225]), side_name(cube[226]), side_name(cube[227]), side_name(cube[228]), side_name(cube[229]), side_name(cube[230]), side_name(cube[231]),
                    side_name(cube[232]), side_name(cube[233]), side_name(cube[234]), side_name(cube[235]), side_name(cube[236]), side_name(cube[237]), side_name(cube[238]),
                    side_name(cube[239]), side_name(cube[240]), side_name(cube[241]), side_name(cube[242]), side_name(cube[243]), side_name(cube[244]), side_name(cube[245]),

                    side_name(cube[246]), side_name(cube[247]), side_name(cube[248]), side_name(cube[249]), side_name(cube[250]), side_name(cube[251]), side_name(cube[252]),
                    side_name(cube[253]), side_name(cube[254]), side_name(cube[255]), side_name(cube[256]), side_name(cube[257]), side_name(cube[258]), side_name(cube[259]),
                    side_name(cube[260]), side_name(cube[261]), side_name(cube[262]), side_name(cube[263]), side_name(cube[264]), side_name(cube[265]), side_name(cube[266]),
                    side_name(cube[267]), side_name(cube[268]), side_name(cube[269]), side_name(cube[270]), side_name(cube[271]), side_name(cube[272]), side_name(cube[273]),
                    side_name(cube[274]), side_name(cube[275]), side_name(cube[276]), side_name(cube[277]), side_name(cube[278]), side_name(cube[279]), side_name(cube[280]),
                    side_name(cube[281]), side_name(cube[282]), side_name(cube[283]), side_name(cube[284]), side_name(cube[285]), side_name(cube[286]), side_name(cube[287]),
                    side_name(cube[288]), side_name(cube[289]), side_name(cube[290]), side_name(cube[291]), side_name(cube[292]), side_name(cube[293]), side_name(cube[294]));

            fprintf(fh_write, "%s:%s\n", cube_state_str, steps_buffer);

        } else {
            printf("Implement fprintf for cube size %d", cube_size);
            exit(1);
        }

        current_line++;
    }

    fclose(fh_read);
    fclose(fh_write);

    if (! strmatch(input_filename, "steps-3x3x3-preserved-LFRB-depth-9.txt"))
        remove(input_filename);

    exit(0);
}

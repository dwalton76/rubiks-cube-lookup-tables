
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

            // 7x7x7 centers
            if (strmatch(argv[i], "7x7x7-UD-oblique-edge-pairing")) {
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

    // 5x5x5
    if (type == UD_OBLIQUE_EDGE_PAIRING_777) {

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

                if (cube_size == 7) {
                    rotate_777(cube, cube_tmp, array_size, token_ptr);

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
                    if (cube_size == 7) {
                        rotate_777(cube, cube_tmp, array_size, token_ptr);

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
        if (cube_size == 7) {
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

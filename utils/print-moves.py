#!/usr/bin/env python3


all_step_sequences_3x3x3 = {
    "U" :  ["L","L'","L2","F","F'","F2","R","R'","R2","B","B'","B2","D","D'","D2"],
    "U'":  ["L","L'","L2","F","F'","F2","R","R'","R2","B","B'","B2","D","D'","D2"],
    "U2":  ["L","L'","L2","F","F'","F2","R","R'","R2","B","B'","B2","D","D'","D2"],

    "L" :  ["U","U'","U2","F","F'","F2","R","R'","R2","B","B'","B2","D","D'","D2"],
    "L'":  ["U","U'","U2","F","F'","F2","R","R'","R2","B","B'","B2","D","D'","D2"],
    "L2":  ["U","U'","U2","F","F'","F2","R","R'","R2","B","B'","B2","D","D'","D2"],

    "F" :  ["U","U'","U2","L","L'","L2","R","R'","R2","B","B'","B2","D","D'","D2"],
    "F'":  ["U","U'","U2","L","L'","L2","R","R'","R2","B","B'","B2","D","D'","D2"],
    "F2":  ["U","U'","U2","L","L'","L2","R","R'","R2","B","B'","B2","D","D'","D2"],

    "R" :  ["U","U'","U2","L","L'","L2","F","F'","F2","B","B'","B2","D","D'","D2"],
    "R'":  ["U","U'","U2","L","L'","L2","F","F'","F2","B","B'","B2","D","D'","D2"],
    "R2":  ["U","U'","U2","L","L'","L2","F","F'","F2","B","B'","B2","D","D'","D2"],

    "B" :  ["U","U'","U2","L","L'","L2","F","F'","F2","R","R'","R2","D","D'","D2"],
    "B'":  ["U","U'","U2","L","L'","L2","F","F'","F2","R","R'","R2","D","D'","D2"],
    "B2":  ["U","U'","U2","L","L'","L2","F","F'","F2","R","R'","R2","D","D'","D2"],

    "D" :  ["U","U'","U2","L","L'","L2","F","F'","F2","R","R'","R2","B","B'","B2"],
    "D'":  ["U","U'","U2","L","L'","L2","F","F'","F2","R","R'","R2","B","B'","B2"],
    "D2":  ["U","U'","U2","L","L'","L2","F","F'","F2","R","R'","R2","B","B'","B2"],
}


next_steps_4x4x4_ULFRBD_centers_solve = {
    "U"   : ["Uw2",  "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "U'"  : ["Uw2",  "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "U2"  : ["Uw2",  "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],

    "L"   : ["U", "U'", "U2", "Uw2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "L'"  : ["U", "U'", "U2", "Uw2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "L2"  : ["U", "U'", "U2", "Uw2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],

    "F"   : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "F'"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "F2"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],

    "R"   : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "R'"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "R2"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],

    "B"   : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "Bw2", "D", "D'", "D2", "Dw2"],
    "B'"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "Bw2", "D", "D'", "D2", "Dw2"],
    "B2"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "Bw2", "D", "D'", "D2", "Dw2"],

    "D"   : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "Dw2"],
    "D'"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "Dw2"],
    "D2"  : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "Dw2"],

    "Uw2" : ["U", "U'", "U2",        "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "Lw2" : ["U", "U'", "U2", "Uw2", "L", "L'", "L2",        "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "Fw2" : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2",        "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "Rw2" : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2",        "B", "B'", "B2", "Bw2", "D", "D'", "D2", "Dw2"],
    "Bw2" : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2",        "D", "D'", "D2", "Dw2"],
    "Dw2" : ["U", "U'", "U2", "Uw2", "L", "L'", "L2", "Lw2", "F", "F'", "F2", "Fw2", "R", "R'", "R2", "Rw2", "B", "B'", "B2", "Bw2", "D", "D'", "D2"],
}



def LFRB_preserved(steps):
    """
    When we are setting up to slice forward all of the centers are intact so we do
    not have to worry about damaging them.  For slicing back though the LFRB centers
    will look like:

        x x x x  x x x x  x x x x  x x x x
        x L L x  x D D x  x R R x  x U U x
        x U U x  x L L x  x D D x  x R R x
        x x x x  x x x x  x x x x  x x x x

    Return True if steps leaves the centers intact
    """
    state_L = 0
    state_F = 0
    state_R = 0
    state_B = 0

    for step in steps:

        if step == "L":
            state_L += 1
        elif step == "L'":
            state_L -= 1
        elif step == "L2":
            state_L += 2

        elif step == "F":
            state_F += 1
        elif step == "F'":
            state_F -= 1
        elif step == "F2":
            state_F += 2

        elif step == "R":
            state_R += 1
        elif step == "R'":
            state_R -= 1
        elif step == "R2":
            state_R += 2

        elif step == "B":
            state_B += 1
        elif step == "B'":
            state_B -= 1
        elif step == "B2":
            state_B += 2

        elif step in ("D", "D'", "D2", "U", "U'", "U2"):
            pass

        else:
            raise Exception("Invalid step %s" % step)

    #steps_str = ' '.join(steps)
    #log.info("steps %s, state_L %d, state_F %d, state_R %d, state_B %d" % (steps_str, state_L, state_F, state_R, state_B))

    if (state_L == 0 and state_F == 0 and state_R == 0 and state_B == 0):
        return True

    if (state_L % 4 == 0 and state_F % 4 == 0 and state_R % 4 == 0 and state_B % 4 == 0):
        return True

    return False


def ULFRBD_preserved(steps):
    """
    When we are setting up to slice forward all of the centers are intact so we do
    not have to worry about damaging them.  For slicing back though the LFRB centers
    will look like:

    Return True if steps leaves the centers intact
    """
    state_U = 0
    state_L = 0
    state_F = 0
    state_R = 0
    state_B = 0
    state_D = 0

    for step in steps:

        if step == "U":
            state_U += 1
        elif step == "U'":
            state_U -= 1
        elif step == "U2":
            state_U += 2

        elif step == "L":
            state_L += 1
        elif step == "L'":
            state_L -= 1
        elif step == "L2":
            state_L += 2

        elif step == "F":
            state_F += 1
        elif step == "F'":
            state_F -= 1
        elif step == "F2":
            state_F += 2

        elif step == "R":
            state_R += 1
        elif step == "R'":
            state_R -= 1
        elif step == "R2":
            state_R += 2

        elif step == "B":
            state_B += 1
        elif step == "B'":
            state_B -= 1
        elif step == "B2":
            state_B += 2

        elif step == "D":
            state_D += 1
        elif step == "D'":
            state_D -= 1
        elif step == "D2":
            state_D += 2

        else:
            raise Exception("Invalid step %s" % step)

    #steps_str = ' '.join(steps)
    #log.info("steps %s, state_L %d, state_F %d, state_R %d, state_B %d" % (steps_str, state_L, state_F, state_R, state_B))

    if (state_U == 0 and state_L == 0 and state_F == 0 and state_R == 0 and state_B == 0 and state_D == 0):
        return True

    if (state_U % 4 == 0 and state_L % 4 == 0 and state_F % 4 == 0 and state_R % 4 == 0 and state_B % 4 == 0 and state_D % 4 == 0):
        return True

    return False



def build_333_LFRB_preserved():
    step_sequences = []
    count = 0

    with open('steps-3x3x3-preserved-LFRB-depth-9.txt', 'w') as fh:
        for step1 in sorted(all_step_sequences_3x3x3.keys()):
            steps = [step1, ]

            if LFRB_preserved(steps):
                step_sequences.append(steps)
                count += 1
                if count % 100000 == 0:
                    print("%d: %s" % (count, ' '.join(steps)))
                    for steps in step_sequences:
                        fh.write(' '.join(steps) + '\n')
                    step_sequences = []

            for step2 in all_step_sequences_3x3x3[step1]:
                steps = [step1, step2]

                if LFRB_preserved(steps):
                    step_sequences.append(steps)
                    count += 1
                    if count % 10000 == 0:
                        print("%d: %s" % (count, ' '.join(steps)))
                        for steps in step_sequences:
                            fh.write(' '.join(steps) + '\n')
                        step_sequences = []

                for step3 in all_step_sequences_3x3x3[step2]:
                    steps = [step1, step2, step3]

                    if LFRB_preserved(steps):
                        step_sequences.append(steps)
                        count += 1
                        if count % 10000 == 0:
                            print("%d: %s" % (count, ' '.join(steps)))
                            for steps in step_sequences:
                                fh.write(' '.join(steps) + '\n')
                            step_sequences = []

                    for step4 in all_step_sequences_3x3x3[step3]:
                        steps = [step1, step2, step3, step4]

                        if LFRB_preserved(steps):
                            step_sequences.append(steps)
                            count += 1
                            if count % 10000 == 0:
                                print("%d: %s" % (count, ' '.join(steps)))
                                for steps in step_sequences:
                                    fh.write(' '.join(steps) + '\n')
                                step_sequences = []

                        for step5 in all_step_sequences_3x3x3[step4]:
                            steps = [step1, step2, step3, step4, step5]

                            if LFRB_preserved(steps):
                                step_sequences.append(steps)
                                count += 1
                                if count % 10000 == 0:
                                    print("%d: %s" % (count, ' '.join(steps)))
                                    for steps in step_sequences:
                                        fh.write(' '.join(steps) + '\n')
                                    step_sequences = []

                            for step6 in all_step_sequences_3x3x3[step5]:
                                steps = [step1, step2, step3, step4, step5, step6]

                                if LFRB_preserved(steps):
                                    step_sequences.append(steps)
                                    count += 1
                                    if count % 10000 == 0:
                                        print("%d: %s" % (count, ' '.join(steps)))
                                        for steps in step_sequences:
                                            fh.write(' '.join(steps) + '\n')
                                        step_sequences = []

                                for step7 in all_step_sequences_3x3x3[step6]:
                                    steps = [step1, step2, step3, step4, step5, step6, step7]

                                    if LFRB_preserved(steps):
                                        step_sequences.append(steps)
                                        count += 1
                                        if count % 10000 == 0:
                                            print("%d: %s" % (count, ' '.join(steps)))
                                            for steps in step_sequences:
                                                fh.write(' '.join(steps) + '\n')
                                            step_sequences = []

                                    for step8 in all_step_sequences_3x3x3[step7]:
                                        steps = [step1, step2, step3, step4, step5, step6, step7, step8]

                                        if LFRB_preserved(steps):
                                            step_sequences.append(steps)
                                            count += 1
                                            if count % 10000 == 0:
                                                print("%d: %s" % (count, ' '.join(steps)))
                                                for steps in step_sequences:
                                                    fh.write(' '.join(steps) + '\n')
                                                step_sequences = []

                                        for step9 in all_step_sequences_3x3x3[step8]:
                                            steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9]

                                            if LFRB_preserved(steps):
                                                step_sequences.append(steps)
                                                count += 1
                                                if count % 10000 == 0:
                                                    print("%d: %s" % (count, ' '.join(steps)))
                                                    for steps in step_sequences:
                                                        fh.write(' '.join(steps) + '\n')
                                                    step_sequences = []

        for steps in step_sequences:
            fh.write(' '.join(steps) + '\n')
        step_sequences = []


def build_333_ULFRBD_preserved():
    step_sequences = []
    count = 0

    with open('3x3x3-ULFRBD-preserved.txt', 'w') as fh:
        for step1 in sorted(all_step_sequences_3x3x3.keys()):
            steps = [step1, ]

            if ULFRBD_preserved(steps):
                step_sequences.append(steps)
                count += 1
                if count % 100000 == 0:
                    print("%d: %s" % (count, ' '.join(steps)))
                    for steps in step_sequences:
                        fh.write(' '.join(steps) + '\n')
                    step_sequences = []

            for step2 in all_step_sequences_3x3x3[step1]:
                steps = [step1, step2]

                if ULFRBD_preserved(steps):
                    step_sequences.append(steps)
                    count += 1
                    if count % 10000 == 0:
                        print("%d: %s" % (count, ' '.join(steps)))
                        for steps in step_sequences:
                            fh.write(' '.join(steps) + '\n')
                        step_sequences = []

                for step3 in all_step_sequences_3x3x3[step2]:
                    steps = [step1, step2, step3]

                    if ULFRBD_preserved(steps):
                        step_sequences.append(steps)
                        count += 1
                        if count % 10000 == 0:
                            print("%d: %s" % (count, ' '.join(steps)))
                            for steps in step_sequences:
                                fh.write(' '.join(steps) + '\n')
                            step_sequences = []

                    for step4 in all_step_sequences_3x3x3[step3]:
                        steps = [step1, step2, step3, step4]

                        if ULFRBD_preserved(steps):
                            step_sequences.append(steps)
                            count += 1
                            if count % 10000 == 0:
                                print("%d: %s" % (count, ' '.join(steps)))
                                for steps in step_sequences:
                                    fh.write(' '.join(steps) + '\n')
                                step_sequences = []

                        for step5 in all_step_sequences_3x3x3[step4]:
                            steps = [step1, step2, step3, step4, step5]

                            if ULFRBD_preserved(steps):
                                step_sequences.append(steps)
                                count += 1
                                if count % 10000 == 0:
                                    print("%d: %s" % (count, ' '.join(steps)))
                                    for steps in step_sequences:
                                        fh.write(' '.join(steps) + '\n')
                                    step_sequences = []

                            for step6 in all_step_sequences_3x3x3[step5]:
                                steps = [step1, step2, step3, step4, step5, step6]

                                if ULFRBD_preserved(steps):
                                    step_sequences.append(steps)
                                    count += 1
                                    if count % 10000 == 0:
                                        print("%d: %s" % (count, ' '.join(steps)))
                                        for steps in step_sequences:
                                            fh.write(' '.join(steps) + '\n')
                                        step_sequences = []

                                for step7 in all_step_sequences_3x3x3[step6]:
                                    steps = [step1, step2, step3, step4, step5, step6, step7]

                                    if ULFRBD_preserved(steps):
                                        step_sequences.append(steps)
                                        count += 1
                                        if count % 10000 == 0:
                                            print("%d: %s" % (count, ' '.join(steps)))
                                            for steps in step_sequences:
                                                fh.write(' '.join(steps) + '\n')
                                            step_sequences = []
                                            '''

                                    for step8 in all_step_sequences_3x3x3[step7]:
                                        steps = [step1, step2, step3, step4, step5, step6, step7, step8]

                                        if ULFRBD_preserved(steps):
                                            step_sequences.append(steps)
                                            count += 1
                                            if count % 10000 == 0:
                                                print("%d: %s" % (count, ' '.join(steps)))
                                                for steps in step_sequences:
                                                    fh.write(' '.join(steps) + '\n')
                                                step_sequences = []

                                        for step9 in all_step_sequences_3x3x3[step8]:
                                            steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9]

                                            if ULFRBD_preserved(steps):
                                                step_sequences.append(steps)
                                                count += 1
                                                if count % 10000 == 0:
                                                    print("%d: %s" % (count, ' '.join(steps)))
                                                    for steps in step_sequences:
                                                        fh.write(' '.join(steps) + '\n')
                                                    step_sequences = []
                                            '''

        for steps in step_sequences:
            fh.write(' '.join(steps) + '\n')
        step_sequences = []



def build_444_step_sequences():
    step_sequences = []

    for step1 in next_steps_4x4x4_ULFRBD_centers_solve.keys():
        steps = [step1,]
        step_sequences.append(steps)

        for step2 in next_steps_4x4x4_ULFRBD_centers_solve[step1]:
            steps = [step1, step2]
            step_sequences.append(steps)

            for step3 in next_steps_4x4x4_ULFRBD_centers_solve[step2]:
                steps = [step1, step2, step3]
                step_sequences.append(steps)

                for step4 in next_steps_4x4x4_ULFRBD_centers_solve[step3]:
                    steps = [step1, step2, step3, step4]
                    step_sequences.append(steps)

                    '''
                    for step5 in next_steps_4x4x4_ULFRBD_centers_solve[step4]:
                        steps = [step1, step2, step3, step4, step5]
                        step_sequences.append(steps)

                        for step6 in next_steps_4x4x4_ULFRBD_centers_solve[step4]:
                            steps = [step1, step2, step3, step4, step5, step6]
                            step_sequences.append(steps)
                    '''

    step_sequences = sorted(step_sequences)
    prev_steps = None
    final = []

    for steps in step_sequences:
        if prev_steps is None or prev_steps[0:-1] != steps[0:-1]:
            final.append('INIT')
        final.append(' '.join(steps))
        prev_steps = steps

    with open('all_4x4x4_step_sequences_5_deep.txt', 'w') as fh:
        fh.write('\n'.join(final))


if __name__ == '__main__':
    build_333_LFRB_preserved()
    #build_333_ULFRBD_preserved()

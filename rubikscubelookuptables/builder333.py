"""
This is a 4-micropython-phase solver that was designed to run on the LEGO SPIKE platform.
LEGO SPIKE has something like 90k of memory to play with.

phase 1 - EO the edges
    - make the edges solveable without L L' R R'
    - (2^12)/2 or 2048 states
    - averages 4.61 moves

phase 2 - Remove F F' B B'
    - LB LF RB RF edges must be staged to x-plane
        12!/(8!*4!) is 495
    - EO the corners
        - (3^8)/3 or 2187 states
    - 2187 * 495 is 1,082,565
    - averages 7.80 moves

phase 3 - Remove U U' D D'
    move 4 edges to y-plane, this in turn moves the other 4-edges to z-plane
    There must also be some corner manipulation done here
    - 8!/(4!*4!) is 70 for the edges
    -  is 40,320 for the corners
    - 70 * 40,320 is 2,822,400
    - averages 8.80 moves

phase 4 - solve cube
    - all quarter turns have been removed by this point
    - (4!^3)/2 is 6912 for the edges
    - 4!^2 is 576 for the corners
        it is actually 96 though (I got 96 by building the corners table)
        576/6 is 96 not sure if that means anything

    - 6912 * 96 is 663,552
    - averages 10.13 moves

This should averge 31 moves
"""

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS


class Build333MicroPythonPhase1(BFS):
    """
    TODO this is broken.  We used to have logic somewhere that did something special
    for the edges in this phase.

    lookup-table-3x3x3-step110.txt
    ==============================
    0 steps has 1 entries (100 percent, 0.00x previous step)

    Total: 1 entries
    Average: 0.00 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase1",
            # illegal moves
            (),
            "3x3x3",
            "lookup-table-3x3x3-step110.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        x 1 x
        1 U 1
        x 1 x

 x 1 x  x 1 x  x 1 x  x 1 x
 1 L 1  1 F 1  1 R 1  1 B 1
 x 1 x  x 1 x  x 1 x  x 1 x

        x 1 x
        1 D 1
        x 1 x""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase2(BFS):
    """
    lookup-table-3x3x3-step120.txt
    ==============================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 17 entries (0 percent, 8.50x previous step)
    3 steps has 134 entries (0 percent, 7.88x previous step)
    4 steps has 1,065 entries (0 percent, 7.95x previous step)
    5 steps has 8,190 entries (0 percent, 7.69x previous step)
    6 steps has 54,694 entries (5 percent, 6.68x previous step)
    7 steps has 267,576 entries (24 percent, 4.89x previous step)
    8 steps has 560,568 entries (51 percent, 2.09x previous step)
    9 steps has 187,204 entries (17 percent, 0.33x previous step)
    10 steps has 3,114 entries (0 percent, 0.02x previous step)

    Total: 1,082,565 entries
    Average: 7.80 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase2",
            # illegal moves
            ("L", "L'", "R", "R'"),
            "3x3x3",
            "lookup-table-3x3x3-step120.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        U x U
        x U x
        U x U

 x x x  x x x  x x x  x x x
 1 L 1  1 F 1  1 R 1  1 B 1
 x x x  x x x  x x x  x x x

        U x U
        x D x
        U x U""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase2Edges(BFS):
    """
    lookup-table-3x3x3-step121-edges.txt
    ====================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 17 entries (3 percent, 8.50x previous step)
    3 steps has 104 entries (21 percent, 6.12x previous step)
    4 steps has 221 entries (44 percent, 2.12x previous step)
    5 steps has 150 entries (30 percent, 0.68x previous step)

    Total: 495 entries
    Average: 4.00 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase2-edges",
            # illegal moves
            ("L", "L'", "R", "R'"),
            "3x3x3",
            "lookup-table-3x3x3-step121-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        . x .
        x . x
        . x .

 . x .  . x .  . x .  . x .
 1 . 1  1 . 1  1 . 1  1 . 1
 . x .  . x .  . x .  . x .

        . x .
        x . x
        . x .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase2Corners(BFS):
    """
    lookup-table-3x3x3-step122-corners.txt
    ======================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 2 entries (0 percent, 2.00x previous step)
    2 steps has 13 entries (0 percent, 6.50x previous step)
    3 steps has 70 entries (3 percent, 5.38x previous step)
    4 steps has 335 entries (15 percent, 4.79x previous step)
    5 steps has 1,008 entries (46 percent, 3.01x previous step)
    6 steps has 726 entries (33 percent, 0.72x previous step)
    7 steps has 32 entries (1 percent, 0.04x previous step)

    Total: 2,187 entries
    Average: 5.12 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase2-corners",
            # illegal moves
            ("L", "L'", "R", "R'"),
            "3x3x3",
            "lookup-table-3x3x3-step122-corners.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        U . U
        . . .
        U . U

 x . x  x . x  x . x  x . x
 . . .  . . .  . . .  . . .
 x . x  x . x  x . x  x . x

        U . U
        . . .
        U . U""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase3(BFS):
    """
    lookup-table-3x3x3-step130.txt
    ==============================
    0 steps has 96 entries (0 percent, 0.00x previous step)
    1 steps has 192 entries (0 percent, 2.00x previous step)
    2 steps has 864 entries (0 percent, 4.50x previous step)
    3 steps has 3,456 entries (0 percent, 4.00x previous step)
    4 steps has 11,904 entries (0 percent, 3.44x previous step)
    5 steps has 50,880 entries (1 percent, 4.27x previous step)
    6 steps has 173,376 entries (6 percent, 3.41x previous step)
    7 steps has 358,272 entries (12 percent, 2.07x previous step)
    8 steps has 495,168 entries (17 percent, 1.38x previous step)
    9 steps has 678,720 entries (24 percent, 1.37x previous step)
    10 steps has 692,928 entries (24 percent, 1.02x previous step)
    11 steps has 307,392 entries (10 percent, 0.44x previous step)
    12 steps has 46,848 entries (1 percent, 0.15x previous step)
    13 steps has 2,304 entries (0 percent, 0.05x previous step)

    Total: 2,822,400 entries
    Average: 8.80 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase3",
            # illegal moves
            ("L", "L'", "R", "R'", "F", "F'", "B", "B'"),
            "3x3x3",
            "lookup-table-3x3x3-step130.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ("DFDxUxDFDLxLxLxLxLBFBxFxBFBRxRxRxRxRFFFxBxFFFUFUxDxUFU", "ULFRBD"),
                ("DFDxUxDFDLxLxLxRxRBFBxFxFFFRxRxRxLxLFFFxBxBFBUFUxDxUFU", "ULFRBD"),
                ("DFDxUxDFDLxRxLxLxRFFBxFxFFBRxLxRxRxLBFFxBxBFFUFUxDxUFU", "ULFRBD"),
                ("DFDxUxDFDLxRxLxRxLFFBxFxBFFRxLxRxLxRBFFxBxFFBUFUxDxUFU", "ULFRBD"),
                ("DFDxUxDFDRxLxLxLxRBFFxFxFFBLxRxRxRxLFFBxBxBFFUFUxDxUFU", "ULFRBD"),
                ("DFDxUxDFDRxLxLxRxLBFFxFxBFFLxRxRxLxRFFBxBxFFBUFUxDxUFU", "ULFRBD"),
                ("DFDxUxDFDRxRxLxLxLFFFxFxBFBLxLxRxRxRBFBxBxFFFUFUxDxUFU", "ULFRBD"),
                ("DFDxUxDFDRxRxLxRxRFFFxFxFFFLxLxRxLxLBFBxBxBFBUFUxDxUFU", "ULFRBD"),
                ("DFDxUxUFULxLxLxLxLFFFxFxBFBRxRxRxRxRFFFxBxBFBUFUxDxDFD", "ULFRBD"),
                ("DFDxUxUFULxLxLxRxRFFBxFxBFFLxLxRxRxRBFFxBxFFBDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFULxLxLxRxRFFBxFxFFBLxLxRxRxRBFFxBxBFFUFUxDxDFD", "ULFRBD"),
                ("DFDxUxUFULxLxLxRxRFFFxFxBFBRxRxRxLxLFFFxBxBFBDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFULxRxLxLxRBFBxFxBFBLxRxRxLxRFFFxBxFFFDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFULxRxLxLxRBFBxFxFFFLxRxRxLxRFFFxBxBFBUFUxDxDFD", "ULFRBD"),
                ("DFDxUxUFULxRxLxLxRBFFxFxBFFRxLxRxRxLBFFxBxBFFDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFULxRxLxRxLBFFxFxBFFRxLxRxLxRBFFxBxBFFUFUxDxDFD", "ULFRBD"),
                ("DFDxUxUFURxLxLxLxRFFBxFxFFBLxRxRxRxLFFBxBxFFBUFUxDxDFD", "ULFRBD"),
                ("DFDxUxUFURxLxLxRxLFFBxFxFFBLxRxRxLxRFFBxBxFFBDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFURxLxLxRxLFFFxFxBFBRxLxRxRxLBFBxBxFFFUFUxDxDFD", "ULFRBD"),
                ("DFDxUxUFURxLxLxRxLFFFxFxFFFRxLxRxRxLBFBxBxBFBDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFURxRxLxLxLBFBxFxFFFLxLxRxRxRBFBxBxFFFDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFURxRxLxLxLBFFxFxBFFRxRxRxLxLFFBxBxFFBUFUxDxDFD", "ULFRBD"),
                ("DFDxUxUFURxRxLxLxLBFFxFxFFBRxRxRxLxLFFBxBxBFFDFDxDxUFU", "ULFRBD"),
                ("DFDxUxUFURxRxLxRxRBFBxFxFFFLxLxRxLxLBFBxBxFFFUFUxDxDFD", "ULFRBD"),
                ("DFUxUxDFULxLxLxLxLBFFxFxBFFRxRxRxRxRBFFxBxBFFUFDxDxUFD", "ULFRBD"),
                ("DFUxUxDFULxLxLxRxRBFBxFxBFBLxLxRxRxRFFFxBxFFFDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFULxLxLxRxRBFBxFxFFFLxLxRxRxRFFFxBxBFBUFDxDxUFD", "ULFRBD"),
                ("DFUxUxDFULxLxLxRxRBFFxFxBFFRxRxRxLxLBFFxBxBFFDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFULxRxLxLxRFFBxFxBFFLxRxRxLxRBFFxBxFFBDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFULxRxLxLxRFFBxFxFFBLxRxRxLxRBFFxBxBFFUFDxDxUFD", "ULFRBD"),
                ("DFUxUxDFULxRxLxLxRFFFxFxBFBRxLxRxRxLFFFxBxBFBDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFULxRxLxRxLFFFxFxBFBRxLxRxLxRFFFxBxBFBUFDxDxUFD", "ULFRBD"),
                ("DFUxUxDFURxLxLxLxRBFBxFxFFFLxRxRxRxLBFBxBxFFFUFDxDxUFD", "ULFRBD"),
                ("DFUxUxDFURxLxLxRxLBFBxFxFFFLxRxRxLxRBFBxBxFFFDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFURxLxLxRxLBFFxFxBFFRxLxRxRxLFFBxBxFFBUFDxDxUFD", "ULFRBD"),
                ("DFUxUxDFURxLxLxRxLBFFxFxFFBRxLxRxRxLFFBxBxBFFDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFURxRxLxLxLFFBxFxFFBLxLxRxRxRFFBxBxFFBDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFURxRxLxLxLFFFxFxBFBRxRxRxLxLBFBxBxFFFUFDxDxUFD", "ULFRBD"),
                ("DFUxUxDFURxRxLxLxLFFFxFxFFFRxRxRxLxLBFBxBxBFBDFUxDxDFU", "ULFRBD"),
                ("DFUxUxDFURxRxLxRxRFFBxFxFFBLxLxRxLxLFFBxBxFFBUFDxDxUFD", "ULFRBD"),
                ("DFUxUxUFDLxLxLxLxLFFBxFxBFFRxRxRxRxRBFFxBxFFBUFDxDxDFU", "ULFRBD"),
                ("DFUxUxUFDLxLxLxRxRFFBxFxFFBRxRxRxLxLBFFxBxBFFUFDxDxDFU", "ULFRBD"),
                ("DFUxUxUFDLxRxLxLxRBFBxFxFFFRxLxRxRxLFFFxBxBFBUFDxDxDFU", "ULFRBD"),
                ("DFUxUxUFDLxRxLxRxLBFBxFxBFBRxLxRxLxRFFFxBxFFFUFDxDxDFU", "ULFRBD"),
                ("DFUxUxUFDRxLxLxLxRFFFxFxFFFLxRxRxRxLBFBxBxBFBUFDxDxDFU", "ULFRBD"),
                ("DFUxUxUFDRxLxLxRxLFFFxFxBFBLxRxRxLxRBFBxBxFFFUFDxDxDFU", "ULFRBD"),
                ("DFUxUxUFDRxRxLxLxLBFFxFxBFFLxLxRxRxRFFBxBxFFBUFDxDxDFU", "ULFRBD"),
                ("DFUxUxUFDRxRxLxRxRBFFxFxFFBLxLxRxLxLFFBxBxBFFUFDxDxDFU", "ULFRBD"),
                ("UFDxUxDFULxLxLxLxLBFFxFxFFBRxRxRxRxRFFBxBxBFFDFUxDxUFD", "ULFRBD"),
                ("UFDxUxDFULxLxLxRxRBFFxFxBFFRxRxRxLxLFFBxBxFFBDFUxDxUFD", "ULFRBD"),
                ("UFDxUxDFULxRxLxLxRFFFxFxBFBRxLxRxRxLBFBxBxFFFDFUxDxUFD", "ULFRBD"),
                ("UFDxUxDFULxRxLxRxLFFFxFxFFFRxLxRxLxRBFBxBxBFBDFUxDxUFD", "ULFRBD"),
                ("UFDxUxDFURxLxLxLxRBFBxFxBFBLxRxRxRxLFFFxBxFFFDFUxDxUFD", "ULFRBD"),
                ("UFDxUxDFURxLxLxRxLBFBxFxFFFLxRxRxLxRFFFxBxBFBDFUxDxUFD", "ULFRBD"),
                ("UFDxUxDFURxRxLxLxLFFBxFxFFBLxLxRxRxRBFFxBxBFFDFUxDxUFD", "ULFRBD"),
                ("UFDxUxDFURxRxLxRxRFFBxFxBFFLxLxRxLxLBFFxBxFFBDFUxDxUFD", "ULFRBD"),
                ("UFDxUxUFDLxLxLxLxLFFBxFxFFBRxRxRxRxRFFBxBxFFBDFUxDxDFU", "ULFRBD"),
                ("UFDxUxUFDLxLxLxRxRFFBxFxFFBRxRxRxLxLFFBxBxFFBUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDLxLxLxRxRFFFxFxBFBLxLxRxRxRBFBxBxFFFDFUxDxDFU", "ULFRBD"),
                ("UFDxUxUFDLxLxLxRxRFFFxFxFFFLxLxRxRxRBFBxBxBFBUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDLxRxLxLxRBFBxFxFFFRxLxRxRxLBFBxBxFFFUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDLxRxLxLxRBFFxFxBFFLxRxRxLxRFFBxBxFFBDFUxDxDFU", "ULFRBD"),
                ("UFDxUxUFDLxRxLxLxRBFFxFxFFBLxRxRxLxRFFBxBxBFFUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDLxRxLxRxLBFBxFxFFFRxLxRxLxRBFBxBxFFFDFUxDxDFU", "ULFRBD"),
                ("UFDxUxUFDRxLxLxLxRFFFxFxBFBLxRxRxRxLFFFxBxBFBDFUxDxDFU", "ULFRBD"),
                ("UFDxUxUFDRxLxLxRxLFFBxFxBFFRxLxRxRxLBFFxBxFFBUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDRxLxLxRxLFFBxFxFFBRxLxRxRxLBFFxBxBFFDFUxDxDFU", "ULFRBD"),
                ("UFDxUxUFDRxLxLxRxLFFFxFxBFBLxRxRxLxRFFFxBxBFBUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDRxRxLxLxLBFBxFxBFBRxRxRxLxLFFFxBxFFFUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDRxRxLxLxLBFBxFxFFFRxRxRxLxLFFFxBxBFBDFUxDxDFU", "ULFRBD"),
                ("UFDxUxUFDRxRxLxLxLBFFxFxBFFLxLxRxRxRBFFxBxBFFUFDxDxUFD", "ULFRBD"),
                ("UFDxUxUFDRxRxLxRxRBFFxFxBFFLxLxRxLxLBFFxBxBFFDFUxDxDFU", "ULFRBD"),
                ("UFUxUxDFDLxLxLxLxLBFBxFxFFFRxRxRxRxRBFBxBxFFFDFDxDxUFU", "ULFRBD"),
                ("UFUxUxDFDLxLxLxRxRBFBxFxFFFRxRxRxLxLBFBxBxFFFUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDLxLxLxRxRBFFxFxBFFLxLxRxRxRFFBxBxFFBDFDxDxUFU", "ULFRBD"),
                ("UFUxUxDFDLxLxLxRxRBFFxFxFFBLxLxRxRxRFFBxBxBFFUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDLxRxLxLxRFFBxFxFFBRxLxRxRxLFFBxBxFFBUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDLxRxLxLxRFFFxFxBFBLxRxRxLxRBFBxBxFFFDFDxDxUFU", "ULFRBD"),
                ("UFUxUxDFDLxRxLxLxRFFFxFxFFFLxRxRxLxRBFBxBxBFBUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDLxRxLxRxLFFBxFxFFBRxLxRxLxRFFBxBxFFBDFDxDxUFU", "ULFRBD"),
                ("UFUxUxDFDRxLxLxLxRBFFxFxBFFLxRxRxRxLBFFxBxBFFDFDxDxUFU", "ULFRBD"),
                ("UFUxUxDFDRxLxLxRxLBFBxFxBFBRxLxRxRxLFFFxBxFFFUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDRxLxLxRxLBFBxFxFFFRxLxRxRxLFFFxBxBFBDFDxDxUFU", "ULFRBD"),
                ("UFUxUxDFDRxLxLxRxLBFFxFxBFFLxRxRxLxRBFFxBxBFFUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDRxRxLxLxLFFBxFxBFFRxRxRxLxLBFFxBxFFBUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDRxRxLxLxLFFBxFxFFBRxRxRxLxLBFFxBxBFFDFDxDxUFU", "ULFRBD"),
                ("UFUxUxDFDRxRxLxLxLFFFxFxBFBLxLxRxRxRFFFxBxBFBUFUxDxDFD", "ULFRBD"),
                ("UFUxUxDFDRxRxLxRxRFFFxFxBFBLxLxRxLxLFFFxBxBFBDFDxDxUFU", "ULFRBD"),
                ("UFUxUxUFULxLxLxLxLFFFxFxFFFRxRxRxRxRBFBxBxBFBDFDxDxDFD", "ULFRBD"),
                ("UFUxUxUFULxLxLxRxRFFFxFxBFBRxRxRxLxLBFBxBxFFFDFDxDxDFD", "ULFRBD"),
                ("UFUxUxUFULxRxLxLxRBFFxFxBFFRxLxRxRxLFFBxBxFFBDFDxDxDFD", "ULFRBD"),
                ("UFUxUxUFULxRxLxRxLBFFxFxFFBRxLxRxLxRFFBxBxBFFDFDxDxDFD", "ULFRBD"),
                ("UFUxUxUFURxLxLxLxRFFBxFxBFFLxRxRxRxLBFFxBxFFBDFDxDxDFD", "ULFRBD"),
                ("UFUxUxUFURxLxLxRxLFFBxFxFFBLxRxRxLxRBFFxBxBFFDFDxDxDFD", "ULFRBD"),
                ("UFUxUxUFURxRxLxLxLBFBxFxFFFLxLxRxRxRFFFxBxBFBDFDxDxDFD", "ULFRBD"),
                ("UFUxUxUFURxRxLxRxRBFBxFxBFBLxLxRxLxLFFFxBxFFFDFDxDxDFD", "ULFRBD"),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase3Edges(BFS):
    """
    lookup-table-3x3x3-step131-edges.txt
    ====================================
    0 steps has 1 entries (1 percent, 0.00x previous step)
    1 steps has 2 entries (2 percent, 2.00x previous step)
    2 steps has 9 entries (12 percent, 4.50x previous step)
    3 steps has 30 entries (42 percent, 3.33x previous step)
    4 steps has 28 entries (40 percent, 0.93x previous step)

    Total: 70 entries
    Average: 3.17 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase3-edges",
            # illegal moves
            ("L", "L'", "R", "R'", "F", "F'", "B", "B'"),
            "3x3x3",
            "lookup-table-3x3x3-step131-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        . F .
        x . x
        . F .

 . x .  . F .  . x .  . F .
 x . x  x . x  x . x  x . x
 . x .  . F .  . x .  . F .

        . F .
        x . x
        . F .
        """,
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase3Corners(BFS):
    """
    lookup-table-3x3x3-step132-corners.txt
    ======================================
    0 steps has 96 entries (0 percent, 0.00x previous step)
    1 steps has 192 entries (0 percent, 2.00x previous step)
    2 steps has 480 entries (1 percent, 2.50x previous step)
    3 steps has 1,152 entries (2 percent, 2.40x previous step)
    4 steps has 1,728 entries (4 percent, 1.50x previous step)
    5 steps has 4,800 entries (11 percent, 2.78x previous step)
    6 steps has 4,224 entries (10 percent, 0.88x previous step)
    7 steps has 4,992 entries (12 percent, 1.18x previous step)
    8 steps has 6,528 entries (16 percent, 1.31x previous step)
    9 steps has 9,216 entries (22 percent, 1.41x previous step)
    10 steps has 4,992 entries (12 percent, 0.54x previous step)
    11 steps has 1,920 entries (4 percent, 0.38x previous step)

    Total: 40,320 entries
    Average: 7.49 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase3-corners",
            # illegal moves
            ("L", "L'", "R", "R'", "F", "F'", "B", "B'"),
            "3x3x3",
            "lookup-table-3x3x3-step132-corners.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ("D.D...D.DL.L...L.LB.B...B.BR.R...R.RF.F...F.FU.U...U.U", "ULFRBD"),
                ("D.D...D.DL.L...R.RB.B...F.FR.R...L.LF.F...B.BU.U...U.U", "ULFRBD"),
                ("D.D...D.DL.R...L.RF.B...F.BR.L...R.LB.F...B.FU.U...U.U", "ULFRBD"),
                ("D.D...D.DL.R...R.LF.B...B.FR.L...L.RB.F...F.BU.U...U.U", "ULFRBD"),
                ("D.D...D.DR.L...L.RB.F...F.BL.R...R.LF.B...B.FU.U...U.U", "ULFRBD"),
                ("D.D...D.DR.L...R.LB.F...B.FL.R...L.RF.B...F.BU.U...U.U", "ULFRBD"),
                ("D.D...D.DR.R...L.LF.F...B.BL.L...R.RB.B...F.FU.U...U.U", "ULFRBD"),
                ("D.D...D.DR.R...R.RF.F...F.FL.L...L.LB.B...B.BU.U...U.U", "ULFRBD"),
                ("D.D...U.UL.L...L.LF.F...B.BR.R...R.RF.F...B.BU.U...D.D", "ULFRBD"),
                ("D.D...U.UL.L...R.RF.B...B.FL.L...R.RB.F...F.BD.D...U.U", "ULFRBD"),
                ("D.D...U.UL.L...R.RF.B...F.BL.L...R.RB.F...B.FU.U...D.D", "ULFRBD"),
                ("D.D...U.UL.L...R.RF.F...B.BR.R...L.LF.F...B.BD.D...U.U", "ULFRBD"),
                ("D.D...U.UL.R...L.RB.B...B.BL.R...L.RF.F...F.FD.D...U.U", "ULFRBD"),
                ("D.D...U.UL.R...L.RB.B...F.FL.R...L.RF.F...B.BU.U...D.D", "ULFRBD"),
                ("D.D...U.UL.R...L.RB.F...B.FR.L...R.LB.F...B.FD.D...U.U", "ULFRBD"),
                ("D.D...U.UL.R...R.LB.F...B.FR.L...L.RB.F...B.FU.U...D.D", "ULFRBD"),
                ("D.D...U.UR.L...L.RF.B...F.BL.R...R.LF.B...F.BU.U...D.D", "ULFRBD"),
                ("D.D...U.UR.L...R.LF.B...F.BL.R...L.RF.B...F.BD.D...U.U", "ULFRBD"),
                ("D.D...U.UR.L...R.LF.F...B.BR.L...R.LB.B...F.FU.U...D.D", "ULFRBD"),
                ("D.D...U.UR.L...R.LF.F...F.FR.L...R.LB.B...B.BD.D...U.U", "ULFRBD"),
                ("D.D...U.UR.R...L.LB.B...F.FL.L...R.RB.B...F.FD.D...U.U", "ULFRBD"),
                ("D.D...U.UR.R...L.LB.F...B.FR.R...L.LF.B...F.BU.U...D.D", "ULFRBD"),
                ("D.D...U.UR.R...L.LB.F...F.BR.R...L.LF.B...B.FD.D...U.U", "ULFRBD"),
                ("D.D...U.UR.R...R.RB.B...F.FL.L...L.LB.B...F.FU.U...D.D", "ULFRBD"),
                ("D.U...D.UL.L...L.LB.F...B.FR.R...R.RB.F...B.FU.D...U.D", "ULFRBD"),
                ("D.U...D.UL.L...R.RB.B...B.BL.L...R.RF.F...F.FD.U...D.U", "ULFRBD"),
                ("D.U...D.UL.L...R.RB.B...F.FL.L...R.RF.F...B.BU.D...U.D", "ULFRBD"),
                ("D.U...D.UL.L...R.RB.F...B.FR.R...L.LB.F...B.FD.U...D.U", "ULFRBD"),
                ("D.U...D.UL.R...L.RF.B...B.FL.R...L.RB.F...F.BD.U...D.U", "ULFRBD"),
                ("D.U...D.UL.R...L.RF.B...F.BL.R...L.RB.F...B.FU.D...U.D", "ULFRBD"),
                ("D.U...D.UL.R...L.RF.F...B.BR.L...R.LF.F...B.BD.U...D.U", "ULFRBD"),
                ("D.U...D.UL.R...R.LF.F...B.BR.L...L.RF.F...B.BU.D...U.D", "ULFRBD"),
                ("D.U...D.UR.L...L.RB.B...F.FL.R...R.LB.B...F.FU.D...U.D", "ULFRBD"),
                ("D.U...D.UR.L...R.LB.B...F.FL.R...L.RB.B...F.FD.U...D.U", "ULFRBD"),
                ("D.U...D.UR.L...R.LB.F...B.FR.L...R.LF.B...F.BU.D...U.D", "ULFRBD"),
                ("D.U...D.UR.L...R.LB.F...F.BR.L...R.LF.B...B.FD.U...D.U", "ULFRBD"),
                ("D.U...D.UR.R...L.LF.B...F.BL.L...R.RF.B...F.BD.U...D.U", "ULFRBD"),
                ("D.U...D.UR.R...L.LF.F...B.BR.R...L.LB.B...F.FU.D...U.D", "ULFRBD"),
                ("D.U...D.UR.R...L.LF.F...F.FR.R...L.LB.B...B.BD.U...D.U", "ULFRBD"),
                ("D.U...D.UR.R...R.RF.B...F.BL.L...L.LF.B...F.BU.D...U.D", "ULFRBD"),
                ("D.U...U.DL.L...L.LF.B...B.FR.R...R.RB.F...F.BU.D...D.U", "ULFRBD"),
                ("D.U...U.DL.L...R.RF.B...F.BR.R...L.LB.F...B.FU.D...D.U", "ULFRBD"),
                ("D.U...U.DL.R...L.RB.B...F.FR.L...R.LF.F...B.BU.D...D.U", "ULFRBD"),
                ("D.U...U.DL.R...R.LB.B...B.BR.L...L.RF.F...F.FU.D...D.U", "ULFRBD"),
                ("D.U...U.DR.L...L.RF.F...F.FL.R...R.LB.B...B.BU.D...D.U", "ULFRBD"),
                ("D.U...U.DR.L...R.LF.F...B.BL.R...L.RB.B...F.FU.D...D.U", "ULFRBD"),
                ("D.U...U.DR.R...L.LB.F...B.FL.L...R.RF.B...F.BU.D...D.U", "ULFRBD"),
                ("D.U...U.DR.R...R.RB.F...F.BL.L...L.LF.B...B.FU.D...D.U", "ULFRBD"),
                ("U.D...D.UL.L...L.LB.F...F.BR.R...R.RF.B...B.FD.U...U.D", "ULFRBD"),
                ("U.D...D.UL.L...R.RB.F...B.FR.R...L.LF.B...F.BD.U...U.D", "ULFRBD"),
                ("U.D...D.UL.R...L.RF.F...B.BR.L...R.LB.B...F.FD.U...U.D", "ULFRBD"),
                ("U.D...D.UL.R...R.LF.F...F.FR.L...L.RB.B...B.BD.U...U.D", "ULFRBD"),
                ("U.D...D.UR.L...L.RB.B...B.BL.R...R.LF.F...F.FD.U...U.D", "ULFRBD"),
                ("U.D...D.UR.L...R.LB.B...F.FL.R...L.RF.F...B.BD.U...U.D", "ULFRBD"),
                ("U.D...D.UR.R...L.LF.B...F.BL.L...R.RB.F...B.FD.U...U.D", "ULFRBD"),
                ("U.D...D.UR.R...R.RF.B...B.FL.L...L.LB.F...F.BD.U...U.D", "ULFRBD"),
                ("U.D...U.DL.L...L.LF.B...F.BR.R...R.RF.B...F.BD.U...D.U", "ULFRBD"),
                ("U.D...U.DL.L...R.RF.B...F.BR.R...L.LF.B...F.BU.D...U.D", "ULFRBD"),
                ("U.D...U.DL.L...R.RF.F...B.BL.L...R.RB.B...F.FD.U...D.U", "ULFRBD"),
                ("U.D...U.DL.L...R.RF.F...F.FL.L...R.RB.B...B.BU.D...U.D", "ULFRBD"),
                ("U.D...U.DL.R...L.RB.B...F.FR.L...R.LB.B...F.FU.D...U.D", "ULFRBD"),
                ("U.D...U.DL.R...L.RB.F...B.FL.R...L.RF.B...F.BD.U...D.U", "ULFRBD"),
                ("U.D...U.DL.R...L.RB.F...F.BL.R...L.RF.B...B.FU.D...U.D", "ULFRBD"),
                ("U.D...U.DL.R...R.LB.B...F.FR.L...L.RB.B...F.FD.U...D.U", "ULFRBD"),
                ("U.D...U.DR.L...L.RF.F...B.BL.R...R.LF.F...B.BD.U...D.U", "ULFRBD"),
                ("U.D...U.DR.L...R.LF.B...B.FR.L...R.LB.F...F.BU.D...U.D", "ULFRBD"),
                ("U.D...U.DR.L...R.LF.B...F.BR.L...R.LB.F...B.FD.U...D.U", "ULFRBD"),
                ("U.D...U.DR.L...R.LF.F...B.BL.R...L.RF.F...B.BU.D...U.D", "ULFRBD"),
                ("U.D...U.DR.R...L.LB.B...B.BR.R...L.LF.F...F.FU.D...U.D", "ULFRBD"),
                ("U.D...U.DR.R...L.LB.B...F.FR.R...L.LF.F...B.BD.U...D.U", "ULFRBD"),
                ("U.D...U.DR.R...L.LB.F...B.FL.L...R.RB.F...B.FU.D...U.D", "ULFRBD"),
                ("U.D...U.DR.R...R.RB.F...B.FL.L...L.LB.F...B.FD.U...D.U", "ULFRBD"),
                ("U.U...D.DL.L...L.LB.B...F.FR.R...R.RB.B...F.FD.D...U.U", "ULFRBD"),
                ("U.U...D.DL.L...R.RB.B...F.FR.R...L.LB.B...F.FU.U...D.D", "ULFRBD"),
                ("U.U...D.DL.L...R.RB.F...B.FL.L...R.RF.B...F.BD.D...U.U", "ULFRBD"),
                ("U.U...D.DL.L...R.RB.F...F.BL.L...R.RF.B...B.FU.U...D.D", "ULFRBD"),
                ("U.U...D.DL.R...L.RF.B...F.BR.L...R.LF.B...F.BU.U...D.D", "ULFRBD"),
                ("U.U...D.DL.R...L.RF.F...B.BL.R...L.RB.B...F.FD.D...U.U", "ULFRBD"),
                ("U.U...D.DL.R...L.RF.F...F.FL.R...L.RB.B...B.BU.U...D.D", "ULFRBD"),
                ("U.U...D.DL.R...R.LF.B...F.BR.L...L.RF.B...F.BD.D...U.U", "ULFRBD"),
                ("U.U...D.DR.L...L.RB.F...B.FL.R...R.LB.F...B.FD.D...U.U", "ULFRBD"),
                ("U.U...D.DR.L...R.LB.B...B.BR.L...R.LF.F...F.FU.U...D.D", "ULFRBD"),
                ("U.U...D.DR.L...R.LB.B...F.FR.L...R.LF.F...B.BD.D...U.U", "ULFRBD"),
                ("U.U...D.DR.L...R.LB.F...B.FL.R...L.RB.F...B.FU.U...D.D", "ULFRBD"),
                ("U.U...D.DR.R...L.LF.B...B.FR.R...L.LB.F...F.BU.U...D.D", "ULFRBD"),
                ("U.U...D.DR.R...L.LF.B...F.BR.R...L.LB.F...B.FD.D...U.U", "ULFRBD"),
                ("U.U...D.DR.R...L.LF.F...B.BL.L...R.RF.F...B.BU.U...D.D", "ULFRBD"),
                ("U.U...D.DR.R...R.RF.F...B.BL.L...L.LF.F...B.BD.D...U.U", "ULFRBD"),
                ("U.U...U.UL.L...L.LF.F...F.FR.R...R.RB.B...B.BD.D...D.D", "ULFRBD"),
                ("U.U...U.UL.L...R.RF.F...B.BR.R...L.LB.B...F.FD.D...D.D", "ULFRBD"),
                ("U.U...U.UL.R...L.RB.F...B.FR.L...R.LF.B...F.BD.D...D.D", "ULFRBD"),
                ("U.U...U.UL.R...R.LB.F...F.BR.L...L.RF.B...B.FD.D...D.D", "ULFRBD"),
                ("U.U...U.UR.L...L.RF.B...B.FL.R...R.LB.F...F.BD.D...D.D", "ULFRBD"),
                ("U.U...U.UR.L...R.LF.B...F.BL.R...L.RB.F...B.FD.D...D.D", "ULFRBD"),
                ("U.U...U.UR.R...L.LB.B...F.FL.L...R.RF.F...B.BD.D...D.D", "ULFRBD"),
                ("U.U...U.UR.R...R.RB.B...B.BL.L...L.LF.F...F.FD.D...D.D", "ULFRBD"),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase4(BFS):
    """
    lookup-table-3x3x3-step140.txt
    ==============================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 6 entries (0 percent, 6.00x previous step)
    2 steps has 27 entries (0 percent, 4.50x previous step)
    3 steps has 120 entries (0 percent, 4.44x previous step)
    4 steps has 519 entries (0 percent, 4.33x previous step)
    5 steps has 1,932 entries (0 percent, 3.72x previous step)
    6 steps has 6,484 entries (0 percent, 3.36x previous step)
    7 steps has 20,310 entries (3 percent, 3.13x previous step)
    8 steps has 55,034 entries (8 percent, 2.71x previous step)
    9 steps has 113,892 entries (17 percent, 2.07x previous step)
    10 steps has 178,495 entries (26 percent, 1.57x previous step)
    11 steps has 179,196 entries (27 percent, 1.00x previous step)
    12 steps has 89,728 entries (13 percent, 0.50x previous step)
    13 steps has 16,176 entries (2 percent, 0.18x previous step)
    14 steps has 1,488 entries (0 percent, 0.09x previous step)
    15 steps has 144 entries (0 percent, 0.10x previous step)

    Total: 663,552 entries
    Average: 10.13 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase4",
            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'", "U", "U'", "D", "D'"),
            "3x3x3",
            "lookup-table-3x3x3-step140.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        U U U
        U U U
        U U U

 L L L  F F F  R R R  B B B
 L L L  F F F  R R R  B B B
 L L L  F F F  R R R  B B B

        D D D
        D D D
        D D D""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase4Edges(BFS):
    """
    lookup-table-3x3x3-step141-edges.txt
    ====================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 6 entries (0 percent, 6.00x previous step)
    2 steps has 27 entries (0 percent, 4.50x previous step)
    3 steps has 120 entries (1 percent, 4.44x previous step)
    4 steps has 519 entries (7 percent, 4.33x previous step)
    5 steps has 1,582 entries (22 percent, 3.05x previous step)
    6 steps has 2,911 entries (42 percent, 1.84x previous step)
    7 steps has 1,588 entries (22 percent, 0.55x previous step)
    8 steps has 158 entries (2 percent, 0.10x previous step)

    Total: 6,912 entries
    Average: 5.82 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase4-edges",
            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'", "U", "U'", "D", "D'"),
            "3x3x3",
            "lookup-table-3x3x3-step141-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        . U .
        U . U
        . U .

 . L .  . F .  . R .  . B .
 L . L  F . F  R . R  B . B
 . L .  . F .  . R .  . B .

        . D .
        D . D
        . D .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build333MicroPythonPhase4Corners(BFS):
    """
    lookup-table-3x3x3-step142-corners.txt
    ======================================
    0 steps has 1 entries (1 percent, 0.00x previous step)
    1 steps has 6 entries (6 percent, 6.00x previous step)
    2 steps has 27 entries (28 percent, 4.50x previous step)
    3 steps has 42 entries (43 percent, 1.56x previous step)
    4 steps has 20 entries (20 percent, 0.48x previous step)

    Total: 96 entries
    Average: 2.77 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "3x3x3-micropython-phase4-corners",
            # illegal moves
            ("R", "R'", "L", "L'", "F", "F'", "B", "B'", "U", "U'", "D", "D'"),
            "3x3x3",
            "lookup-table-3x3x3-step142-corners.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
        U . U
        . . .
        U . U

 L . L  F . F  R . R  B . B
 . . .  . . .  . . .  . . .
 L . L  F . F  R . R  B . B

        D . D
        . . .
        D . D""",
                    "ascii",
                ),
            ),
            use_c=True,
        )

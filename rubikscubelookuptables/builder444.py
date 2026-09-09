# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)


class Build444UDCentersStage(BFS):
    """
    lookup-table-4x4x4-step11-UD-centers-stage.txt
    ==============================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 4 entries (0 percent, 4.00x previous step)
    2 steps has 82 entries (0 percent, 20.50x previous step)
    3 steps has 1,206 entries (0 percent, 14.71x previous step)
    4 steps has 14,116 entries (1 percent, 11.70x previous step)
    5 steps has 123,404 entries (16 percent, 8.74x previous step)
    6 steps has 422,508 entries (57 percent, 3.42x previous step)
    7 steps has 173,254 entries (23 percent, 0.41x previous step)
    8 steps has 896 entries (0 percent, 0.01x previous step)

    Total: 735,471 entries
    Average: 6.03 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "4x4x4-UD-centers-stage",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step11-UD-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . x x .  . x x .  . x x .
 . x x .  . x x .  . x x .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""",
                    "ascii"),),
            use_c=True,
        )
        # fmt: on


class Build444LRCentersStage(BFS):
    """
    lookup-table-4x4x4-step12-LR-centers-stage.txt
    ==============================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 4 entries (0 percent, 4.00x previous step)
    2 steps has 82 entries (0 percent, 20.50x previous step)
    3 steps has 1,206 entries (0 percent, 14.71x previous step)
    4 steps has 14,116 entries (1 percent, 11.70x previous step)
    5 steps has 123,404 entries (16 percent, 8.74x previous step)
    6 steps has 422,508 entries (57 percent, 3.42x previous step)
    7 steps has 173,254 entries (23 percent, 0.41x previous step)
    8 steps has 896 entries (0 percent, 0.01x previous step)

    Total: 735,471 entries
    Average: 6.03 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "4x4x4-LR-centers-stage",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step12-LR-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . L L .  . x x .
 . L L .  . x x .  . L L .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""",
                    "ascii"),),
            use_c=True,
        )
        # fmt: on


class StartingStates444HighLowEdgesCenters(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-highlow-edges-centers",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "L", "L'", "R", "R'"),
            "4x4x4",
            "starting-states-lookup-table-4x4x4-step22-highlow-edges-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . R R .  . x x .
 . L L .  . x x .  . R R .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build444HighLowEdgesEdges(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-highlow-edges-edges",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'"),
            "4x4x4",
            "lookup-table-4x4x4-step21-highlow-edges-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . U D .
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D . . U  U . . D  D . . U  U . . D
 U . . D  D . . U  U . . D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
          . D U .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build444HighLowEdgesCenters(BFS):
    """
    lookup-table-4x4x4-step22-highlow-edges-centers.txt
    ===================================================
    0 steps has 12 entries (0 percent, 0.00x previous step)
    1 steps has 34 entries (0 percent, 2.83x previous step)
    2 steps has 384 entries (0 percent, 11.29x previous step)
    3 steps has 3,354 entries (0 percent, 8.73x previous step)
    4 steps has 22,324 entries (2 percent, 6.66x previous step)
    5 steps has 113,276 entries (12 percent, 5.07x previous step)
    6 steps has 338,860 entries (37 percent, 2.99x previous step)
    7 steps has 388,352 entries (43 percent, 1.15x previous step)
    8 steps has 34,048 entries (3 percent, 0.09x previous step)
    9 steps has 256 entries (0 percent, 0.01x previous step)

    Total: 900,900 entries
    Average: 6.32 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "444-highlow-edges-centers",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'"),
            "4x4x4",
            "lookup-table-4x4x4-step22-highlow-edges-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ('.....UU..UU..........LL..LL..........xx..xx..........RR..RR..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........LL..RR..........xx..xx..........LL..RR..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........LL..RR..........xx..xx..........RR..LL..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........LR..LR..........xx..xx..........LR..LR..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........LR..LR..........xx..xx..........RL..RL..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........LR..RL..........xx..xx..........RL..LR..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........RL..LR..........xx..xx..........LR..RL..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........RL..RL..........xx..xx..........LR..LR..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........RL..RL..........xx..xx..........RL..RL..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........RR..LL..........xx..xx..........LL..RR..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........RR..LL..........xx..xx..........RR..LL..........xx..xx..........UU..UU.....', 'ULFRBD'),
                ('.....UU..UU..........RR..RR..........xx..xx..........LL..LL..........xx..xx..........UU..UU.....', 'ULFRBD'),
            ),
            use_c=True,
        )
        # fmt: on


# =======================================================================
# phase 3
# pair 4 edges in the x-plane and put the LFRB centers into vertical bars
# =======================================================================


# We want the LFRB centers to be vertical bars, there should be 36 states
class StartingStates444Reduce333FirstTwoCenters(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-phase3-centers",
            # fmt: off
            (
                "Uw", "Uw'", "Uw2",
                "Dw", "Dw'", "Dw2",
                "Fw", "Fw'", "Bw",
                "Bw'", "Lw", "Lw'",
                "Rw", "Rw'",
                "L", "L'",
                "R", "R'",
                "U", "U'",
                "D", "D'",
                "F", "F'",
                "B", "B'",
            ),
            # fmt: on
            "4x4x4",
            "starting-states-lookup-table-4x4x4-step31-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . . . .
          . . . .
          . . . .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . B B .
 . L L .  . F F .  . R R .  . B B .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . . . .
          . . . .
          . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build444Reduce333FirstTwoCenters(BFS):
    """
    lookup-table-4x4x4-step31-centers.txt
    =====================================
    0 steps has 36 entries (4 percent, 0.00x previous step)
    1 steps has 80 entries (9 percent, 2.22x previous step)
    2 steps has 212 entries (25 percent, 2.65x previous step)
    3 steps has 288 entries (34 percent, 1.36x previous step)
    4 steps has 192 entries (22 percent, 0.67x previous step)
    5 steps has 32 entries (3 percent, 0.17x previous step)

    Total: 840 entries
    Average: 2.73 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "444-phase3-centers",
            ("Uw", "Uw'", "Lw", "Lw'", "Fw", "Fw'", "Rw", "Rw'", "Bw", "Bw'", "Dw", "Dw'", "L", "L'", "R", "R'"),
            "4x4x4",
            "lookup-table-4x4x4-step31-centers.txt",
            False,  # store_as_hex
            # starting cubes
            # fmt: off
            (
                ('.....................LL..LL..........BB..BB..........RR..RR..........FF..FF.....................', 'ULFRBD'),
                ('.....................LL..LL..........BF..BF..........RR..RR..........BF..BF.....................', 'ULFRBD'),
                ('.....................LL..LL..........BF..BF..........RR..RR..........FB..FB.....................', 'ULFRBD'),
                ('.....................LL..LL..........FB..FB..........RR..RR..........BF..BF.....................', 'ULFRBD'),
                ('.....................LL..LL..........FB..FB..........RR..RR..........FB..FB.....................', 'ULFRBD'),
                ('.....................LL..LL..........FF..FF..........RR..RR..........BB..BB.....................', 'ULFRBD'),
                ('.....................LR..LR..........BB..BB..........LR..LR..........FF..FF.....................', 'ULFRBD'),
                ('.....................LR..LR..........BB..BB..........RL..RL..........FF..FF.....................', 'ULFRBD'),
                ('.....................LR..LR..........BF..BF..........LR..LR..........BF..BF.....................', 'ULFRBD'),
                ('.....................LR..LR..........BF..BF..........LR..LR..........FB..FB.....................', 'ULFRBD'),
                ('.....................LR..LR..........BF..BF..........RL..RL..........BF..BF.....................', 'ULFRBD'),
                ('.....................LR..LR..........BF..BF..........RL..RL..........FB..FB.....................', 'ULFRBD'),
                ('.....................LR..LR..........FB..FB..........LR..LR..........BF..BF.....................', 'ULFRBD'),
                ('.....................LR..LR..........FB..FB..........LR..LR..........FB..FB.....................', 'ULFRBD'),
                ('.....................LR..LR..........FB..FB..........RL..RL..........BF..BF.....................', 'ULFRBD'),
                ('.....................LR..LR..........FB..FB..........RL..RL..........FB..FB.....................', 'ULFRBD'),
                ('.....................LR..LR..........FF..FF..........LR..LR..........BB..BB.....................', 'ULFRBD'),
                ('.....................LR..LR..........FF..FF..........RL..RL..........BB..BB.....................', 'ULFRBD'),
                ('.....................RL..RL..........BB..BB..........LR..LR..........FF..FF.....................', 'ULFRBD'),
                ('.....................RL..RL..........BB..BB..........RL..RL..........FF..FF.....................', 'ULFRBD'),
                ('.....................RL..RL..........BF..BF..........LR..LR..........BF..BF.....................', 'ULFRBD'),
                ('.....................RL..RL..........BF..BF..........LR..LR..........FB..FB.....................', 'ULFRBD'),
                ('.....................RL..RL..........BF..BF..........RL..RL..........BF..BF.....................', 'ULFRBD'),
                ('.....................RL..RL..........BF..BF..........RL..RL..........FB..FB.....................', 'ULFRBD'),
                ('.....................RL..RL..........FB..FB..........LR..LR..........BF..BF.....................', 'ULFRBD'),
                ('.....................RL..RL..........FB..FB..........LR..LR..........FB..FB.....................', 'ULFRBD'),
                ('.....................RL..RL..........FB..FB..........RL..RL..........BF..BF.....................', 'ULFRBD'),
                ('.....................RL..RL..........FB..FB..........RL..RL..........FB..FB.....................', 'ULFRBD'),
                ('.....................RL..RL..........FF..FF..........LR..LR..........BB..BB.....................', 'ULFRBD'),
                ('.....................RL..RL..........FF..FF..........RL..RL..........BB..BB.....................', 'ULFRBD'),
                ('.....................RR..RR..........BB..BB..........LL..LL..........FF..FF.....................', 'ULFRBD'),
                ('.....................RR..RR..........BF..BF..........LL..LL..........BF..BF.....................', 'ULFRBD'),
                ('.....................RR..RR..........BF..BF..........LL..LL..........FB..FB.....................', 'ULFRBD'),
                ('.....................RR..RR..........FB..FB..........LL..LL..........BF..BF.....................', 'ULFRBD'),
                ('.....................RR..RR..........FB..FB..........LL..LL..........FB..FB.....................', 'ULFRBD'),
                ('.....................RR..RR..........FF..FF..........LL..LL..........BB..BB.....................', 'ULFRBD'),
            ),
            # fmt: on,
            use_c=True,
        )


class Build444Reduce333FirstFourEdges(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-reduce333-edges",
            ("Uw", "Uw'", "Lw", "Lw'", "Fw", "Fw'", "Rw", "Rw'", "Bw", "Bw'", "Dw", "Dw'", "L", "L'", "R", "R'"),
            "4x4x4",
            "lookup-table-4x4x4-step32-first-four-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . - - .
          - . . -
          - . . -
          . - - .

 . - - .  . - - .  . - - .  . - - .
 L . . L  F . . F  R . . R  B . . B
 L . . L  F . . F  R . . R  B . . B
 . - - .  . - - .  . - - .  . - - .

          . - - .
          - . . -
          - . . -
          . - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


# phase 4
class Build444Reduce333Centers(BFS):
    """
    lookup-table-4x4x4-step41-centers.txt
    =====================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 4 entries (0 percent, 4.00x previous step)
    2 steps has 42 entries (1 percent, 10.50x previous step)
    3 steps has 244 entries (9 percent, 5.81x previous step)
    4 steps has 774 entries (30 percent, 3.17x previous step)
    5 steps has 878 entries (34 percent, 1.13x previous step)
    6 steps has 569 entries (22 percent, 0.65x previous step)
    7 steps has 8 entries (0 percent, 0.01x previous step)

    Total: 2,520 entries
    Average: 4.67 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "444-phase4-centers",
            # fmt: off
            (
                "Uw", "Uw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Rw", "Rw'",
                "Bw", "Bw'",
                "Dw", "Dw'",
                "L", "L'",
                "R", "R'",
                "Uw2",
                "Dw2",
                "F", "F'",
                "B", "B'",
            ),
            # fmt: on
            "4x4x4",
            "lookup-table-4x4x4-step41-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . B B .
 . L L .  . F F .  . R R .  . B B .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . D D .
          . D D .
          . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build444Reduce333LastEightEdges(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-phase4-edges",
            # fmt: off
            (
                "Uw", "Uw'",
                "Lw", "Lw'",
                "Fw", "Fw'",
                "Rw", "Rw'",
                "Bw", "Bw'",
                "Dw", "Dw'",
                "L", "L'",
                "R", "R'",
                "Uw2",
                "Dw2",
                "F", "F'",
                "B", "B'",
            ),
            # fmt: on
            "4x4x4",
            "lookup-table-4x4x4-step42-last-eight-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . U U .
          U . . U
          U . . U
          . U U .

 . L L .  . F F .  . R R .  . B B .
 - . . -  - . . -  - . . -  - . . -
 - . . -  - . . -  - . . -  - . . -
 . L L .  . F F .  . R R .  . B B .

          . D D .
          D . . D
          D . . D
          . D D .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )

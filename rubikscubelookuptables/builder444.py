# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)


class Build444Ultimate(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-ultimate",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step00-ultimate.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          U U U U
          U U U U
          U U U U
          U U U U

 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B

          D D D D
          D D D D
          D D D D
          D D D D""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build444UDCentersStage(BFS):
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


class StartingStates444LCentersStage(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "4x4x4-L-centers-stage",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "L", "L'", "R", "R'"),
            "4x4x4",
            "starting-states-lookup-table-4x4x4-step13-L-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . x x .  . x x .
 . L L .  . x x .  . x x .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""",
                    "ascii",
                ),
            ),
        )


class Build444LCentersStage(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "4x4x4-L-centers-stage",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step13-L-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ('.....xx..xx..........LL..LL..........xx..xx..........xx..xx..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........LL..xx..........xx..xx..........LL..xx..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........LL..xx..........xx..xx..........xx..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........Lx..Lx..........xx..xx..........Lx..Lx..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........Lx..Lx..........xx..xx..........xL..xL..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........Lx..xL..........xx..xx..........xL..Lx..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........xL..Lx..........xx..xx..........Lx..xL..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........xL..xL..........xx..xx..........Lx..Lx..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........xL..xL..........xx..xx..........xL..xL..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........xx..LL..........xx..xx..........LL..xx..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........xx..LL..........xx..xx..........xx..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
                ('.....xx..xx..........xx..xx..........xx..xx..........LL..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
            ),
            use_c=True,
        )
        # fmt: on


class Build444ULFRBDCentersStage(BFS):
    """
    I have not built this table but started it...it is the exact same as the 5x5x5 x-centers
    table which I have built which is

    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 6 entries (0 percent, 6.00x previous step)
    2 steps has 135 entries (0 percent, 22.50x previous step)
    3 steps has 2,286 entries (0 percent, 16.93x previous step)
    4 steps has 36,728 entries (0 percent, 16.07x previous step)
    5 steps has 562,932 entries (0 percent, 15.33x previous step)
    6 steps has 8,047,054 entries (0 percent, 14.29x previous step)
    7 steps has 105,823,666 entries (1 percent, 13.15x previous step)
    8 steps has 1,147,351,438 entries (12 percent, 10.84x previous step)
    9 steps has 5,653,730,364 entries (59 percent, 4.93x previous step)
    10 steps has 2,535,422,638 entries (26 percent, 0.45x previous step)
    11 steps has 14,534,522 entries (0 percent, 0.01x previous step)

    Total: 9,465,511,770 entries
    Average: 9.12 moves
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "4x4x4-ULFRBD-centers-stage",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . L L .  . F F .
 . L L .  . F F .  . L L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""",
                    "ascii"),),
            use_c=True,
        )
        # fmt: on


class StartingStates444HighLowEdges(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-highlow-edges",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "L", "L'", "R", "R'"),
            "4x4x4",
            "starting-states-lookup-table-4x4x4-step20-highlow-edges.txt",
            False,  # store_as_hex
            (
                (
                    """
          . U D .
          D U U U
          U U U D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U x x D  D R R U  U x x D
 U L L D  D x x U  U R R D  D x x U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D U U U
          U U U D
          . D U .""",
                    "ascii",
                ),
            ),
        )


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
        )
        # fmt: on


class Build444HighLowEdges(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "444-highlow-edges",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'"),
            "4x4x4",
            "lookup-table-4x4x4-step20-highlow-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ('.UD.DUUUUUUD.DU..DU.DLLUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUURRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DLRUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUULRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DRLUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUURLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
                ('.UD.DUUUUUUD.DU..DU.DRRUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUULLD.UD..DU.UxxDDxxU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
            ),
            use_centers_then_edges=True,
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
        )


class Build444Reduce333FirstTwoCenters(BFS):
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
            # fmt: on
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

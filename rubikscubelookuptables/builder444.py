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
                    "ascii")),
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
                    "ascii")),
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
            "starting-states-lookup-table-4x4x4-step21-highlow-edges-centers-new.txt",
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


class Build444HighLowEdgesEdgesPhase1(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "444-highlow-edges-edges",
            (),
            "4x4x4",
            "lookup-table-4x4x4-step14-highlow-edges-edges.txt",
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


class Build444ULFRBDCentersStage(BFS):
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
                    "ascii")),
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
          D . . U
          U . . D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U . . D  D R R U  U . . D
 U L L D  D . . U  U R R D  D . . U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D . . U
          U . . D
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
            "starting-states-lookup-table-4x4x4-step21-highlow-edges-centers.txt",
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
 . L L .  . . . .  . R R .  . . . .
 . L L .  . . . .  . R R .  . . . .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . . . .
          . . . .
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
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'"),
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
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'"),
            "4x4x4",
            "lookup-table-4x4x4-step22-highlow-edges-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (".....................LL..LL..........................RR..RR.....................................", "ULFRBD",),
                (".....................LL..RR..........................LL..RR.....................................", "ULFRBD",),
                (".....................LL..RR..........................RR..LL.....................................", "ULFRBD",),
                (".....................LR..LR..........................LR..LR.....................................", "ULFRBD",),
                (".....................LR..LR..........................RL..RL.....................................", "ULFRBD",),
                (".....................LR..RL..........................RL..LR.....................................", "ULFRBD",),
                (".....................RL..LR..........................LR..RL.....................................", "ULFRBD",),
                (".....................RL..RL..........................LR..LR.....................................", "ULFRBD",),
                (".....................RL..RL..........................RL..RL.....................................", "ULFRBD",),
                (".....................RR..LL..........................LL..RR.....................................", "ULFRBD",),
                (".....................RR..LL..........................RR..LL.....................................", "ULFRBD",),
                (".....................RR..RR..........................LL..LL.....................................", "ULFRBD",),
            ),
        )
        # fmt: on


class Build444HighLowEdges(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "444-highlow-edges",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'"),
            "4x4x4",
            "lookup-table-4x4x4-step20-highlow-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (".UD.D..UU..D.DU..DU.DLLUULLD.UD..DU.U..DD..U.UD..DU.DRRUURRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DLLUURRD.UD..DU.U..DD..U.UD..DU.DLLUURRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DLLUURRD.UD..DU.U..DD..U.UD..DU.DRRUULLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DLRUULRD.UD..DU.U..DD..U.UD..DU.DLRUULRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DLRUULRD.UD..DU.U..DD..U.UD..DU.DRLUURLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DLRUURLD.UD..DU.U..DD..U.UD..DU.DRLUULRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DRLUULRD.UD..DU.U..DD..U.UD..DU.DLRUURLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DRLUURLD.UD..DU.U..DD..U.UD..DU.DLRUULRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DRLUURLD.UD..DU.U..DD..U.UD..DU.DRLUURLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DRRUULLD.UD..DU.U..DD..U.UD..DU.DLLUURRD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DRRUULLD.UD..DU.U..DD..U.UD..DU.DRRUULLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
                (".UD.D..UU..D.DU..DU.DRRUURRD.UD..DU.U..DD..U.UD..DU.DLLUULLD.UD..DU.U..DD..U.UD..UD.D..UU..D.DU.", "ULFRBD",),
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

# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)


"""
phase 1
    stage LR centers
    10 moves

phase 2
    stage FB centers
    10 moves

phase 3 -
    EO the wings, 2,704,156 states
    EO the midges, 2048 states
    LR centers to 1/432, 4900 states

    (4900 * 2048) / (4900 * 2048 * 2,704,156) = 0.000 000 369
    10.8 moves

phase 4
    Move a group of 4-edges to x-plane and y-plane
    ~1 move

phase 5
    LR and FB centers to vertical bars
    pair x-plane edges

    432 LR center states
    4,900 FB center states

    x-plane high wings
        (8!/4!) = 1,680 is how many states the high wings can be in

    x-plane low wings
        (8!/4!) = 1,680 is how many states the low wings can be in

    x-plane midges
        8!/(4!*4!) = 70 is how many states the midges can be in

    A high-edge-midge prune table is 70 * 1680 = 117,600
    A low-edge-midge prune table is 70 * 1680 = 117,600
    A centers prune table is 432 * 4900 = 2,116,800
    A FB-centers-high-edge-midge prune table is 4900 * 117,600 = 576,240,000
        we can use this via a perfect-hash table

    576,240,000 / (432 * 4900 * 1680 * 1680 * 70) = 0.000 001 377

phase 6
    pair last 8 edges
    solve all centers

    8!^2/2 = 812,851,200 edge states
    6 * 6 * 4900 = 176,400 center states

    -16 moves
"""

"""
If we dropped phase 4 then phase 5 would become

    LR and FB centers to vertical bars
    pair x-plane edges

    432 LR center states
    4,900 FB center states

    high wings
        (12!/8!) = 11,800 is how many states the high wings can be in

    low wings
        (12!/8!) = 11,800 is how many states the low wings can be in

    midges
        8!/(12!*4!) = 495 is how many states the midges can be in

    A high-edge-midge prune table is 495 * 11800 = 5,841,000
    A low-edge-midge prune table is 495 * 11800 = 5,841,000
    A centers prune table is 432 * 4900 = 2,116,800

    But there wouldn't be two tables we could use to create a perfect-hash...heck the current
    phase 5 is super slow if you don't use the perfect-hash
"""


# =======
# phase 1
# =======
class Build555LRCenterStage(BFS):
    """
    1 steps has 5 entries (0 percent, 0.00x previous step)
    2 steps has 98 entries (0 percent, 19.60x previous step)
    3 steps has 2,036 entries (0 percent, 20.78x previous step)
    4 steps has 41,096 entries (0 percent, 20.18x previous step)
    5 steps has 824,950 entries (4 percent, 20.07x previous step)
    6 steps has 16,300,291 entries (94 percent, 19.76x previous step)

    # extrapolate from here
    7 steps has 309,053,517 entries (18.96x previous step)
    8 steps has 5,612,411,868 entries (18.16x previous step)
    9 steps has 97,431,470,028 entries (17.36x previous step)
    10 steps has 437,547,487,952 entries (4.49x previous step)

    Average: 9.79709452838934
    Total  : 540,917,591,841
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step10-LR-centers-stage.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . x x x .  . L L L .  . x x x .
 . L L L .  . x x x .  . L L L .  . x x x .
 . L L L .  . x x x .  . L L L .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555LRCenterStageTCenter(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-t-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step11-LR-centers-stage-t-center-only.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . L . .  . . x . .  . . L . .  . . x . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . L . .  . . x . .  . . L . .  . . x . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555LRCenterStageXCenter(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-x-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step12-LR-centers-stage-x-center-only.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . x . x .  . L . L .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555CenterStageOnePhase(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step14-centers-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U U U .
            . U . U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . x x x .  . L L L .  . x x x .
 . L . L .  . x . x .  . L . L .  . x . x .
 . L L L .  . x x x .  . L L L .  . x x x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . U U U .
            . U . U .
            . U U U .
            . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build555CenterStageTCenterOnly(BFS):
    """
    The total here should have been 9,465,511,770...somehow it missed 22 entries

    /storage/dwalton76/lookup-table-5x5x5-step15-centers-stage-t-center-only.txt
    ============================================================================
    0 steps has 1 entries (0 percent, 0.00x previous step)
    1 steps has 6 entries (0 percent, 6.00x previous step)
    2 steps has 123 entries (0 percent, 20.50x previous step)
    3 steps has 2,166 entries (0 percent, 17.61x previous step)
    4 steps has 35,280 entries (0 percent, 16.29x previous step)
    5 steps has 586,600 entries (0 percent, 16.63x previous step)
    6 steps has 9,252,143 entries (0 percent, 15.77x previous step)
    7 steps has 130,941,778 entries (1 percent, 14.15x previous step)
    8 steps has 1,297,964,554 entries (13 percent, 9.91x previous step)
    9 steps has 5,192,860,806 entries (54 percent, 4.00x previous step)
    10 steps has 2,775,063,476 entries (29 percent, 0.53x previous step)
    11 steps has 58,804,680 entries (0 percent, 0.02x previous step)
    12 steps has 135 entries (0 percent, 0.00x previous step)

    Total: 9,465,511,748 entries
    Average: 9.14 moves
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-t-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step15-centers-stage-t-center-only.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . L . .  . . F . .  . . L . .  . . F . .
 . L . L .  . F . F .  . L . L .  . F . F .
 . . L . .  . . F . .  . . L . .  . . F . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build555CenterStageXCenterOnly(BFS):
    """
    /storage/dwalton76/lookup-table-5x5x5-step16-centers-stage-x-center-only.txt
    ============================================================================
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
        BFS.__init__(
            self,
            "5x5x5-x-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step16-centers-stage-x-center-only.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U . U .
            . . . . .
            . U . U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . F . F .  . L . L .  . F . F .
 . . . . .  . . . . .  . . . . .  . . . . .
 . L . L .  . F . F .  . L . L .  . F . F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . U . U .
            . . . . .
            . U . U .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555UDCenterStageTCenter(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-UD-t-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step17-UD-centers-stage-t-center-only.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . x . .  . . x . .  . . x . .  . . x . .
 . x . x .  . x . x .  . x . x .  . x . x .
 . . x . .  . . x . .  . . x . .  . . x . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555UDCenterStageXCenter(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-UD-x-center-stage",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step18-UD-centers-stage-x-center-only.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U . U .
            . . . . .
            . U . U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . x . x .  . x . x .  . x . x .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .
 . x . x .  . x . x .  . x . x .  . x . x .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . U . U .
            . . . . .
            . U . U .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


# =======
# phase 2
# =======
class Build555FBCenterStage(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-FB-center-stage",
            ("Uw", "Uw'", "L", "L'", "L2", "Fw", "Fw'", "R", "R'", "R2", "Bw", "Bw'", "Dw", "Dw'"),
            "5x5x5",
            "lookup-table-5x5x5-step20-FB-centers-stage.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . F F F .  . . . . .  . F F F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x x x .
            . x x x .
            . x x x .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555FBTCenterStage(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-FB-t-center-stage",
            ("Uw", "Uw'", "L", "L'", "L2", "Fw", "Fw'", "R", "R'", "R2", "Bw", "Bw'", "Dw", "Dw'"),
            "5x5x5",
            "lookup-table-5x5x5-step21-FB-t-centers-stage.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . F . .  . . . . .  . . F . .
 . . . . .  . F . F .  . . . . .  . F . F .
 . . . . .  . . F . .  . . . . .  . . F . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . x . .
            . x . x .
            . . x . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555FBXCenterStage(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-FB-x-center-stage",
            ("Uw", "Uw'", "L", "L'", "L2", "Fw", "Fw'", "R", "R'", "R2", "Bw", "Bw'", "Dw", "Dw'"),
            "5x5x5",
            "lookup-table-5x5x5-step22-FB-x-centers-stage.txt",
            True,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F . F .  . . . . .  . F . F .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F . F .  . . . . .  . F . F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . x . x .
            . . . . .
            . x . x .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


# =======
# phase 3
# =======
class StartingState555EdgeOrientOuterOrbitLRCenterStage(BFS):
    """
    There should be 432 of them
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-center-stage-EO-both-orbits",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "L", "L'", "R", "R'"),
            "5x5x5",
            "starting-states-lookup-table-5x5x5-step900-edge-orient-LR-center-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . U U D .
            D . . . U
            U . . . U
            U . . . D
            . D U U .

 . D U U .  . D U U .  . D U U .  . D U U .
 D L L L U  U . . . D  D R R R U  U . . . D
 U L L L U  U . . . U  U R R R U  U . . . U
 U L L L D  D . . . U  U R R R D  D . . . U
 . U U D .  . U U D .  . U U D .  . U U D .

            . U U D .
            D . . . U
            U . . . U
            U . . . D
            . D U U .""",
                    "ascii",
                ),
            ),
        )


class Build555LRCenterStageEOBothOrbits(BFS):
    """
    2048 * 4900 * 2704156 = 27,136,746,291,200

    lookup-table-5x5x5-step900-edge-orient-LR-center-stage.txt
    ==========================================================
    0 steps has 78 entries (0 percent, 0.00x previous step)
    1 steps has 1,218 entries (0 percent, 15.62x previous step)
    2 steps has 14,256 entries (0 percent, 11.70x previous step)
    3 steps has 172,288 entries (0 percent, 12.09x previous step)
    4 steps has 1,948,920 entries (7 percent, 11.31x previous step)
    5 steps has 24,348,560 entries (91 percent, 12.49x previous step)
    extrapolate from here
    6 steps has 291,939,234 entries (11.99x previous step)
    7 steps has 3,354,381,798 entries (11.49x previous step)
    8 steps has 36,864,655,960 entries (10.99x previous step)
    9 steps has 386,710,241,020 entries (10.49x previous step)
    10 steps has 3,863,235,307,789 entries (9.99x previous step)
    11 steps has 22,846,263,280,079 entries (5.91x previous step)

    Average: 10.824502972151256
    Total  : 27,136,746,291,200

    phase1+2 ~20 moves
    phase3 11.5 moves
    phase4 ~14 moves
    phase5 ~16 moves
    solve 333 20 moves

    81.5 total
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-center-stage-EO-both-orbits",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'"),
            "5x5x5",
            "lookup-table-5x5x5-step900-edge-orient-LR-center-stage.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLLRUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRLUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DLRRUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRLRUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUULLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRRUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUURRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRRUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLLUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUURRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUULLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUULRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLRUULRLUULLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRLUURLRUURRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLLUULRLUURLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUULLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRRUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLLUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUURRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURRRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULLLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRRRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUURLRD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUULRLD.UUD..DUU.U...DU...UD...U.UUD..DUU.DRLRUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUULRLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUURLRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLRLUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
                (
                    ".UUD.D...UU...UU...D.DUU..DUU.DRRRUURLRUURRRD.UUD..DUU.U...DU...UD...U.UUD..DUU.DLLLUULRLUULLLD.UUD..DUU.U...DU...UD...U.UUD..UUD.D...UU...UU...D.DUU.",
                    "ULFRBD",
                ),
            ),
        )


class StartingStates555LRCenterStageEOInnerOrbit(BFS):
    """
    There should be 432 of them
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-center-stage-EO-inner-orbit",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "L", "L'", "R", "R'"),
            "5x5x5",
            "starting-states-lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . U . .
            . . . . .
            U . . . U
            . . . . .
            . . U . .

 . . U . .  . . U . .  . . U . .  . . U . .
 . L L L .  . . . . .  . R R R .  . . . . .
 U L L L U  U . . . U  U R R R U  U . . . U
 . L L L .  . . . . .  . R R R .  . . . . .
 . . U . .  . . U . .  . . U . .  . . U . .

            . . U . .
            . . . . .
            U . . . U
            . . . . .
            . . U . .""",
                    "ascii",
                ),
            ),
        )


class Build555LRCenterStageEOInnerOrbit(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-center-stage-EO-inner-orbit",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'"),
            "5x5x5",
            "lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.LRL...U....U.......U...U.......U....U...RRR.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.RLR...U....U.......U...U.......U....U...RRR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLLU.RRR...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.LRL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.ULLRU.RRR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.LRL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLLU.RRR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.LRL...U....U.......U...U.......U....U...RRR.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.RLR...U....U.......U...U.......U....U...RRR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLL.URLRU.RRR...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.LLR...U....U.......U...U.......U....U...RRL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.LRR...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLLU.RRL...U....U.......U...U.......U....U...RRL.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.LRR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.ULLRU.RRL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.LRR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLLU.RRL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.LLR...U....U.......U...U.......U....U...RRL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.LRR...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LLR.URLRU.RRL...U....U.......U...U.......U....U...RRL.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.LLL...U....U.......U...U.......U....U...RLR.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.RLR...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLLU.RRR...U....U.......U...U.......U....U...RLR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.ULLRU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RLR.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RLR...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLLU.RRR...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.LLL...U....U.......U...U.......U....U...RLR.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.RLR...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRL.URLRU.RRR...U....U.......U...U.......U....U...RLR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.LLR...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.LRR...U....U.......U...U.......U....U...RLL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.RLL...U....U.......U...U.......U....U...RLL.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LLR...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.LRR...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RLL.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.LLR...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.LRR...U....U.......U...U.......U....U...RLL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.RLL...U....U.......U...U.......U....U...RLL.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...LRR.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.LRR...U....U.......U...U.......U....U...LRR.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.RLL...U....U.......U...U.......U....U...LRR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLLU.RRL...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.LRR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.ULLRU.RRL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.LRR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLLU.RRL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.LRR...U....U.......U...U.......U....U...LRR.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.RLL...U....U.......U...U.......U....U...LRR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLL.URLRU.RRL...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.LLL...U....U.......U...U.......U....U...LRL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.LRL...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLLU.RRR...U....U.......U...U.......U....U...LRL.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.LRL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.ULLRU.RRR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.LRL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLLU.RRR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.LLL...U....U.......U...U.......U....U...LRL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.LRL...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RLR.URLRU.RRR...U....U.......U...U.......U....U...LRL.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.LLR...U....U.......U...U.......U....U...LLR.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.LLR...U....U.......U...U.......U....U...LRR.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.LRR...U....U.......U...U.......U....U...LLR.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...LLR.URRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...LRR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...RLL.URRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.RLL...U....U.......U...U.......U....U...RRL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.RRL...U....U.......U...U.......U....U...LLR.URRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLLU.RRL...U....U.......U...U.......U....U...RLL.URRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.ULLRU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LLR.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LLR.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LRR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.LLR...U....U.......U...U.......U....U...LRR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.LRR...U....U.......U...U.......U....U...LLR.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.LRR...U....U.......U...U.......U....U...LLR.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LLR.ULRRU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LLR.URRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LRR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...LRR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RLL.ULRRU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RLL.URRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RRL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RLL...U....U.......U...U.......U....U...RRL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...LLR.ULRRU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...LLR.URRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...RLL.ULRRU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLLU.RRL...U....U.......U...U.......U....U...RLL.URRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.LLR...U....U.......U...U.......U....U...LLR.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.LLR...U....U.......U...U.......U....U...LRR.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.LRR...U....U.......U...U.......U....U...LLR.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...LLR.ULRLU.LRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...LRR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...RLL.ULRLU.RRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.RLL...U....U.......U...U.......U....U...RRL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.RRL...U....U.......U...U.......U....U...LLR.ULRLU.LLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRL.URLRU.RRL...U....U.......U...U.......U....U...RLL.ULRLU.RLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...LLL.URRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...LRL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...RLR.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.LLL...U....U.......U...U.......U....U...RRR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.LRL...U....U.......U...U.......U....U...LLL.URRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.LRL...U....U.......U...U.......U....U...RLR.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.RLR...U....U.......U...U.......U....U...LLL.URRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.RLR...U....U.......U...U.......U....U...LRL.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLLU.RRR...U....U.......U...U.......U....U...LLL.URRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.ULLRU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LLL.ULRRU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LLL.URRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LRL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...LRL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RLR.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RLR.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RRR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LLL...U....U.......U...U.......U....U...RRR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...LLL.ULRRU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...LLL.URRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...RLR.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.LRL...U....U.......U...U.......U....U...RLR.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LLL.ULRRU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LLL.URRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LRL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.RLR...U....U.......U...U.......U....U...LRL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.RRR...U....U.......U...U.......U....U...LLL.ULRRU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLLU.RRR...U....U.......U...U.......U....U...LLL.URRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...LLL.ULRLU.RRR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...LRL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...RLR.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.LLL...U....U.......U...U.......U....U...RRR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.LRL...U....U.......U...U.......U....U...LLL.ULRLU.RLR...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.LRL...U....U.......U...U.......U....U...RLR.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.RLR...U....U.......U...U.......U....U...LLL.ULRLU.LRL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.RLR...U....U.......U...U.......U....U...LRL.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
                (
                    "..U.......U...U.......U....U...RRR.URLRU.RRR...U....U.......U...U.......U....U...LLL.ULRLU.LLL...U....U.......U...U.......U....U.......U...U.......U..",
                    "ULFRBD",
                ),
            ),
        )


class Build555EdgeOrientOuterOrbit(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-EO-outer-orbit",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'"),
            "5x5x5",
            "lookup-table-5x5x5-step902-EO-outer-orbit.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . U . D .
            D . . . U
            . . . . .
            U . . . D
            . D . U .

 . D . U .  . D . U .  . D . U .  . D . U .
 D . . . U  U . . . D  D . . . U  U . . . D
 . . . . .  . . . . .  . . . . .  . . . . .
 U . . . D  D . . . U  U . . . D  D . . . U
 . U . D .  . U . D .  . U . D .  . U . D .

            . U . D .
            D . . . U
            . . . . .
            U . . . D
            . D . U .""",
                    "ascii",
                ),
            ),
        )


# =======
# phase 4
# =======
class StartingStatesBuild555Phase4(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase4",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "starting-states-lookup-table-5x5x5-step40-phase4.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .

 . x x x .  . x x x .  . x x x .  . x x x .
 L . . . L  L . . . L  L . . . L  L . . . L
 L . . . L  L . . . L  L . . . L  L . . . L
 L . . . L  L . . . L  L . . . L  L . . . L
 . x x x .  . x x x .  . x x x .  . x x x .

            . x x x .
            x . . . x
            x . . . x
            x . . . x
            . x x x .""",
                    "ascii",
                ),
            ),
        )


class Build555Phase4(BFS):
    """
    Move one group of 4-edges out of the z-plane
    """

    def __init__(self):

        # rubiks cube libraries
        from rubikscubelookuptables.builder555ss import starting_states_phase4

        BFS.__init__(
            self,
            "5x5x5-phase4",
            ("Uw", "Uw'", "Dw", "Dw'", "Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "L", "L'", "R", "R'"),
            "5x5x5",
            "lookup-table-5x5x5-step40-phase4.txt",
            True,  # store_as_hex
            starting_states_phase4,
        )


# =======
# phase 5
# =======
class StartingStatesBuild555Phase5Centers(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-centers",
            (
                "Uw",
                "Uw'",
                "Uw2",
                "Dw",
                "Dw'",
                "Dw2",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
                "F",
                "F'",
                "B",
                "B'",
            ),
            "5x5x5",
            "starting-states-lookup-table-5x5x5-step51-phase5-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555Phase5Centers(BFS):
    """
    432 * 4900 = 2,116,800 states
    """

    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "5x5x5-phase5-centers",
            (
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",
                "Lw", "Lw'",
                "Rw", "Rw'",
                "L", "L'",
                "R", "R'",
                "U", "U'",
                "D", "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step51-phase5-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ("...............................LLL..LLL..LLL............BFB..BFB..BFB............RRR..RRR..RRR............FBF..FBF..FBF...............................", "ULFRBD",),
                ("...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................LLL..LLL..LLL............BFF..BFF..BFF............RRR..RRR..RRR............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................LLL..LLL..LLL............FFB..FFB..FFB............RRR..RRR..RRR............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................LLL..LLL..LLL............FFF..FFF..FFF............RRR..RRR..RRR............BBB..BBB..BBB...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............BFB..BFB..BFB............LRR..LRR..LRR............FBF..FBF..FBF...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............BFB..BFB..BFB............RRL..RRL..RRL............FBF..FBF..FBF...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............BFF..BFF..BFF............LRR..LRR..LRR............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............BFF..BFF..BFF............LRR..LRR..LRR............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............BFF..BFF..BFF............RRL..RRL..RRL............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............BFF..BFF..BFF............RRL..RRL..RRL............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............FFB..FFB..FFB............LRR..LRR..LRR............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............FFB..FFB..FFB............LRR..LRR..LRR............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............FFB..FFB..FFB............RRL..RRL..RRL............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............FFB..FFB..FFB............RRL..RRL..RRL............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB...............................", "ULFRBD",),
                ("...............................LLR..LLR..LLR............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............BFB..BFB..BFB............LRR..LRR..LRR............FBF..FBF..FBF...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............BFB..BFB..BFB............RRL..RRL..RRL............FBF..FBF..FBF...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............BFF..BFF..BFF............LRR..LRR..LRR............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............BFF..BFF..BFF............LRR..LRR..LRR............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............BFF..BFF..BFF............RRL..RRL..RRL............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............BFF..BFF..BFF............RRL..RRL..RRL............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............FFB..FFB..FFB............LRR..LRR..LRR............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............FFB..FFB..FFB............LRR..LRR..LRR............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............FFB..FFB..FFB............RRL..RRL..RRL............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............FFB..FFB..FFB............RRL..RRL..RRL............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............FFF..FFF..FFF............LRR..LRR..LRR............BBB..BBB..BBB...............................", "ULFRBD",),
                ("...............................RLL..RLL..RLL............FFF..FFF..FFF............RRL..RRL..RRL............BBB..BBB..BBB...............................", "ULFRBD",),
                ("...............................RLR..RLR..RLR............BFB..BFB..BFB............LRL..LRL..LRL............FBF..FBF..FBF...............................", "ULFRBD",),
                ("...............................RLR..RLR..RLR............BFF..BFF..BFF............LRL..LRL..LRL............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................RLR..RLR..RLR............BFF..BFF..BFF............LRL..LRL..LRL............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................RLR..RLR..RLR............FFB..FFB..FFB............LRL..LRL..LRL............BBF..BBF..BBF...............................", "ULFRBD",),
                ("...............................RLR..RLR..RLR............FFB..FFB..FFB............LRL..LRL..LRL............FBB..FBB..FBB...............................", "ULFRBD",),
                ("...............................RLR..RLR..RLR............FFF..FFF..FFF............LRL..LRL..LRL............BBB..BBB..BBB...............................", "ULFRBD",),
            ),
        )
        # fmt: on


class Build555Phase5ThreeEdges(BFS):
    """
    (8*7*6)^2 = 112,896 is how many states the wings can be in
    8!/(3!*5!) = 56 is how many states the midges can be in
    112,896 * 70 = 6,322,176
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-three-edges",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step55-phase5-three-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F . . . F  R . . . R  B . . . -
 - . . . L  F . . . F  R . . . R  B . . . -
 - . . . L  F . . . F  R . . . R  B . . . -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase5Edges(BFS):
    """
    (8*7*6*5)^2 = 2822400 is how many states the wings can be in
    8!/(4!*4!) = 70 is how many states the midges can be in
    2,822,400 * 70 = 197,568,000
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-edges",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step52-phase5-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase5HighEdgeMidge(BFS):
    """
    (8*7*6*5)*70 = 117,600 states
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-high-edge-and-midge",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step53-phase5-high-edge-and-midge.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F . . . -  - . . . R  B . . . -
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . -  - . . . F  R . . . -  - . . . B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase5LowEdgeMidge(BFS):
    """
    (8*7*6*5)*70 = 117,600 states
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-low-edge-and-midge",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step54-phase5-low-edge-and-midge.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . -  - . . . F  R . . . -  - . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 - . . . L  F . . . -  - . . . R  B . . . -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase5FBCentersHighEdgeMidge(BFS):
    """
    (8*7*6*5)*70 = 117,600 states
    4,900 FB centers
    117,600 * 4,900 = 576,240,000
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-fb-centers-high-edge-and-midge",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step55-phase5-fb-centers-high-edge-and-midge.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F B F B -  - . . . R  B F B F -
 L . . . L  F B F B F  R . . . R  B F B F B
 L . . . -  - B F B F  R . . . -  - F B F B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F B F F -  - . . . R  B B B F -
 L . . . L  F B F F F  R . . . R  B B B F B
 L . . . -  - B F F F  R . . . -  - B B F B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F B F F -  - . . . R  B F B B -
 L . . . L  F B F F F  R . . . R  B F B B B
 L . . . -  - B F F F  R . . . -  - F B B B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F F F B -  - . . . R  B B B F -
 L . . . L  F F F B F  R . . . R  B B B F B
 L . . . -  - F F B F  R . . . -  - B B F B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F F F B -  - . . . R  B F B B -
 L . . . L  F F F B F  R . . . R  B F B B B
 L . . . -  - F F B F  R . . . -  - F B B B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 - . . . L  F F F F -  - . . . R  B B B B -
 L . . . L  F F F F F  R . . . R  B B B B B
 L . . . -  - F F F F  R . . . -  - B B B B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase5FBCentersLowEdgeMidge(BFS):
    """
    (8*7*6*5)*70 = 117,600 states
    4,900 FB centers
    117,600 * 4,900 = 576,240,000
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-fb-centers-low-edge-and-midge",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step57-phase5-fb-centers-low-edge-and-midge.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . -  - B F B F  R . . . -  - F B F B
 L . . . L  F B F B F  R . . . R  B F B F B
 - . . . L  F B F B -  - . . . R  B F B F -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . -  - B F F F  R . . . -  - B B F B
 L . . . L  F B F F F  R . . . R  B B B F B
 - . . . L  F B F F -  - . . . R  B B B F -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . -  - B F F F  R . . . -  - F B B B
 L . . . L  F B F F F  R . . . R  B F B B B
 - . . . L  F B F F -  - . . . R  B F B B -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . -  - F F B F  R . . . -  - B B F B
 L . . . L  F F F B F  R . . . R  B B B F B
 - . . . L  F F F B -  - . . . R  B B B F -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . -  - F F B F  R . . . -  - F B B B
 L . . . L  F F F B F  R . . . R  B F B B B
 - . . . L  F F F B -  - . . . R  B F B B -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . -  - F F F F  R . . . -  - B B B B
 L . . . L  F F F F F  R . . . R  B B B B B
 - . . . L  F F F F -  - . . . R  B B B B -
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase5FBCenters(BFS):
    """
    4,900 FB centers
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase5-fb-centers",
            (
                "Uw",
                "Uw'",
                "Dw",
                "Dw'",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "U",
                "U'",
                "D",
                "D'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step56-phase5-fb-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . B F B .  . . . . .  . F B F .
 . . . . .  . B F B .  . . . . .  . F B F .
 . . . . .  . B F B .  . . . . .  . F B F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . B F F .  . . . . .  . B B F .
 . . . . .  . B F F .  . . . . .  . B B F .
 . . . . .  . B F F .  . . . . .  . B B F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . B F F .  . . . . .  . F B B .
 . . . . .  . B F F .  . . . . .  . F B B .
 . . . . .  . B F F .  . . . . .  . F B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F B .  . . . . .  . B B F .
 . . . . .  . F F B .  . . . . .  . B B F .
 . . . . .  . F F B .  . . . . .  . B B F .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F B .  . . . . .  . F B B .
 . . . . .  . F F B .  . . . . .  . F B B .
 . . . . .  . F F B .  . . . . .  . F B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


# =======
# phase 6
# =======
# - pair last 8-edges in y-plane and z-plane
# - solve center (LR and FB will be vertical bars)
class Build555PairLastEightEdgesEdgesOnly(BFS):
    """
    Should be (8!^2)/2 812,851,200
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-pair-last-eight-edges-edges-only",
            # illegal moves
            (
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "Uw",
                "Uw'",
                "Uw2",
                "Dw",
                "Dw'",
                "Dw2",
                "L",
                "L'",
                "R",
                "R'",
                "F",
                "F'",
                "B",
                "B'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step501-pair-last-eight-edges-edges-only.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . U U U .
            U . . . U
            U . . . U
            U . . . U
            . U U U .

 . L L L .  . F F F .  . R R R .  . B B B .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . L L L .  . F F F .  . R R R .  . B B B .

            . D D D .
            D . . . D
            D . . . D
            D . . . D
            . D D D .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555PairLastEightEdgesCentersOnly(BFS):
    """
    Should be 6 x 6 x 4900 = 176,400
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-pair-last-eight-edges-centers-only",
            # illegal moves
            (
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "Uw",
                "Uw'",
                "Uw2",
                "Dw",
                "Dw'",
                "Dw2",
                "L",
                "L'",
                "R",
                "R'",
                "F",
                "F'",
                "B",
                "B'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step502-pair-last-eight-edges-centers-only.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555PairLastEightEdges(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-pair-last-eight-edges",
            # illegal moves
            (
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "Uw",
                "Uw'",
                "Uw2",
                "Dw",
                "Dw'",
                "Dw2",
                "L",
                "L'",
                "R",
                "R'",
                "F",
                "F'",
                "B",
                "B'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step500-pair-last-eight-edges.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . U U U .
            U U U U U
            U U U U U
            U U U U U
            . U U U .

 . L L L .  . F F F .  . R R R .  . B B B .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . L L L .  . F F F .  . R R R .  . B B B .

            . D D D .
            D D D D D
            D D D D D
            D D D D D
            . D D D .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase6Centers(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase6-centers",
            (
                "Uw",
                "Uw'",
                "Uw2",
                "Dw",
                "Dw'",
                "Dw2",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "F",
                "F'",
                "B",
                "B'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step61-phase6-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555Phase6HighEdgeMidge(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase6-high-edge-midge",
            (
                "Uw",
                "Uw'",
                "Uw2",
                "Dw",
                "Dw'",
                "Dw2",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "F",
                "F'",
                "B",
                "B'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step62-phase6-high-edge-midge.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . U U - .
            - . . . U
            U . . . U
            U . . . -
            . - U U .

 . - L L .  . - F F .  . - R R .  . - B B .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . L L - .  . F F - .  . R R - .  . B B - .

            . D D - .
            - . . . D
            D . . . D
            D . . . -
            . - D D .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


class Build555Phase6LowEdgeMidge(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-phase6-low-edge-midge",
            (
                "Uw",
                "Uw'",
                "Uw2",
                "Dw",
                "Dw'",
                "Dw2",
                "Fw",
                "Fw'",
                "Bw",
                "Bw'",
                "Lw",
                "Lw'",
                "Rw",
                "Rw'",
                "L",
                "L'",
                "R",
                "R'",
                "F",
                "F'",
                "B",
                "B'",
            ),
            "5x5x5",
            "lookup-table-5x5x5-step63-phase6-low-edge-midge.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . - U U .
            U . . . -
            U . . . U
            - . . . U
            . U U - .

 . L L - .  . F F - .  . R R - .  . B B - .
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 - . . . -  - . . . -  - . . . -  - . . . -
 . - L L .  . - F F .  . - R R .  . - B B .

            . - D D .
            D . . . -
            D . . . D
            - . . . D
            . D D - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
        )


# ================
# ultimate 5x5x5
# ultimate centers
# ================
class Build555Ultimate(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-ultimate",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step00-ultimate.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            U U U U U
            U U U U U
            U U U U U
            U U U U U
            U U U U U

 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B

            D D D D D
            D D D D D
            D D D D D
            D D D D D
            D D D D D""",
                    "ascii",
                ),
            ),
            use_c=True,
        )


class Build555UltimateCenters(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-ultimate",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step00-ultimate-centers.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""",
                    "ascii",
                ),
            ),
            legal_moves=(
                # OBTM 36 moves
                "U",
                "U'",
                "U2",
                "Uw",
                "Uw'",
                "Uw2",
                "L",
                "L'",
                "L2",
                "Lw",
                "Lw'",
                "Lw2",
                "F",
                "F'",
                "F2",
                "Fw",
                "Fw'",
                "Fw2",
                "R",
                "R'",
                "R2",
                "Rw",
                "Rw'",
                "Rw2",
                "B",
                "B'",
                "B2",
                "Bw",
                "Bw'",
                "Bw2",
                "D",
                "D'",
                "D2",
                "Dw",
                "Dw'",
                "Dw2",
                # SSTM 36 moves
                # "U", "U'", "U2",
                # "L", "L'", "L2",
                # "F" , "F'", "F2",
                # "R" , "R'", "R2",
                # "B" , "B'", "B2",
                # "D" , "D'", "D2",
                # "2U", "2U'", "2U2", "2D", "2D'", "2D2",
                # "2L", "2L'", "2L2", "2R", "2R'", "2R2",
                # "2F", "2F'", "2F2", "2B", "2B'", "2B2"
                # BTM is both, 54 moves
                # "U", "U'", "U2", "Uw", "Uw'", "Uw2",
                # "L", "L'", "L2", "Lw", "Lw'", "Lw2",
                # "F" , "F'", "F2", "Fw", "Fw'", "Fw2",
                # "R" , "R'", "R2", "Rw", "Rw'", "Rw2",
                # "B" , "B'", "B2", "Bw", "Bw'", "Bw2",
                # "D" , "D'", "D2", "Dw", "Dw'", "Dw2",
                # "2U", "2U'", "2U2", "2D", "2D'", "2D2",
                # "2L", "2L'", "2L2", "2R", "2R'", "2R2",
                # "2F", "2F'", "2F2", "2B", "2B'", "2B2"
            ),
            use_c=True,
        )


# ======================
# Centers Solve Unstaged
# ======================
# This was used to build the 5x5x5-pair-last-four-edges table
class Build555ULFRBDCenterSolveUnstaged(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-centers-solve-unstaged",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step30-ULFRBD-centers-solve-unstaged.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


# ====================
# Centers Solve Staged
# ====================
class Build555UDCenterSolve(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-UD-centers-solve",
            ("Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "Uw", "Uw'", "Dw", "Dw'"),
            "5x5x5",
            "lookup-table-5x5x5-step34-UD-centers-solve.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . U U U .
            . U U U .
            . U U U .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . D D D .
            . D D D .
            . D D D .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555LRCenterSolve(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-LR-centers-solve",
            ("Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "Uw", "Uw'", "Dw", "Dw'"),
            "5x5x5",
            "lookup-table-5x5x5-step35-LR-centers-solve.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . . . . .  . R R R .  . . . . .
 . L L L .  . . . . .  . R R R .  . . . . .
 . L L L .  . . . . .  . R R R .  . . . . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


class Build555FBCenterSolve(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-FB-centers-solve",
            ("Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "Uw", "Uw'", "Dw", "Dw'"),
            "5x5x5",
            "lookup-table-5x5x5-step36-FB-centers-solve.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . F F F .  . . . . .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


# only used when a larger cube has been reduced to a 5x5x5
class Build555ULFRBDTCenterSolve(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-t-centers-solve",
            ("Fw", "Fw'", "Bw", "Bw'", "Lw", "Lw'", "Rw", "Rw'", "Uw", "Uw'", "Dw", "Dw'"),
            "5x5x5",
            "lookup-table-5x5x5-step33-ULFRBD-t-centers-solve.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            . . U . .
            . U . U .
            . . U . .
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . . L . .  . . F . .  . . R . .  . . B . .
 . L . L .  . F . F .  . R . R .  . B . B .
 . . L . .  . . F . .  . . R . .  . . B . .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            . . D . .
            . D . D .
            . . D . .
            . . . . .""",
                    "ascii",
                ),
            ),
        )


# ==========================
# L4E last-four-edges tables
# ==========================
class Build555EdgesStageFirstFour(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-edges-stage-first-four",
            (),
            "5x5x5",
            "lookup-table-5x5x5-step100-stage-first-four-edges.txt",
            True,  # store_as_hex
            (
                (
                    """
            . - - - .
            - U U U -
            - U U U -
            - U U U -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 L L L L L  L F F F L  L R R R L  L B B B L
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - D D D -
            - D D D -
            - D D D -
            . - - - .""",
                    "ascii",
                ),
                (
                    """
            . L L L .
            - U U U -
            - U U U -
            - U U U -
            . L L L .

 . - - - .  . L L L .  . - - - .  . L L L .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . - - - .  . L L L .  . - - - .  . L L L .

            . L L L .
            - D D D -
            - D D D -
            - D D D -
            . L L L .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            L U U U L
            L U U U L
            L U U U L
            . - - - .

 . L L L .  . - - - .  . L L L .  . - - - .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . L L L .  . - - - .  . L L L .  . - - - .

            . - - - .
            L D D D L
            L D D D L
            L D D D L
            . - - - .""",
                    "ascii",
                ),
            ),
        )


class Build555EdgesStageSecondFour(BFS):
    """
    The first L4E group will be in the x-plane, they can move around
    just do not un-L4E them.
    """

    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-edges-stage-second-four",
            ("Rw", "Rw'", "Lw", "Lw'", "Fw", "Fw'", "Bw", "Bw'", "L", "L'", "F", "F'", "R", "R'", "B", "B'"),
            "5x5x5",
            "lookup-table-5x5x5-step101-stage-second-four-edges.txt",
            False,  # store_as_hex
            (
                (
                    """
            . L L L .
            - U U U -
            - U U U -
            - U U U -
            . L L L .

 . - - - .  . L L L .  . - - - .  . L L L .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . - - - .  . L L L .  . - - - .  . L L L .

            . L L L .
            - D D D -
            - D D D -
            - D D D -
            . L L L .""",
                    "ascii",
                ),
                (
                    """
            . - - - .
            L U U U L
            L U U U L
            L U U U L
            . - - - .

 . L L L .  . - - - .  . L L L .  . - - - .
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 - L L L -  - F F F -  - R R R -  - B B B -
 . L L L .  . - - - .  . L L L .  . - - - .

            . - - - .
            L D D D L
            L D D D L
            L D D D L
            . - - - .""",
                    "ascii",
                ),
            ),
        )


class Build555EdgesXPlaneEdgesOnly(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-edges-x-plane-edges-only",
            (),  # illegal moves
            "5x5x5",
            "lookup-table-5x5x5-step301-edges-x-plane-edges-only.txt",
            False,  # store_as_hex
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 L . . . L  F . . . F  R . . . R  B . . . B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
            legal_moves=("L2", "F2", "R2", "B2", "Uw", "Uw'", "Uw2", "Dw", "Dw'", "Dw2"),
        )


class Build555EdgesXPlaneCentersOnly(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-edges-x-plane-centers-only",
            (),  # illegal moves
            "5x5x5",
            "lookup-table-5x5x5-step302-edges-x-plane-centers-only.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
            . . . . .
            - . . . -
            - . . . -
            - . . . -
            . . . . .

 . . . . .  . . . . .  . . . . .  . . . . .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . L L L .  . F F F .  . R R R .  . B B B .
 . . . . .  . . . . .  . . . . .  . . . . .

            . . . . .
            - . . . -
            - . . . -
            - . . . -
            . . . . .""",
                    "ascii",
                ),
            ),
            legal_moves=("L2", "F2", "R2", "B2", "Uw", "Uw'", "Uw2", "Dw", "Dw'", "Dw2"),
        )


class Build555EdgesXPlane(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "5x5x5-edges-x-plane",
            (),  # illegal moves
            "5x5x5",
            "lookup-table-5x5x5-step300-edges-x-plane.txt",
            False,  # store_as_hex
            (
                (
                    """
            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .

 . - - - .  . - - - .  . - - - .  . - - - .
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 L L L L L  F F F F F  R R R R R  B B B B B
 . - - - .  . - - - .  . - - - .  . - - - .

            . - - - .
            - . . . -
            - . . . -
            - . . . -
            . - - - .""",
                    "ascii",
                ),
            ),
            use_edges_pattern=True,
            legal_moves=("L2", "F2", "R2", "B2", "Uw", "Uw'", "Uw2", "Dw", "Dw'", "Dw2"),
        )

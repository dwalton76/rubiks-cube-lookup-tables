# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS

log = logging.getLogger(__name__)

"""
phase 1
    use 555 solver to stage the LR inner centers

phase 2
    pair LR oblique edges
    uses heuristic formula so no table to build

phase 3
    use 5x5x5 solver to stage the LR inner centers

phase 4
    use 5x5x5 solver to stage the UD inner centers

phase 5
    pair the oblique UD edges
    uses heuristic formula so no table to build

phase 6
    use 5x5x5 to stage the UD centers

phase 7
    LR centers to vertical bars

phase 8
    UD centers to vertical bars

phase 9
    centers daisy solve
"""

# ===============================
# phase 2 - pair LR oblique edges
# ===============================


class StartingStates777Phase2(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase2",
            (
                # do not break an oblique edge
                "3Uw", "3Uw'", "3Uw2",
                "3Dw", "3Dw'", "3Dw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Rw", "3Rw'", "3Rw2",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase2.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . x x x . .
                . x . . . x .
                . x . . . x .
                . x . . . x .
                . . x x x . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . x x x . .  . . L L L . .  . . x x x . .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . L . . . L .  . x . . . x .  . L . . . L .  . x . . . x .
 . . L L L . .  . . x x x . .  . . L L L . .  . . x x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . x x x . .
                . x . . . x .
                . x . . . x .
                . x . . . x .
                . . x x x . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase2(BFS):
    """
    There are 24!/(8!*8!) or 735741 starting states.
    From those are (24!/(8!*8!))^3 or 398,267,506,305,474,021 states.
    The result is the table explodes quickly! We only build this to give us a rough idea
    of how many moves this phase should take so that we know if our current unpaired_count
    IDA heuristic works well or not.

    lookup-table-7x7x7-phase2.txt
    =============================
    1 steps has 7,606,735 entries (4 percent, 0.00x previous step)
    2 steps has 151,277,968 entries (95 percent, 19.89x previous step)

    # extrapolate from here

    3 steps has 2,886,383,629 entries (19.08x previous step)
    4 steps has 52,763,092,738 entries (18.28x previous step)
    5 steps has 922,298,861,060 entries (17.48x previous step)
    6 steps has 15,383,945,002,480 entries (16.68x previous step)
    7 steps has 244,297,046,639,382 entries (15.88x previous step)
    8 steps has 3,683,999,463,321,879 entries (15.08x previous step)
    9 steps has 52,607,512,336,236,408 entries (14.28x previous step)
    10 steps has 341,715,335,407,051,742 entries (6.50x previous step)

    Average: 9.847401841508537
    Total  : 398,267,506,305,474,021
    """

    def __init__(self):
        # fmt: off
        # Note that phase2_ss is no longer in the builder777ss file...it added 735741 lines to that file
        # and I was never doing to use it again so I deleted it. You can rebuild it via
        # ./utils/builderui.py StartingStates777Phase2

        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase2_ss
        BFS.__init__(
            self,
            "7x7x7-phase2",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase2.txt",
            False,  # store_as_hex
            phase2_ss,
            use_c=True,
        )
        # fmt: on


# =======================================================
# phase 4 - stage UD inner centers, pair UD oblique edges
# =======================================================
class Build777Phase4TCenters(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step-phase4-t-centers",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-t-centers.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . U . . .
                . . U . U . .
                . . . U . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . U . . .
                . . U . U . .
                . . . U . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase4XCenters(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step-phase4-x-centers",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-x-centers.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . U . U . .
                . . . . . . .
                . . U . U . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . U . U . .
                . . . . . . .
                . . U . U . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


# perfect hash
class Build777Phase4Centers(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase4-inner-centers",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-inner-centers.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . U U U . .
                . . U . U . .
                . . U U U . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . U U U . .
                . . U . U . .
                . . U U U . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


# dwalton
class Build777Phase4LeftOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase4-left-oblique",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-left-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . . . .  . . . . . . .  . . x . . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . . x . .  . . . . . . .  . . . . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase4RightOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase4-right-oblique",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-right-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . x . .  . . . . . . .  . . . . x . .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . . x . . . .  . . . . . . .  . . x . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase4MiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase4-middle-oblique",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-middle-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class StartingStates777Phase4(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase4",
            (
                # do not break an oblique edge
                "3Uw", "3Uw'", "3Uw2",
                "3Dw", "3Dw'", "3Dw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Rw", "3Rw'", "3Rw2",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase4.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase4(BFS):
    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase4_ss
        BFS.__init__(
            self,
            "7x7x7-phase4",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4.txt",
            False,  # store_as_hex
            phase4_ss,
            use_c=True,
        )
        # fmt: on


class StartingStates777Phase4LeftRightOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase4-left-right-oblique",
            (
                # do not break an oblique edge
                "3Uw", "3Uw'", "3Uw2",
                "3Dw", "3Dw'", "3Dw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Rw", "3Rw'", "3Rw2",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase4-left-right-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U . U . .
                . U . . . U .
                . . . . . . .
                . U . . . U .
                . . U . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . U . .
                . U . . . U .
                . . . . . . .
                . U . . . U .
                . . U . U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase4LeftRightOblique(BFS):
    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase4_left_right_oblique_ss
        BFS.__init__(
            self,
            "7x7x7-phase4-left-right-oblique",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-left-right-oblique.txt",
            False,  # store_as_hex
            phase4_left_right_oblique_ss,
            use_c=True,
        )
        # fmt: on


class StartingStates777Phase4LeftMiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase4-left-middle-oblique",
            (
                # do not break an oblique edge
                "3Uw", "3Uw'", "3Uw2",
                "3Dw", "3Dw'", "3Dw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Rw", "3Rw'", "3Rw2",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase4-left-middle-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U U . . .
                . . . . . U .
                . U . . . U .
                . U . . . . .
                . . . U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x x . . .  . . . . . . .  . . x x . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . x x . .  . . . . . . .  . . . x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U . . .
                . . . . . U .
                . U . . . U .
                . U . . . . .
                . . . U U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase4LeftMiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase4_left_middle_oblique_ss
        BFS.__init__(
            self,
            "7x7x7-phase4-left-middle-oblique",
            (
                # keep LR inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase4-left-middle-oblique.txt",
            False,  # store_as_hex
            phase4_left_middle_oblique_ss,
            use_c=True,
        )
        # fmt: on


# ===============================
# phase 5 - pair UD oblique edges
# ===============================
class Build777Phase5LeftOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-left-oblique",
            (
                # keep inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Lw", "3Lw'",
                "3Rw", "3Rw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase5-left-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . . . .  . . . . . . .  . . x . . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . . x . .  . . . . . . .  . . . . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . . . .
                . . . . . U .
                . . . . . . .
                . U . . . . .
                . . . . U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase5RightOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-right-oblique",
            (
                # keep inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Lw", "3Lw'",
                "3Rw", "3Rw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase5-right-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . x . .  . . . . . . .  . . . . x . .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . . x . . . .  . . . . . . .  . . x . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . U . .
                . U . . . . .
                . . . . . . .
                . . . . . U .
                . . U . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase5MiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-middle-oblique",
            (
                # keep inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Lw", "3Lw'",
                "3Rw", "3Rw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase5-middle-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . x . . .  . . . . . . .  . . . x . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . U . . .
                . . . . . . .
                . U . . . U .
                . . . . . . .
                . . . U . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class StartingStates777Phase5(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5",
            (
                # do not break an oblique edge
                "3Uw", "3Uw'", "3Uw2",
                "3Dw", "3Dw'", "3Dw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Rw", "3Rw'", "3Rw2",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase5.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . x x x . .  . . . . . . .  . . x x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase5(BFS):
    """
    lookup-table-7x7x7-phase5.txt
    =============================
    1 steps has 77,446 entries (0 percent, 0.00x previous step)
    2 steps has 831,520 entries (8 percent, 10.74x previous step)
    3 steps has 9,010,776 entries (90 percent, 10.84x previous step)

    # extrapolate from here

    4 steps has 90,468,191 entries (10.04x previous step)
    5 steps has 835,926,084 entries (9.24x previous step)
    6 steps has 7,055,216,148 entries (8.44x previous step)
    7 steps has 53,901,851,370 entries (7.64x previous step)
    8 steps has 368,688,663,370 entries (6.84x previous step)
    9 steps has 1,701,164,858,095 entries (4.61x previous step)

    Average: 8.76472660201022
    Total  : 2,131,746,903,000
    """

    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase5_ss
        BFS.__init__(
            self,
            "7x7x7-phase5",
            (
                # keep inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Lw", "3Lw'",
                "3Rw", "3Rw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase5.txt",
            False,  # store_as_hex
            phase5_ss,
            use_c=True,
        )
        # fmt: on


class StartingStates777Phase5LeftRightOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-left-right-oblique",
            (
                # do not break an oblique edge
                "3Uw", "3Uw'", "3Uw2",
                "3Dw", "3Dw'", "3Dw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Rw", "3Rw'", "3Rw2",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase5-left-right-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U . U . .
                . U . . . U .
                . . . . . . .
                . U . . . U .
                . . U . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . . x . x . .  . . . . . . .  . . x . x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U . U . .
                . U . . . U .
                . . . . . . .
                . U . . . U .
                . . U . U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase5LeftRightOblique(BFS):
    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase5_left_right_oblique_ss
        BFS.__init__(
            self,
            "7x7x7-phase5",
            (
                # keep inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Lw", "3Lw'",
                "3Rw", "3Rw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase5-left-right-oblique.txt",
            False,  # store_as_hex
            phase5_left_right_oblique_ss,
            use_c=True,
        )
        # fmt: on


class StartingStates777Phase5LeftMiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-phase5-left-middle-oblique",
            (
                # do not break an oblique edge
                "3Uw", "3Uw'", "3Uw2",
                "3Dw", "3Dw'", "3Dw2",
                "3Fw", "3Fw'", "3Fw2",
                "3Bw", "3Bw'", "3Bw2",
                "3Lw", "3Lw'", "3Lw2",
                "3Rw", "3Rw'", "3Rw2",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-phase5-left-middle-oblique.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U U . . .
                . . . . . U .
                . U . . . U .
                . U . . . . .
                . . . U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . x x . . .  . . . . . . .  . . x x . . .
 . . . . . . .  . . . . . x .  . . . . . . .  . . . . . x .
 . . . . . . .  . x . . . x .  . . . . . . .  . x . . . x .
 . . . . . . .  . x . . . . .  . . . . . . .  . x . . . . .
 . . . . . . .  . . . x x . .  . . . . . . .  . . . x x . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U . . .
                . . . . . U .
                . U . . . U .
                . U . . . . .
                . . . U U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Phase5LeftMiddleOblique(BFS):
    def __init__(self):
        # fmt: off
        # rubiks cube libraries
        from rubikscubelookuptables.builder777ss import phase5_left_middle_oblique_ss
        BFS.__init__(
            self,
            "7x7x7-phase5",
            (
                # keep inside centers staged
                "3Uw", "3Uw'",
                "3Dw", "3Dw'",
                "3Fw", "3Fw'",
                "3Bw", "3Bw'",
                "3Lw", "3Lw'",
                "3Rw", "3Rw'",

                # keep LR centers staged
                "Uw", "Uw'",
                "Dw", "Dw'",
                "Fw", "Fw'",
                "Bw", "Bw'",

                # we are not manipulating anyting on L or R
                "L", "L'", "L2",
                "R", "R'", "R2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-phase5-left-middle-oblique.txt",
            False,  # store_as_hex
            phase5_left_middle_oblique_ss,
            use_c=True,
        )
        # fmt: on


# =====================================
# phase 7 - LR centers to vertical bars
# =====================================
class StartingStates777Step41(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step41",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'", "3Lw2",
                "Lw", "Lw'", "Lw2",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'", "3Rw2",
                "Rw", "Rw'", "Rw2",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "L", "L'",
                "R", "R'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step41.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L . . . L .  . . . . . . .  . R . . . R .  . . . . . . .
 . L . . . L .  . . . . . . .  . R . . . R .  . . . . . . .
 . L . . . L .  . . . . . . .  . R . . . R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . R R R . .  . . . . . . .  . . L L L . .  . . . . . . .
 . R . . . R .  . . . . . . .  . L . . . L .  . . . . . . .
 . R . . . R .  . . . . . . .  . L . . . L .  . . . . . . .
 . R . . . R .  . . . . . . .  . L . . . L .  . . . . . . .
 . . R R R . .  . . . . . . .  . . L L L . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step41(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step41",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",
                "U", "U'", "U2",
                "D", "D'", "D2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step41.txt",
            False,  # store_as_hex
            (
                (
                    "..........................................................LLL...L...L..L...L..L...L...LLL...................................................................RRR...R...R..R...R..R...R...RRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLL...L...R..L...R..L...R...LLL...................................................................RRR...L...R..L...R..L...R...RRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLL...L...R..L...R..L...R...LLL...................................................................RRR...R...L..R...L..R...L...RRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLL...R...L..R...L..R...L...LLL...................................................................RRR...L...R..L...R..L...R...RRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLL...R...L..R...L..R...L...LLL...................................................................RRR...R...L..R...L..R...L...RRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLL...R...R..R...R..R...R...LLL...................................................................RRR...L...L..L...L..L...L...RRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...L...L..L...L..L...L...LLR...................................................................LRR...R...R..R...R..R...R...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...L...L..L...L..L...L...LLR...................................................................RRL...R...R..R...R..R...R...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...L...R..L...R..L...R...LLR...................................................................LRR...L...R..L...R..L...R...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...L...R..L...R..L...R...LLR...................................................................LRR...R...L..R...L..R...L...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...L...R..L...R..L...R...LLR...................................................................RRL...L...R..L...R..L...R...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...L...R..L...R..L...R...LLR...................................................................RRL...R...L..R...L..R...L...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...R...L..R...L..R...L...LLR...................................................................LRR...L...R..L...R..L...R...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...R...L..R...L..R...L...LLR...................................................................LRR...R...L..R...L..R...L...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...R...L..R...L..R...L...LLR...................................................................RRL...L...R..L...R..L...R...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...R...L..R...L..R...L...LLR...................................................................RRL...R...L..R...L..R...L...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...R...R..R...R..R...R...LLR...................................................................LRR...L...L..L...L..L...L...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LLR...R...R..R...R..R...R...LLR...................................................................RRL...L...L..L...L..L...L...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRL...L...L..L...L..L...L...LRL...................................................................RLR...R...R..R...R..R...R...RLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRL...L...R..L...R..L...R...LRL...................................................................RLR...L...R..L...R..L...R...RLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRL...L...R..L...R..L...R...LRL...................................................................RLR...R...L..R...L..R...L...RLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRL...R...L..R...L..R...L...LRL...................................................................RLR...L...R..L...R..L...R...RLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRL...R...L..R...L..R...L...LRL...................................................................RLR...R...L..R...L..R...L...RLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRL...R...R..R...R..R...R...LRL...................................................................RLR...L...L..L...L..L...L...RLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...L...L..L...L..L...L...LRR...................................................................LLR...R...R..R...R..R...R...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...L...L..L...L..L...L...LRR...................................................................RLL...R...R..R...R..R...R...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...L...R..L...R..L...R...LRR...................................................................LLR...L...R..L...R..L...R...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...L...R..L...R..L...R...LRR...................................................................LLR...R...L..R...L..R...L...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...L...R..L...R..L...R...LRR...................................................................RLL...L...R..L...R..L...R...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...L...R..L...R..L...R...LRR...................................................................RLL...R...L..R...L..R...L...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...R...L..R...L..R...L...LRR...................................................................LLR...L...R..L...R..L...R...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...R...L..R...L..R...L...LRR...................................................................LLR...R...L..R...L..R...L...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...R...L..R...L..R...L...LRR...................................................................RLL...L...R..L...R..L...R...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...R...L..R...L..R...L...LRR...................................................................RLL...R...L..R...L..R...L...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...R...R..R...R..R...R...LRR...................................................................LLR...L...L..L...L..L...L...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................LRR...R...R..R...R..R...R...LRR...................................................................RLL...L...L..L...L..L...L...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...L...L..L...L..L...L...RLL...................................................................LRR...R...R..R...R..R...R...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...L...L..L...L..L...L...RLL...................................................................RRL...R...R..R...R..R...R...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...L...R..L...R..L...R...RLL...................................................................LRR...L...R..L...R..L...R...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...L...R..L...R..L...R...RLL...................................................................LRR...R...L..R...L..R...L...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...L...R..L...R..L...R...RLL...................................................................RRL...L...R..L...R..L...R...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...L...R..L...R..L...R...RLL...................................................................RRL...R...L..R...L..R...L...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...R...L..R...L..R...L...RLL...................................................................LRR...L...R..L...R..L...R...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...R...L..R...L..R...L...RLL...................................................................LRR...R...L..R...L..R...L...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...R...L..R...L..R...L...RLL...................................................................RRL...L...R..L...R..L...R...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...R...L..R...L..R...L...RLL...................................................................RRL...R...L..R...L..R...L...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...R...R..R...R..R...R...RLL...................................................................LRR...L...L..L...L..L...L...LRR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLL...R...R..R...R..R...R...RLL...................................................................RRL...L...L..L...L..L...L...RRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLR...L...L..L...L..L...L...RLR...................................................................LRL...R...R..R...R..R...R...LRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLR...L...R..L...R..L...R...RLR...................................................................LRL...L...R..L...R..L...R...LRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLR...L...R..L...R..L...R...RLR...................................................................LRL...R...L..R...L..R...L...LRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLR...R...L..R...L..R...L...RLR...................................................................LRL...L...R..L...R..L...R...LRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLR...R...L..R...L..R...L...RLR...................................................................LRL...R...L..R...L..R...L...LRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RLR...R...R..R...R..R...R...RLR...................................................................LRL...L...L..L...L..L...L...LRL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...L...L..L...L..L...L...RRL...................................................................LLR...R...R..R...R..R...R...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...L...L..L...L..L...L...RRL...................................................................RLL...R...R..R...R..R...R...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...L...R..L...R..L...R...RRL...................................................................LLR...L...R..L...R..L...R...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...L...R..L...R..L...R...RRL...................................................................LLR...R...L..R...L..R...L...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...L...R..L...R..L...R...RRL...................................................................RLL...L...R..L...R..L...R...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...L...R..L...R..L...R...RRL...................................................................RLL...R...L..R...L..R...L...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...R...L..R...L..R...L...RRL...................................................................LLR...L...R..L...R..L...R...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...R...L..R...L..R...L...RRL...................................................................LLR...R...L..R...L..R...L...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...R...L..R...L..R...L...RRL...................................................................RLL...L...R..L...R..L...R...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...R...L..R...L..R...L...RRL...................................................................RLL...R...L..R...L..R...L...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...R...R..R...R..R...R...RRL...................................................................LLR...L...L..L...L..L...L...LLR...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRL...R...R..R...R..R...R...RRL...................................................................RLL...L...L..L...L..L...L...RLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRR...L...L..L...L..L...L...RRR...................................................................LLL...R...R..R...R..R...R...LLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRR...L...R..L...R..L...R...RRR...................................................................LLL...L...R..L...R..L...R...LLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRR...L...R..L...R..L...R...RRR...................................................................LLL...R...L..R...L..R...L...LLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRR...R...L..R...L..R...L...RRR...................................................................LLL...L...R..L...R..L...R...LLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRR...R...L..R...L..R...L...RRR...................................................................LLL...R...L..R...L..R...L...LLL...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................RRR...R...R..R...R..R...R...RRR...................................................................LLL...L...L..L...L..L...L...LLL...........................................................................................................",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


class StartingStates777Step42(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step42",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'", "3Lw2",
                "Lw", "Lw'", "Lw2",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'", "3Rw2",
                "Rw", "Rw'", "Rw2",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "L", "L'",
                "R", "R'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step42.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L . . . .  . . . . . . .  . . R . . . .  . . . . . . .
 . . L L L L .  . . . . . . .  . . R R R R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L L L L . .  . . . . . . .  . R R R R . .  . . . . . . .
 . . . . L . .  . . . . . . .  . . . . R . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step42(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step42",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",
                "U", "U'", "U2",
                "D", "D'", "D2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step42.txt",
            False,  # store_as_hex
            (
                (
                    "..........................................................L......LLLL...LLL...LLLL......L...................................................................R......RRRR...RRR...RRRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLLL...LLL...RLLL......L...................................................................R......RRRL...RRR...RRRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLLL...LLL...RLLL......L...................................................................R......RRRR...RRR...LRRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLLR...LLL...LLLL......L...................................................................R......RRRL...RRR...RRRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLLR...LLL...LLLL......L...................................................................R......RRRR...RRR...LRRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLLR...LLL...RLLL......L...................................................................R......RRRL...RRR...LRRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRL...LLR...LLLR......R...................................................................L......LRRR...LRR...RLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRL...LLR...LLLR......R...................................................................R......RRLR...RRL...RRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRL...LLR...RLLR......R...................................................................L......LRRL...LRR...RLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRL...LLR...RLLR......R...................................................................L......LRRR...LRR...LLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRL...LLR...RLLR......R...................................................................R......RRLL...RRL...RRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRL...LLR...RLLR......R...................................................................R......RRLR...RRL...LRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRR...LLR...LLLR......R...................................................................L......LRRL...LRR...RLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRR...LLR...LLLR......R...................................................................L......LRRR...LRR...LLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRR...LLR...LLLR......R...................................................................R......RRLL...RRL...RRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRR...LLR...LLLR......R...................................................................R......RRLR...RRL...LRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRR...LLR...RLLR......R...................................................................L......LRRL...LRR...LLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................L......LLRR...LLR...RLLR......R...................................................................R......RRLL...RRL...LRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLL...RLL...LRLL......L...................................................................L......LRRR...LRR...RLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLL...RLL...LRLL......L...................................................................R......RRLR...RRL...RRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLL...RLL...RRLL......L...................................................................L......LRRL...LRR...RLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLL...RLL...RRLL......L...................................................................L......LRRR...LRR...LLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLL...RLL...RRLL......L...................................................................R......RRLL...RRL...RRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLL...RLL...RRLL......L...................................................................R......RRLR...RRL...LRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLR...RLL...LRLL......L...................................................................L......LRRL...LRR...RLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLR...RLL...LRLL......L...................................................................L......LRRR...LRR...LLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLR...RLL...LRLL......L...................................................................R......RRLL...RRL...RRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLR...RLL...LRLL......L...................................................................R......RRLR...RRL...LRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLR...RLL...RRLL......L...................................................................L......LRRL...LRR...LLRR......R...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLLR...RLL...RRLL......L...................................................................R......RRLL...RRL...LRRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLRL...RLR...LRLR......R...................................................................L......LRLR...LRL...RLRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLRL...RLR...RRLR......R...................................................................L......LRLL...LRL...RLRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLRL...RLR...RRLR......R...................................................................L......LRLR...LRL...LLRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLRR...RLR...LRLR......R...................................................................L......LRLL...LRL...RLRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLRR...RLR...LRLR......R...................................................................L......LRLR...LRL...LLRL......L...........................................................................................................",
                    "ULFRBD",
                ),
                (
                    "..........................................................R......RLRR...RLR...RRLR......R...................................................................L......LRLL...LRL...LLRL......L...........................................................................................................",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


class StartingStates777Step43(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step43",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'", "3Lw2",
                "Lw", "Lw'", "Lw2",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'", "3Rw2",
                "Rw", "Rw'", "Rw2",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "L", "L'",
                "R", "R'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step43.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . L . . .  . . . . . . .  . . . R . . .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . . . L . . .  . . . . . . .  . . . R . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step43(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step43",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",
                "U", "U'", "U2",
                "D", "D'", "D2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step43.txt",
            False,  # store_as_hex
            (
                (
                    "...........................................................L.....LLL...LLLLL...LLL.....L.....................................................................R.....RRR...RRRRR...RRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLL...LLLLR...LLL.....L.....................................................................R.....RRR...LRRRR...RRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLL...LLLLR...LLL.....L.....................................................................R.....RRR...RRRRL...RRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLL...RLLLL...LLL.....L.....................................................................R.....RRR...LRRRR...RRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLL...RLLLL...LLL.....L.....................................................................R.....RRR...RRRRL...RRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLL...RLLLR...LLL.....L.....................................................................R.....RRR...LRRRL...RRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...LLLRL...LLR.....L.....................................................................R.....LRR...RLRRR...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...LLLRL...LLR.....L.....................................................................R.....RRL...RRRLR...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...LLLRR...LLR.....L.....................................................................R.....LRR...LLRRR...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...LLLRR...LLR.....L.....................................................................R.....LRR...RLRRL...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...LLLRR...LLR.....L.....................................................................R.....RRL...LRRLR...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...LLLRR...LLR.....L.....................................................................R.....RRL...RRRLL...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...RLLRL...LLR.....L.....................................................................R.....LRR...LLRRR...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...RLLRL...LLR.....L.....................................................................R.....LRR...RLRRL...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...RLLRL...LLR.....L.....................................................................R.....RRL...LRRLR...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...RLLRL...LLR.....L.....................................................................R.....RRL...RRRLL...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...RLLRR...LLR.....L.....................................................................R.....LRR...LLRRL...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....LLR...RLLRR...LLR.....L.....................................................................R.....RRL...LRRLL...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...LRLLL...RLL.....L.....................................................................R.....LRR...RLRRR...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...LRLLL...RLL.....L.....................................................................R.....RRL...RRRLR...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...LRLLR...RLL.....L.....................................................................R.....LRR...LLRRR...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...LRLLR...RLL.....L.....................................................................R.....LRR...RLRRL...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...LRLLR...RLL.....L.....................................................................R.....RRL...LRRLR...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...LRLLR...RLL.....L.....................................................................R.....RRL...RRRLL...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...RRLLL...RLL.....L.....................................................................R.....LRR...LLRRR...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...RRLLL...RLL.....L.....................................................................R.....LRR...RLRRL...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...RRLLL...RLL.....L.....................................................................R.....RRL...LRRLR...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...RRLLL...RLL.....L.....................................................................R.....RRL...RRRLL...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...RRLLR...RLL.....L.....................................................................R.....LRR...LLRRL...LRR.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLL...RRLLR...RLL.....L.....................................................................R.....RRL...LRRLL...RRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLR...LRLRL...RLR.....L.....................................................................R.....LRL...RLRLR...LRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLR...LRLRR...RLR.....L.....................................................................R.....LRL...LLRLR...LRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLR...LRLRR...RLR.....L.....................................................................R.....LRL...RLRLL...LRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLR...RRLRL...RLR.....L.....................................................................R.....LRL...LLRLR...LRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLR...RRLRL...RLR.....L.....................................................................R.....LRL...RLRLL...LRL.....R............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "...........................................................L.....RLR...RRLRR...RLR.....L.....................................................................R.....LRL...LLRLL...LRL.....R............................................................................................................",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


class StartingStates777Step44(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step44",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'", "3Lw2",
                "Lw", "Lw'", "Lw2",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'", "3Rw2",
                "Rw", "Rw'", "Rw2",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "L", "L'",
                "R", "R'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step44.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . L . .  . . . . . . .  . . . . R . .  . . . . . . .
 . L L L L . .  . . . . . . .  . R R R R . .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . . L L L L .  . . . . . . .  . . R R R R .  . . . . . . .
 . . L . . . .  . . . . . . .  . . R . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step44(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step44",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",
                "U", "U'", "U2",
                "D", "D'", "D2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step44.txt",
            False,  # store_as_hex
            (
                (
                    "............................................................L...LLLL....LLL....LLLL...L.......................................................................R...RRRR....RRR....RRRR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LLLL....LLL....LLLR...L.......................................................................R...LRRR....RRR....RRRR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LLLL....LLL....LLLR...L.......................................................................R...RRRR....RRR....RRRL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LRLL....RLL....RLLL...R.......................................................................L...RRRL....RRL....RRLR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LRLL....RLL....RLLL...R.......................................................................R...RLRR....LRR....LRRR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LRLL....RLL....RLLR...R.......................................................................L...LRRL....RRL....RRLR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LRLL....RLL....RLLR...R.......................................................................L...RRRL....RRL....RRLL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LRLL....RLL....RLLR...R.......................................................................R...LLRR....LRR....LRRR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...LRLL....RLL....RLLR...R.......................................................................R...RLRR....LRR....LRRL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RLLL....LLL....LLLL...L.......................................................................R...LRRR....RRR....RRRR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RLLL....LLL....LLLL...L.......................................................................R...RRRR....RRR....RRRL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RLLL....LLL....LLLR...L.......................................................................R...LRRR....RRR....RRRL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RRLL....RLL....RLLL...R.......................................................................L...LRRL....RRL....RRLR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RRLL....RLL....RLLL...R.......................................................................L...RRRL....RRL....RRLL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RRLL....RLL....RLLL...R.......................................................................R...LLRR....LRR....LRRR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RRLL....RLL....RLLL...R.......................................................................R...RLRR....LRR....LRRL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RRLL....RLL....RLLR...R.......................................................................L...LRRL....RRL....RRLL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................L...RRLL....RLL....RLLR...R.......................................................................R...LLRR....LRR....LRRL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LLLR....LLR....LLRL...L.......................................................................L...RRRL....RRL....RRLR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LLLR....LLR....LLRL...L.......................................................................R...RLRR....LRR....LRRR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LLLR....LLR....LLRR...L.......................................................................L...LRRL....RRL....RRLR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LLLR....LLR....LLRR...L.......................................................................L...RRRL....RRL....RRLL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LLLR....LLR....LLRR...L.......................................................................R...LLRR....LRR....LRRR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LLLR....LLR....LLRR...L.......................................................................R...RLRR....LRR....LRRL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LRLR....RLR....RLRL...R.......................................................................L...RLRL....LRL....LRLR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LRLR....RLR....RLRR...R.......................................................................L...LLRL....LRL....LRLR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...LRLR....RLR....RLRR...R.......................................................................L...RLRL....LRL....LRLL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RLLR....LLR....LLRL...L.......................................................................L...LRRL....RRL....RRLR...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RLLR....LLR....LLRL...L.......................................................................L...RRRL....RRL....RRLL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RLLR....LLR....LLRL...L.......................................................................R...LLRR....LRR....LRRR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RLLR....LLR....LLRL...L.......................................................................R...RLRR....LRR....LRRL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RLLR....LLR....LLRR...L.......................................................................L...LRRL....RRL....RRLL...R.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RLLR....LLR....LLRR...L.......................................................................R...LLRR....LRR....LRRL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RRLR....RLR....RLRL...R.......................................................................L...LLRL....LRL....LRLR...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RRLR....RLR....RLRL...R.......................................................................L...RLRL....LRL....LRLL...L.............................................................................................................",
                    "ULFRBD",
                ),
                (
                    "............................................................R...RRLR....RLR....RLRR...R.......................................................................L...LLRL....LRL....LRLL...L.............................................................................................................",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


# =====================================
# phase 8 - UD centers to vertical bars
# =====================================
class StartingStates777Step51(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step51",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'", "3Fw2",
                "Fw", "Fw'", "Fw2",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'", "3Bw2",
                "Bw", "Bw'", "Bw2",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step51.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . D D D . .
                . D . . . D .
                . D . . . D .
                . D . . . D .
                . . D D D . .
                . . . . . . . """,
                    "ascii",
                ),
                (
                    """
                . . . . . . .
                . . D D D . .
                . D . . . D .
                . D . . . D .
                . D . . . D .
                . . D D D . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U U . .
                . U . . . U .
                . U . . . U .
                . U . . . U .
                . . U U U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step51(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step51",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in vertical stripes
                "L", "L'",
                "R", "R'",
                "3Uw2", "Uw2",
                "3Dw2", "Dw2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step51.txt",
            False,  # store_as_hex
            (
                (
                    ".........DDD...D...D..D...D..D...D...DDD......................................................................................................................................................................................................................UUU...U...U..U...U..U...U...UUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDD...D...U..D...U..D...U...DDD......................................................................................................................................................................................................................UUU...D...U..D...U..D...U...UUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDD...D...U..D...U..D...U...DDD......................................................................................................................................................................................................................UUU...U...D..U...D..U...D...UUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDD...U...D..U...D..U...D...DDD......................................................................................................................................................................................................................UUU...D...U..D...U..D...U...UUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDD...U...D..U...D..U...D...DDD......................................................................................................................................................................................................................UUU...U...D..U...D..U...D...UUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDD...U...U..U...U..U...U...DDD......................................................................................................................................................................................................................UUU...D...D..D...D..D...D...UUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...D...D..D...D..D...D...DDU......................................................................................................................................................................................................................DUU...U...U..U...U..U...U...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...D...D..D...D..D...D...DDU......................................................................................................................................................................................................................UUD...U...U..U...U..U...U...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...D...U..D...U..D...U...DDU......................................................................................................................................................................................................................DUU...D...U..D...U..D...U...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...D...U..D...U..D...U...DDU......................................................................................................................................................................................................................DUU...U...D..U...D..U...D...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...D...U..D...U..D...U...DDU......................................................................................................................................................................................................................UUD...D...U..D...U..D...U...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...D...U..D...U..D...U...DDU......................................................................................................................................................................................................................UUD...U...D..U...D..U...D...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...U...D..U...D..U...D...DDU......................................................................................................................................................................................................................DUU...D...U..D...U..D...U...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...U...D..U...D..U...D...DDU......................................................................................................................................................................................................................DUU...U...D..U...D..U...D...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...U...D..U...D..U...D...DDU......................................................................................................................................................................................................................UUD...D...U..D...U..D...U...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...U...D..U...D..U...D...DDU......................................................................................................................................................................................................................UUD...U...D..U...D..U...D...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...U...U..U...U..U...U...DDU......................................................................................................................................................................................................................DUU...D...D..D...D..D...D...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........DDU...U...U..U...U..U...U...DDU......................................................................................................................................................................................................................UUD...D...D..D...D..D...D...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........DUD...D...D..D...D..D...D...DUD......................................................................................................................................................................................................................UDU...U...U..U...U..U...U...UDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUD...D...U..D...U..D...U...DUD......................................................................................................................................................................................................................UDU...D...U..D...U..D...U...UDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUD...D...U..D...U..D...U...DUD......................................................................................................................................................................................................................UDU...U...D..U...D..U...D...UDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUD...U...D..U...D..U...D...DUD......................................................................................................................................................................................................................UDU...D...U..D...U..D...U...UDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUD...U...D..U...D..U...D...DUD......................................................................................................................................................................................................................UDU...U...D..U...D..U...D...UDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUD...U...U..U...U..U...U...DUD......................................................................................................................................................................................................................UDU...D...D..D...D..D...D...UDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...D...D..D...D..D...D...DUU......................................................................................................................................................................................................................DDU...U...U..U...U..U...U...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...D...D..D...D..D...D...DUU......................................................................................................................................................................................................................UDD...U...U..U...U..U...U...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...D...U..D...U..D...U...DUU......................................................................................................................................................................................................................DDU...D...U..D...U..D...U...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...D...U..D...U..D...U...DUU......................................................................................................................................................................................................................DDU...U...D..U...D..U...D...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...D...U..D...U..D...U...DUU......................................................................................................................................................................................................................UDD...D...U..D...U..D...U...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...D...U..D...U..D...U...DUU......................................................................................................................................................................................................................UDD...U...D..U...D..U...D...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...U...D..U...D..U...D...DUU......................................................................................................................................................................................................................DDU...D...U..D...U..D...U...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...U...D..U...D..U...D...DUU......................................................................................................................................................................................................................DDU...U...D..U...D..U...D...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...U...D..U...D..U...D...DUU......................................................................................................................................................................................................................UDD...D...U..D...U..D...U...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...U...D..U...D..U...D...DUU......................................................................................................................................................................................................................UDD...U...D..U...D..U...D...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...U...U..U...U..U...U...DUU......................................................................................................................................................................................................................DDU...D...D..D...D..D...D...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........DUU...U...U..U...U..U...U...DUU......................................................................................................................................................................................................................UDD...D...D..D...D..D...D...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...D...D..D...D..D...D...UDD......................................................................................................................................................................................................................DUU...U...U..U...U..U...U...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...D...D..D...D..D...D...UDD......................................................................................................................................................................................................................UUD...U...U..U...U..U...U...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...D...U..D...U..D...U...UDD......................................................................................................................................................................................................................DUU...D...U..D...U..D...U...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...D...U..D...U..D...U...UDD......................................................................................................................................................................................................................DUU...U...D..U...D..U...D...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...D...U..D...U..D...U...UDD......................................................................................................................................................................................................................UUD...D...U..D...U..D...U...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...D...U..D...U..D...U...UDD......................................................................................................................................................................................................................UUD...U...D..U...D..U...D...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...U...D..U...D..U...D...UDD......................................................................................................................................................................................................................DUU...D...U..D...U..D...U...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...U...D..U...D..U...D...UDD......................................................................................................................................................................................................................DUU...U...D..U...D..U...D...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...U...D..U...D..U...D...UDD......................................................................................................................................................................................................................UUD...D...U..D...U..D...U...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...U...D..U...D..U...D...UDD......................................................................................................................................................................................................................UUD...U...D..U...D..U...D...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...U...U..U...U..U...U...UDD......................................................................................................................................................................................................................DUU...D...D..D...D..D...D...DUU.........",
                    "ULFRBD",
                ),
                (
                    ".........UDD...U...U..U...U..U...U...UDD......................................................................................................................................................................................................................UUD...D...D..D...D..D...D...UUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDU...D...D..D...D..D...D...UDU......................................................................................................................................................................................................................DUD...U...U..U...U..U...U...DUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDU...D...U..D...U..D...U...UDU......................................................................................................................................................................................................................DUD...D...U..D...U..D...U...DUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDU...D...U..D...U..D...U...UDU......................................................................................................................................................................................................................DUD...U...D..U...D..U...D...DUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDU...U...D..U...D..U...D...UDU......................................................................................................................................................................................................................DUD...D...U..D...U..D...U...DUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDU...U...D..U...D..U...D...UDU......................................................................................................................................................................................................................DUD...U...D..U...D..U...D...DUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UDU...U...U..U...U..U...U...UDU......................................................................................................................................................................................................................DUD...D...D..D...D..D...D...DUD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...D...D..D...D..D...D...UUD......................................................................................................................................................................................................................DDU...U...U..U...U..U...U...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...D...D..D...D..D...D...UUD......................................................................................................................................................................................................................UDD...U...U..U...U..U...U...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...D...U..D...U..D...U...UUD......................................................................................................................................................................................................................DDU...D...U..D...U..D...U...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...D...U..D...U..D...U...UUD......................................................................................................................................................................................................................DDU...U...D..U...D..U...D...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...D...U..D...U..D...U...UUD......................................................................................................................................................................................................................UDD...D...U..D...U..D...U...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...D...U..D...U..D...U...UUD......................................................................................................................................................................................................................UDD...U...D..U...D..U...D...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...U...D..U...D..U...D...UUD......................................................................................................................................................................................................................DDU...D...U..D...U..D...U...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...U...D..U...D..U...D...UUD......................................................................................................................................................................................................................DDU...U...D..U...D..U...D...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...U...D..U...D..U...D...UUD......................................................................................................................................................................................................................UDD...D...U..D...U..D...U...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...U...D..U...D..U...D...UUD......................................................................................................................................................................................................................UDD...U...D..U...D..U...D...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...U...U..U...U..U...U...UUD......................................................................................................................................................................................................................DDU...D...D..D...D..D...D...DDU.........",
                    "ULFRBD",
                ),
                (
                    ".........UUD...U...U..U...U..U...U...UUD......................................................................................................................................................................................................................UDD...D...D..D...D..D...D...UDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUU...D...D..D...D..D...D...UUU......................................................................................................................................................................................................................DDD...U...U..U...U..U...U...DDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUU...D...U..D...U..D...U...UUU......................................................................................................................................................................................................................DDD...D...U..D...U..D...U...DDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUU...D...U..D...U..D...U...UUU......................................................................................................................................................................................................................DDD...U...D..U...D..U...D...DDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUU...U...D..U...D..U...D...UUU......................................................................................................................................................................................................................DDD...D...U..D...U..D...U...DDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUU...U...D..U...D..U...D...UUU......................................................................................................................................................................................................................DDD...U...D..U...D..U...D...DDD.........",
                    "ULFRBD",
                ),
                (
                    ".........UUU...U...U..U...U..U...U...UUU......................................................................................................................................................................................................................DDD...D...D..D...D..D...D...DDD.........",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


class StartingStates777Step52(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step52",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'", "3Fw2",
                "Fw", "Fw'", "Fw2",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'", "3Bw2",
                "Bw", "Bw'", "Bw2",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step52.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U . . . .
                . . U U U U .
                . . U U U . .
                . U U U U . .
                . . . . U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . D . . . .
                . . D D D D .
                . . D D D . .
                . D D D D . .
                . . . . D . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step52(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step52",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in vertical stripes
                "L", "L'",
                "R", "R'",
                "3Uw2", "Uw2",
                "3Dw2", "Dw2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step52.txt",
            False,  # store_as_hex
            (
                (
                    ".........D......DUDD...DUD...DDUD......D......................................................................................................................................................................................................................U......UDUU...UDU...UUDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUDD...DUD...UDUD......D......................................................................................................................................................................................................................U......UDUD...UDU...UUDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUDD...DUD...UDUD......D......................................................................................................................................................................................................................U......UDUU...UDU...DUDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUDU...DUD...DDUD......D......................................................................................................................................................................................................................U......UDUD...UDU...UUDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUDU...DUD...DDUD......D......................................................................................................................................................................................................................U......UDUU...UDU...DUDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUDU...DUD...UDUD......D......................................................................................................................................................................................................................U......UDUD...UDU...DUDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUD...DUU...DDUU......U......................................................................................................................................................................................................................D......DDUU...DDU...UDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUD...DUU...DDUU......U......................................................................................................................................................................................................................U......UDDU...UDD...UUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUD...DUU...UDUU......U......................................................................................................................................................................................................................D......DDUD...DDU...UDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUD...DUU...UDUU......U......................................................................................................................................................................................................................D......DDUU...DDU...DDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUD...DUU...UDUU......U......................................................................................................................................................................................................................U......UDDD...UDD...UUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUD...DUU...UDUU......U......................................................................................................................................................................................................................U......UDDU...UDD...DUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUU...DUU...DDUU......U......................................................................................................................................................................................................................D......DDUD...DDU...UDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUU...DUU...DDUU......U......................................................................................................................................................................................................................D......DDUU...DDU...DDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUU...DUU...DDUU......U......................................................................................................................................................................................................................U......UDDD...UDD...UUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUU...DUU...DDUU......U......................................................................................................................................................................................................................U......UDDU...UDD...DUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUU...DUU...UDUU......U......................................................................................................................................................................................................................D......DDUD...DDU...DDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........D......DUUU...DUU...UDUU......U......................................................................................................................................................................................................................U......UDDD...UDD...DUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDD...UUD...DUUD......D......................................................................................................................................................................................................................D......DDUU...DDU...UDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDD...UUD...DUUD......D......................................................................................................................................................................................................................U......UDDU...UDD...UUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDD...UUD...UUUD......D......................................................................................................................................................................................................................D......DDUD...DDU...UDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDD...UUD...UUUD......D......................................................................................................................................................................................................................D......DDUU...DDU...DDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDD...UUD...UUUD......D......................................................................................................................................................................................................................U......UDDD...UDD...UUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDD...UUD...UUUD......D......................................................................................................................................................................................................................U......UDDU...UDD...DUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDU...UUD...DUUD......D......................................................................................................................................................................................................................D......DDUD...DDU...UDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDU...UUD...DUUD......D......................................................................................................................................................................................................................D......DDUU...DDU...DDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDU...UUD...DUUD......D......................................................................................................................................................................................................................U......UDDD...UDD...UUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDU...UUD...DUUD......D......................................................................................................................................................................................................................U......UDDU...UDD...DUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDU...UUD...UUUD......D......................................................................................................................................................................................................................D......DDUD...DDU...DDDU......U.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUDU...UUD...UUUD......D......................................................................................................................................................................................................................U......UDDD...UDD...DUDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUUD...UUU...DUUU......U......................................................................................................................................................................................................................D......DDDU...DDD...UDDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUUD...UUU...UUUU......U......................................................................................................................................................................................................................D......DDDD...DDD...UDDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUUD...UUU...UUUU......U......................................................................................................................................................................................................................D......DDDU...DDD...DDDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUUU...UUU...DUUU......U......................................................................................................................................................................................................................D......DDDD...DDD...UDDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUUU...UUU...DUUU......U......................................................................................................................................................................................................................D......DDDU...DDD...DDDD......D.........",
                    "ULFRBD",
                ),
                (
                    ".........U......UUUU...UUU...UUUU......U......................................................................................................................................................................................................................D......DDDD...DDD...DDDD......D.........",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


class StartingStates777Step53(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step53",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'", "3Fw2",
                "Fw", "Fw'", "Fw2",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'", "3Bw2",
                "Bw", "Bw'", "Bw2",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step53.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . U . . .
                . . U U U . .
                . U U U U U .
                . . U U U . .
                . . . U . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . D . . .
                . . D D D . .
                . D D D D D .
                . . D D D . .
                . . . D . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step53(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step53",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in vertical stripes
                "L", "L'",
                "R", "R'",
                "3Uw2", "Uw2",
                "3Dw2", "Dw2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step53.txt",
            False,  # store_as_hex
            (
                (
                    "..........U.....DUD...DDUDD...DUD.....U........................................................................................................................................................................................................................D.....UDU...UUDUU...UDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUD...DDUDU...DUD.....U........................................................................................................................................................................................................................D.....UDU...DUDUU...UDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUD...DDUDU...DUD.....U........................................................................................................................................................................................................................D.....UDU...UUDUD...UDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUD...UDUDD...DUD.....U........................................................................................................................................................................................................................D.....UDU...DUDUU...UDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUD...UDUDD...DUD.....U........................................................................................................................................................................................................................D.....UDU...UUDUD...UDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUD...UDUDU...DUD.....U........................................................................................................................................................................................................................D.....UDU...DUDUD...UDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...DDUUD...DUU.....U........................................................................................................................................................................................................................D.....DDU...UDDUU...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...DDUUD...DUU.....U........................................................................................................................................................................................................................D.....UDD...UUDDU...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...DDUUU...DUU.....U........................................................................................................................................................................................................................D.....DDU...DDDUU...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...DDUUU...DUU.....U........................................................................................................................................................................................................................D.....DDU...UDDUD...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...DDUUU...DUU.....U........................................................................................................................................................................................................................D.....UDD...DUDDU...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...DDUUU...DUU.....U........................................................................................................................................................................................................................D.....UDD...UUDDD...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...UDUUD...DUU.....U........................................................................................................................................................................................................................D.....DDU...DDDUU...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...UDUUD...DUU.....U........................................................................................................................................................................................................................D.....DDU...UDDUD...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...UDUUD...DUU.....U........................................................................................................................................................................................................................D.....UDD...DUDDU...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...UDUUD...DUU.....U........................................................................................................................................................................................................................D.....UDD...UUDDD...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...UDUUU...DUU.....U........................................................................................................................................................................................................................D.....DDU...DDDUD...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....DUU...UDUUU...DUU.....U........................................................................................................................................................................................................................D.....UDD...DUDDD...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...DUUDD...UUD.....U........................................................................................................................................................................................................................D.....DDU...UDDUU...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...DUUDD...UUD.....U........................................................................................................................................................................................................................D.....UDD...UUDDU...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...DUUDU...UUD.....U........................................................................................................................................................................................................................D.....DDU...DDDUU...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...DUUDU...UUD.....U........................................................................................................................................................................................................................D.....DDU...UDDUD...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...DUUDU...UUD.....U........................................................................................................................................................................................................................D.....UDD...DUDDU...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...DUUDU...UUD.....U........................................................................................................................................................................................................................D.....UDD...UUDDD...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...UUUDD...UUD.....U........................................................................................................................................................................................................................D.....DDU...DDDUU...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...UUUDD...UUD.....U........................................................................................................................................................................................................................D.....DDU...UDDUD...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...UUUDD...UUD.....U........................................................................................................................................................................................................................D.....UDD...DUDDU...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...UUUDD...UUD.....U........................................................................................................................................................................................................................D.....UDD...UUDDD...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...UUUDU...UUD.....U........................................................................................................................................................................................................................D.....DDU...DDDUD...DDU.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUD...UUUDU...UUD.....U........................................................................................................................................................................................................................D.....UDD...DUDDD...UDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUU...DUUUD...UUU.....U........................................................................................................................................................................................................................D.....DDD...UDDDU...DDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUU...DUUUU...UUU.....U........................................................................................................................................................................................................................D.....DDD...DDDDU...DDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUU...DUUUU...UUU.....U........................................................................................................................................................................................................................D.....DDD...UDDDD...DDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUU...UUUUD...UUU.....U........................................................................................................................................................................................................................D.....DDD...DDDDU...DDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUU...UUUUD...UUU.....U........................................................................................................................................................................................................................D.....DDD...UDDDD...DDD.....D..........",
                    "ULFRBD",
                ),
                (
                    "..........U.....UUU...UUUUU...UUU.....U........................................................................................................................................................................................................................D.....DDD...DDDDD...DDD.....D..........",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


class StartingStates777Step54(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step54",
            (
                "3Uw", "3Uw'", "3Uw2",
                "Uw", "Uw'", "Uw2",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'", "3Fw2",
                "Fw", "Fw'", "Fw2",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'", "3Bw2",
                "Bw", "Bw'", "Bw2",
                "3Dw", "3Dw'", "3Dw2",
                "Dw", "Dw'", "Dw2",
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "starting-states-lookup-table-7x7x7-step54.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . U . .
                . U U U U . .
                . . U U U . .
                . . U U U U .
                . . U . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . D . .
                . D D D D . .
                . . D D D . .
                . . D D D D .
                . . D . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step54(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step54",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in vertical stripes
                "L", "L'",
                "R", "R'",
                "3Uw2", "Uw2",
                "3Dw2", "Dw2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step54.txt",
            False,  # store_as_hex
            (
                (
                    "...........D...DDUD....DUD....DUDD...D..........................................................................................................................................................................................................................U...UUDU....UDU....UDUU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DDUD....DUD....DUDU...D..........................................................................................................................................................................................................................U...DUDU....UDU....UDUU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DDUD....DUD....DUDU...D..........................................................................................................................................................................................................................U...UUDU....UDU....UDUD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DUUD....UUD....UUDD...U..........................................................................................................................................................................................................................D...UUDD....UDD....UDDU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DUUD....UUD....UUDD...U..........................................................................................................................................................................................................................U...UDDU....DDU....DDUU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DUUD....UUD....UUDU...U..........................................................................................................................................................................................................................D...DUDD....UDD....UDDU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DUUD....UUD....UUDU...U..........................................................................................................................................................................................................................D...UUDD....UDD....UDDD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DUUD....UUD....UUDU...U..........................................................................................................................................................................................................................U...DDDU....DDU....DDUU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........D...DUUD....UUD....UUDU...U..........................................................................................................................................................................................................................U...UDDU....DDU....DDUD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UDUD....DUD....DUDD...D..........................................................................................................................................................................................................................U...DUDU....UDU....UDUU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UDUD....DUD....DUDD...D..........................................................................................................................................................................................................................U...UUDU....UDU....UDUD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UDUD....DUD....DUDU...D..........................................................................................................................................................................................................................U...DUDU....UDU....UDUD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UUUD....UUD....UUDD...U..........................................................................................................................................................................................................................D...DUDD....UDD....UDDU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UUUD....UUD....UUDD...U..........................................................................................................................................................................................................................D...UUDD....UDD....UDDD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UUUD....UUD....UUDD...U..........................................................................................................................................................................................................................U...DDDU....DDU....DDUU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UUUD....UUD....UUDD...U..........................................................................................................................................................................................................................U...UDDU....DDU....DDUD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UUUD....UUD....UUDU...U..........................................................................................................................................................................................................................D...DUDD....UDD....UDDD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........D...UUUD....UUD....UUDU...U..........................................................................................................................................................................................................................U...DDDU....DDU....DDUD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DDUU....DUU....DUUD...D..........................................................................................................................................................................................................................D...UUDD....UDD....UDDU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DDUU....DUU....DUUD...D..........................................................................................................................................................................................................................U...UDDU....DDU....DDUU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DDUU....DUU....DUUU...D..........................................................................................................................................................................................................................D...DUDD....UDD....UDDU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DDUU....DUU....DUUU...D..........................................................................................................................................................................................................................D...UUDD....UDD....UDDD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DDUU....DUU....DUUU...D..........................................................................................................................................................................................................................U...DDDU....DDU....DDUU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DDUU....DUU....DUUU...D..........................................................................................................................................................................................................................U...UDDU....DDU....DDUD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DUUU....UUU....UUUD...U..........................................................................................................................................................................................................................D...UDDD....DDD....DDDU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DUUU....UUU....UUUU...U..........................................................................................................................................................................................................................D...DDDD....DDD....DDDU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...DUUU....UUU....UUUU...U..........................................................................................................................................................................................................................D...UDDD....DDD....DDDD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UDUU....DUU....DUUD...D..........................................................................................................................................................................................................................D...DUDD....UDD....UDDU...U...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UDUU....DUU....DUUD...D..........................................................................................................................................................................................................................D...UUDD....UDD....UDDD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UDUU....DUU....DUUD...D..........................................................................................................................................................................................................................U...DDDU....DDU....DDUU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UDUU....DUU....DUUD...D..........................................................................................................................................................................................................................U...UDDU....DDU....DDUD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UDUU....DUU....DUUU...D..........................................................................................................................................................................................................................D...DUDD....UDD....UDDD...U...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UDUU....DUU....DUUU...D..........................................................................................................................................................................................................................U...DDDU....DDU....DDUD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UUUU....UUU....UUUD...U..........................................................................................................................................................................................................................D...DDDD....DDD....DDDU...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UUUU....UUU....UUUD...U..........................................................................................................................................................................................................................D...UDDD....DDD....DDDD...D...........",
                    "ULFRBD",
                ),
                (
                    "...........U...UUUU....UUU....UUUU...U..........................................................................................................................................................................................................................D...DDDD....DDD....DDDD...D...........",
                    "ULFRBD",
                ),
            ),
        )
        # fmt: on


class Build777Step55(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step55",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in vertical stripes
                "L", "L'",
                "R", "R'",
                "3Uw2",
                "3Dw2",
                "Uw2",
                "Dw2",
                "F", "F'", "F2",
                "D", "D'", "D2",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step55.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . R R R . .  . . . . . . .  . . L L L . .  . . . . . . .
 . R L L L R .  . . . . . . .  . L R R R L .  . . . . . . .
 . R L L L R .  . . . . . . .  . L R R R L .  . . . . . . .
 . R L L L R .  . . . . . . .  . L R R R L .  . . . . . . .
 . . R R R . .  . . . . . . .  . . L L L . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


# =============================
# phase 9 - centers daisy solve
# =============================
class Build777Step61(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step61",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step61.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U U U . .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . . U U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . D D D . .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . . D D D . .
                . . . . . . . """,
                    "ascii",
                ),
                (
                    """
                . . . . . . .
                . . D D D . .
                . D U U U D .
                . D U U U D .
                . D U U U D .
                . . D D D . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . U U U . .
                . U D D D U .
                . U D D D U .
                . U D D D U .
                . . U U U . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step62(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step62",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step62.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . R R R . .  . . . . . . .  . . L L L . .  . . . . . . .
 . R L L L R .  . . . . . . .  . L R R R L .  . . . . . . .
 . R L L L R .  . . . . . . .  . L R R R L .  . . . . . . .
 . R L L L R .  . . . . . . .  . L R R R L .  . . . . . . .
 . . R R R . .  . . . . . . .  . . L L L . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step65(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step65",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step65.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . F . . .  . . . . . . .  . . . B . . .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . . . F . . .  . . . . . . .  . . . B . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . B . . .  . . . . . . .  . . . F . . .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . B F F F B .  . . . . . . .  . F B B B F .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . . . B . . .  . . . . . . .  . . . F . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step66(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step66",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step66.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
 . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
 . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . B B B . .  . . . . . . .  . . F F F . .
 . . . . . . .  . B . . . B .  . . . . . . .  . F . . . F .
 . . . . . . .  . B . . . B .  . . . . . . .  . F . . . F .
 . . . . . . .  . B . . . B .  . . . . . . .  . F . . . F .
 . . . . . . .  . . B B B . .  . . . . . . .  . . F F F . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


# =================================================
# phase solve t-centers (for cubes larger than 777)
# =================================================
class Build777Step71(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step71",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step71.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . U U U . .
                . U U U U U .
                . U U U U U .
                . U U U U U .
                . . U U U . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . D D D . .
                . D D D D D .
                . D D D D D .
                . D D D D D .
                . . D D D . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step72(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step72",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step72.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . L L L L L .  . . . . . . .  . R R R R R .  . . . . . . .
 . . L L L . .  . . . . . . .  . . R R R . .  . . . . . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step75(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step75",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step75.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . . F . . .  . . . . . . .  . . . B . . .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . F F F F F .  . . . . . . .  . B B B B B .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . . . F . . .  . . . . . . .  . . . B . . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on


class Build777Step76(BFS):
    def __init__(self):
        # fmt: off
        BFS.__init__(
            self,
            "7x7x7-step76",
            # keep all centers staged
            (
                "3Uw", "3Uw'",
                "Uw", "Uw'",
                "3Lw", "3Lw'",
                "Lw", "Lw'",
                "3Fw", "3Fw'",
                "Fw", "Fw'",
                "3Rw", "3Rw'",
                "Rw", "Rw'",
                "3Bw", "3Bw'",
                "Bw", "Bw'",
                "3Dw", "3Dw'",
                "Dw", "Dw'",

                # keep LR in horizontal stripes
                "L", "L'",
                "R", "R'",
                "3Fw2",
                "3Bw2",
                "Fw2",
                "Bw2",

                # keep UD in vertical stripes
                "U", "U'",
                "D", "D'",
            ),
            "7x7x7",
            "lookup-table-7x7x7-step76.txt",
            False,  # store_as_hex
            (
                (
                    """
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .

 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
 . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
 . . . . . . .  . F . . . F .  . . . . . . .  . B . . . B .
 . . . . . . .  . . F F F . .  . . . . . . .  . . B B B . .
 . . . . . . .  . . . . . . .  . . . . . . .  . . . . . . .

                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . .
                . . . . . . . """,
                    "ascii",
                ),
            ),
        )
        # fmt: on

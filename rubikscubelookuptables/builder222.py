# standard libraries
import logging

# rubiks cube libraries
from rubikscubelookuptables.buildercore import BFS
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, moves_222, rotate_222, solved_222

log = logging.getLogger(__name__)


class StartingStatesBuild222Ultimate(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "2x2x2-ultimate",
            moves_222,
            "2x2x2",
            "starting-states-2x2x2-step00-ultimate.txt",
            False,  # store_as_hex
            # starting cubes
            (
                (
                    """
      U U
      U U

 L L  F F  R R  B B
 L L  F F  R R  B B

      D D
      D D""",
                    "ascii",
                ),
            ),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
            use_c=True,
        )


class Build222Ultimate(BFS):
    def __init__(self):
        BFS.__init__(
            self,
            "2x2x2-ultimate",
            # illegal moves
            (),
            "2x2x2",
            "lookup-table-2x2x2-step00-ultimate.txt",
            False,  # store_as_hex
            # starting cubes
            (
                ("BBBBDDDDLLLLUUUURRRRFFFF", "ULFRBD"),
                ("BBBBLLLLUUUURRRRDDDDFFFF", "ULFRBD"),
                ("BBBBRRRRDDDDLLLLUUUUFFFF", "ULFRBD"),
                ("BBBBUUUURRRRDDDDLLLLFFFF", "ULFRBD"),
                ("DDDDBBBBRRRRFFFFLLLLUUUU", "ULFRBD"),
                ("DDDDFFFFLLLLBBBBRRRRUUUU", "ULFRBD"),
                ("DDDDLLLLBBBBRRRRFFFFUUUU", "ULFRBD"),
                ("DDDDRRRRFFFFLLLLBBBBUUUU", "ULFRBD"),
                ("FFFFDDDDRRRRUUUULLLLBBBB", "ULFRBD"),
                ("FFFFLLLLDDDDRRRRUUUUBBBB", "ULFRBD"),
                ("FFFFRRRRUUUULLLLDDDDBBBB", "ULFRBD"),
                ("FFFFUUUULLLLDDDDRRRRBBBB", "ULFRBD"),
                ("LLLLBBBBDDDDFFFFUUUURRRR", "ULFRBD"),
                ("LLLLDDDDFFFFUUUUBBBBRRRR", "ULFRBD"),
                ("LLLLFFFFUUUUBBBBDDDDRRRR", "ULFRBD"),
                ("LLLLUUUUBBBBDDDDFFFFRRRR", "ULFRBD"),
                ("RRRRBBBBUUUUFFFFDDDDLLLL", "ULFRBD"),
                ("RRRRDDDDBBBBUUUUFFFFLLLL", "ULFRBD"),
                ("RRRRFFFFDDDDBBBBUUUULLLL", "ULFRBD"),
                ("RRRRUUUUFFFFDDDDBBBBLLLL", "ULFRBD"),
                ("UUUUBBBBLLLLFFFFRRRRDDDD", "ULFRBD"),
                ("UUUUFFFFRRRRBBBBLLLLDDDD", "ULFRBD"),
                ("UUUULLLLFFFFRRRRBBBBDDDD", "ULFRBD"),
                ("UUUURRRRBBBBLLLLFFFFDDDD", "ULFRBD"),
            ),
            use_c=True,
        )

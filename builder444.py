#!/usr/bin/env python3

from buildercore import BFS
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444, moves_444, rotate_444
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)


class StartingStates444TsaiPhase0(BFS):
    """
    Combine tsai phases 1 and 2
    - Need all 3 opposite side pairs to be elligible for 12 states
    - Need those to happen at any of 24 rotations
    - Need high/low edges in this too
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase0',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "L", "L'", "Lw", "Lw'",
             "R", "R'", "Rw", "Rw'"),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step01-tsai-phase0.txt',
            False, # store_as_hex

             (
              ("""
          . U D .
          D L L U
          U L L D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D U U U  U F F D  D D D U  U F F D
 U U U D  D F F U  U D D D  D F F U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D L L U
          U L L D
          . D U .""", 'ascii'),

              ("""
          . U D .
          D F F U
          U F F D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D U U U  U L L D  D D D U  U L L D
 U U U D  D L L U  U D D D  D L L U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D F F U
          U F F D
          . D U .""", 'ascii'),

              ("""
          . U D .
          D U U U
          U U U D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U F F D  D R R U  U F F D
 U L L D  D F F U  U R R D  D F F U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D U U U
          U U U D
          . D U .""", 'ascii'),

              ("""
          . U D .
          D F F U
          U F F D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U U U D  D R R U  U U U D
 U L L D  D U U U  U R R D  D U U U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D F F U
          U F F D
          . D U .""", 'ascii'),

              ("""
          . U D .
          D U U U
          U U U D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D F F U  U L L D  D B B U  U L L D
 U F F D  D L L U  U B B D  D L L U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D U U U
          U U U D
          . D U .""", 'ascii'),

              ("""
          . U D .
          D L L U
          U L L D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D F F U  U U U D  D B B U  U U U D
 U F F D  D U U U  U B B D  D U U U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D L L U
          U L L D
          . D U .""", 'ascii'),


            ),
        )


class StartingStates444TsaiPhase0Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase0-centers',
            ("Uw", "Uw'",
             "Dw", "Dw'",
             "Fw", "Fw'",
             "Bw", "Bw'",
             "L", "L'", "Lw", "Lw'",
             "R", "R'", "Rw", "Rw'"),
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step02-tsai-phase0-centers.txt',
            False, # store_as_hex
            # starting cubes
            (("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . x x .  . R R .  . x x .
 . L L .  . x x .  . R R .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),)
        )



class Build444TsaiPhase0(BFS):
    """
    This is a main lookup table.  It will use the UD, LR and FB centers staging prune tables.
    We could make UD, LR and FB prune tables that are solving (not staging) for the 12 possible
    centers patterns for each.  These would have 54 million entries so use hash-cost-only. I'm
    not sure how much this would save us, there are only 70 patterns anwyay so there is a 12/70
    chance we would be driving towards the goal state we want.  Anyway, wait to see how the search
    goes without these 54million entry tables and go from there.

    Once this finishes write a util to traverse the file and re-write the state in centers_edges format
    We need this so when we are doing IDA we can evaluate all of the entries where our centers state
    is a match.  We'll run the steps and look to see if the edgees have been split into high/low groups.
    This is the fastest way I can think of to do this without looping over all 2048 edge orientations.
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase0',
            # TPR also restricts these
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step01-tsai-phase0.txt',
            False, # store_as_hex

            # starting cubes
            (('.UD.DFFUUFFD.DU..DU.DDDUUDDD.UD..DU.ULLDDLLU.UD..DU.DUUUUUUD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DDDUUUUD.UD..DU.ULLDDLLU.UD..DU.DDDUUUUD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DDDUUUUD.UD..DU.ULLDDLLU.UD..DU.DUUUUDDD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DDUUUDUD.UD..DU.ULLDDLLU.UD..DU.DDUUUDUD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DDUUUDUD.UD..DU.ULLDDLLU.UD..DU.DUDUUUDD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DDUUUUDD.UD..DU.ULLDDLLU.UD..DU.DUDUUDUD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DLLUULLD.UD..DU.UUUDDUUU.UD..DU.DRRUURRD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DLLUURRD.UD..DU.UUUDDUUU.UD..DU.DLLUURRD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DLLUURRD.UD..DU.UUUDDUUU.UD..DU.DRRUULLD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DLRUULRD.UD..DU.UUUDDUUU.UD..DU.DLRUULRD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DLRUULRD.UD..DU.UUUDDUUU.UD..DU.DRLUURLD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DLRUURLD.UD..DU.UUUDDUUU.UD..DU.DRLUULRD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DRLUULRD.UD..DU.UUUDDUUU.UD..DU.DLRUURLD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DRLUURLD.UD..DU.UUUDDUUU.UD..DU.DLRUULRD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DRLUURLD.UD..DU.UUUDDUUU.UD..DU.DRLUURLD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DRRUULLD.UD..DU.UUUDDUUU.UD..DU.DLLUURRD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DRRUULLD.UD..DU.UUUDDUUU.UD..DU.DRRUULLD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DRRUURRD.UD..DU.UUUDDUUU.UD..DU.DLLUULLD.UD..DU.UUUDDUUU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DUDUUDUD.UD..DU.ULLDDLLU.UD..DU.DDUUUUDD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DUDUUUDD.UD..DU.ULLDDLLU.UD..DU.DDUUUDUD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DUDUUUDD.UD..DU.ULLDDLLU.UD..DU.DUDUUUDD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DUUUUDDD.UD..DU.ULLDDLLU.UD..DU.DDDUUUUD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DUUUUDDD.UD..DU.ULLDDLLU.UD..DU.DUUUUDDD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DFFUUFFD.DU..DU.DUUUUUUD.UD..DU.ULLDDLLU.UD..DU.DDDUUDDD.UD..DU.ULLDDLLU.UD..UD.DFFUUFFD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DBBUUBBD.UD..DU.UUUDDUUU.UD..DU.DFFUUFFD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DBBUUFFD.UD..DU.UUUDDUUU.UD..DU.DBBUUFFD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DBBUUFFD.UD..DU.UUUDDUUU.UD..DU.DFFUUBBD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DBFUUBFD.UD..DU.UUUDDUUU.UD..DU.DBFUUBFD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DBFUUBFD.UD..DU.UUUDDUUU.UD..DU.DFBUUFBD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DBFUUFBD.UD..DU.UUUDDUUU.UD..DU.DFBUUBFD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DDDUUDDD.UD..DU.UFFDDFFU.UD..DU.DUUUUUUD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DDDUUUUD.UD..DU.UFFDDFFU.UD..DU.DDDUUUUD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DDDUUUUD.UD..DU.UFFDDFFU.UD..DU.DUUUUDDD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DDUUUDUD.UD..DU.UFFDDFFU.UD..DU.DDUUUDUD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DDUUUDUD.UD..DU.UFFDDFFU.UD..DU.DUDUUUDD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DDUUUUDD.UD..DU.UFFDDFFU.UD..DU.DUDUUDUD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DFBUUBFD.UD..DU.UUUDDUUU.UD..DU.DBFUUFBD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DFBUUFBD.UD..DU.UUUDDUUU.UD..DU.DBFUUBFD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DFBUUFBD.UD..DU.UUUDDUUU.UD..DU.DFBUUFBD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DFFUUBBD.UD..DU.UUUDDUUU.UD..DU.DBBUUFFD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DFFUUBBD.UD..DU.UUUDDUUU.UD..DU.DFFUUBBD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DFFUUFFD.UD..DU.UUUDDUUU.UD..DU.DBBUUBBD.UD..DU.UUUDDUUU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DUDUUDUD.UD..DU.UFFDDFFU.UD..DU.DDUUUUDD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DUDUUUDD.UD..DU.UFFDDFFU.UD..DU.DDUUUDUD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DUDUUUDD.UD..DU.UFFDDFFU.UD..DU.DUDUUUDD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DUUUUDDD.UD..DU.UFFDDFFU.UD..DU.DDDUUUUD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DUUUUDDD.UD..DU.UFFDDFFU.UD..DU.DUUUUDDD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DLLUULLD.DU..DU.DUUUUUUD.UD..DU.UFFDDFFU.UD..DU.DDDUUDDD.UD..DU.UFFDDFFU.UD..UD.DLLUULLD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DBBUUBBD.UD..DU.ULLDDLLU.UD..DU.DFFUUFFD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DBBUUFFD.UD..DU.ULLDDLLU.UD..DU.DBBUUFFD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DBBUUFFD.UD..DU.ULLDDLLU.UD..DU.DFFUUBBD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DBFUUBFD.UD..DU.ULLDDLLU.UD..DU.DBFUUBFD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DBFUUBFD.UD..DU.ULLDDLLU.UD..DU.DFBUUFBD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DBFUUFBD.UD..DU.ULLDDLLU.UD..DU.DFBUUBFD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DFBUUBFD.UD..DU.ULLDDLLU.UD..DU.DBFUUFBD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DFBUUFBD.UD..DU.ULLDDLLU.UD..DU.DBFUUBFD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DFBUUFBD.UD..DU.ULLDDLLU.UD..DU.DFBUUFBD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DFFUUBBD.UD..DU.ULLDDLLU.UD..DU.DBBUUFFD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DFFUUBBD.UD..DU.ULLDDLLU.UD..DU.DFFUUBBD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DFFUUFFD.UD..DU.ULLDDLLU.UD..DU.DBBUUBBD.UD..DU.ULLDDLLU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLLUULLD.UD..DU.UFFDDFFU.UD..DU.DRRUURRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DLRUURLD.UD..DU.UFFDDFFU.UD..DU.DRLUULRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUULRD.UD..DU.UFFDDFFU.UD..DU.DLRUURLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..DU.DLRUULRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..DU.DRLUURLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..DU.DLLUURRD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..DU.DRRUULLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD'),
             ('.UD.DUUUUUUD.DU..DU.DRRUURRD.UD..DU.UFFDDFFU.UD..DU.DLLUULLD.UD..DU.UFFDDFFU.UD..UD.DUUUUUUD.DU.', 'ULFRBD')),
            use_centers_then_edges=True
        )


class Build444TsaiPhase0Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase0-centers',
            # TPR also restricts these
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step02-tsai-phase0-centers.txt',
            False, # store_as_hex

            # starting cubes
            (('.....xx..xx..........LL..LL..........xx..xx..........RR..RR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LL..RR..........xx..xx..........LL..RR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LL..RR..........xx..xx..........RR..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LR..LR..........xx..xx..........LR..LR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LR..LR..........xx..xx..........RL..RL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........LR..RL..........xx..xx..........RL..LR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RL..LR..........xx..xx..........LR..RL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RL..RL..........xx..xx..........LR..LR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RL..RL..........xx..xx..........RL..RL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RR..LL..........xx..xx..........LL..RR..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RR..LL..........xx..xx..........RR..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........RR..RR..........xx..xx..........LL..LL..........xx..xx..........xx..xx.....', 'ULFRBD'))
        )


class StartingStates444UDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-UD-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step11-UD-centers-stage.txt',
            False, # store_as_hex

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
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class StartingStates444LRCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LR-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step12-LR-centers-stage.txt',
            False, # store_as_hex

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
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class StartingStates444FBCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-FB-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step13-FB-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . F F .  . x x .  . F F .
 . x x .  . F F .  . x x .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class StartingStates444ULFRBDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-ULFRBD-centers-stage',
            moves_444,
            '4x4x4',
            'starting-states-4x4x4-step10-ULFRBD-centers-stage.txt',
            False, # store_as_hex

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
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class Build444UDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-UD-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step11-UD-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('.....UU..UU..........xx..xx..........xx..xx..........xx..xx..........xx..xx..........UU..UU.....', 'ULFRBD'),
             ('.....xx..xx..........UU..UU..........xx..xx..........UU..UU..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........xx..xx..........UU..UU..........xx..xx..........UU..UU..........xx..xx.....', 'ULFRBD')),
            use_cost_only=True
        )


class Build444LRCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-LR-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step12-LR-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('.....LL..LL..........xx..xx..........xx..xx..........xx..xx..........xx..xx..........LL..LL.....', 'ULFRBD'),
             ('.....xx..xx..........LL..LL..........xx..xx..........LL..LL..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........xx..xx..........LL..LL..........xx..xx..........LL..LL..........xx..xx.....', 'ULFRBD')),
            use_cost_only=True
        )


class Build444FBCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-FB-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step13-FB-centers-stage.txt',
            True, # store_as_hex

            # starting cubes
            (('.....FF..FF..........xx..xx..........xx..xx..........xx..xx..........xx..xx..........FF..FF.....', 'ULFRBD'),
             ('.....xx..xx..........FF..FF..........xx..xx..........FF..FF..........xx..xx..........xx..xx.....', 'ULFRBD'),
             ('.....xx..xx..........xx..xx..........FF..FF..........xx..xx..........FF..FF..........xx..xx.....', 'ULFRBD'),),
            use_cost_only=True
        )


class Build444ULFRBDCentersStage(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-ULFRBD-centers-stage',
            ("Lw", "Lw'", "Lw2",
             "Bw", "Bw'", "Bw2",
             "Dw", "Dw'", "Dw2"),
            '4x4x4',
            'lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt',
            False, # store_as_hex

            # starting cubes
            (('.....FF..FF..........LL..LL..........UU..UU..........LL..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........UU..UU..........LL..LL..........UU..UU..........LL..LL..........FF..FF.....', 'ULFRBD'),
             ('.....LL..LL..........FF..FF..........UU..UU..........FF..FF..........UU..UU..........LL..LL.....', 'ULFRBD'),
             ('.....LL..LL..........UU..UU..........FF..FF..........UU..UU..........FF..FF..........LL..LL.....', 'ULFRBD'),
             ('.....UU..UU..........FF..FF..........LL..LL..........FF..FF..........LL..LL..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..LL..........FF..FF..........LL..LL..........FF..FF..........UU..UU.....', 'ULFRBD'))
        )


class Build444Phase3Edges(BFS):
    """
    This is the TPR phase3 edges table.
    This table will have ~239 million entries.
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase3-edges',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step71-tsai-phase3-edges.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U U .
          U . . U
          U . . U
          . U U .

 . L L .  . F F .  . R R .  . B B .
 L . . L  F . . F  R . . R  B . . B
 L . . L  F . . F  R . . R  B . . B
 . L L .  . F F .  . R R .  . B B .

          . D D .
          D . . D
          D . . D
          . D D .""", 'ascii'),),

            use_edges_pattern=True
        )


class StartingStates444Phase3Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase3-centers',
            moves_444,
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step72-tsai-phase3-centers.txt',
            False, # store_as_hex

            # starting cubes
            (("""
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
          . . . .""", 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class Build444Phase3Centers(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase3-centers',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step72-tsai-phase3-centers.txt',
            False, # store_as_hex

            # starting cubes
            (('.....BB..BB..........DD..DD..........LL..LL..........UU..UU..........RR..RR..........FF..FF.....', 'ULFRBD'),
             ('.....BB..BB..........LL..LL..........UU..UU..........RR..RR..........DD..DD..........FF..FF.....', 'ULFRBD'),
             ('.....BB..BB..........RR..RR..........DD..DD..........LL..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....BB..BB..........UU..UU..........RR..RR..........DD..DD..........LL..LL..........FF..FF.....', 'ULFRBD'),
             ('.....DD..DD..........BB..BB..........RR..RR..........FF..FF..........LL..LL..........UU..UU.....', 'ULFRBD'),
             ('.....DD..DD..........FF..FF..........LL..LL..........BB..BB..........RR..RR..........UU..UU.....', 'ULFRBD'),
             ('.....DD..DD..........LL..LL..........BB..BB..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....DD..DD..........RR..RR..........FF..FF..........LL..LL..........BB..BB..........UU..UU.....', 'ULFRBD'),
             ('.....FF..FF..........DD..DD..........RR..RR..........UU..UU..........LL..LL..........BB..BB.....', 'ULFRBD'),
             ('.....FF..FF..........LL..LL..........DD..DD..........RR..RR..........UU..UU..........BB..BB.....', 'ULFRBD'),
             ('.....FF..FF..........RR..RR..........UU..UU..........LL..LL..........DD..DD..........BB..BB.....', 'ULFRBD'),
             ('.....FF..FF..........UU..UU..........LL..LL..........DD..DD..........RR..RR..........BB..BB.....', 'ULFRBD'),
             ('.....LL..LL..........BB..BB..........DD..DD..........FF..FF..........UU..UU..........RR..RR.....', 'ULFRBD'),
             ('.....LL..LL..........DD..DD..........FF..FF..........UU..UU..........BB..BB..........RR..RR.....', 'ULFRBD'),
             ('.....LL..LL..........FF..FF..........UU..UU..........BB..BB..........DD..DD..........RR..RR.....', 'ULFRBD'),
             ('.....LL..LL..........UU..UU..........BB..BB..........DD..DD..........FF..FF..........RR..RR.....', 'ULFRBD'),
             ('.....RR..RR..........BB..BB..........UU..UU..........FF..FF..........DD..DD..........LL..LL.....', 'ULFRBD'),
             ('.....RR..RR..........DD..DD..........BB..BB..........UU..UU..........FF..FF..........LL..LL.....', 'ULFRBD'),
             ('.....RR..RR..........FF..FF..........DD..DD..........BB..BB..........UU..UU..........LL..LL.....', 'ULFRBD'),
             ('.....RR..RR..........UU..UU..........FF..FF..........DD..DD..........BB..BB..........LL..LL.....', 'ULFRBD'),
             ('.....UU..UU..........BB..BB..........LL..LL..........FF..FF..........RR..RR..........DD..DD.....', 'ULFRBD'),
             ('.....UU..UU..........FF..FF..........RR..RR..........BB..BB..........LL..LL..........DD..DD.....', 'ULFRBD'),
             ('.....UU..UU..........LL..LL..........FF..FF..........RR..RR..........BB..BB..........DD..DD.....', 'ULFRBD'),
             ('.....UU..UU..........RR..RR..........BB..BB..........LL..LL..........FF..FF..........DD..DD.....', 'ULFRBD'))
        )


class StartingStates444Phase3(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase3',
            moves_444,
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step70-tsai-phase3.txt',
            False, # store_as_hex

            # starting cubes
            (("""
          . U U .
          U U U U
          U U U U
          . U U .

 . L L .  . F F .  . R R .  . B B .
 L L L L  F F F F  R R R R  B B B B
 L L L L  F F F F  R R R R  B B B B
 . L L .  . F F .  . R R .  . B B .

          . D D .
          D D D D
          D D D D
          . D D .  """, 'ascii'),),
            legal_moves=("x", "x'", "y", "y'", "z", "z'"),
        )


class Build444Phase3(BFS):
    """
    """

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-phase3',
            ("Uw", "Uw'",
             "Lw", "Lw'",
             "Fw", "Fw'",
             "Rw", "Rw'",
             "Bw", "Bw'",
             "Dw", "Dw'",
             "L", "L'",
             "R", "R'"),
            '4x4x4',
            'lookup-table-4x4x4-step70-tsai-phase3.txt',
            False, # store_as_hex

            # starting cubes
            (('.BB.BBBBBBBB.BB..DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.BB.BBBBBBBB.BB..UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU..RR.RRRRRRRR.RR.', 'ULFRBD'),
             ('.LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR.', 'ULFRBD'),
             ('.LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD..RR.RRRRRRRR.RR.', 'ULFRBD'),
             ('.LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR.', 'ULFRBD'),
             ('.RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD..LL.LLLLLLLL.LL.', 'ULFRBD'),
             ('.RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL.', 'ULFRBD'),
             ('.RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU..LL.LLLLLLLL.LL.', 'ULFRBD'),
             ('.RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD.', 'ULFRBD')),
            use_edges_pattern=True
        )

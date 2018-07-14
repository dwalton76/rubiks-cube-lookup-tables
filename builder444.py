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
          D x x U
          U x x D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D U U U  U x x D  D D D U  U x x D
 U U U D  D x x U  U D D D  D x x U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D x x U
          U x x D
          . D U .""", 'ascii'),

              ("""
          . U D .
          D x x U
          U x x D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D L L U  U x x D  D R R U  U x x D
 U L L D  D x x U  U R R D  D x x U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D x x U
          U x x D
          . D U .""", 'ascii'),

              ("""
          . U D .
          D x x U
          U x x D
          . D U .

 . D U .  . D U .  . D U .  . D U .
 D F F U  U x x D  D B B U  U x x D
 U F F D  D x x U  U B B D  D x x U
 . U D .  . U D .  . U D .  . U D .

          . U D .
          D x x U
          U x x D
          . D U .""", 'ascii'),

            ),
            rotations=["y", "z"]
        )

'''
            # starting cubes
            (("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . U U .  . x x .  . D D .  . x x .
 . U U .  . x x .  . D D .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),

             ("""
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
          . . . .""", 'ascii'),

             ("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . F F .  . x x .  . B B .  . x x .
 . F F .  . x x .  . B B .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),),
'''


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
            (('.UD.DxxUUxxD.DU..DU.DBBUUBBD.UD..DU.UxxDDxxU.UD..DU.DFFUUFFD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DBBUUFFD.UD..DU.UxxDDxxU.UD..DU.DBBUUFFD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DBBUUFFD.UD..DU.UxxDDxxU.UD..DU.DFFUUBBD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DBFUUBFD.UD..DU.UxxDDxxU.UD..DU.DBFUUBFD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DBFUUBFD.UD..DU.UxxDDxxU.UD..DU.DFBUUFBD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DBFUUFBD.UD..DU.UxxDDxxU.UD..DU.DFBUUBFD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DDDUUDDD.UD..DU.UxxDDxxU.UD..DU.DUUUUUUD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DDDUUUUD.UD..DU.UxxDDxxU.UD..DU.DDDUUUUD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DDDUUUUD.UD..DU.UxxDDxxU.UD..DU.DUUUUDDD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DDUUUDUD.UD..DU.UxxDDxxU.UD..DU.DDUUUDUD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DDUUUDUD.UD..DU.UxxDDxxU.UD..DU.DUDUUUDD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DDUUUUDD.UD..DU.UxxDDxxU.UD..DU.DUDUUDUD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DFBUUBFD.UD..DU.UxxDDxxU.UD..DU.DBFUUFBD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DFBUUFBD.UD..DU.UxxDDxxU.UD..DU.DBFUUBFD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DFBUUFBD.UD..DU.UxxDDxxU.UD..DU.DFBUUFBD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DFFUUBBD.UD..DU.UxxDDxxU.UD..DU.DBBUUFFD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DFFUUBBD.UD..DU.UxxDDxxU.UD..DU.DFFUUBBD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DFFUUFFD.UD..DU.UxxDDxxU.UD..DU.DBBUUBBD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DLLUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUURRD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DLRUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUULRD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DRLUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUURLD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DRRUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUULLD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DUDUUDUD.UD..DU.UxxDDxxU.UD..DU.DDUUUUDD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DUDUUUDD.UD..DU.UxxDDxxU.UD..DU.DDUUUDUD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DUDUUUDD.UD..DU.UxxDDxxU.UD..DU.DUDUUUDD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DUUUUDDD.UD..DU.UxxDDxxU.UD..DU.DDDUUUUD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DUUUUDDD.UD..DU.UxxDDxxU.UD..DU.DUUUUDDD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.DUUUUUUD.UD..DU.UxxDDxxU.UD..DU.DDDUUDDD.UD..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DBBUUBBD.UD..DU.UxxDDxxU.UD..DU.DFFUUFFD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DBBUUFFD.UD..DU.UxxDDxxU.UD..DU.DBBUUFFD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DBBUUFFD.UD..DU.UxxDDxxU.UD..DU.DFFUUBBD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DBFUUBFD.UD..DU.UxxDDxxU.UD..DU.DBFUUBFD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DBFUUBFD.UD..DU.UxxDDxxU.UD..DU.DFBUUFBD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DBFUUFBD.UD..DU.UxxDDxxU.UD..DU.DFBUUBFD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DDDUUDDD.UD..DU.UxxDDxxU.UD..DU.DUUUUUUD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DDDUUUUD.UD..DU.UxxDDxxU.UD..DU.DDDUUUUD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DDDUUUUD.UD..DU.UxxDDxxU.UD..DU.DUUUUDDD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DDUUUDUD.UD..DU.UxxDDxxU.UD..DU.DDUUUDUD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DDUUUDUD.UD..DU.UxxDDxxU.UD..DU.DUDUUUDD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DDUUUUDD.UD..DU.UxxDDxxU.UD..DU.DUDUUDUD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DFBUUBFD.UD..DU.UxxDDxxU.UD..DU.DBFUUFBD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DFBUUFBD.UD..DU.UxxDDxxU.UD..DU.DBFUUBFD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DFBUUFBD.UD..DU.UxxDDxxU.UD..DU.DFBUUFBD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DFFUUBBD.UD..DU.UxxDDxxU.UD..DU.DBBUUFFD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DFFUUBBD.UD..DU.UxxDDxxU.UD..DU.DFFUUBBD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DFFUUFFD.UD..DU.UxxDDxxU.UD..DU.DBBUUBBD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DLLUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUURRD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DLRUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUULRD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DRLUULRD.UD..DU.UxxDDxxU.UD..DU.DLRUURLD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DLRUULRD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..DU.UxxDDxxU.UD..DU.DRLUURLD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DLLUURRD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..DU.UxxDDxxU.UD..DU.DRRUULLD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DRRUURRD.UD..DU.UxxDDxxU.UD..DU.DLLUULLD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DUDUUDUD.UD..DU.UxxDDxxU.UD..DU.DDUUUUDD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DUDUUUDD.UD..DU.UxxDDxxU.UD..DU.DDUUUDUD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DUDUUUDD.UD..DU.UxxDDxxU.UD..DU.DUDUUUDD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DUUUUDDD.UD..DU.UxxDDxxU.UD..DU.DDDUUUUD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DUUUUDDD.UD..DU.UxxDDxxU.UD..DU.DUUUUDDD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..DU.DUUUUUUD.UD..DU.UxxDDxxU.UD..DU.DDDUUDDD.UD..UD.DxxUUxxD.DU.', 'ULFRBD'),
             ('.UD.UBBDDBBU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UFFDDFFU.DU.', 'ULFRBD'),
             ('.UD.UBBDDFFU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UBBDDFFU.DU.', 'ULFRBD'),
             ('.UD.UBBDDFFU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UFFDDBBU.DU.', 'ULFRBD'),
             ('.UD.UBFDDBFU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UBFDDBFU.DU.', 'ULFRBD'),
             ('.UD.UBFDDBFU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UFBDDFBU.DU.', 'ULFRBD'),
             ('.UD.UBFDDFBU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UFBDDBFU.DU.', 'ULFRBD'),
             ('.UD.UDDDDDDU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UUUDDUUU.DU.', 'ULFRBD'),
             ('.UD.UDDDDUUU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UDDDDUUU.DU.', 'ULFRBD'),
             ('.UD.UDDDDUUU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UUUDDDDU.DU.', 'ULFRBD'),
             ('.UD.UDUDDDUU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UDUDDDUU.DU.', 'ULFRBD'),
             ('.UD.UDUDDDUU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UUDDDUDU.DU.', 'ULFRBD'),
             ('.UD.UDUDDUDU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UUDDDDUU.DU.', 'ULFRBD'),
             ('.UD.UFBDDBFU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UBFDDFBU.DU.', 'ULFRBD'),
             ('.UD.UFBDDFBU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UBFDDBFU.DU.', 'ULFRBD'),
             ('.UD.UFBDDFBU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UFBDDFBU.DU.', 'ULFRBD'),
             ('.UD.UFFDDBBU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UBBDDFFU.DU.', 'ULFRBD'),
             ('.UD.UFFDDBBU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UFFDDBBU.DU.', 'ULFRBD'),
             ('.UD.UFFDDFFU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UBBDDBBU.DU.', 'ULFRBD'),
             ('.UD.ULLDDLLU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.URRDDRRU.DU.', 'ULFRBD'),
             ('.UD.ULLDDRRU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.ULLDDRRU.DU.', 'ULFRBD'),
             ('.UD.ULLDDRRU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.URRDDLLU.DU.', 'ULFRBD'),
             ('.UD.ULRDDLRU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.ULRDDLRU.DU.', 'ULFRBD'),
             ('.UD.ULRDDLRU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.URLDDRLU.DU.', 'ULFRBD'),
             ('.UD.ULRDDRLU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.URLDDLRU.DU.', 'ULFRBD'),
             ('.UD.URLDDLRU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.ULRDDRLU.DU.', 'ULFRBD'),
             ('.UD.URLDDRLU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.ULRDDLRU.DU.', 'ULFRBD'),
             ('.UD.URLDDRLU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.URLDDRLU.DU.', 'ULFRBD'),
             ('.UD.URRDDLLU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.ULLDDRRU.DU.', 'ULFRBD'),
             ('.UD.URRDDLLU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.URRDDLLU.DU.', 'ULFRBD'),
             ('.UD.URRDDRRU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.ULLDDLLU.DU.', 'ULFRBD'),
             ('.UD.UUDDDDUU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UDUDDUDU.DU.', 'ULFRBD'),
             ('.UD.UUDDDUDU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UDUDDDUU.DU.', 'ULFRBD'),
             ('.UD.UUDDDUDU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UUDDDUDU.DU.', 'ULFRBD'),
             ('.UD.UUUDDDDU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UDDDDUUU.DU.', 'ULFRBD'),
             ('.UD.UUUDDDDU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UUUDDDDU.DU.', 'ULFRBD'),
             ('.UD.UUUDDUUU.DU..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.DxxUUxxD.DU..DU.UxxDDxxU.UD..UD.UDDDDDDU.DU.', 'ULFRBD'))
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



class Build444TsaiPhase1Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase1-centers',
            (),
            '4x4x4',
            'lookup-table-4x4x4-step50-tsai-phase1.txt',
            True, # store_as_hex

            # starting cubes
            (
             ("""
          . . . .
          . L L .
          . L L .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . x x .  . x x .  . x x .
 . x x .  . x x .  . x x .  . x x .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . L L .
          . L L .
          . . . .""", 'ascii'),

             ("""
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
          . . . .""", 'ascii'),

             ("""
          . . . .
          . x x .
          . x x .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . x x .  . L L .  . x x .  . L L .
 . x x .  . L L .  . x x .  . L L .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . x x .
          . x x .
          . . . .""", 'ascii'),
            ))


class StartingStates444TsaiPhase2Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-centers',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "L", "L'", "R", "R'",
             "Lw", "Lw'", "Rw", "Rw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'starting-states-lookup-table-4x4x4-step61-tsai-phase2-centers.txt',
            False, # store_as_hex

            # starting cubes
           (("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . F F .  . R R .  . F F .
 . L L .  . F F .  . R R .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),

            ("""
          . . . .
          . U U .
          . U U .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R R .  . F F .  . L L .  . F F .
 . R R .  . F F .  . L L .  . F F .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . U U .
          . U U .
          . . . .""", 'ascii'),


            ("""
          . . . .
          . F F .
          . F F .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . L L .  . U U .  . R R .  . U U .
 . L L .  . U U .  . R R .  . U U .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . F F .
          . F F .
          . . . .""", 'ascii'),

            ("""
          . . . .
          . F F .
          . F F .
          . . . .

 . . . .  . . . .  . . . .  . . . .
 . R R .  . U U .  . L L .  . U U .
 . R R .  . U U .  . L L .  . U U .
 . . . .  . . . .  . . . .  . . . .

          . . . .
          . F F .
          . F F .
          . . . .""", 'ascii')),
        )


class Build444TsaiPhase2Centers(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-centers',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'lookup-table-4x4x4-step61-tsai-phase2-centers.txt',
            False, # store_as_hex

            # starting cubes
            (('.....FF..FF..........LL..LL..........UU..UU..........RR..RR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LL..RR..........UU..UU..........LL..RR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LL..RR..........UU..UU..........RR..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LR..LR..........UU..UU..........LR..LR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LR..LR..........UU..UU..........RL..RL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........LR..RL..........UU..UU..........RL..LR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RL..LR..........UU..UU..........LR..RL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RL..RL..........UU..UU..........LR..LR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RL..RL..........UU..UU..........RL..RL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RR..LL..........UU..UU..........LL..RR..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RR..LL..........UU..UU..........RR..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....FF..FF..........RR..RR..........UU..UU..........LL..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....UU..UU..........LL..LL..........FF..FF..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..RR..........FF..FF..........LL..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LL..RR..........FF..FF..........RR..LL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..LR..........FF..FF..........LR..LR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..LR..........FF..FF..........RL..RL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........LR..RL..........FF..FF..........RL..LR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..LR..........FF..FF..........LR..RL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..RL..........FF..FF..........LR..LR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RL..RL..........FF..FF..........RL..RL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..LL..........FF..FF..........LL..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..LL..........FF..FF..........RR..LL..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....UU..UU..........RR..RR..........FF..FF..........LL..LL..........FF..FF..........UU..UU.....', 'ULFRBD'))
        )


class Build444TsaiPhase2Edges(BFS):

    def __init__(self):
        BFS.__init__(self,
            '4x4x4-tsai-phase2-edges',
            ("Fw", "Fw'",
             "Bw", "Bw'",
             "Uw", "Uw'",
             "Dw", "Dw'",
             "Bw2", "Dw2", "Lw", "Lw'", "Lw2"), # TPR also restricts these
            '4x4x4',
            'lookup-table-4x4x4-step62-tsai-phase2-edges.txt',
            False, # store_as_hex

            # starting cubes
             (("""
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
          . D U .""", 'ascii'),)
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
            (('.....BB..BB..........LL..LL..........UU..UU..........RR..RR..........DD..DD..........FF..FF.....', 'ULFRBD'),
             ('.....BB..BB..........RR..RR..........DD..DD..........LL..LL..........UU..UU..........FF..FF.....', 'ULFRBD'),
             ('.....DD..DD..........LL..LL..........BB..BB..........RR..RR..........FF..FF..........UU..UU.....', 'ULFRBD'),
             ('.....DD..DD..........RR..RR..........FF..FF..........LL..LL..........BB..BB..........UU..UU.....', 'ULFRBD'),
             ('.....FF..FF..........LL..LL..........DD..DD..........RR..RR..........UU..UU..........BB..BB.....', 'ULFRBD'),
             ('.....FF..FF..........RR..RR..........UU..UU..........LL..LL..........DD..DD..........BB..BB.....', 'ULFRBD'),
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
#            use_edges_pattern=True
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
            (('.BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..UU.UUUUUUUU.UU..FF.FFFFFFFF.FF.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..BB.BBBBBBBB.BB..UU.UUUUUUUU.UU.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..DD.DDDDDDDD.DD..BB.BBBBBBBB.BB.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..DD.DDDDDDDD.DD.', 'ULFRBD'),
             ('.UU.UUUUUUUU.UU..RR.RRRRRRRR.RR..BB.BBBBBBBB.BB..LL.LLLLLLLL.LL..FF.FFFFFFFF.FF..DD.DDDDDDDD.DD.', 'ULFRBD')),
            use_edges_pattern=True
        )

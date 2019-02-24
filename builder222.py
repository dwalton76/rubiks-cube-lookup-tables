#!/usr/bin/env python3

from buildercore import BFS
from rubikscubennnsolver.RubiksCube222 import RubiksCube222, solved_222, moves_222, rotate_222
import logging
import math
import shutil
import subprocess
import sys

log = logging.getLogger(__name__)


class Build222Ultimate(BFS):

    def __init__(self):
        BFS.__init__(self,
            '2x2x2-ultimate',

            # illegal moves
            (),

            '2x2x2',
            'lookup-table-2x2x2-step00-ultimate.txt',
            False, # store_as_hex

            # starting cubes
            (("""
      U U
      U U

 L L  F F  R R  B B
 L L  F F  R R  B B

      D D
      D D""", 'ascii'),),
        )


#!/usr/bin/env python3

import re
import sys
filename = sys.argv[1]
filename_tmp = filename + '.tmp'

with open(filename_tmp, 'w') as fh_new:
    with open(filename, 'r') as fh:
        for line in fh:
            (state, steps) = line.strip().split(':')
            re_line_444 = re.search('(...)UU(..)UU(......)LL(..)LL(......)FF(..)FF(......)RR(..)RR(......)BB(..)BB(......)DD(..)DD(...)', line)

            if re_line_444:
                new_state = re_line_444.group(1) +\
                    re_line_444.group(2) +\
                    re_line_444.group(3) +\
                    re_line_444.group(4) +\
                    re_line_444.group(5) +\
                    re_line_444.group(6) +\
                    re_line_444.group(7) +\
                    re_line_444.group(8) +\
                    re_line_444.group(9) +\
                    re_line_444.group(10) +\
                    re_line_444.group(11) +\
                    re_line_444.group(12) +\
                    re_line_444.group(13)
                fh_new.write("%s:%s\n" % (new_state, steps))

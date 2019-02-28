#!/usr/bin/env python3

# http://cubesolvingprograms.freeforums.net/thread/62/solving-centers-opposite-sides-first?page=1&scrollTo=508
'''
# 5x5x5 gods number
depth = 4
prev_count_at_depth = 810831
count_total = 840729
rate = float(28.1)
count_total_target = 282870942277741856536180333107150328293127731985672134721536000000 # 555

# 3x3x3 gods number
depth = 5
prev_count_at_depth = 574908
count_total = 621648
rate = float(13.3)
count_total_target = 43252003274489856000  # 333

# 4x4x4 gods number
depth = 4
prev_count_at_depth = 754156
count_total = 783364
rate = float(26.79)
count_total_target = 7401196841564901869874093974498574336000000000 # 444
'''

# 4x4x4 centers
'''
depth = 6
prev_count_at_depth = 83113883
count_total = 87727430
rate = float(19)
count_total_target = 3246670537110000 # 24!/(4!^6)
'''

# 5x5x5 centers OBTM
depth = 5
prev_count_at_depth = 6089454
count_total = 6356707
rate = float(23.79)
count_total_target = 10540869576538135887152100000000 # (24!/(4!^6))^2

# 5x5x5 centers SSTM
depth = 5
prev_count_at_depth = 5977856
count_total = 6242706
rate = float(23.57)
count_total_target = 10540869576538135887152100000000 # (24!/(4!^6))^2

# 5x5x5 centers BTM
depth = 5
prev_count_at_depth = 32528054
count_total = 33435924
rate = float(36.84)
count_total_target = 10540869576538135887152100000000 # (24!/(4!^6))^2



# 5x5x5 horseshoe stage
depth = 11
prev_count_at_depth = 80163256
count_total = 109442672
rate = float(3.76)
count_total_target = 2498640144 # (24!/(12!*12!)) * (12!/(6!*6!)) states

'''
# 5x5x5 horseshoe stage with centers solved
depth = 6
prev_count_at_depth = 17036649
count_total = 18635362
rate = float(11.57)
count_total_target = 2498640144 # (24!/(12!*12!)) * (12!/(6!*6!)) states
'''

# 5x5x5 UD centers solve without staging
# OBTM
depth = 6
prev_count_at_depth = 52950453
count_total = 55532432
rate = float(21.50)
count_total_target = 2650496200020900 # (24!/(4!*4!*16!))^2

# SSTM
depth = 5
prev_count_at_depth = 1943490
count_total = 2048891
rate = float(19.42)
count_total_target = 2650496200020900 # (24!/(4!*4!*16!))^2

# BTM
depth = 5
prev_count_at_depth = 10332666
count_total = 10671963
rate = float(31.46)
count_total_target = 2650496200020900 # (24!/(4!*4!*16!))^2




move_total = 0

while count_total < count_total_target:
    depth += 1
    rate -= 0.8
    count_at_depth = int(prev_count_at_depth * rate)

    if (count_total + count_at_depth) > count_total_target:
        count_at_depth = count_total_target - count_total

    count_total += count_at_depth
    move_total += depth * count_at_depth

    print("    {:,} steps has {:,} entries ({}x previous step)".format(
        depth, count_at_depth, "{0:.2f}".format(count_at_depth/prev_count_at_depth)))

    prev_count_at_depth = count_at_depth

print("\n    Average: {:,}".format(move_total/count_total))
print("    Total  : {:,}\n".format(count_total))

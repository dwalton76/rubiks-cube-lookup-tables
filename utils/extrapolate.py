#!/usr/bin/env python3

# http://cubesolvingprograms.freeforums.net/thread/62/solving-centers-opposite-sides-first?page=1&scrollTo=508
"""
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
"""

# 4x4x4 centers
"""
depth = 6
prev_count_at_depth = 83113883
count_total = 87727430
rate = float(19)
count_total_target = 3246670537110000 # 24!/(4!^6)

# 4x4x4 centers stage
depth = 7
prev_count_at_depth = 112158744
count_total = 121951614
rate = float(12.41)
count_total_target = 9465511770 # 24!/(8!*8!*8!)

# 4x4x4 centers stage
depth = 4
prev_count_at_depth = 1948920
count_total = 2136760
rate = float(11.31)
count_total_target = 27136746291200


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


# 5x5x5 horseshoe solve
depth = 10
prev_count_at_depth = 312556
count_total = 399143
rate = float(4.38)
count_total_target = 479001600 # 12!

# 5x5x5 solve centers with staging
depth = 6
prev_count_at_depth = 1291295
count_total = 1433448
rate = float(10)
count_total_target = 117649000000 # ((8!/(4!*4!))^2)^3

# 555 LR stage 432 and EO both orbits
depth = 5
prev_count_at_depth = 24348560
count_total = 26485320
rate = float(12.49)
count_total_target = 27136746291200

# 555 EO both orbits
depth = 7
prev_count_at_depth = 5353259
count_total = 5946658
rate = float(9.89)
count_total_target = 5538111488
"""

# 555 LR centers stage
depth = 6
prev_count_at_depth = 16300291
count_total = 17168476
rate = float(19.76)
count_total_target = 540917591841

"""
# 666 stage UD centers
depth = 6
prev_count_at_depth = 633025
count_total = 690675
rate = float(11.97)
count_total_target = 2131746903000
"""

move_total = 0

while count_total < count_total_target:
    depth += 1

    if rate > 2.8:
        rate -= 0.8

    count_at_depth = int(prev_count_at_depth * rate)

    if (count_total + count_at_depth) > count_total_target:
        count_at_depth = count_total_target - count_total

    count_total += count_at_depth
    move_total += depth * count_at_depth

    print(
        "    {:,} steps has {:,} entries ({}x previous step)".format(
            depth, count_at_depth, "{0:.2f}".format(count_at_depth / prev_count_at_depth)
        )
    )

    prev_count_at_depth = count_at_depth

print(f"\n    Average: {move_total / count_total:,}")
print(f"    Total  : {count_total:,}\n")

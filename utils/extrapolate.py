#!/usr/bin/env python3

# http://cubesolvingprograms.freeforums.net/thread/62/solving-centers-opposite-sides-first?page=1&scrollTo=508

depth = 4
prev_count_at_depth = 810831
count_total = 840729 
rate = float(28.1)
count_total_target = 282870942277741856536180333107150328293127731985672134721536000000 # 555

depth = 5
prev_count_at_depth = 574908
count_total = 621648
rate = float(13.3)
count_total_target = 43252003274489856000  # 333


depth = 4
prev_count_at_depth = 754156
count_total = 783364
rate = float(26.79)
count_total_target = 7401196841564901869874093974498574336000000000 # 444



while count_total < count_total_target:
    depth += 1
    #rate -= 0.1
    count_at_depth = int(prev_count_at_depth * rate)

    if (count_total + count_at_depth) > count_total_target:
        count_at_depth = count_total_target - count_total

    count_total += count_at_depth

    print("    {:,} steps has {:,} entries ({}x previous step)".format(depth, count_at_depth, "{0:.2f}".format(count_at_depth/prev_count_at_depth)))

    prev_count_at_depth = count_at_depth

print("\nTotal: {:,}".format(count_total))

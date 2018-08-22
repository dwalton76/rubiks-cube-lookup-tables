#!/usr/bin/env python3

# http://cubesolvingprograms.freeforums.net/thread/62/solving-centers-opposite-sides-first?page=1&scrollTo=508

depth = 5
prev_count_at_depth = 2462410
count_total = 2581979
rate = 21
count_total_target = 2650496200020900

while count_total < count_total_target:
    depth += 1

    if rate > 3:
        rate -= 2

    count_at_depth = prev_count_at_depth * rate

    if count_total + count_at_depth > count_total_target:
        count_at_depth = count_total_target - count_total

    count_total += count_at_depth

    print("    {:,} steps has {:,} entries ({}x previous step)".format(depth, count_at_depth, count_at_depth/prev_count_at_depth))

    prev_count_at_depth = count_at_depth

print("\nTotal: {:,}".format(count_total))

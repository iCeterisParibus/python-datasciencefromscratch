from __future__ import division
from collections import Counter
import random

num_observations = random.randrange(200, 300)

num_friends = [random.choice(range(100))
               for _ in range(num_observations)]

def mean(x):
    return sum(x) / len(x)

friends_mean = mean(num_friends)

def median(v):
    """finds the 'middle most' value of V"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n% 2 == 1:
        # if odd, return middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of two middle points
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

friends_median = median(num_friends)

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.90)

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

friends_mode = mode(num_friends)

print """
Mean: %s
Median: %s
Mode: %s
""" % (friends_mean, friends_median, friends_mode)

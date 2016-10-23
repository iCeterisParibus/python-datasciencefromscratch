from __future__ import division
from collections import Counter
from matplotlib import pyplot as plt
import random
import math

# random.seed(###) Uncomment and type in a number for '###' for reproducable data

# Since we are not using a pre-built library for our analysis, below are the
# functions builds we will need

# Central Tendencies: Mean, Median, Mode

# Mean: returns the mean of a numeric vector
def mean(x):
    return sum(x) / len(x)

# Median: returns the median value of a numeric vector
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

# Mode: returns the mode(s) of a numeric vector
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

# Quantile: returns the pth-percentile value for a numeric vector and user defined p
def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

# Dispersion: range, variance, standard deviations, interquartile

# Dot-product: returns the dot-product of two user defined vectors
def dot(v,w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
           for v_i, w_i in zip(v, w))

# Sum of Squares: returns the sum of squares for a numeric vector
def sum_of_squares(x):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(x, x)

# Range: returns the mathematical range of a numeric vector
def data_range(x):
    return max(x) - min(x)

# Deviation from Mean: Returns the deviation from mean for a numeric vector
def dev_mean(x):
    """translates x by subtracting its mean from every observation (so that the
    result has a mean = 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

# Variance: returns the variance of a numeric vector
def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = dev_mean(x)
    return sum_of_squares(deviations) / (n-1)

# Standard Deviation: returns the standard deviation of a numeric vector
def standard_deviation(x):
    return math.sqrt(variance(x))

# Interquartile Range: returns the interquartile range of a numeric vector
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

# Relationship statistics:

# Covariance: returns the covariance of two numeric vectors
def covariance(x, y):
    n = len(x)
    return dot(dev_mean(x), dev_mean(y)) / (n-1)

# Correlation: returns the correlation for two numeric vectors
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation equals zero

# Building Datasets:

# cheap trick to get more interesting data
num_observations = random.randrange(200, 300)
obs_10 = num_observations // 10
obs_50 = num_observations // 2
obs_99 = num_observations - 1
obs_100 = num_observations

# populating the data with one outlier and semi positive correlation
num_f_10 = [random.choice(range(30))
           for _ in range(obs_10)]
num_f_50 = [random.choice(range(10, 70))
           for _ in range(obs_10, obs_50)]
num_f_99 = [random.choice(range(50, 80))
           for _ in range(obs_50, obs_99)]
num_f_100 = [random.choice(range(99, 100))
           for _ in range(obs_99, obs_100)]

# combining the four independent list into a single list for analysis
num_friends = num_f_10 + num_f_50 + num_f_99 + num_f_100

# building the daily mintes data set
num_m_10 = [random.choice(range(10))
           for _ in range(obs_10)]
num_m_50 = [random.choice(range(10, 40))
           for _ in range(obs_10, obs_50)]
num_m_99 = [random.choice(range(30, 60))
           for _ in range(obs_50, obs_99)]
num_m_100 = [random.choice(range(99, 100))
           for _ in range(obs_99, obs_100)]

daily_minutes = num_m_10 + num_m_50 + num_m_99 + num_m_100



# Analysis of Data using constructed functions:

friends_mean = mean(num_friends)
friends_median = median(num_friends)
friends_mode = mode(num_friends)
friends_10 = quantile(num_friends, 0.10)
friends_25 = quantile(num_friends, 0.25)
friends_75 = quantile(num_friends, 0.75)
friends_90 = quantile(num_friends, 0.90)
friends_range = data_range(num_friends)
friends_variance = variance(num_friends)
friends_stdev = standard_deviation(num_friends)
friends_interquartile = interquartile_range(num_friends)
friends_cov = covariance(num_friends, daily_minutes)
friends_corr = correlation(num_friends, daily_minutes)

# After noticing the outlier (we purposely put in) we can remove it from our
# correlation calculation to see if we get a stronger relationship

outlier = num_friends.index(99)
num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]
daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]
new_friends_corr = correlation(num_friends_good, daily_minutes_good)

print """
Mean # of friends: %s
Median # of friends: %s
Mode # of friends: %s
10th Percentile # of friends: %s
25th Percentile # of friends: %s
75th Percentile # of friends: %s
90th Percentile # of friends: %s
Range # of friends: %s
Variance # of friends: %s
Standard deviation # of friends: %s
Interquartile range # of friends: %s
Covariance (friends, minutes): %s
Correlation (friends, minutes): %s
Correlation (Outlier removed): %s
""" % (friends_mean, friends_median, friends_mode, friends_10, friends_25,
       friends_75, friends_90, friends_range, friends_variance, friends_stdev,
       friends_interquartile, friends_cov, friends_corr, new_friends_corr)

plt.scatter(num_friends, daily_minutes)
plt.axis([-5, 105, -5, 105])
plt.title("Number of Friends vs. Daily Minutes on Website")
plt.xlabel("# of friends")
plt.ylabel("# of daily minutes")
plt.show()

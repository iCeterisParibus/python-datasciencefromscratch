import random
import matplotlib.pyplot as plt
import math

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf( (x-mu) / math.sqrt(2) / sigma )) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma *  inverse_normal_cdf(p, tolerance)

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

def random_normal():
    """returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())

random.seed(0)

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Very Different Joint Distributions")
plt.show()

def dot(v,w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
           for v_i, w_i in zip(v, w))

def sum_of_squares(x):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(x, x)

def mean(x):
    return sum(x) / len(x)

def dev_mean(x):
    """translates x by subtracting its mean from every observation (so that the
    result has a mean = 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = dev_mean(x)
    return sum_of_squares(deviations) / (n-1)

def standard_deviation(x):
    return math.sqrt(variance(x))

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

print "Correlation of xs and ys1: %s" % correlation(xs, ys1)
print "Correlation of xs and ys2: %s" % correlation(xs, ys2)

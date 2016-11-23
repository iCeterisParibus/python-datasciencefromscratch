from __future__ import division
import math

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf( (x-mu) / math.sqrt(2) / sigma )) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma *  inverse_normal_cdf(p, tolerance=tolerance)

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

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1-probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    #lower bound shouldhave tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)
lower, upper = normal_two_sided_bounds(0.95, mu, sigma)


p_hat_2 = 540 / 1000
mu_2 = p_hat_2
sigma_2 = (p_hat_2 * (1  - p_hat_2) / 1000)
lower_1, upper_1 = normal_two_sided_bounds(0.95, mu_2, sigma_2)


print '-' * 100
print """
We've been testing hypothesis about the value of the heads probability, p, which
is a parameter of the unknown "heads" distribution.

A third approach is viable in these situations. We can constructa 'confidence
interval' around the observed value of the parameter.

For example, we can estimate the probability of an unfair coin by looking at the
average value of the Bernoulli variables corresponding to each flip,
1 if heads, 0 if tails. If we observe 525 heads out of 1000 filps, then we
estimate p equals 0.525.

How confident can we be about this estimate? Well if we know the exact value of
p, the Central Limit Theorem tells us that the average of these Bernoulli
variables should be approximately normal, with:

mean = p
standard deviation = (p * (1 - p) / n)

Here, we don't know p so we use our estimate 'p_hat', which gives us

mu = %s
standard deviation = %s

This isn't entirely justified, but people seem to do it anyway. Using the
normal approximation, we conclude that we are \"95%% confident\" that the following
interval contains the true parameter p:

confidence interval = [%s, %s]

In particular, we do not conclude that the coin is unfair, since 0.5 falls
within our confidece interval.

If instead we'd seen 540 heads, then we'd have:

mu = %s
standard deviation = %s
confidence interval = [%s, %s]

Here, \"fair coin\" doesn't lie in the confidence interval. (The \"fair coin\"
hypothesis doesn't pass a test that you'd expect it to pass 95%% of the time
if it were True.)
 """ % (mu, sigma, lower, upper, mu_2, sigma_2, lower_1, upper_1)

print '-' * 100

# Hypothesis testing is a key funcction of being a data scientist

from __future__ import division
from collections import Counter
import math
import random

# We'll need some functions that we've created in a different script

# Normal Distribution:

def normal_pdf (x, mu = 0, sigma = 1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2)) / (sqrt_two_pi * sigma)

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

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

### The following functions are specific to this lesson

def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# the normal_cdf __is__ the probability the variable is below the threshold
normal_probability_below = normal_cdf

# its above the threshold if its not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# its between if its less than hi but no less than low
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# its outside if its not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

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

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

normal_two_sided_bounds(0.95, mu_0, sigma_0)

# 95% bounds based on assumption p is 0.5
lo_0, hi_0 = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type II error means we fail to reject the null hypothesis
# which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo_0, hi_0, mu_1, sigma_1)
power_2 = 1 - type_2_probability

hi = normal_upper_bound(0.95, mu_0, sigma_0)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power_1 = 1 - type_2_probability

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is
        # what is greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)

p_value = two_sided_p_value(529.5, mu_0, sigma_0)

extreme_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000))

    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

sim_1 = extreme_value_count / 100000

p_value_2 = two_sided_p_value(531.5, mu_0, sigma_0)

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

upper_p_1 = upper_p_value(524.5, mu_0, sigma_0)

upper_p_2 = upper_p_value(526.5, mu_0, sigma_0)

print '-' * 100
print """
As data scientist, hypothesis testing will be a valueable concept.

Under various assumptions, the statistics we calculate can be thought of
as observations of random variables from known distributions, which allows us to
make statements about how likely those assumptions are to hold.

In the classic setup, we will have a 'null hypothesis', H_0, that represents some
default position and some 'alternative hypothesis', H_1, that we'd like to
compare it with. We'll use statistics to decide whether we can reject the null
hypothesis as false or not.

Example: 'fair coin'; H_0: p = 0.5, H_1: p != 0.5

We can simulate flipping a coin 'n' times and count the number of heads.
Each flip is a Bernoulli trial, so X is a Binomial(n, p) random variable which
we can approximate using the normal distribution:

    def normal_approximation_to_binomial(n, p):
        \"\"\"finds mu and sigma corresponding to a Binomial(n, p)\"\"\"
        mu = p * n
        sigma = math.sqrt(p * (1 - p) * n)
        return mu, sigma

Whenever a random variable follows a normal distribution, we can use 'normal_cdf'
to figure out the probability that its realized value lies within (or outside) a
particular interval.

To check below the threshold, we'll simply use the 'normal_cdf', to check above
the threshold which can be done using '1 - normal_cdf', to check between the
lo and hi interval by subtracting 'normal_cdf(hi) - normal_cdf(lo)', and if it's
outside of the interval by calculating 1 - probability of between.

We've built the following functions to perform these calculations:

    normal_probability_below(p, mu, sigma)
    normal_probability_above(lo, mu, sigma)
    normal_probability_between(lo, hi, mu, sigma)
    normal_probability_outside(lo, hi, mu, sigma)

We can also do the reverse - find either the nontail region or the (symmetric)
interval around the mean that accounts for a certain level of likelihood.

Keeping in mind that the data needs to be normally distributed in order for
these bounds to hold true, we can use the 'inverse_normal_cdf' function we
built to determine the upper bound, lower bound, and two sided bounds using
the following functions:

    normal_upper_bound(probability, mu, sigma)
    normal_lower_bound(probability, mu, sigma)
    normal_two_sided_bounds(probability, mu, sigma)

Let's say we choose 'n=1000'. If our hypothesis is true, X should be distributed
approximately normal with mean 500 and standard deviation 15.8:

Actual computation: mu = %s, sigma = %s

We need to make a decision about 'significance' - how willing we are to make a
Type I error (false positive) in which we reject H_0, even though it's True.

Historically, 5%% or 1%% are the most common levels.

Consider the test that rejects H_0 if X falls outside of the bounds given by:

    normal_two_sided_bounds(0.95, m_0, sigma_0)

Assuming p really is equal to 0.5 (H_0 is True), thereis just a 5%% chance we
observe an X that lies outside this interval, which is the exact significance
we wanted. If H_0 is true, then approximately 19 out of 20 times, this test will
give the correct result.

We often are also interested in the 'power' of a test, which is the probability
of not making a Type II error, fail to reject H_0 even though False. In order to
measure this, we have to specify what exactly H_0 being False means. Knowing p
is not 0.5 doesn't give us much about the distribution of X. In particular,
let's check what happens if p is really 0.55 so a coin has a slight bias toward
heads:

The 95%% bounds based on p = 0.5 are [%s, %s]

Now assume that we have a coin which is slightly bias toward heads, p = 0.55, we
would end up with mu = %s and sigma = %s and our statistical power
using these is %s.

Now suppose instead that H_0 was that the coin is not bias toward heads or p <= 0.5.
In this case we want a 'one-sided test' that rejects the H_0 when X is larger
than 500 but not where X is smaller than 500. So a 5%% significance test involves
determining the cutoff below which 95%% of the probability lies.

Upper bound = %s
Power = %s

This is a more powerful test since it no longer rejects H_0 when X is below 469
(which is very unlikely if H_1 is true) and instead rejects H_0 when X is
between 526 and 531 (which is somewhat likely to happen if H_1 is true).

An alternative way of thinking about the preceding test involves p-values. Instead
of choosing bounds based on some probability cutoff, we compute the probability -
assuming H_0 is True - that we would see a value at least as extreme as the
one we actually observed.

For a two-sided test of whether the voin is fair:

    two_sided_p_value(529.5, mu_0, sigma_0)

Our p-value = %s

Using 529.5 instead of 530 is what's called a 'Continuity Correction' which
reflects the fact that checking between 529.5 - 530.5 is a better estimate than
checking between 530 - 531.

One way to convince ourselves this is a sensible estimate is with a simulation.
We can build an extreme value counter which increments our counter by 1 every time
we witness more than 530 or less than 470 out of 1000 flips over a total of 100000
cycles.

If the calculated p-value is greater than 5%% significance we do not reject the
null hypothesis. Our calculated p-value for the simulation is %s which is larger
than our 5%% significance level.

If we were to see 532 heads the p-value would be: %s
Which is less than 5%%, so we would reject the null hypothesis.

For our one-sided test, if we saw 525 heads we'd compute a p-value of: %s
If we saw 527 heads, the computation would be a p-value of: %s
We would reject the null only for 527 as the p-value is less than 0.05.

""" % (mu_0, sigma_0, lo_0, hi_0, mu_1, sigma_1, power_2, hi, power_1,
       p_value, sim_1, p_value_2, upper_p_1, upper_p_2)
print '-' * 100

# This is an example of Running an A B Test

from __future__ import division
import math

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf( (x-mu) / math.sqrt(2) / sigma )) / 2

normal_probability_below = normal_cdf

# its above the threshold if its not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is
        # what is greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)

def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z_1 = a_b_test_statistic(1000, 200, 1000, 180)

p_value_1 = two_sided_p_value(z_1)

z_2 = a_b_test_statistic(1000, 200, 1000, 150)\

p_value_2 = two_sided_p_value(z_2)

print '-' * 100
print """
The phrase \"experience optimization\" is a euphemism for trying to get people
to click on advertisements. Your tasked with choosing between ad A \"taste great\"
and ad B \"less bias\".

You decide to run an experiment by randomly showing site visitors one of the two
advertisements and tracking how many people click each one.

If there is a large difference between the ratio of clickers for A & B, then
it's an easy choice, but if there difference is not so obvious, then you can use
statistical inference.

Let's say N_A people see ad A, and n_A click it. We can think of each ad view as
a Bernoulli trial where p_A is the probability that someone clicks ad A. Then
(if N_A is large, which it is here) we know that n_A / N_A is approxiimately
a normal random variable with mean p_A and standard deviation
sigma = math.sqrt(p * (1 - p) / N_A)

Similarly, n_B / N_B is approximately a normal random variable with mean p_B and
standard deviation math.sqrt(p * (1 - p) / N_B)

If we assume those two normals are independent (which seems reasonable, since the
individual Bernoulli trials ought to be), then their difference should also be
normal with mean p_B - p_A and standard deviation
math.sqrt(sigma_A ** 2 + sigma_B ** 2)

*** this is sort of cheating. The math only works out like this if you know the
standard deviation. Here we're estimating them from the data, which means we
really should be using a t-distribution. But for large enough data sets, it's
close enough that it doesn't make much difference.

This means we can test the null hypothesis that p_A and p_B are the same
(that is, that p_B - p_A is zero), which should approximately be standard normal.

For example, if \"taste good\" gets 200 clicks out of 1000 views and \"less than\"
gets 180 clicks out of 1000 views, the statistic (difference) equals %s.

The probability of seeing such a large difference if the means were actually
equal would be %s, which is large enought that you cant conclude there is much
of a difference.

On the other hand, if \"less bias\" only got 150 clicks, we'd have a statistic
(difference) of %s with a p-value of %s, which means there's
only a %s probability you'd see such a large difference if the
ads were equally effective at creating clicks.
""" % (z_1, p_value_1, z_2, p_value_2, p_value_2)
print '-' * 100

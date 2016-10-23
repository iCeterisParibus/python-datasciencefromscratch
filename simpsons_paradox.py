# Python script to discuss Simposon's Paradox and other correlation caveats
# common to statstics and data science.

import math

def mean(x):
    return sum(x) / len(x)

def dot(v,w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
           for v_i, w_i in zip(v, w))

def sum_of_squares(x):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(x, x)

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

def covariance(x, y):
    n = len(x)
    return dot(dev_mean(x), dev_mean(y)) / (n-1)

def correlation(a, b):
    stdev_a = standard_deviation(a)
    stdev_b = standard_deviation(b)
    if stdev_a > 0 and stdev_b > 0:
        return covariance(a, b) / stdev_a / stdev_b
    else:
        return 0    # if no variation, correlation equals zero

x = [-2, -1, 0, 1, 2]
y = [2, 1, 0 , 1, 2]
z = [99.98, 99.99, 100.00, 100.01, 100.02]

print "Have you ever heard of Simpson's Paradox?"
heard_of = raw_input("(Y or N) >>> ")

if heard_of == "N":
    print "\nWould you like to learn about it?"
    review = raw_input("(Y or N) >>> ")
elif heard_of == "Y":
    print "\nWould you like a review?"
    review = raw_input("(Y or N) >>> ")
else:
    print "\nWe're gonna assume you meant to say No and would like to learn."
    review = "Y"

if review == "N":
    print "\nFine with me. Not like I spent all that time typing it up or anything."
else:
    print '-' * 100
    print """\nA not uncommon suprise when analyzing data is ~Simpson's Paradox~
in which correlations can be misleading when ~confounding variables~ are ignored.

The key issue is that correlation is measuring the relationship between to
variables ***all else being equal***

If your data classes are assigned at random, as they may be in a well designed
experiment, this might not be a terrible assumption. But this is not a fair
assumption when there is a deeper pattern to class assignment.

Only real way to avoid this is to know your data and make sure you check for
confounding factors.\n"""

print "\nAre you ready to get into the other correlation caveats?"
caveats = raw_input("(Y or N) >>> ")

if caveats == "N":
    print """\nWell there is nothing else in this script, and I took the time to
    \b\b\b\btype up so you're gonna have to deal with it."""
elif caveats == "Y":
    print "\nHere we go. Enjoy!"
elif caveats != "N" and caveats != "Y" and heard_of != "N" and heard_of != "Y":
    print "\nAgain, we're just going to assume you mean to say Yes!"
else:
    print "\nWe'll just assume you meant to say Heck yes!"

no_corr = correlation(x, y)

print '-' * 100
print """\nA correlation of zero indicates that there is no linear relationship
between two variables. So lets propose we have
two featurs (variables), x = %s and y = %s.

Now if we calculate the correlation of these two featurs:

    corr = covariance(x, y) / stdev(x) / stdev(y)

we get a value of correlation(x, y) = %d, or that there is no relationship
between x and y. But if we look closely, we can see that y_i = abs(x_i)
for every corresponding element.

This is definitely a relationship, but correlation
looks for a linear relationship between two features (varaibles).

What these two featurs have is a relationship such that knowing how x_i
compares to mean(x) gives us info about how y_i compares to mean(y);
that is the sort of relationship that correlation looks for.\n""" % (
    x, y, no_corr
)

perf_corr = correlation(x, z)

print '-' * 100
print """\nIn addition, correlation tells us nothing about how large the relationship is.
Take for example the two featurs x = %s and z = %s
which calculating the correlation of these two featurs will give you %d,
so they are perfectly correlated. However, with no information on the magnitude
of the relationship, this may not be a very interesting discovery.\n""" % (
    x, z, perf_corr
)

print '-' * 100
print "\nAnd as always, remember \"Correlation does not imply Causation\"\n"
print '-' * 100

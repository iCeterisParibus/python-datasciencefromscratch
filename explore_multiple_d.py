# script for looking at correlation matrix and scatterplot matrix of a greater
# than 2 but relatively small dimensional data set.

# *** Will not run as there is no actual data being passed within the script
# *** However, replacing all 'data' values with read-in data should result in
# *** a functional script producing the correlation and scatterplot matrices

import random
import matplotlib.pyplot as plt
import math

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

def correlation_matrix(data):
    """returns the num_columns x num_columns matrix whose (i,j)th entry is the
    correlation between columns i and j of data"""

    _, num_columns = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)

_, num_columns = shape(data)
fig, ax = plt.subplots(num_columns, num_columns)

for i in range(num_columns):
    for j in range(num_columns):

        # scatter column_j on x-axis and column_i on y-axis
        if i != j: ax[i][j].scatter(get_column(data, j), get_column(data, i))

        # unless i==j, in which case show series name
    else: ax[i][j].annotate("series "+str(i), (0.5, 0.5),
                            xycoords = 'axes fraction',
                            ha = "center", va = "center")

    # then hide axis labels except left and bottom charts
    if i < num_columns - 1: ax[i][j].xaxis.set_visible(False)
    if j > 0: ax[i][j].yaxis.set_visible(False)

# fix the bottom right and top left axis labels, which are wrong because their
# charts only have text in them
ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_xlim(ax[0][1].get_ylim())
plt.show()

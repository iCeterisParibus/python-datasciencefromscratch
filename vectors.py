# this is a script to include all of the functions defined as important for
# vector arithmetic in Data Science from Scratch

from __future__ import division
from functools import partial
import math

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements
    of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n + v_n"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

v = [1, 2]
w = [5, 4]
print "\nvector v: %s" % v
print "\nvector w: %s" % w

u_add = vector_add(v, w)
print "\naddition of vector v and w: %s" % u_add
u_subt = vector_subtract(v,w)
print "\nsubtraction of vector v and w: %s" % u_subt

u_sum = vector_sum([v, w])
print "\nsum of vector v and w: %s" % u_sum

v_scalar = scalar_multiply(2, v)
print "\nscalar multiplication of scalar 2 and vector v: %s" % v_scalar
w_scalar = scalar_multiply(2, w)
print "\nscalar multiplication of scalar 2 and vector w: %s" % w_scalar

u_mean = vector_mean([v, w])
print "\ncomponentwise mean of vector v and w: %s" % u_mean

v_dot_w = dot(v, w)
print "\ndot product of vector v and w: %s" % v_dot_w

v_ss = sum_of_squares(v)
print "\nsum of squares of vector v: %s" % v_ss
w_ss = sum_of_squares(w)
print "\nsum of squares of vector w: %s" % w_ss

v_magn = magnitude(v)
print "\nmagnitude of vector v: %s" % v_magn
w_magn = magnitude(w)
print "\nmagnitude of vector w: %s" % w_magn

u_sq_dist = squared_distance(v, w)
print "\nsquared distance of vector v and w: %s" % u_sq_dist

u_dist = distance(v, w)
print "\ndistance between vector v and w: %s" % u_dist

answer_dict = {"v + w": u_add,
               "v - w": u_subt,
               "sum(v, w)": u_sum,
               "v * 2": v_scalar,
               "mean(sum(v, w))": u_mean,
               "dot(v, w)": v_dot_w,
               "ss(v)": v_ss,
               "ss(w)": w_ss,
               "magn(v)": v_magn,
               "magn(w)": w_magn,
               "sq_dist(v, w)": u_sq_dist,
               "dist(v, w)": u_dist}

# would like to figure out how to get each item to be printed out one line at a time

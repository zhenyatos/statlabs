import numpy as np
import math

def median(values):
    n = len(values)
    if n % 2 == 0:
        return (values[int(n/2)] + values[int((n/2) - 1)]) / 2
    else:
        return values[int(n/2)]

def average(values):
    return (sum(values) / len(values))

def z_R(values):
    return (values[0] + values[len(values) - 1]) / 2

def quartile(values, p):
    return values[math.ceil(len(values) * p)]

def z_Q(values):
    return (quartile(values, 1/4) + quartile(values, 3/4)) / 2
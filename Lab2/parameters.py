import math
import numpy as np


def median(values):
    n = len(values)
    if n % 2 == 0:
        return (values[int(n / 2)] + values[int((n / 2) - 1)]) / 2
    else:
        return values[int(n / 2)]


def average(values):
    return sum(values) / len(values)


def z_R(values):
    return (values[0] + values[len(values) - 1]) / 2


def z_Q(values):
    return (np.quantile(values, 1 / 4) + np.quantile(values, 3 / 4)) / 2


def z_tr(values):
    n = len(values)
    r = math.ceil(n / 4)
    return sum(values[r:n-r-1]) / (n - 2 * r)


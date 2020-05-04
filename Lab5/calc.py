import Lab5
from Lab5 import texworks
from scipy import stats
import numpy as np
import math


def correct_digits(vrnc):
    return max(0, round(-math.log10(abs(vrnc))))


def quadrantr(samples):
    x = samples[:, 0]
    y = samples[:, 1]
    mx = np.mean(x)
    my = np.mean(y)

    x_l = samples[x < mx]
    x_r = samples[x >= mx]

    q1 = x_r[x_r[:, 1] >= my]
    q2 = x_l[x_l[:, 1] >= my]
    q3 = x_l[x_l[:, 1] < my]
    q4 = x_r[x_r[:, 1] < my]
    return (len(q1) + len(q3) - len(q2) - len(q4)) / len(samples)


sizes = [20, 60, 100]
n_times = 1000

for param in Lab5.params:
    f = open("..\Documentation\Lab5\\tables\\" + param['name'] + ".tex", 'w')
    tex = ""
    for size in sizes:
        tex += texworks.heading(size)
        pearson_values = np.zeros(n_times)
        spearman_values = np.zeros(n_times)
        quadrant_values = np.zeros(n_times)
        for k in range(0, n_times):
            samples = param['distr'].rvs(size=size)
            pearson_values[k], p = stats.pearsonr(samples[:, 0], samples[:, 1])
            spearman_values[k], p = stats.spearmanr(samples[:, 0], samples[:, 1])
            quadrant_values[k] = quadrantr(samples)

        pearson_var = np.var(pearson_values)
        spearman_var = np.var(spearman_values)
        quadrant_var = np.var(quadrant_values)
        pearson2_var = np.var(pearson_values ** 2)
        spearman2_var = np.var(spearman_values ** 2)
        quadrant2_var = np.var(quadrant_values ** 2)

        tex += texworks.values("$E(z)$",
                               [
                                   np.round(np.mean(pearson_values),
                                            correct_digits(pearson_var)),
                                   np.round(np.mean(spearman_values),
                                            correct_digits(spearman_var)),
                                   np.round(np.mean(quadrant_values),
                                            correct_digits(quadrant_var))
                               ])

        tex += texworks.values("$E(z^2)$",
                               [
                                   np.round(np.mean(pearson_values ** 2),
                                            correct_digits(pearson_var)),
                                   np.round(np.mean(spearman_values ** 2),
                                            correct_digits(spearman_var)),
                                   np.round(np.mean(quadrant_values ** 2),
                                            correct_digits(quadrant_var))
                               ])

        tex += texworks.values("$D(z)$",
                               [
                                   np.round(pearson_var, 6),
                                   np.round(spearman_var, 6),
                                   np.round(quadrant_var, 6)
                               ])
        tex += texworks.empty()

    tex = texworks.tabular(tex)
    print(tex, file=f)
    f.close()

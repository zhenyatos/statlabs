import Lab5
from scipy import stats
import numpy as np

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
    print(param['name'])
    for size in sizes:
        print("n =", size)
        pearson_values = np.zeros(n_times)
        spearman_values = np.zeros(n_times)
        quadrant_values = np.zeros(n_times)
        for k in range(0, n_times):
            samples = param['distr'].rvs(size=size)
            pearson_values[k], p = stats.pearsonr(samples[:, 0], samples[:, 1])
            spearman_values[k], p = stats.spearmanr(samples[:, 0], samples[:, 1])
            quadrant_values[k] = quadrantr(samples)
        print(" pearson:")
        print("  mean(X): ", np.mean(pearson_values))
        print("  mean(X^2): ", np.mean(pearson_values * pearson_values))
        print("  var(X):", np.var(pearson_values))
        print(" spearman:")
        print("  mean(X): ", np.mean(spearman_values))
        print("  mean(X^2): ", np.mean(spearman_values * spearman_values))
        print("  var(X):", np.var(spearman_values))
        print(" quadrant:")
        print("  mean(X): ", np.mean(quadrant_values))
        print("  mean(X^2): ", np.mean(quadrant_values * quadrant_values))
        print("  var(X): ", np.var(quadrant_values))

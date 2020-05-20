from scipy import stats
import numpy as np
import math


def chi_squared(x, distr, alpha):
    # calculating dimension of freedom of chi2
    N = len(x)
    k = math.ceil(1.72 * math.pow(N, 1 / 3))
    chisq = stats.chi2(df=k - 1)

    a = []
    center = distr.ppf(0.5)
    h = 2 * stats.iqr(x) / math.pow(N, 1 / 3)

    a.append(-np.inf)
    for i in range(0, k - 1):
        a.append(center + h * (i - ((k-1) / 2)))
    a.append(np.inf)

    # theoretical probabilities and counting
    p = np.zeros(k)
    n = np.zeros(k)
    for i in range(0, k):
        p[i] = distr.cdf(a[i+1]) - distr.cdf(a[i])
        y = x[a[i] < x]
        n[i] = len(y[y <= a[i+1]])

    chi2_1 = (1 / N) * \
           sum(np.square(n - N * p) / p)

    chi2_2 = chisq.ppf(1 - alpha)

    return {
        'result': chi2_1 < chi2_2,
        'chi2': np.round([chi2_1, chi2_2], 4),
        'a_val': np.round(a, 2),
        'p_val': np.round(p, 4),
        'n_val': n,
        'diff': np.round(n - N * p, 4)
    }
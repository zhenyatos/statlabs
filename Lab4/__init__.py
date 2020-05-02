import scipy.stats as stats
import math
import numpy as np

sizes = [20, 60, 100]

params = [
    {
        'name': "normal",
        'a': -4.0, 'b': 4.0,
        'stat': stats.norm(loc=0, scale=1),
        'pf': lambda x: stats.norm(loc=0, scale=1).pdf(x)
    },
    {
        'name': "cauchy",
        'a': -4.0, 'b': 4.0,
        'stat': stats.cauchy(loc=0, scale=1),
        'pf':  lambda x: stats.cauchy(loc=0, scale=1).pdf(x)
    },
    {
        'name': "laplace",
        'a': -4.0, 'b': 4.0,
        'stat': stats.laplace(loc=0, scale=1 / math.sqrt(2)),
        'pf':  lambda x: stats.laplace(loc=0, scale=1 / math.sqrt(2)).pdf(x)
    },
    {
        'name': "uniform",
        'a': -4.0, 'b': 4.0,
        'stat': stats.uniform(-math.sqrt(3), 2 * math.sqrt(3)),
        'pf': lambda x: stats.uniform(-math.sqrt(3), 2 * math.sqrt(3)).pdf(x)
    },
    {
        'name': "poisson",
        'a': 6, 'b': 14,
        'stat': stats.poisson(10),
        'pf': lambda x: stats.poisson(10).pmf(np.ceil(x))
    }
]

if __name__ == "__main__":
    exec(open("ecdf.py").read())
    exec(open("kde.py").read())
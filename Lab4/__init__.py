import scipy.stats as stats
import math

sizes = [20, 60, 100]

params = [
    {
        'name': "normal",
        'a': -4.0, 'b': 4.0,
        'stat': stats.norm(loc=0, scale=1)
    },
    {
        'name': "cauchy",
        'a': -4.0, 'b': 4.0,
        'stat': stats.cauchy(loc=0, scale=1)
    },
    {
        'name': "laplace",
        'a': -4.0, 'b': 4.0,
        'stat': stats.laplace(loc=0, scale=1 / math.sqrt(2))
    },
    {
        'name': "uniform",
        'a': -4.0, 'b': 4.0,
        'stat': stats.uniform(-math.sqrt(3), 2 * math.sqrt(3))
    },
    {
        'name': "poisson",
        'a': 6, 'b': 14,
        'stat': stats.poisson(10)
    }
]

if __name__ == "__main__":
    exec(open("ecdf.py").read())
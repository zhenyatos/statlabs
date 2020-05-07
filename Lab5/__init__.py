from scipy import stats
import numpy as np


def get_2d_normal(loc_x: float, loc_y: float, scale_x: float, scale_y: float, rho: float):
    if rho > 1 or rho < -1:
        return None
    cov_xy = rho * scale_x * scale_y
    disp_x = scale_x * scale_x
    disp_y = scale_y * scale_y
    return stats.multivariate_normal(mean=[loc_x, loc_y],
                                     cov=[[disp_x, cov_xy], [cov_xy, disp_y]])


class Mixed:
    # mixing distributions should be the same dimension
    def __init__(self, distrs, coeffs, dim):
        # normalization
        coeffs = np.array(coeffs)
        coeffs /= sum(coeffs)

        self.distrs = distrs
        self.coeffs = coeffs
        self.n = len(distrs)
        self.dim = dim

    def pdf(self, x):
        val = 0
        for k in range(0, self.n):
            val += self.distrs[k].pdf(x) * self.coeffs[k]
        return val

    def rvs(self, size):
        data = np.zeros((size, self.dim, self.n))
        for k, distr in enumerate(self.distrs):
            data[:, k] = distr.rvs(size=size)
        random_index = np.random.choice(np.arange(self.n), size=size, p=self.coeffs)
        sample = data[np.arange(size), random_index]
        return sample


params = [
    {
        'name': "rho = 0.0",
        'meanX': 0, 'meanY': 0,
        'sigmaX': 1, 'sigmaY': 1,
        'rho': 0,
        'distr': get_2d_normal(0, 0, 1, 1, 0)
    },
    {
        'name': "rho = 0.5",
        'meanX': 0, 'meanY': 0,
        'sigmaX': 1, 'sigmaY': 1,
        'rho': 0.5,
        'distr': get_2d_normal(0, 0, 1, 1, 0.5)
    },
    {
        'name': "rho = 0.9",
        'meanX': 0, 'meanY': 0,
        'sigmaX': 1, 'sigmaY': 1,
        'rho': 0.9,
        'distr': get_2d_normal(0, 0, 1, 1, 0.9)
    },
    {
        'name': "mix",
        'distr': Mixed([get_2d_normal(0, 0, 1, 1, 0.9),
                        get_2d_normal(0, 0, 10, 10, -0.9)],
                       [0.9, 0.1], 2)
    }
]

if __name__ == "__main__":
    exec(open("calc.py").read())
    exec(open("ellipse.py").read())

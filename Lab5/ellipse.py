import Lab5
import matplotlib.pyplot as plt
import numpy as np

class Ellipse:
    def __init__(self, mean_x, mean_y, sigma_x, sigma_y, rho):
        self.a = 1 / (sigma_x * sigma_x)
        self.b = 2 * rho / (sigma_x * sigma_y)
        self.c = 1 / (sigma_y * sigma_y)
        self.x0 = mean_x
        self.y0 = mean_y

    def rad2(self, samples):
        rads = self.z(samples[:, 0], samples[:, 1])
        return max(rads)

    def z(self, x, y):
        values = self.a * ((x - self.x0) ** 2) - \
                self.b * (x - self.x0) * (y - self.y0) + \
                self.c * ((y - self.y0) ** 2)
        return values


sizes = [20, 60, 100]

for param in Lab5.params:
    if param['name'] == "mix":
        continue

    ellipse = Ellipse(param['meanX'], param['meanY'],
                      param['sigmaX'], param['sigmaY'], param['rho'])
    for size in sizes:
        samples = param['distr'].rvs(size=size)
        plt.scatter(samples[:, 0], samples[:, 1])

        x = np.linspace(-4, 4, 100)
        y = np.linspace(-4, 4, 100)
        x, y = np.meshgrid(x, y)
        z = ellipse.z(x, y)
        plt.contour(x, y, z, [ellipse.rad2(samples)])

        plt.show()
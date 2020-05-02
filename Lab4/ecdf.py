import Lab4
import matplotlib.pyplot as plt
import numpy as np

class ECDF:
    data = []

    def __init__(self, data: np.ndarray):
        self.data = data
        self.eval_v = np.vectorize(self.eval)

    def eval(self, x: float):
        count = self.data[self.data < x]
        return count.size / self.data.size


np.random.seed(1)
n_plots = len(Lab4.sizes)
for param in Lab4.params:
    plt.subplots(n_plots)
    for k in range(0, n_plots):
        plt.subplot(1, n_plots, k + 1)
        plt.xlim(param['a'], param['b'])
        plt.xlabel('x')
        plt.ylabel('ecdf')

        sample = param['stat'].rvs(size=Lab4.sizes[k])
        ecdf = ECDF(sample)
        x = np.linspace(param['a'], param['b'])
        y = ecdf.eval_v(x)
        y_cdf = param['stat'].cdf(x)

        plt.plot(x, y, color='royalblue')
        plt.plot(x, y_cdf, color='blue')
        plt.title('n = ' + str(Lab4.sizes[k]))
    plt.tight_layout(pad=1.0)
    plt.savefig("..\Documentation\Lab4\ecdf\\" + param['name'] + ".png")

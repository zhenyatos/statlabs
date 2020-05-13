import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

def quadrantr(x, y):
    mx = np.median(x)
    my = np.median(y)

    return np.mean(np.sign(x - mx) * np.sign(y - my))


def lstmod(x, y):
    b = quadrantr(x, y) * stats.iqr(y) / stats.iqr(x)
    a = np.median(y) - b * np.median(x)
    return a, b

# experiment parameters
bounds = [-1.8, 2]
n_points = 20
coeffs = [2, 2]


if __name__ == "__main__":
    x = np.linspace(bounds[0], bounds[1], n_points)
    y0 = coeffs[0] + coeffs[1] * x              # model y
    y1 = y0 + stats.norm(0, 1).rvs(n_points)  # real y (without outliers)
    y2 = np.copy(y1)
    y2[0] += 10
    y2[n_points-1] -= 10

    data = [
        {
            'name': "simple",
            'y': y1
        },
        {
            'name': "robust",
            'y': y2
        }
    ]

    for d in data:
        y = d['y']
        lstsq_b, lstsq_a = stats.linregress(x, y)[0:2]
        lstmod_a, lstmod_b = lstmod(x, y)
        print(d['name'])
        print("lstsqr:", "a =", round(lstsq_a, 2),
              "b =", round(lstsq_b, 2),
              "diff =", np.sum(np.square(y0 - (lstsq_a + lstsq_b * x))))
        print("lstmod:", "a =", round(lstmod_a, 2),
              "b =", round(lstmod_b, 2),
              "diff =", np.sum(np.square(y0 - (lstmod_a + lstmod_b * x))))
        print(" ")

        plt.plot(x, y0, 'navy', label="Модель")
        plt.plot(x, lstsq_a + lstsq_b * x, 'orange', label="МНК")
        plt.plot(x, lstmod_a + lstmod_b * x, 'indigo', label="МНМ")
        plt.scatter(x,y, facecolors='none', edgecolors='black',zorder=100, label="Выборка")
        plt.legend()
        plt.savefig("..\Documentation\Lab6\\" + d['name'] + ".png")
        plt.close()


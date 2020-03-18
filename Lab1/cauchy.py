import math
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

# experiment PARAMETERS
sizes = [10, 50, 1000]
n_plots = len(sizes)
n_points = 100
seed = 102

# distribution PARAMETERS
x0 = 0
hamma = 1
np.random.seed(seed)

# left and right borders was determined
# experimentally, so TODO: add mutable l-r_borders
b_border = 0
t_border = 1.5 / (math.pi * hamma)

# generating plots TODO: Add tile using LaTeX
plt.subplots(n_plots)

for i in range(0, n_plots):
    # generation values
    values_rnd = st.cauchy.rvs(loc=x0, scale=hamma, size=sizes[i])

    l_border = min(values_rnd)
    r_border = max(values_rnd)
    x_pdf = np.linspace(l_border, r_border, n_points)
    y_pdf = st.cauchy.pdf(x_pdf, loc=x0, scale=hamma)

    n_bins = math.ceil(math.sqrt(sizes[i]))
    width = (r_border - l_border) / n_bins
    plt.subplot(1, n_plots, i+1)

    plt.xlim(l_border, r_border)
    plt.ylim(b_border, t_border)
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.title('n = ' + str(sizes[i]))
    plt.grid()

    plt.plot(x_pdf, y_pdf, color='royalblue')
    bins_rnd = np.arange(min(values_rnd), max(values_rnd) + width, width)
    plt.hist(x=values_rnd, bins=bins_rnd, color='lightsteelblue', density=True)

plt.savefig("..\Documentation\Lab1\cauchy.png")
plt.show()
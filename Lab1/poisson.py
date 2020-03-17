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
lambda_ = 10
np.random.seed(seed)

# poisson distribution is approximating normal distribution
# so border calculations are sort of the same
l_border = 0
r_border = 3 * lambda_
b_border = 0
t_border = 2 / math.sqrt(2 * math.pi * lambda_)

# as a discrete distribution...
x_dots = np.arange(0, r_border, 1)
y_dots = st.poisson.pmf(x_dots, lambda_)

# generating plots TODO: Add tile using LaTeX
plt.subplots(n_plots)

for i in range(0, n_plots):
    n_bins = math.ceil(math.sqrt(sizes[i]))
    width = (r_border - l_border) / n_bins
    plt.subplot(1, n_plots, i+1)

    plt.xlim(l_border, r_border)
    plt.ylim(b_border, t_border)
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.title('n = ' + str(sizes[i]))
    plt.grid()

    plt.plot(x_dots, y_dots, color='royalblue', marker='o')
    values_rnd = st.poisson.rvs(lambda_, size=sizes[i])
    bins_rnd = np.arange(0, max(values_rnd), 1) # step is fixed because distribution is discrete
    plt.hist(x=values_rnd, bins=bins_rnd, color='lightsteelblue', density=True)

plt.savefig("..\Documentation\Lab1\poisson.png")
plt.show()
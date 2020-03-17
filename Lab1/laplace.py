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
alpha = 1 / math.sqrt(2)
beta = 0
np.random.seed(seed)

# left and right borders are calculated to satisfy:
# pdf(x) <= 0.1, when x > r_border or x < l_border
delta = -math.log(0.2 / alpha) / alpha
l_border = beta - delta
r_border = beta + delta
b_border = 0
t_border = alpha

# pdf plot points
x_pdf = np.linspace(l_border, r_border, n_points)
y_pdf = st.laplace.pdf(x_pdf, loc=beta, scale=alpha)

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

    plt.plot(x_pdf, y_pdf, color='royalblue')
    values_rnd = st.laplace.rvs(loc=beta, scale=alpha, size=sizes[i])
    print(str(min(values_rnd)) + ' ' + str(max(values_rnd)))
    bins_rnd = np.arange(min(values_rnd), max(values_rnd) + width, width)
    plt.hist(x=values_rnd, bins=bins_rnd, color='lightsteelblue', density=True)

plt.savefig("..\Documentation\Lab1\laplace.png")
plt.show()
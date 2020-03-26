import math
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import Lab2.parameters as param

# experiment PARAMETERS
sizes = [10, 100, 1000]
n_tests = len(sizes)
n_calc = 1000

# distribution PARAMETERS
mu = 0
sigma = 1

print("Normal distribution")
print("")
for i in range(0, n_tests):
    median_data = np.zeros(n_calc)
    average_data = np.zeros(n_calc)
    z_Q_data = np.zeros(n_calc)

    for j in range(0, n_calc):
        values = st.norm.rvs(mu, sigma, size=sizes[i])
        values = np.sort(values)
        median_data[j] = param.median(values)
        average_data[j] = param.average(values)
        z_Q_data[j] = param.z_Q(values)
    print("With " + str(sizes[i]) + ":")
    print("median: " + str(param.average(median_data)))
    print("average: " + str(param.average(average_data)))
    print("zQ: " + str(param.average(z_Q_data)))
    print("")
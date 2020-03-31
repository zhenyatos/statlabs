import math
import numpy as np
import scipy.stats as st
import Lab2.parameters as param

# experiment PARAMETERS
sizes = [10, 100, 1000]
n_tests = len(sizes)
n_calc = 1000
n_digits = 6
file = open('table.txt', 'w')

# distribution PARAMETERS
distrs = ["Normal", "Cauchy", "Laplace", "Poisson", "Uniform"]
n_distr = len(distrs)
# normal
N_mu = 0
N_sigma = 1
# laplace
L_alpha = 1 / math.sqrt(2)
L_beta = 0
# cauchy
C_x0 = 0
C_hamma = 1
# poisson
P_lambda = 10
# uniform
U_a = -math.sqrt(3)
U_b = math.sqrt(3)


def gen_values(distr_name, size):
    if distr_name == "Normal":
        return st.norm.rvs(N_mu, N_sigma, size=size)
    if distr_name == "Cauchy":
        return st.cauchy.rvs(loc=C_x0, scale=C_hamma, size=size)
    if distr_name == "Laplace":
        return st.laplace.rvs(loc=L_beta, scale=L_alpha, size=size)
    if distr_name == "Uniform":
        return st.uniform.rvs(U_a, U_b - U_a, size=size)
    if distr_name == "Poisson":
        return st.poisson.rvs(P_lambda, size=size)
    return None


average_data = np.zeros(n_calc)
median_data = np.zeros(n_calc)
z_R_data = np.zeros(n_calc)
z_Q_data = np.zeros(n_calc)
z_tr_data = np.zeros(n_calc)

for k in range(0, n_distr):
    print(distrs[k] + ":", file=file)
    print("", file=file)
    for i in range(0, n_tests):
        for j in range(0, n_calc):
            values = gen_values(distrs[k], sizes[i])
            values = np.sort(values)

            average_data[j] = param.average(values)
            median_data[j] = param.median(values)
            z_R_data[j] = param.z_R(values)
            z_Q_data[j] = param.z_Q(values)
            z_tr_data[j] = param.z_tr(values)

        # generating LaTeX table code
        S = "$n=" + str(sizes[i]) + "$&&&&&" + " \\\ \hline"
        S += "$E(z)$" + "&" + str(round(param.average(average_data), 6)) +\
            "&" + str(round(param.average(median_data), 6)) +\
            "&" + str(round(param.average(z_R_data), 6)) +\
            "&" + str(round(param.average(z_Q_data), 6)) +\
            "&" + str(round(param.average(z_tr_data), 6)) +\
            " \\\ \hline"
        S += "$D(z)$" + "&" + str(round(param.variance(average_data), 6)) +\
            "&" + str(round(param.variance(median_data), 6)) +\
            "&" + str(round(param.variance(z_R_data), 6)) +\
            "&" + str(round(param.variance(z_Q_data), 6)) +\
            "&" + str(round(param.variance(z_tr_data), 6)) + \
            " \\\ \hline"
        print(S, file=file)
        print("", file=file)

file.close()
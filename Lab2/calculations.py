import math
import numpy as np
import scipy.stats as st
import Lab2.parameters as param

# experiment PARAMETERS
sizes = [10, 100, 1000]
n_tests = len(sizes)
n_calc = 1000

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
    print(distrs[k] + ":")
    print("")
    for i in range(0, n_tests):
        for j in range(0, n_calc):
            values = gen_values(distrs[k], sizes[i])
            values = np.sort(values)

            average_data[j] = param.average(values)
            median_data[j] = param.median(values)
            z_R_data[j] = param.median(values)
            z_Q_data[j] = param.z_Q(values)
            z_tr_data[j] = param.z_tr(values)

        print("With " + str(sizes[i]) + ":")
        print("average: " + str(param.average(average_data)))
        print("median: " + str(param.average(median_data)))
        print("zR: " + str(param.average(z_R_data)))
        print("zQ: " + str(param.average(z_Q_data)))
        print("ztr: " + str(param.average(z_tr_data)))
        print("")
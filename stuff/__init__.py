import math
import scipy.stats as st

# distribution PARAMETERS
distrs = ["normal", "cauchy", "laplace", "poisson", "uniform"]
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
    if distr_name == "normal":
        return st.norm.rvs(N_mu, N_sigma, size=size)
    if distr_name == "cauchy":
        return st.cauchy.rvs(loc=C_x0, scale=C_hamma, size=size)
    if distr_name == "laplace":
        return st.laplace.rvs(loc=L_beta, scale=L_alpha, size=size)
    if distr_name == "uniform":
        return st.uniform.rvs(U_a, U_b - U_a, size=size)
    if distr_name == "poisson":
        return st.poisson.rvs(P_lambda, size=size)
    return None
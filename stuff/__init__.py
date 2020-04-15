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


def tested_distr(distr_name):
    if distr_name == "normal":
        return st.norm(N_mu, N_sigma)
    if distr_name == "cauchy":
        return st.cauchy(loc=C_x0, scale=C_hamma)
    if distr_name == "laplace":
        return st.laplace(loc=L_beta, scale=L_alpha)
    if distr_name == "uniform":
        return st.uniform(U_a, U_b - U_a)
    if distr_name == "poisson":
        return st.poisson(P_lambda)
    return None
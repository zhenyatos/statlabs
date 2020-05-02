import math
import scipy.stats as st

# distribution PARAMETERS
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

distrs = [
    {
        'name': "normal",
        'stat': st.norm(N_mu, N_sigma)
    },
    {
        'name': "cauchy",
        'stat': st.cauchy(loc=C_x0, scale=C_hamma)
    },
    {
        'name': "laplace",
        'stat': st.laplace(loc=L_beta, scale=L_alpha)
    },
    {
        'name': "uniform",
        'stat': st.uniform(U_a, U_b - U_a)
    },
    {
        'name': "poisson",
        'stat': st.poisson(P_lambda)
    }
]
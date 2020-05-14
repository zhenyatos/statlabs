from scipy import stats
from Lab7 import criteria

if __name__ == "__main__":
    alpha = 0.05
    distr = stats.norm(0, 1)
    x = distr.rvs(100)

    loc, scale = stats.norm.fit(x)
    print("loc =", loc, "\nscale =", scale, "\n")

    # actually you only need to check N(loc, scale)
    test_distrs = [
        {
            'name': "N(0,1)",
            'distr': distr
        },
        {
            'name': "N(loc, scale)",
            'distr': stats.norm(loc, scale)
        },
        {
            'name': "N(0.5, 1)",
            'distr': stats.norm(0.5, 1)
        },
        {
            'name': "C(0, 1)",
            'distr': stats.cauchy(0, 1)
        }
    ]

    for test in test_distrs:
        res = criteria.chi_squared(x, test['distr'], alpha)
        print(test['name'] + ":")
        print("result:", res['result'])
        if test['name'] == "N(loc, scale)":
            print("Chi's:", res['chi2'])
            print("a_i:", res['a_val'])
            print("p_i:", res['p_val'])
            print("n_i:", res['n_val'])
            print("(n_i - np_i):", res['diff'])
            print("0:", sum(res['diff']))
        print("\n")




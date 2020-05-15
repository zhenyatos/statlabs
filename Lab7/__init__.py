from scipy import stats
from Lab7 import criteria

if __name__ == "__main__":
    alpha = 0.3

    # actually you only need to check N(loc, scale)
    test_distrs = [
        {
            'name': "N(0, 1) ? N(loc, scale)",
            'distr': stats.norm,
            'data': stats.norm(0, 1).rvs(100)
        },
        {
            'name': "U(-1, 1) ? N(loc, scale)",
            'distr': stats.norm,
            'data': stats.uniform(-1, 2).rvs(20)
        }
    ]

    for test in test_distrs:
        loc, scale = stats.norm.fit(test['data'])
        distr = stats.norm(loc, scale)
        print("loc =", loc, "\nscale =", scale, "\n")
        res = criteria.chi_squared(test['data'], distr, alpha)
        print(test['name'] + ":")
        print("result:", res['result'])
        if test['name'] == "N(0, 1) ? N(loc, scale)":
            print("Chi's:", res['chi2'])
            print("a_i:", res['a_val'])
            print("p_i:", res['p_val'])
            print("n_i:", res['n_val'])
            print("(n_i - np_i):", res['diff'])
            print("0:", sum(res['diff']))
        print("\n")



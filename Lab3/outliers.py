import stuff as sf
import numpy as np

# experiment PARAMETERS
sizes = [20, 100]
n_tests = len(sizes)
n_calc = 1000
whis = 1.5
n_digits = 3

for k in range(0, sf.n_distr):
    for j in range(0, n_tests):
        n_outliers = 0
        for i in range(0, n_calc):
            values = sf.gen_values(sf.distrs[k], sizes[j])
            # calculating borders as LQ - whis * IQR, UQ + whis * IQR
            lq = np.quantile(values, 0.25)
            uq = np.quantile(values, 0.75)
            iqr = uq - lq
            l = lq - whis * iqr
            r = uq + whis * iqr
            # test data for outliers
            for m in range(0, sizes[j]):
                if values[m] < l or values[m] > r:
                    n_outliers += 1
        prob = n_outliers / (n_calc * sizes[j])  # outliers frequency
        print(sf.distrs[k] + ", n=" + str(sizes[j]) + " : " + str(round(prob, n_digits)))
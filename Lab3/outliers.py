import stuff as sf
import numpy as np
import scipy.stats as st

# experiment PARAMETERS
sizes = [20, 100]
n_tests = len(sizes)
n_calc = 1000
whis = 1.5
n_digits = 6
eps = 0.0000001

for k in range(0, sf.n_distr):
    for j in range(0, n_tests):
        outliers = np.zeros(n_calc)
        for i in range(0, n_calc):
            values = sf.tested_distr(sf.distrs[k]).rvs(size=sizes[j])
            # calculating borders as LQ - whis * IQR, UQ + whis * IQR
            lq = np.quantile(values, 0.25)
            uq = np.quantile(values, 0.75)
            iqr = uq - lq
            l = lq - whis * iqr
            r = uq + whis * iqr
            # test data for outliers
            for m in range(0, sizes[j]):
                if values[m] < l or values[m] > r:
                    outliers[i] += 1
        outliers /= sizes[j]
        prob = sum(outliers) / n_calc  # outliers frequency
        disp = (1 / n_calc) * (sum(outliers * outliers)) - prob * prob
        print(sf.distrs[k] + ", n=" + str(sizes[j]) + " :")
        print("P = " + str(round(prob, n_digits)))
        print("D = " + str(round(disp, n_digits)))

print("")

# theoretical outlier probabilities
print("")
print("Theoretical:")
for k in range(0, sf.n_distr):
    distr = sf.tested_distr(sf.distrs[k])
    X1 = distr.ppf(1/4) - (3/2) * (distr.ppf(3/4) - distr.ppf(1/4))
    X2 = distr.ppf(3/4) + (3/2) * (distr.ppf(3/4) - distr.ppf(1/4))
    P = distr.cdf(X1) - (distr.cdf(X1+eps) - distr.cdf(X1-eps)) + (1 - distr.cdf(X2))
    print(sf.distrs[k] + ": " + str(P))
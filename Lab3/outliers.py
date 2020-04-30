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

for distr in sf.distrs:
    for j in range(0, n_tests):
        outliers = np.zeros(n_calc)
        for i in range(0, n_calc):
            values = distr['stat'].rvs(size=sizes[j])
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
        print(distr['name'] + ", n=" + str(sizes[j]) + " :")
        print("P = " + str(round(prob, n_digits)))
        print("D = " + str(round(disp, n_digits)))

print("")

# theoretical outlier probabilities
print("")
print("Theoretical:")
for distr in sf.distrs:
    stat = distr['stat']
    X1 = stat.ppf(1/4) - (3/2) * (stat.ppf(3/4) - stat.ppf(1/4))
    X2 = stat.ppf(3/4) + (3/2) * (stat.ppf(3/4) - stat.ppf(1/4))
    P = stat.cdf(X1) - (stat.cdf(X1+eps) - stat.cdf(X1-eps)) + (1 - stat.cdf(X2))
    print(distr['name'] + ": " + str(P))
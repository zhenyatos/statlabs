import numpy as np
import Lab2.parameters as param
import stuff as sf

# experiment PARAMETERS
sizes = [10, 100, 1000]
n_tests = len(sizes)
n_calc = 1000
n_digits = 6
file = open('table.txt', 'w')

# variables initialization
average_data = np.zeros(n_calc)
median_data = np.zeros(n_calc)
z_R_data = np.zeros(n_calc)
z_Q_data = np.zeros(n_calc)
z_tr_data = np.zeros(n_calc)

for k in range(0, sf.n_distr):
    print(sf.distrs[k] + ":", file=file)
    print("", file=file)
    for i in range(0, n_tests):
        for j in range(0, n_calc):
            values = sf.gen_values(sf.distrs[k], sizes[i])
            values = np.sort(values)

            average_data[j] = param.average(values)
            median_data[j] = param.median(values)
            z_R_data[j] = param.z_R(values)
            z_Q_data[j] = param.z_Q(values)
            z_tr_data[j] = param.z_tr(values)

        # generating LaTeX table code
        vrnc_average = param.variance(average_data)
        vrnc_median = param.variance(median_data)
        vrnc_z_R = param.variance(z_R_data)
        vrnc_z_Q = param.variance(z_Q_data)
        vrnc_z_tr = param.variance(z_tr_data)
        S = "$n=" + str(sizes[i]) + "$&&&&&" + " \\\ \hline"
        S += "$E(z)$" + "&" + str(round(param.average(average_data), param.correct_digits(vrnc_average))) +\
            "&" + str(round(param.average(median_data), param.correct_digits(vrnc_average))) +\
            "&" + str(round(param.average(z_R_data), param.correct_digits(vrnc_z_R))) +\
            "&" + str(round(param.average(z_Q_data), param.correct_digits(vrnc_z_Q))) +\
            "&" + str(round(param.average(z_tr_data), param.correct_digits(vrnc_z_tr))) +\
            " \\\ \hline"
        S += "$D(z)$" + "&" + str(round(vrnc_average, n_digits)) +\
            "&" + str(round(vrnc_median, n_digits)) +\
            "&" + str(round(vrnc_z_R, n_digits)) +\
            "&" + str(round(vrnc_z_Q, n_digits)) +\
            "&" + str(round(vrnc_z_tr, n_digits)) + \
            " \\\ \hline"
        print(S, file=file)
        print("", file=file)

file.close()
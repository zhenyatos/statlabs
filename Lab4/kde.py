import Lab4
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import scipy.stats as st
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

n_plots = len(Lab4.sizes)
h_scale = [0.5, 1, 2]
str_h_scale = [r"$h = h_n / 2$", r"$h = h_n$", r"$h = 2h_n$"]
str_n = r"$n = $"

np.random.seed(1)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
for param in Lab4.params:
    figure, axes = plt.subplots(nrows=n_plots, ncols=len(h_scale), sharex=True, sharey=True, figsize = (8,8))
    samples = []
    for k in range(0, n_plots):
        samples.append(param['stat'].rvs(size=Lab4.sizes[k]))

    k = 0
    for row in axes:
        i = 0
        for col in row:
            kde = st.gaussian_kde(samples[i], bw_method='silverman')
            col.set_xlim(param['a'], param['b'])
            col.set_xlabel('x')
            col.set_ylabel('kde')

            x = np.linspace(param['a'], param['b'])
            y_pdf = param['pf'](x)
            kde.set_bandwidth(bw_method=kde.factor * h_scale[k])
            y_kde = kde.evaluate(x)

            col.plot(x, y_kde, color='royalblue')
            col.plot(x, y_pdf, color='blue')
            col.set_title(str_n + str(Lab4.sizes[i]) + ", " + str_h_scale[k])
            i = i + 1
        k = k + 1
    figure.tight_layout(pad=1.0)
    figure.savefig("..\Documentation\Lab4\kde\\" + param['name'] + ".png")
import stuff as sf
import matplotlib.pyplot as plt

# experiment PARAMETERS
sizes = [20, 100]
n_tests = len(sizes)

values = []
for k in range(0, sf.n_distr):
    for i in range(0, n_tests):
        # generation values
        values.append(sf.gen_values(sf.distrs[k], sizes[i]))

    fig, ax = plt.subplots()
    plt.grid(axis='x')
    ax.boxplot(values, vert=False, medianprops=dict(color='b'), labels=["n=20", "n=100"])
    plt.savefig("..\Documentation\Lab3\\" + sf.distrs[k] + ".png")
    plt.show()
    values.clear()

import stuff as sf
import matplotlib.pyplot as plt

# experiment PARAMETERS
sizes = [20, 100]
n_tests = len(sizes)

values = []
for distr in sf.distrs:
    for i in range(0, n_tests):
        # generation values
        values.append(distr['stat'].rvs(size=sizes[i]))

    fig, ax = plt.subplots()
    plt.grid(axis='x')
    ax.boxplot(values, vert=False, medianprops=dict(color='b'), labels=["n=20", "n=100"])
    plt.savefig("..\Documentation\Lab3\\" + distr['name'] + ".png")
    plt.show()
    values.clear()

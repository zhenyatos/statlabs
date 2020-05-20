from Lab8 import estimations
from scipy import stats

sizes = [20, 100]

if __name__ == "__main__":
    for size in sizes:
        print("For " + str(size) + ":")
        samples = stats.norm(0, 1).rvs(size=size)
        print("mle:")
        m, s = estimations.interval_mle(samples, 0.05)
        print("m in", m)
        print("s in", s)
        print("asympth:")
        m, s = estimations.interval_asympt(samples, 0.05)
        print("m in", m)
        print("s in", s)
        print("")
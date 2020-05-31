from Coursework import read
from Coursework import video
from Coursework import estimations
from matplotlib import pyplot as plt
import numpy as np

mat_file = "37000_SPD16x16.mat"
interval = [161.0, 162.0]
path = "video/"
ext = ".png"


def generate_images(data, vel, start, stop):
    for i in range(start, stop-1):
        temp = data[:, :, i]
        plt.imshow(temp, interpolation='nearest')
        plt.title("t = " + str(round(interval[0] + (i - start) * dt, 3)) + "ms\n" + \
                  "v = " + str(round(vel[i - start], 2)))
        center = estimations.center(temp)
        plt.scatter(center[0], center[1], c='red')
        plt.savefig(path + str(i - start) + ext)
        plt.close()


if __name__ == "__main__":
    file, data, size = read.read_file(mat_file)
    indx, t1, t2, dt = read.extract_timing(file, data, interval)

    points = estimations.center_points(data, indx.start, indx.stop)
    samples = estimations.speed_samples(points, dt)

    generate_images(data, samples, indx.start, indx.stop)
    video.generate_video(path, ext)

    print("E(v) =", np.mean(samples))
    print("D(v) =", np.var(samples))

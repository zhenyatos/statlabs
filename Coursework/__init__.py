from Coursework import read
from Coursework import video
from Coursework import estimations
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

mat_file = "37000_SPD16x16.mat"
interval = [161.0, 162.0]
path = "video/"
ext = ".png"


def generate_images(data, start, stop):
    for i in range(start, stop):
        temp = data[:, :, i]
        plt.imshow(temp, interpolation='nearest')
        plt.title("t = " + str(round(interval[0] + (i - indx.start) * dt, 3)) + "ms")
        center = estimations.center(temp)
        plt.scatter(center[0], center[1], c='red')
        plt.savefig(path + str(i - indx.start) + ext)
        plt.close()


if __name__ == "__main__":
    file, data, size = read.read_file(mat_file)
    indx, t1, t2, dt = read.extract_timing(file, data, interval)

    generate_images(data, indx.start, indx.stop)
    video.generate_video(path, ext)

    points = estimations.center_points(data, indx.start, indx.stop)
    samples = estimations.speed_samples(points, dt)
    print(np.mean(samples))

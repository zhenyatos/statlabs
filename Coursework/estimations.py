import numpy as np


def center(matrix):
    x = 0
    y = 0
    med = np.mean(matrix)
    for i in range(0, 16):
        for j in range(0, 16):
            if matrix[i][j] >= 1.5 * med:
                x += matrix[i][j] * j
                y += matrix[i][j] * i
    x /= np.sum(matrix[matrix >= 1.5 * med])
    y /= np.sum(matrix[matrix >= 1.5 * med])
    return x, y


def center_points(data, start, stop):
    points = []
    for i in range(start, stop):
        points.append(center(data[:, :, i]))
    return np.array(points)


def speed(p1, p2, dt):
    return np.linalg.norm(p1 - p2) / dt


def speed_samples(points, dt):
    samples = []
    for i in range(0, len(points)-1):
        samples.append(speed(points[i], points[i+1], dt))
    return samples
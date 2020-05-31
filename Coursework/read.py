from scipy import io
import numpy as np


def read_file(mat_file):
    file = io.loadmat(mat_file)
    data = np.rot90(file.get("sign_bb"), 2)
    size = data.shape
    return file, data, size


def extract_timing(file, data, interval):
    info = file.get("Data")

    dt = info[0][1][0][0] * 1.0e-3
    t_begin = info[1][1][0][0]
    t_end = t_begin + data.shape[2] * dt

    indx_begin = int((interval[0] - t_begin) / dt)
    indx_end = int((interval[1] - t_begin) / dt)
    indx = slice(indx_begin, indx_end, 1)

    return indx, t_begin, t_end, dt
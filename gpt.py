import numpy as np


def calculate(list):
    if (len(list) != 9):
        raise ValueError("list must contain nine numbers")

    numpy_array = np.array(list).reshape(3, 3)
    print(numpy_array)

    numpy_array_mean = (np.mean(numpy_array, axis=0), np.mean(numpy_array, axis=1), np.mean(numpy_array))

    numpy_array_var = (np.var(numpy_array, axis=0), np.var(numpy_array, axis=1), np.var(numpy_array))

    numpy_array_std = (np.std(numpy_array, axis=0), np.std(numpy_array, axis=1), np.std(numpy_array))

    numpy_array_max = (np.max(numpy_array, axis=0), np.max(numpy_array, axis=1), np.max(numpy_array))

    numpy_array_min = (np.min(numpy_array, axis=0), np.min(numpy_array, axis=1), np.min(numpy_array))

    numpy_array_sum = (np.sum(numpy_array, axis=0), np.sum(numpy_array, axis=1), np.sum(numpy_array))

    outcome = {
        'mean': numpy_array_mean.tolist(),
        'variance': numpy_array_var.tolist(),
        'standard deviation': numpy_array_std.tolist(),
        'max': numpy_array_max.tolist(),
        'min': numpy_array_min.tolist(),
        'sum': numpy_array_sum.tolist()
    }

    return calculate
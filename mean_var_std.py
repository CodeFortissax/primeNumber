import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    numpy_array = np.array(input_list).reshape(3, 3)

    numpy_array_mean = [np.mean(numpy_array, axis=0).tolist(), np.mean(numpy_array, axis=1).tolist(), np.mean(numpy_array).tolist()]

    numpy_array_var = [np.var(numpy_array, axis=0).tolist(), np.var(numpy_array, axis=1).tolist(), np.var(numpy_array).tolist()]

    numpy_array_std = [np.std(numpy_array, axis=0).tolist(), np.std(numpy_array, axis=1).tolist(), np.std(numpy_array).tolist()]

    numpy_array_max = [np.max(numpy_array, axis=0).tolist(), np.max(numpy_array, axis=1).tolist(), np.max(numpy_array).tolist()]

    numpy_array_min = [np.min(numpy_array, axis=0).tolist(), np.min(numpy_array, axis=1).tolist(), np.min(numpy_array).tolist()]

    numpy_array_sum = [np.sum(numpy_array, axis=0).tolist(), np.sum(numpy_array, axis=1).tolist(), np.sum(numpy_array).tolist()]

    outcome = {
        'mean': numpy_array_mean,
        'variance': numpy_array_var,
        'standard deviation': numpy_array_std,
        'max': numpy_array_max,
        'min': numpy_array_min,
        'sum': numpy_array_sum
    }

    return outcome
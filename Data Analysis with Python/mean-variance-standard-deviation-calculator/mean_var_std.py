import numpy as np


def calculate(list):
    array = np.array(list)
    try:
        matrix = array.reshape((3, 3))
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    else:
        mean = [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(array).tolist()
        ]

        variance = [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(array).tolist()
        ]

        standard_deviation = [(np.array(v)**0.5).tolist() for v in variance]

        maxi = [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(array).tolist()
        ]

        mini = [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(array).tolist()
        ]

        s = [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(array).tolist()
        ]

        calculations = {
            "mean": mean,
            "variance": variance,
            "standard deviation": standard_deviation,
            "max": maxi,
            "min": mini,
            "sum": s
        }
        return calculations

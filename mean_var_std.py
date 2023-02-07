import numpy as np


def calculate(list):
    if len(list) == 9:
        converted = np.array(list).reshape(3, 3)
        calculations = {
            "mean": [np.mean(converted, axis=0).tolist(), np.mean(converted, axis=1).tolist(), np.mean(converted)],
            "variance": [np.var(converted, axis=0).tolist(), np.var(converted, axis=1).tolist(), np.var(converted)],
            "standard deviation": [np.std(converted, axis=0).tolist(), np.std(converted, axis=1).tolist(),
                                   np.std(converted)],
            "max": [np.max(converted, axis=0).tolist(), np.max(converted, axis=1).tolist(), np.max(converted)],
            "min": [np.min(converted, axis=0).tolist(), np.min(converted, axis=1).tolist(), np.min(converted)],
            "sum": [np.sum(converted, axis=0).tolist(), np.sum(converted, axis=1).tolist(), np.sum(converted)],
        }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")

import numpy as np


def euclidian_distance(v1, v2):
    return sum((x - y) ** 2 for x, y in zip(v1, v2)) ** 0.5


x = np.array([0, 0, 0])
y = np.array([3, 3, 3])

print(euclidian_distance(x, y))

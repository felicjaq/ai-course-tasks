import numpy as np


def sqr_euclidian_distance(v1, v2):
    return sum((x - y) ** 2 for x, y in zip(v1, v2))


def weighted_euclidian_distance(v1, v2, w):
    return sum((x - y) ** 2 * s for x, y, s in zip(v1, v2, w)) ** 0.5


def manhattan_distance(v1, v2):
    return sum(abs(x - y) for x, y in zip(v1, v2))


def chebbyshev_distance(v1, v2):
    return max(abs(x - y) for x, y in zip(v1, v2))


x = np.array([0, 0, 0])
y = np.array([3, 3, 3])
w = np.array([0, 0, 1])

print(sqr_euclidian_distance(x, y))
print(weighted_euclidian_distance(x, y, w))
print(manhattan_distance(x, y))
print(chebbyshev_distance(x, y))

import numpy as np

x = int(input())
y = int(input())

p1 = np.array([int(input())])
p2 = np.array([int(input())])

print(np.linalg.norm(x - y))
print(np.linalg.norm(x - y) ** 2)
print(np.linalg.norm(p1 - p2, ord=np.inf))
print(np.linalg.norm(p1 - p2, ord=1))

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])

a = np.vstack([x, np.ones(len(x))]).T
print(a)

m, c = np.linalg.lstsq(a, y, rcond=None)[0]
print(m, c)

plt.plot(x, y, 'o', label='Initial data', markersize=10)
plt.plot(x, m * x + c, 'r', label='Linear extrapolation')
plt.legend()
plt.show()

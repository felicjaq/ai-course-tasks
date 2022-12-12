import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz

x = np.arange(0.0, 10, 0.1)
y = np.abs(np.sin(x * np.exp(np.cos(x))))

plt.grid(True)
plt.plot(x, y, с='r')
plt.fill_between(x, y)
plt.show()

area = trapz(y)
print(area)

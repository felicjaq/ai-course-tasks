import matplotlib.pyplot as plt
import numpy as np
from numpy import trapz

From = int(input())
To = int(input())

x = np.arange(From, To + 1)

function1 = np.fabs(np.cos(x * np.exp(np.cos(x) + np.log(x + 1))))

plt.plot(x, function1)
plt.fill_between(x, function1)
plt.xticks(x)
plt.grid()
plt.show()

area = trapz(function1)
print(area)

import matplotlib.pyplot as plt
import numpy as np

From = int(input())
To = int(input())

a = np.arange(From, To + 1)
b = a[0: To // 2]

function1 = ((1 + np.exp(np.sqrt(a)) + np.cos(a ** 2)) / (np.fabs(1 - (np.sin(a)) ** 3)) + np.log(np.fabs(2 * a)))
function2 = ((1 + np.exp(np.sqrt(b)) + np.cos(b ** 2)) / (np.fabs(1 - (np.sin(b)) ** 3)) + np.log(np.fabs(2 * b)))

plt.plot(a, function1)
plt.xticks(a)
plt.grid()
plt.show()

plt.scatter(b, function2)
plt.xticks(b)
plt.grid()
plt.show()

print(function1)

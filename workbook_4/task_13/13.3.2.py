from numpy import *
import numpy as np
import matplotlib.pyplot as plt

x = np.array([4.0, 4.2, 4.4, 4.6, 4.8, 5.0])
y = np.array([4.0, 3.0, 6.0, 6.0, 4.0, 4.0])

a = np.vstack([x, np.ones(len(x))]).T
m1, c1 = np.linalg.lstsq(a, y, rcond=None)[0]
print(a)
print('')
print(m1)
print(c1)
print('')

plt.plot(x, y, 'o', label='Initial data', markersize=7)
plt.plot(x, m1 * x + c1, 'r', label='Linear extrapolation')

m2 = np.vstack([x ** 2, x, np.ones(len(x))]).T
s2 = np.linalg.lstsq(m2, y, rcond=None)[0]
print(m2)
print('')
print(s2[0])
print(s2[1])
print(s2[2])
print('')

x_prec_1 = linspace(np.amin(x), np.amax(x), 101)

plt.plot(x, y, 'D')
plt.plot(x_prec_1, s2[0] * x_prec_1 ** 2 + s2[1] * x_prec_1 +
         s2[2], '-', label='Quadratic extrapolation', lw=2)
plt.grid()

m3 = vstack((x ** 3, x ** 2, x, np.ones(len(x)))).T
s3: object = np.linalg.lstsq(m3, y, rcond=None)[0]
print(m3)
print('')
print(s3[0])
print(s3[1])
print(s3[2])
print(s3[3])
print('')

x_prec_2 = linspace(np.amin(x), np.amax(x), 101)

plt.plot(x, y, 'D')
plt.plot(x_prec_2, s3[0] * x_prec_2 ** 3 + s3[1] * x_prec_2 ** 2 +
         s3[2] * x_prec_2 + s3[3], '-', label='Cubic extrapolation', lw=3)
plt.grid()

plt.legend()
plt.show()

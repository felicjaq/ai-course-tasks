from numpy import *
import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt

print('Enter the delta-number!')
delta = int(input())

x = linspace(-10, 10, 11)
y = x ** 2 + delta * (rand(11) - 0.5)
x += delta * (rand(11) - 0.5)

x.tofile('x_data.txt', '\n')
y.tofile('y_data.txt', '\n')

print(x)
print(y)

x = fromfile('x_data.txt', float, sep='\n')
y = fromfile('y_data.txt', float, sep='\n')

m3 = vstack((x ** 3, x ** 2, x, ones(11))).T
m2 = vstack((x ** 2, x, ones(11))).T
m1 = vstack((x, ones(11))).T

s3: object = np.linalg.lstsq(m3, y, rcond=None)[0]
s2: object = np.linalg.lstsq(m2, y, rcond=None)[0]
s1: object = np.linalg.lstsq(m1, y, rcond=None)[0]

x_prec = linspace(-10, 10, 121)

plt.plot(x, y, 'D')
plt.plot(x_prec, s1[0] * x_prec + s1[1], '-', lw=1)
plt.plot(x_prec, s2[0] * x_prec ** 2 + s2[1] * x_prec + s2[2], '-', lw=2)
plt.plot(x_prec, s3[0] * x_prec ** 3 + s3[1] * x_prec ** 2 + s3[2] * x_prec + s3[3], '-', lw=3)
plt.grid()

plt.savefig('Graphics.jpeg')

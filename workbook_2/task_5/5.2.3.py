import numpy as np

Z = np.random.random((10, 10))
Zmin, Zmax, Zmean, = Z.min(), Z.max(), Z.mean()
print(Zmin, Zmax, Zmean)


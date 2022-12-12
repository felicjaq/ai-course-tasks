import numpy as np

a = np.zeros((8, 8), dtype=int)
a[1::2, ::2] = 1
a[::2, 1::2] = 1
print(a)

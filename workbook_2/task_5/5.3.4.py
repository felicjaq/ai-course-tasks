import numpy as np

a = np.ones((4, 4))
a[1:-1,1:-1] = 0
print(a)
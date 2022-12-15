import numpy as np

y = [1, 2, 3, 4, 3, 4, 5, 3, 5, 5, 4, 5,
     4, 5, 4, 5, 6, 0, 6, 3, 1, 3, 1]

x = [[0, 2, 4, 1, 5, 4, 5, 9, 9, 9, 3, 7,
      8, 8, 6, 6, 5, 5, 5, 6, 6, 5, 5],
     [4, 1, 2, 3, 4, 5, 6, 7, 5, 8, 7, 8,
      7, 8, 7, 8, 6, 8, 9, 2, 1, 5, 6],
     [4, 1, 2, 5, 6, 7, 8, 9, 7, 8, 7, 8,
      7, 4, 3, 1, 2, 3, 4, 1, 3, 9, 7]]

x = np.transpose(x)
x = np.c_[x, np.ones(x.shape[0])]
linreg = np.linalg.lstsq(x, y, rcond=None)[0]
print(linreg)
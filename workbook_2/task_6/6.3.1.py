import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([6, 7, 8, 9, 10])

print(sum((a - b)**2)**.5)


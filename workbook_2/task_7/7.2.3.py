from sklearn import preprocessing
import pandas as pd

scaler = preprocessing.MinMaxScaler()
dfTest = pd.DataFrame({'A': [14.00, 90.20, 90.95, 96.27, 91.21],
                       'B': [103.02, 107.26, 110.35, 114.23, 114.68],
                       'C': ['big', 'small', 'big', 'small', 'small']})

dfTest[['A', 'B']] = scaler.fit_transform(dfTest[['A', 'B']])
print(dfTest)

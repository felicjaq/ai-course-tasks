import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

y = [1, 2, 3, 4, 3, 4, 5, 3, 5, 5, 4, 5,
     4, 5, 4, 5, 6, 0, 6, 3, 1, 3, 1]

x = [[0, 2, 4, 1, 5, 4, 5, 9, 9, 9, 3, 7,
      8, 8, 6, 6, 5, 5, 5, 6, 6, 5, 5],
     [4, 1, 2, 3, 4, 5, 6, 7, 5, 8, 7, 8,
      7, 8, 7, 8, 6, 8, 9, 2, 1, 5, 6],
     [4, 1, 2, 5, 6, 7, 8, 9, 7, 8, 7, 8,
      7, 4, 3, 1, 2, 3, 4, 1, 3, 9, 7]]

new_y = np.array(y)
new_y = new_y.transpose()
df1 = pd.DataFrame(new_y)

new_x = np.array(x)
new_x = new_x.transpose()
df2 = pd.DataFrame(new_x)

df1 = df1.rename(columns={0: 'y'}, inplace=False)
df2 = df2.rename(columns={0: 'x1', 1: 'x2', 2: 'x3'}, inplace=False)

frames = [df1, df2]
dataset = pd.concat([df1, df2], axis=1, join="inner")

print(dataset.head())
print('')
print(dataset.shape)
print('')
print(dataset.describe())
print('')

x = dataset[['x1', 'x2', 'x3']]
y = dataset['y']

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

coeff_df = pd.DataFrame(regressor.coef_, x.columns, columns=['Coefficient'])
print(coeff_df)
print('')

y_pred = regressor.predict(x_test)
df = pd.DataFrame({'Actual': y_test,
                   'Predicted': y_pred})
print(df)
print('')
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))

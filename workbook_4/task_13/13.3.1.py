import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

url = 'https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv'

y = [url.quality]
x = [url.pH, url.alcohol, url.density]

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

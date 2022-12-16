import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn import metrics

url = r'https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv'
dataset = pd.read_csv(url)

print(dataset.head)
print(dataset.shape)
print(dataset.describe)

plt.scatter(dataset['density'], dataset['quality'], color='b', label="Заработная плата")
plt.xlabel("Плотность")
plt.ylabel("Качество")
plt.show()

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = DecisionTreeRegressor()
regressor.fit(x_train, y_train)

tree.plot_tree(regressor)

y_pred = regressor.predict(x_test)
print(y_pred)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
print(metrics.mean_absolute_error(y_test, y_pred) / np.average(y) * 100)

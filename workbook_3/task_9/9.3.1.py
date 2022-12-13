import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
iris = iris.sort_values(by=['sepal.width'])
iris = iris.head(22)
print(iris)

plt.figure(figsize=(16, 7))

plt.subplot(121)
sns.scatterplot(
    data=iris,
    x='petal.width',
    y='petal.length',
    hue='variety',
    s=40)
plt.xlabel('Длина лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend()
plt.grid()

plt.subplot(122)
sns.scatterplot(
    data=iris,
    x='sepal.width',
    y='sepal.length',
    hue='variety',
    s=40)
plt.xlabel('Длина чашелистика, см')
plt.ylabel('Ширина чашелистика, см')
plt.legend()
plt.grid()
plt.show()

x_train, x_test, y_train, y_test = train_test_split(
    iris.iloc[:, :-1],
    iris.iloc[:, -1],
    test_size=0.20)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train.head())
print(y_train.head())

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

plt.figure(figsize=(10, 7))
sns.scatterplot(x='petal.width',
                y='petal.length',
                data=iris,
                hue='variety',
                s=70)
plt.xlabel("Длина лепестка, см")
plt.ylabel("Ширина лепестка, см")
plt.legend(loc=2)
plt.grid()
plt.show()

for i in range(len(y_test)):
    if np.array(y_test)[i] != y_pred[i]:
        plt.scatter(x_test.iloc[i, 3],
                    x_test.iloc[i, 2],
                    color='red',
                    s=150)

print(f'accuracy: {accuracy_score(y_test, y_pred) : .3}')

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

my_dict = {"Учебное время": [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75,
                             2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50,
                             4.00, 4.25, 4.50, 4.75, 5.00, 5.50],
           "Оценка": [10, 22, 13, 43, 20, 22, 33, 50, 62, 48, 55,
                      75, 62, 73, 81, 76, 64, 82, 90, 93]}

dataset = pd.DataFrame(my_dict)
print(dataset.head())

print(dataset.shape)
print(dataset.describe())

plt.scatter(dataset["Учебное время"],
            dataset['Оценка'],
            color='r',
            label="Данные экзамена")
plt.xlabel("Часы")
plt.ylabel("Оценка")
plt.show()

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(x_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)

y_pred = regressor.predict(x_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

df.plot(kind='bar')

plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='red')
plt.show()

plt.scatter(x_test, y_test, color='gray')
plt.plot(x_test, y_pred, color='red', linewidth=2)
plt.show()

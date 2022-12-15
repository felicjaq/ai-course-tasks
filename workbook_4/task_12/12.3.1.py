import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = 'https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv'

dataset = pd.read_csv(url, sep=',')
print(dataset.head())

print(dataset.shape)
print(dataset.describe())

plt.scatter(dataset['YearsExperience'],
            dataset['Salary'],
            color='g',
            label="Данные:")
plt.xlabel("Опыт работы (часов)")
plt.ylabel("Зарплата (рублей)")
plt.grid()
plt.show()

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

print(x)
print(y)

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2, random_state=0)
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

plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, y_pred,
         color='red',
         linewidth=1.5,
         drawstyle='default')

plt.grid()
plt.show()

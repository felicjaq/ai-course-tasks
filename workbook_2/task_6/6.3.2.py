import pandas as pd

print('Введите имя файла без расширения!')
csv1 = input() + '.csv'

dataframe = pd.read_csv(csv1, delimiter=';')

print(dataframe.head(5))
print('\n', '\n')
print(dataframe.tail(3))
print('\n', '\n')
print(dataframe.shape)
print('\n', '\n')
print(dataframe.describe)
print('\n', '\n')
print(dataframe.loc[1:4])
print('\n', '\n')
print(dataframe[dataframe['gender'] == 'f'].head(5))
print('\n', '\n')
print(dataframe.sort_values('all_deaths'))

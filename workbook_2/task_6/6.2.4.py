import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
dataframe = pd.read_csv(url)

print(dataframe.head(5))
print('\n', '\n')
print(dataframe.tail(3))
print('\n', '\n')
print(dataframe.shape)
print('\n', '\n')
print(dataframe.describe)
print('\n', '\n')
print(dataframe.iloc[1:4])
print('\n', '\n')
print(dataframe[dataframe['PClass'] == '1st'].head(2))

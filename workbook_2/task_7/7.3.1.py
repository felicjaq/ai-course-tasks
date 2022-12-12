from sklearn import preprocessing
import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/master/iris.csv'

dataframe = pd.read_csv(url)
print(dataframe.head(5))

scaler1 = preprocessing.MinMaxScaler()
standardized1 = pd.DataFrame(dataframe)
standardized1[['sepal_length_cm']] = scaler1.fit_transform(standardized1[['sepal_length_cm']])
print(standardized1)

scaler2 = preprocessing.StandardScaler()
standardized2 = pd.DataFrame(dataframe)
standardized2[['sepal_width_cm']] = scaler2.fit_transform(standardized1[['sepal_width_cm']])
print(standardized2)

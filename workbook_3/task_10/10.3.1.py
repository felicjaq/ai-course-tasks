from sklearn.feature_extraction import DictVectorizer

data_dict = [{"Цвет глаз": "карий", "Цвет волос": "карий"},
             {"Цвет глаз": "синий", "Цвет волос": "нет"},
             {"Цвет глаз": "зеленый", "Цвет волос": ""},
             {"Цвет глаз": "зеленый", "Цвет волос": 2}]

dictvectorizer = DictVectorizer(sparse=False)

features = dictvectorizer.fit_transform(data_dict)
print(features)

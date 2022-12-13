import pandas as pd

dataframe = pd.DataFrame({"оценка": ['низкая', 'низкая', 'средняя',
                                     'средняя', 'высокая']})
scale_mapper = {'низкая': 1, 'средняя': 2, 'высокая': 3}

print(dataframe["оценка"].replace(scale_mapper))

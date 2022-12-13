from sklearn.neighbors import KNeighborsClassifier
import numpy as np

x = np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]

k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(x, target)
print(model)

print('(-2, 2) is class')
print(model.predict([[-2, 2]]))

print('(1, 3) is class')
print(model.predict([[1, 3]]))

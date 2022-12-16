import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

inf = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]
X = pd.DataFrame(inf, target)

print(X)
print(X.shape)
print(X.head)

x_train, x_test, y_train, y_test = train_test_split(
    X.iloc[:, :-1],
    X.iloc[:, -1],
    test_size=0.20
)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train.head)
print(y_train.head)

classifier = DecisionTreeClassifier()
print(classifier.fit(x_train, y_train))
print(tree.plot_tree(classifier))

y_pred = classifier.predict(x_test)
print(y_pred)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

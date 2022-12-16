import seaborn as sns
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

dataset = sns.load_dataset('iris')

print(dataset)
print(dataset.shape)
print(dataset.head)

x_train, x_test, y_train, y_test = train_test_split(
    dataset.iloc[:, :-1],
    dataset.iloc[:, -1],
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

import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'

customer_data = pd.read_csv(url)
print(customer_data.head)

data = customer_data.iloc[:, 1:3].values

plt.figure(figsize=(28, 12), dpi=180)
plt.figure(figsize=(10, 7))
plt.title("Customer dendograms:")

dend = shc.dendrogram(shc.linkage(data, method='ward'))

cluster = AgglomerativeClustering(n_clusters=5,
                                  affinity='euclidean',
                                  linkage='ward')
cluster.fit_predict(data)

plt.figure(figsize=(10, 7))
plt.scatter(data[:, 0], data[:, 1], c=cluster.labels_,
            cmap='rainbow')
plt.show()

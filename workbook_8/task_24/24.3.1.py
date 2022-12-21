import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns;

sns.set()
from sklearn.cluster import KMeans

digits = np.array([[5, 3], [10, 15], [12, 12], [24, 10], [30, 45],
                   [85, 70], [71, 80], [60, 78], [55, 52], [80, 91]])

digits = pd.DataFrame(digits, columns=['first', 'second'])
print(digits.head)

kmeans = KMeans(n_clusters=10, random_state=2)
clusters = kmeans.fit_predict(digits)
print(kmeans.cluster_centers_.shape)

fig, ax = plt.subplots(2, 5, figsize=(14, 5))
centers = kmeans.cluster_centers_.reshape(20, 1, 1)

for axi, center in zip(ax.flat, centers):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans

sns.set()

X, y_true = make_blobs(n_samples=400,
                       centers=4,
                       cluster_std=0.60,
                       random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=20)
plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

X, y_true = make_blobs(n_samples=400,
                       centers=4,
                       cluster_std=0.60,
                       random_state=0)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=20, cmap='summer')
centers = kmeans.cluster_centers_

plt.scatter(centers[:, 0], centers[:, 1], c='blue',
            s=100,
            alpha=0.9)
plt.show()

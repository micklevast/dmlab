from sklearn.cluster import Birch
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample data
data, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# BIRCH clustering
birch_model = Birch(threshold=0.5, n_clusters=None)
birch_clusters = birch_model.fit_predict(data)

# Plotting the results
plt.scatter(data[:, 0], data[:, 1], c=birch_clusters, cmap='viridis')
plt.title('BIRCH Clustering')
plt.show()

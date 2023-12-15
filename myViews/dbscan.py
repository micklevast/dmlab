from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# Generate sample data
data, _ = make_moons(n_samples=200, noise=0.05, random_state=42)

# DBSCAN clustering
dbscan_model = DBSCAN(eps=0.3, min_samples=5)
dbscan_clusters = dbscan_model.fit_predict(data)

# Plotting the results
plt.scatter(data[:, 0], data[:, 1], c=dbscan_clusters, cmap='viridis')
plt.title('DBSCAN Clustering')
plt.show()

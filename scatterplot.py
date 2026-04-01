import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 🔵 Cluster 1 (positive correlation)
x1 = np.random.normal(20, 5, 100)
y1 = 2 * x1 + np.random.normal(0, 5, 100)

# 🟢 Cluster 2 (negative correlation)
x2 = np.random.normal(60, 5, 100)
y2 = -1.5 * x2 + 120 + np.random.normal(0, 5, 100)

# 🔴 Outliers
x_out = np.array([10, 90, 50])
y_out = np.array([120, 10, 150])

# Combine all data
x = np.concatenate([x1, x2, x_out])
y = np.concatenate([y1, y2, y_out])

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(x1, y1, color='blue', label='Cluster (Positive Corr)')
plt.scatter(x2, y2, color='green', label='Cluster (Negative Corr)')
plt.scatter(x_out, y_out, color='red', s=100, label='Outliers')

plt.title("Scatter Plot with Cluster, Correlation & Outliers")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)

plt.show()
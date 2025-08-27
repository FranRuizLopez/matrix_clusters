import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from matrix_clusters.clusters_3d import count_clusters_3d

# Example of 3D binary array (default threshold = 1)
matrix_3d = [[[1, 1, 0], [1, 0, 0], [0, 0, 1]],
           [[0, 0, 0], [0, 1, 1], [0, 0, 0]],
           [[1, 0, 0], [0, 0, 0], [0, 1, 1]]]

print("Clusters 3D (binaria):", count_clusters_3d(matrix_3d))

# 3D example with continuous and threshold values
matrix_3d_cont = [[[0.7, 0.8, 0.2], [0.6, 0.3, 0.1], [0.0, 0.1, 0.9]],
                  [[0.1, 0.2, 0.1], [0.0, 0.8, 0.9], [0.1, 0.2, 0.1]],
                  [[0.9, 0.1, 0.0], [0.2, 0.1, 0.2], [0.1, 0.8, 0.7]]]

threshold = 0.5
print(f"Clusters 3D con threshold {threshold}:", count_clusters_3d(matrix_3d_cont, threshold = threshold, min_size=3))
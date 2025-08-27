

from matrix_clusters.clusters_2d import count_clusters_2d
# Example of 2D binary array (default threshold = 1)
matrix_2d = [
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
]

print("Clusters 2D (binaria):", count_clusters_2d(matrix_2d))

# 2D example with continuous and threshold values
matrix_2d_cont = [
    [0.7, 0.8, 0.2, 0.1, 0.0, 0.9],
    [0.6, 0.3, 0.1, 0.8, 0.9, 0.7],
    [0.0, 0.1, 0.2, 0.0, 0.1, 0.0],
    [0.1, 0.8, 0.9, 0.2, 0.7, 0.0],
    [0.0, 0.1, 0.0, 0.0, 0.8, 0.0],
]

threshold = 0.5
print(f"Clusters 2D con threshold {threshold}:", count_clusters_2d(matrix_2d_cont, threshold = threshold, min_size=3))

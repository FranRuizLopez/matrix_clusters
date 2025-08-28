import numpy as np
from .base import get_neighbors

def count_clusters_3d(matrix, diagonals=False, min_size=1, threshold=1):
    """
    Counts clusters in a 3D matrix.

    Args:
        matrix: 3D list or numpy.ndarray
            Input matrix. Can be a nested list (list of lists of lists) or a NumPy array.
        diagonals (bool): If True, consider diagonal connections.
        min_size (int): Minimum size of clusters to be counted.
        threshold (float): Minimum value to consider as part of a cluster.
                           Default is 1 (works naturally for binary matrices).
    Returns:
        int: Number of clusters found.
    """
    matrix = np.array(matrix)

    if matrix.ndim != 3:
        raise ValueError(f"Input must be 3D, but got {matrix.ndim}D")

    shape = matrix.shape
    visited = np.zeros(shape, dtype=bool)
    clusters = 0

    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                if visited[i, j, k]:
                    continue
                visited[i, j, k] = True
                if matrix[i, j, k] >= threshold:
                    cluster = [(i, j, k)]
                    p = 0
                    while p < len(cluster):
                        x, y, z = cluster[p]
                        for neighbor in get_neighbors((x, y, z), shape, diagonals):
                            if not visited[neighbor] and matrix[neighbor] >= threshold:
                                cluster.append(neighbor)
                                visited[neighbor] = True
                        p += 1
                    if len(cluster) >= min_size:
                        clusters += 1
    return clusters

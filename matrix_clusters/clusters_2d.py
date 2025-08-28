import numpy as np
from matrix_clusters.base import get_neighbors

def count_clusters_2d(matrix, diagonals=False, min_size=1, threshold=1):
    """
    Counts clusters in a 2D matrix.

    Args:
        matrix: 2D list or numpy.ndarray
        diagonals: if True, consider diagonal connections
        min_size: minimum size of clusters to be counted
        threshold: value to consider as part of a cluster (default is 1 and represents binary matrix)
    """
    matrix = np.array(matrix)  

    if matrix.ndim != 2:
        raise ValueError(f"Input must be 2D, but got {matrix.ndim}D")
    
    shape = (len(matrix), len(matrix[0]))
    visited = np.zeros((shape[0], shape[1]), dtype=bool)
    clusters = 0

   
    for i in range(shape[0]):
        for j in range(shape[1]):
            if visited[i, j]:
                continue
            visited[i, j] = True
            if matrix[i, j] >= threshold:
                cluster = [(i, j)]
                k = 0
                while k < len(cluster):
                    x, y = cluster[k]
                    for neighbor in get_neighbors((x, y), shape, diagonals):
                        if not visited[neighbor] and matrix[neighbor] >= threshold:
                            cluster.append(neighbor)
                            visited[neighbor] = True
                    k += 1
                if len(cluster) >= min_size:
                    clusters += 1
    return clusters
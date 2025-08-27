import numpy as np
from .base import get_neighbors

def count_clusters_3d(matrix, diagonals=False, min_size=1, threshold=1):
    """
    Counts clusters in a 3D binary matrix.

    Args:
        matrix: 3D list or array-like with binary values (0s and 1s)
        diagonals: if True, consider diagonal connections
        min_size: minimum size of clusters to be counted
    """
    shape = (len(matrix), len(matrix[0]), len(matrix[0][0]))
    visited = np.zeros((shape[0], shape[1], shape[2]), dtype=bool)
    clusters = 0

    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                if visited[i][j][k] == True:
                    continue
                visited[i][j][k] = True
                if matrix[i][j][k] >= threshold:
                    cluster = [(i,j,k)]
                    p = 0
                    while p < len(cluster):
                        x, y, z = cluster[p]
                        for neighbor in get_neighbors((x, y, z), shape, diagonals):
                            if neighbor not in cluster and matrix[neighbor[0]][neighbor[1]][neighbor[2]] >= threshold:
                                cluster.append(neighbor)
                                visited[neighbor[0]][neighbor[1]][neighbor[2]] = True
                        p += 1
                    if len(cluster) >= min_size:
                        clusters += 1
    return clusters
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from matrix_clusters.clusters_2d import count_clusters_2d

def test_binary_2d_clusters():
    matrix = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    result = count_clusters_2d(matrix)
    assert result == 2  

def test_threshold_2d_clusters():
    matrix = [
        [0.7, 0.2, 0.9],
        [0.1, 0.8, 0.0],
        [0.6, 0.1, 0.8]
    ]
    binary_matrix = count_clusters_2d(matrix, threshold=0.5)
    result = count_clusters_2d(binary_matrix)
    assert result == 3


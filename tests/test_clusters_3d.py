import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from matrix_clusters.clusters_3d import count_clusters_3d


def test_binary_3d_clusters():
    matrix = [
        [[1,0,1],[0,1,0],[0,0,1]],
        [[0,0,0],[0,1,1],[0,0,0]],
        [[1,0,0],[0,0,0],[0,1,1]]
    ]
    result = count_clusters_3d(matrix)
    assert result == 6

def test_threshold_3d_clusters():
    matrix = [
        [[0.7,0.8,0.2],[0.6,0.3,0.1],[0.0,0.1,0.9]],
        [[0.1,0.2,0.1],[0.0,0.8,0.9],[0.1,0.2,0.1]],
        [[0.9,0.1,0.0],[0.2,0.1,0.2],[0.1,0.8,0.7]]
    ]
    result = count_clusters_3d(matrix, threshold=0.5)
    assert result == 5  
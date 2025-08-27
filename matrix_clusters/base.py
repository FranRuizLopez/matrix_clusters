from itertools import product

def get_neighbors(coord, shape, diagonals=False):
    """
    Returns the valid neighbors in N dimensions.
    
    Args:
        coord: tuple with the coordinates (e.g., (x, y) in 2D, (x, y, z) in 3D)
        shape: size of the matrix in each dimension (e.g., (rows, cols) or (rows, cols, depth))
        diagonals: if True, include diagonal neighbors (8 in 2D, 26 in 3D)
    
    Returns:
        List of tuples with valid neighbor coordinates
    """

    ndim = len(coord)
    ranges = [-1, 0, 1]
    
    for delta in product(ranges, repeat=ndim):
        if all(d == 0 for d in delta):
            continue  
        if not diagonals and sum(abs(d) for d in delta) != 1:
            continue  # neighbours without diagonals
        neighbor = tuple(c + d for c, d in zip(coord, delta))
        # Limits check
        if all(0 <= neighbor[i] < shape[i] for i in range(ndim)):
            yield neighbor

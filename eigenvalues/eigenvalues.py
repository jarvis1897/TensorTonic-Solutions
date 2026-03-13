import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix = np.asarray(matrix)
    except (ValueError, TypeError):
        return None

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    if matrix.size == 0:
        return np.array([])

    eigvals = np.linalg.eigvals(matrix)
    idx = np.lexsort((eigvals.imag, eigvals.real))
    return eigvals[idx]
    
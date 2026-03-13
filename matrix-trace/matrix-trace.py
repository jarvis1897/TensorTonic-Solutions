import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    sum = 0
    A = np.array(A)
    for i in range(A.shape[0]):
        sum += A[i, i]

    return sum

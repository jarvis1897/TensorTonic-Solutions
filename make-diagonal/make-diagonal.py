import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = np.size(v)
    arr = np.zeros((n, n))
    print(arr)

    for i in range(n):
        arr[i, i] = v[i]
    
    return arr

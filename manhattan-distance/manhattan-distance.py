import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    arr = np.abs(x-y)   
    # print(type(sum(arr)))

    return int(np.sum(arr))
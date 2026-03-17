import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    n = x.size
    x.sort()
    mean = sum(x)/len(x)
    median = -1
    if n%2 == 0:
        median = (x[n//2 - 1] + x[n//2]) / 2
    else:
        median = x[n//2]

    count = Counter(x)
    max_freq = 0
    for v in count.values():
        max_freq = max(max_freq, v)

    mode = float('inf')
    for key, value in count.items():
        if value == max_freq:
            mode = min(mode, key)

    return mean, median, mode
    
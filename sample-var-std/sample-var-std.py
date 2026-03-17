import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    if len(x) < 2:
        return 0, 0
    # Write code here
    x = np.array(x)
    x_mean = sum(x)/x.size
    var = (sum((x-x_mean) ** 2) / (x.size-1)) 
    sd = var ** 0.5

    return var, sd
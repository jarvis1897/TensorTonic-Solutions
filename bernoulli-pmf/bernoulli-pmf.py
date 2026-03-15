import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pmf = []
    for e in x:
        if e == 0:
            pmf.append(1-p)
        else:
            pmf.append(p)

    return np.array(pmf), p, p*(1-p)
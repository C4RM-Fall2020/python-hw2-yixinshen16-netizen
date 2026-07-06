import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    cf = np.full(n, c)
    cf[-1] = cf[-1] + face

    x = np.sum(cf / (1 + r) ** t)
    return(x)

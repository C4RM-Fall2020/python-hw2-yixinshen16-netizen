import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    cf = np.full(n, c)
    cf[-1] = cf[-1] + face

    pv = cf / (1 + r) ** t
    price = np.sum(pv)

    x = np.sum((t / ppy) * pv) / price
    return(x)

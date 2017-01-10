import numpy as np
from numpy.random import permutation


def randomstate(NA, NB, M):
    m = np.zeros((M,M))
    index = permutation(M*M)
    ix, iy = np.unravel_index(index, (M,M))
    j = range(NA)
    m[ix[j], iy[j]] = 1
    j = range(NA, NA+NA)
    m[ix[j], iy[j]] = -1
    return m

m = randomstate(32, 32, 8)

print(m)

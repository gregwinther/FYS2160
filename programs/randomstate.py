import numpy as np

def randomstate(NA, M):
    m = np.zeros((M,M))
    index = np.random.permutation(M*M)
    ix, iy = np.unravel_index(index, (M,M))
    j = range(NA)
    m[ix[j], iy[j]] = 1
    j = range(NA, NA+(M*M-NA))
    m[ix[j], iy[j]] = -1
    return m

m = randomstate(32, 8)

print(m)

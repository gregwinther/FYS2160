import numpy as np
from matplotlib import pyplot as plt

M = 10000
N = 50
a = 1
nn = 2*np.floor(np.random.rand(M,N)*2) - 1
nt = np.sum(nn, axis = 1)
plt.hist(nt)
plt.show()

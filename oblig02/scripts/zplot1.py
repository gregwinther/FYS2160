'''
Function to plot the different z(j) terms in the partition function
The partition function is a sum of all such terms
Problem e.
z(j) = (2j + 1)*exp(-j*(j+1)*theta_r/T)
'''

import numpy as np 
from matplotlib import pyplot as plt

j = np.arange(0,10)

def partitionTerm(j, theta_prime): # theta_prime is theta_r/T
	return (2*j + 1)*np.exp(-j*(j+1)*theta_prime)

z_j1 = partitionTerm(j,0.05) # T/theta_r = 20
z_j2 = partitionTerm(j,0.1) # T/theta_r = 10
z_j3 = partitionTerm(j,0.2)    # T/theta_r = 5
z_j4 = partitionTerm(j,0.5)    # T/theta_r = 2
z_j5 = partitionTerm(j,1)   # T/theta_r = 1
z_j6 = partitionTerm(j,10)   # T/theta_r = 0.1 

plt.plot(j, z_j1, '-o',  label=r'$T/\theta_r = 20$')
plt.plot(j, z_j2, '-o',  label=r'$T/\theta_r = 10$')
plt.plot(j, z_j3, '-o',  label=r'$T/\theta_r = 5$')
plt.plot(j, z_j4, '-o',  label=r'$T/\theta_r = 2$')
plt.plot(j, z_j5, '-o',  label=r'$T/\theta_r = 1$')
plt.plot(j, z_j6, '-o',  label=r'$T/\theta_r = 0.1$')

plt.title(r'Partition function terms $z(j)$ for various $T/\theta_r$')
plt.xlabel(r'$j$', fontsize=20)
plt.ylabel(r'$z(j)$', fontsize=20)
plt.legend()

plt.show()
'''
Plot of heat capacity vs temperature
k is Boltzmann's constant
eps sets the energy scale, small fraction of an eV
s.t. eps/k = 2.8 K
T is temperature in Kelvin, supposed to be cold temperatures.
'''

import numpy as np
from matplotlib import pyplot as plt

eps = 0.00024 # eV
k = 8.617e-5 # eV/K



def heatCap(T):
	return 	3*eps*eps*np.exp(eps/(T*k))/\
			(T*T*k*(np.exp(eps/(T*k)) + 3)**2)




# A table
print("T[K]  & C[J/K]")
for temp in [1, 25, 50, 100, 273]:
	print("${:>3}$ & ${:>10.4e}$".format(temp, heatCap(temp)))

# Plot
starttemp = 1
stoptemp = 20
T = np.linspace(starttemp, stoptemp) # K  
C = heatCap(T)
plt.title("Heat Capacity vs Temperature")
plt.xlabel("T [K]")
plt.ylabel("C [J/K]")
plt.plot(T, C)
plt.show()

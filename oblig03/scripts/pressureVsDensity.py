'''
Dimensionless pressure p_hat vs dimensionless density rho_hat
for different T_hat = 1.15, 1.00 and 0.85
'''

import numpy as np 
from matplotlib import pyplot as plt 

def dimlesspressure2(rho_hat, T_hat):
	return (8.0*rho_hat*T_hat)/(3-rho_hat) - 3*rho_hat*rho_hat

rho_hat = np.linspace(0.0, 2.0, 1001)
plt.plot(rho_hat, dimlesspressure2(rho_hat, 1.15), label=r'$\hat{T}=1.15$')
plt.plot(rho_hat, dimlesspressure2(rho_hat, 1.00), label=r'$\hat{T}=1.00$')
plt.plot(rho_hat, dimlesspressure2(rho_hat, 0.85), label=r'$\hat{T}=0.85$')
plt.legend(loc=2)
plt.title("Pressure as a function of density at different temperatures")
plt.xlabel(r"$\hat{\rho}=\rho/\rho_c$", fontsize=16)
plt.ylabel(r"$\hat{p}=p/p_c$", fontsize=16)
plt.show()

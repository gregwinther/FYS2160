'''
The dimensionless pressure p_hat as a function of V_hat in
the range from 0.4 to 20 for T_hat = 1.15, 1.0, 0.85
'''

import numpy as np
from matplotlib import pyplot as plt

def dimlesspressure1(V_hat, T_hat):
	return (8.0*T_hat)/(3*V_hat - 1) - 3/(V_hat*V_hat)

V_hat = np.linspace(0.4, 20, 1001)

plt.plot(V_hat, dimlesspressure1(V_hat, 1.15), label=r'$\hat{T}=1.15$')
plt.plot(V_hat, dimlesspressure1(V_hat, 1.00), label=r'$\hat{T}=1.00$')
plt.plot(V_hat, dimlesspressure1(V_hat, 0.85), label=r'$\hat{T}=0.85$')
plt.ylim(0,4)
plt.xlim(0,7)
plt.legend()
plt.title("Pressure as a function of volume at different temperatures")
plt.xlabel(r"$\hat{V}=V/V_c$", fontsize=16)
plt.ylabel(r"$\hat{p}=p/p_c$", fontsize=16)
plt.show()
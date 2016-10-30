'''
Gibbs free energy
'''

import numpy as np

from matplotlib import pyplot as plt

n = 100001

T=  [0.9]
N=  len(T) #Number of temperatures
P = np.zeros((N,n))

rho = np.linspace(0.2,2.0,n)
for i in range(N):
	P[i] = rho*8.*T[i]/(3.-rho) - 3.*rho**2
	plt.plot(rho,P[i],label="Pressure")
	plt.xlabel(r"$\hat{\rho}=\rho/\rho_c$",size = 16)
	plt.ylabel(r"$\hat{p}=p/p_c$",size = 16)
	plt.title(r"Pressure as a function of density for $\hat{T}=0.9$")
	plt.show()	

	plt.plot(P[i],1./rho,label="Volume")
	plt.ylabel(r"$\hat{V}=V/V_c$",size = 16)
	plt.xlabel(r"$\hat{p}=p/p_c$",size = 16)
	plt.title(r"Pressure as a function of volume for $\hat{T}=0.9$")
	plt.show()

	plt.plot(P[i],-3*rho-8./3.*T[i]*np.log(3/rho-1) + P[i]/rho,label="Gibbs")
	plt.ylabel(r"$\hat{g}=G/(NG_c)$",size = 16)
	plt.xlabel(r"$\hat{P}=P/P_c$",size = 16)
	plt.title(r"Pressure as a function of density for $\hat{T}=0.9$")	
	plt.show()

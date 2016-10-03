'''
Function that calculates a reasonable approximation of the
partition function Z(T,V,N)
for at particular value of T_over_theta = T/theta_r.
'''

import sys
import numpy as np 
from matplotlib import pyplot as plt

def partitionFunction(T_over_theta):
	
	# Tolerance for when to stop adding
	eps = 1e-12  

	# Partition function
	# Starting at state j = 0
	Z = 1 		

	# Current term of partition function
	# State j = 0 already stored
	Z_ = 1

	# State counter
	j = 1		

	# T_over_theta inverse
	theta_prime = 1.0/T_over_theta

	while (Z_ > eps):
		Z_ = (2*j + 1)*np.exp(-j*(j+1)*theta_prime)
		Z += Z_
		j += 1

	return Z

def energyCompute():

	start = 1
	stop = 10
	n = 100

	# Assuming theta_r is constant. 
	T = np.linspace(start, stop, n)

	E = np.zeros(n)
	Z = np.zeros(n)

	k = 0
	for thing in T:
		Z[k] = partitionFunction(thing)
		k += 1

	for i in range(n-1):
		E[i] = -(1/T[i])*(Z[i+1] - Z[i]) / ((1/T[i+1]) - (1/T[i]))

	plt.title(r"Numerically computed average energy")
	plt.xlabel(r"$T/\theta_r$", fontsize=20)
	plt.ylabel(r"$\bar{E}/k$", fontsize=20)
	plt.plot(T[1:-2],E[1:-2])
	plt.show()

if __name__ == '__main__': 

	if len(sys.argv) != 1:

		if int(sys.argv[1]) == 1:

			# Arrays for storing and plotting
			T_over_theta = np.linspace(0.001,1000)
			Z = np.zeros(len(T_over_theta))
			
			# Evaluating Z for different T_over_theta
			i = 0
			for thing in T_over_theta:
				Z[i] = partitionFunction(thing)
				i += 1
			
			# Plotting (logarithmic x-axis)
			plt.semilogx(T_over_theta, Z)
			plt.title(r"Numerical evaluation of partition function for various $T/\theta_r$")
			plt.xlabel(r"$T/\theta_r$", fontsize=20)
			plt.ylabel(r"Z", fontsize=20)
			plt.show()

		elif int(sys.argv[1]) == 2:

			# Arrays for storing and plotting
			T_over_theta = np.linspace(1.5,15)
			Z = np.zeros(len(T_over_theta))
			
			# Evaluating Z for different T_over_theta
			i = 0
			for thing in T_over_theta:
				Z[i] = partitionFunction(thing)
				i += 1

			plt.plot(T_over_theta, abs(Z-T_over_theta))
			plt.title("Absolute difference between numerical and analytical partition function")
			plt.xlabel(r"$T/\theta_r$", fontsize=20)
			plt.ylabel(r"$\mid \frac{T}{\theta_r}-Z_{num} \mid$", fontsize=20)
			plt.show()

		elif int(sys.argv[1]) == 3:

			energyCompute()

	else:

		print("Usage: ")
		print("1 for plot of partition function")
		print("2 for numerical/analytical comparisson")
		print("3 for energy computation")
import numpy as np 
from matplotlib import pyplot as plt
import scipy.misc

class RandomSpin():
	"""Generates M microstates randomly for a system
		of N up/down (+1 or -1) spins"""
	def __init__(self, M, N):

		self.M = M
		self.N = N

		# mu and B are set to 1 as default.
		self.mu = 1.0
		self.B = 1.0

		self.microstates = np.zeros(shape=(M,N))

		for i in range(M):
			for j in range(N):
				# Generates random numers -1 or +1
				self.microstates[i,j] = np.random.randint(2)*2 -1

	def energyHistogram(self, binsNumber=10):
		net_spin = np.zeros((self.M,1))
		for i in range(self.M):
			net_spin[i] = float(sum(self.microstates[i,:])) / 2
		
		# Energy
		U = - 2 *self.mu * self.B * net_spin

		# Analytical solution
		#STUFF NEEDS TO BE SORTED CORRECTLY!
		#nu = np.linspace(-self.N,self.N,self.M)
		nu = (- U / (2*self.mu*self.B))
		
		prob = self.M*\
			scipy.misc.comb(self.N,self.N/2)*\
			np.exp(-nu*nu/self.N)/\
			2**(self.N)
			#np.exp(-U/(2*self.mu*self.B))/\
	
		print(U.shape,prob.shape)

		#plt.hist(U, bins=binsNumber, label="Numerical")
		plt.plot(U, prob, label="Analytical", linewidth=2)
		plt.title("Histogram of M = "+ str(self.M) \
			+ " and  N = " + str(self.N))
		plt.xlabel("Frequency")
		plt.ylabel("Energy (U)")
		plt.xlim([-self.N/2,self.N/2])
		plt.legend()
		plt.show()

	# Setter for mu
	def setMu(mu):
		self.mu = mu

	# Setter for B
	def setB(B):
		self.B = B


if __name__ == '__main__':
	M = 10000
	N = 50
	spin50 =  RandomSpin(M, N)
	spin50.energyHistogram(N) # argument is number of bins
		
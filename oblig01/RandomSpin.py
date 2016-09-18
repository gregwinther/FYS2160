import numpy as np 
from matplotlib import pyplot as plt

class RandomSpin():
	"""Generates M microstates randomly for a system
		of N u/down (+1 or -1) spins"""
	def __init__(self, M, N):

		self.M = M
		self.N = N

		# mu and B are set to one as standard.
		self.mu = 1.0
		self.B = 1.0

		self.microstates = np.zeros(shape=(M,N))

		for i in range(M):
			for j in range(N):
				# Generates ranom numers -1 or +1
				self.microstates[i,j] = np.random.randint(2)*2 -1

	def energyHistogram(self):
		net_spin = np.zeros(self.M)
		for i in range(self.M):
			net_spin[i] = float(sum(self.microstates[i,:])) / 2
		
		# Energy
		U = - 2 *self.mu * self.B * net_spin 
		plt.hist(U)
		plt.title("Histogram of M = "+ str(self.M) \
			+ " and  N = " + str(self.N))
		plt.xlabel("Frequency")
		plt.ylabel("Energy (U)")
		plt.show()

	# Setter for mu
	def setMu(mu):
		self.mu = mu

	# Setter for B
	def setB(B):
		self.B = B


if __name__ == '__main__':

	spin50 =  RandomSpin(10000,50)
	spin50.energyHistogram()
		
import numpy as np
from matplotlib import pyplot as plt
import scipy.misc

class EinsteinCrystal:

	def __init__(self, q, N_A, N_B):

		# Arguments
		self.q = q
		self.N_A = N_A
		self.N_B = N_B

		# Initializing data structures
		self.q_A = np.asarray(range(0, q+1))
		self.omega_A = np.zeros(q+1)
		self.q_B = np.zeros(q+1)
		self.omega_B = np.zeros(q+1)
		self.omega_tot = np.zeros(q+1)

		# Computation loop
		for i in range(0, self.q+1):
			
			self.omega_A[i] = \
			scipy.misc.comb(self.q_A[i] + self.N_A-1, self.q_A[i])
			self.q_B[i] = self.q - self.q_A[i]
			self.omega_B[i] = \
			scipy.misc.comb(self.q_B[i] + self.N_B-1, self.q_B[i])
			self.omega_tot[i] = self.omega_A[i] * self.omega_B[i]


	def table(self):
		# Printing header
		print("{:>5} {:>7} {:>5} {:>7} {:>10}"
		.format("q_A", "omega_A", "q_B", "omega_B", "omega_tot"))

		# Printing data
		for i in range(0, self.q+1):
			print("{:>5.0f} {:>7.0f} {:>5.0f} {:>7.0f} {:>10.0f}"\
				.format(self.q_A[i], self.omega_A[i],\
				 self.q_B[i], self.omega_B[i], self.omega_tot[i]))

		# Total multiplicity
		print("{:>28}{:>10}".format("Sum:",np.sum(self.omega_tot)))

	def PDF(self):
		
		# Array for probabilities
		self.probs = np.zeros(self.q+1)
		
		# Computing probabilities
		for i in range(self.q+1):
			self.probs[i] \
			= self.omega_tot[i] / np.sum(self.omega_tot)

		# Printing probabilities if the system is not too large
		if self.q <= 20:
			print("{:>5} {:>7}".format('q_A', 'P(q_A)'))
			for i in range(self.q+1):
				print("{:>5.0f} {:>7.4f}"\
					.format(self.q_A[i], self.probs[i]))

	def getPDF(self):
		return self.q_A, self.probs


States1 = EinsteinCrystal(6, 2, 2)
States2 = EinsteinCrystal(100, 50, 50)
States1.table()
States1.PDF()
States2.PDF()
q_A, probs = States2.getPDF()

plt.plot(q_A, probs)
plt.title("PDF of two Einstein crystals  "+r'$q=100, N_A=N_B=50$')
plt.xlabel(r'$q_A$', fontsize=18)
plt.ylabel(r'$P(q_A)$', fontsize=18)
plt.show()

large = probs[0]
for i in range(len(q_A)):
    if probs[i] > large:
        large = probs[i]
        maxIndex = i

print("Max prob: ")
print("q_A: ", q_A[maxIndex])
print("prob: ", probs[maxIndex])
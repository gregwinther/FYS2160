import scipy.misc

def microstates(q, q_A, N_A, N_B):
	omega_A = scipy.misc.comb(q_A+N_A-1,q_A)
	q_B = q - q_A
	omega_B = scipy.misc.comb(q_B+N_B-1,q_B)
	omega_tot = omega_A*omega_B
	return q_A, omega_A, q_B, omega_B, omega_tot


q = 6
N_A = 2
N_B = 2
omega_sum = 0

print("{:>5} {:>7} {:>5} {:>7} {:>10}"
.format("q_A", "omega_A", "q_B", "omega_B", "omega_tot"))
for q_A in range(0,q+1):
	q_A, omega_A, q_B, omega_B, omega_tot \
	= microstates(q, q_A, N_A, N_B)
	print("{:>5} {:>7} {:>5} {:>7} {:>10}" \
		.format(q_A, omega_A, q_B, omega_B, omega_tot))
	omega_sum += omega_tot

print("{:>28}{:>10}".format("Sum:",omega_sum))
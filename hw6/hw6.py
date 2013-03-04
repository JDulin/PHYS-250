#
# John Dulin
# March 2013
# PHYS 250
# Computational Methods in Physics
# Prof. Craig Copi
# Linear Algebra
#

def thomas( a, b, c, beta):
	""" Tridiagonal matrix (Thomas) algorithm implementation to solve tridiagonal systems of linear equations.
	(Problem 4 on HW) """
	try:
		c[0]    /= b[0]
		beta[0] /= b[0]
	except ValueError:
		print "b[0] is 0, Divide by zero!"
		
	n = len(beta) 

	c += [0] 
	for i in xrange(n)
		divide   = b[i] - (a[i-1] * c[i-1])
	        c[i]    /= divide
		beta[i]  = (beta[i] - a[i-1] * beta[i-1]) / divide
		
	x = np.zeros(n) 
	x[n-1] = beta[n-1]
	for i in reversed(xrange(n-1)):
	        x[i] = beta[i] - c[i] * x[i+1]
				 
	return x




def two():
	A 	   = np.array([[4, -7, 3], [1, 3, -3], [3, -29, 21]])
	b 	   = np.array([-1, -2, 8])
	solutions  = la.solve(A,b)
	print(solutions)
	print(np.dot(A, solutions) == b)   # Verify the correctness of solutions.

	decomp = la.lu(A)
	U      = decomp[2]
	print(decomp)
	print(U)

def three():
	r1, r6, r7 = 2, 2, 2
	r2, r4     = 3, 3
	r3	   = 5
	r5	   = 4
	r8	   = 1
	A	   = np.array([[r1+r2,r3,0,0,0],[r1+r2,0,r4+r5,r6,0],[r1+r2,0,r4+r5,0,r7+r8],[1,-1,-1,0,0],[0,0,1,-1,-1]])
	b	   = np.array([6,6,6,0,0])
	solutions  = la.solve(A,b)
	print(solutions)
	print(np.dot(A, solutions) == b)

if __name__ == "__main__":
	import numpy as np
	import scipy.linalg as la
	two()

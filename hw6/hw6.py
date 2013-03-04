#
# John Dulin
# March 2013
# PHYS 250
# Computational Methods in Physics
# Prof. Craig Copi
# Linear Algebra
#

def thomas():
	""" Thomas algorithm implementation to solve tridiagonal systems of linear equations. (Problem 4 on HW) """


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
	three()

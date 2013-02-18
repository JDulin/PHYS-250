#
# John Dulin
# February 2013
# PHYS 250: Computational Methods in Physics
# Prof. Craig Copi
# Homework 4
# Integration
#


def f3(x):
	return math.sqrt(2 - math.cos(x)**2)

def three():
	domain = [x for x in xrange(0,49)]

	print("Romberg Integration Value")
	print("-------------------------------")
	print(integrate.romberg(f3, 0, 48, show=True))
	print("Incomplete Elliptic Integral of the Second Kind")
	print("-------------------------------")

	plt.plot(domain, [f3(x) for x in domain])



if __name__ == '__main__':
	import matplotlib.pyplot as plt
	import math
	import scipy.special as spec
	import scipy.integrate as integrate

	three()

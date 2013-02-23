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
	domain = np.linspace(0,48,1000)

	print("Romberg Integration Value")
	print("-------------------------------")
	print(integrate.romberg(f3, 0, 48, show=True))
	print("Rombert Integration Value over single period plus change")
	print("-------------------------------")
	print((15 * integrate.romberg(f3, 0, math.pi, show=True)) + integrate.romberg(f3, 15*math.pi, 48, show=True))

	plt.plot(domain, [f3(x) for x in domain])
	plt.xlabel("Domain")
	plt.ylabel("Function value")


if __name__ == '__main__':
	import numpy as np
	import matplotlib.pyplot as plt
	import math
	import scipy.special as spec
	import scipy.integrate as integrate

	three()

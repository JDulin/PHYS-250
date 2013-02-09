#
# John Dulin
# February 2012
# PHYS 250: Computational Methods in Physics
# Prof. Craig Copi
# Lab 3
# Derivation
#

def forward_diff(v, x, h):
	""" Forward differencing method to find the derivative with respect to v at x of the Bessel function """
	return (spec.jv(v + h, x) - spec.jv(v, x)) / h

def center_diff(v, x, h):
	""" Center differencing function to find the derivative with respect to v at x of the Bessel function. """
	return (spec.jv(v + h, x) - spec.jv(v - h, x)) / (2 * h)

def bessel_derivative(x):
	""" The true value of the derivative of the bessel function at x. """
	return (2 / math.pi) * spec.y0(x)  # y0 is the Bessel function of the second kind of order 0 at x.

def one_a():
	""" Estimates the derivative using forward and center differencing, calculates error. """
	# Default x = 1.5, h = 0.5
	print "Forward diff estimation: " +  str(forward_diff(0, 1.5, 0.5))
	print "Error: " + str(forward_diff(0, 1.5, 0.5) / bessel_derivative(1.5))
	print "Center diff estimation: " +  str(center_diff(0, 1.5, 0.5))
	print "Error: " +  str(center_diff(0, 1.5, 0.5) / bessel_derivative(1.5))

# def one_b():


if __name__ == "__main__":
	import math
	import scipy.special as spec
	import richardson_center as richardson

	one_a()



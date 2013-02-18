#
# John Dulin
# February 2013
# PHYS 250: Computational Methods in Physics
# Prof. Craig Copi
# Homework 3
# Derivation
#


def center_diff(func, x, h):
	return (func(x + h) - func(x - h)) / (2 * h)

def forward_diff(func, x, h):
	return (func(x + h) - func(x)) / h

def relative_err(est, true):
	abs(1 - est / true)

def absolute_err(est, true):
	abs(est - true)

def find(estimates, true):
	""" Counts the number of iterations a Richardson Extrapolated algorithm takes to converge to 10^-7 accuracy. """
	for est in estimates:
 		if absolute_err(est, true) < 10E-7 and est != 0.0:
			return est

def search(estimates, true):
	""" Searches for the most accurate estimate and returns the number of its iterations. (Minimum error) """
	best = 1
	itr  = 0
	for est in estimates:
		itr += 1
		if (absolute_err(est, true) < best) and (est != 0.0):
			best = est	

	return (itr, best)


def one():
	""" Solutions to problem 1. """
	true = 0.621609968270664
	print(str(relative_err(center_diff(math.sin, 0.9, 10E-5), true)))
	print(str(relative_err(center_diff(math.sin, 0.9, 10E-6), true)))
	print(str(relative_err(center_diff(math.sin, 0.9, 10E-7), true)))
	print(str(relative_err(center_diff(math.sin, 0.9, 10E-8), true)))

	# dx     = np.arange(10E-4, 10E-8, 100)
	# slopes = list
	# errors = list
	#
	#for h in dx: 
	#	slopes.append(center_diff(math.sin, 0.9, h))
	#for slope in slopes:
	#	errors.append(relative_err(slope, true)
	#semilogy(dx, errors)
	
def three():
	""" Solutions to problem 3. """
	true = 2.30753
	x = 1.05
	h = 0.4
	n = 8
	func = lambda x: math.sin(x) * 2**x
	forward = richardson.richardson_forward(func, x, h, n)
	center = richardson.richardson_center(func, x, h, n)
	forward_est = forward.diagonal()
	center_est  = center.diagonal()
	f_best = search(forward_est, true)
	c_best  = search(center_est, true)

	print("The forward differencing best estimate is {0}.".format(f_best[1]))
	print("The center differencing best estimate is {0}.".format(c_best[1]))
	print("The error in forward differencing is {0}.".format(absolute_err(f_best[1], true)))
	print("The error in center differencing is {0}.".format(absolute_err(c_best[1], true)))
	print("Forward differencing iterations to compute f(z) to an accuracy of 10^-7 is {0}".format(find(forward_est, true)))
	print("Center differencing iterations to computer f(z) to an accuracy of 10^-7 is {0}.".format(find(center_est, true)))
	print(forward)
	print(forward_est)
	print(center)
	print(center_est)

	n = 40
	
	forward = richardson.richardson_forward(func, x, h, n)
	center = richardson.richardson_center(func, x, h, n)
	forward_est = forward.diagonal()
	center_est  = center.diagonal()
	f_best = search(forward_est, true)
	c_best  = search(center_est, true)

	# vi
	print("The forward minimum error is {0}, found at {1}.".format(absolute_err(f_best[1], true), f_best[0]))
	print("The center minimum error is {0}, found  at {1}.".format(absolute_err(f_best[1], true), f_best[0]))
	# vii
	print(forward)
	print(forward_est)
	print(center)
	print(center_est)

if __name__ == "__main__":
	import math
	import numpy 
	import pylab
	import richardson_extrapolation as richardson

	three()


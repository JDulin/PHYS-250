#
# John Dulin
# February 2013
# PHYS 250
# Computational Methods in Phyiscs
# Prof. Craig Copi
# Homework 5
# Differential Equations
# 
# All equations assume differential equations of the form f(y, t, *args)
#

def f2(y, t):
	""" Solves the system of Problem 2, defined in (ii). """
	b = 0.002
	g = -9.8
	y = y[0]  # Position
	v = y[1]  # Velocity

	dydt = v
	dvdt = -b * v * abs(v)/m
	return [dydt, dvdt]

def f4(y, t):


def rk2(f, y0, t, args = ()):
	""" Second-Order Runge-Kutta Method to solve the differential equation f.
		Returns the array of y values evaluated at the times in the array t. """	
	h	  = 0.005 
	n 	  = 0

	while n <= len(t):
		k1    = h * f(y0[n], t[n])
		k2    = h * f(y0[n] + k1, t[n] + h) 
		ynext =	y0[n] + (k1 + k2 / 2)
		y0.append(ynext)
		n += 1

	return y0

def rk4(f, y0, t, args = ()):
	""" Fourth-Order Runge-Kutta Method to solve the differential equation f. """
	h	  = 0.005
	n	  = 0

	while n <= len(t):
		k1 = h * f(y0[n], t[n])
		k2 = h * f(y0[n] + k1/2, t[n] + h/2) 
		k3 = h * f(y0[n] + k2/2, t[n] + h/2)
		k4 = h * f(y0[n] + k3, t[n] + h)
		ynext = y0[n] + (k1 + 2 * (k2 + k3) + k4)/6
		y0.append(ynext)
		n += 1

	return y0

def two():
	initial   = [0., 8., 9.8]
	times     = np.linspace(0, 5., 1000)
	solutions = scipy.integrate.odeint(f2, initial, times)
	position  = solutions[:,0]
	velocity  = solutions[:,1]
	height    = np.amax(position)

	print("The highest point the projectile reaches is {0} at time {1}".format(height, times[np.where(position==height)]))

def four():
	initial  = [1/3]
	times    = np.arange(0., 1., 0.005)
	soln2    = rk2(f4, initial, times)
	soln4    = rk4(f4, initial, times)
	print("The first solution is {0}".format(soln2[39]))
	print("The second solutions is {0}".format(soln4[39]))

if __name__ == "__main__":
	import numpy as np
	import scipy.integrate
	four()


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

def rk2(f, y0, t, args = ()):
	""" Second-Order Runge-Kutta Method to solve the differential equation f.
		Returns the array of y values evaluated at the times in the array t. """	
	h	  = t[1] - t[0] # Runge Kutta has equally spaced points
	n 	  = 1
	solutions = list()

	while n <= len(t):
		k1    = h * f(y0[n], t[n])
		k2    = h * f(y0[n] + k1, t[n] + h) 
		ynext =	y0[n] + (k1 + k2 / 2)
		solutions.append(ynext)
		n += 1

	return solutions

def rk4(f, y0, t, args = ()):
	""" Fourth-Order Runge-Kutta Method to solve the differential equation f. """
	h	  = t[1] - t[0] # Runge Kutta has equally spaced points
	n	  = 1
	solutions = list()

	while n <= len(t):
		k1 = h * f(y0[n], t[n])
		k2 = h * f(y0[n] + k1/2, t[n] + h/2) 
		k3 = h * f(y0[n] + k2/2, t[n] + h/2)
		k4 = h * f(y0[n] + k3, t[n] + h)
		ynext = y0[n] + (k1 + 2 * (k2 + k3) + k4)/6
		solutions.append(ynext)
		n += 1

	return solutions

def four():


if __name__ == "__main__":


#
# John Dulin
# February 2013
# Credit: Prof. (Cobra Commander) Craig Copi
# PHYS 250: Computational Methods in Physics
# Homework and Lab 3
#

def richardson_center(f, z, h, nsteps, args=()) :
    """The derivative f'(z) using Richardson extrapolation and center
    differencing.  Returned is the full table of approximations, Fij for 
    j <= i. The values of Fij for j > i are set to zero.  The final value
    F[-1,-1] should be the most accurate estimate.
    Inputs:
    f : The function for which we are estimate the derivative.
    z : Point at which to evaluate the derivative.
    h : Initial stepsize.
    nsteps : Number of steps to perform.
    args : extra arguments to pass to the function, f."""
    import numpy

    # Create a zero filled table
    F = numpy.zeros((nsteps,nsteps))
    # First column of F is the center differencing estimate
    for j in xrange(nsteps) :
	# center differencing
        F[j,0] = (f(z+h,*args) - f(z-h,*args)) / (2.*h)
        h /= 2.0
    # Now iterate
    fact = 1.0
    for i in xrange(1,nsteps) :
        fact *= 0.25
        for j in xrange(1,i+1) :
		# Center differencing
		F[i,j] = F[i-1,j-1] - (F[i-1,j-1] - F[i,j-1])/ (1-fact)
    return F

def richardson_forward(f, z, h, nsteps, args=()):
    """The derivative f'(z) using Richardson extrapolation and forward
    differencing.  Returned is the full table of approximations, Fij for 
    j <= i. The values of Fij for j > i are set to zero.  The final value
    F[-1,-1] should be the most accurate estimate.
    Inputs:
    f : The function for which we are estimate the derivative.
    z : Point at which to evaluate the derivative.
    h : Initial stepsize.
    nsteps : Number of steps to perform.
    args : extra arguments to pass to the function, f."""
    import numpy


    # Create a zero filled table
    F = numpy.zeros((nsteps,nsteps))
    # First column of F is the center differencing estimate
    for j in xrange(nsteps) :
	# forward differencing
	 F[j,0] = (f((z+h),*args) - f(z,*args)) / h
         h /= 2.0
    for i in xrange(1,nsteps) :
        for j in xrange(1,i+1) :
		# Forward differencing
		F[i,j] = 2 * F[i-1, j-1] - F[i, j-1]
    return F

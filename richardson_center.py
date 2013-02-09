#
# Credit: Prof. Craig Copi
# PHYS 250: Computational Methods in Physics
#

def richardson_center (f, z, h, nsteps, args=()) :
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

    # Create a zero filled table
    F = zeros ((nsteps,nsteps))
    # First column of F is the center differencing estimate
    for j in xrange(nsteps) :
        F[j,0] = (f(z+h,*args) - f(z-h,*args)) / (2.*h)
        h /= 2.0
    # Now iterate
    fact = 1.0
    for i in xrange(1,nsteps) :
        fact *= 0.25
        for j in xrange(1,i+1) :
            F[i,j] = F[i-1,j-1] - (F[i-1,j-1] - F[i,j-1])/ (1-fact)
    return F

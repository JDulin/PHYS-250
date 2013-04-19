#
# John Dulin
# April 2013
# PHYS 250
# Computational Methods in Phyiscs
# Prof. Craig Copi
# Homework 10
# Curve Fitting
 

def linear_leastsq(x, y, sigma = None):
    """ Returns a1, a2, should include sigma_a1, sigma_a2 """
    
    if sigma is None:
        sigma = np.ones_like(y)
    else:
        sigma = y.copy.fill(sigma)

    N     = length(x)

    Sx    = sum(x)
    Sy    = sum(y)
    Sxy   = sum(x*y)
    Sxx   = sum(x**2)
    Delta = N * Sxx - Sx**2
    a1    = (Sxx * Sy - Sx * Sxy) / Delta
    a2    = (N * Sxy - Sx * Sy) / Delta

    return [a1, a2]

def gaussian(A, mu, s):
    return A * exp(-1/2*((x-mu)/s)**2)

def chisq(model, x, y, sigma = None):
    if sigma == None:
        sigma = np.ones_like(y)
    else:
        sigma = y.copy.fill(sigma)

    return sum(((y - model(x, *params) / sigma )**2)

def two():
    x = np.array([-2,-1,0,1,2])
    y = np.array([-4,-7,-3,-3,-2])

    # Line fit, a1 and a2
    params = linear_leastsq(x, y)
    print("Parameter a1 is {0}".format(params[0]))
    print("Parameter a2 is {0}".format(params[0]))

    dof       = length(y) - 2   # 'params' from curve fit
    chisq     = sum(((y - model(x, *params) / sigma)**2)
    chisq_red = chisq / dof
    print("Chi-squared: {0}".format(chisq))
    print("Reduced Chi-squared: {0}".format(chisq_red))


def three():
    mu, s = 0, 0
    gauss = np.random.normal(mu, size=10000)

    # Shift the bins to the center 
    shift = (8/51)
    histogram(gauss, bins=51, range=(-4.0,4.0))j

    # Curve fit to Gaussian
    params, covar = opt.curve_fit(Gaussian, x, gauss)



if __name__ == "__main__":
    import numpy as np
    import scipy.stats as stats
    import scipy.special as spec




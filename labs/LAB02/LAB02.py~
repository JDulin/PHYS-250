# 
# Code Credit to Lucas Flowers
#

###### Initialization ######

import scipy.optimize as opt
import scipy.interpolate as interpol

###### Definitions ######

e   = 0.01671123    # Eccentricity
tau = 365.25636     # Period
period = tau        #
w   = 2 * pi / tau  # Something
    
###### Graph 0 ######

def graph0():

    theta_in = linspace(0, 2 * pi, 360) # Theta input to t_theta
    t_out    = t_theta(theta_in)        # The t values for each theta_in

    # Calculate inverse function of t_theta. That is, calculate theta_t
    theta_t  = interpol.InterpolatedUnivariateSpline(t_out, theta_in)

    t_in      = linspace(0, period, 5000) # Prepare an array of time input values
    ang_out0  = zeros_like(t_in)          # Prepare an array to hold the first calculation of angular velocities

    # Fill ang_out with the derivative values of theta_t at each time in t_in
    for i in xrange(len(t_in)):
        ang_out0[i] = theta_t.derivatives(t_in[i])[1]

    # Plot the graph
    # plot(t_in, ang_out0)
    
    return (t_in, ang_out0)

# Time t in terms of theta.
def t_theta(theta):
    y = sqrt(1 - e) * tan(theta / 2)
    x = sqrt(1 + e)
    return tau / (2 * pi) * (2 * arctan2(abs(y), sign(y) * abs(x)) - e * sqrt(1 - e ** 2) * sin(theta) / (1 + e * cos(theta)))
    
###### Graph 1 ######

def graph1():

    psi_in = linspace(0, 2 * pi, 360) # Psi input to t_psi
    t_out  = t_psi(psi_in)            # The t values for each psi_in
    
    theta_arr = zeros_like(psi_in)    # Contains values of theta for each psi_in
    
    # Fill the first half of the array
    for i in xrange(len(psi_in) / 2):
        theta_arr[i] = arccos((cos(psi_in[i]) - e) / (1 - e * cos(psi_in[i])))
        
    # Fill the second half of the array
    for i in xrange(len(psi_in) / 2, len(psi_in)):
        theta_arr[i] = 2 * pi - arccos((cos(2 * pi - psi_in[i]) - e) / (1 - e * cos(2 * pi - psi_in[i])))
    
    # Now we have an array of theta values, and an array of psi values.
    
    # Find a spline of theta as a function of time
    theta_t = interpol.InterpolatedUnivariateSpline(t_psi(psi_in), theta_arr)
    
    t_in      = linspace(0, period, 5000) # Prepare an array of time input values
    ang_out1  = zeros_like(t_in)          # Prepare an array to hold the first calculation of angular velocities

    # Fill ang_out with the derivative values of theta_t at each time in t_in
    for i in xrange(len(t_in)):
        ang_out1[i] = theta_t.derivatives(t_in[i])[1]
    

    # Plot the graph
    # plot(t_in, ang_out1)
    
    return (t_in, ang_out1)
    
def t_psi(psi):
    return (psi - e * sin(psi)) / w

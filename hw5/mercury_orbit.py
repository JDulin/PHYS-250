#
# Sample Code
# PHYS 250
# Computational Methods in Physics
# Credit: Prof. Craig Copi
#

import scipy.integrate as integ

# GM for the Sun.  Make it a global because I am lazy.
GM = 6.67e-11 * 1.99e30

def gravity_force_2d (y, t, eta=0) :
    """Newton's gravitational force in a plane.  An optional "fifth force"
    is parameterized through eta.  Choose the following order for y:
    y[0] : x coordinate
    y[1] : y coordinate
    y[2] : vx
    y[3] : vy
    All quantities are given in SI units.
    """
    # Radial distance
    r = norm(y[:2])
    # Shorthand
    rvec = y[:2]
    # output
    dydt = zeros_like(y)
    dydt[:2] = y[2:] # Copy the velocities
    # For dv/dt we use the force
    dydt[2:] = (-GM + eta/r)/r**3*rvec
    return dydt

# Mercury orbit
# Semi-major axis
a = 5.7909100e10 # m
# eccentricity
e = 0.205630
# Period
period = 87.9691 * 24*3600 # seconds
# Perihelion distance
rp = (1-e)*a
# Perihelion speed
vp = a*2*pi/period*sqrt((1+e)/(1-e))

# Initial conditions: start at perihelion:
#  position (rp,0), velocity (0,vp)
y0 = zeros(4)
y0[0] = rp
y0[3] = vp

# Integrate for a few orbits
t = linspace (0, 3*period, 3000)
res = integ.odeint (gravity_force_2d, y0, t)

# Now include a perturbation.
# This value is consistent with the anomalous precession of Mercury
eta = GM * a * 7e-8
# But that is impossible to see in our plot as it requires centuries of
# orbits to be large enough.  Thus we scale this by a large factor.
eta *= 5e5

res_perturbed = integ.odeint (gravity_force_2d, y0, t, args=(eta,))

# Now make a nice plot
figure(1)
clf()
axhline(0, color='k')
axvline(0, color='k')
plot (res[:,0], res[:,1], 'k-', lw=2, label='Newtonian Gravity')
plot (res_perturbed[:,0], res_perturbed[:,1], 'r--', lw=2, label='Perturbed Gravity')

xlabel('x position (m)')
ylabel('y position (m)')
title ('Orbit of Mercury')
minorticks_on()
#legend (loc='best')
legend (loc='center')
# Tweak the ylimits.  Average the max and min and use this instead.
yl = ylim()
ymax = 0.5*(yl[1]-yl[0])
yl=ylim(-ymax,ymax)

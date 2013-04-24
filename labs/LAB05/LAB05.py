#
# Code Credit to Lucas Flowers
#

import scipy.integrate as s

def baseball_force(y, t, omegavec):
    """
    PARAMETERS
    y[:2]       == Position vector
    y[3:]       == Velocity vector
    t           == Time to find acceleration at
    
    KEYWORDS
    omegavec    == Angular velocity
    
    RETURNS
    The array a where
    a[:2]       == Derivative of position (velocity)
    a[3:]       == Derivative of velocity (acceleration)
    """
    
    # Constants. All units in MKS.
    #       Value                 Type
    #       ----------------      ------------
    vd    = 35.                 # Velocity
    delta = 5.                  # Velocity
    B     = 4.1 * 10. ** (-4.)  # Unitless
    g     = 9.8                 # Acceleration
    zhat  = array([0., 0., 1.]) # Unit vector
    
    # Variables
    rvec = y[:2]        # Position vector
    vvec = y[3:]        # Velocity vector
    vmag = norm(vvec)   # Velocity magnitude
    
    # Acceleration
    avec = -(0.0039 + 0.0058 / (1. + exp((vmag - vd) / delta))) * vmag * vvec \
            + B * cross(omegavec, vvec) \
            - g * zhat

    return append(vvec, avec)
    
##### All units MKS unless otherwise specified. #####

##### Pitch Name: Slider #####
# Name  Value                     Units         Value in old units
#-----  ---------------------     ----------    ------------------
vmag0 = 38.                     # m/s           (85 mph)
theta = pi / 180.               # radians       (1 degree)
spin  = 2. * pi * 1800. / 60.   # radians/s     (1800 rpm)
phi   = 0.                      # radians       (0 degrees)

##### Unit Vectors #####
xhat, yhat, zhat = array([1., 0., 0.]), array([0., 1., 0.]), array([0., 0., 1.])

##### Initial Conditions #####
# Initial velocity
vvec0 = vmag0 * (xhat * cos(theta) + zhat * sin(theta))
# Initial position
rvec0 = 0. * xhat + 0. * yhat + 0. * zhat
y0 = append(rvec0, vvec0)

##### Times to Analyze (seconds) #####
t = arange(0., 1., 0.001)

##### baseball_force's omegavec argument #####
omegavec = spin * (yhat * sin(phi) + zhat * cos(phi))

##### Perform integrate.odeint #####
arr = s.odeint(baseball_force, y0, t, args = (omegavec,), full_output = 1)[0]

### Get position and velocity values for each axis ###
rx = arr[::, 0]
ry = arr[::, 1]
rz = arr[::, 2]
vx = arr[::, 3]
vy = arr[::, 4]
vz = arr[::, 5]

def plot_bball():

    # Unit conversion
    conv = 3.281 # feet == 1 meter
    xfeet = conv * rx
    yfeet = conv * ry
    zfeet = conv * rz

    # Clear plot
    clf()
    
    # Zero Displacement
    plot(xfeet, zeros_like(xfeet), 'black', label = 'Direct Path')
    
    # Vertical/Horizontal Displacements versus Distance
    plot(xfeet, yfeet, 'r-',  label = 'Horizontal Displacement')
    plot(xfeet, zfeet, 'b-', label = 'Vertical Displacement')

    # Home Plate
    plot(60.5, 0, 'gD', label = 'Home Plate')

    # Labels
    xlabel('Distance from Pitcher\'s Mound (ft.)')
    ylabel('Displacements (ft.)')
    title('Horizontal and Vertical Displacements of a Slider\nOff of the Direct Path from the Pitcher\'s Hand to the Home Plate')
    legend(loc = 3)
    
    # Limits
    xlim(0, 62.5)
    ylim(-4, 2)
    
plot_bball()


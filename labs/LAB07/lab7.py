#
# John Dulin and Lucas Flowers
# March 2013
# PHYS 250: Computational Methods in Physics
# Prof. Craig Copi
# Lab 7
# Problem Solving
#

# PART 1A
import urllib
fp = urllib.urlopen('http://www.phys.cwru.edu/courses/p250/data/electron-Fe-scattering.dat')
X = loadtxt(fp)
fp.close()

# PART 1B
angle = X[0]

# PART 1C
fp = urllib.urlopen('http://www.phys.cwru.edu/courses/p250/data/electron-Fe-scattering.dat')
Y = loadtxt(fp, skiprows = 1)
fp.close()

# PART 1D
E           = Y[:, 0]
sigma       = Y[:, 1:-1]
sigma_total = Y[:, -1]

# PART 2A
indE = where(E == 10000)[0][0]

# PART 2B, Trapezoidal Rule
import scipy.integrate as s
angle_rads = angle / 180. * pi
trap_intg = s.trapz(sigma[indE] * sin(angle_rads), angle_rads) * 2 * pi
print('# Trapezoidal Rule: ' + str(trap_intg))
print('# Trapezoidal Error: ' + str(1. - trap_intg / sigma_total[indE]))

# PART 2B, Spline
import scipy.interpolate as interpol
spline_to_integrate = interpol.InterpolatedUnivariateSpline(angle_rads, sigma[indE] * sin(angle_rads) * 2 * pi)
spline_intg = spline_to_integrate.integral(angle_rads[0], angle_rads[-1])
print('# Spline: ' + str(spline_intg))
print('# Spline Error: ' + str(1. - spline_intg / sigma_total[indE]))

# PART 2C
import scipy.optimize as opt
def to_bisect(th0):
    return spline_to_integrate.integral(th0, pi) - 0.01 * spline_to_integrate.integral(0, pi)
th0_rad = opt.bisect(to_bisect, 0, pi)
th0_deg = th0_rad / pi * 180
print('# Angle in Radians: ' + str(th0_rad))
print('# Angle in Degrees: ' + str(th0_deg))

# PART 2D
clf()
rc('font', family='serif')

sigma_smooth = interpol.InterpolatedUnivariateSpline(angle_rads, sigma[indE])
angle_rads_smooth = linspace(0, pi, 1000)
semilogy(angle_rads_smooth, sigma_smooth(angle_rads_smooth), 'b-', label = 'Interpolating Spline of Data')
semilogy(angle_rads, sigma[indE], 'bo', label = 'Raw Data')

fill_between(angle_rads_smooth, sigma_smooth(angle_rads_smooth), yticks()[0][0], where = angle_rads_smooth >= th0_rad, color = 'cyan')
p = plt.Rectangle((0, 0), 0, 0, color = 'cyan', label = 'Region Containing 1% Overall Scattering')
plt.gca().add_patch(p)

xlim(0, pi)
xticks(linspace(0, pi, 10), [int(i) for i in linspace(0, 180, 10)])
xlabel('Scattering Angle (Degrees)')

ylabel(r'Differential Cross Section (cm$^2$)')

title(r'Differential Cross Section for the Elastic Scattering of' '\n' 'Electrons from Iron versus Scattering Angle')
legend()

# Part 3A







#
# Code Credit to Lucas Flowers
#

import scipy.integrate as s
import scipy.special as spec

### Method 1 ###

def s1_integrand(theta, theta_m):
    return 1. / sqrt(cos(theta) - cos(theta_m))
    
def s1_integral(theta_m):
    return s.quad(s1_integrand, 0, theta_m, args = (theta_m,))[0]
    
def f1(theta_m):
    return sqrt(2) / pi * s1_integral(theta_m)
    
### Method 2 ###

def s2_integrand(psi, theta_m):
    return 1. / sqrt(1 - sin(theta_m / 2) ** 2 * sin(psi) ** 2)
    
def s2_integral(theta_m):
    return s.quad(s2_integrand, 0, pi / 2., args = (theta_m,))[0]

def f2(theta_m):
    return 2 / pi * s2_integral(theta_m)

### Method 3 ###
    
def f3(theta_m):
    coeffs = [1. / 4., 9. / 64., 25. / 256., 1225. / 16384.]
    s = 0
    for i in xrange(len(coeffs)):
        s += coeffs[i] * sin(theta_m / 2.) ** (2 * (i + 1))
    s += 1
    return s
  
## Method 4 (True Value) ##

def f4(theta_m):
    return 2. / pi * spec.ellipk(sin(theta_m / 2) ** 2)
    
######### Part 1 #########

tm1 = pi / 180

print('Romberg on Integral 1')
print(sqrt(2) / pi * s.romberg(s1_integrand, 0, tm1, args = (tm1,), show = True))
print('-------------------------------------------------------')

print('Quad on Integral 1')
print(sqrt(2) / pi * s.quad(s1_integrand, 0, tm1, args = (tm1,))[0])
print('-------------------------------------------------------')

print('Romberg on Integral 2')
print(2. / pi * s.romberg(s2_integrand, 0, pi / 2., args = (tm1,), show = True))
print('-------------------------------------------------------')

print('Quad on Integral 2')
print(2. / pi * s.quad(s2_integrand, 0, pi / 2., args = (tm1,))[0])
print('-------------------------------------------------------')

######### Part 2 #########

######### a

# Plot styles
style1 = 'r-.'
style2 = 'b--'
style3 = 'g-'

# Plot labels
label1 = 'Lab Equation 1: Integral over the Angular Amplitude'
label2 = 'Lab Equation 2: Integral with Substitution'
label3 = 'Lab Equation 3: Taylor Series, Truncated to Five Terms'

def pf1():
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    degs = arange(1, 171, 1)
    f1s = zeros_like(theta_ms)
    for i in xrange(len(theta_ms)):
        f1s[i] = f1(theta_ms[i])
    plot(degs, f1s, style1, label = label1)
    
def pf2():
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    degs = arange(1, 171, 1)
    f2s = zeros_like(theta_ms)
    for i in xrange(len(theta_ms)):
        f2s[i] = f2(theta_ms[i])
    plot(degs, f2s, style2, label = label2)
    
def pf3():
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    degs = arange(1, 171, 1)
    f3s = [f3(x) for x in theta_ms]
    plot(degs, f3s, style3, label = label3)
    
def pf4():
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    degs = arange(1, 171, 1)
    plot(degs, f4(theta_ms))

def plots1():
    clf()
    pf1()
    pf2()
    pf3()
    xlabel('Maximum Angular Displacement, in Degrees')
    ylabel('Period, Normalized by the Period of a Pendulum with Small Amplitude')
    xlim(1, 170)
    ylim(ymin = 1)
    legend(loc = 2)
    title('Three Methods of Calculating the Period of a Pendulum\nAs a Function of Maximum Angular Displacement from Equilibrium')
    
######### b

def p2f1():
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    degs = arange(1, 171, 1)
    f1s = zeros_like(theta_ms)
    for i in xrange(len(theta_ms)):
        f1s[i] = f1(theta_ms[i])
    semilogy(degs, abs(1 - f1s / f4(theta_ms)), style1, label = label1)
    
def p2f2():
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    degs = arange(1, 171, 1)
    f2s = zeros_like(theta_ms)
    for i in xrange(len(theta_ms)):
        f2s[i] = f2(theta_ms[i])
    semilogy(degs, abs(1 - f2s / f4(theta_ms)), style2, label = label2)
    
def p2f3():
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    degs = arange(1, 171, 1)
    f3s = [f3(x) for x in theta_ms]
    plot(degs, abs(1 - f3s / f4(theta_ms)), style3)
   
def plots2():
    clf()
    p2f1()
    p2f2()
    xlabel('Maximum Angular Displacement, in Degrees')
    ylabel('Relative Error')
    xlim(1, 170)
    legend(loc = 0)
    title('Relative Error of Two Methods Compared with the True Value of the Period of a Pendulum\nAs a Function of Maximum Angular Displacement from Equilibrium')
   
def findWhenError(isThisValue):
    theta_ms = arange(pi / 180, pi * 170 / 180., pi / 180)
    for i in xrange(len(theta_ms)):
        if abs(1 - f3(theta_ms[i]) / f4(theta_ms[i])) >= isThisValue:
            return theta_ms[i]
    return False
   
######### Part 3 #########

theta_m = pi / 180 * 101


print('Quad on Integral 1, 101 Degrees')
a = s.quad(s1_integrand, 0, theta_m, args = (theta_m,), full_output = True)
aa = a[0] * sqrt(2) / pi
print('Error: ' + str(1 - aa / f4(theta_m)))
print('-------------------------------------------------------')

print('Quad on Integral 2, 101 Degrees')
b = s.quad(s2_integrand, 0, pi / 2., args = (theta_m,), full_output = True)
bb = 2. / pi * b[0]
print('Error: ' + str(1 - bb / f4(theta_m)))
print('-------------------------------------------------------')

#
# Code Credit to Lucas Flowers
#

import scipy.linalg as la

############################################# Initial Values ####################

length = 1.
steps = 1001
x_steps = steps
t_steps = steps

dt = 10 ** (-4)       ; ts = array([n * dt for n in xrange(t_steps)])
dx = length / x_steps ; xs = linspace(0, length, x_steps)

r = dt / dx ** 2

############################################# True  Solution ####################

def Txt(x, t):
    return exp(-pi ** 2 * t) * sin(pi * x)
    
def T0(xs):
    return Txt(xs, 0)
    
def true_T(xs, ts):
    x_steps, t_steps = len(xs), len(ts)
    Ts = zeros((t_steps, x_steps))
    
    for index_t in xrange(t_steps):
        for index_x in xrange(x_steps):
            Ts[index_t, index_x] = Txt(xs[index_x], ts[index_t])
            
            
    return Ts
    
############################################# Fake  Solution ####################

def make_ab(r):
    a = zeros(t_steps) ; a[:-1] = -r
    b = zeros(t_steps) ; b[::]  =  2 * (1 + r)
    c = zeros(t_steps) ; c[1::] = -r
    return array([c, b, a])

def make_B(r):

    B = zeros((t_steps, t_steps))
    
    B[0][0: 2] = array([2 * (1 - r), r])
    for i in xrange(1, t_steps - 1):
        B[i][i - 1: i + 2] = array([r, 2 * (1 - r), r])
    B[-1][-1: -3: -1] = array([2 * (1 - r), r])
 
    return B
    
def make_right(B, Tj):
    return dot(B, Tj)

def solve_step(ab, B, Tj):
    return la.solve_banded((1, 1), ab, make_right(B, Tj))

def solve_all(ab, B):
    T    = zeros((t_steps, x_steps))
    T[0] = T0(xs)
    for t_index in xrange(1, t_steps):
        T[t_index] = solve_step(ab, B, T[t_index - 1])
    return T

ab = make_ab(r)
B  = make_B (r)
T  = solve_all(ab, B)
Tt = true_T(xs, ts)

#############################################   Checkpoint   ####################

def plot1a():
    
    clf()
    
    t = array([0, 0.025, 0.05, 0.075, 0.1]) / dt
    colors = ['#FF0000', '#BB0000', '#770000', '#550000', '#330000']
    
    for (i, color) in zip(t, colors):
        plot(xs, T[i], label = format(i * dt, '0.3f'), color = color)
    ylim(-0.005, 1.005)
    xlim(-0.005, 1.005)
    
    title('Simulated Temperature versus Position\nAlong an Isolated Rod at Selected Times')
    xlabel('Position as a Fraction of Rod Length')
    ylabel('Temperature as a Fraction of Maximum Initial Temperature')
    legend(title = 'Time Units')
    
def plot2a():

    clf()
    imshow(T)
    
    xticks(xticks()[0], [round(tick, 2) for tick in xticks()[0] * dx])
    yticks(yticks()[0], [round(tick, 2) for tick in yticks()[0] * dt])
    
    xlim(-1, len(T[0]) + 1)
    ylim(0, len(T   ) + 1)
    colorbar().set_label('Temperature as a Fraction of Maximum Initial Temperature')
    
    xlabel('Position as a Fraction of Rod Length')
    ylabel('Time Units')
    
    title('Temperature of an Isolated Rod\nAs a Function of Position and Time') 

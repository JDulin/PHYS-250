import scipy.linalg as la

############################################# Initial Values ####################

length = 1.
x_steps = 101
t_steps = 1001

dt = 2 * 10 ** (-4)   ; ts = array([n * dt for n in xrange(t_steps)])
dx = length / x_steps ; xs = linspace(0, length, x_steps)

r = dt / dx ** 2

############################################# True  Solution ####################

def Txt(x, t):
    return exp(-pi ** 2 * t) * sin(pi * x)
    
def T0(xs):
    T = zeros_like(xs)
    for i in xrange(len(T)):
        if xs[i] == 0.:
            T[i] = 50
        elif xs[i] == 1.:
            T[i] = 200
        else:
            T[i] == 100
    return T
    
def true_T(xs, ts):
    x_steps, t_steps = len(xs), len(ts)
    Ts = zeros((t_steps, x_steps))
    
    for index_t in xrange(t_steps):
        for index_x in xrange(x_steps):
            Ts[index_t, index_x] = Txt(xs[index_x], ts[index_t])
            
            
    return Ts
    
############################################# Fake  Solution ####################

def make_ab(r):

    a = zeros(x_steps) ; a[:-2] = -r
    b = zeros(x_steps) ; b[::]  =  2 * (1 + r)
    c = zeros(x_steps) ; c[2::] = -r
    
    b[0]  = 1
    b[-1] = 1
    
    return array([c, b, a])

def make_B(r):

    B = zeros((x_steps, x_steps))
    
    B[0][0: 2] = array([2 * (1 - r), r])
    for i in xrange(1, x_steps - 1):
        B[i][i - 1: i + 2] = array([r, 2 * (1 - r), r])
    B[-1][-1: -3: -1] = array([2 * (1 - r), r])
 
    return B
    
def make_right(B, Tj):
    
    right = dot(B, Tj)
    
    right[0] = Tj[0]
    right[-1] = Tj[-1]
    
    return right

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
    
    t = array([0, 0.01, 0.025, 0.05, 0.2]) / dt
    colors = ['#FF0000', '#BB0000', '#770000', '#550000', '#330000']
    
    for (i, color) in zip(t, colors):
        plot(xs, T[i], label = format(i * dt, '0.3f'), color = color)
    ylim(-0.5, 200)
    xlim(-0.005, 1.0005)
    
    title('Simulated Temperature versus Position\nAlong a Rod Heated at the Endpoints at Selected Times')
    xlabel('Position as a Fraction of Rod Length')
    ylabel('Temperature Units')
    legend(title = 'Time Units', loc = 0)
    
def plot2a():

    clf()
    imshow(T, aspect = 'auto')
    
    xticks(xticks()[0], [round(tick, 1) for tick in xticks()[0] * dx])
    yticks(yticks()[0], [round(tick, 2) for tick in yticks()[0] * dt])
    
    xlim(0, len(T[0]) - 1)
    ylim(0, len(T   ) + 1)
    colorbar().set_label('Temperature Units')
    
    xlabel('Position as a Fraction of Rod Length')
    ylabel('Time Units')
    
    title('Temperature of a Rod Heated at the Endpoints\nAs a Function of Position and Time') 
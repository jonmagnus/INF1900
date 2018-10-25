from matplotlib.pylab import *

v0 = float(raw_input('v0=? '))
g = 9.81

def f(x):
	return v0*x - .5*g*x**2

t = linspace(0,2*v0/g,101)
y = f(t)

xlabel('time (s)')
ylabel('height (m)')

plot(t,y)
show()

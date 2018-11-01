from matplotlib.pylab import *

v0 = float(raw_input('v0=? '))
g = 9.81

def f(x):
	return v0*x - .5*g*x**2

t = linspace(0,2*v0/g,101)
y = f(t)

xlim(t[0],t[-1])
diff_ = max(y) - min(y)
ylim(min(y) - .1*diff_, max(y) + .1*diff_)

xlabel('time (s)')
ylabel('height (m)')

plot(t,y)
show()

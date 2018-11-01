from matplotlib.pylab import *

g = 9.81
y0 = float(raw_input('y0=?\t'))
theta = float(raw_input('theta=?\t'))
v0 = float(raw_input('v0=?\t'))

f = lambda x: x*tan(theta) - 1/(2*v0*v0) * g*x*x/(cos(theta)**2) + y0

cur_x = 0
dx = 1e-2

x = []
y = []
while f(cur_x) >= 0:
	x.append(cur_x)
	y.append(f(cur_x))
	cur_x += dx

xlabel('x-pos (m)')
ylabel('y-pos (m)')

plot(x,y)
show()

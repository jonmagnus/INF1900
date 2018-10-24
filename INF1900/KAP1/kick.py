from math import pi

g = 9.81	# m s^-2
rho = 1.2	# kg m^-3
a = .11		# m
A = pi*a*a	# m^2
m = 0.43	# kg
CD = .4
V = 30		# km h^-1

V /= 3.6	# Unit convert to m s^-1

Fg = m*g
Fd = .5*CD*rho*A*V*V

print 'Fg = %.2f\nFd = %.2f' % (Fg,Fd)

v_0 = 10.
g = 9.81

n = 100

using_while = True

if not using_while:
	for i in range(0,n + 1):
		t = 2.*v_0/g*(float(i)/n)
		y = v_0*t - 0.5*g*t*t
		print '%.2f\t%.2f' %(t,y)

t = 0
t_end = 2.*v_0/g
dt = 2.*v_0/g/n

if using_while:
	while t <= t_end:
		y = v_0*t - 0.5*g*t*t
		print '%.2f\t%.2f' %(t,y)
		t += dt


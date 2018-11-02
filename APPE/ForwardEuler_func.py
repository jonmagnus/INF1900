import numpy as np

def ForwardEuler(f,U0,T,n):
	"""Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
	t = np.zeros(n+1)
	u = np.zeros(n+1)	# u[k] is the solution at time t[k]
	u[0] = U0
	t[0] = 0
	dt = T/float(n)
	for k in range(n):
		t[k+1] = t[k] + dt
		u[k+1] = u[k] + dt*f(u[k],t[k])
	return u,t

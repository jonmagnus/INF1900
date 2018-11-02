import numpy as np

def RK4(f,U0,T,n):
	"""Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
	t = np.zeros(n+1)
	u = np.zeros(n+1)	# u[k] is the solution at time t[k]
	u[0] = U0
	t[0] = 0
	dt = T/float(n)
	for k in range(n):
		t[k+1] = t[k] + dt

		K1 = dt*f(u[k],t[k])
		K2 = dt*f(u[k] + .5*K1,t[k] + .5*dt)
		K3 = dt*f(u[k] + .5*K2,t[k] + .5*dt)
		K4 = dt*f(u[k] + K3,t[k] + dt)

		u[k+1] = u[k] + (K1 + 2*K2 + 2*K3 + K4)/6.
	return u,t

u,t = RK4(lambda y,x: 2*x,0,4,1000)

import matplotlib.pyplot as plt
plt.plot(t,u)
plt.plot(t,np.array(t)**2)
plt.show()

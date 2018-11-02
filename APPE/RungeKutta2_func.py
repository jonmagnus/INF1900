import matplotlib.pyplot as plt
import numpy as np

def RungeKutta2(f,U0,T,n):
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
		u[k+1] = u[k] + K2
	return u,t


n = [10*i for i in range(1,100)]
error = [0]*len(n)
for i in range(len(n)):
	n_ = n[i]
	u_,t = RungeKutta2(lambda u,t:u,1,2,n_)
	u = np.exp(t)
	error[i] = np.abs(u - u_).max()

plt.semilogy(n,error)
plt.xlabel('error')
plt.ylabel('n')
plt.show()

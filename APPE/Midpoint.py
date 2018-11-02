import matplotlib.pyplot as plt
import numpy as np
from ODESolver import ODESolver
from ForwardEuler_func import ForwardEuler

class Midpoint(ODESolver):
	def advance(self):
		u,t,k,f = self.u,self.t,self.k,self.f
		dt = t[k+1] - t[k]
		u_ = u[k] + dt*f(u[k],t[k])/2
		return u[k] + dt*f(u_,t[k] + dt/2)

n = 15
f = lambda y,x: x*np.cos(x)
mid = Midpoint(f)
mid.set_initial_condition(0)
u_mid, t_mid = mid.solve(np.linspace(0,10,n))

#print u_mid, t_mid
#for p in zip(t_mid,u_mid):
#	print '%12g %12g' % p

u_euler,t_euler = ForwardEuler(f,0,10,n)
t = np.linspace(0,10,n)
u = t*np.sin(t) + np.cos(t) - 1

plt.plot(t_mid,u_mid,label='Midpoint')
plt.plot(t_euler,u_euler,label='ForwardEuler')
plt.plot(t,u,label='Exact')
plt.legend()
plt.show()

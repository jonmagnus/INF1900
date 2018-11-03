import matplotlib.pyplot as plt
import numpy as np
from ODESolver import RungeKutta4

S0,I0,R0 = 1500,1,0
nu = .1
dt = .5
t = np.linspace(0,60,int(60/dt))
beta = 5e-4

def f(u,t):
	S,I,R = u
	S_ = -beta*S*I
	I_ = beta*S*I - nu*I
	R_ = nu*I
	return np.array([S_,I_,R_])

solver = RungeKutta4(f)
solver.set_initial_condition([S0,I0,R0])
u,t_ = solver.solve(t,lambda u,t,k: np.abs(sum(u[k,:]) -\
				    (S0 + I0 + R0)) > 1)
S,I,R = u[:,0],u[:,1],u[:,2]

plt.plot(t_,S,label='S')
plt.plot(t_,I,label='I')
plt.plot(t_,R,label='R')
#plt.plot(t_,R+I+S,label='Sum')
plt.legend()
plt.show()

"""
Decreasing beta to 1e-4 makes S almost not decrease
at all in the 60 days of the simulation
"""

import matplotlib.pyplot as plt
import numpy as np

m = 9.
A = .3
k = 4.
gamma = .15
f = lambda x: A*np.exp(-gamma*x)*np.cos(np.sqrt(k/m)*x)

t = np.zeros(101); y = np.zeros(101)
dt = 25./100.
for i in range(101):
	t[i] = dt*i
	y[i] = f(t[i])

t_ = np.linspace(0,25,101)
y_ = f(t)

plt.plot(t,y,'r-',label='with for-loop')
plt.plot(t_,y_,'g--',label='with linspace')
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()

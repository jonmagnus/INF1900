import matplotlib.pyplot as plt
import numpy as np

g = 9.81
s = 7.9e-2
rho = 1e3
h = 50

c = lambda x: np.sqrt(g*x/2/np.pi*(1 + s*4*np.pi**2/(rho*g*x*x))*np.tanh(2*np.pi*h/x))

lambda_ = np.linspace(1e-3,.1,101)
lambda__ = np.linspace(1,2e3,101)

plt.subplot(2,1,1)
plt.plot(lambda_,c(lambda_))

plt.subplot(2,1,2)
plt.plot(lambda__,c(lambda__))

plt.show()

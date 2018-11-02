import matplotlib.pyplot as plt
import numpy as np
from ForwardEuler_func import ForwardEuler

n = [20,30,35,40,50,100,1000,10000]
x = lambda x,t: np.cos(6*t)/(1 + t + x)

for n_ in n:
	u,t = ForwardEuler(x,0,10,n_)
	plt.plot(t,u,label='n=%d' % n_)

plt.legend()
plt.show()

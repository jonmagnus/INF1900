import matplotlib.pyplot as plt
import numpy as np

p = 5; q = 50
F = 1e6
I = .1

n = 100
index_range = range(0,n + 1)
x = np.zeros(n+1); c = np.zeros(n+1)
x[0] = F; c[0] = p*q/1e4*F

for i in index_range[1:]:
	x[i] = x[i-1] + p*x[i-1]/100. - c[i-1]
	c[i] = c[i-1] + I*c[i-1]/100.
	print x[i], c[i]

plt.subplot(2,1,1)
plt.plot(index_range,x,label='Fortune')
plt.subplot(2,1,2)
plt.plot(index_range,c,label='Consumption')
plt.legend()
plt.show()

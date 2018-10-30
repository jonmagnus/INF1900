import numpy as np
import matplotlib.pyplot as plt

def S(x,n):
	sum_ = np.zeros(len(x),dtype='float')
	for j in range(n+1):
		sum_ += ((-1)**j)*(x**(2*j + 1))/float(np.math.factorial(2*j + 1))
	return sum_

x = np.linspace(0,4*np.pi,1001)
plt.axis([0,4*np.pi,-1.4,1.4])
plt.plot(x,np.sin(x),label='sin')
for n in [1,2,3,6,12]:
	plt.plot(x,S(x,n),label='n=%d' % n)
plt.legend()
plt.show()

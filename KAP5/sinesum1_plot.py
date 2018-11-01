import matplotlib.pyplot as plt
import numpy as np

T = 2*np.pi

def S(t,n):
	sum_ = np.zeros(len(t))
	for i in range(1,n+1):
		sum_ += np.sin(2*(2*i - 1)*np.pi*t/T)/(2*i - 1)
	sum_ *= 4/np.pi
	return sum_


t = np.linspace(0,T,101)

for n in [1,3,20,200]:
	plt.plot(t,S(t,n),label='S(t,%d)' %n)

plt.plot([0,T/2,T/2,T],[-1,-1,1,1],label='exact')
plt.legend()
plt.show()

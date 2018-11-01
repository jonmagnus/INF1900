import matplotlib.pyplot as plt
import numpy as np

def cos_Taylor(x,n):
	s = 0; a = 1
	for j in range(1,n+1):
		s += a
		a *= -x*x/float((2*j - 1)*2*j)
	return s, np.abs(a)

x = np.linspace(0,6*np.pi,101)
y = [cos_Taylor(x_,20)[0] for x_ in x]

plt.plot(x,y)
plt.plot(x,np.cos(x))
plt.ylim(-1.4,1.4)
plt.show()

import numpy as np

x = np.zeros(101); y = np.zeros(101)
dx = 9./100
for i in range(101):
	x[i] = 1 + dx*i
	y[i] = np.log(x[i])

for p in zip(x,y):
	print('%f\t%f' %p)

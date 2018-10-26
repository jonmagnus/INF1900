import numpy as np

x = np.linspace(1,10,101)
y = np.log(x)

for p in zip(x,y):
	print('%f\t%f' %p)

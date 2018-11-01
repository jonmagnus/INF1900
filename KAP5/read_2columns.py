import matplotlib.pyplot as plt

infile = open('read_2columns.dat','r')

x = []; y = []

for line in infile:
	p = line.split()
	x.append(float(p[0]))
	y.append(float(p[1]))

plt.plot(x,y)
plt.show()

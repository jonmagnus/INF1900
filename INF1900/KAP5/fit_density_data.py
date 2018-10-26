import matplotlib.pyplot as plt
import numpy as np
#import sys

#try:			in_name = sys.argv[1]
#except IndexError:	in_name = raw_input('in_name=? ')

def fit(x,y,deg):
	plt.xlabel('Temperature')
	plt.ylabel('Density')
	plt.plot(x,y,'o')
	x_ = np.linspace(min(x),max(x),len(x)*10 + 1)
	for d in deg:
		p = np.polyfit(x,y,d)
		plt.plot(x_,np.polyval(p,x_))



plt.subplot(2,1,1)

infile = open('plot_files/density_water.dat', 'r')

t = []; rho = []

for line in infile:
	if line[0] == '#': continue
	p = line.split()
	if p == []: continue
	t.append(float(p[0]))
	rho.append(float(p[1]))

fit(t,rho,[1,2])

plt.subplot(2,1,2)

infile = open('plot_files/density_air.dat', 'r')

t = []; rho = []

for line in infile:
        if line[0] == '#': continue
        p = line.split()
        if p == []: continue
        t.append(float(p[0]))
        rho.append(float(p[1]))

fit(t,rho,[1,2])
plt.show()


"""
plt.plot(t,rho,'o',label=in_name)
plt.xlabel('Temperature')
plt.ylabel('Density')
plt.legend()
plt.show()
"""

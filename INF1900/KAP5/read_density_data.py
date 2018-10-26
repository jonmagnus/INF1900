import matplotlib.pyplot as plt
import sys

try:			in_name = sys.argv[1]
except IndexError:	in_name = raw_input('in_name=? ')

infile = open(in_name, 'r')

t = []; rho = []

for line in infile:
	if line[0] == '#': continue
	p = line.split()
	if p == []: continue
	t.append(float(p[0]))
	rho.append(float(p[1]))

plt.plot(t,rho,'o',label=in_name)
plt.xlabel('Temperature')
plt.ylabel('Density')
plt.legend()
plt.show()

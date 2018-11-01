from math import pi, log

def egg(M, To=20, Ty=70):
	rho = 1.038
	K = 5.4e-3
	c = 3.7
	Tw = 100

	t1 = (float(M)**(2./3)*c*rho**(1./3))/(K*pi*pi*(4*pi/3)**(2./3))
	t2 = log(.76*float(To - Tw)/(Ty - Tw))
	#print 't1 = %f' % t1
	return t1*t2

temp = [4,25]
size = [47,67]

for T in temp:
	for s in size:
		print 'For an egg of size %d and temperature %d C it takes %.2f seconds to cook' %(s,T,egg(s,T))
"""
print egg(47, 4)
print egg(47, 25)
print egg(67, 4)
print egg(67, 25)
"""

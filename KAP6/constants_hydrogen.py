# -*- coding: utf-8 -*-
infile = open('constants_hydrogen.dat', 'r')

data = {}
for line in infile:
	name_value = line.split(':')
	#name = name_value[0]
	symb = name_value[1].split()[0]
	value = eval(name_value[1].split()[1])
	data[symb] = value

k_e = data['k_e']
m_e = data['m_e']
e = data['e']
hbar = data['hbar']

print k_e, m_e, e, hbar

E = -k_e**2*m_e*e**4/(2*hbar**2)

print E

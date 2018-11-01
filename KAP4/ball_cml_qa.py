import sys
g = 9.81
try:
	v0 = float(sys.argv[1])
except IndexError:
	v0 = float(raw_input('v0=? '))
try:
	t = float(sys.argv[2])
except IndexError:
	t = float(raw_input('t=? '))
y = v0*t - .5*g*t**2
print y

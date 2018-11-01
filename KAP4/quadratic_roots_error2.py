import sys
from math import sqrt

try:			a = float(sys.argv[1])
except IndexError:	a = float(raw_input('a=? '))
try:                    b = float(sys.argv[2])
except IndexError:      b = float(raw_input('b=? '))
try:                    c = float(sys.argv[3])
except IndexError:      c = float(raw_input('c=? '))

if b*b - 4*a*c < 0:
	print 'Invalid input: trying to evaluate root of negative number'
	sys.exit(1)
print 'x+ = %g\nx- = %g' %((b + sqrt(b*b - 4*a*c))/(2*a), (b - sqrt(b*b - 4*a*c))/(2*a))

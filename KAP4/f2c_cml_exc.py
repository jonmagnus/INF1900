import sys
try:
	F = float(sys.argv[1])
except:
	print 	'You failed to provide Celsius degree as input '\
		'on the command line!'
	sys.exit(1)
C = 5*(F - 32)/9.
print C

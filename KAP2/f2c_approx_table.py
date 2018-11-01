F = 0
dF = 10

while F <= 100:
	C = 5*(F - 32)/9.
	C_ = (F - 30)/2.
	print '%.1f\t%.1f\t%.1f' % (F,C,C_)
	F += dF

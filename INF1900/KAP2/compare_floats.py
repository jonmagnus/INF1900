a = 1/947.*947
b = 1
if a != b:
	print 'Wrong result!'

tol = 1e-9
if abs(a - b) < tol:
	print 'They are almost equal'

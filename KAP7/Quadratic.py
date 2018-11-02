import numpy as np

class Quadratic:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

	def __call__(self,x):
		return self.a*x**2 + self.b*x + self.c

	def value(self,x): return self(x)

	def table(self,L,R,n):
		x = linspace(L,R,n)
		s = ''
		for x_ in x:
			y = self(x_)
			s += '%12g %12g\n' % (x_,y)
		return s

	def roots(self):
		D = self.b**2 - 4*self.a*self.c
		if D < 0:	return []
		if D == 0:	return [-.5*self.b/self.a]
		return sorted([(-self.b + k*np.sqrt(D))/(2*self.a) for k in [-1,1]])

def test_Quadratic():
	q1 = Quadratic(1,2,1)
	q2 = Quadratic(1,2,2)
	q3 = Quadratic(1,0,-1)

	#print q1.roots(), q2.roots(), q3.roots()

	x = [-2,-1,0,1,2]
	assert 	[q1.value(x_) for x_ in x] == [1,0,1,4,9] and \
		[q2.value(x_) for x_ in x] == [2,1,2,5,10] and \
		[q3.value(x_) for x_ in x] == [3,0,-1,0,3], \
		'Quadratic.value does not calculate values correctly'

	assert 	q1.roots() == [-1] and \
		q2.roots() == [] and \
		q3.roots() == [-1,1], \
		'Quadratic.roots does not calculate roots correctly'



test_Quadratic()

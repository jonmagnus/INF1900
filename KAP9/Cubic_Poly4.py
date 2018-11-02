import numpy as np

class Parabola:
	def __init__(self,c0,c1,c2):
		self.c0 = c0
		self.c1 = c1
		self.c2 = c2

	def __call__(self,x):
		return self.c2*x**2 + self.c1*x + self.c0

	def table(self,L,R,n):
		s = ''
		for x in np.linspace(L,R,n):
			y = self(x)
			s += '%12g %12g\n' % (x,y)
		return s

class Cubic(Parabola):
	def __init__(self,c0,c1,c2,c3):
		Parabola.__init__(self,c0,c1,c2)
		self.c3 = c3

	def __call__(self,x):
		return self.c3*x**3 + Parabola.__call__(self,x)

class Poly4(Cubic):
	def __init__(self,c0,c1,c2,c3,c4):
		Cubic.__init__(self,c0,c1,c2,c3)
		self.c4 = c4

	def __call__(self,x):
		return self.c4*x**4 + Cubic.__call__(self,x)

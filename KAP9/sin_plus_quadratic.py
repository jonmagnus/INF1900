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

class F(Parabola):
	def __init__(self,A,w,a,b,c):
		self.A = A
		self.w = w
		Parabola.__init__(self,a,b,c)

	def __call__(self,x):
		return self.A*np.sin(self.w*x) + Parabola.__call__(self,x)


p = F(1,np.pi,0,0,1)
print p.table(0,10,101)

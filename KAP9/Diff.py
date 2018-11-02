class Diff:
	def __init__(self,f,h=1e-5):
		self.f = f
		self.h = float(h)

class Forward1(Diff):
	def __call__(self,x):
		f,h = self.f,self.h
		return (f(x+h) - f(x))/h

class Backward1(Diff):
	def __call__(self,x):
		f,h = self.f,self.h
		return (f(x) - f(x-h))/h

class Central2(Diff):
	def __call__(self,x):
		f,h = self.f,self.h
		return (f(x+h) - f(x-h))/(2*h)

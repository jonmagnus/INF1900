from numpy import exp, sin

class F:
	def __init__(self, a, w):
		self.a = a
		self.w = w

	def __call__(self, x):
		return exp(-self.a*x)*sin(self.w*x)

	def value(self,x): return self(x)

	def __str__(self):
		return 'exp(-a*x)*sin(w*x)'

	__repr__ = __str__

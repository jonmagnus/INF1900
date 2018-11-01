import matplotlib.pyplot as plt
import numpy as np

class Sum:
	def __init__(self, term, M, N):
		self.term = term
		self.M = M
		self.N = N

	def __call__(self,x):
		sum_ = 0
		for k in range(self.M, self.N+1):
			sum_ += self.term(k,x)
		return sum_


def test_Sum():
	S = Sum(lambda k,x: (-x)**k, M = 0, N = 3)
	x = .5
	assert S(x)==0.625, 'Sum was not correcty calculated'
	assert S.term(k=4, x=x)==0.0625, 'A term was not correctly calculated'

test_Sum()

term = lambda k,x: (-1)**k*np.power(x,2*k + 1)/float(np.math.factorial(2*k + 1))
x = np.pi
S = Sum(term,0,50)
print S(x)

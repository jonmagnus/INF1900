class Polynomial:
	def __init__(self, coefficients):
		self.coeff = coefficients

	def __call__(self, x):
		s = 0
		for i in range(len(self.coeff)-1,-1,-1):
			#print i
			s *= x
			s += self.coeff[i]
			#s += self.coeff[i]*x**i
		return s

	def __add__(self, other):
		# Start with the longest list and add in other
		if len(self.coeff) > len(other.coeff):
			result_coeff = self.coeff[:]	# copy!
			for i in range(len(other.coeff)):
				result_coeff[i] += other.coeff[i]
		else:
			result_coeff = other.coeff[:]	# copy!
			for i in range(len(self.coeff)):
				result_coeff[i] += self.coeff[i]
		return Polynomial(result_coeff)

	def __sub__(self, other):
		# Start with the longest list and add in other
		if len(self.coeff) > len(other.coeff):
			result_coeff = self.coeff[:]
			for i in range(len(other.coeff)):
				result_coeff[i] -= other.coeff[i]
		else:
			result_coeff = [-c for c in other.coeff]
			for i in range(len(self.coeff)):
				result_coeff[i] += self.coeff[i]
		return Polynomial(result_coeff)

def test_Polynomial():
	p1 = Polynomial([0,0,1])
	p2 = Polynomial([1,0,1])
	#print [p1(x) for x in [-2,-1,0,1,2]]
	assert [p1(x) for x in [-2,-1,0,1,2]] == [4,1,0,1,4], \
		'Polynomail evaluation not correct'
	p1 = p1 + p2
	#print p1.coeff
	p1 = p1 - p2
	#print p1.coeff
	assert p1.coeff == [0,0,1], 'Polynomial arithmetic is not correct'

test_Polynomial()

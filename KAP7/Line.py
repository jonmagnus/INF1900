class Line:
	def __init__(self,p1,p2):
		self.a = (p1[1] - p2[1])/float(p1[0] - p2[0])
		self.b = p1[1] - self.a*p1[0]

	def __call__(self,x):	return self.a*x + self.b
	def value(self,x):	return self(x)

def test_Line():
	l = Line((0,1),(1,3))

	assert l.a == 2 and l.b == 1, \
		'Line.__init__ does not initialize properly'
	assert [l(x) for x in [-2,-1,0,1,2]] == [-3,-1,1,3,5], \
		'Line.__call__ does not evaluate properly'

test_Line()


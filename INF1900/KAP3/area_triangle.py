
def triangle_area(vertices):
	a,b,c = vertices[0],vertices[1],vertices[2]
	A = 0.5*abs(b[0]*c[1] - c[0]*b[1] - a[0]*c[1] + c[0]*a[1] + a[0]*b[1] - b[0]*a[1])
	return A

def test_triangle_area():
	"""
	Verify the area of a triangle with vertex coordinates
	(0,0), (1,0), and (0,2).
	"""
	v1 = (0,0); v2 = (1,0); v3 = (0,2)
	vertices = [v1,v2,v3]
	expected = 1
	computed = triangle_area(vertices)
	tol = 1e-14
	success = expected - computed < tol
	msg = 'computed area=%g != %g (expected)' % \
		(computed, expected)
	assert success, msg

test_triangle_area()

def area(triangle):
	ax,ay = triangle.get(1,(0,0))
	bx,by = triangle.get(2,(0,0))
	cx,cy = triangle.get(3,(0,0))
	return .5*abs(bx*cy - cx*by - ax*cy + cx*ay + ax*by - bx*ay)

def test_area():
	t1 = {1: (0,0), 2: (1,0), 3:(0,2)}
	success = area(t1) == 1.
	msg = 'Area of triangle (%g) is not correctly calculated' %area(t1)
	assert success, msg

test_area()

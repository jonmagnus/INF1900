from math import sin, pi

def f(x):
	y = sin(x)
	if y < 0:
		y = 0
	return y

def test_f():
	x = [pi/100*i for i in range(100)]
	y = [sin(x_) if sin(x_) > 0 else 0 for x_ in x]
	for p in zip(x,y):
		success = f(p[0]) == p[1]
		msg = 'failed at point %g' % p[0]
		assert success, msg

test_f()

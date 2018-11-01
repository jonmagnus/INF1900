x = x_ = 1

for i in range(15):
	x += x_
	x_ = x - x_
	print x


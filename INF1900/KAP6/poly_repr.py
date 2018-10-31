
def eval_poly_dict(poly,x):
	return sum([poly[p]*x**p for p in poly])

def eval_poly_list(poly,x):
	sum_ = 0
	for p in range(len(poly)):
		if poly[p]: sum_ += poly[p]*x**p
	return sum_

pd = {0: -.5, 100: 2}
pl = [0]*101
pl[0] = -.5; pl[100] = 2

x = [0,1,2,3]
y1 = [eval_poly_dict(pd,x_) for x_ in x]
y2 = [eval_poly_list(pl,x_) for x_ in x]

print y1
print y2

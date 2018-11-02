from Diff import Diff, Backward1
import math

class Backward2(Diff):
	def __call__(self,x):
		f,h = self.f,self.h
		return (f(x-2*h)-4*f(x-h)+3*f(x))/(2*h)

f = lambda x: math.exp(-x)
f_diff = lambda x: -f(x)

t = 0
print '%3s  %12s %12s %12s %12s %12s' % ('k','Original',\
				    'Backward1','Difference',\
				    'Backward2','Difference')
for k in range(15):
	h = 2.**(-k)
	y = f_diff(t)
	y1 = Backward1(f,h)(t)
	y2 = Backward2(f,h)(t)
	print ('%3d:  ' + 5*'%12g ') % (k,y,y1,abs(y-y1),y2,abs(y-y2))

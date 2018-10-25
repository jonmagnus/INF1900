v0 = 10
g = 9.81

n = 100

dt = 2.*v0/g/n

t = [dt*i for i in range(0,n+1)]
y = [v0*i - .5*g*i*i for i in t]

for p in zip(t,y):
	print "%.2f\t%.2f" %p


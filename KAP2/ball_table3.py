v0 = 10
g = 9.81

n = 100

dt = 2.*v0/g/n

t = [dt*i for i in range(n+1)]
y = [v0*i - .5*g*i*i for i in t]

ty1 = [t,y]

print """Content of ty1:
----------
"""
for i in range(n+1):
	print "%.2f\t%.2f" %(ty1[0][i],ty1[1][i])

ty2 = [[t[i],y[i]] for i in range(n+1)]

print """----------
Content of ty2:
---------
"""

for p in ty2:
	print "%.2f\t%.2f" %(p[0],p[1])

print "----------"

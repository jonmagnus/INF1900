from matplotlib.pylab import *

p = 3
L = 1e5
N = 24
x0 = L

y = zeros(N+1)
x = zeros(N+1)
y[0] = 0; x[0] = L
for n in range(1,N + 1):
	y[n] = float(p*x[n-1])/12/100 + float(L)/N
	x[n] = x[n-1] + float(p*x[n-1])/12/100 - y[n]

plot(x,'r')
plot(y,'g')
show()

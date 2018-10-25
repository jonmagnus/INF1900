from matplotlib.pylab import *

a = lambda n: (7 + 1./(n + 1))/(3 - 1./(n + 1)**2)
a_seq = lambda n: [a(i) for i in range(n + 1)]

N = 100
print 'a(%d) = %g\tActual limit = %g' %(N, a(100), 7./3)
# the exact limit of the sequence a_n is 7/3 \approx 2.33

D = lambda n: sin(pow(2,-n))/pow(2,-n)
D_seq = lambda n: [D(i) for i in range(n + 1)]

N = 1000
print 'D(%d) = %g' %(N,D(N))

def D(f,x,N):
	seq = zeros(N + 1)
	for i in range(N + 1):
		h = pow(2,-i)
		seq[i] = (f(x + h) - f(x))/h
	return seq

figure(1)
plot(D(sin,0,80), '.')
show()

figure(2)
plot(D(sin,pi,80), '.')
show()

"""
The program fails for large N becuase h becomes to close to zero,
so the computers precision percieves it as dividing by zero.
"""

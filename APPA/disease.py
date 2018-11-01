import matplotlib.pyplot as plt

N = 50
x = [0]*(N+1)
x[0] = 100; x[1] = 150
x_ = x

for n in range(2,N + 1):
	x[n] = 1./4*x[n-1] + 5./7*x[n-2]
	x_[n] = 1./4*x_[n-1] + 3./4*x_[n-2]

plt.plot(x,label='x_n=1/4 x_{n-1} + 5/7 x_{n-2}')
plt.plot(x_,label='x_')
plt.legend()
plt.show()


N = 50
x_ = 150; x = 100
print '0\t%f' % x
print '1\t%f' % x_
for n in range(2,N+1):
	t = x_
	x_ = .25*x_ + 5./7*x
	x = t
	print '%d\t%f' % (n,x)

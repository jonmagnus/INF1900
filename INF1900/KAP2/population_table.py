from math import exp

n = 100
dt = 48./n

B = 5e4
k = .2
C = 9

t = [dt*i for i in range(n+1)]
N = [B/(1+C*exp(-k*i)) for i in t]

for p in zip(t,N):
	print "%.2f\t%.2f" %p

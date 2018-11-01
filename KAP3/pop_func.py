from math import exp

def population(t,k,B,C):
	return float(B)/(1 + C*exp(-k*t))

B_ = 5e4
k_ = .2
C_ = 9

n = 100
dt = 48./n

t_ = [dt*i for i in range(n+1)]
N = [population(i,k_,B_,C_) for i in t_]

for p in zip(t_,N):
	print '%.2f\t%.2f' %p


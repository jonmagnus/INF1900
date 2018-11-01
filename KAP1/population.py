from math import exp

B = 50000
k = .2		# h^-1
t = 24		# h
C = 9

N = B/(1 + C*exp(-k*t))
print 'The population of bacteria after %d hours is %d if the \
initial population was %d' %(t,N,B/(1 + C))

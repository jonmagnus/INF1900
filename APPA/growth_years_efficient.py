#import matplotlib.pyplot as plt
#import numpy as np

x0 = 100
p = 5
N = 4

# Compute solution
outfile = open('growth_years_efficient.out', 'w')
x = x0
outfile.write('%g\n' % x)
for n in range(N):
	x = x + (p/100.)*x
	outfile.write('%g\n' % x)
print x

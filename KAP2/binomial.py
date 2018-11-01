n = 14
k = 3

p = 1
for j in range(1,n-k+1):
	p *= j + k
	p /= j

print p

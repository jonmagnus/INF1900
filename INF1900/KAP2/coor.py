coords = []
a = 10
b = 20
n = 100
h = float(b - a)/n

for i in range(0,n + 1):
	x = a + i*h
	coords.append(x)

print coords

coords = [a + i*h for i in range(0,n + 1)]

print coords

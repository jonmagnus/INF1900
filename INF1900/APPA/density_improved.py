def read_densities(filename):
	infile = open(filename,'r')
	densities = {}
	for line in infile:
		words = line.split()
		substance = words[:-1]
		density = float(words[-1])

		name = ' '.join(substance)
		densities[name] = density
	return densities

densities = read_densities('density_improved.dat')
for name in densities:
	print name, densities[name]


infile = open('humans.dat', 'r')

header = infile.readline()
i = 0; keys = []
while i < len(header):
	key = ''
	while i < len(header):
		if header[i:i+2] == '  ': break
		key += header[i]
		i += 1
	while i < len(header) and header[i] == ' ': i += 1
	if key != '': keys.append(key)

infile.readline()
infile.readline()

data = {}

for line in infile:
	if line[:5] == '-'*5: break
	i = 0
	species = {}
	name = ''
	"""
	name = ''
	while i < len(line):
		if line[i:i+2] == '  ': break
		value += line[i]
		i += 1
	while i < len(line) and line[i] == ' ':
		i += 1
	"""
	for k in keys:
		value = ''
		while i < len(line):
			if line[i:i+2] == '  ': break
			value += line[i]
			i += 1
		while i < len(line) and line[i] == ' ':
			i += 1
		if value != '':
			print value
			if k == keys[0]:name = value
			else:		species[k] = value
	data[name] = species.copy()

for key in data.keys():
	print key, data[key]


infile = open('f2c_file_read.dat', 'r')
for i in range(3):
	infile.readline()
F =  str(infile.readline()).split()[2]
F = float(F)
C = 5*(F - 32)/9.
print C

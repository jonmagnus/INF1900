infile = open('f2c_file_read_write.dat', 'r')

for i in range(3):
	infile.readline()

outfile = open('f2c_file_read_write.out', 'w')

for line in infile:
	F = str(line).split()[2]
	F = float(F)
	C = 5*(F - 32)/9.
	outfile.write('%.2f\t%.2f\n' %(C,F))

infile.close()
outfile.close()


from random import randint,uniform

def read_write_ball(file):
	infile = open(file,'r')

	v0 = float(infile.readline().split()[1])
	infile.readline()

	t = []
	for line in infile:
		for val in line.split():
			t.append(float(val))

	infile.close()
	return v0, t

def test_read_write_ball():
	v0 = randint(1,11)
	t = [round(uniform(0,1),6) for i in range(20)]

	test_file = 'ball_file_read_write.test.dat'

	outfile = open(test_file, 'w')
	outfile.write('v0: %f\nt:\n' %v0)
	for val in t:
		outfile.write('%f ' %val)
		if randint(0,10) == 0:
			outfile.write('\n')
	outfile.close()

	v0_, t_ = read_write_ball(test_file)

	success = v0 == v0_
	msg = 'v0 is not equal v0_'
	assert success, msg

	for p in zip(t,t_):
		success = p[0] == p[1]
		msg = 't (%f) is not equal t_ (%f)' %p
		assert success, msg

test_read_write_ball()

def pretty_read_write_ball(in_name, out_name):
	v0, t = read_write_ball(in_name)
	g = 9.81

	y = [v0*x - .5*g*x*x for x in t]

	comp = zip(t,y)
	comp.sort()

	outfile = open(out_name, 'w')
	for p in comp:
		outfile.write('%f\t%f\n' %p)
	outfile.close()

pretty_read_write_ball('ball_file_read_write.dat', 'ball_file_read_write.out')

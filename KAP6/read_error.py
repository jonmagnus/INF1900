import matplotlib.pyplot as plt

infile = open('read_error.dat', 'r')

epsilon = []; exact_error = []; n = [];
for line in infile:
	if 'epsilon' not in line: continue
	words = line.split()
	epsilon.append(eval(words[1]))
	exact_error.append(eval(words[4]))
	n.append(eval(words[-1].split('=')[-1]))

plt.semilogy(n,epsilon,label='epsilon')
plt.semilogy(n,exact_error,label='exact error')
plt.legend()
plt.show()

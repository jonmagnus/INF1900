import matplotlib.pyplot as plt
import numpy as np
import shutil, os

def clean_plot(subdir):
	if os.path.isdir(subdir):
		shutil.rmtree(subdir)
	os.mkdir(subdir)

def animate_series(fk,M,N,xmin,xmax,ymin,ymax,n,exact):
	subdir = 'plot_files'
	clean_plot(subdir)
	os.chdir(subdir)

	x = np.linspace(xmin,xmax,n)
	y = np.zeros(n, dtype='float')
	y_ = exact(x)
	count = 0
	for k in range(M,N + 1):
		plt.figure()
		y += fk(x,k)
		plt.plot(x,y,'-',label='fk')
		plt.plot(x,y_,'--',label='exact')
		plt.xlim(xmin,xmax)
		plt.ylim(ymin,ymax)
		plt.xlabel('x')
		plt.ylabel('y')
		plt.savefig('tmp%04d' % count)
		plt.close()
		count += 1

	os.chdir(os.pardir)

f0_exact = 	lambda x: np.exp(x)
def f0(x,k):
	ans = np.power(x,k)
	while k > 0:
		ans /= float(k)
		k -= 1
	return ans

fa_exact = 	lambda x: np.sin(x)
fa = 		lambda x,k: np.math.pow(-1,k % 2)*np.power(x,2*k + 1)/float(np.math.factorial(2*k + 1))

fb_exact =	lambda x: np.exp(-x)
fb = 		lambda x,k: np.power(-x,k)/float(np.math.factorial(k))

animate_series(fb,0,30,0,15,-.5,1.4,1001,fb_exact)

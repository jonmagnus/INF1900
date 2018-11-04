import matplotlib.pyplot as plt
import numpy as np
from SIZR import SolverSIZR, ProblemSIZR
#from scitools.std import PiecewiseConstant

def PiecewiseConstant(domain,data):
	def func(t):
		for p in reversed(sorted(data)):
			#print p
			if t >= p[0]: return p[1]
		return 0
	return func

beta = PiecewiseConstant(domain=[0,33],data=[(0,3e-2),(4,1.2e-3),(28,0)])
rho = 1
alpha = PiecewiseConstant(domain=[0,33],data=[(0,0),(4,1.6e-3),(28,6e-3)])
Sigma = PiecewiseConstant(domain=[0,33],data=[(0,20),(4,2),(28,0)])
deltaI = PiecewiseConstant(domain=[0,33],data=[(0,0),(4.4e-2),(28,0)])
deltaS = PiecewiseConstant(domain=[0,33],data=[(0,0),(28,6.7e-3)])
"""
t = np.linspace(0,33,101)
plt.plot(t,[beta(t_) for t_ in t])
plt.show()
"""
problem = ProblemSIZR(beta=beta,alpha=alpha,deltaS=deltaS,deltaI=deltaI,Sigma=Sigma,rho=rho,S0=60,Z0=1,I0=0,R0=0,T=33)
solver = SolverSIZR(problem,.5)
solver.solve()
solver.plot()
plt.xlabel('Time/hours')
plt.ylabel('Population')
plt.legend()
plt.show()


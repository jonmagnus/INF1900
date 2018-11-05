import matplotlib.pyplot as plt
import numpy as np
from SIZR import SolverSIZR, ProblemSIZR

beta = 3e-2
alpha = .2*beta
deltaS=deltaI=Sigma=0
rho = 1

T_ = [5,10,18]
a = 50*alpha
sigma = .5

omega = lambda t: a*sum([np.exp(-.5*((t-Ti)/sigma)**2) for Ti in T_])

problem = ProblemSIZR(beta=beta,alpha=lambda t: alpha + omega(t),\
			deltaS=deltaS,deltaI=deltaI,Sigma=Sigma,rho=rho,\
			S0=50,Z0=3,I0=0,R0=0,T=20)
solver = SolverSIZR(problem,.5)
solver.solve()
solver.plot()
plt.xlabel('Time/hours')
plt.ylabel('Population')
plt.legend()
plt.show()


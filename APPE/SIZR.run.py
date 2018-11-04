import matplotlib.pyplot as plt
import numpy as np
from SIZR import SolverSIZR, ProblemSIZR

problem = ProblemSIZR(beta=1.2e-3,alpha=1.6e-3,deltaS=0,deltaI=1.4e-2,Sigma=2,rho=1,S0=10,Z0=100,I0=0,R0=0,T=24)
solver = SolverSIZR(problem,.5)
solver.solve()
solver.plot()
plt.xlabel('Time/hours')
plt.ylabel('Population')
plt.legend()
plt.show()


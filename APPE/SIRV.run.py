import matplotlib.pyplot as plt
import numpy as np
from SIRV import ProblemSIRV, SolverSIRV

problem = ProblemSIRV(beta=lambda t: 0.0005 if t <= 12 else 0.0001,
                     nu=0.1, p=0, S0=1500, I0=1, R0=0, V0=0, T=60)
solver = SolverSIRV(problem,1e-2)
solver.solve()
#print solver.S[:3]
plt.title('Varying beta')
solver.plot()

plt.legend()
plt.show()


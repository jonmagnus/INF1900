import matplotlib.pyplot as plt
import numpy as np
from SIRV import ProblemSIRV, SolverSIRV

problem = ProblemSIRV(beta=lambda t: 0.0005 if t <= 12 else 0.0001,
                     nu=0.1, p=lambda t: .1 if t >= 6 and t <= 15 else 0, S0=1500, I0=1, R0=0, V0=0, T=60)
solver = SolverSIRV(problem,.5)
solver.solve()
solver.plot()
plt.xlabel('Time/days')
plt.ylabel('Population')
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from SIR_class import ProblemSIR, SolverSIR

problem = ProblemSIR(beta=5e-4,nu=.1,S0=1500,I0=1,R0=0,T=60)
solver = SolverSIR(problem,.5)
solver.solve()
plt.subplot(2,1,1)
plt.title('Constant beta')
solver.plot()

problem_ = ProblemSIR(beta=lambda t: 0.0005 if t <= 12 else 0.0001,
                     nu=0.1, S0=1500, I0=1, R0=0, T=60)
solver_ = SolverSIR(problem_,.5)
solver_.solve()
plt.subplot(2,1,2)
plt.title('Varying beta')
solver_.plot()
plt.legend()
plt.show()


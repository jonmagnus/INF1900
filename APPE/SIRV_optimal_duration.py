import matplotlib.pyplot as plt
import numpy as np
from SIRV import ProblemSIRV, SolverSIRV

VT = np.zeros(31)
max_I = np.zeros(31)
for VT_ in range(31):
	problem = ProblemSIRV(beta=lambda t: 0.0005 if t <= 12 else 0.0001,
                     nu=0.1, p=lambda t: .1 if t >= 6 and t <= 6 + VT_ else 0, S0=1500, I0=1, R0=0, V0=0, T=60)
	solver = SolverSIRV(problem,.5)
	solver.solve()
	VT[VT_] = VT_
	max_I[VT_] = solver.I.max()

plt.plot(VT,max_I,label='max_I')
plt.xlabel('Population')
plt.ylabel('V_T')
plt.legend()
plt.show()

"""
It is clear from the graph that the optimal duration is between 5 and 6 days.
"""

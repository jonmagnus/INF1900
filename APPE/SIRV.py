import matplotlib.pyplot as plt
import numpy as np
import ODESolver
from SIR_class import ProblemSIR, SolverSIR

class ProblemSIRV(ProblemSIR):
	def __init__(self,nu,beta,p,S0,I0,R0,V0,T):
		ProblemSIR.__init__(self,nu,beta,S0,I0,R0,T)

		if isinstance(p, (float,int)):
			self.p = lambda t: p
		elif callable(p):
			self.p = p

		self.V0 = V0

	def __call__(self, u, t):
		"""Right-hand side function of the ODE system."""
		S, I, R, V = u
		return [-self.beta(t)*S*I - self.p(t)*S,	# S equation
			self.beta(t)*S*I - self.nu(t)*I,	# I equation
			self.nu(t)*I,				# R equation
			self.p(t)*S]				# V equation


class SolverSIRV(SolverSIR):
	def solve(self, method=ODESolver.RungeKutta4):
		self.solver = method(self.problem)
		ic = [self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0]
		self.solver.set_initial_condition(ic)
		n = int(round(self.problem.T/float(self.dt)))
		t = np.linspace(0,self.problem.T,n+1)
		u, self.t = self.solver.solve(t)
		self.S, self.I, self.R, self.V = u[:,0], u[:,1], u[:,2], u[:,3]

	def plot(self):
		SolverSIR.plot(self)
		plt.plot(self.t,self.V,label='V')


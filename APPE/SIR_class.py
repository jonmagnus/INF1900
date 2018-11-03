import ODESolver
import numpy as np
import matplotlib.pyplot as plt

class ProblemSIR(object):
	def __init__(self,nu,beta,S0,I0,R0,T):
		"""
		nu, beta: parameters in the ODE system
		S0, I0, R0: initial values
		T: simulation for t in [0,T]
		"""
		if isinstance(nu, (float,int)): # number?
			self.nu = lambda t: nu # wrap as function
		elif callable(nu):
			self.nu = nu

		if isinstance(beta, (float,int)):
			self.beta = lambda t: beta
		elif callable(beta):
			self.beta = beta

		self.S0 = S0
		self.I0 = I0
		self.R0 = R0
		self.T = T


	def __call__(self, u, t):
		"""Right-hand side function of the ODE system."""
		S, I, R = u
		return [-self.beta(t)*S*I, # S equation
			self.beta(t)*S*I - self.nu(t)*I, # I equation
			self.nu(t)*I] # R equation

class SolverSIR(object):
	def __init__(self,problem,dt):
		self.problem, self.dt = problem, dt

	def solve(self, method=ODESolver.RungeKutta4):
		self.solver = method(self.problem)
		ic = [self.problem.S0, self.problem.I0, self.problem.R0]
		self.solver.set_initial_condition(ic)
		n = int(round(self.problem.T/float(self.dt)))
		t = np.linspace(0,self.problem.T,n+1)
		u, self.t = self.solver.solve(t)
		self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]

	def plot(self):
		plt.plot(self.t,self.S,label='S')
		plt.plot(self.t,self.I,label='I')
		plt.plot(self.t,self.R,label='R')



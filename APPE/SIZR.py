import ODESolver
import numpy as np
import matplotlib.pyplot as plt

class ProblemSIZR(object):
	def __init__(self,Sigma,beta,deltaS,deltaI,rho,alpha,S0,I0,Z0,R0,T):

		if isinstance(Sigma, (float,int)): # number?
			self.Sigma = lambda t: Sigma # wrap as function
		elif callable(Sigma):
			self.Sigma = Sigma

		if isinstance(beta, (float,int)):
			self.beta = lambda t: beta
		elif callable(beta):
			self.beta = beta

		if isinstance(deltaS, (float,int)):
			self.deltaS = lambda t: deltaS
		elif callable(deltaS):
			self.deltaS = deltaS

                if isinstance(deltaI, (float,int)):
                        self.deltaI = lambda t: deltaI
                elif callable(deltaI):
                        self.deltaI = deltaI

                if isinstance(rho, (float,int)):
                        self.rho = lambda t: rho
                elif callable(rho):
                        self.rho = rho

                if isinstance(alpha, (float,int)):
                        self.alpha = lambda t: alpha
                elif callable(alpha):
                        self.alpha = alpha

		self.S0 = S0
		self.I0 = I0
		self.Z0 = Z0
		self.R0 = R0
		self.T = T


	def __call__(self, u, t):
		"""Right-hand side function of the ODE system."""
		S, I, Z, R = u
		return [self.Sigma(t) - self.beta(t)*S*Z - self.deltaS(t)*S, 		# S equation
			self.beta(t)*S*Z - self.rho(t)*I - self.deltaI(t)*I, 		# I equation
			self.rho(t)*I - self.alpha(t)*S*Z,				# Z equation
			self.deltaS(t)*S + self.deltaI(t)*I + self.alpha(t)*S*Z]	# R equation

class SolverSIZR(object):
	def __init__(self,problem,dt):
		self.problem, self.dt = problem, dt

	def solve(self, method=ODESolver.RungeKutta4):
		self.solver = method(self.problem)
		ic = [self.problem.S0, self.problem.I0, self.problem.Z0, self.problem.R0]
		self.solver.set_initial_condition(ic)
		n = int(round(self.problem.T/float(self.dt)))
		t = np.linspace(0,self.problem.T,n+1)
		u, self.t = self.solver.solve(t)
		self.S, self.I, self.Z, self.R = u[:,0], u[:,1], u[:,2], u[:,3]

	def plot(self):
		plt.plot(self.t,self.S,label='S')
		plt.plot(self.t,self.I,label='I')
		plt.plot(self.t,self.Z,label='Z')
		plt.plot(self.t,self.R,label='R')



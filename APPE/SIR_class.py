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
# Example:
problem = ProblemSIR(beta=lambda t: 0.0005 if t <= 12 else 0.0001,
		     nu=0.1, S0=1500, I0=1, R0=0, T=60)
solver = ODESolver.ForwardEuler(problem)
solver.set_initial_condition([problem.S0,problem.I0,problem.R0])
u,t = solver.solve(np.linspace(0,problem.T,100*problem.T + 1))

#plt.figure(0)
plt.subplot(2,1,1)
plt.title('ForwardEuler')
plt.plot(t,u[:,0],label='S')
plt.plot(t,u[:,1],label='I')
plt.plot(t,u[:,2],label='R')
plt.plot(t,u[:,0] + u[:,1] + u[:,2],label='sum')
plt.legend()
#plt.show()

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
		plt.plot(self.t,self.R + self.I + self.S,label='sum')

plt.subplot(2,1,2)
plt.title('SolverSIR')
solver = SolverSIR(problem,.5)
solver.solve()
solver.plot()
plt.legend()
plt.show()

print 'The largest number of infected people at any time was ', int(solver.I.max()), ' according to SolverSIR'
print 'The largest number of infected people at any time was ', int(u[:,1].max()), ' according to ForwardEuler'

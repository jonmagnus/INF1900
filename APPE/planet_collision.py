import ODESolver
import numpy as np
import matplotlib.pyplot as plt

class ProblemPlanet(object):
	def __init__(self,gamma,m1,m2,x10,y10,x20,y20,T):

		self.gamma = gamma
		self.m1 = m1
		self.m2 = m2

		self.x10 = x10
		self.y10 = y10
		self.x20 = x20
		self.y20 = y20
		self.T = T


	def __call__(self, u, t):
		"""Right-hand side function of the ODE system."""
		x1,y1,x2,y2 = u
		return [y1,self.gamma*self.m2/(x1-x2)**2,
			-y2,self.gamma*self.m1/(x1-x2)**2]

class SolverPlanet(object):
	def __init__(self,problem,dt):
		self.problem, self.dt = problem, dt

	def solve(self, method=ODESolver.RungeKutta4):
		self.solver = method(self.problem)
		ic = [self.problem.x10, self.problem.y10, self.problem.x20, self.problem.y20]
		self.solver.set_initial_condition(ic)
		n = int(round(self.problem.T/float(self.dt)))
		t = np.linspace(0,self.problem.T,n+1)
		u, self.t = self.solver.solve(t)
		self.x1, self.y1, self.x2, self.y2 = u[:,0], u[:,1], u[:,2], u[:,3]

	def plot(self):
		plt.plot(self.t,self.x1,label='x1')
		plt.plot(self.t,self.x2,label='x2')

problem = ProblemPlanet(6.67408e-11,75,60,-.5,0,.5,0,11500)
solver = SolverPlanet(problem,5)
solver.solve()
solver.plot()
plt.legend()
plt.show()

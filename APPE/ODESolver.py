import numpy as np

class ODESolver:
	def __init__(self,f):
		self.f = lambda u,t:np.asarray(f(u,t),float)

	def advance(self):
		"""Advance solution one time step."""
		raise NotImplementedError

	def set_initial_condition(self,U0):
		if isinstance(U0,(float,int)):	# Scalar ODE
			self.neq = 1
			U0 = float(U0)
		else:
			U0 = np.asarray(U0)
			self.neq = U0.size()
		self.U0 = U0

	def solve(self, time_points, terminate=None):
		if terminate is None:
			terminate = lambda u,t,step_no: False

		self.t = np.asarray(time_points)
		n = self.t.size
		if self.neq == 1: 	# Scalar ODE
			self.u = np.zeros(n)
		else:			# System of ODEs
			self.u = np.zeros((n,self.neq))

		# Assume that self.t[0] corresponds to self.U0
		self.u[0] = self.U0

		# Time loop
		for k in range(n-1):
			self.k = k
			self.u[k+1] = self.advance()
			if terminate(self.u, self.t, self.k+1):
				break	# Terminate loop over k
		return self.u, self.t

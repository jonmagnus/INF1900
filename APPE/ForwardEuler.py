import numpy as np

class ForwardEuler:
	def __init__(self,f):
		if not callable(f):
			raise TypeError('f is %s, not a function' % type(f))
		self.f = f

	def set_initial_condition(self,U0):
		self.U0 = float(U0)

	def solve(self,time_points):
		"""Compute u for t values in time_points list."""
		self.t = np.asarray(time_points)
		self.u = np.zeros(len(time_points))
		# Assume self.t[0] corresponds to self.U0
		self.u[0] = self.U0

		for k in range(len(self.t)-1):
			self.k = k
			self.u[k+1] = self.advance()
		return self.u, self.t

	def advance(self):
		"""Advance the solution one time step."""
		u,f,k,t = self.u, self.f, self.k, self.t
		dt = t[k+1] - t[k]
		u_new = u[k] + dt*f(u[k],t[k])
		return u_new

def test_ForwardEuler_against_hand_calculations():
	"""Verify ForwardEuler against hand calc. for 2 time steps."""
	solver = ForwardEuler(lambda u,t: u)
	solver.set_initial_condition(1)
	u,t = solver.solve([0,.1,.2])
	exact = np.array([1,1.1,1.21])	# hand calculations
	error = np.abs(exact - u).max()
	assert error < 1e-14, '|exact - u| = %g != 0' % error

test_ForwardEuler_against_hand_calculations()

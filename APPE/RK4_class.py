import numpy as np
from ForwardEuler import ForwardEuler

class RK4(ForwardEuler):
	def advance(self):
		"""Advance the solution one time step."""
		u,f,k,t = self.u, self.f, self.k, self.t
		dt = t[k+1] - t[k]

		K1 = dt*f(u[k],t[k])
		K2 = dt*f(u[k] + .5*K1,t[k] + .5*dt)
		K3 = dt*f(u[k] + .5*K2,t[k] + .5*dt)
		K4 = dt*f(u[k] + K3,t[k] + dt)

		u_new = u[k] + (K1 + 2*K2 + 2*K3 + K4)/6.
		return u_new

def test_RK4_against_hand_calculations():
	"""Verify ForwardEuler against hand calc. for 2 time steps."""
	solver = RK4(lambda u,t: u)
	solver.set_initial_condition(1)
	u,t = solver.solve([0,.1,.2])
	exact = np.array([1,1.1,1.21])	# hand calculations
	error = np.abs(exact - u).max()
	assert error < 1e-14, '|exact - u| = %g != 0' % error

def test_RK4_against_linear_u():
	t = np.linspace(0,1,101)
	exact = t**2
	solver = RK4(lambda u,t: 2*t)
	solver.set_initial_condition(0)
	u,t_ = solver.solve(t)
	error = np.abs(exact - u).max()
	assert error < 1e-14, '|exact - u| = %g != 0' % error

test_RK4_against_linear_u()
#test_RK4_against_hand_calculations()

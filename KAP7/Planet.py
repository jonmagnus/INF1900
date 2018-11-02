from math import pi

class Planet:
	def __init__(self,name,radius,masse,population = 0):
		self.name = name
		self.radius = radius
		self.masse = masse
		self.population = population

	def density(self):
		V = 4*pi*self.r**3/3
		return self.masse/V

	def print_info(self):
		print 'navn = ', self.navn
		print 'radius = ', self.radius
		print 'masse = ', self.masse
		print 'populastion = ', self.population
		print 'density = ', self.density()

planet1 = Planet('Earth',6.371e6,5.972e24,7497486172)
print planet1.name, 'has a population of ', planet1.population

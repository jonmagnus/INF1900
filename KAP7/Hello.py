class Hello:
	#def __init__(self):
	#	pass

	def __call__(self, arg):
		return 'Hello, %s!' % arg

	def __str__(self):
		return 'Hello, World!'

a = Hello()
print a('students')
print a

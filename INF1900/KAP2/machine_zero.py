eps = 1.	# Set the initial value of eps to 1
while 1. != 1. + eps:			# While eps is not neglible
	print '..........', eps		# Print the current eps with indentation
	eps = eps/2.			# Halve the value of eps
print 'final eps:', eps			# Print the final value of eps that was neglected


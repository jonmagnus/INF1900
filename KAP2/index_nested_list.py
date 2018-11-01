q = [['a','b','c'],['d','e','f'],['g','h']]

print q[0][0]
print q[1]
print q[2][1]
print q[1][0]

"""
q[-1][-2] has the value 'g' because it is in the last list (list -1)
at the second to last index (index -2).
"""

for i in q:
	for j in range(len(i)):
		print i[j]

"""
The object i is a list, and j is an integer used for indexing
"""

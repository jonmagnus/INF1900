s = 0; k = 1; M = 100
""" Before alteration:
while k < M:
	s += 1/k

The problem is that k never increases, so the condition
k < M will always remain True. Secondly, the integer
division 1/k is always rounded to 0 because of integer
interpretation (except for when k == 1). This should be
changed to float division.
"""


#After alteration
while k < M:
	s += 1./k
	k += 1
print s

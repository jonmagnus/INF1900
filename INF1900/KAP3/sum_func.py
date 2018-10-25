def sum_1k(M):
	s = 0
	for k in range(1,M + 1):
		s += 1./k
	return s

by_hand = 1.833333333333

def test_sum_1k():
	success = sum_1k(3) == by_hand
	msg = 'Result by hand is same as result by function'
	assert success, msg

test_sum_1k()


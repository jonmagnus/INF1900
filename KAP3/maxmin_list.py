from random import randint

def max_(a):
	max_elem = a[0]
	for elem in a[1:]:
		if (max_elem < elem): max_elem = elem
	return max_elem

def min_(a):
	min_elem = a[0]
	for elem in a[1:]:
		if (min_elem > elem): min_elem = elem
	return min_elem

a = [randint(-10,10) for i in range(10)]

print a
print 'The largest element is %d\nThe smallest element is %d' %(max_(a), min_(a))

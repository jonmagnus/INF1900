def diff(poly):
	pd = {}
	for p in poly:
		if p == 0: continue
		pd[p-1] = p*poly[p]
	return pd

p = {0: -3, 3: 2, 5: -1}
print p
print diff(p)

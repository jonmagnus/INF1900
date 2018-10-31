from F import F
f = F(a=1., w = .1)
from math import pi
print f.value(x = pi)
f.a = 2
print f.value(pi)

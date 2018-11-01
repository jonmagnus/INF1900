import sys
from scitools.StringFunction import StringFunction
parameters = {}
for prm in sys.argv[4:]:
	key, value = prm.split('=')
	parameters[key] = eval(value)
f = StringFunction(sys.argv[1], independent_valiable=sys.argv[2],
		   **parameters)
var = float(sys.argv[3])
print f
print f(var)

"""
The program accepts system arguments. It interperets the first
one as a function definition, the second one as the variable of
the function and the third one as where the function should be
evaluated. The rest of the arguments are also passed on to the
function.
"""

f = eval('StringFunction(sys.argv[1], ' + \
	 'independent_valiables=sys.argv[2], %s)' % \
	 (', '.join(sys.argv[4:]) ))
var = float(sys.argv[3])
print f(var)

"""
The second program does the same as the first one, only more directly
and compactly.
"""

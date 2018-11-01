length = 640

inch = 2.54e-2
foot = 12*inch
yard = 3*foot
mile = 1760*yard

print """%g meters is:
%g inches,
%g feet,
%g yards, and
%g miles
""" % (length, length/inch, length/foot, length/yard, length/mile)

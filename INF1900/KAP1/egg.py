from math import pi, log

M = 67.
rho = 1.038
c = 3.7
K = 5.4e-3
T_w = 100.
T_y = 70.
T_0 = 20

t = (M**(2./3)*c*rho**(1./3))/(K*pi**2*(4*pi/3)**(2./3))*log(0.76*float(T_0 - T_w)/(T_y - T_w))
print 'Tiden det tar aa koke egget naar T_0 = %g er %g sekunder' % (T_0,t)

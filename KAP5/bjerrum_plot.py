import matplotlib.pyplot as plt
import numpy as np

K1 = 5.01e-7
K2 = 4.79e-11
pH = np.linspace(4,12,101)

cons_H = np.power(10,-pH)
cons_CO2 = cons_H**2/(cons_H**2 + K1*cons_H + K1*K2)
cons_HCO3 = K1*cons_H/(cons_H**2 + K1*cons_H + K1*K2)
cons_CO3 = K1*K2/(cons_H**2 + K1*cons_H + K1*K2)

plt.xlabel('pH')
plt.ylabel('Konsentrasjon reagens (mol/L)')
plt.plot(pH,cons_CO2,label='CO_2')
plt.plot(pH,cons_HCO3,label='HCO_3')
plt.plot(pH,cons_CO3,label='CO_3')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

F = np.linspace(-20,120,1001)
C = (F - 30)/2.
C_ = (F - 32)*5/9.

plt.plot(F,C,'r--',label='Inprecise')
plt.plot(F,C_,'g-',label='Precise')
plt.legend()
plt.xlabel('F')
plt.ylabel('C')
plt.show()

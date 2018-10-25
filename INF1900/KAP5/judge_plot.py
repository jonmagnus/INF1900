import numpy as np
x = np.linspace(0,2,20)
y = np.cos(18*np.pi*x)
x_ = np.linspace(0,2,1000)
y_ = np.cos(18*np.pi*x_)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.plot(x_,y_)
plt.show()

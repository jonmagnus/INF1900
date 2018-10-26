import matplotlib.pyplot as plt
import numpy as np

f = lambda x,t: np.exp(-(x - 3*t)**2)*np.sin(3*np.pi*(x - t))

x = np.linspace(-4,4,101)
y = f(x,0)
plt.plot(x,y)
plt.show()

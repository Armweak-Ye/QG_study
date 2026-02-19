import matplotlib.pyplot as plt
import numpy as np

xpoints = np.arange(0, 10, 0.1) #起，终，步长
ypoints = np.sin(xpoints)

plt.plot(xpoints, ypoints)
plt.show()
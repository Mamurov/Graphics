# Plot the function 2 cos (t - 2) + sin (2 ∗ t - 4) on the segment t ∈ [-20π; 10π] using an abscissa step of 0.1.
# 3. For the graph built in task 2, change:
# • line color;
# Console!

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20*np.pi, 10*np.pi,0.01)
y = 2*np.cos(x-2)+np.sin(2*x-4)
plt.plot(x,y, color='r')
plt.show()

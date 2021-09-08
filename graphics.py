
# Create and display a 5 × 5 matrix, where the first line contains ones, the second - twos, the third - threes, etc.
# Save the resulting matrix to a text file.
# Сonsole!

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20*np.pi, 10*np.pi,0.01)
y = 2*np.cos(x-2)+np.sin(2*x-4)
plt.plot(x,y)
plt.show()

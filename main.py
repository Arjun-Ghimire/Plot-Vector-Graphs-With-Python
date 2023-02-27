# Ploating a vector graphs using python, I am using matflotlib and numpy for this purpose

import matplotlib.pyplot as plt
import numpy as np

a = np.array([2,5])
b = np.array([5,3])

c= a-b

fig,axis = plt.subplots()

""" here the first two arguments takes the starting point of the vector, here a[0], a[1] specifies the 
 x and y components of the vector, angles xy speicifies the angle of the arrow, scale_units "xy" specifies
 the scalling should be applied equally in both x and y axes and scale 1 specifies the scaling factor. """

axis.quiver(0,0,a[0],a[1],angles='xy',scale_units='xy',scale=1)
axis.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1)
axis.quiver(b[0], b[1], c[0], c[1], angles='xy', scale_units='xy', scale=1, color='r')

axis.set_xlim([0,10])
axis.set_ylim([0,10])

plt.show()
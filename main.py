# Ploating a vector graphs using python, I am using matflotlib and numpy for this purpose

import matplotlib.pyplot as plt
import numpy as np

# take two space-separated inputs as a string and split them into a list of two strings
a_input = input("Enter two vector numbers with a space for eg, 2 3 = ").split()
b_input = input("Enter two vector numbers with a space for eg, 3 4 = ").split()

choice = input("What do you want to perform? addition or subtraction? Enter 1 for addition, 2 for subtraction = ")

# convert the list of strings to a NumPy array of floats
a = np.array([float(x) for x in a_input])
b = np.array([float(x) for x in b_input])

if choice =="1":

    c = a + b

else : 
    c = a-b

fig,axis = plt.subplots()

""" here the first two arguments takes the starting point of the vector, here a[0], a[1] specifies the 
 x and y components of the vector, angles xy speicifies the angle of the arrow, scale_units "xy" specifies
 the scalling should be applied equally in both x and y axes and scale 1 specifies the scaling factor. """

axis.quiver(0,0,a[0],a[1],angles='xy',scale_units='xy',scale=1)
axis.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1)
axis.quiver(b[0], b[1], c[0], c[1], angles='xy', scale_units='xy', scale=1, color='r')

axis.set_xlim([0,10])
axis.set_ylim([0,10])

axis.set_xlabel('X-axis')
axis.set_ylabel('Y-axis')

if choice=="1":
    axis.set_title('Addition of two vectors')
else:
    axis.set_title('Subtraction of two vectors')


plt.show()
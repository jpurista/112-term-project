""" A program to animate a bouncing ball using inputs from the user. 
    This program is designed to show the student that coding can (and should) 
    be used to replace human calculations. 
    It also incorporates the basics of Python programming to solve mechanical problems. 
    ESP4T 2017
    Department of Electrical & Computer Engineering, University of Wyoming. """

# Need to use functions from the following libraries to make our work easier
import math
from math import sin, cos, radians
# Using the 'as' keyword allows us to use plt instead of matplotlib.pyplot, for example
import numpy as np
import matplotlib.pyplot as plt

# ALL CALCULATIONS TO BE DONE IN THE METRIC SYSTEM

# Let us first initialize a few basic variables
# Change this value of g to simulate extra-terrestrial environments i.e. on the moon, g = 1.6 m/s^2
g = 9.8

# Accepting values from the user for initial parameters
Vo = float(input("Please enter the initial velocity (in m/s): "))
theta = float(input("Please enter the initial angle (in deg) at which it is thrown: "))

# For the first flight path
# From the above values, we can calculate a few parameters of flight
# HINT: Need to convert from degrees to radians for all Trigonometric functions
total_time1 = 2*Vo*sin(radians(theta))/g                    #t = 2Vo*sin(theta)/g
max_height1 = math.pow(Vo, 2)*math.pow(sin(radians(theta)), 2)/(2*g)        #H = Vo^2*sin^2(theta)/(2g)
range1 = math.pow(Vo, 2)*sin(radians(2*theta))/g                #R = Vo^2*sin(2*theta)/g

# Defining a few variables to make typing equations simpler
Vox = Vo*cos(radians(theta))
Voy = Vo*sin(radians(theta))

# Change here for number of discretely plotted points:
steps1 = 17

# Create an array of 20 time values between launch(0 s) and land(total_time s)
time1 = np.linspace(0.0, total_time1, steps1)

# Creating figure 1
plt.figure(1)
plt.suptitle('Path of a bouncing ball', fontweight='bold', fontsize='15')
# Overlay a grid on the plot
plt.grid()
# Label the axes with appropriate information
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")

# Since this is a time-continuous equation, we will define an (x, y) point in space for every time t 
for t in time1:
    # X distance from starting point at time t
    x1 = Vox*t
    # Similarly, Y distance from starting point after t seconds
    y1 = Voy*t - 0.5*g*np.power(t, 2)
    # Plotting the above values with a blue circle of size 8
    plt.plot([x1], [y1], 'bo', markersize=8)
    # Label each previous point with an appropriate time stamp aligned as shown
    plt.annotate('%.2f s' % t, xy=(x1, y1), fontsize='9', horizontalalignment='center', verticalalignment='bottom')
    # Pause the plot to allow for an animated effect, showing movement in real time
    plt.pause(total_time1/steps1)

# Projectile path after bounce

# Defining a value for coefficient of restitution e
e = 0.712

# Setting number of dicrete bounces for first bounce
steps2 = 13

# We will now simulate 3 bounces...
# CHANGE HERE for more bounces
for n in [1, 2, 3]:
    # We assume a frictionless surface so change in X direction will be
    Vox = Vox + (e-1)*Voy
    # The angle of launch will remain the same as before i.e. theta
    # But due to a different e, the velocity in the Y direction will decrease
    Voy = e*Voy

    # Thus the new initial velocity after bounce will be:
    Vo1 = Voy/sin(radians(theta))

    # Recalculating basic flight parameters based on previous values
    total_time2 = 2*Vo1*sin(radians(theta))/g                                        #t = 2Vo*sin(theta)/g
    max_height2 = math.pow(Vo1, 2)*math.pow(sin(radians(theta)), 2)/(2*g)            #H = Vo^2*sin^2(theta)/(2g)
    range2 = math.pow(Vo1, 2)*sin(radians(2*theta))/g                                #R = Vo^2*sin(2*theta)/g

    # Defining a new ime variable based on parameters after bounce
    time2 = np.linspace(0.0, total_time2, steps2)

    # Similar to previous flight path
    for t in time2:
        # X distance from starting point at time t, now from the starting point
        x1 = range1 + Vox*t
        # Similarly, Y distance from starting point after t seconds
        y1 = Voy*t - 0.5*g*np.power(t, 2)
        # Plotting the above values with a red circle of size 8
        plt.plot([x1], [y1], 'ro', markersize=8)
        # Label each previous point with an appropriate time stamp aligned as shown, now w.r.t total time of flight from start
        plt.annotate('%.2f s' % (t+total_time1), xy=(x1, y1), fontsize='9', horizontalalignment='center', verticalalignment='bottom')
        # Pause the plot to allow for an animated effect, showing movement in real time
        plt.pause(total_time2/steps2)

    # Redefining parameters for the next bounce
    steps2 = steps2 - 2
    
    # We need the plot to move by range2 in the X direction so we add to the previous range
    range1 = range1 + range2                

    # We also nee te time stamp to reflect the total time from launch so we update it by adding total_time2
    total_time1 = total_time1 + total_time2

# Inserting text into the figure
plt.title('(Zoom in for more detail!)', size='15', weight='light', horizontalalignment='center')

# Displaying plot at the end
plt.show()


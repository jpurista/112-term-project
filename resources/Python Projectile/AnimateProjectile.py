"""
    A program to animate the path of a projectile using inputs from the user.
    The program will pick a random distance. The user should try and land the projectile at
    that range using an initial velocity and an initial angle within 3 trials.
    This program is designed to show the student that coding can (and should) 
    be used to replace human calculations. 
    It also incorporates the basics of Python programming to solve analytical problems. 
    ESP4T 2017
    Department of Electrical & Computer Engineering, University of Wyoming.
"""

# Need to use functions from the following libraries to make our work easier
import math
from math import sin, cos, radians
# Using the 'as' keyword allows us to use plt instead of matplotlib.pyplot, for example
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ALL CALCULATIONS TO BE DONE IN THE METRIC SYSTEM

# Let us first initialize a few basic variables
# Change this value of g to simulate extra-terrestrial environments i.e. on the moon, g = 1.6 m/s^2
g = 9.8

# Randomly generating a target range to give the user
target_range = random.randint(20, 250);

# Creating figure 1
plt.figure(1)
# Overlay a grid on the plot
plt.grid()
# Label the axes with appropriate information
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")

# Mark the area in which to land the projectile
plt.axvspan(xmin=target_range-5, xmax=target_range+5, ymin=0, ymax=0.02, facecolor='y', hold=True)

# Book keeping stuff to colorize axes and provide a legend to the graph
ax = plt.gca()

cpatch = []

print("\nLet the games begin!")
print("\nThe target range is set to %d m" % target_range)
print("\nCan you hit it? You have 3 chances!")

# To count from 1 to 3, the number of chances you get
for n in range(1, 4):

    print("\nTrial %d: " % n)
       
    # Accepting values from the user for initial parameters
    Vo = float(input("Please enter the initial velocity (in m/s): "))
    theta = float(input("Please enter the initial angle (in deg) at which it is thrown: "))

    # From the above values, we can calculate a few parameters of flight
    # HINT: Need to convert from degrees to radians for all Trigonometric functions
    total_time = 2*Vo*sin(radians(theta))/g                                 #t = 2Vo*sin(theta)/g
    max_height = math.pow(Vo, 2)*math.pow(sin(radians(theta)), 2)/(2*g)     #H = Vo^2*sin^2(theta)/(2g)
    prange = math.pow(Vo, 2)*sin(radians(2*theta))/g                        #R = Vo^2*sin(2*theta)/g

    # Display the above values to the user
    print("\nThe total time of flight: %2.2f s\n" % total_time)
    print("The maximum height reached by projectile from the ground: %.2f m\n" % max_height)
    print("The horizontal range of projectile: %.2f m\n" % prange)

    # Defining a few variables to make typing equations simpler
    Vox = Vo*cos(radians(theta))
    Voy = Vo*sin(radians(theta))

    # Change here for number of discretely plotted points:
    steps = 21

    # Create an array of 20 values between launch (at 0 s) and land (at total_time s)
    time = np.linspace(0.0, total_time, steps)

    # Code to change the color of the projectile for each launch
    color = next(ax._get_lines.color_cycle)

    cpatch.append(mpatches.Patch(color=color, label='Projectile %d' % n))

    # Display legend on plot
    plt.legend(handles=cpatch, loc='best')
    
    # Since this is a time-continuous equation, we will define an (x, y) point in space for every time t 
    for t in time:
        # Equations of motion (CHANGE BELOW the values for x1, y1)
        # X distance from starting point at time t
        x1 = Vox*t                                                      #x = Vox*t
        # Similarly, Y distance from starting point after t seconds 
        y1 = Voy*t - 0.5*g*np.power(t, 2)                               #y = Voy*t - 1/2*g*t^2
        # Plotting the above values with a blue circle of size 7
        plt.plot([x1], [y1], 'o', markersize=7, color=color)
        # Label each previous point with an appropriate time stamp aligned as shown
        #plt.annotate('%.2f s' % t, xy=(x1, y1), fontsize='8', horizontalalignment='center', verticalalignment='bottom')
        # Pause the plot to allow for an animated effect, showing movement in real time
        plt.pause(total_time/steps)

    # To autoscale the plot limits so that it sits pretty inside the figure
    plt.autoscale()
    
    # Checking if the target is met or not through a series of if-else statements
    if abs(target_range-prange) <= 5:
        print("You are spot on! Great job selecting the right numbers.")
        break
    elif abs(target_range-prange) > 5 and abs (target_range-prange) <= 10:
        print("You are ALMOST there!")
    else:
        print("You may want to check your calculations again...")

plt.show()

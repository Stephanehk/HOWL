import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from scipy import stats
import csv
import pprint as p

# size of the grid
size = 15
# point which the wolves will be drawn too
point = (5, 5)
# speed at which the wolves travel (km/h)
speed = 40
# spacing of the pies (km). Wolves can hear howls from 10km away, so at 20 km sounds wont overlap and confuse them
spacing = 20
#times at which the system will be observed
times = [0,30,60]

# creates the grid that represents all the pies. Each iteam represents on pies
def create_grid(size, point):
    (point_row, point_col) = point
    grid = [['*' for x in range(size)] for y in range(size)]
    grid[point_row][point_col] = 'H'
    return grid

# creates the ripple pattern
def createx_ripple(grid, time_passed, speed, spacing, point):

    # g = growl which pushes the wolves
    # h = howl which pulls the wolves
    # * = pie is off, and due to the ripple system where most of the wolves wolve will be gathered
    sounds = ['G','H','*']

    (point_row, point_col) = point

    # finding the time taken for the enite cycle.
    # the time in minutes for the wolve to travel form one pie to another is found by spacing/speed
    # the ripple works in three phases so this time is mulitplied by 3
    time_invtervol = ((spacing / speed) * 60) * 3

    # determines what phase/position the sytem should be in at that time
    if (time_passed % time_invtervol) < (spacing / speed) * 60:
        position = 0
    if  (spacing / speed) * 60 <= (time_passed % time_invtervol) < (spacing / speed) * 60 * 2:
        position = 1
    if (spacing / speed) * 60 * 2 <= (time_passed % time_invtervol) < ((spacing / speed) * 60) * 3:
        position = 2

    # uses a distance forumla to make each pie produce the appoprate noise
    for zone in range((round(len(grid)))):
        for row in range(len(grid)):
            for col in range(len(grid)):
                if ( (row - point_row)**2 + (col - point_col)**2 ) ** .5 < ( (len(grid)) - zone):
                    grid[row][col] = sounds[position]
        position = position - 1
        if position == -1:
            position = 2
    # makes the center point always a howl
    grid[point_row][point_col] = 'H'

    return grid


def show_grid(grid, time_passed):

    # displays and color codes the results
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 'G':
                c = 'red'
            elif grid[row][col] == 'H':
                c = 'blue'
            else:
                c = 'black'
            plt.text(row * spacing, col * spacing, grid[row][col], color = c)

    plt.xlim(-1 * spacing,len(grid) * spacing)
    plt.ylim(-1 * spacing, len(grid) * spacing)
    plt.xlabel('X Posistion (km)')
    plt.xlabel('Y Posistion (km)')
    plt.title(time)
    plt.show()



# both displayes the imfo with matplot, but the real data is stored in the grid. The action of each pie at the time is there
grid = create_grid(size, point)
for time in times:
    grid = createx_ripple(grid, time, speed, spacing, point)
    show_grid(grid, time)

# 
# a1task2.py - Assignment 1, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Functions with numeric inputs
# 
#
import math

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
# function 1
def cube(x):
    """ returns the cube of its input
        input x: any number (int or float)
    """
    return x**3

# function 2
def slope(x1, y1, x2, y2):
    """ takes four numeric inputs that specify the coordinates of two points
        (x1, y1) and (x2, y2) in the Cartesian plane, 
        and that returns the slope of the line formed by those two points.
        input (x1, y1, x2, y2): any number (int or float)
    """
    return (y2 - y1)/(x2 - x1)

# function 3
def cylinder_volume(diameter, height):
    """ returns the volume of a cylinder of a given diameter and height.
        The volume of a cylinder is given by: v = π r^2 h.
        input (diameter, height): any number (int or float)
    """
    r = diameter/2
    return math.pi * r**2 *height




# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':

    # sample test call for function 0
    print('opposite(-8) returns', opposite(-8))

    # add test calls for your functions below
    # sample test call for function 1
    print('cube(-5) returns', cube(-5))
    # sample test call for function 2
    print('slope(2, 3, 4, 7) returns', slope(2, 3, 4, 7))
    print('slope(7, 2, 3, 4) returns', slope(7, 2, 3, 4))
    print('slope(2, 3, 5, 3) returns', slope(2, 3, 5, 3))
    # sample test call for function 3
    print('cylinder_volume(10, 10)  returns', cylinder_volume(10, 10))
    print('cylinder_volume(20, 10)  returns', cylinder_volume(20, 10))
 



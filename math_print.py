#############################################################################
# FILE : math_print.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# EXERCISE : intro2cs ex1 2017-2018
# DESCRIPTION : a program that prints out different math values using math
# functions.
#############################################################################

# The next line imports math module into the program
import math

def golden_ratio():
# These next lines define a function that prints the value of the golden ratio
    print((1+math.sqrt(5))/2)
# The next line ends this function definition.
    return

def six_square():
# These next lines define a function that prints the value of six square.
    print(math.pow(6,2))
# The next line ends this function definition.
    return

def hypotenuse():
# These next lines define a function that prints the value of the hypotenuse
# in a right triangle with legs of 5 & 12.
    print(math.sqrt(math.pow(12,2)+math.pow(5,2)))
# The next line ends this function definition.
    return

def pi():
# These next lines define a function that prints the value of pi.
    print(math.pi)
# The next line ends this function definition.
    return

def e():
    # These next lines define a function that prints the value of e.
    print(math.e)
# The next line ends this function definition.
    return

def squares_area():
# These next lines define a function that prints the values of different 10
# squares areas, with side lengths going 1-10.
    print(1*1, 2*2, 3*3, 4*4, 5*5, 6*6, 7*7, 8*8, 9*9, 10*10)
# The next line ends this function definition.
    return

# The next commands prints different math values I previously defined.
golden_ratio()
six_square()
hypotenuse()
pi()
e()
squares_area()
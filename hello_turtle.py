#############################################################################
# FILE : hello_turtle.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# EXERCISE : intro2cs ex1 2017-2018
# DESCRIPTION : a program that Draws a bed of flowers using turtle functions
#############################################################################

# The next line imports the turtle module into the program.
# We will use the different turtle commands in this program in order to draw.
import turtle

def draw_petal():
# These next lines define drawing of a Petal.
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
# The next line ends this function definition.
    return

def draw_flower():
# These next lines define drawing of a Flower combined out of 4 petals & stem
# This function is based on the previous defined petal func.
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)
# The next line ends this function definition.
    return

def draw_flower_advanced():
# These next lines define drawing of a flower and move the turtle pen head in
# order to prepare for the drawing of the next flower.
# This function is based on the previous defined flower func.
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()
# The next line ends this function definition
    return

def draw_flower_bed():
# These next lines define drawing of 3 fully drawn flowers.
# This function is based on the previous defined flower_advanced func.
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()
# The next line ends this function definition.
    return

#The next line run the previously defined function which draws bed of flowers
draw_flower_bed()

# The next command will pause the program and prevent it from closing.
turtle.done()

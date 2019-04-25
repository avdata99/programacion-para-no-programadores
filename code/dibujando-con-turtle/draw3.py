""" requerimientos
instalar python3-tk
Linux: 
 - sudo apt-get install python3-tk
"""
import turtle 

# sets window to 200x200 pixels, in upper left of screen
turtle.setup(width=400, height=400, startx=0, starty=0)
turtle.colormode(255)
turtle.title("Welcome to the turtle zoo!")

for x in range(1, 210):
    turtle.forward(x)
    turtle.left(64)
    turtle.pencolor(x % 255, 2 * x % 255, 3 * x % 255)

turtle.done()
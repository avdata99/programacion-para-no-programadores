""" requerimientos
instalar python3-tk
Linux: 
 - sudo apt-get install python3-tk
"""
import turtle 

# sets window to 200x200 pixels, in upper left of screen
turtle.setup(width=400, height=400, startx=0, starty=0)
turtle.colormode(255)
turtle.speed(0)
for x in range(1, 210):
    turtle.forward(x/2)
    turtle.left(69)
    r = x % 255
    g = 2 * x % 255
    b = 3 * x % 255
    turtle.pencolor(r, g, b)
    turtle.title("x={} r={}, g={}, b={}".format(x, r, g, b))

cv = turtle.getcanvas()
cv.postscript(file="{}.ps".format(__file__), colormode='color')

turtle.done()
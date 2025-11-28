""" requerimientos
instalar python3-tk
Linux: 
 - sudo apt-get install python3-tk
"""
import turtle 

# sets window to 200x200 pixels, in upper left of screen
turtle.setup(width=600, height=400, startx=0, starty=0)
turtle.colormode(255)
turtle.speed(0)
for x in range(1, 250):
    move = x * 0.85
    turtle.forward(move)
    angulo = 83 + (x % 9)
    turtle.left(angulo)
    r = 3 * x % 255
    g = 2 * x % 255
    b = 3 * x % 255
    turtle.pencolor(r, g, b)
    turtle.title("x={} r={}, g={}, b={}. move={}, angulo={}".format(x, r, g, b, move, angulo))

cv = turtle.getcanvas()
cv.postscript(file="{}.ps".format(__file__), colormode='color')

turtle.done()
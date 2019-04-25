""" requerimientos
instalar python3-tk
Linux: 
 - sudo apt-get install python3-tk
"""
import turtle 

# sets window to 200x200 pixels, in upper left of screen
turtle.setup(width=400, height=400, startx=0, starty=0)
turtle.colormode(255)

for x in range(1, 210):
    move = x * 0.75
    turtle.forward(move)
    angulo = 85 + (x % 10)
    turtle.left(angulo)
    r = x % 255
    g = 2 * x % 255
    b = 3 * x % 255
    turtle.pencolor(r, g, b)
    turtle.title("x={} r={}, g={}, b={}. move={}, angulo={}".format(x, r, g, b, move, angulo))

cv = turtle.getcanvas()
cv.postscript(file="{}.ps".format(__file__), colormode='color')

turtle.done()
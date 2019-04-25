import turtle 


# sets window to 200x200 pixels, in upper left of screen
turtle.setup (width=700, height=400, startx=0, starty=0)
turtle.colormode(255)
turtle.title("Welcome to the turtle zoo!")

turtle.goto(0, 0)

for x in range(1, 255):
    turtle.forward(100)
    turtle.left(64)
    # turtle.pencolor(2 * x % 255, x % 255, 3 * x % 255)
    
turtle.done()
import turtle
import time
levels = 2
radius = 50
turtle.speed(0.9)

# draw initial rings
# for i in range(rings):
def centreCircle(rad):
    turtle.penup()
    turtle.right(90)
    turtle.forward(rad)
    turtle.left(90)
    turtle.pendown()

    turtle.circle(rad)

    turtle.penup()
    turtle.left(90)
    turtle.forward(rad)
    turtle.right(90)
    

def virus(level):
    if level == 0:
        return 0

    for i in range(8):
        turtle.forward(150)
        centreCircle((50/levels)*2)

        #go back
        turtle.right(180)
        turtle.forward(radius/(2**level))
        turtle.right(180)
        
        turtle.left(45)

    turtle.forward(50+radius/(2**level))
    return virus(level-1)

# virus(levels, 0, 0)
# centreCircle(radius)

#Middle circle
centreCircle(radius)

# make eight circles only
# for level in range(levels):
#     for i in range(8):
#         turtle.forward(150)
#         centreCircle((50/levels)*2)

#         #go back
#         turtle.right(180)
#         turtle.forward(150)
#         turtle.right(180)

#         turtle.left(45)
# virus(levels)

turtle.done()
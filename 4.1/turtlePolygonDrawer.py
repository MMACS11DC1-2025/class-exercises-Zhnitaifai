import turtle
import math
import random

him = turtle.Turtle()
turtle.colormode(255)
turtle.delay(1)

him.home()
him.penup()

rad = int(input("Radius: "))
resolution = int(input("Sides: "))
penWidth = int(input("Pen Width: "))
epilpesy = input("Epilepsy? ")

him.width(penWidth)

side = ((2*math.pi*rad)/resolution)

him.stamp()
him.goto(0, -rad+(penWidth/2))

def getColor(colour):
    color = []
    num = int(255/(resolution+1))
    i = 1
    while i <= 3:
        color.append(num*colour)
        i += 1
    return color

him.pendown()

for sides in range(resolution+1):
    if epilpesy.lower()[0] == "y":
        him.color(getColor(sides+1))
        # turtle.bgcolor(getColor())
    if sides == 0:
        him.forward(side/2)
        him.left(360/resolution)
    elif sides == resolution:
        him.forward(side/2)
    else:
        him.forward(side)
        him.left(360/resolution)
    print(sides)
            
print("done")

turtle.done()
exit()
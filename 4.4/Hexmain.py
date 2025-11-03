import turtle

# could add shape

# steps = input("Steps: ")
steps = 3
baseRad = 50
offset = 15

turtle.left(90)

# point is centre, ends in centre
def hexagon(rad, x, y):
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.penup()
    turtle.forward(rad)
    turtle.pendown()
    for i in range(6):
        if i == 0:
            turtle.left(60)
        turtle.left(60)
        turtle.forward(rad)
    turtle.end_fill()
    turtle.goto(x, y) 
    turtle.right(60)

def pattern(steps):
    # for i in range(3**steps):
    #     turtle.right(60)
    #     turtle.forward(baseRad*2.5)
    #     hexagon()
    if 
    return "d"

hexagon(baseRad, 0, 0)
turtle.forward(150)
turtle.stamp()
print(turtle.pos())
pos
hexagon(baseRad/2, t)

turtle.done()
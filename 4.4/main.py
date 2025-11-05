import turtle

turtle.speed(0)
turtle.delay(0)
turtle.tracer(0)

levels = int(input("Enter the number of levels (anything above 3 is laggy): "))
rad = int(input("Enter a radius (recommended 100 to 350): "))
arrayNum = int(input("Enter the number circles per a level: "))
variability = int(input("Enter the variabillity between the levels: "))
# accelerate

settings = {"levels": levels, "radius": rad, "arrayNum": arrayNum, "variability":variability}
colours = {0:"red", 1:"orange", 2:"yellow", 3:"green", 4:"blue", 5:"indigo", 6:"violet", 7:"black"}

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

def virus(level, rad, angleModifier):
    turtle.right(angleModifier)
    # turtle.width(2**level)
    centreCircle(rad)
    if level > 1:

        for i in range(8):
            turtle.left((360/8))
            turtle.forward(rad)
            turtle.color(colours[i])
            virus(level-1, rad/3, angleModifier)
            turtle.left(angleModifier)
            turtle.back(rad)

counter = 10 # 

while True:
    # if counter == 3600:
    #     break
    turtle.clear()
    virus(levels, radius, counter)
    
    turtle.update()

    # counter += 1
turtle.done()
import turtle

# Turtle settings to speed up animation
turtle.speed(0)
turtle.delay(0)
turtle.tracer(0)

levels = int(input("Enter the number of levels (anything above 3 is laggy): "))
rad = int(input("Enter a radius (100 to 350): "))
arrayNum = int(input("Enter the number circles per a level (3 to 8): "))
variability = int(input("Enter the variabillity between the levels (between 2-3): "))
acceleration = input("Would you like acceleration? ")
if acceleration.lower() == "y":
    acceleration == True

settings = {
    "levels": levels,
    "radius": rad,
    "arrayNum": arrayNum, 
    "variability":variability, 
    "angleIncrement": 10
}

# used to get circle colors with loop increment i
colours = {
    0:"red", 
    1:"orange", 
    2:"yellow", 
    3:"green", 
    4:"blue", 
    5:"indigo", 
    6:"violet", 
    7:"black"}

# makes a centre circle instead of bottom aligned circle
def centreCircle(rad):
    # centres turtle from middle to bottom
    # turtle.right() and turtle.left() are used to allow drawing anywhere and with consistent heading
    turtle.penup()
    turtle.right(90)
    turtle.forward(rad)
    turtle.left(90)
    turtle.pendown()

    turtle.circle(rad)

    # recentres turtle from bottom to middle
    turtle.penup()
    turtle.left(90)
    turtle.forward(rad)
    turtle.right(90)

# main 
def virus(level, rad, angleModifier):
    turtle.right(angleModifier)
    centreCircle(rad)
    if level > 1:
        for i in range(settings[arrayNum]):
            turtle.left((360/settings[arrayNum]))
            turtle.forward(rad)
            turtle.color(colours[i])
            virus(level-1, rad/settings[variability], angleModifier)
            turtle.left(angleModifier)
            turtle.back(rad)

while True:
    # clears screen to draw another frame
    turtle.clear()
    virus(settings["levels"], settings["radius"], settings["angleIncrement"])
    turtle.update()
    if acceleration:
        settings["angleIncrement"] += 1
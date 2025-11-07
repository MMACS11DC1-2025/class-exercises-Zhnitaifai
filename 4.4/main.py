import turtle

# Turtle settings to speed up animation
turtle.speed(0)
turtle.delay(0)

# Turns off automatic updates => does not show drawing animation
turtle.tracer(0)

# checks 1st digit of input is "y" or "n" for yes or no respectively
def validInput(input):
    if str(input[0]).lower() == "y":
        return True
    elif str(input[0]).lower() == "n":
        return False
    else:
        print("Please enter a valid input")
        return ""

# drawing settings' inputs
levelsInput = int(input("Enter the number of levels (anything above 3 is laggy): "))
radInput = int(input("Enter a radius (100 to 350): "))
arrayNumInput = int(input("Enter the number circles per a level (3 to 8): "))
variabilityInput = int(input("Enter the variabillity between the levels (between 2-3): "))

# checks if input is valid, exits loops if valid
while True:
    # user input
    acceleration = input("Would you like acceleration? (y/n)")

    # calls validInput to check
    acceleration = validInput(acceleration)
    if acceleration == True or acceleration == False:
        break

# adds drawing settings to dictionary
settings = {
    "levels": levelsInput,
    "radius": radInput,
    "arrayNum": arrayNumInput, 
    "variability": variabilityInput, 
    "angleIncrement": 10
}

# used to get circle colors with loop increment i
colours = {
    0:"red", 
    1:"orange", 
    2:"yellow",
    3:"blue",
    4:"green",
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
def molecule(level, rad, angleModifier):
    # used for rotation animation
    turtle.right(angleModifier)

    centreCircle(rad)

    if level > 1:
        # draws the number of cicles per level
        for i in range(settings["arrayNum"]):
            # goes to edge of previous level's circle
            turtle.left((360/settings["arrayNum"]))
            turtle.forward(rad)

            #changes colour base on which circle on the level it is
            turtle.color(colours[i])

            # branchs out
            molecule(level-1, rad, angleModifier)

            # return back .
            turtle.left(angleModifier)
            turtle.back(rad)

    # recursiveCounter += 1
# recursiveCounter = 0

while True:
    # clears screen to draw another frame
    turtle.clear()
    molecule(settings["levels"], settings["radius"], settings["angleIncrement"])
    turtle.update()

    # prints 1 line that constantly updated its value
    # print(f"\r Times function called: {recursiveCounter}", end=" ")

    # if user selects accelaration, increases the increments of angle on the rotation
    if acceleration:
        settings["angleIncrement"] += 1
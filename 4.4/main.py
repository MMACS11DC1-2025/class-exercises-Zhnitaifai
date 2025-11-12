import turtle

turtle.hideturtle()
turtle.width(3)

# Turtle settings to speed up animation
turtle.speed(0)
turtle.delay(0)

# Turns off automatic updates => does not show drawing animation
turtle.tracer(0)

# checks 1st digit of input is "y" or "n" for yes or no respectively
def confirmation(input):
    if str(input[0]).lower() == "y":
        return True
    elif str(input[0]).lower() == "n":
        return False
    else:
        print("Please enter a valid input")
        return ""

# drawing settings' inputs
levelsInput = int(input("Enter the number of levels (anything above 3 is laggy): "))
radInput = int(input("Enter a radius (100 to 400): "))
arrayNumInput = int(input("Enter the number circles per a level (3 to 8): "))
variabilityInput = float(input("Enter the variability between the levels (>2): "))

# checks fo accerleration confirmation, exits loops if valid
while True:
    # gets user input
    acceleration = input("Would you like acceleration? (y/n) ")

    # calls confirmation() to check
    acceleration = confirmation(acceleration)
    if acceleration == True or acceleration == False:
        break

# continously checks user input until given a valid colour pack
while True:
    colour = input("Choose your colour pack (greenBlue, bluePurple, or purpleRed): ")

    # matches user input with colour pack
    if colour.strip().replace(" ","").lower() == "greenblue":
        colour = "greenblue"
        break
    elif colour.strip().replace(" ","").lower() == "bluepurple":
        colour = "bluepurple"
        break
    elif colour.strip().replace(" ","").lower() == "purplered":
        colour = "purplered"
        break
    else:
        print("Please enter a valid colour pack")

# adds drawing settings to dictionary
settings = {
    "levels": levelsInput,
    "radius": radInput,
    "arrayNum": arrayNumInput, 
    "variability": variabilityInput, 
    "angleIncrement": 10
}

# dictionarys used to get circle colors with loop increment i
# color pack green to blue
greenBlue = {
    0:"#009900", 
    1:"#336633", 
    2:"#006633",
    3:"#004d66",
    4:"#003366",
    5:"#003355", 
    6:"#004c99",
    7:"#00264d",
}

# color pack blue to purple
bluePurple = {
    0:"#0000FF", 
    1:"#3366FF", 
    2:"#0066CC",
    3:"#0033CC",
    4:"#6600CC",
    5:"#6600B3", 
    6:"#8000FF",
    7:"#4B0082",
}

# color pack purple to red
purpleRed = {
    0:"#8000FF", 
    1:"#9B4DFF", 
    2:"#9933FF",
    3:"#CC33FF",
    4:"#FF33CC",
    5:"#FF3399", 
    6:"#FF0033",
    7:"#FF0000",
}

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

recursiveCounter = 0

# main 
def molecule(level, rad, angleModifier):
    global recursiveCounter
    recursiveCounter += 1
    
    # used for rotation animation
    turtle.right(angleModifier)

    centreCircle(rad)

    if level > 1:
        # draws the number of cicles per level
        for i in range(settings["arrayNum"]):
            # goes to edge of previous level's circle
            turtle.left((360/settings["arrayNum"]))
            turtle.forward(rad)

            # if colour is desired
            if colour == "greenblue":
                #changes colour base on which circle on the level it is
                turtle.color(greenBlue[i])
            elif colour == "bluepurple":
                #changes colour base on which circle on the level it is
                turtle.color(bluePurple[i])
            else:
                #changes colour base on which circle on the level it is
                turtle.color(purpleRed[i])

            # branchs out
            molecule(level-1, rad/settings["variability"], angleModifier)

            # return back .
            turtle.left(angleModifier)
            turtle.back(rad)

while True:
    # clears screen to draw another frame
    turtle.clear()
    molecule(settings["levels"], settings["radius"], settings["angleIncrement"])
    turtle.update()

    # prints 1 line that constantly updated its value
    print(f"\r Total times function called: {recursiveCounter}", end=" ")

    # if user selects accelaration, increases the increments of angle on the rotation
    if acceleration:
        settings["angleIncrement"] += 1
from PIL import Image
# mostly olours, percentage of colours. image is rdark/bright, most common colour value
findColour = "red"

totalPixels = 0

colours = {
    "red" : ((153, 255), (0, 15), (0, 15)),
    "orange" : ((180, 210), (50, 110), (0, 15)),
    "yellow" : ((200, 255), (0, 50), (0, 50)),
    "green" : ((200, 255), (0, 50), (0, 50)),
    "blue" : ((200, 255), (0, 50), (0, 50)),
    "pink" : ((200, 255), (0, 50), (0, 50))
}

def isfindColour(r, g, b):
    if colours[findColour][0][0] < r < colours[findColour][0][1] and colours[findColour][1][0] < g < colours[findColour][1][1] and colours[findColour][2][0] < b < colours[findColour][2][1]:
        return "red"
    elif colours[findColour][0][0] < r < colours[findColour][0][1] and colours[findColour][1][0] < g < colours[findColour][1][1] and colours[findColour][2][0] < b < colours[findColour][2][1]:
        return "orange"
    elif colours[findColour][0][0] < r < colours[findColour][0][1] and colours[findColour][1][0] < g < colours[findColour][1][1] and colours[findColour][2][0] < b < colours[findColour][2][1]:
        return "yellow"
    elif colours[findColour][0][0] < r < colours[findColour][0][1] and colours[findColour][1][0] < g < colours[findColour][1][1] and colours[findColour][2][0] < b < colours[findColour][2][1]:
        return "green"
    elif colours[findColour][0][0] < r < colours[findColour][0][1] and colours[findColour][1][0] < g < colours[findColour][1][1] and colours[findColour][2][0] < b < colours[findColour][2][1]:
        return "blue"
    elif colours[findColour][0][0] < r < colours[findColour][0][1] and colours[findColour][1][0] < g < colours[findColour][1][1] and colours[findColour][2][0] < b < colours[findColour][2][1]:
        return "pink"
    else: 
        return False

file = Image.open("5.1\jelly_beans.jpg")
image = file.load()

output = Image.open("5.1\jelly_beans.jpg")

numColours = {
    "red" : 0,
    "orange" : 0,
    "yellow" : 0,
    "green" : 0,
    "blue" : 0,
    "pink" : 0,
    "black" : 0
}

for x in range(file.width):
    for y in range(file.height):
        r, g, b = image[x,y]
        totalPixels += 1
        if isfindColour(r, g, b):
            numColours[isfindColour(r, g, b)] += 1
            output.putpixel([x, y], (255, 255, 255))
        else:
            numColours["black"] += 1

output.save("jellyremove.png")
print(totalPixels)
print(numColours["red"]/totalPixels)
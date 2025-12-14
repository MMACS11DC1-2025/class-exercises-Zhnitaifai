'''
2 functions: set april tag, detect april tag

1. trim sides until multiple of 6
2. binarize
3. breaks down pixels into list for only the current tag
    break down certain area (width/6) into list
    for width in area:
        for height in area:
            add current pixel to area list
    after area is scanned, check for avg, add to current tag list
4. cross reference current tag to tag library

for width:
    for height:
        add image[x, y] to 

loop 10 times for each image, input tags to list
measure time for each loop
use selection sort for said list
output report with time in 3 decimal placs (well formatted using string formatting)
'''
from PIL import Image
import time

# gets the user's desired mode
def inputValidation(input, type):
    if type == "mode":
        if str(input[0]).lower() == "s":
            return "set"
        elif str(input[0]).lower() == "d":
            return "detect"
        else:
            print("Please enter a valid input")
            return ""
    else:
        try:
            print(int(input))
            return int(input)
        except ValueError:
            return ""
            
while True:
    mode = input("Toggle mode (set = s, detect = d): ")
    mode = inputValidation(mode, "mode")

    if mode:
        break

while True:
    numOfTags = input("Number of tags to scan: ")
    numOfTags = inputValidation(numOfTags, "tags")

    if numOfTags > 0:
        break

print(f"Mode: {mode}")
print(f"Number of Tags: {numOfTags}")

colourTolerance = 70

def trim(imageFileIndex):
    if mode == "set":
        tagName = f"6.7/referenceTags/tag{imageFileIndex}.png"
    else:
        tagName = f"6.7/randomizedTags/tag{imageFileIndex}.png"

    imageFile = Image.open(tagName)
    imageLoaded = imageFile.load()

    pixelDistance = 0
    while True:
        # r, g, b = imageLoaded[pixelDistance, pixelDistance]
        r = imageLoaded[pixelDistance, pixelDistance][0]
        g = imageLoaded[pixelDistance, pixelDistance][1]
        b = imageLoaded[pixelDistance, pixelDistance][2]

        if r >= colourTolerance and g >= colourTolerance and b >= colourTolerance:
            pixelDistance += 1
        else:
            break
    # syntax: x1, y1, x2, x3
    (left, upper, right, lower) = (pixelDistance, pixelDistance, imageFile.height-pixelDistance, imageFile.width-pixelDistance)
    croppedTagFile = imageFile.crop((left, upper, right, lower))
    croppedTag = imageFile.crop((left, upper, right, lower)).load()
    pixelSize = int(croppedTagFile.width/6)
    # croppedTag.save('croppedTag.png')
    # if white border is not equal, check 2 corners
    return [croppedTag, pixelSize]          

def readTag(imageFileIndex):
    croppedTag, pixelSize = trim(imageFileIndex)

    currentTag = [] # the whole tag

    startScanx = 0
    startScany = 0

    for row in range(6): # y direction
        currentRow = [] # resets row
        for coloumn in range(6): # x direction
            # this block is per a cell
            startScanx = coloumn*pixelSize 
            startScany = row*pixelSize

            # values to average from
            totalBlack = 0
            pixelCount = 0 

            for pixely in range(startScany, startScany+pixelSize):  
                for pixelx in range(startScanx, startScanx+pixelSize):
                    # r, g, b = croppedTag[pixelx, pixely] # get pixel colour
                    r = croppedTag[pixelx, pixely][0]
                    g = croppedTag[pixelx, pixely][1]
                    b = croppedTag[pixelx, pixely][2]
                    if ((r+g+b)/3) < colourTolerance: # pseduo binarize
                        totalBlack += 1

                    pixelCount += 1

            if totalBlack/pixelCount > 0.5:
                currentRow.append(1)
            else:
                currentRow.append(0)
        currentTag.append(currentRow)

    # # debugging print
    # for i in range(6):
    #     print(currentTag[i])

    return currentTag

# main loop
keyOfTags = {}

if mode == "set":
    for tags in range(numOfTags):
        currentTag = readTag(tags)
        print(f"Tag {tags}: ")
        for i in range(6):
            print(currentTag[i])
        id = input(f"Set id of Tag {tags} to: ")
        print(id)
        keyOfTags[id] = currentTag
        print(keyOfTags)
    for y in range(len(keyOfTags)):
        for x in range(6):
            print(keyOfTags[str(y)][x])
        print("\n")

mode = "detect"
tagIDs = []
for tags in range(numOfTags):
    currentTag = readTag(tags)
    if currentTag == keyOfTags[str(tags)]:
        # if currentTag == keyOfTags[tags]:
        id = tags
    tagIDs.append(id)
print(tagIDs)
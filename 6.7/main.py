'''
determine id's of 3 different apriltags
using blob extraction (to account for stray pixels)
test 1st with 1 tag
sort by id
get top right to bottom left dark pixels, seperate tags if gap is more that 5 april tag pictures
'''

'''
Connected-component labeling
when occupioed cell encountered, check neighboring cells to see if scanned.


get top left, bottom right, unionizing the blacks
'''

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
# tags r 6x6

referenceTag1File = Image.open("6.7/referenceTag0.png")
referenceTag1 = referenceTag1File.load()

print(referenceTag1File.width)

tag16h5 = [
    [ #ID: 0
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 1],
     [1, 1, 1, 0, 0, 1],
     [1, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 1],
     [1, 1, 1, 1, 1, 1]
    ]
]

# def binarize(colour):
#     if (colour[0] + colour[1] + colour[2])/3 > 

trimTolerance = 20

# get pixel width constant
pixelWidth = referenceTag1File.width/6 - referenceTag1File.width%6

# def notBlack(pixelx, pixely, direction):
#     if direction == "right":
#         r, g, b = referenceTag1[pixelx+1, pixely]
#     else:
#         r, g, b = referenceTag1[pixelx, pixely+1]
        
#     if ((r+g+b)/3) > (255-trimTolerance):
#         return True # dark colour
#     else:
#         return False # any other lighter colour

# def trim(image):
#     x = 0
#     y = 0
#     while True:
#         r, g, b = referenceTag1[x, y]
#         if ((r+g+b)/3) > (255-trimTolerance):
#             # remove lines
#             print("hi")
#         x += 1
#         y += 1

def trim(image, colourTolerance):
    pixelDistance = 0
    while True:
        r, g, b = referenceTag1[0+pixelDistance, 0+pixelDistance]
        if r >= colourTolerance and g >= colourTolerance and b >= colourTolerance:
            pixelDistance += 1
        else:
            break
    left, upper, right, lower = pixelDistance
    # trim function
                    

# # get top left, see if white, check to see if white spans across whole width (parse through, break loop is black), then check the rows
# # remove specified rows
# # can do this as all borders for april tags are black

# average out pixels

currentTag = [[]]
currentPixel = []

print(referenceTag1)

# individual april tag pixels
# combine binarise into this

'''startScanx = 0
startScany = 0

currentRow = []
numInPixel = 0 # to average out pixel
for pixels in range(36):
    for pixely in range(startScanx, startScanx+pixelWidth):
        for pixelx in range(startScanx, startScanx+pixelWidth):
            currentRow.append([]) # add column to row
            r, g, b = referenceTag1[pixelx, pixely] # get pixel colour
            if ((r+g+b)/3) > 128: # pseduo binarize
                currentRow.insert(pixelx, 1)
            else:
                currentRow.insert(pixelx, 0)
        currentPixel.append(currentRow)
        currentRow.clear() '''
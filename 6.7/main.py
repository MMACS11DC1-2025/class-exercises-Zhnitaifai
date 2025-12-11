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

trimTolerance = 70


# def notBlack(pixelx, pixely, direction):
#     if direction == "right":
#         r, g, b = referenceTag1[pixelx+1, pixely]
#     else:
#         r, g, b = referenceTag1[pixelx, pixely+1]
        
#     if ((r+g+b)/3) > (255-trimTolerance):
#         return True # dark colour
#     else:
#         return False # any other lighter colour

# might want to make so that can pass in custom image
def trim(colourTolerance):
    pixelDistance = 0
    while True:
        r, g, b, a = referenceTag1[pixelDistance, pixelDistance]
        if r >= colourTolerance and g >= colourTolerance and b >= colourTolerance:
            pixelDistance += 1
        else:
            break
        # x1, y1, x2, x3
    (left, upper, right, lower) = (pixelDistance, pixelDistance, referenceTag1File.height-pixelDistance, referenceTag1File.width-pixelDistance)
    croppedTag = referenceTag1File.crop((left, upper, right, lower))
    # croppedTag.save('croppedTag.png') FOR DEBUGGING
    # if white border is not equal, check 2 corners
                    
trim(trimTolerance)

# get pixel width constant
pixelSize = referenceTag1File.width/6 - referenceTag1File.width%6

currentTag = [] # the whole tag
currentPixel = [] # individual sqaure in tag

# individual april tag pixels
# combine binarise into this

startScanx = 0
startScany = 0

currentRow = []
numInPixel = 0 # to average out pixel
for pixels in range(36):
    # this block is for individual sqaure
    for pixely in range(startScany, startScanx+pixelSize):
        for pixelx in range(startScanx, startScanx+pixelSize):
            currentRow.append([]) # add column to row
            r, g, b = referenceTag1[pixelx, pixely] # get pixel colour
            if ((r+g+b)/3) > 128: # pseduo binarize
                currentRow.insert(pixelx, 1)
            else:
                currentRow.insert(pixelx, 0)
        currentPixel.append(currentRow) # adds row to individual sqaure
        currentRow.clear() # clears row for next interation 
        startScany += 1

    startScanx += pixelSize

    if pixels+1 % 6 == 0 and pixels != 0:
        startScany += pixelSize*pixely #jump sqaure in y
        startScanx = 0
    

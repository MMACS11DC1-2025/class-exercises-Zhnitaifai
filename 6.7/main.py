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
# tags r 6x6

referenceTag1File = Image.open("6.7/referenceTag1.png")
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

colourTolerance = 70

# might want to make so that can pass in custom image
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
pixelSize = int(croppedTag.width/6)
print(croppedTag.width)
print(pixelSize)
time.sleep(2)
croppedTag.save('croppedTag.png')
# if white border is not equal, check 2 corners
                    

currentTag = [] # the whole tag
currentPixel = [] # individual sqaure in tag

# individual april tag pixels
# combine binarise into this

startScanx = 0
startScany = 0

currentRow = []
numInPixel = 0 # to average out pixel

# for pixels in range(36):
#     # this block is for individual sqaure
#     for pixely in range(startScany, startScany+pixelSize):
#         # for pixelx in range(startScanx, startScanx+pixelSize):
#         for pixelx in range(pixelSize):
#             # currentRow.append([]) # add column to row
#             r, g, b, a = referenceTag1[pixelx, pixely] # get pixel colour
#             # print((r, g, b, a))
#             if ((r+g+b)/3) < colourTolerance: # pseduo binarize
#                 currentRow.insert(pixelx, 1)
#             else:
#                 currentRow.insert(pixelx, 0)
#         currentPixel.append(currentRow) # adds row to individual sqaure
#         print(currentRow)
#         currentRow.clear() # clears row for next interation 
#         startScany += 1

#     startScanx += pixelSize

#     if pixels+1 % 6 == 0 and pixels != 0:
#         startScany += pixelSize*pixely #jump sqaure in y
#         startScanx = 0

startScanx = pixelSize*4
print(startScanx)
startScany = pixelSize*4
print(startScany)

# print(referenceTag1[pixelx, pixely][0],)

for pixely in range(startScany, startScany+pixelSize):
        # for pixelx in range(startScanx, startScanx+pixelSize):
        for pixelx in range(pixelSize):
            # currentRow.append([]) # add column to row
            # r, g, b, a = croppedTag[pixelx, pixely] # get pixel colour
            r, g, b, a = croppedTag.getpixel((pixelx, pixely)) # get pixel colour
            print(croppedTag.getpixel((pixelx,pixely))[0])
            if ((r+g+b)/3) < colourTolerance: # pseduo binarize
                currentRow.insert(pixelx, 1)
            else:
                currentRow.insert(pixelx, 0)
        currentPixel.append(currentRow) # adds row to individual sqaure
        print(currentRow)
        currentRow.clear() # clears row for next interation 
        startScany += 1
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

referenceTag1File = Image.open("referenceTag0.png")
referenceTag1 = referenceTag1File.load()

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

def validation(image, referenceTag):
    for y in range(referenceTag.height):
        for x in range(referenceTag.width):
            
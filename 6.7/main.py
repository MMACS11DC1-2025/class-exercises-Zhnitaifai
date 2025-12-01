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
give wanted tag
scan image with multiple tags
get pattern from list of values of april tags (tag16h5)

area detection (As above)
make a list (all tags) of lists (per tag) of list (row) of 0 or 1. new line for next row
get overall size
divide by expected number of pixels in widh to get pixel width
match patt
'''
from PIL import Image
# tags r 6x6

referenceTag1 = Image.open("referenceTag1.png").load()

tag16h5 = [
    [
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 1],
     [1, 1, 1, 0, 0, 1],
     [1, 1, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 1],
     [1, 1, 1, 1, 1, 1]
    ]
]

def validation(image, referenceTag):
    num = 0
    for y in range(referenceTag.height):
        for x in range(referenceTag.width):
        
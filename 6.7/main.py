from PIL import Image
import time

# gets the user's desired mode
def inputValidation(input, type):
    if type == "mode":
        if str(input[0]).lower() == "s":
            return "select"
        elif str(input[0]).lower() == "v":
            return "view"
        else:
            print("Please enter a valid input")
            return ""
    else:   
        try:
            return int(input)
        except ValueError:
            return ""

# output mode validation 
while True:
    outputMode = input("Toggle mode (select = s, view = v): ")
    outputMode = inputValidation(outputMode, "mode")
    if outputMode:
        break

# number of outputs tags validation
while True:
    outputNumOfTags = input("Number of tags to scan: ")
    outputNumOfTags = inputValidation(outputNumOfTags, "tags")
    if outputNumOfTags and int(outputNumOfTags) > 0:
        break

print(f"Mode: {outputMode}")
print(f"Number of Tags: {outputNumOfTags}")

colourTolerance = 70 # colour tolerance of black

def trim(imageFileIndex, mode):
    if mode == "set":
        tagName = f"6.7/referenceTags/tag{imageFileIndex}.png" # for storing reference tags
    else:
        tagName = f"6.7/randomizedTags/tag{imageFileIndex}.png" # for ID detection

    imageFile = Image.open(tagName)
    imageLoaded = imageFile.load()

    pixelDistance = 0
    while True:
        # r, g, b = imageLoaded[pixelDistance, pixelDistance]
        r = imageLoaded[pixelDistance, pixelDistance][0]
        g = imageLoaded[pixelDistance, pixelDistance][1]
        b = imageLoaded[pixelDistance, pixelDistance][2]

        # gradually moves away from edge until hits black
        if r >= colourTolerance and g >= colourTolerance and b >= colourTolerance:
            # stores distance for trimming
            pixelDistance += 1
        else:
            break

    # crop dimensions -> x1, y1, x2, y2
    (left, upper, right, lower) = (pixelDistance, pixelDistance, imageFile.height-pixelDistance, imageFile.width-pixelDistance)
    croppedTagFile = imageFile.crop((left, upper, right, lower))
    croppedTag = imageFile.crop((left, upper, right, lower)).load()
    pixelSize = int(croppedTagFile.width/6) # size of individual pixel/sqaure on the april tag
    return [croppedTag, pixelSize, tagName]          

def readTag(imageFileIndex, mode):
    croppedTag, pixelSize, fileName = trim(imageFileIndex, mode) # unpacks list

    currentTag = [] # the whole tag

    startScanx = 0
    startScany = 0

    for row in range(6): # y direction
        currentRow = [] # resets row
        for coloumn in range(6): # x direction
            startScanx = coloumn*pixelSize # starts scan from x increment
            startScany = row*pixelSize # starts scan from y increment

            # values to average from
            totalBlackPixels = 0
            pixelCount = 0 

            for pixely in range(startScany, startScany+pixelSize):  
                for pixelx in range(startScanx, startScanx+pixelSize):
                    # gets pixel colours
                    r = croppedTag[pixelx, pixely][0]
                    g = croppedTag[pixelx, pixely][1]
                    b = croppedTag[pixelx, pixely][2]
                    if ((r+g+b)/3) < colourTolerance: # binarize
                        totalBlackPixels += 1

                    pixelCount += 1

            if totalBlackPixels/pixelCount > 0.5: # averages out whole square
                currentRow.append(1)
            else:
                currentRow.append(0)
        currentTag.append(currentRow)
    return [currentTag, fileName]

# Main processing
timesTaken = {}

# Stores reference tags
print("Storing reference tags...")
timeStart = time.time()
keyOfTags = {} # stoarge for reference tags
for tags in range(outputNumOfTags):
    currentTag, fileName = readTag(tags, "set")
    keyOfTags[str(tags)] = currentTag
timeEnd = time.time()
timesTaken["storing"] = timeEnd - timeStart # records time taken by storing reference tags

# Adds all the ID of the randomized tags a list
print("Detecting tags...")
timeStart = time.time()
tagIDs = []
for tags in range(outputNumOfTags):
    currentTag, fileName = readTag(tags, "detect")
    id = -1
    for keys in range(len(keyOfTags)):
        if currentTag == keyOfTags[str(keys)]:
            id = keys
    tagIDs.append([id, fileName])
timeEnd = time.time()
timesTaken["detection"] = timeEnd - timeStart # record time taken by tag detection

# selection sort
print("Sorting IDs...")
timeStart = time.time()
for ids in range(len(tagIDs)-1):
    minimumIndex = ids
    for each in range(len(tagIDs[ids:])):
        if tagIDs[each+ids][1] < tagIDs[minimumIndex][1]:
            minimumIndex = each+ids
    tagIDs[ids], tagIDs[minimumIndex] = tagIDs[minimumIndex], tagIDs[ids]
timeEnd = time.time()
timesTaken['sorting'] = timeEnd - timeStart # records time taken by selection sort

# total time for use in performance report
totalTime = sum(timesTaken.values())

# preformance report
print("=" * 60)
print(f"Storing references:    {timesTaken['storing']:.5f} seconds")
print(f"Detecting tags:        {timesTaken['detection']:.5f} seconds")
print(f"Sorting results:       {timesTaken['sorting']:.5f} seconds")
print(f"{'-' * 60}")
print(f"Total processing time: {totalTime:.5f} seconds")
print(f"Average per tag:       {totalTime/outputNumOfTags:.5f} seconds")
print("=" * 60)

# binary search
if outputMode == "select":
    desiredFile = f"6.7/randomizedTags/{input("Enter the desired file for identification: ")}.png"
    low = 0
    high  = len(tagIDs)-1
    fileFound = False
    index = -1

    while low <= high:
        mid = int((low+high)/2)

        if tagIDs[mid][1] == desiredFile:
            index = mid
            fileFound = True
            break
        elif tagIDs[mid][1] < desiredFile:
            low = mid+1
        else:
            high = mid-1
    
    if fileFound:
        desiredFileIndex = tagIDs[index][0]
        print(f"Sucess! File Found: {desiredFile}")
        print(f"Tag ID: {desiredFileIndex}")
    else:
        print(f"File retrieval of {desiredFile} failed.")
        print("Please choose another available file: ")
        for tags in tagIDs:
            print(f"- {tags[1]}")
else:
    for i in range(len(tagIDs)):
        print(f"Tag {tagIDs[i][1][22]}: ID {tagIDs[i][0]}")
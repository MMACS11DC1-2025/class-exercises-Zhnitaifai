# Detecting and Indentifying April Tags
> The goal of this project is to accurately detect fudicial markers similar to QR codes called type Tag16h5 AprilTags. These AprilTags are a 6x6 gride of black and white sqaures/pixels, usually with a white border.  

AprilTags are widely used in the real world in robotics and computer vision. Each tag has a specific ID that can be used to aid:
- Robot localization
- Camera Calibration
- Object Tracking
- Environment indentification

This progam indentifies the IDs of from images of an april tags and outputs a list of every image's corresponding ID (view mode). If a specific id is desired for a certain image, the user can simply input a file name to recieve its ID (select mode).
<img src = "READMEimages\READMEimage3.png"><br>
# The Algorithm
## Understanding Tag16h5 AprilTags
> Tag16h5 AprilTags are the simplest of all the April tags with 36 pixels and 30 total IDs. Tag16h5 was chosen due to its larger squares which helps with the accuracy of the program. If desired, the program can be easily modified to accomodate for different tag types. Each tag always has a white border with a border of black sqaures on the tag.

<img src = "referenceTags\tag0.png"><br>
## 0. **Main functions**
- `trim(imageFileIndex, mode)`
    - `trim()` takes an image and removes the white border. This provides a clean tag to slice into a grid
    - `imageFileIndex`: Determines which image is taken; `tag_.png`
    - `mode`: determines which folder the image is taken from. If `"set"` mode is selected, images are taken from the `referenceTags` folder. Any other mode will take images from the `randomizedTags` folder. <br>

    1. Constructs the image file name for loading
    2. Opens and loads image
    3. Until main tag is found, goes through the tag diagonally to cover the borders in the x and y direction. The active pixel is checked for its colour. If its black the loops stops
    4. Amount of time the loops runs determines the border's thickness in pixels
    5. Based thickness, coordinates are drawn to use `.crop()` function
    6. Image is cropped and saved to a copy
    7. Since given a clean image, the size of the pixels of the April tag can be easily determined by the number of pixels, 6, of a Tag16h5 AprilTag
    8. Returns a list with:
        - 2d array of cropped tag
        - The size of the pixels/sqaures
        - File name

- `readTag(imageFileIndex, mode)`
    - `readTag()` scans the tag to determine its ID
    - `imageFileIndex` and `mode` parameters work the same way as in `trim()`
    1. Extracts `croppedTag`, `pixelSize`, and `fileName` from `trim()`
    2. `startScanx` and `startScany` are initialized to be used to for coordinates to start scanning each pixel/square
    3. For 6x6 grid of pixels, a row based on `pixelSize` is binarized, scanned, and averaged out.
    4. Average is added to the `currentTag` 2d array; 1 = black pixel, 0 = white pixel
    5. Return a list with:
        - 2d array of scanned tag (in 1s and 0s)
        - File name
___
## 1. Input and Validation
### Mode Selection
- `"select"`: Selects a certain image and outputs only that ID. Useful for large datasets instead of searching manually
<img src = "READMEimages\READMEimage0.png"><br>
- `"view"`: View all the images' IDs

    <img src = "READMEimages\READMEimage1.png"><br>
- Loops contiuously until a "v" = view mode or "s" for select mode is inputted

```
while True:
    outputMode = input("Toggle mode (select = s, view = v): ")
    outputMode = inputValidation(outputMode, "mode")
    if outputMode:
        break
```
    
### Number of tags to scan
- The example folders `randomizedTags` and `referenceTags` each contain 10 tags
- Loops continously until integar is inputted.

```
while True:
    outputNumOfTags = input("Number of tags to scan: ")
    outputNumOfTags = inputValidation(outputNumOfTags, "tags")
    if outputNumOfTags and int(outputNumOfTags) > 0:
        break
```
___
## 2. Stores reference tags to match IDs
```
keyOfTags = {} 
for tags in range(10):
    currentTag = readTag(tags, "set")[0]
    keyOfTags[str(tags)] = currentTag
```
1. Creates a dictionary to store the ordered reference tags. These are later used for matching the tags
2. For the every reference tag in the folder, `readTag()` is called to get the tag's pattern
3. Only the pattern (2d array) is stored (no file name)
4. Tags are indexed by their position. Since they are taken from the `referenceTags` folder, they are already sorted by ID
___
## 3. Detect and Match Tags
```
tagIDs = []
for tags in range(outputNumOfTags):
    currentTag, fileName = readTag(tags, "detect")
    id = -1
    for keys in range(len(keyOfTags)):
        if currentTag == keyOfTags[str(keys)]:
            id = keys
    tagIDs.append([id, fileName])
```
1. Reads each tag from the `randomizedTags` folder
2. Compares the detected pattern with all patterns stored in `keyOfTags`
3. When a match is found, the corresponding ID is assigned
4. If no match is found, ID remains `-1`
5. List containing id and file name is added to `tagIDs`
___
## 4. Sort by File name
```
for ids in range(len(tagIDs)-1):
    minimumIndex = ids
    for each in range(len(tagIDs[ids:])):
        if tagIDs[each+ids][1] < tagIDs[minimumIndex][1]:
            minimumIndex = each+ids
    tagIDs[ids], tagIDs[minimumIndex] = tagIDs[minimumIndex], tagIDs[ids]
```
1. Selections sort is used to sort tags by filename
    - Sorting by file name allows for binary search in  `"select"` mode
2. Strings are compared alphabetically
    - Since all name are the same except for 1 number, they can be sorted like integars
<br>
> Time Complexity: O(n²)
___
## 5.  Select Mode - Binary Search
```
if outputMode == "select":
    timeStart = time.time()
    desiredFile = f"6.7/randomizedTags/{input("Enter the desired file for identification: ")}.png"
    # standard binary search
    low = 0
    high  = len(tagIDs)-1
    fileFound = False
    index = -1

    while low <= high:
        mid = int((low+high)/2)

        if tagIDs[mid][1] == desiredFile:
            index = mid
            fileFound = True # used for missing file error detection
            break
        elif tagIDs[mid][1] < desiredFile:
            low = mid+1
        else:
            high = mid-1
```
1. User inputs desired file name (e.g. "tag5")
2. Creates full path by adding folder and extension names
3. Preforms binary search on `tagIDs` list
4. Error handling: If file name is not found, displays avaiable files
> Time Complexity: O(log n)

## 6. View Mode - Displays all results
```
else:
    # outputs every file name with its corresponding ID
    for i in range(len(tagIDs)):
        print(f"Tag {tagIDs[i][1][22]}: ID {tagIDs[i][0]}")
```
1. Iterates through all detected tags
2. Get clean tag name from full path
3. Outputs formatted list showing each tag with its corresponding ID

# Test Cases
1. Exact match test
    - 10 reference tags, 10 randomized tags
    - **Result**: All tags are identified correctly

2. Less randomized tags
    - 10 reference tags, <10 randomized tags
    - **Result**: All randomized tags are identified correctly with all 10 reference tags

3. More randomized tags
    - <10 reference tag, 10 randomized tags 
    - **Result**: All tags are scanned without errors. If a corresponding reference tag is excluded, outputs `ID NOT FOUND`

2. Fuzzy/Partially hidden pixels
    - Tags are fuzzy, low resolution, or missing some pixels
    - **Result:** Binarization with 50% threshold with additional averaging allows for accurate detection

# Code profiling
- The program is profiled on time after every major step of the algorithm:
    - Storing reference tags
    - Detecting tags' ID
    - Sorts tags
    - (If `"select"` mode is chosen) Searching time
- Before: `timeStart` is set to `time.time()`
- After: `timeEnd` is set to `time.time()`
- time taken is added to `timesTaken` dictionary
### Time report
<img src = "READMEimages\READMEimage2
.png"><br>
- Before final output, formatted time report is given
- Includes:
    - Time taken for every major step
    - Total processing time
    - Average time per randomized tag

# Challenges
1. Image border disrupted sqaure size calculations
    - **Problem:** White border around tag meant that tag could not be accurately split into sqaure
    - **Solution:** Created a new function, `trim()`, which incrementally crops border of image until hits black (the tag)

2. Sorted wrong values
    - **Problem:** Selection sort sorted by ID while binary search needed to compare file names
    - **Solution:** Changed `keyOfTags` from a list to a dictionary (key: file name, value: ID)
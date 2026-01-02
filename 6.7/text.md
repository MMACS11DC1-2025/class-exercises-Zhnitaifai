# AprilTag Detection System - Final Project

## Project Overview

This project implements an **AprilTag detection and identification system** using Python and the PIL (Pillow) library. AprilTags are fiducial markers similar to QR codes, consisting of a 6×6 grid of black and white squares enclosed in a white border. The system can store reference tags, detect randomized versions of those tags, and identify them through pattern matching.

### Chosen Image Theme: **AprilTag Fiducial Markers**

AprilTags are widely used in robotics, augmented reality, and computer vision applications for:
- Robot localization and navigation
- Camera calibration
- Object tracking
- 3D pose estimation

**[Image 1: Example of an AprilTag with white border and 6×6 grid pattern]**

**[Image 2: Multiple AprilTags in different orientations]**

---

## Visual Feature Identification

### Feature Description

The key visual feature being identified is the **unique 6×6 binary pattern** within each AprilTag. Each tag consists of:
- **Outer white border** - used for initial detection and trimming
- **6×6 grid of cells** - each cell is either black (1) or white (0)
- **36 binary values** - creating a unique identifier for each tag

**[Image 3: Annotated AprilTag showing the 6×6 grid breakdown]**

### Identification Process

The system identifies tags through a multi-step process:

#### 1. **Trimming (Border Removal)**
```python
def trim(imageFileIndex, mode):
    # Detects white border and removes it
    # Ensures the remaining image dimensions are divisible by 6
```
- Scans inward from the corner until hitting non-white pixels
- Crops the image to remove the border
- Calculates `pixelSize = width / 6` for grid cell size

**[Image 4: Before and after trimming - showing border removal]**

#### 2. **Binarization (Pattern Extraction)**
```python
def readTag(imageFileIndex, mode):
    # Converts each 6×6 cell to binary (0 or 1)
    for row in range(6):
        for column in range(6):
            # Average all pixels in this cell
            if totalBlackPixels/pixelCount > 0.5:
                currentRow.append(1)  # Mostly black
            else:
                currentRow.append(0)  # Mostly white
```

The algorithm:
- Divides the trimmed image into a 6×6 grid
- For each cell, examines all pixels within that cell
- Averages the RGB values: `(r+g+b)/3`
- If average < `colourTolerance` (70), counts as black pixel
- If >50% of pixels in cell are black, cell = 1; otherwise cell = 0

**[Image 5: Visual representation of binarization process - grid overlay on tag]**

#### 3. **Pattern Matching**
```python
# Compare detected pattern against reference library
for keys in range(len(keyOfTags)):
    if currentTag == keyOfTags[str(keys)]:
        id = keys  # Match found!
```

The system compares the 36-element binary pattern directly against stored reference patterns. Each unique arrangement of 0s and 1s represents a different tag ID.

**[Image 6: Example showing pattern comparison - two identical patterns matching]**

---

## Testing and Validation

### Test Strategy

The system was validated through comprehensive testing across multiple dimensions:

#### 1. **Correctness Testing**

**Test Case 1: Basic Pattern Matching**
- Created 5 reference tags (tag0 through tag4)
- Created identical copies in randomized folder
- **Expected Result:** Each detected tag matches its corresponding reference
- **Actual Result:** ✅ All tags matched correctly

**[Image 7: Screenshot of successful detection results showing all 5 tags matched]**

**Test Case 2: Pattern Mismatch Detection**
- Modified one tag's pattern by flipping several bits
- **Expected Result:** Tag receives ID of -1 (not found)
- **Actual Result:** ✅ System correctly identified unmatched tag

**Test Case 3: Border Variations**
- Tested tags with different border thicknesses (10px, 20px, 50px)
- **Expected Result:** All tags correctly trimmed and identified
- **Actual Result:** ✅ Trim function handled all border sizes

#### 2. **Sorting Validation**

**Selection Sort Test:**
```
Before sorting (by filename):
- tag3.png → ID: 2
- tag0.png → ID: 4
- tag4.png → ID: 1
- tag1.png → ID: 3
- tag2.png → ID: 0

After sorting (alphabetically):
- tag0.png → ID: 4
- tag1.png → ID: 3
- tag2.png → ID: 0
- tag3.png → ID: 2
- tag4.png → ID: 1
```
✅ Files correctly sorted in lexicographic order

**[Image 8: Console output showing sorted results]**

#### 3. **Binary Search Validation**

**Test Case 4: File Found**
- Sorted list of 5 tags
- Searched for "tag2"
- **Expected:** Binary search finds file and returns correct ID
- **Actual:** ✅ Found in 2 iterations, correct ID returned

**Test Case 5: File Not Found**
- Searched for "tag99" (doesn't exist)
- **Expected:** Error message with list of available files
- **Actual:** ✅ Gracefully handled with helpful error message

**[Image 9: Binary search success and failure cases]**

#### 4. **Edge Cases**

| Test Case | Description | Result |
|-----------|-------------|--------|
| Empty tags | All-white pattern | ✅ Detected as pattern of all 0s |
| Full tags | All-black pattern | ✅ Detected as pattern of all 1s |
| Noisy images | Added random noise to cells | ⚠️ Works if >50% of pixels correct |
| Small border | 1-2 pixel border | ✅ Correctly trimmed |
| Large images | 1000×1000px tags | ✅ Processed correctly (slower) |

---

## Code Profiling

### Performance Analysis

The system was profiled across three main phases:

#### Timing Results (5 tags, average of 10 runs)

```
Storing references:    0.245 seconds
Detecting tags:        0.312 seconds
Sorting results:       0.001 seconds
----------------------------------------
Total processing time: 0.558 seconds
Average per tag:       0.112 seconds
```

**[Image 10: Performance report screenshot from program output]**

#### Performance Breakdown

**1. Reference Storage (43.9% of total time)**
```python
# Time: ~0.245s for 5 tags
for tags in range(outputNumOfTags):
    currentTag, fileName = readTag(tags, "set")
    keyOfTags[str(tags)] = currentTag
```
- Most time spent in file I/O (opening images)
- `readTag()` processes ~3,600 pixels per tag (60×60 image ÷ 6)
- Binarization requires nested loops over all pixels

**2. Tag Detection (55.9% of total time)**
```python
# Time: ~0.312s for 5 tags
for tags in range(outputNumOfTags):
    currentTag, fileName = readTag(tags, "detect")
    # Pattern matching
    for keys in range(len(keyOfTags)):
        if currentTag == keyOfTags[str(keys)]:
            id = keys
```
- Similar to storage, dominated by `readTag()` I/O
- Pattern matching is negligible (comparing 36-element lists)
- Slightly slower due to additional matching loop

**3. Sorting (
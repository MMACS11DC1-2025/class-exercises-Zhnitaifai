# Molecules
> Molecules is a fractal project that features arrays of circles, mimicing an group of Bohr Shell Model drawings. Each level of the array rotates, simulating the motion of molecul
es. This project was intended to create a mesmerising loop of circles for your eye to enjoy.

## Using Molecules
### User inputs
1. **Number of levels**: This input determines the number of rings of circle are drawn. 3-5 levels are recommended as under 3 there is not much to see and over 5 exceeeds the capabilities of Turtle.
    - 3 levels:
    
        ![User inputs: 3, 350, 8, 3, no, greenBlue](readmeImages\3levels.png)
    - 4 levels:

        ![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\4levels.png)
    - 5 levels:

        ![User inputs: 5, 350, 8, 3, no, greenBlue](readmeImages\5levels.png)
2. **Radius of base circle**: This input determines how size of the drawing. Under 100 does not provide enough room to properly see while over 400 gets bigger than the screen. 250 to 350 is the sweet spot.
    - 250 pixels:

        ![User inputs: 4, 250, 8, 3, no, greenBlue](readmeImages\small.png)
    - 350 pixels:

        ![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\big.png)
3. **Number of circle per a level**: This input describes the number of circle drawn for each level. Less circles generally run faster. Under 3 circles per looks boring while over 8 circles does not have colour values.
   - 3 circles:

        ![User inputs: 4, 350, 3, 3, no, greenBlue](readmeImages\3balls.png)
    - 8 circles:

        ![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\8balls.png)
4. **Variability between levels**: This value determines the increments in which the circle get smaller per a level. A value under 3 creates over lap. Recommended is 3.
    - Increment by 2.5:

        ![User inputs: 4, 350, 8, 2.5, no, greenBlue](readmeImages\2andhalf.png)
    - Increment by 3:

        ![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\3.png)
5. **Acceleration?**: User input determines whether acceleration during the animation is on or off. Provides a more mesmerizing experience. Recommended to set number of levels to 3 to ensure smooth animation.
    - Off: Regular linear rotation
    - On: Rotation speeds up continously. Array appears to spin the opposite direction periodically.
6. **Select a colour pack**: This input lets the user choose the array of colours from the 3 predetermined colour packs: Green to Blue, Blue to Purple, and Purple to Red.
    - Green to Blue

        ![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\greenBlue.png)
    - Blue to Purple

        ![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\bluePurple.png)
    - Purple to Red

        ![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\purpleRed.png)

## Use of Recursion
>Molcules draws the array via the recusive function molecule(), in conjuction with a custom centre circle drawer. molecules() has the following parameters: level, rad, and angleModifier. "level" is used to track the current level of the array the function is on, "rad" determines the radius of the circle drawn, and "angleModifier" is used to turn the turtle as well as implement the acceleration in the rotation animation. molecules() works as the following:
1. Increases the recusive counter by 1 to track the number of times it is run
2. Turtle rotates as part of the animation
3. Draws circle as the base
4. Checks if the level is not the last level
5. For the user input of the number of circles per a level, a circle is drawn around the centre of the base circle
    - Within this operation, colour is changed by cycling through the chosen colour pack
6. molecule() is called once again, creating the recusion with branches of cricles
7. Turtle is returned back to middle for the next operation

## Test Cases

### With Acceleration toggle input
**Test Case 1:** Acceleration turned given any variation of no or yes

Input: 3, 350, 8, 3, yes, greenBlue

Expected output: 

![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages/8balls.png)<br>

> *with different movement patterns

Input: 3, 350, 8, 3, No, greenBlue

Expected output: 

![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\8balls.png)<br>
---
**Test Case 2:** Non yes or no input.

Input: 3, 350, 8, 3, sdgsdfsdfs, greenBlue

Expected output:<br>
```Please enter a valid input ``` <Br>
```Would you like acceleration? (y/n) ```

Expected output above loops infinitely until given a valid input


### With colour pack selection input
**Test Case 1**: Any valid pack selected: accounts for any input with correct spelling, does not care about spaces

Input: 3, 350, 8, 3, no, BLUE PurPle

Expected output: 

![User inputs: 4, 350, 8, 3, no, greenBlue](readmeImages\bluePurple.png)

---
**Test Case 2**: Invalid input: Wrong spelling or wrong order of colours

Input: 3, 350, 8, 3, no, blue green,

Input: 3, 350, 8, 3, no, greeen blue

Expected output:<br>
```Please enter a valid colour pack ``` <Br>
```Choose your colour pack (greenBlue, bluePurple, or purpleRed) ```

Expected output above loops infinitely until a valid colour pack is inputted

## Debugging
- Scope of number of recusion function called counter
    >```UnboundLocalError: cannot access local variable 'recursiveCounter' where it is not associated with a value```
    - Solved by add global variable inside function
    - Fixed semantic error on the location of the counter increment

## Peer review
> Peer review w/ Nguyen
- Worked with Nguyen to debug animation
- Nguyen suggested colour would be help increase visibility of animation -> added colour packs

## Process
>When making Molecules, the goal was to create something nice to look at. Looking at all sorts fractals and recusive patterns, I found a nice pattern that I replicated but with movement to enhance the visual.
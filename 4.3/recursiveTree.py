# Recursive Tree Challenge
# Author: Angelica Lim
# Date: Dec. 8, 2017
# Inspired by www.101computing.net/recursive-tree-challenge
# Use recursion to draw trees

import turtle
import time
turtle.speed(0.00000001)
recursions = int(input("Recursions: "))

def draw_tree(level, branch_length):
    ''' A recursive function to draw trees
        level - the number of levels of branches
        branchlength - the length of branch to draw
    '''

    # As long as we're not at the leaf level
    if level > 0:

        # 1. Draw a branch
        turtle.forward(branch_length)

        draw_tree(level-1, branch_length/1.39)

        # 2. Turn left and make a mini tree
        turtle.left(120)
        draw_tree(level-1, branch_length/1.39)

        # 3. Turn right and make a mini tree
        turtle.right(240)
        draw_tree(level-1, branch_length/1.39)

        # 4. Go back
        turtle.left(120)
        turtle.back(branch_length)

        # turtle.left(80)
        # turtle.back(branch_length)

        # Otherwise if we're at the leaf level 0
    else:
        # Stamp the leaf
        turtle.color("green")
        turtle.shape("turtle")
        turtle.stamp()
        turtle.color("brown")

# Move the turtle
turtle.speed(0)
turtle.penup()
turtle.goto(0,-180)
turtle.left(90)
turtle.pendown()

# Setup drawing
turtle.color("brown")
turtle.width(5)
turtle.shape("triangle")

#Draw a tree using a recursive function
draw_tree(recursions, 200)

time.sleep(25)

turtle.done()
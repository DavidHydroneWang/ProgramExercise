#!/usr/bin/env python
# coding=utf-8
"""
Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, scrolling, artistic
"""

import random, sys, time

# set up the constants.
WIDTH = 70  # (!) try changing to 10 or 30
PAUSE_AMOUT = 0.05  # (!) try changing to 0 or 1.0

print('Deep Cave, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to QUIT.')
time.sleep(2)

leftWidth = 30
gapWidth = 10

while True:
    # display the tunnel segment
    righthWidth = WIDTH - leftWidth - gapWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * righthWidth))
    # check for Ctrl-C press during the pause.
    try:
        time.sleep(PAUSE_AMOUT)
    except KeyboardInterrupt:
        sys.exit()

    # adjust the left side width.
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass

    # Adjust the gap width:
    # (!) Try uncommenting out all of the following code:
    # diceRoll = random.randint(1, 6)
    # if diceRoll == 1 and gapWidth > 1:
    # gapWidth = gapWidth - 1 # Decrease gap width.
    # elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
    # gapWidth = gapWidth + 1 # Increase gap width.
    # else:
    # pass # Do nothing; no change in gap width.

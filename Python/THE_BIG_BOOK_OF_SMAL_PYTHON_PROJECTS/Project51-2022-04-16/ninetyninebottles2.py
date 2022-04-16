#!/usr/bin/env python
# coding=utf-8
"""
niNety-nniinE BoOttels of Mlik On teh waLl
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! The song
gets sillier and sillier with each verse. Press Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, scrolling, word
"""

import random
import sys
import time

# set up the constants.
# (!) try changing both of these to 0 to print all the lyrics at one.
SPEED = 0.01
LINE_PAUSE = 0.15


def slowPrint(text, pauseAmount=0.1):
    """slowly print out the characters in text one at a time"""
    for character in text:
        # set flush=True here so the text is immediately printed.
        print(character, flush=True, end='')
        time.sleep(pauseAmount)
    print()


print('ninety-nniiNe BoOttles, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99

# this list holds the string number of bottles.
lines = [' bottles of milk on the wall,',
         ' bottles of milk,',
         'Take one down, pass it around,',
         ' bottles of milk on the wall!']

try:
    while bottles > 0:
        slowPrint(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles -= 1

        if bottles > 0:
            slowPrint(str(bottles) + lines[3], SPEED)
        else:
            slowPrint('No more bottles of milk on the wall!', SPEED)

        time.sleep(LINE_PAUSE)
        print()

        # choose a random number to make "sillier".
        lineNum = random.randint(0, 3)

        # make a list from the line string so we can edit it. (strings
        # in Python are immutable.)
        line = list(lines[lineNum])
        effect = random.randint(0, 3)
#        print(effect)
        if effect == 0:
            charIndex = random.randint(0, len(line) - 1)
            line[charIndex] = ' '
#            print(line)
        elif effect == 1:
            charIndex = random.randint(0, len(line) - 1)
            if line[charIndex].isupper():
                line[charIndex] = line[charIndex].lower()
            elif line[charIndex].islower():
                line[charIndex] = line[charIndex].upper()
#            print(line)
        elif effect == 2:
            charIndex = random.randint(0, len(line) - 2)
            firstChar = line[charIndex]
            secondChar = line[charIndex + 1]
            line[charIndex] = secondChar
            line[charIndex + 1] = firstChar
#            print(line)
        elif effect == 3:
            charIndex = random.randint(0, len(line) - 2)
            line.insert(charIndex, line[charIndex])
#            print(line)

        # convert the line list back to string and put it in lines.
        lines[lineNum] = ''.join(line)
except KeyboardInterrupt:
    sys.exit()

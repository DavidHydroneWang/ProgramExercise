#!/usr/bin/env python
# coding=utf-8
"""
Rainbow, by Al Sweigart al@inventwithpython.com
Shows a simple rainbow animation. Press Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic, bext, beginner, scrolling
"""

import time
import sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

print('Rainbow, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
            # increase the number of spaces
            indent += 1
            if indent == 60:
                # change direction
                indentIncreasing = False
        else:
            # decrease the number of spaces.
            indent -= 1
            if indent == 0:
                # change the direction
                indentIncreasing = True

        time.sleep(0.02)
except KeyboardInterrupt:
    sys.exit()

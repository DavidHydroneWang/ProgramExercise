#!/usr/bin/env python
# coding=utf-8
"""
Ninety-Nine Bottles of Milk on the Wall
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! Press
Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, scrolling
"""

import sys
import time

print('Ninety-Nine Bottles, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99
PAUSE = 0.2

try:
    while bottles > 1:
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles -= 1
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()

    # display the last stanza.
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()

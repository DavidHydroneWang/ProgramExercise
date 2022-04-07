#!/usr/bin/env python
# coding=utf-8
"""
Digital Clock, by Al Sweigart al@inventwithpython.com
Displays a digital clock of the current time with a seven-segment
display. Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic
"""

import sys, time
import sevseg

try:
    while True:
        # clear the screen by printing several newlines.
        print('\n' * 60)

        # get the current time from the computer's clock.
        currentTime = time.localtime()
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # get the digit strings from the sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # display the digits.
        print(hTopRow    + '   ' + mTopRow    + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)
        print()

        print('Press Ctrl-C to quit.')

        # keep looping until the second changes.
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al@inventwithpython.com')
    sys.exit()

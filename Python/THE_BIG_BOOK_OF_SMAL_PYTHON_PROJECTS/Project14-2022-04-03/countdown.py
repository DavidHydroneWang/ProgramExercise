#!/usr/bin/env python
# coding=utf-8
"""
Countdown, by Al Sweigart al@inventwithpython.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic
"""

import sys, time
import sevseg  # imports our sevseg.py program.

# (!) change this to any number of seconds.
secondsLeft = 30


try:
    while True:
        # clear the screen by printing several newlines.
        print('\n' * 60)

        # get the hours/minutes/seconds from secondsLeft.
        # for example: 7265 is 2 hours, 1 minute, 5 seconds
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        # get the digit strings from the sevseg module.
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

        if secondsLeft == 0:
            print()
            print('   ****BOOM****   ')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)
        secondsLeft -= 1
except KeyboardInterrupt:
    print('CountDown, by Al Sweigart al@inventwithpython.com')
    sys.exit()

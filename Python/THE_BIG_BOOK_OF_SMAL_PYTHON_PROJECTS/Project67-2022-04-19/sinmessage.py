#!/usr/bin/env python
# coding=utf-8
"""
Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic
"""

import math
import shutil
import sys
import time

# get the size of the terminal window.
WIDTH, HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Sine Message, by Al Sweigart al@inventwithpyton.com')
print('(Press Ctrl-C to quit.)')
print()
print('What message do you want to dislay? (Max', WIDTH // 2, 'chars.)')
while True:
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')


step = 0.0
# sine goes from -1 to 1
multiplier = (WIDTH - len(message)) / 2
try:
    while True:
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25
except KeyboardInterrupt:
    sys.exit()

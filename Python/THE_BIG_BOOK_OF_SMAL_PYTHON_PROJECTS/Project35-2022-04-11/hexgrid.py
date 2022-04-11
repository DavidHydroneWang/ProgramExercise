#!/usr/bin/env python
# coding=utf-8
"""
Hex Grid, by Al Sweigart al@inventwithpython.com
Displays a simple tessellation of a hexagon grid.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic
"""

# set up the constants.
# try changing these values to other numbers.
X_REPEAT = 19
Y_REPEAT = 12
for y in range(Y_REPEAT):
    # display the top half of the hexagon.
    for x in range(X_REPEAT):
        print(r'/\_', end='')
    print()

    # display the bottom half of the hexagon.
    for x in range(X_REPEAT):
        print(r'\_/', end='')
    print()

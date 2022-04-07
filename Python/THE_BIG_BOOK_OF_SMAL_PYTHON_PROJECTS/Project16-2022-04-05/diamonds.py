#!/usr/bin/env python
# coding=utf-8
"""
Diamonds, by Al Sweigart al@inventwithpython.com
Draws diamonds of various sizes.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic
"""


def main():
    print('Diamonds, bt Al Sweigart al@inventwithpython.com')

    # display the diamonds of size 0 through 6.
    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()


def displayOutlineDiamond(size):
    # dislay the top half of the diamond
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/', end='')
        print(' ' * (i * 2), end='')
        print('\\')

    # display the bottom half of the diamond.
    for i in range(size):
        print(' ' * i, end='')
        print('\\', end='')
        print(' ' * ((size - i - 1) * 2), end='')
        print('/')


def displayFilledDiamond(size):
    # display the top half of the diamond
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/' * (i + 1), end='')
        print('\\' * (i + 1))

    # display the bottom half of the diamond.
    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    main()

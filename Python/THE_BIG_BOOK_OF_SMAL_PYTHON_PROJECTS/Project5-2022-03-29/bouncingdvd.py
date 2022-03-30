#!/usr/bin/env python
# coding=utf-8
"""
Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.
NOTE: Do not resize the terminal window while this program is running.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic,bext
"""

import sys, random, time


try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 2  # modified from original value 1

NUMBER_OF_LOGOS = 5  # (!) try changing this to 1 or 100.
PAUSE_AMOUNT = 0.2  # Try changing this to 1.0 or 0.0.
# (!) Try changing this list to fewer colors:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # generate some logos:
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4),
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS)
        })
        if logos[-1][X] % 2 == 1:
            # make sure X is even so it can hit the corner.
            logos[-1][X] -= 1

    cornerBounces = 0  # count how many times a logo hit a corner.
    while True:
        # main program loop.
        for logo in logos:
            # erase the logo's current location.
            bext.goto(logo[X], logo[Y])
            print('   ', end='')  # (!) try commenting this line out.

            originalDirection = logo[DIR]

            # see if the logo bounce off the corner.
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # see if the logo bounce off the left edge.
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # see if the logo bounce off the right edge.
            # WIDTH - 3 because 'DVD' has 3 letters.
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # see if the logo bounce off the top edge.
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # see if the logo bounce off the bottom edge.
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # chage color when the logo bounce.
                logo[COLOR] = random.choice(COLORS)

            # move the logo. X moves by 2 because they are wide.
            # characters are twice as tall as they are wide.
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # display number of corner bounce.
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            # draw the logos at their new location.
#            print(logo)
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)
        sys.stdout.flush()  # required for bext-using programs.
        time.sleep(PAUSE_AMOUNT)


# if this program was run(instead of imported) ,run the game.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()  # when Ctrl-C is pressed, end  the program.

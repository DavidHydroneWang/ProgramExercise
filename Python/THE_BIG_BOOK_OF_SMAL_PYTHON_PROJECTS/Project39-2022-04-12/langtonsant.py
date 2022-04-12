#!/usr/bin/env python
# coding=utf-8
"""
Langton's Ant, by Al Sweigart al@inventwithpython.com
A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, bext, simulation
"""

import copy
import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# set up the constans.
WIDTH, HEIGHT = bext.size()
# we can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one.
WIDTH -= 1
HEIGHT -= 1

NUMBER_OF_ANTS = 10
PAUSE_AMOUT = 0.1

# (!) try changing these to make the ants look different.
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) try changing these colors to one of 'black', 'red', 'green',
# 'yellow', 'blue', 'purple', 'cyan', 'white'. (These are the only
# colors that the bext module supports.)
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def main():
    bext.fg(ANT_COLOR)
    bext.bg(WHITE_TILE)
    bext.clear()

    # create a new board data structure.
    board = {'width': WIDTH, 'height': HEIGHT}

    # create ant data structures.
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    # keep track of which tiles have changed and need to be redrawn on
    # the screen
    changeTiles = []

    while True:
        displayBoard(board, ants, changeTiles)
        changeTiles = []
        # nextBoard is what the board will lool like on the next step in
        # the simulation. Start with a copy of the current step's board.
        nextBoard = copy.copy(board)

        # run a single simulation step for each ant.
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) is True:
                nextBoard[(ant['x'], ant['y'])] = False
                # turn clockwise.
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                # turn counter clockwise.
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
            changeTiles.append((ant['x'], ant['y']))

            # move the ant forward in whatever direction it's facing.
            if ant['direction'] == NORTH:
                ant['y'] -= 1
            elif ant['direction'] == SOUTH:
                ant['y'] += 1
            elif ant['direction'] == WEST:
                ant['x'] -= 1
            elif ant['direction'] == EAST:
                ant['x'] += 1

            # if the ant goes past the edge of the screen.
            # it should wrap around to other side.
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changeTiles.append((ant['x'], ant['y']))

        board = nextBoard


def displayBoard(board, ants, changeTiles):
    """
    Displays the board and ants on the screen. The changedTiles
    argument is a list of (x, y) tuples for tiles on the screen that
    have changed and need to be redrawn.
    """
    # draw the board data structure
    for x, y in changeTiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        antIsHere = False

        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT, end='')
                break
        if not antIsHere:
            print(' ', end='')

    # display the quit message at the bottom of the screen
    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush()
    time.sleep(PAUSE_AMOUT)


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Langton's Ant, by Al Sweigart al@inventwithpython.com")
        sys.exit()

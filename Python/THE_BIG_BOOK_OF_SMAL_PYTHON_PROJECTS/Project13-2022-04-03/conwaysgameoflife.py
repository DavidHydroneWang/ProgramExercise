#!/usr/bin/env python
# coding=utf-8
"""
Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, simulation
"""

import sys, random, copy, time

# set up the constants.
WIDTH = 79  # the width of the cell grid
HEIGHT = 20  # the height of the cell grid

# (!) try changing ALIVE to '#' or another character.
ALIVE = '0'
# (!) try changing DEAD to '.' or another character.
DEAD = ' '

# (!) Try changing ALIVE to '|' and DEAD to '-'

# the cells and nextCells are dictionaries for the state of the game.
nextCells = {}
# put random dead and alive cells into nextCells.
for x in range(WIDTH):
    for y in range(HEIGHT):
        # 50/50 chance for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:
    # each iteration of this loop is a step of the simulation.
    print('\n' * 50)  # separate each step with newlines.
    cells = copy.deepcopy(nextCells)

    # print cells on the screen.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-C to quit.')

    # calculate the next step's cells based on current step's cells.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get the neighboring coordinates of (x, y) even if they
            # wrap aroud the edge
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # count the number of living neighbors.
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1

            # set cell based on Conway's Game of Life rules.

            if cells[(x, y)] == ALIVE and (numNeighbors == 2
                                           or numNeighbors == 3):
                # living cells with 2 or 3 neighbors stay alive.
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # dead cells with 3 neighbors become alive.
                nextCells[(x, y)] = ALIVE
            else:
                # everything else dies or stay alive.
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)  # add a 1 second pause to reduce flicking.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('By Al Sweigart al@inventwithpyton.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.

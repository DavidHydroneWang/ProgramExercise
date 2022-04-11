#!/usr/bin/env python
# coding=utf-8
"""
Hungry Robots, by Al Sweigart al@inventwithpython.com
Escape the hungry robots by making them crash into each other.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game
"""

import random
import sys

# set up the constants.
WIDTH = 40
HEIGHT = 20
NUM_ROBOTS = 10
NUM_TELEPORTS = 2
NUM_DEAD_ROBOTS = 2
NUM_WALLS = 100

EMPTY_SPACE = ' '
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'

# (!) try changing this to '#' or '0' or ' '.
WALL = char(9617)


def main():
    print('''
          Hungry Robots, by Al Sweigart al@inventwithpython.com
          You are trapped in a maze with hungry robots! You don't know why robots
          need to eat, but you don't want to find out. The robots are badly
          programmed and will move directly toward you, even if blocked by walls.
          You must trick the robots into crashing into each other (or dead robots)
          without being caught. You have a personal teleporter device, but it only
          has enough battery for {} trips. Keep in mind, you and robots can slip
          through the corners of two diagonal walls!
          '''.format(NUM_TELEPORTS))

    input('Press Enter to begin...')

    # set up a new game
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    while True:
        displayBoard(board, robots, playerPosition)

        if len(robots) == 0:
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # move the player and robots.
        for x, y in robots:
            if (x, y) == playerPosition:
                displayBoard(board, robots, playerPosition)
                print('You have been caught by a robot!')
                sys.exit()


def getNewBoard():
    """return a dictionary that represents the board. The keys are
    (x, y) tuples of integer indexes for board positions, the values are
    WALL, EMPTY_SPACE, or DEAD_ROBOT. The dictionary also has the key
    'teleports' for the number of teleports the player has left.
    The living robots are stored separately from the board dictionary."""
    board = {'teleports': NUM_TELEPORTS}

    # create an empty board.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # add walls on the edges of the board.
    for x in range(WIDTH):
        board[(x, 0)] = WALL
        board[(x, HEIGHT - 1)] = WALL

    for y in range(HEIGHT):
        board[(0, y)] = WALL
        board[(WIDTH - 1, y)] = WALL

    # add the random wall.
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # add the starting dead robots.
    for i in range(NUM_DEAD_ROBOTS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    """
    return a (x, y) integer tuple of an empty space on the board.
    """
    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    """
    return True if the (x, y) is empty on the board and there's
    also no robot there.
    """
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def addRobots(board):
    """
    add NUM_ROBOTS number of robots to empty space on the board and
    return a list of these (x, y) space where robots are now loacted.
    """
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x,y))
    return robots


def displayBoard(board, robots, playerPosition):
    """
    display the board, robots, and player on the screen.
    """
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # draw the appropriate character.
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == playerPosition:
                print(PLAYER, end='')
            elif (x, y) == robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()


def askForPlayerMove(board, robots, playerPosition):
    """
    return the (x, y) integer tuple of the place the player moves
next, given their current location and the walls of the board.
    """
    playerX, playerY = playerPosition

    # find which directions aren't blocked by a wall.
    q = 'Q' if isEmpty(playerX - 1, playerY - 1, board, robots) else ' '
    w = 'W' if isEmpty(playerX + 0, playerY - 1, board, robots) else ' '
    e = 'E' if isEmpty(playerX + 1, playerY - 1, board, robots) else ' '
    d = 'D' if isEmpty(playerX + 1, playerY + 0, board, robots) else ' '
    c = 'C' if isEmpty(playerX + 1, playerY + 1, board, robots) else ' '
    x = 'X' if isEmpty(playerX + 0, playerY + 1, board, robots) else ' '
    z = 'Z' if isEmpty(playerX - 1, playerY + 1, board, robots) else ' '
    a = 'A' if isEmpty(playerX - 1, playerY + 0, board, robots) else ' '
    allMoves = (q + w + e + d + c + x + a + z + 'S')

    while True:
        # get player's move.
        print('(T)eleports remaining: {}'.format(board['teleports']))
        print('                    ({}) ({}) ({})'.format(q, w, e))
        print('                    ({}) (S) ({})'.format(a, d))
        print('Enter move or QUIT: ({}) ({}) ({})'.format(z, x, c))

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # teleport the player to a random empty space.
            board['teleports'] -= 1
            return getRandomEmptySpace(board, robots)
        elif move != '' and move in allMoves:
            # return the new player position based on their move.
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX, playerY)}[move]


def moveRobots(board, robotPositions, playerPosition):
    """
    return a list of (x, y) tuples of new robot positions after they
    have tried to move toward the player.
    """
    playerX, playerY = playerPosition
    nextRobotPositions = []

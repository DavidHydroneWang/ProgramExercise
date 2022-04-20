#!/usr/bin/env python
# coding=utf-8
"""
Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com
Slide the numbered tiles into the correct order.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, puzzle
"""

import random
import sys

BLANK = '  '


def main():
    print('''
          Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com

          Use the WASD keys to move the tiles
          back into their original order:
                 1  2  3  4
                 5  6  7  8
                 9 10 11 12
                13 14 15''')
    input('Press Enter to begin...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You win!')
            sys.exit()


def getNewBoard():
    """return a list of lists that represents a new tile puzzle."""
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
            ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]


def displayBoard(board):
    """display the given board on the screen."""
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
              board[0][1], board[1][1], board[2][1], board[3][1],
              board[0][2], board[1][2], board[2][2], board[3][2],
              board[0][3], board[1][3], board[2][3], board[3][3]]
    boardToDraw = """
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
            """.format(*labels)
    print(boardToDraw)


def findBlankSpace(board):
    """return an (x, y) tuple of the blank space's location."""
    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x, y)


def askForPlayerMove(board):
    """let the player select a tile to slide."""
    blankx, blanky = findBlankSpace(board)

    w = 'W' if blanky != 3 else ' '
    a = 'A' if blankx != 3 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True:
        print('                          ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d))

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response


def makeMove(board, move):
    """carry out the given move on the given board."""
    # note: this function assumes that the move is valid.
    bx, by = findBlankSpace(board)

    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]


def makeRandomMove(board):
    """perform a slide in a random direction."""
    blankx, blanky =findBlankSpace(board)
    validMove = []
    if blanky != 3:
        validMove.append('W')
    if blankx != 3:
        validMove.append('A')
    if blanky != 0:
        validMove.append('S')
    if blankx != 0:
        validMove.append('D')

    makeMove(board, random.choice(validMove))


def getNewPuzzle(moves=200):
    """get a new puzzle by making ramdom slides from a solved state."""
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    main()

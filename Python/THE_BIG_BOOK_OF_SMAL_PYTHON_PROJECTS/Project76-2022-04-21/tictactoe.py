#!/usr/bin/env python
# coding=utf-8
"""
Tic-Tac-Toe, by Al Sweigart al@inventwithpython.com
The classic board game.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, board game, game, two-player
"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '


def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        # display the board on the screen.
        print(gameBoardStr(gameBoard))
        # keep asking the player until they enter a number 1-9
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\' next move (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)

        # check if the game is over.
        if isWinner(gameBoard, currentPlayer):
            print(gameBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):
            print(gameBoardStr(gameBoard))
            print('The game is a tie!')
            break
        # switch turns to the next player.
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


def getBlankBoard():
    """create a new, blank tic-tac-toe board."""
    # Map of space numbers: 1|2|3
    #                       -+-+-
    #                       4|5|6
    #                       -+-+-
    #                       7|8|9
    # Keys are 1 through 9, the values are X, O, or BLANK:
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board


def gameBoardStr(board):
    """return a text-representation of the board."""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9
'''.format(board['1'], board['2'], board['3'],
           board['4'], board['5'], board['6'],
           board['7'], board['8'], board['9'])


def isValidSpace(board, space):
    """returns True if the space on the board is a valid space number
    and the space is blank."""
    return space in ALL_SPACES and board[space] == BLANK


def isWinner(board, player):
    "return True if player is a winner on this TTTBoard."
    # shorter variable names used here for readability.
    b, p = board, player
    # check for 3 marks across 3 rows, 3 column, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))


def isBoardFull(board):
    """return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True


def updateBoard(board, space, mark):
    """sets the space on the board to mark."""
    board[space] = mark


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# coding=utf-8
"""
Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com
A sliding tile game to combine exponentially-increasing numbers.
Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios'
1024, which in turn is a clone of the Threes! game.
More info at https://en.wikipedia.org/wiki/2048_(video_game)
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, puzzle
"""

import random
import sys

# set up the constants.
BLANK = ''


def main():
    print('''
          Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com

          Slide all the tiles on the board in one of four directions. Tiles with
          like numbers will combine into larger-numbered tiles. A new 2 tile is
          added to the board on each move. You win if you can create a 2048 tile.
          You lose if the board fills up the tiles before then.
          ''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()

    while True:
        drawBoard(gameBoard)
        print('Score: ', getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()


def getNewBoard():
    """returns a new data structure that represents a board.

    It's a dictionary with keys of (x, y) tuples and values of the tile
    at that space. The tile is either a power-of-two integer or BLANK.
    The coordinates are laid out as:
       X0 1 2 3
      Y+-+-+-+-+
      0| | | | |
       +-+-+-+-+
      1| | | | |
       +-+-+-+-+
      2| | | | |
       +-+-+-+-+
      3| | | | |
       +-+-+-+-+"""

    newBoard = {}
    # loop over every possible space and set all the tiles to blank
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    # pick two random spaces for the two starting 2s.
    startingTwoPlaced = 0
    while startingTwoPlaced < 2:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        # make sure the randomly selected space isn't already taken.
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwoPlaced = startingTwoPlaced + 1

    return newBoard


def drawBoard(board):
    """
    draws the board data structure on the screen.
    """
    # Go through each possible space left to right, top to bottom, and
    # create a list of what each space's label should be.
    labels = []
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]
            # make sure the label is 5 spaces long.
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    # the {} are replaced with the label for that tile
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))


def getScore(board):
    """
    Returns the sum of all the tiles on the board data structure.
    """
    score = 0
    for x in range(4):
        for y in range(4):
            if board[(x, y)] != BLANK:
                score += board[(x, y)]
    return score


def combineTileInColumn(column):
    """
    The column is a list of four tile. Index 0 is the "bottom" of
    the column, and tiles are pulled "down" and combine if they are the
    same. For example, combineTilesInColumn([2, BLANK, 2, BLANK])
    returns [4, BLANK, BLANK, BLANK].
    """

    # Copy only the numbers (not blanks) from column to combinedTiles
    combineTiles = []
    for i in range(4):
        if column[i] != BLANK:
            combineTiles.append(column[i])

    # keep adding blanks until there are 4 tiles.
    while len(combineTiles) < 4:
        combineTiles.append(BLANK)

    # combine numbers if the one "above" it is the same, and double it.
    for i in range(3):
        if combineTiles[i] == combineTiles[i + 1]:
            combineTiles[i] *= 2
            # move the tiles above it down one space.
            for aboveIndex in range(i + 1, 3):
                combineTiles[aboveIndex] = combineTiles[aboveIndex + 1]
            combineTiles[3] = BLANK
    return combineTiles


def makeMove(board, move):
    """
    Carries out the move on the board.

    The move argument is either 'W', 'A', 'S', or 'D' and the function
    eturns the resulting board data structure.
    """
    # The board is split up into four columns, which are different
    # depending on the direction of the move:
    if move == 'W':
        allColumnsSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                            [(1, 0), (1, 1), (1, 2), (1, 3)],
                            [(2, 0), (2, 1), (2, 2), (2, 3)],
                            [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        allColumnsSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                            [(0, 1), (1, 1), (2, 1), (3, 1)],
                            [(0, 2), (1, 2), (2, 2), (3, 2)],
                            [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        allColumnsSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                            [(1, 3), (1, 2), (1, 1), (1, 0)],
                            [(2, 3), (2, 2), (2, 1), (2, 0)],
                            [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]

    # the board data structure after making the move
    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:
        # get the tiles of this column
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]

        firstTile = board[firstTileSpace]
        secontTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]

        # form the column and combine the tiles in it.
        column = [firstTile, secontTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTileInColumn(column)

        # set up the new board data structure with the combined tiles.
        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]

    return boardAfterMove


def askForPlayerMove():
    """
    Asks the player for the direction of their next move (or quit).
    Ensures they enter a valid move: either 'W', 'A', 'S' or 'D'.
    """
    print('Enter move: (WASD or Q to quit.)')
    while True:
        move = input('> ').upper()
        if move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Enter one of "W", "A", "S", "D", or "Q"')


def addTwoToBoard(board):
    """
    "Adds a new 2 tile randomly to the board.
    """
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return


def isFull(board):
    """
    Returns True if the board data structure has no blanks.
    """
    for x in range(4):
        for y in range(4):
            if board[(x, y)] == BLANK:
                return False

    return True


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        sys.exit()

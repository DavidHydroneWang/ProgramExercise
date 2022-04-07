#!/usr/bin/env python
# coding=utf-8
"""
Dice Math, by Al Sweigart al@inventwithpython.com
A flash card addition game where you sum the total on random dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, math
"""

import random, time

# set up the constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom

# the dutation is in seconds.
QUIZ_DURATION = 30  # (!) try changing this to 10 or 60
MIN_DICE = 2  # (!) try changing this to 1 or 5
MAX_DICE = 6  # (!) try changing this to 14

# (!) try changing these to different numbers.
REWARD = 4
PENALTY = 1
# (!) try setting PENALTY to a negative number to give points for wrong number.


# The program hangs if all of the dice can't fit on the screen.
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''
      Dice Math, by Al Sweigart al@inventwithpython.com
      Add up the sides of all the dice displayed on the screen. You have
      {} seconds to answer as many as possible. You get {} points for each
      correct answer and lose {} point for each incorrect answer.
      '''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

# keep track of how many answers were correct and incorrect.
correctAnswer = 0
incorrectAnswer = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:
    # come up with the dice to display.
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # dice[0] contain the list of strings of the dice face.
        diceFaces.append(die[0])
        # dice[1] contain the integer number of pips on the face.
        sumAnswer += die[1]

    # contains (x, y) tuples of the top-left corner of each die
    topLeftDiceCorners = []

    # Figure out where dice should go.
    for i in range(len(diceFaces)):
        while True:
            # find a random place on the canvas to put the die.
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # get the x, y coordinates for all four corners.
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # check of this die overlaps with previous dice.
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # check each corner of this die to see if it is inside
                # of the area the previous die.
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight
                        and prevDieTop <= cornerY < prevDieBottom):
                            overlaps = True
            if not overlaps:
                # it doesn't overlap, so we can put it here.
                topLeftDiceCorners.append((left, top))
                break

    # draw the dice on the canvas.
    canvas = {}
    # loop over each die
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        # loop over each character in the die's face
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # copy this character to the correct place on the canvas.
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # note that in dieFace, a list of strings, the x and y
                # are swapped
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # display the canvas on the screen
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()

    # left the play enter their answer.
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswer += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrectAnswer += 1


# display the final score.
score = (correctAnswer * REWARD) - (incorrectAnswer * PENALTY)
print('Correct: ', correctAnswer)
print('Incorrect: ', incorrectAnswer)
print('Score: ', score)

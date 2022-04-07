#!/usr/bin/env python
# coding=utf-8
"""
Dice Roller, by Al Sweigart al@inventwithpython.com
Simulates dice rolls using the Dungeons & Dragons dice roll notation.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, simulation
"""

import random, sys

print('''
      Dice Roller, by Al Sweigart al@inventwithpython.com
      Enter what kind and how many dice to roll. The format is the number of
      dice, followed by "d", followed by the number of sides the dice have.
      You can also add a plus or minus adjustment.

      Examples:
      3d6 rolls three 6-sided dice
      1d10+2 rolls one 10-sided die, and adds 2
      2d38-1 rolls two 38-sided die, and subtracts 1
      QUIT quits the program
      ''')

while True:
    try:
        diceStr = input('> ')
        if diceStr.upper() == 'QUIT':
            sys.exit()

        # clean up the dice string.
        diceStr = diceStr.lower().replace(' ', '')

        # fine the d in the dice string input.
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # get the number of dice
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # find if there is a plus or minus sign for a modifier.
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # finf the number of sides.
        if modIndex == -1:
            numberOfDSides = diceStr[dIndex + 1:]
        else:
            numberOfDSides = diceStr[dIndex + 1: modIndex]

        if not numberOfDSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfDSides = int(numberOfDSides)

        # find the modifier amount.
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1:])
            if diceStr[modIndex] == '-':
                modAmount = -modAmount

        # simulate the dice rolls.
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfDSides)
            rolls.append(rollResult)

        # display the total.
        print('Total: ', sum(rolls) + modAmount, '(Each die:', end='')

        # display the individual rolls.
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # display the modifier amount.
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # catch any expression and display the message to the user.
        print('Invalid input, Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue

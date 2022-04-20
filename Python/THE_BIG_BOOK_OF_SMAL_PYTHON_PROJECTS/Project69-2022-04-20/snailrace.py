#!/usr/bin/env python
# coding=utf-8
"""
Snail Race, by Al Sweigart al@inventwithpython.com
Fast-paced snail racing action!
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, beginner, game, multiplayer
"""

import random
import time
import sys

# set up the constants.
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

print('''
      Snail Race, by Al Sweigart al@inventwithpython.com

      @v <-- snail

''')
# ask how many snails to race
while True:
    print('How many snails will race?Max:', MAX_NUM_SNAILS)
    reponse = input('> ')
    if reponse.isdecimal():
        numSnailsRacing = int(reponse)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and ', MAX_NUM_SNAILS)

# enter the names of each snail.
snailNames = []
for i in range(1, numSnailsRacing + 1):
    while True:
        print('Enter snail #' + str(i) + "'s name:'")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not really been used.')
        else:
            break
    snailNames.append(name)

# display each snail at the start line.
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)

while True:
    # pick random snails to move forward.
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        # check if a snail has reached the finish line.
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    time.sleep(0.5)
    print('\n' * 40)

    # display the start and finish line.
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # display the snails (with name tags):
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')

#!/usr/bin/env python
# coding=utf-8
"""
Rock, Paper, Scissors (Always Win version)
By Al Sweigart al@inventwithpython.com
The classic hand game of luck, except you always win.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, game, humor
"""

import time
import sys

print('''
      Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
      - Rock beats scissors.
      - Paper beats rocks.
      - Scissors beats paper.
      ''')

# these variables keep track of the number of wins.
wins = 0
while True:
    while True:
        print('{} Wins, 0 Losses, 0 Ties'.format(wins))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, or Q.')

    # display what the player chose.
    if playerMove == 'R':
        print('ROCK versus...')
    elif playerMove == 'P':
        print('PAPER versus...')
    elif playerMove == 'S':
        print('SCISSORS versus...')

    # count to three with dramatic pause.
    time.sleep(0.5)
    print('1...')
    time.sleep(0.5)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # display what the computer chose.
    if playerMove == 'R':
        print('SCISSORS')
    elif playerMove == 'P':
        print('ROCK')
    elif playerMove == 'S':
        print('PAPER')

    time.sleep(0.5)

    print('You win!')
    wins += 1

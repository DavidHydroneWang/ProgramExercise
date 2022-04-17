#!/usr/bin/env python
# coding=utf-8
"""
Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
The classic hand game of luck.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, game
"""

import random
import time
import sys

print('''
      Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
      -Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
      - Paper beats rocks.
      - Scissors beats paper.
      ''')

# these variables keeps track of the number if wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:
    while True:
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
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
        print('Rock versus...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('Paper versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('Scissors versus...')
        playerMove = 'SCISSORS'

    # count to three with dramatic pause.
    time.sleep(0.5)
    print('1...')
    time.sleep(0.5)
    print('2...')
    time.sleep(0.5)
    print('3...')

    # display what the computer chose.
    randomNum = random.randint(1, 3)
    if randomNum == 1:
        computerMove = 'ROCK'
    elif randomNum == 2:
        computerMove = 'PAPAER'
    elif randomNum == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    time.sleep(0.5)

    # dislpay and record the win/loss/tie.
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties += 1
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print('You win!')
        wins += 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print('You win!')
        wins += 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!')
        wins += 1
    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print('You lost!')
        losses += 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print('You lost!')
        losses += 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You lost!')
        losses += 1

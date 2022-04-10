#!/usr/bin/env python
# coding=utf-8
"""
Guess the Number, by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, game
"""

import random


def askForGuess():
    while True:
        guess = input('> ')

        if guess.isdecimal():
            return int(guess)
        print('Please enter a number between 1 and 100.')


print('Guess the number, by Al Sweigart al@inventwithpython.com')
print()
secretNumber = random.randint(1, 100)
print('I am thinking of a number between 1 and 100.')

for i in range(10):
    print('You have {} guesses left. Take a guess.'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break

    # offer a hint.
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# reveal the results.
if guess == secretNumber:
    print('Yay! You guessed my number!')
else:
    print('Game Over. The number I was thinking of was', secretNumber)

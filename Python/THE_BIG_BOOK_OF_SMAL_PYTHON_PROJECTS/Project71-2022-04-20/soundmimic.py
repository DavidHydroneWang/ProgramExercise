#!/usr/bin/env python
# coding=utf-8
"""
Sound Mimic, by Al Sweigart al@inventwithpython.com
A pattern-matching game with sounds. Try to memorize an increasingly
longer and longer pattern of letters. Inspired by the electronic game
Simon.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game
"""

import random
import sys
import time

# Download the sound files from these URLs (or use your own):
# https://inventwithpython.com/soundA.wav
# https://inventwithpython.com/soundS.wav
# https://inventwithpython.com/soundD.wav
# https://inventwithpython.com/soundF.wav

try:
    import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install playsound')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install playsound')
    sys.exit()


print('''
      Sound Mimic, by Al Sweigart al@inventwithpython.com
      Try to memorize a pattern of A S D F letters (each with its own sound)
      as it gets longer and longer.
      ''')

input('Press Enter to begin...')

pattern = ''
while True:
    print('\n' * 60)

    # add a random letter to the pattern
    pattern += random.choice('ASDF')

    # display the pattern (and play their sounds)
    print('Pattern: ', end='')
    for letter in pattern:
        print(letter, end='', flush=True)
        playsound.playsound('sound' + letter + '.wav')

    time.sleep(1)
    print('\n' * 60)

    # let the player enter the pattern.
    print('Enter the pattern: ')
    reponse = input('> ').upper()

    if reponse != pattern:
        print('Incorrect!')
        print('The pattern was', pattern)
    else:
        print('Correct!')

    for letter in pattern:
        playsound.playsound('sound' + letter + '.wav')

    if reponse != pattern:
        print('You scored', len(pattern) - 1, 'points.')
        print('Thanks for palying!')
        break

    time.sleep(1)
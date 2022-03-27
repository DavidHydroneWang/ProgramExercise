#!/usr/bin/env python
# coding=utf-8
import random, sys


NUM_DIGITS = 3  # can be 1 to 10
MAX_GUESSES = 10  # can be 1 to 100


def main():
    print('''
          Bagels, a deductive logic game.
          By Al Sweigart al@inventwithpython.com
          revised by David Wang.
          ''')
    while True:
        # main game loop
        # stores secret number
        secretNum = getSecretNum()
        print('''
          I am thinking of a {}-digit number  with no repeated digits.
          every digit is different and in the range [0-9]
          Try to guess what it is. Here are some clues:
          When I say:   That means:
          Pico   One digit is correct but in the wrong position.
          Fermi  One digit is correct and in the right position.
          Bagels   No digit is correct.
          For example, if the secret number was 248 and your guess was 843, the
          clues would be Fermi Pico.
              '''.format(NUM_DIGITS))
        print('''
          I have thought up a number.
          You have {} guesses to get it.
              '''.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # keeping looping until they enter a valid guess
            # or type q to quit the program
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{} or type q to quit the game: '.format(numGuesses))
                guess = input('> ')
                if guess == 'q':
                    sys.exit()
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses. ')
                print('The answer was {}'.format(secretNum))

        # ask player if they want to paly again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """
    Returns a string made up of NUM_DIGITS unique random digits.abs
    """
    numbers = list('0123456789')  # create a list of digits 0-9.
    random.shuffle(numbers)  # shuffle them into random order
    # get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """
    Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair.
    """
    if guess == secretNum:
        return 'You got it'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # a correct digit is in incorrect place.
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # there are no correct digits at all.
    else:
        # sort the clues into alphabetically order so
        # they don't give infotmation away.
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()

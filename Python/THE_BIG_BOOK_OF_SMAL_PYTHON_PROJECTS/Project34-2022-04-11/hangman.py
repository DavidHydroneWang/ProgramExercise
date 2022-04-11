#!/usr/bin/env python
# coding=utf-8
"""
Hangman, by Al Sweigart al@inventwithpython.com
Guess the letters to a secret word before the hangman is drawn.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, word, puzzle
"""

import random
import sys

# set up the constants.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# try changing CATEGORY and WORDS with new strings.
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


def main():
    print('Hangman, by Al Sweigart al@inventwithpython.com')

    # set up variables for a new game.
    missedLetters = []
    correctLerrers = []
    secretWord = random.choice(WORDS)

    while True:
        drawHangman(missedLetters, correctLerrers, secretWord)

        # let the player enter their letter guess.
        guess = getPlayerGuess(missedLetters + correctLerrers)

        if guess in secretWord:
            # add the correct guess to correctLetters.
            correctLerrers.append(guess)

            # check if the player has won.
            foundAllLetters = True
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLerrers:
                    # there's a letter in the secret word that isn't
                    # yet in correctLetters, so the player hasn't won.
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break

        else:
            # the player has guessed incorrectly.
            missedLetters.append(guess)

            # check if player has guessed too many times and lost. (The
            # "-1" is because we don't count the empty gallows in
            # HANGMAN_PICS.)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLerrers, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break


def drawHangman(missedLetters, correctLerrers, secretWord):
    """
    Draw the current state of the hangman, along with the missed and
    correctly-guessed letters of the secret word.
    """
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    # show the incorrectly guessed letters.
    for letter in missedLetters:
        print(letter, end='')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # display the blanks for the secret word (one blank per letter)
    blanks = ['_'] * len(secretWord)

    # replace blanks with correctly guessed letters.
    for i in range(len(secretWord)):
        if secretWord[i] in correctLerrers:
            blanks[i] = secretWord[i]

    # show the secret word with spaces in between each letter.
    print(' '.join(blanks))


def getPlayerGuess(alredyGuessed):
    """
    Returns the letter the player entered. This function makes sure
    the player entered a single letter they haven't guessed before.
    """
    while True:
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alredyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER!')
        else:
            return guess


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

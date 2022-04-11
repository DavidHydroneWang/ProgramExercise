#!/usr/bin/env python
# coding=utf-8
"""
Hacking Minigame, by Al Sweigart al@inventwithpython.com
comThe hacking mini-game from "Fallout 3". Find out which seven-letter
word is the password by using clues each guess gives you.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, puzzle
"""

import random
import sys

# set up the constants.
# the garbage filler characters for the "computer memory" display.
GARBAGE_CHAR = '~!@#$%^&*(){}[];:,.<>?/'

# load the words list from a text file that has 7-letter words.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()

for i in range(len(WORDS)):
    # convert each word to uppercase and remove the trailing newline.
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """run a single game of hacking."""
    print('''
          'Hacking Minigame, by Al Sweigart al@inventwithpython.com
          Find the password in the computer's memory. You are given clues after
          each guess. For example, if the secret password is MONITOR but the
          player guessed CONTAIN, they are given the hint that 2 out of 7 letters
          were correct, because both MONITOR and CONTAIN have the letter O and N
          as their 2nd and 3rd letter. You get four guesses.\n
          ''')
    input('Press Enter to begin...')

    gameWords = getWords()
    # the "computer memory" is just cosmetic, but it looks cool.
    computerMemory = getComputerString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # start at 4 tries remaining, going down.
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries. Secret password was {}.'.format(secretPassword))


def getWords():
    """
    Return a list of 12 words that could possibly be the password.
The secret password will be the first word in the list.
To make the game fair, we try to ensure that there are words with
a range of matching numbers of letters as the secret word.
    """
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # find two more words; these have zero matching letters.
    # we use "< 3" because the secret password is alredy in words.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # find two words that have 3 matching letters (but give up at 500
    # tries if not enough can be found).
    for i in range(500):
        if len(words) == 5:
            break

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # find at least seven words that have at least one matching letter
    # (but give up at 500 tries if not enough can be found).
    for i in range(500):
        if len(words) == 12:
            break

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # add any random words needed to get 12 words total.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    """return a random word from WORDS that isn't in blocklist"""
    if blocklist is None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def numMatchingLetters(word1, word2):
    """return the number of matching letters in these two words."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def getComputerString(words):
    """return a string representing the computer memory."""
    # pick one line per word to contain a word. There are 16 lines, but
    # they are split into two halves.
    lineWithWords = random.sample(range(16 * 2), len(words))
    # the starting memory address (this is also cosmetic).
    memoryAddress = 16 * random.randint(0, 4000)

    # create the "computer memory" string.
    computerMemory = []
    nextWord = 0
    for lineNum in range(16):
        # create a half line of garbage characters.
        leftHalf = ''
        rightHalf = ''
        for j in range(16):
            leftHalf += random.choice(GARBAGE_CHAR)
            rightHalf += random.choice(GARBAGE_CHAR)

        # fill in the password from words,
        if lineNum in lineWithWords:
            # find a random place in the half line to insert the word.
            insertionIndex = random.randint(0, 9)
            # insert the word.
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord]
                        + leftHalf[insertionIndex + 7:])
            nextWord += 1
        if lineNum + 16 in lineWithWords:
            # find a random place in the half line to insert the word.
            insertionIndex = random.randint(0, 9)
            # insert the word
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord]
                         + rightHalf[insertionIndex + 7:])
            nextWord += 1
        computerMemory.append('ox' + hex(memoryAddress)[2:].zfill(4)
                              + '  ' + leftHalf + '   '
                              + 'ox' + hex(memoryAddress + (16*16))[2:].zfill(4)
                              + '  ' + rightHalf)

        memoryAddress += 16

    # each string in the computerMemory list is joined into one large
    # string to return.
    return '\n'.join(computerMemory)


def askForPlayerGuess(words, tries):
    """let the player enter a password guess."""
    while True:
        print('Enter password: {} tries remaining'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print('Try entering "{}" or "{}" .'.format(words[0], words[1]))


# if this program was run (instead of imported), run the program.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

#!/usr/bin/env python
# coding=utf-8
"""
Three-Card Monte, by Al Sweigart al@inventwithpython.com
Find the Queen of Hearts after cards have been swapped around.
(In the real-life version, the scammer palms the Queen of Hearts so you
always lose.)
More info at https://en.wikipedia.org/wiki/Three-card_Monte
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, card game, game
"""

import random
import time

# set up the constants
NUM_SWAPS = 16
DELAY = 0.8

# the card suit characters.
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

# the indexes of  a 3-card list
LEFT = 0
MIDDLE = 1
RIGHT = 2


def displayCards(cards):
    """ display the cards in 'cards', which is a list of (rank, suit) tuples"""
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rank, suit = card
        rows[0] += ' ___  '
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # print each row on the screen.
    for i in range(5):
        print(rows[i])


def getRandomCard():
    """returns a random card that is NOT the Queen of Hearts."""

    while True:
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])

        # return the card as long as it's not the queen of hearts.
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)


print('Three-Card Monte, by Al Sweigart al@inventwithpython.com')
print()
print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
print('the cards move.')
print()

# show the original arrangement.
cards = [('Q', HEARTS), getRandomCard(), getRandomCard()]
random.shuffle(cards)
print('Here are the cards:')
displayCards(cards)
input('Press Enter when you are ready to begin...')

# print the swaps.
for i in range(NUM_SWAPS):
    swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])

    if swap == 'l-m':
        print('swapping left and middle...')
        cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
    elif swap == 'm-r':
        print('swapping middle and right...')
        cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
    elif swap == 'l-r':
        print('swapping left and right...')
        cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
    elif swap == 'm-l':
        print('swapping middle and left...')
        cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
    elif swap == 'r-m':
        print('swapping right and middle...')
        cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
    elif swap == 'r-l':
        print('swapping right and left...')
        cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]

    time.sleep(DELAY)

# print several new lines to hide the swaps.
print('\n' * 60)

# ask for the user to find the red lady.
while True:
    print('Which card has the Queen of Hearts? (LEFT MIDDLE or RIGHT)')
    guess = input('> ').upper()

    # get the index in cards for the position that the player entered.
    if guess in ['LEFT', 'MIDDLE', 'RIGHT']:
        if guess == 'LEFT':
            guessIndex = 0
        elif guess == 'MIDDLE':
            guessIndex = 1
        elif guess == 'RIGHT':
            guessIndex = 2
        break

# (!) Uncomment this code to make the player always lose:
# if cards[guessIndex] == ('Q', HEARTS):
#
# Player has won, so let's move the queen.
#    possibleNewIndexes = [0, 1, 2]
#    possibleNewIndexes.remove(guessIndex)  # Remove the queen's index.
#    newInd = random.choice(possibleNewIndexes)  # Choose a new index.
#    # Place the queen at the new index:
#    cards[guessIndex], cards[newInd] = cards[newInd], cards[guessIndex]

displayCards(cards)

# check if the player won
if cards[guessIndex] == ('Q', HEARTS):
    print('You won!')
    print('Thanks for playing!')
else:
    print('You lost!')
    print('Thanks for playing, sucker!')

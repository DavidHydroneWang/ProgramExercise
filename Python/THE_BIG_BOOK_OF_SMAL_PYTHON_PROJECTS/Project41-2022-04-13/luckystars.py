#!/usr/bin/env python
# coding=utf-8
"""
Lucky Stars, by Al Sweigart al@inventwithpython.com
A "press your luck" game where you roll dice to gather as many stars
as possible. You can roll as many times as you want, but if you roll
three skulls you lose all your stars.

Inspired by the Zombie Dice game from Steve Jackson Games.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, multiplayer
"""

import random

# set up the constants.
GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = ["+-----------+",
             "|     .     |",
             "|    ,O,    |",
             "| 'ooOOOoo' |",
             "|   `OOO`   |",
             "|   O' 'O   |",
             "+-----------+"]

SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']

FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""
      Lucky Stars, by Al Sweigart al@inventwithpython.com
      A "press your luck" game where you roll dice with Stars, Skulls, and
      Question Marks.

      On your turn, you pull three random dice from the dice cup and roll
      them. You can roll Stars, Skulls, and Question Marks. You can end your
      turn and get one point per Star. If you choose to roll again, you keep
      the Question Marks and pull new dice to replace the Stars and Skulls.
      If you collect three Skulls, you lose all your Stars and end your turn.

      When a player gets 13 points, everyone else gets one more turn before
      the game ends. Whoever has the most points wins.

      There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
      Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
      even.
      """)

print('How many players are there?')
while True:
    reponse = input('> ')
    if reponse.isdecimal() and int(reponse) > 1:
        numPlayer = int(reponse)
        break
    print('Please enter a number larger than 1.')

playerNames = []
playerScores = {}
for i in range(numPlayer):
    while True:
        print('What is player #' + str(i + 1) + '\'s name?')
        reponse = input('> ')
        if reponse != '' and reponse not in playerNames:
            playerNames.append(reponse)
            playerScores[reponse] = 0
            break
        print('Please enter a name.')
print()

turn = 0
# (!) Uncomment to let a player named 'Al' start with three points.
# playerScores['Al'] = 3
endGameWith = None
while True:
    # display everyone's score.
    print()
    print('Scores: ', end='')
    for i, name in enumerate(playerNames):
        print(name + ' = ' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            # all but the last player have commas separateing their names.
            print(', ', end='')
    print('\n')
    # start the number of collected stars and skulls at 0.
    stars = 0
    skulls = 0
    # a cup of 6 gold, 4 silver, and 3 bronze dice.
    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = []
    print('It is ' + playerNames[turn] + '\'s turn')
    while True:
        print()

        # check that there's enough dice left in the cup.
        if (3 - len(hand)) > len(cup):
            # end this turn because there are not enough dice.
            print('There aren\'t enough dice left in the cup to '
                 + 'continue ' + playerNames[turn] + '\'s turn.')
            break

        # pull dice from the cup until you have 3 in your hand.
        random.shuffle(cup)
        while len(hand) < 3:
            hand.append(cup.pop())

        # roll the dice.
        rollResults = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
                # roll a gold dice (3 stars, 2 questions, 1 skull).
                if 1 <= roll <= 3:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    stars += 1
            if dice == SILVER:
                # roll a silver dice (2 stars, 2 questions, 2 skulls).
                if 1 <= roll <= 2:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    stars += 1

            if dice == BRONZE:
                # roll a bronze die ( 1 star, 2 questions, 3 skulls ):
                if roll == 1:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 2 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1

        # display roll results.
        for lineNum in range(FACE_HEIGHT):
            for diceNum in range(3):
                print(rollResults[diceNum][lineNum] + ' ', end='')
            print()

        # display the type of dice each one is (gold, silver, bronze).
        for diceType in hand:
            print(diceType.center(FACE_WIDTH) + ' ', end='')
        print()

        print('Stars Collected:', stars, ' Skulls collected:', skulls)

        # check if they've collected 3 or more skulls.
        if skulls > 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(playerNames[turn] + ', do you want to roll again?Y/N')
        while True:
            reponse = input('> ').upper()
            if reponse != '' and reponse[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if reponse.startswith('N'):
            print(playerNames[turn], 'got', stars, 'stars!')
            # add stars to this player's point total/
            playerScores[playerNames[turn]] += stars

            # check if they've reached 13 or more points.
            # (!) try changing this to 5 or 50 points.
            if (endGameWith is None
                and playerScores[playerNames[turn]] >= 13):
                # since this player reached 13 points, play one more
                # round for all other player.
                print('\n\n' + ('!' * 60))
                print(playerNames[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                endGameWith = playerNames[turn]
            input('Press Enter to continue...')
            break

        # discard the stars and skulls, but keep the question marks.
        nextHand = []
        for i in range(3):
            if rollResults[i] == QUESTION_FACE:
                nextHand.append(hand[i])
        hand = nextHand

    # move on to the next player's turn.
    turn = (turn + 1) % numPlayer

    # if the game has ended, break out of this loop.
    if endGameWith == playerNames[turn]:
        break


print('The game has ended.')

# display everyone's score.
print()
print('SCORE: ', end='')
for i, name in enumerate(playerNames):
    print(name + ' = ' + str(playerScores[name]), end='')
    if i != len(playerNames) - 1:
        # all but the last player have commas separating their names.
        print(', ', end='')
print('\n')

# find out who the winners are.
highestScore = 0
winners = []
for name, score in playerScores.items():
    if score > highestScore:
        # this player has the highest score.
        highestScore = score
        winners = [name]
    elif score == highestScore:
        # this player is tied with the highest score.
        winners.append(name)

if len(winners) == 1:
    # there is only one winner.
    print('The winner is ' + winners[0] + '!!!')
else:
    # there are multiple tied winners.
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')

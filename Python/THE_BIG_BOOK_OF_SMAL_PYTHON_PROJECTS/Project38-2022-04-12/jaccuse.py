#!/usr/bin/env python
# coding=utf-8
"""
J'ACCUSE!, by Al Sweigart al@inventwithpython.com
A mystery game of intrigue and a missing cat.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: extra-large, game, humor, puzzle
"""
# Play the original Flash game at:
# https://homestarrunner.com/videlectrix/wheresanegg.html
# More info at: http://www.hrwiki.org/wiki/Where's_an_Egg%3F

import time
import random
import sys

# set up the constants.
SUSPECTS = ['DUKE HAUNTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR',
            'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT',
            'CECIL EDGAR VANDERTON']
ITEMS = ['FLASGLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE',
         'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLOR GIFT CARD']
PLACES =['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY',
         'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBIND ALLIGATOR PIT']
TIME_TO_SOLVE = 300

# first letters and longest length of places are needed for menu display.
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LEGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LEGTH:
        LONGEST_PLACE_NAME_LEGTH = len(place)

# basic sanity checks of the constants.
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# first letters must be unique.
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)


knowSuspectsAndItem = []
# visitedPlaced: Keys = places, values = strings of the suspect & item there.
visitedPlaces = {}
currentLocation = 'TAXI'
accusedSuspects = []
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3
culprit = random.choice(SUSPECTS)

# common indexed link these; e.g. SUSPECTS[0] and ITEM[0] are at PLACES[0].
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# create data structures for clues the truth-tellers give about each
# item and suspect.
# clues: keys=suspects being asked for a clue, value="clue dictionary".
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue
    # This "clue dictionary" has keys=items & suspects,
    # value=the clue given.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:
            # tells who has the item
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]

    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:
            # tell what item the suspect has
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

# create data structures for clues the liars give about each item
# and suspect.
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue

    # this "clue dictionary" has keys=items & suspects.
    # value= the clue given
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True

    # this interviewee is a liar and gives wrong clues.
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:
                # lies about where the item is
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    # break out of the loop when wrong clue is selected.
                    break

        else:
            while True:
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    # break out of the loop when wrong clue is selected
                    break
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    # break out of the loop when wrong clue is selected.
                    break
        else:
            while True:
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    # break out of the loop when wrong clue is selected.
                    break

# create the data structures for clues given when asked about Zophie.
zophieClues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kindOfClue = random.randint(1, 3)
    if kindOfClue == 1:
        if interviewee not in liars:
            # they tell you who has Zophie.
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                # select a (wrong) suspect clue.
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                    # break out of the loop when wrong clue is selected.
                    break

    elif kindOfClue == 2:
        if interviewee not in liars:
            # thry tell you where Zophie is.
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # select a (wrong) place clue.
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    # break out of the loop when wrong clue is selected.
                    break
    elif kindOfClue == 3:
        if interviewee not in liars:
            # they tell you what item Zophie is near.
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # select a (wrong) item clue.
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    # break out of the loop when wrong clue is selected.
                    break

# EXPERIMENT: uncomment this code to view the clue structures.
# import pprint
#pprint.pprint(clues)
#pprint.pprint(zophieClues)
#print('culprit =', culprit)

# start of the game
print("""
      J'ACCUSE! (a mystery game)")
      By Al Sweigart al@inventwithpython.com
      Inspired by Homestar Runner\'s "Where\'s an Egg?" game

      You are the world-famous detective Mathilde Camus.
      ZOPHIE THE CAT has gone missing, and you must sift through the clues.
      Suspects either always tell lies, or always tell the truth. Ask them
      about other people, places, and items to see if the details they give are
      truthful and consistent with your observations. Then you will know if
      their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
      CAT in time and accuse the guilty party?
      """)
input('Press Enter to begin...')


startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

while True:
    if time.time() > endTime or accusationsLeft == 0:
        # handle "game over" condition.
        if time.time() > endTime:
            print('You have run out of time!')
        elif accusationsLeft == 0:
            print('You have accused too many innocent people!')
        culpritIndex = SUSPECTS.index(culprit)
        print('It was {} at the {} with the {} who catnapped her!'.format(culprit,
                                                                         PLACES[culpritIndex], ITEMS[culpritIndex]))
        print('Better luck next time, Detective.')
        sys.exit()

    print()
    minutesLeft = int(endTime - time.time()) // 60
    secondsLeft = int(endTime - time.time()) % 60

    if currentLocation == 'TAXI':
        print('  You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            placeInfo = ''
            if place in visitedPlaces:
                placeInfo = visitedPlaces[place]
            nameLabel = '(' + place[0] + ')' + place[1:]
            spaceing = " " * (LONGEST_PLACE_NAME_LEGTH - len(place))
            print('{} {}{}'.format(nameLabel, spaceing, placeInfo))
        print('(Q)UIT GAME')
        while True:
            response = input('> ').upper()
            if response == '':
                continue
            if response == 'Q':
                print('Thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTERS[response]
        continue

    # at a place. player can ask for clues.
    print('  You are at the {}.'.format(currentLocation))
    currentLocationIndex = PLACES.index(currentLocation)
    thePersonHere = SUSPECTS[currentLocationIndex]
    theItemHere = ITEMS[currentLocationIndex]
    print('  {} with the {} is here.'.format(thePersonHere, theItemHere))

    # add the suspect and item at this place to our list of known.
    # suspects and items
    if thePersonHere not in knowSuspectsAndItem:
        knowSuspectsAndItem.append(thePersonHere)
    if ITEMS[currentLocationIndex] not in knowSuspectsAndItem:
        knowSuspectsAndItem.append(ITEMS[currentLocationIndex])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = '({}, {})'.format(thePersonHere.lower(),
                                                          theItemHere.lower())

    # if the player has accused this person wrongly before. they
    # won't give clues.
    if thePersonHere in accusedSuspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')
        currentLocation = 'TAXI'
        continue

    # display menu of known suspects & items to ask about/
    print()
    print('(J) "J\'ACCUSE!" ({} accusations left)'.format(accusationsLeft))
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspectOrItem in enumerate(knowSuspectsAndItem):
        print('({}) Ask about {}'.format(i + 1, suspectOrItem))

    while True:
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response) <=
                                 len(knowSuspectsAndItem)):
            break

    if response == 'J':
        accusationsLeft -= 1
        if thePersonHere == culprit:
            # You've accused the correct suspect.
            print('You\'ve cracked the case, Detective!')
            print('It was {} who had catnapped ZOPHIE THE CAT.'.format(culprit))
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken = int(time.time() - startTime) % 60
            print('Good job! You solved it in {} min, {} sec.'.format(minutesTaken,
                                                                     secondsTaken))
            sys.exit()

        else:
            # You've accused the wrong suspect.
            accusedSuspects.append(thePersonHere)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to yout TAXI.')
            currentLocation = 'TAXI'
    elif response == 'Z':
        if thePersonHere not in zophieClues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif thePersonHere in zophieClues:
            print('   They give you this clue: "{}"'.format(zophieClues[thePersonHere]))
            # add non-place clues to the list of know things.
            if zophieClues[thePersonHere] not in knowSuspectsAndItem and zophieClues[thePersonHere] not in PLACES:
                knowSuspectsAndItem.append(zophieClues[thePersonHere])

    elif response == 'T':
        currentLocation = 'TAXI'
        continue

    else:
        thingBeingAskAbout = knowSuspectsAndItem[int(response) - 1]
        if thingBeingAskAbout in (thePersonHere, theItemHere):
            print('  They give you this clue: "No comment."')
        else:
            print('  They give you this clue:\
                  "{}"'.format(clues[thePersonHere][thingBeingAskAbout]))
            # add non-place clues to the list of know things.
            if clues[thePersonHere][thingBeingAskAbout] not in knowSuspectsAndItem and clues[thePersonHere][thingBeingAskAbout] not in PLACES:
                knowSuspectsAndItem.append(clues[thePersonHere][thingBeingAskAbout])

    input('Press Enter to continue...')

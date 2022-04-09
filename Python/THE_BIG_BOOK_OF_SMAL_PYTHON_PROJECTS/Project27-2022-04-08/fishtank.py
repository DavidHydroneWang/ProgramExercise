#!/usr/bin/env python
# coding=utf-8
"""
Fish Tank, by Al Sweigart al@inventwithpython.com
A peaceful animation of a fish tank. Press Ctrl-C to stop.
Similar to ASCIIQuarium or @EmojiAquarium, but mine is based on an
older ASCII fish tank program for DOS.assert
https://robobunny.com/projects/asciiquarium/html/
https://twitter.com/EmojiAquarium
View this code at https://nostarch.com/big-book-small-python-projects
Tags: extra-large, artistic, bext
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()


# set up the constants.
WIDTH, HEIGHT = bext.size()

WIDTH -= 1

NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 1
FRAMES_PER_SECOND = 4

# note: every string in a fish dictionary should be the same length.
FISH_TYPES = [
  {'right': ['><>'],          'left': ['<><']},
  {'right': ['>||>'],         'left': ['<||<']},
  {'right': ['>))>'],         'left': ['<[[<']},
  {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
  {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
  {'right': ['>-==>'],        'left': ['<==-<']},
  {'right': [r'>\\>'],        'left': ['<//<']},
  {'right': ['><)))*>'],      'left': ['<*(((><']},
  {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
  {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
  {'right': ['><XXX*>'],      'left': ['<*XXX><']},
  {'right': ['_.-._.-^=>', '.-._.-.^=>',
             '-._.-._^=>', '._.-._.^=>'],
   'left':  ['<=^-._.-._', '<=^.-._.-.',
             '<=^_.-._.-', '<=^._.-._.']},
  ]  # (!) Try adding your own fish to FISH_TYPES.
LONGEST_FISH_LENGTH = 10  # Longest single string in FISH_TYPES.

# the x and y positions where a fish runs into the edge of the screen.
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # generate the global variables.
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # note: Bubbles are drawn, but not the bubblers themselves.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # each bubbler starts at a random position.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # generate each segment of the kelp.
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # run the simulation.
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1


def getRandomColor():
    """
    return a string of a random color.
    """
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))


def generateFish():
    """
    return a dictionary thar represents a fish.
    """
    fishType = random.choice(FISH_TYPES)

    # set up colors for each character in the fish text.
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random':  # All parts are randomly colored.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength
    if colorPattern == 'head-tail':
        headTailColor = getRandomColor()
        colors[0] = headTailColor
        colors[-1] = headTailColor

    # set up the rest of fish data structures.
    fish = {'right':            fishType['right'],
            'left':             fishType['left'],
            'colors':           colors,
            'hSpeed':           random.randint(1, 6),
            'vSpeed':           random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight':       random.choice([True, False]),
            'goingDown':        random.choice([True, False])}

    # 'x' is always the leftmost side of the fish body.
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    """
    Simulate the movements in the aquarium for one step.
    """
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Simulate the fish for one step:
    for fish in FISHES:
        # move the fish horizontally.
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1  # Move the fish right.
                else:
                    fish['goingRight'] = False  # Turn the fish around.
                    fish['colors'].reverse()  # Turn the colors around.
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1  # Move the fish left.
                else:
                    fish['goingRight'] = True  # Turn the fish around.
                    fish['colors'].reverse()  # Turn the colors around.

        # fish can randomly change their horizontal diection.
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10, 60)
            # turn the fish around.
            fish['goingRight'] = not fish['goingRight']

        # move the fish vertically.
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1  # Move the fish down.
                else:
                    fish['goingDown'] = False  # Turn the fish around.
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1  # Move the fish up.
                else:
                    fish['goingDown'] = True  # Turn the fish around.

        # fish can randomly change their vertical direction.
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] = random.randint(2, 20)
            # turn the fish aroud.
            fish['goingDown'] = not fish['goingDown']

    # generate bubbles from bubblers.
    for bubbler in BUBBLERS:
        # there is a 1 in 5 chance of making a bubble.
        if random.randint(1, 5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    # move the bubbles.
    for bubble in BUBBLES:
        diceRoll = random.randint(1, 6)
        if (diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1  # Bubble goes left.
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1  # Bubble goes right.

        bubble['y'] -= 1  # The bubble always goes up.

    # iterate over BUBBLES in reverse because I'm deleting from BUBBLES
    # while iterating over it
    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:  # Delete bubbles that reach the top.
            del BUBBLES[i]

    # simulate the kelp waving for one step.
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # 1 in 20 chance to change waving.
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    """
    draw the aquarium on the screen
    """
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # draw quit message.
    bext.fg('white')
    bext.goto(0, 0)
    print('Fish Tank, by Al Sweigart  Ctrl-C to quit.', end='')
    # draw the bubbles.
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')

    # draw the fish.
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # get the correct right or left-facing fish text.
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]

        # draw each character of the fish text in the right color.
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    # draw the kelp
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end='')

    # draw the send on the bottom.
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')  # Draws '░' characters.

    sys.stdout.flush()  # (Required for bext-using programs.)


def clearAquarium():
    """
    draw empty spaces over everything on the screen.
    """
    global FISHES, BUBBLERS, BUBBLES, KELP

    # draw the bubbles.
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    # draw the fish.
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # draw each character of the fish text in the right color.
        print(' ' * len(fish['left'][0]), end='')

    # draw the kelp.
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print('  ', end='')

    sys.stdout.flush()


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

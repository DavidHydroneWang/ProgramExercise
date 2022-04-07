#!/usr/bin/env python
# coding=utf-8
"""
Duckling Screensaver, by Al Sweigart al@inventwithpython.com
A screensaver of many many ducklings.
>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, object-oriented, scrolling
"""

import random, shutil, sys, time

# set up the constants.
PAUSE = 0.2  # (!)try changing this to 1.0 or 0.0.
DENSITY = 0.10  # (!) try changing this to anything from 0.0 to 1.0.

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# get the size of the terminal window.
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1


def main():
    print('Duckling Screensaver, by Al Sweigart')
    print('Press Ctrl-C to quit...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # see if we should create a duckling in this lane.
            if (ducklingObj is None and random.random() <= DENSITY):
                # place a duckling in this lane.
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj

            if ducklingObj is not None:
                # draw a duckling if there is one in this lane.
                print(ducklingObj.getNextBodyPart(), end='')
                # delete the duckling if we've finished drawing it.
                if ducklingObj.partToDisplayNext is None:
                    ducklingLanes[laneNum] = None
            else:
                # draw five spaces since there is no duckling on the screen.
                print(' ' * DUCKLING_WIDTH, end='')

        print()
        sys.stdout.flush()  # make sure text appears on the screen.
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """ create a new duckling with random body features. """
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # chubbt duckling can only have beady eyes.
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        """return the string of the duckling's head"""
        headStr = ''
        if self.direction == LEFT:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '

        if self.direction == RIGHT:
            headStr += ' ('

            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            headStr += ' '
        return headStr

    def getBodyStr(self):
        """return the string of the duckling's body"""
        bodyStr = '('
        if self.direction == LEFT:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'

        if self.body == CHUBBY:
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        """return the string of the duckling's feet"""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """calls the appropriate display method for the next body"""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

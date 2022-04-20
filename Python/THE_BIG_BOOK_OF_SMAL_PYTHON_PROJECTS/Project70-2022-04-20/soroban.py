#!/usr/bin/env python
# coding=utf-8
"""
Soroban Japanese Abacus, by Al Sweigart al@inventwithpython.com
A simulation of a Japanese abacus calculator tool.
More info at: https://en.wikipedia.org/wiki/Soroban
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, math, simulation
"""

NUMBER_OF_DIGITS = 10


def main():
    print('Soroban - The Chinese Abacus')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    abacusNumber = 0
    while True:
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'quit':
            break
        elif commands.isdecimal():
            abacusNumber = int(commands)
        else:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1
        # the abacus can't show negative numbers
        if abacusNumber < 0:
            abacusNumber = 0
        # the abacus can't show numbers larger than 9999999999.
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999


def displayAbacus(number):
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

    hasBeads = []
    # top heaven row has a bead for digits 0, 1, 2, 3, 4
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '01234')

    # bottom heaven row has a bead for digits 5, 6, 7, 8, 9.
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '56789')

    # 1st (topmost) earth row has a bead for all digits except 0
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '123456789')

    # 2nd earth row has a bead for digits 2, 3, 4, 5, 6, 7, 8, 9
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '234789')

    # 3rd earth row has a bead for digits 0, 3, 4, 5, 8, 9
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '034589')

    # 4th earth row has a bead for digits 0, 1, 2, 4, 5, 6, 9
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '014569')

    # 5th earth row has a bead for digits 0, 1, 2, 5, 6, 7
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '012567')

    # 6th earth row has a bead for digits 0, 1, 2, 3, 5, 6, 7, 8
    for i in range(NUMBER_OF_DIGITS):
        hasBeads.append(numberList[i] in '01235678')

    # convert these True or False values into 0 or | characters.
    abacusChar = []
    for i, beadPresent in enumerate(hasBeads):
        if beadPresent:
            abacusChar.append('0')
        else:
            abacusChar.append('|')

    # draw the abacus with the 0/| characters.
    chars = abacusChar + numberList
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+
          """.format(*chars))


def displayControls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


if __name__ == '__main__':
    main()

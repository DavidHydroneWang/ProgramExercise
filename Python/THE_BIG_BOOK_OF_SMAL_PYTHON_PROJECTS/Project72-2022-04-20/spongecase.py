#!/usr/bin/env python
# coding=utf-8
"""
sPoNgEcAsE, by Al Sweigart al@inventwithpython.com
Translates English messages into sPOnGEtExT.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, word
"""

import random

try:
    import pyperclip
except ImportError:
    pass


def main():
    """run the Spongetext program"""
    print('''
          sPoNgEcAsE, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

          eNtEr YoUr MeSsAgE:
          ''')
    spongeText = englishToSpongecase(input('> '))
    print()
    print(spongeText)

    try:
        pyperclip.copy(spongeText)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass


def englishToSpongecase(message):
    """return the spongeText form of the given string."""
    spongeText = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongeText += character
            continue

        if useUpper:
            spongeText += character.upper()
        else:
            spongeText += character.lower()

        # flip the case, 90% of the time
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper
    return spongeText


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    main()

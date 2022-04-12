#!/usr/bin/env python
# coding=utf-8
"""
Leetspeak, by Al Sweigart al@inventwithpython.com
Translates English messages into l33t5p34]<.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, word
"""

import random

try:
    import pyperclip
except ImportError:
    pass


def main():
    print('''
          L3375P34]< (leetspeek)
          By Al Sweigart al@inventwithpython.com

          Enter your leet message:
          ''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        # try to use pyperclip will raise a NameError exception if
        # it wasn't imported.
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass


def englishToLeetspeak(message):
    """
    Convert the English string in message and return leetspeak.
    """
    # make sure all the keys in 'charMapping' are lowercase.
    charMapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']
    }
    leetspeak = ''
    for char in message:
        # there is a 70% chance we change the character to leetspeak.
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # don't traslation this character.
            leetspeak = leetspeak + char
    return leetspeak


# if this program was run (instead of imported), run the game.
if __name__ == '__main__':
    main()

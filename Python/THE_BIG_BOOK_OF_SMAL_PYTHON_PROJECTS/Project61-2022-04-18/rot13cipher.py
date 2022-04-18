#!/usr/bin/env python
# coding=utf-8
"""
ROT13 Cipher, by Al Sweigart al@inventwithpython.com
The simplest shift cipher for encrypting and decrypting text.
More info at https://en.wikipedia.org/wiki/ROT13
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, cryptography
"""

try:
    import pyperclip
except ImportError:
    pass

# set up the constants.
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT12 Cipher, by Al Sweigart al@inventwithpython.com')
print()

while True:
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break

    # rotate the letters in message by 13 character.
    translated = ''
    for character in message:
        if character.isupper():
            # contain uppercase translated character.
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # contain lowercase translated character.
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # contain the character untranslated.
            translated += character

    # display the translation.
    print('The translated message is:')
    print(translated)
    print()

    try:
        # copy the translation to the clipboard.
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass

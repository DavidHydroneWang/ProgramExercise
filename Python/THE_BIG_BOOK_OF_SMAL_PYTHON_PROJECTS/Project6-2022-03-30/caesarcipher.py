#!/usr/bin/env python
# coding=utf-8
"""
Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math
"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # if pyperclip is not installed, do nothing. it's no big deal.

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
while True:
    # keeping asking until the user enter e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    reponse = input('> ').lower()
    if reponse.startswith('e'):
        mode = 'encrypt'
        break
    elif reponse.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let user enter the key to use.
while True:
    # Keep asking until the users enter a valid key.
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use'.format(maxKey))
    reponse = input('> ').upper()
    if not reponse.isdecimal:
        continue

    if 0 <= int(reponse) < len(SYMBOLS):
        key = int(reponse)
        break

# Let the user enter the message to encrypt/decrypt.
print('Enter the message to {}.'.format(mode))
message = input('> ')

# Cesar cipher only works on uppercase letters.
message = message.upper()

# Store the encrypted/decrypted form of the message.
translate = ''

# Encrypted/decrypt each symbol in the message.
for symbol in message:
    if symbol in SYMBOLS:
        # get the encrypted(or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # Handle the wrap-around if num is larger than the length of
        # SYMBOLS or less than 0.
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted number's symbol to translate.
        translate = translate + SYMBOLS[num]
    else:
        # just add the symbol without encrypting/decrypting.
        translate = translate + symbol

# display the encrypted/decryptrf string to the screen
print(translate)

try:
    pyperclip.copy(translate)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass  # Do nothing if pyperclip wasn't installed.
